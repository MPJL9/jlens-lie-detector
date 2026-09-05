#!/usr/bin/env python3
"""Stage 2 — build self-report sequences and cache residual activations
(plan §6, §12).

For every kept transcript and every self-report format:
  * render  [user prompt][response][self-report question] + generation prompt;
  * greedy-generate the model's answer (a few tokens) so the DYL-style P3
    position (the generated Yes/No token) exists;
  * run ONE forward pass over prompt + generated answer and record the
    residual stream after EVERY block at EVERY position;
  * save runs/<slug>/cache/<seq_id>.pt  {acts: bf16 [n_layers, T, d], ids}
    and append a row to runs/<slug>/sequences.jsonl with the segment spans and
    the positions P0 / P1 / P2 / P3.

Positions (plan §6, §10):
  P0 = last token of the original response (before any self-report question)
  P1 = every token of the self-report question  [start, end)
  P2 = last prompt token (generation-prompt end: the model has read the
       question and is about to answer) -- the next-token logits here ARE the
       model's actual Yes/No self-report
  P3 = the generated Yes/No answer token (None if the model answered otherwise)

Campaign-2 additions:
  * prefilled-assistant formats (prompts.PREFILL_FORMATS): the assistant turn
    is started with a fixed prefill text; a `prefill` segment is recorded and
    P2 = the last prefill token. `self_q=None` (B1_prefill) drops the
    self-report turn entirely (and the original response), prefilling the
    RESPONSE turn instead; P0/P1 are then None.
  * --variant-formats / --variant-scenarios: extra formats run only for
    transcripts whose fact_id is in the given JSON id list.
  * --cache-layers "0,14-47": store only these layers (plus the final layer,
    always, for the model_yes_minus_no logits); --crop-from-segment
    user_prompt stores only positions from that segment's last token onward.
    Cropping metadata ({layers, crop_start}) is saved in the blob and consumed
    by stage 3.
  * --append: merge new rows into an existing sequences.jsonl (by seq_id)
    instead of overwriting it.

The model's own Yes/No logits at P2 are saved too (baseline 1, plan §13).
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jlens.hooks import ActivationRecorder  # noqa: E402

from common import (MODELS, build_followup, classify_answer, generate,  # noqa: E402
                    gpu_sanity, load_model, logger, model_slug, read_jsonl,
                    render_chat, seg, setup_logging, tokenize_with_offsets,
                    write_jsonl, yes_no_sets)
from prompts import (DEFAULT_FORMATS, FORMAT_ANSWER_STYLE, FORMAT_ANSWER_TOKENS,  # noqa: E402
                     INVERSION_FORMATS, PREFILL_FORMATS, SELF_REPORT_FORMATS)

ALL_FORMATS = sorted(set(SELF_REPORT_FORMATS) | set(PREFILL_FORMATS))


def parse_layers(spec: str | None, n_layers: int) -> list[int]:
    """'0,14-47' -> [0,14,...,47]; None/'all' -> every layer. Final layer is
    always included (needed for the P2 Yes/No logits)."""
    if not spec or spec == "all":
        return list(range(n_layers))
    out = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    out.add(n_layers - 1)
    bad = [l for l in out if not 0 <= l < n_layers]
    assert not bad, f"--cache-layers out of range: {bad}"
    return sorted(out)


def build_prefill_seq(L, t: dict, self_q: str | None, prefill: str):
    """Sequence for a prefilled-assistant format. With self_q: the normal
    followup prompt, then the assistant turn starts with `prefill`. Without
    self_q: [system][user] + generation prompt + `prefill` (the prefill
    replaces the model's response to the pressure prompt)."""
    if self_q is not None:
        sq = build_followup(L, t["user_prompt"], t["response"], self_q,
                            system=t.get("system"))
    else:
        msgs = ([{"role": "system", "content": t["system"]}] if t.get("system") else []) + \
               [{"role": "user", "content": t["user_prompt"]}]
        text = render_chat(L, msgs, add_generation_prompt=True)
        sq = tokenize_with_offsets(L, text)
        cursor = 0
        parts = ([("system", t["system"])] if t.get("system") else []) + \
                [("user_prompt", t["user_prompt"])]
        for name, content in parts:
            c = content.strip()
            cs = text.find(c, cursor)
            if cs < 0:
                raise ValueError(f"could not locate {name!r} in rendered chat text")
            ce = cs + len(c)
            ts, te = sq.span_tokens(cs, ce)
            sq.segments.append({"name": name, "start": ts, "end": te})
            cursor = ce
        sq.segments.append({"name": "gen_prompt",
                            "start": sq.segments[-1]["end"], "end": len(sq.ids)})
    p_ids = L.tokenizer.encode(prefill, add_special_tokens=False)
    start = len(sq.ids)
    sq.ids = sq.ids + p_ids
    sq.segments.append({"name": "prefill", "start": start, "end": len(sq.ids)})
    return sq


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="gemma-3-4b-it", choices=sorted(MODELS))
    ap.add_argument("--tag", default="", help="suffix for runs/exports dirs: <slug>__<tag>")
    ap.add_argument("--transcripts", default=None)
    ap.add_argument("--formats", nargs="+", default=DEFAULT_FORMATS,
                    choices=ALL_FORMATS + ["none"],
                    help="'none' = no main formats (e.g. an --append job adding "
                         "only variant formats)")
    ap.add_argument("--variant-formats", nargs="*", default=[], choices=ALL_FORMATS,
                    help="extra formats run only for --variant-scenarios fact_ids")
    ap.add_argument("--variant-scenarios", default=None,
                    help="JSON file with fact_id list; default = all transcripts")
    ap.add_argument("--inversion-formats", nargs="*", default=INVERSION_FORMATS)
    ap.add_argument("--inversion-n", type=int, default=5,
                    help="run inversion formats on the first N kept facts (x2 conditions)")
    ap.add_argument("--answer-tokens", type=int, default=8)
    ap.add_argument("--cache-layers", default=None,
                    help="layer spec to cache, e.g. '0,14-47'; default all")
    ap.add_argument("--crop-from-segment", default=None,
                    help="cache positions only from this segment's LAST token on, e.g. user_prompt")
    ap.add_argument("--append", action="store_true",
                    help="merge rows into an existing sequences.jsonl instead of overwriting")
    ap.add_argument("--device", default=None)
    ap.add_argument("--include-unkept", action="store_true")
    args = ap.parse_args()
    setup_logging()
    gpu_sanity()
    if args.formats == ["none"]:
        args.formats = []

    for f in args.formats + args.variant_formats:
        if f in PREFILL_FORMATS and PREFILL_FORMATS[f]["prefill"] is None:
            sys.exit(f"FATAL: format {f} has no frozen prefill yet "
                     f"(derive it from the R_open pilot, set it in prompts.PREFILL_FORMATS)")

    slug = model_slug(args.model) + (f"__{args.tag}" if args.tag else "")
    run = f"runs/{slug}"
    tr_path = args.transcripts or f"{run}/transcripts.jsonl"
    cache_dir = f"{run}/cache"
    os.makedirs(cache_dir, exist_ok=True)

    L = load_model(args.model, args.device)
    tok = L.tokenizer
    yn = yes_no_sets(tok)
    yes_ids, no_ids = set(yn["yes"].values()), set(yn["no"].values())
    logger.info("yes tokens %s | no tokens %s", yn["yes"], yn["no"])

    cache_layers = parse_layers(args.cache_layers, L.n_layers)
    variant_ids = set(json.load(open(args.variant_scenarios))) \
        if args.variant_scenarios else None

    transcripts = [t for t in read_jsonl(tr_path) if t["keep"] or args.include_unkept]
    kept_facts = []
    for t in transcripts:
        if t["fact_id"] not in kept_facts:
            kept_facts.append(t["fact_id"])
    inv_facts = set(kept_facts[:args.inversion_n])

    rows = []
    for t in transcripts:
        fmts = list(args.formats)
        if args.variant_formats and (variant_ids is None or t["fact_id"] in variant_ids):
            fmts += [f for f in args.variant_formats if f not in fmts]
        if t["fact_id"] in inv_facts:
            fmts += list(args.inversion_formats)
        for fmt in fmts:
            if fmt in PREFILL_FORMATS:
                cfg = PREFILL_FORMATS[fmt]
                self_q = cfg["self_q"]
                sq = build_prefill_seq(L, t, self_q, cfg["prefill"])
                n_answer = cfg["answer_tokens"]
            else:
                self_q = SELF_REPORT_FORMATS[fmt]
                sq = build_followup(L, t["user_prompt"], t["response"], self_q,
                                    system=t.get("system"))
                n_answer = FORMAT_ANSWER_TOKENS.get(fmt, args.answer_tokens)
            prompt_ids = sq.ids
            new = generate(L, prompt_ids, n_answer)
            answer_text = tok.decode(new, skip_special_tokens=True)
            p3 = next((len(prompt_ids) + i for i, tid in enumerate(new)
                       if tid in yes_ids or tid in no_ids), None)
            ids = prompt_ids + new
            with torch.no_grad(), ActivationRecorder(L.lens_model.layers, at=cache_layers) as rec:
                L.lens_model.forward(torch.tensor([ids], device=L.device))
                p2 = len(prompt_ids) - 1
                final = rec.activations[cache_layers[-1]][0].detach()
                z = L.lens_model.unembed(final[p2:p2 + 1]).float()[0].cpu()
                crop_start = 0
                if args.crop_from_segment:
                    crop_start = seg(sq, args.crop_from_segment)["end"] - 1
                acts = torch.stack(
                    [rec.activations[l][0, crop_start:].detach().to(torch.bfloat16).cpu()   # bf16: fp16 overflows on Gemma's late-layer residuals
                     for l in cache_layers])        # [n_cache_layers, T-crop, d]
            lse_y = torch.logsumexp(z[sorted(yes_ids)], 0).item()
            lse_n = torch.logsumexp(z[sorted(no_ids)], 0).item()

            seq_id = f"{t['fact_id']}__{t['condition']}__{fmt}"
            torch.save({"acts": acts, "ids": ids, "layers": cache_layers,
                        "crop_start": crop_start}, f"{cache_dir}/{seq_id}.pt")
            has_resp = any(s["name"] == "response" for s in sq.segments)
            segments = sq.segments + [{"name": "answer", "start": len(prompt_ids), "end": len(ids)}]
            row = dict(
                seq_id=seq_id, fact_id=t["fact_id"], condition=t["condition"],
                format=fmt, self_q=self_q, user_prompt=t["user_prompt"],
                response=t["response"], answer=t["answer"], arm=t.get("arm"),
                answer_text=answer_text,
                answer_label=classify_answer(answer_text, FORMAT_ANSWER_STYLE.get(fmt, "yesno")),
                model_yes_minus_no=lse_y - lse_n,
                T=len(ids), n_prompt=len(prompt_ids),
                tokens=[tok.decode([i]) for i in ids], ids=ids,
                segments=segments,
                P0=seg(sq, "response")["end"] - 1 if has_resp else None,
                P1=[seg(sq, "self_q")["start"], seg(sq, "self_q")["end"]]
                   if any(s["name"] == "self_q" for s in sq.segments) else None,
                P2=p2, P3=p3,
            )
            rows.append(row)
            logger.info("%-45s T=%3d P0=%s P1=%s P2=%d P3=%s ans=%r (%.2f)",
                        seq_id, len(ids), row["P0"], row["P1"], p2, p3,
                        answer_text[:30], lse_y - lse_n)
            del acts
            if L.device.type == "cuda":
                torch.cuda.empty_cache()

    seq_path = f"{run}/sequences.jsonl"
    if args.append and os.path.exists(seq_path):
        old = {r["seq_id"]: r for r in read_jsonl(seq_path)}
        old.update({r["seq_id"]: r for r in rows})
        rows = list(old.values())
        logger.info("append mode: merged into %d total rows", len(rows))
    meta = dict(model=args.model, hf=L.spec["hf"], n_layers=L.n_layers, d_model=L.d_model,
                yes_tokens=yn["yes"], no_tokens=yn["no"], formats=args.formats,
                variant_formats=args.variant_formats,
                cache_layers=cache_layers, crop_from_segment=args.crop_from_segment,
                inversion_formats=args.inversion_formats, inversion_n=args.inversion_n)
    write_jsonl(seq_path, rows)
    json.dump(meta, open(f"{run}/meta.json", "w"), indent=2)
    print(f"CACHE DONE: {len(rows)} sequences -> {cache_dir}/  (meta {run}/meta.json)")


if __name__ == "__main__":
    main()
