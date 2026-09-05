#!/usr/bin/env python3
"""Bootstrap CIs for the headline family AUROCs and the paired family-minus-
probe difference on the IDENTICAL Q9 items (2026-09-03; replaces the void
paired bootstrap that used the mis-positioned probe).

Per-item family score = the scorer's own rule (families/score_families.py:
presence count of family words in the top-16 readout at the declared
address, lie-side minus truth-side, primary lens J). Probe score = the
corrected-position offline scorer output
(runs/<slug>__c3_q9/dyl_probe_from_cache_before.jsonl). Items are one per
scenario x condition in these cells, so item resampling = scenario
resampling. 2000 stratified resamples (lie and truth separately), seed 0,
95% percentile CI; the paired difference resamples the same items for both
scores.
"""
import json, os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "families"))
from score_families import seg, pos_of, auroc  # noqa: E402

TARGETS = [  # model, family name, address (pos, lo, hi), cell answer_label (None = all items)
    ("gemma-3-12b-it", "F2 suspicion-emoji", ("postresp_slot2", 14, 44), None),
    ("gemma-3-12b-it", "F1 lie-words", ("postresp_slot1", 22, 33), None),
    ("gemma-3-27b-it", "F2 suspicion-emoji", ("postresp_slot2", 14, 44), None),
    ("qwen3.6-27b", "Q-A falsehood/honesty", ("postresp_slot1", 48, 63), None),
    ("qwen3.6-27b", "Q-A falsehood/honesty", ("postresp_slot1", 48, 63), "no"),
    ("gemma-3-12b-it", "F2 suspicion-emoji", ("postresp_slot2", 14, 44), "no"),
]
SLUG = {"gemma-3-12b-it": "gemma_3_12b_it", "gemma-3-27b-it": "gemma_3_27b_it", "qwen3.6-27b": "qwen3_6_27b"}

def family_scores(block, fam, addr, answer_label):
    exp = os.path.join(ROOT, block["export"])
    lab = {(k.split("|")[0], k.split("|")[1]): v["label"]
           for k, v in json.load(open(os.path.join(ROOT, block["labels"]))).items()}
    man = json.load(open(os.path.join(exp, "manifest.json")))
    layers = man["layers"]; lidx = {L: i for i, L in enumerate(layers)}
    lw = [w.lower() for w in fam["lie"]]; tw = [w.lower() for w in fam.get("truth", [])]
    pname, band = addr[0], (addr[1], addr[2])
    bidx = [lidx[L] for L in layers if band[0] <= L <= band[1]]
    out = {}
    for it in man["items"]:
        if it["format"] != "Q9_dyl" or "provided_facts" not in it["fact_id"]:
            continue
        if answer_label and it["answer_label"] != answer_label:
            continue
        v = lab.get((it["fact_id"], it["condition"]))
        if v not in ("lie", "truth"):
            continue
        f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
        vocab = {int(k): w for k, w in f["vocab"].items()}
        p = pos_of(f, pname)
        seen = set()
        if p is not None and p < len(f["tokens"]):
            for li in bidx:
                for t, _ in f["readout"]["J"][li][p]:
                    seen.add(vocab[t].strip().lower())
        out[(it["fact_id"], it["condition"])] = (v, sum(w in seen for w in lw) - sum(w in seen for w in tw))
    return out

def ci(vals):
    vals = sorted(vals); n = len(vals)
    return vals[int(0.025 * n)], vals[int(0.975 * n) - 1]

def main():
    spec = {b["model"]: b for b in json.load(open(os.path.join(ROOT, "families/specs/family_spec_q9.json")))}
    print(f"{'model':<15} {'family @ address':<42} {'cell':<8} {'n l/t':>6} {'family AUROC (95% CI)':>24} {'probe AUROC (95% CI)':>24} {'fam − probe (95% CI)':>24} {'P(diff≤0)':>9}")
    for model, fname, addr, ans in TARGETS:
        block = spec[model]
        fam = next(f for f in block["families"] if f["name"] == fname)
        fs = family_scores(block, fam, addr, ans)
        probe = {}
        for l in open(os.path.join(ROOT, f"runs/{SLUG[model]}__c3_q9/dyl_probe_from_cache_before.jsonl")):
            r = json.loads(l)
            if r["src"] == "pf" and (not ans or r["dyl_answer"] == ans):
                probe[(r["fact_id"], r["condition"])] = r["probe_score"]
        keys = [k for k in fs if k in probe]
        lies = [k for k in keys if fs[k][0] == "lie"]; truths = [k for k in keys if fs[k][0] == "truth"]
        F = lambda ks: [fs[k][1] for k in ks]; P = lambda ks: [probe[k] for k in ks]
        a_f, a_p = auroc(F(lies), F(truths)), auroc(P(lies), P(truths))
        rng = random.Random(0); bf, bp, bd = [], [], []
        for _ in range(2000):
            L = [rng.choice(lies) for _ in lies]; T = [rng.choice(truths) for _ in truths]
            x, y = auroc(F(L), F(T)), auroc(P(L), P(T))
            bf.append(x); bp.append(y); bd.append(x - y)
        cf, cp, cd = ci(bf), ci(bp), ci(bd)
        print(f"{model:<15} {fname + ' @ ' + addr[0] + f' L{addr[1]}-{addr[2]}':<42} {('said-' + ans) if ans else 'all':<8} {len(lies):>2}/{len(truths):<3} "
              f"{a_f:.3f} ({cf[0]:.3f}–{cf[1]:.3f}){'':>3} {a_p:.3f} ({cp[0]:.3f}–{cp[1]:.3f}){'':>3} "
              f"{a_f - a_p:+.3f} ({cd[0]:+.3f}..{cd[1]:+.3f}) {sum(d <= 0 for d in bd) / len(bd):>9.4f}")

if __name__ == "__main__":
    main()
