#!/usr/bin/env python3
"""Position check for the released DYL probes on AISI's OWN rollouts.

Question (results/dyl_comparison_audit.md §4.3): is the probe meant
to read the residual at the generated Yes/No token, or at the token before it
(the position whose next-token prediction is the answer)? On our caches the
probes' shipped training mean/std match the token BEFORE. This script settles
it on their data: it re-tokenizes sampled rows of their released rollouts
(huggingface ai-safety-institute/lie-detection-rollouts, staged as
data/dyl_rollouts/<config>__<split>__sample120.jsonl by the audit — 60 `lie`
+ 60 `honest` rows, seed 0), runs one forward pass per row, reads the residual
at the probe layer at BOTH positions, and reports for each: z-score RMS
(≈1 = matches the training statistics), AUROC lie vs honest, balanced
accuracy and flag rates at the shipped threshold. Compare with the checkpoint's
own validation metrics printed from sweep.json. The correct position should
reproduce those; the wrong one should not.

Their label semantics (unchanged here): `lie` = the model lied and DENIED it
when asked; `honest` = correct answer + "No" OR lie + confession "Yes";
`ambiguous` rows are excluded upstream.

Qwen note: their Qwen rollouts carry reasoning before every turn. The chat
template renders reasoning only for assistant turns after the last user
query unless preserve_thinking=True; --preserve-thinking renders the
first-turn reasoning too (unknown which they used — run both).

CLUSTER SCRIPT (needs weights + GPU; user submits; sbatch lines in
slurm/campaign2.md). Output: runs/dyl_replication/<slug>__<split>[__pt].jsonl
+ printed summary.
"""
import argparse, enum, json, os, sys, types

import torch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from common import load_model, model_slug, setup_logging, logger  # noqa: E402
from jlens.hooks import ActivationRecorder  # noqa: E402
from dyl_probe_from_cache import PROBE_DIRS, load_probe, auroc, boot_ci, fmt  # noqa: E402

CONFIGS = {"gemma-3-12b-it": "google-gemma-3-12b-it",
           "gemma-3-27b-it": "google-gemma-3-27b-it",
           "qwen3.6-27b": "qwen-qwen3.6-27b",
           "gpt-oss-20b": "openai-gpt-oss-20b"}

def render(L, messages, preserve_thinking, reasoning_effort=None, drop_thinking=False):
    kw = dict(L.spec["chat_kwargs"])
    if preserve_thinking:
        kw["preserve_thinking"] = True
    if reasoning_effort:
        kw["reasoning_effort"] = reasoning_effort
    if drop_thinking:
        # hypothesis test (gpt-oss, 2026-09-03): render the answer turn WITHOUT
        # its reasoning block, i.e. the yes/no directly after the question
        messages = [dict(m, reasoning_content=None) if m.get("role") == "assistant" else m
                    for m in messages]
    if L.spec.get("harmony"):
        # gpt-oss template takes the chain of thought as `thinking` and renders
        # it as an analysis channel (for the last assistant turn); their rows
        # store it as `reasoning_content`
        messages = [dict(m, thinking=m["reasoning_content"]) if m.get("role") == "assistant"
                    and m.get("reasoning_content") else m for m in messages]
    return L.tokenizer.apply_chat_template(messages, tokenize=False,
                                           add_generation_prompt=False, **kw)

