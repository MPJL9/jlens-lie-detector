#!/usr/bin/env python3
"""Stage-2 scores with CIs on the Q9 (DYL-wording) sequences: P(lie > truth |
model answered "No" to the self-report), for every family x address in a spec,
plus the corrected DYL probe in the same cell. Family score = the scorer's
presence rule; 2,000 stratified item resamples, seed 0. 2026-09-03."""
import argparse, json, os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "families"))
from score_families import pos_of, auroc, era_of  # noqa: E402
SLUG = {"gemma-3-12b-it": "gemma_3_12b_it", "gemma-3-27b-it": "gemma_3_27b_it", "qwen3.6-27b": "qwen3_6_27b"}

def ci(pos, neg, n=2000):
    rng = random.Random(0); v = []
    for _ in range(n):
        v.append(auroc([rng.choice(pos) for _ in pos], [rng.choice(neg) for _ in neg]))
    v.sort(); return v[int(0.025 * n)], v[int(0.975 * n) - 1]

ap = argparse.ArgumentParser(); ap.add_argument("--spec", required=True); ap.add_argument("--lens", default="J")
ap.add_argument("--answer", default="no"); args = ap.parse_args()
for block in json.load(open(os.path.join(ROOT, args.spec))):
    model = block["model"]
    if model not in SLUG:
        continue
    exp = os.path.join(ROOT, block["export"])
    lab = {(k.split("|")[0], k.split("|")[1]): v["label"] for k, v in json.load(open(os.path.join(ROOT, block["labels"]))).items()}
    man = json.load(open(os.path.join(exp, "manifest.json"))); layers = man["layers"]; lidx = {L: i for i, L in enumerate(layers)}
    files = {}
    for it in man["items"]:
        if it["format"] != "Q9_dyl" or "provided_facts" not in it["fact_id"] or it["answer_label"] != args.answer:
            continue
        v = lab.get((it["fact_id"], it["condition"]))
        if v in ("lie", "truth"):
            files[(it["fact_id"], it["condition"])] = (v, json.load(open(os.path.join(exp, it["seq_id"] + ".json"))))
    nl = sum(v == "lie" for v, _ in files.values()); nt = len(files) - nl
    probe = {}
    for l in open(os.path.join(ROOT, f"runs/{SLUG[model]}__c3_q9/dyl_probe_from_cache_before.jsonl")):
        r = json.loads(l)
        if r["src"] == "pf" and r["dyl_answer"] == args.answer:
            probe[(r["fact_id"], r["condition"])] = r["probe_score"]
    P = [probe[k] for k, (v, _) in files.items() if v == "lie" and k in probe]; N = [probe[k] for k, (v, _) in files.items() if v == "truth" and k in probe]
    c = ci(P, N)
    print(f"\n## {model} — stage 2, said-{args.answer} cell on Q9 items: {nl} lie / {nt} truth (spec {os.path.basename(args.spec)}, lens {args.lens})")
    print("| detector | address | era | AUROC (95% CI) | visibility lie/truth |\n|---|---|---|---|---|")
    print(f"| **DYL probe, token before answer** | probe layer | elicited | **{auroc(P, N):.3f}** ({c[0]:.3f}–{c[1]:.3f}) | — |")
    for fam in block["families"]:
        lw = [w.lower() for w in fam["lie"]]; tw = [w.lower() for w in fam.get("truth", [])]
        for a in fam["addresses"]:
            pname, band = a[0], (a[1], a[2]); bidx = [lidx[L] for L in layers if band[0] <= L <= band[1]]
            pos, neg, vl, vt = [], [], 0, 0
            for k, (v, f) in files.items():
                vocab = {int(t): w for t, w in f["vocab"].items()}; p = pos_of(f, pname); seen = set()
                if p is not None and p < len(f["tokens"]):
                    for li in bidx:
                        for t, _ in f["readout"][args.lens][li][p]:
                            seen.add(vocab[t].strip().lower())
                s = sum(w in seen for w in lw) - sum(w in seen for w in tw); vis = any(w in seen for w in lw + tw)
                (pos if v == "lie" else neg).append(s)
                if v == "lie": vl += vis
                else: vt += vis
            a_ = auroc(pos, neg)
            if a_ is None: continue
            c = ci(pos, neg)
            print(f"| {fam['name']} | {pname} L{band[0]}–{band[1]} | {era_of(pname)} | {a_:.3f} ({c[0]:.3f}–{c[1]:.3f}) | {vl}/{nl} {vt}/{nt} |")
