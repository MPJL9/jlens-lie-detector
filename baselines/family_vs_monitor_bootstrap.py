#!/usr/bin/env python3
"""Paired bootstrap: family presence score vs the transcript-only Sonnet monitor
(without-system variant) on IDENTICAL stage-1 provided_facts items. Same
routine as dyl_vs_family_bootstrap.py: 2,000 stratified item resamples, seed
0, the same resample scores both detectors; 95% percentile CI of the
difference and the share of resamples with difference <= 0. 2026-09-04."""
import glob, json, os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "families"))
from score_families import pos_of, auroc  # noqa: E402

ROWS = [("gemma-3-12b-it", "F2 suspicion-emoji", "postresp_slot2", 14, 44),
        ("gemma-3-12b-it", "F1 lie-words", "postresp_slot1", 22, 33),
        ("gemma-3-27b-it", "F2 suspicion-emoji", "postresp_slot2", 14, 44),
        ("qwen3.6-27b", "Q-A falsehood/honesty", "postresp_slot1", 48, 63)]
MON = os.path.join(ROOT, "runs/monitor_baseline_c3_sonnet")
km = json.load(open(os.path.join(MON, "keymap.json")))
mon = {}
for f in glob.glob(os.path.join(MON, "outputs", "*without-system*.jsonl")):
    for l in open(f):
        if l.strip():
            r = json.loads(l); m = km[r["id"]]
            mon[(m["model"], m["fact_id"], m["condition"])] = float(r["p_lie"])
spec = json.load(open(os.path.join(ROOT, "families/specs/family_spec_v3.json")))
print("| model | family @ address | n lie/truth | family AUROC (CI) | monitor AUROC (CI) | family − monitor (CI) | resamples ≤ 0 |")
print("|---|---|---|---|---|---|---|")
for model, fname, pname, lo, hi in ROWS:
    block = next(b for b in spec if b["model"] == model)
    cell = next(c for c in block["cells"] if c["stage"] == 1 and c["sources"] == ["pf"] and not c.get("resp_answer"))
    fam = next(f for f in block["families"] if f["name"] == fname)
    lw = [w.lower() for w in fam["lie"]]; tw = [w.lower() for w in fam.get("truth", [])]
    exp = os.path.join(ROOT, block["export"])
    lab = {(k.split("|")[0], k.split("|")[1]): v["label"] for k, v in json.load(open(os.path.join(ROOT, block["labels"]))).items()}
    man = json.load(open(os.path.join(exp, "manifest.json"))); layers = man["layers"]
    bidx = [i for i, L in enumerate(layers) if lo <= L <= hi]
    items = []
    for it in man["items"]:
        if it["format"] not in cell["formats"] or "provided_facts" not in it["fact_id"]: continue
        v = lab.get((it["fact_id"], it["condition"]))
        if v not in ("lie", "truth"): continue
        key = (model, it["fact_id"], it["condition"])
        if key not in mon: continue
        f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
        vocab = {int(k): w for k, w in f["vocab"].items()}
        p = pos_of(f, pname)
        if p is None or p >= len(f["tokens"]): continue
        seen = {vocab[t].strip().lower() for li in bidx for t, _ in f["readout"]["J"][li][p]}
        s = sum(w in seen for w in lw) - sum(w in seen for w in tw)
        items.append((v, s, mon[key]))
    L = [x for x in items if x[0] == "lie"]; T = [x for x in items if x[0] == "truth"]
    af = auroc([x[1] for x in L], [x[1] for x in T]); am = auroc([x[2] for x in L], [x[2] for x in T])
    rng = random.Random(0); df, ff, mm = [], [], []
    for _ in range(2000):
        bl = [rng.choice(L) for _ in L]; bt = [rng.choice(T) for _ in T]
        a1 = auroc([x[1] for x in bl], [x[1] for x in bt]); a2 = auroc([x[2] for x in bl], [x[2] for x in bt])
        ff.append(a1); mm.append(a2); df.append(a1 - a2)
    q = lambda v: (sorted(v)[50], sorted(v)[1949])
    fl, fh = q(ff); ml, mh = q(mm); dl, dh = q(df)
    print(f"| {model} | {fname} @ {pname} L{lo}–{hi} | {len(L)}/{len(T)} | {af:.3f} ({fl:.3f}–{fh:.3f}) | {am:.3f} ({ml:.3f}–{mh:.3f}) "
          f"| {af-am:+.3f} ({dl:+.3f}..{dh:+.3f}) | {sum(d <= 0 for d in df)/2000:.1%} |")