def locate_answer(L, text, ids, offsets, content):
    """Token index of the yes/no token of the LAST assistant message."""
    c = content.strip()
    cs = text.rfind(c)
    if cs < 0:
        return None, None
    word = None
    for w in ("yes", "no"):
        if c.lower().startswith(w):
            word = w
    if word is None:
        return None, None
    ce = cs + len(word)
    idx = [i for i, (a, b) in enumerate(offsets) if b > cs and a < ce and b > a]
    if not idx:
        return None, None
    i = idx[0]
    return i, L.tokenizer.decode([ids[i]])

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True, choices=sorted(CONFIGS))
    ap.add_argument("--split", default="dyl_validate_varied_deception",
                    choices=["dyl_validate_varied_deception", "dyl_train_city_countries"])
    ap.add_argument("--preserve-thinking", action="store_true",
                    help="render reasoning_content for ALL assistant turns (Qwen)")
    ap.add_argument("--drop-thinking", action="store_true",
                    help="render assistant turns without their reasoning_content "
                         "(tests whether the probe was trained on contexts without "
                         "the reasoning block)")
    ap.add_argument("--reasoning-effort", default=None,
                    help="harmony models: override the template's reasoning level "
                         "(spec default 'low'; their rollouts' level is unknown)")
    ap.add_argument("--layers", default=None,
                    help="extra layers to score, e.g. '45,47' (default: probe layer only)")
    ap.add_argument("--device", default=None)
    ap.add_argument("--max-rows", type=int, default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    setup_logging()

    cfg = CONFIGS[args.model]
    path = os.path.join(ROOT, f"data/dyl_rollouts/{cfg}__{args.split}__sample120.jsonl")
    rows = [json.loads(l) for l in open(path)]
    if args.max_rows:
        rows = rows[:args.max_rows]
    layer, mean, std, thr, probe = load_probe(PROBE_DIRS[args.model])
    layers = [layer] + ([int(x) for x in args.layers.split(",")] if args.layers else [])
    sweep = json.load(open(os.path.join(ROOT, PROBE_DIRS[args.model], "sweep.json")))
    ref = next((s["results"] for s in sweep["sweep"] if s["safe_name"] == sweep["default_filename"]), None)
    logger.info("probe layer %d thr %.4f; their validation metrics for this checkpoint: %s", layer, thr, ref)
    L = load_model(args.model, device=args.device)

    out_rows, n_skip = [], 0
    for k, r in enumerate(rows):
        msgs = r["messages"]
        text = render(L, msgs, args.preserve_thinking, args.reasoning_effort, args.drop_thinking)
        enc = L.tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
        ids, offs = list(enc["input_ids"]), [tuple(o) for o in enc["offset_mapping"]]
        ai, atok = locate_answer(L, text, ids, offs, msgs[-1]["content"] or "")
        if ai is None or ai == 0:
            n_skip += 1
            logger.info("row %d: could not locate a yes/no answer token — skipped", r["row_index"])
            continue
        with torch.no_grad(), ActivationRecorder(L.lens_model.layers, at=layers) as rec:
            L.lens_model.forward(torch.tensor([ids], device=L.device))
            acts = {l: rec.activations[l][0].float().cpu() for l in layers}
        rec_row = dict(row_index=r["row_index"], is_lie=r["is_lie"], lie_reason=r["lie_reason"][:80],
                       answer_text=(msgs[-1]["content"] or "").strip()[:20], n_tokens=len(ids),
                       answer_token=atok, before_token=L.tokenizer.decode([ids[ai - 1]]))
        for l in layers:
            for name, p in (("before", ai - 1), ("answer", ai)):
                h = acts[l][p]
                z = h if mean is None else (h - mean) / std
                s = float(probe(z))
                rec_row[f"L{l}_{name}_score"] = s
                rec_row[f"L{l}_{name}_zrms"] = None if mean is None else float(z.pow(2).mean().sqrt())
        out_rows.append(rec_row)
        if k % 20 == 0:
            logger.info("%d/%d rows", k, len(rows))

    slug = model_slug(args.model)
    out = args.out or os.path.join(ROOT, "runs/dyl_replication",
                                   f"{slug}__{args.split}{'__pt' if args.preserve_thinking else ''}"
                                   f"{'__nothink' if args.drop_thinking else ''}"
                                   f"{('__' + args.reasoning_effort) if args.reasoning_effort else ''}.jsonl")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        for rr in out_rows:
            f.write(json.dumps(rr, ensure_ascii=False) + "\n")

    lies = [rr for rr in out_rows if rr["is_lie"] == "lie"]
    hon = [rr for rr in out_rows if rr["is_lie"] == "honest"]
    print(f"\n{args.model} / {args.split}{' (preserve_thinking)' if args.preserve_thinking else ''}"
          f"{' (reasoning dropped)' if args.drop_thinking else ''}: "
          f"{len(lies)} lie / {len(hon)} honest scored, {n_skip} skipped")
    print(f"their validation metrics for this checkpoint: {ref}")
    print(f"tokens seen: before={sorted({rr['before_token'] for rr in out_rows})[:6]} "
          f"answer={sorted({rr['answer_token'] for rr in out_rows})[:6]}")
    print(f"{'layer':>5} {'position':>8} {'z-RMS med':>9} {'AUROC':>7} {'95% CI':>13} {'bal.acc':>7} {'flag lie':>8} {'flag hon':>8}")
    for l in layers:
        for name in ("before", "answer"):
            S = lambda g: [rr[f"L{l}_{name}_score"] for rr in g]
            zr = sorted(rr[f"L{l}_{name}_zrms"] for rr in out_rows if rr[f"L{l}_{name}_zrms"] is not None)
            a = auroc(S(lies), S(hon)); ci = boot_ci(S(lies), S(hon))
            tpr = sum(s > thr for s in S(lies)) / max(1, len(lies)); fpr = sum(s > thr for s in S(hon)) / max(1, len(hon))
            ba = (tpr + (1 - fpr)) / 2
            print(f"{l:>5} {name:>8} {(zr[len(zr)//2] if zr else float('nan')):>9.2f} {fmt(a):>7} "
                  f"{(f'{ci[0]:.3f}–{ci[1]:.3f}' if ci else 'n/a'):>13} {ba:>7.3f} {tpr:>8.2f} {fpr:>8.2f}")
    print(f"\nDONE -> {out}")

if __name__ == "__main__":
    main()
