#!/usr/bin/env python3
"""LOGIT-LENS-primary scouting pass (pipeline v3 P4; TODO item 2).

Mirror of the J-lens scouting method with the lens swapped: per model x
format x position x band, a frequency table over ALL judge-labeled
provided_facts items (unconditional on the self-report answer) — token ->
number of lie / truth items containing it in the LOGIT-LENS top-16 at that
position at >=1 band layer — with the same counts split by self-report
answer group (said-Yes / said-No) as columns. Trace positions
(preresp/postresp) are format-shared, so they are scouted once (on the Q1
sequences); elicited positions are scouted per format. No selection
threshold feeds scoring; tables are ranked by one-sided Fisher p purely for
display, and candidate counts are re-verified by the scorer against the raw
exports.

Output: results/scout_LL_v3.md — per-address ranked tables (top 12 a side
where min p < 0.1) plus a per-model digest of the strongest tokens.

Usage: python3 families/scout_LL_v3.py > results/scout_LL_v3.md
"""
import collections, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_families import ROOT, era_of, fisher_p, pos_of  # noqa: E402

MODELS = [
    dict(model="gemma-3-12b-it", export="exports/gemma_3_12b_it__c3_g0_k16",
         labels="runs/gemma_3_12b_it__c3_g0/judge_final_labels.json",
         formats=["Q1_bare", "Q2_after"],
         bands=[(14, 21), (22, 33), (34, 47)],
         positions=[f"{p}_slot{i}" for p in ("preresp", "postresp", "preans")
                    for i in range(5)] + ["q_last"]),
    dict(model="gemma-3-27b-it", export="exports/gemma_3_27b_it__c3_g0_k16",
         labels="runs/gemma_3_27b_it__c3_g0/judge_final_labels.json",
         formats=["Q1_bare", "Q2_after"],
         bands=[(14, 27), (28, 44), (45, 61)],
         positions=[f"{p}_slot{i}" for p in ("preresp", "postresp", "preans")
                    for i in range(5)] + ["q_last"]),
    dict(model="qwen3.6-27b", export="exports/qwen3_6_27b__c3_g0_k16",
         labels="runs/qwen3_6_27b__c3_g0/judge_final_labels.json",
         formats=["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab"],
         bands=[(14, 26), (27, 47), (48, 63)],
         positions=[f"{p}_slot{i}" for p in ("preresp", "postresp", "preans")
                    for i in range(5)] + ["q_last"]
                   + [f"think_slot{i}" for i in range(4)]),
]
TOPN = 12


def main():
    for M in MODELS:
        exp = os.path.join(ROOT, M["export"])
        lab = {}
        for k, v in json.load(open(os.path.join(ROOT, M["labels"]))).items():
            lab[(k.split("|")[0], k.split("|")[1])] = v["label"]
        man = json.load(open(os.path.join(exp, "manifest.json")))
        layers = man["layers"]
        lidx = {L: i for i, L in enumerate(layers)}
        # counts[(fmt,pname,band)][token] = [lie, truth, sy_l, sy_t, sn_l, sn_t]
        counts = collections.defaultdict(lambda: collections.defaultdict(lambda: [0] * 6))
        totals = collections.defaultdict(lambda: [0, 0])
        for it in man["items"]:
            fmt = it["format"]
            if fmt not in M["formats"] or "provided_facts" not in it["fact_id"]:
                continue
            v = lab.get((it["fact_id"], it["condition"]))
            if v not in ("lie", "truth"):
                continue
            li = 0 if v == "lie" else 1
            ans = it["answer_label"]
            f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
            voc = {int(k): w for k, w in f["vocab"].items()}
            for pname in M["positions"]:
                if era_of(pname) == "trace" and fmt != "Q1_bare":
                    continue  # trace positions are format-shared; scout once
                p = pos_of(f, pname)
                if p is None or p >= len(f["tokens"]):
                    continue
                for band in M["bands"]:
                    key = (fmt if era_of(pname) == "elicited" else "shared",
                           pname, band)
                    if pname == M["positions"][0]:
                        pass
                    seen = set()
                    for L in layers:
                        if band[0] <= L <= band[1]:
                            for t, _pr in f["readout"]["LL"][lidx[L]][p]:
                                seen.add(voc[t].strip().lower())
                    seen.discard("")
                    for w in seen:
                        c = counts[key][w]
                        c[li] += 1
                        if ans == "yes":
                            c[2 + li] += 1
                        elif ans == "no":
                            c[4 + li] += 1
            for pname in M["positions"]:
                if era_of(pname) == "trace" and fmt != "Q1_bare":
                    continue
                key0 = (fmt if era_of(pname) == "elicited" else "shared",
                        pname, M["bands"][0])
                totals[key0[0]][li] = totals[key0[0]][li]  # placeholder
        # per-format lie/truth item totals
        ftot = collections.defaultdict(lambda: [0, 0])
        for it in man["items"]:
            fmt = it["format"]
            if fmt not in M["formats"] or "provided_facts" not in it["fact_id"]:
                continue
            v = lab.get((it["fact_id"], it["condition"]))
            if v in ("lie", "truth"):
                ftot[fmt][0 if v == "lie" else 1] += 1
        print(f"\n# {M['model']} — logit-lens scout "
              f"(pf, judge labels; items per format: "
              + ", ".join(f"{k} {v[0]}/{v[1]}" for k, v in sorted(ftot.items()))
              + "; trace positions scouted once on Q1 sequences)")
        digest = []
        for key in sorted(counts):
            fmt, pname, band = key
            nl, nt = ftot["Q1_bare"] if fmt == "shared" else ftot[fmt]
            rows = []
            for w, c in counts[key].items():
                p_lie = fisher_p(c[0], nl - c[0], c[1], nt - c[1])
                p_tru = fisher_p(c[1], nt - c[1], c[0], nl - c[0])
                rows.append((min(p_lie, p_tru), p_lie <= p_tru, w, c))
            rows.sort()
            strong = [r for r in rows if r[0] < 0.1]
            if not strong:
                continue
            lie_side = [r for r in rows if r[1]][:TOPN]
            tru_side = [r for r in rows if not r[1]][:TOPN]
            print(f"\n## {fmt} · {pname} ({era_of(pname)}) · L{band[0]}-{band[1]} "
                  f"[{nl} lie / {nt} truth]")
            print("| side | token | lie/truth | saidYes l/t | saidNo l/t | p |")
            print("|---|---|---|---|---|---|")
            for p, is_lie, w, c in lie_side + tru_side:
                if p >= 0.1:
                    continue
                side = "lie" if is_lie else "truth"
                print(f"| {side} | `{w}` | {c[0]}/{c[1]} | {c[2]}/{c[3]} "
                      f"| {c[4]}/{c[5]} | {p:.4f} |")
                digest.append((p, side, w, fmt, pname, band, c))
        print(f"\n## DIGEST {M['model']} — strongest tokens across addresses (p<0.01)")
        digest.sort()
        seen_w = set()
        print("| side | token | best address | lie/truth | p |")
        print("|---|---|---|---|---|")
        for p, side, w, fmt, pname, band, c in digest:
            if p >= 0.01 or (side, w) in seen_w:
                continue
            seen_w.add((side, w))
            print(f"| {side} | `{w}` | {fmt}·{pname}·L{band[0]}-{band[1]} "
                  f"| {c[0]}/{c[1]} | {p:.5f} |")


if __name__ == "__main__":
    main()
