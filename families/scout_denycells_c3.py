#!/usr/bin/env python3
"""Fresh deny-cell vocabulary scout (2026-08-26 redo; first pass voided).

Cells: 12B Q6_factual said-No, 12B Q7_ab said-No, 27B Q7_ab said-No.
Method identical to analysis_scout_c3_k16.md: per cell x position class x
layer band, count items where a token (stripped, lowercased) appears in the
J-lens top-16 at that single position at >=1 band layer. Sources
(provided_facts / doubling_down) shown separately. Display filter: >=3 items
total. No selection threshold - eyeball material.

Usage: python3 families/scout_denycells_c3.py > analysis_scout_denycells_c3_fresh.md
"""
import json, glob, os, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CELLS = [
    # (label, export_dir, format, answer_label, bands)
    ("12b_Q6_saidNo", "gemma_3_12b_it__c3_g0_k16", "Q6_factual", "no",
     [(14, 21), (22, 33), (34, 47)]),
    ("12b_Q7_saidNo", "gemma_3_12b_it__c3_g0_k16", "Q7_ab", "no",
     [(14, 21), (22, 33), (34, 47)]),
    ("27b_Q7_saidNo", "gemma_3_27b_it__c3_g0_k16", "Q7_ab", "no",
     [(14, 27), (28, 44), (45, 61)]),
]

MAX_ROWS = 30
MIN_TOTAL = 3

def seg(item, name):
    for s in item["segments"]:
        if s["name"] == name:
            return s
    return None

def positions(item):
    """position-class name -> token index (guaranteed positions only)."""
    out = {}
    resp = seg(item, "response")
    q = seg(item, "self_q")
    gen = seg(item, "gen_prompt")
    T = len(item["tokens"])
    if resp and q:
        for i in range(5):
            p = resp["end"] + i
            if p < q["start"]:
                out[f"postresp_slot{i}"] = p
    if q:
        out["q_last"] = q["end"] - 1
    if gen:
        for i in range(min(5, gen["end"] - gen["start"])):
            out[f"preans_slot{i}"] = gen["start"] + i
    return {k: v for k, v in out.items() if 0 <= v < T}

def source(fact_id):
    return "pf" if "provided_facts" in fact_id else "dd"

def main():
    for label, exp_dir, fmt, ans, bands in CELLS:
        d = os.path.join(ROOT, "exports", exp_dir)
        man = json.load(open(os.path.join(d, "manifest.json")))
        layer_list = man["layers"]
        lidx = {L: i for i, L in enumerate(layer_list)}
        rows = [it for it in man["items"]
                if it["format"] == fmt and it["answer_label"] == ans]
        # tally: (posclass, band) -> token -> {(cond,src): n_items}
        tally = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
        n_cell = collections.Counter()
        sanity = collections.Counter()
        for it in rows:
            f = json.load(open(os.path.join(d, it["seq_id"] + ".json")))
            cond, src = f["condition"], source(f["fact_id"])
            n_cell[(cond, src)] += 1
            vocab = {int(k): v for k, v in f["vocab"].items()}
            pos = positions(f)
            for pname, p in pos.items():
                sanity[(pname, f["tokens"][p])] += 1
            J = f["readout"]["J"]  # [layer_idx][pos][k] -> [tok_id, score]
            for lo, hi in bands:
                band_layers = [lidx[L] for L in layer_list if lo <= L <= hi]
                for pname, p in pos.items():
                    seen = set()
                    for li in band_layers:
                        for tok_id, _s in J[li][p]:
                            w = vocab[tok_id].strip().lower()
                            seen.add(w)
                    for w in seen:
                        tally[(pname, f"L{lo}-{hi}")][w][(cond, src)] += 1

        nl = n_cell[("lie", "pf")] + n_cell[("lie", "dd")]
        nt = n_cell[("truth", "pf")] + n_cell[("truth", "dd")]
        print(f"\n# CELL {label} ({fmt}, answer_label={ans})")
        print(f"n: {nl} lie ({n_cell[('lie','pf')]}pf+{n_cell[('lie','dd')]}dd) / "
              f"{nt} truth ({n_cell[('truth','pf')]}pf+{n_cell[('truth','dd')]}dd)")
        print("\nposition-token sanity (class -> tokens seen):")
        bypos = collections.defaultdict(collections.Counter)
        for (pname, tok), c in sanity.items():
            bypos[pname][tok] += c
        for pname in sorted(bypos):
            toks = ", ".join(f"{t!r}x{c}" for t, c in bypos[pname].most_common(4))
            print(f"  {pname}: {toks}")

        pclasses = ([f"postresp_slot{i}" for i in range(5)] + ["q_last"] +
                    [f"preans_slot{i}" for i in range(5)])
        for pname in pclasses:
            for lo, hi in bands:
                key = (pname, f"L{lo}-{hi}")
                if key not in tally:
                    continue
                scored = []
                for w, c in tally[key].items():
                    l = c[("lie", "pf")] + c[("lie", "dd")]
                    t = c[("truth", "pf")] + c[("truth", "dd")]
                    if l + t < MIN_TOTAL:
                        continue
                    gap = abs(l / nl - t / nt)
                    scored.append((gap, w, c, l, t))
                scored.sort(key=lambda x: -x[0])
                print(f"\n## {label} | {pname} | L{lo}-{hi}  "
                      f"(n: {nl} lie / {nt} truth)\n")
                print("| token | lie (pf+dd) | truth (pf+dd) | gap |")
                print("|---|---|---|---|")
                for gap, w, c, l, t in scored[:MAX_ROWS]:
                    print(f"| {w} | {l} ({c[('lie','pf')]}+{c[('lie','dd')]}) "
                          f"| {t} ({c[('truth','pf')]}+{c[('truth','dd')]}) "
                          f"| {gap:.2f} |")

if __name__ == "__main__":
    main()
