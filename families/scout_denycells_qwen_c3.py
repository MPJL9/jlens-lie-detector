#!/usr/bin/env python3
"""Qwen3.6-27B deny-cell (said-No) vocabulary scout — judge labels, sources
split, pre/post-response position classes kept separate per the 2026-08-26
binding rule. Method otherwise identical to the Gemma scouts: per cell x
position class x layer band, count = items whose J-lens top-16 at that single
position contains the token (stripped, lowercased) at >=1 band layer.
Display filter >=3 items total; no selection threshold - eyeball material.

Position classes (all stage-2, guaranteed): postresp_slot0-4 (post-response
boundary), q_last, preans_slot0-4 (pre-answer boundary), think_slot0-3 (the
Qwen-only empty <think> scaffold; think_slot3 = P2).
Bands from the band-location pass (not included) (label-blind): L14-26 early,
L27-47 workspace, L48-63 motor.

Usage: python3 families/scout_denycells_qwen_c3.py > analysis_scout_denycells_qwen_c3_k16.md
"""
import json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = os.path.join(ROOT, "exports", "qwen3_6_27b__c3_g0_k16")
LABELS = os.path.join(ROOT, "runs", "qwen3_6_27b__c3_g0", "judge_final_labels.json")
BANDS = [(14, 26), (27, 47), (48, 63)]
FORMATS = ["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab", "Q8_debrief"]
MAX_ROWS = 25
MIN_TOTAL = 3

def seg(f, name):
    for s in f["segments"]:
        if s["name"] == name:
            return s

def positions(f):
    out = {}
    resp, q, g = seg(f, "response"), seg(f, "self_q"), seg(f, "gen_prompt")
    T = len(f["tokens"])
    for i in range(5):
        p = resp["end"] + i
        if p < q["start"]:
            out[f"postresp_slot{i}"] = p
    out["q_last"] = q["end"] - 1
    gl = g["end"] - g["start"]
    for i in range(min(5, gl)):
        out[f"preans_slot{i}"] = g["start"] + i
    for i in range(4):
        p = g["start"] + 5 + i
        if p < g["end"]:
            out[f"think_slot{i}"] = p
    return {k: v for k, v in out.items() if 0 <= v < T}

def main():
    jl = {}
    for k, v in json.load(open(LABELS)).items():
        fact_id, cond = k.split("|")[0], k.split("|")[1]
        jl[("mask_" + fact_id if not fact_id.startswith("mask_") else fact_id,
            cond)] = v["label"]
    man = json.load(open(os.path.join(EXP, "manifest.json")))
    layer_list = man["layers"]
    lidx = {L: i for i, L in enumerate(layer_list)}

    print("# Qwen3.6-27B deny-cell scout — judge labels, top-16 J-lens")
    print("Bands (label-blind location): L14-26 early / L27-47 workspace / "
          "L48-63 motor. Counts show (provided_facts+doubling_down).")

    for fmt in FORMATS:
        rows = [it for it in man["items"]
                if it["format"] == fmt and it["answer_label"] == "no"]
        tally = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
        n_cell = collections.Counter()
        sanity = collections.defaultdict(collections.Counter)
        for it in rows:
            lab = jl.get((it["fact_id"], it["condition"]))
            if lab not in ("lie", "truth"):
                continue  # ambiguous or missing -> excluded
            f = json.load(open(os.path.join(EXP, it["seq_id"] + ".json")))
            src = "pf" if "provided_facts" in f["fact_id"] else "dd"
            n_cell[(lab, src)] += 1
            vocab = {int(k): v for k, v in f["vocab"].items()}
            pos = positions(f)
            for pname, p in pos.items():
                sanity[pname][f["tokens"][p]] += 1
            J = f["readout"]["J"]
            for lo, hi in BANDS:
                band = [lidx[L] for L in layer_list if lo <= L <= hi]
                for pname, p in pos.items():
                    seen = set()
                    for li in band:
                        for tok_id, _s in J[li][p]:
                            seen.add(vocab[tok_id].strip().lower())
                    for w in seen:
                        tally[(pname, f"L{lo}-{hi}")][w][(lab, src)] += 1

        nl = n_cell[("lie", "pf")] + n_cell[("lie", "dd")]
        nt = n_cell[("truth", "pf")] + n_cell[("truth", "dd")]
        print(f"\n# CELL qwen_{fmt}_saidNo")
        print(f"n: {nl} lie ({n_cell[('lie','pf')]}pf+{n_cell[('lie','dd')]}dd) / "
              f"{nt} truth ({n_cell[('truth','pf')]}pf+{n_cell[('truth','dd')]}dd)"
              f"  [judge labels; ambiguous excluded]")
        print("position sanity:", {p: sanity[p].most_common(2) for p in sorted(sanity)[:4]})
        if nl < 5 or nt < 5:
            print("(cell below 5/side — tables skipped)")
            continue

        pclasses = ([f"postresp_slot{i}" for i in range(5)] + ["q_last"] +
                    [f"preans_slot{i}" for i in range(5)] +
                    [f"think_slot{i}" for i in range(4)])
        for pname in pclasses:
            for lo, hi in BANDS:
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
                print(f"\n## qwen_{fmt}_saidNo | {pname} | L{lo}-{hi}  "
                      f"(n: {nl} lie / {nt} truth)\n")
                print("| token | lie (pf+dd) | truth (pf+dd) | gap |")
                print("|---|---|---|---|")
                for gap, w, c, l, t in scored[:MAX_ROWS]:
                    print(f"| {w} | {l} ({c[('lie','pf')]}+{c[('lie','dd')]}) "
                          f"| {t} ({c[('truth','pf')]}+{c[('truth','dd')]}) "
                          f"| {gap:.2f} |")

if __name__ == "__main__":
    main()
