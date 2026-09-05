"""Merge the per-wording curator outputs results/family_gen_near_answer_qwen_<wording>.md
into one scoring spec (families/specs/family_spec_near_answer_gen.json). Mechanical: the first
JSON array in each file, families verbatim (name prefixed with the wording tag), cells copied
from families/specs/family_spec_preans_sweep.json.

Usage: python3 families/build_near_answer_spec.py
"""
import json, re, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fams, report = [], []
for path in sorted(glob.glob(f"{ROOT}/results/family_gen_near_answer_qwen_*.md")):
    tag = re.search(r"family_gen_near_answer_qwen_(.+)\.md$", path).group(1)
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"```(?:json)?\s*(\[.*?\])\s*```", txt, re.S) or \
        re.search(r"(\[\s*\{.*\"families\".*?\}\s*\])", txt, re.S)
    if not m:
        report.append(f"{tag}: NO JSON FOUND"); continue
    blocks = json.loads(m.group(1))
    n = 0
    for b in blocks:
        for f in b["families"]:
            fams.append({"name": f"[{tag}] {f['name']}", "lie": f.get("lie", []),
                         "truth": f.get("truth", []),
                         "addresses": [[a[0], int(a[1]), int(a[2])] for a in f["addresses"]],
                         "flags": f.get("flags", [])})
            n += 1
    report.append(f"{tag}: {n} families")
base = json.load(open(f"{ROOT}/families/specs/family_spec_preans_sweep.json", encoding="utf-8"))
for blk in base:
    blk["families"] = fams
out = f"{ROOT}/families/specs/family_spec_near_answer_gen.json"
json.dump(base, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n".join(report)); print(len(fams), "families ->", out)
