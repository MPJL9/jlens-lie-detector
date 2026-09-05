#!/usr/bin/env python3
"""Stage 3 — apply the J-lens and the logit lens to the cached activations
and export viewer-ready JSON (plan §7, §12, §13).

For every cached sequence, at every layer l and position t:
    z_J  = unembed( J_l @ h_{l,t} )       (J-lens; identity at the final layer)
    z_LL = unembed( h_{l,t} )             (logit lens — mandatory baseline)
and the Yes-vs-No score
    s = logsumexp_{y in YES} z_y  -  logsumexp_{n in NO} z_n
with the Yes/No single-token sets fixed by stage 2 (runs/<slug>/meta.json).

Output: exports/<slug>/<seq_id>.json  +  exports/<slug>/manifest.json

  {
    "seq_id","fact_id","condition","format","self_q","user_prompt","response",
    "answer","answer_text","answer_label","model_yes_minus_no",
    "layers": [0..n-1], "top_k": K,
    "tokens": [...], "segments": [{"name","start","end"}],
    "P0": int, "P1": [start,end], "P2": int, "P3": int|null,
    "vocab": {"<id>": "string"},
    "scores": {"J": [layer][pos] float, "LL": [layer][pos] float},
    "readout": {"J": [layer][pos] -> [[id,prob]*K], "LL": same}
  }

Both lenses read exactly the same activations (plan §12). The unembedding is
the model's own final norm + LM head (via jlens), so the J-lens logits are
scale-invariant in J and no norm-equalisation is needed.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (MODELS, gpu_sanity, load_lens, load_model, logger,  # noqa: E402
                    model_slug, read_jsonl, setup_logging)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="gemma-3-4b-it", choices=sorted(MODELS))
    ap.add_argument("--tag", default="", help="suffix for runs/exports dirs: <slug>__<tag>")
    ap.add_argument("--top-k", type=int, default=12)
    ap.add_argument("--layer-stride", type=int, default=1)
    ap.add_argument("--device", default=None)
    ap.add_argument("--out", default=None, help="default exports/<slug>")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    setup_logging()
    gpu_sanity()

    slug = model_slug(args.model) + (f"__{args.tag}" if args.tag else "")
    run = f"runs/{slug}"
    out = args.out or f"exports/{slug}"
    os.makedirs(out, exist_ok=True)
    meta = json.load(open(f"{run}/meta.json"))
    rows = read_jsonl(f"{run}/sequences.jsonl")
    if args.limit:
        rows = rows[:args.limit]

    L = load_model(args.model, args.device)
    lens = load_lens(args.model)
    n_layers = L.n_layers
    final = n_layers - 1
    # cache_layers: layer subset stored by stage 2 (campaign 2); None = all
    cached = meta.get("cache_layers") or list(range(n_layers))
    layers = sorted((set(range(0, n_layers, args.layer_stride)) | {final}) & set(cached))
    for l in layers:
        assert l == final or l in lens.jacobians, f"layer {l} not in lens"
    yes_ids = sorted(meta["yes_tokens"].values())
    no_ids = sorted(meta["no_tokens"].values())
    K = args.top_k
    tok = L.tokenizer
    dev = L.device

    # J on device in fp32, one layer at a time would re-upload per item; the
    # whole stack is n_layers*d^2*4 B (gemma-3-4b: ~0.9 GB) — keep it resident.
    J = {l: lens.jacobians[l].to(dev, torch.float32) for l in layers if l != final}

    manifest = dict(model=args.model, hf=L.spec["hf"], slug=slug, layers=layers,
                    top_k=K, lenses=["LL", "J"], yes_tokens=meta["yes_tokens"],
                    no_tokens=meta["no_tokens"], formats=sorted({r["format"] for r in rows}),
                    items=[])
    t_all = time.perf_counter()
    for r in rows:
        t0 = time.perf_counter()
        blob = torch.load(f"{run}/cache/{r['seq_id']}.pt")
        acts = blob["acts"]                       # [n_cached_layers, T-crop, d] bf16 cpu
        blob_layers = blob.get("layers") or list(range(acts.shape[0]))
        lrow = {l: i for i, l in enumerate(blob_layers)}
        crop = blob.get("crop_start", 0)
        T = acts.shape[1]
        scores = {"J": [], "LL": []}
        readout = {"J": [], "LL": []}
        vocab_ids = set()
        with torch.no_grad():
            for l in layers:
                h = acts[lrow[l]].to(dev, torch.float32)       # [T, d]
                for name in ("LL", "J"):
                    hh = h if (name == "LL" or l == final) else h @ J[l].T
                    z = L.lens_model.unembed(hh).float()         # [T, V]
                    lse = torch.logsumexp(z, -1, keepdim=True)
                    s = (torch.logsumexp(z[:, yes_ids], -1) - torch.logsumexp(z[:, no_ids], -1))
                    vals, idx = z.topk(K, -1)
                    probs = (vals - lse).exp().cpu()
                    idx = idx.cpu()
                    fin = lambda v, d: round(float(v), d) if math.isfinite(v) else None
                    scores[name].append([fin(v, 4) for v in s.cpu()])
                    readout[name].append([[[int(idx[t, j]), fin(probs[t, j], 5)]
                                           for j in range(K)] for t in range(T)])
                    vocab_ids.update(idx.flatten().tolist())
                    del z
        item = {k: r.get(k) for k in ("seq_id", "fact_id", "condition", "format", "self_q",
                                      "user_prompt", "response", "answer", "answer_text",
                                      "answer_label", "model_yes_minus_no", "arm")}
        # crop-aware position bookkeeping: exported arrays start at `crop`, so
        # tokens/segments/P* are shifted into the cropped frame; orig_T keeps
        # the full sequence length for the length-confound gate (stage 4).
        shift = lambda p: (p - crop) if (p is not None and p >= crop) else None
        segments = []
        for s in r["segments"]:
            if s["end"] <= crop:
                continue
            segments.append({"name": s["name"], "start": max(s["start"] - crop, 0),
                             "end": s["end"] - crop})
        item.update(tokens=r["tokens"][crop:], segments=segments,
                    P0=shift(r.get("P0")),
                    P1=[max(r["P1"][0] - crop, 0), r["P1"][1] - crop] if r.get("P1") else None,
                    P2=shift(r["P2"]), P3=shift(r.get("P3")),
                    crop_start=crop, orig_T=r["T"],
                    layers=layers, top_k=K,
                    vocab={str(i): tok.decode([i]) for i in sorted(vocab_ids)},
                    scores=scores, readout=readout)
        with open(f"{out}/{r['seq_id']}.json", "w") as f:
            json.dump(item, f, ensure_ascii=False)
        manifest["items"].append({k: r[k] for k in ("seq_id", "fact_id", "condition", "format",
                                                   "answer_label", "model_yes_minus_no",
                                                   "T", "P0", "P2", "P3")})
        logger.info("%-45s T=%3d %.1fs", r["seq_id"], T, time.perf_counter() - t0)
    json.dump(manifest, open(f"{out}/manifest.json", "w"), indent=1)
    # viewer model list: every sibling export dir that has a manifest
    root = os.path.dirname(os.path.abspath(out))
    idx = sorted(d for d in os.listdir(root)
                 if os.path.exists(os.path.join(root, d, "manifest.json")))
    json.dump(idx, open(os.path.join(root, "index.json"), "w"))
    print(f"READOUT DONE: {len(rows)} items -> {out}/  ({time.perf_counter() - t_all:.0f}s)")


if __name__ == "__main__":
    main()
