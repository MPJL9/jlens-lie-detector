#!/usr/bin/env python3
"""95% bootstrap CI for one family x address x cell row of a scorer spec.
Same item selection and presence score as score_families.py; same bootstrap
as family_scores_saidno_ci.py (2,000 stratified item resamples, seed 0,
percentile CI). Usage:
  python3 families/family_auroc_ci.py --spec families/specs/family_spec_v3.json \
      --model qwen3.6-27b --cell Q7_saidNo_pf --family "Q-A falsehood/honesty" \
      --address preans_slot1:48-63 [--lens J|LL]
"""
import argparse, json, os, random, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "families"))
from score_families import pos_of, auroc  # noqa: E402

def ci(pos, neg, n=2000):
    rng = random.Random(0); v = []
    for _ in range(n):
        v.append(auroc([rng.choice(pos) for _ in pos], [rng.choice(neg) for _ in neg]))
    v.sort(); return v[int(0.025 * n)], v[int(0.975 * n) - 1]

ap = argparse.ArgumentParser()
ap.add_argument("--spec", required=True); ap.add_argument("--model", required=True)
ap.add_argument("--cell", required=True); ap.add_argument("--family", required=True)
ap.add_argument("--address", required=True, help="pos:lo-hi"); ap.add_argument("--lens", default="J")
a = ap.parse_args()
pname, band = a.address.split(":"); lo, hi = (int(x) for x in band.split("-"))
block = next(b for b in json.load(open(os.path.join(ROOT, a.spec))) if b["model"] == a.model)
cell = next((c for c in block["cells"] if c["name"] == a.cell), None)
if cell is None:
    sys.exit("cells: " + ", ".join(c["name"] for c in block["cells"]))
fam = next((f for f in block["families"] if f["name"] == a.family), None)
if fam is None:
    sys.exit("families: " + " | ".join(f["name"] for f in block["families"]))
lw = [w.lower() for w in fam["lie"]]; tw = [w.lower() for w in fam.get("truth", [])]
exp = os.path.join(ROOT, block["export"])
lab = {(k.split("|")[0], k.split("|")[1]): v["label"] for k, v in json.load(open(os.path.join(ROOT, block["labels"]))).items()}
resp_ans = {}
for l in open(os.path.join(ROOT, block["transcripts"])):
    r = json.loads(l); resp_ans[(r["fact_id"], r["condition"])] = r.get("answer_said")
man = json.load(open(os.path.join(exp, "manifest.json"))); layers = man["layers"]
bidx = [i for i, L in enumerate(layers) if lo <= L <= hi]
pos, neg = [], []
for it in man["items"]:
    if it["format"] not in cell["formats"]: continue
    if cell.get("answer_label") and it["answer_label"] != cell["answer_label"]: continue
    if cell.get("resp_answer") and resp_ans.get((it["fact_id"], it["condition"])) != cell["resp_answer"]: continue
    src = "pf" if "provided_facts" in it["fact_id"] else "dd"
    if src not in cell["sources"]: continue
    v = lab.get((it["fact_id"], it["condition"]))
    if v not in ("lie", "truth"): continue
    f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
    vocab = {int(k): w for k, w in f["vocab"].items()}
    p = pos_of(f, pname)
    if p is None or p >= len(f["tokens"]): continue
    seen = {vocab[t].strip().lower() for li in bidx for t, _ in f["readout"][a.lens][li][p]}
    s = sum(w in seen for w in lw) - sum(w in seen for w in tw)
    (pos if v == "lie" else neg).append(s)
au = auroc(pos, neg); lo_, hi_ = ci(pos, neg)
print(f"{a.model} | {a.cell} {len(pos)}/{len(neg)} | {a.family} | {a.address} | {a.lens} | "
      f"AUROC {au:.3f} (95% CI {lo_:.3f}–{hi_:.3f})")
