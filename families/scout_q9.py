#!/usr/bin/env python3
"""Scouting pass for the Q9 (exact DYL wording) cells — pipeline v3 P4.

The c3_q9 runs were scored with the FROZEN families only; this is the
missing scout of the Q9 sequences' own readouts. Same procedure as
scout_LL_v3.py / the J scout: per model x position x band, over all
judge-labeled provided_facts Q9 items (unconditional on the self-report
answer), token -> lie/truth item counts in the top-16 at >=1 band layer,
with said-Yes / said-No splits as columns; ranked by one-sided Fisher p for
display only. ELICITED positions only — trace positions are format-shared
and were scouted in the v3 passes. BOTH lenses, each in its own table
column block (J first, then LL), since family generation runs per lens.

Question-echo warning for curation: Q9's text contains "lie" ("Did you lie
in the last message..."), so lie/lying/lied tokens at elicited addresses
carry the same echo status "deceptive" had under Q1 — both classes read the
same question, so separation remains informative, but flag them.

Usage: python3 families/scout_q9.py > results/scout_q9.md
"""
import collections, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score_families import ROOT, era_of, fisher_p, pos_of  # noqa: E402

MODELS = [
    dict(model="gemma-3-12b-it", export="exports/gemma_3_12b_it__c3_q9",
         labels="runs/gemma_3_12b_it__c3_g0/judge_final_labels.json",
         bands=[(14, 21), (22, 33), (34, 47)],
         positions=[f"preans_slot{i}" for i in range(5)] + ["q_last"]),
    dict(model="gemma-3-27b-it", export="exports/gemma_3_27b_it__c3_q9",
         labels="runs/gemma_3_27b_it__c3_g0/judge_final_labels.json",
         bands=[(14, 27), (28, 44), (45, 61)],
         positions=[f"preans_slot{i}" for i in range(5)] + ["q_last"]),
    dict(model="qwen3.6-27b", export="exports/qwen3_6_27b__c3_q9",
         labels="runs/qwen3_6_27b__c3_g0/judge_final_labels.json",
         bands=[(14, 26), (27, 47), (48, 63)],
         positions=[f"preans_slot{i}" for i in range(5)] + ["q_last"]
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
        counts = {lens: collections.defaultdict(
            lambda: collections.defaultdict(lambda: [0] * 6))
            for lens in ("J", "LL")}
        nl = nt = 0
        for it in man["items"]:
            if it["format"] != "Q9_dyl" or "provided_facts" not in it["fact_id"]:
                continue
            v = lab.get((it["fact_id"], it["condition"]))
            if v not in ("lie", "truth"):
                continue
            li = 0 if v == "lie" else 1
            nl += li == 0
            nt += li == 1
            ans = it["answer_label"]
            f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
            voc = {int(k): w for k, w in f["vocab"].items()}
            for pname in M["positions"]:
                assert era_of(pname) == "elicited"
                p = pos_of(f, pname)
                if p is None or p >= len(f["tokens"]):
                    continue
                for band in M["bands"]:
                    for lens in ("J", "LL"):
                        seen = set()
                        for L in layers:
                            if band[0] <= L <= band[1]:
                                for t, _pr in f["readout"][lens][lidx[L]][p]:
                                    seen.add(voc[t].strip().lower())
                        seen.discard("")
                        for w in seen:
                            c = counts[lens][(pname, band)][w]
                            c[li] += 1
                            if ans == "yes":
                                c[2 + li] += 1
                            elif ans == "no":
                                c[4 + li] += 1
        print(f"\n# {M['model']} — Q9 (exact DYL wording) scout, elicited "
              f"positions [{nl} lie / {nt} truth provided_facts items, judge "
              f"labels; both lenses; question-echo candidates: lie/lied/lying "
              f"and 'message' appear in the Q9 question text]")
        for lens in ("J", "LL"):
            digest = []
            for key in sorted(counts[lens]):
                pname, band = key
                rows = []
                for w, c in counts[lens][key].items():
                    p_lie = fisher_p(c[0], nl - c[0], c[1], nt - c[1])
                    p_tru = fisher_p(c[1], nt - c[1], c[0], nl - c[0])
                    rows.append((min(p_lie, p_tru), p_lie <= p_tru, w, c))
                rows.sort()
                if not [r for r in rows if r[0] < 0.1]:
                    continue
                lie_side = [r for r in rows if r[1]][:TOPN]
                tru_side = [r for r in rows if not r[1]][:TOPN]
                print(f"\n## [{lens}] {pname} · L{band[0]}-{band[1]}")
                print("| side | token | lie/truth | saidYes l/t | saidNo l/t | p |")
                print("|---|---|---|---|---|---|")
                for p, is_lie, w, c in lie_side + tru_side:
                    if p >= 0.1:
                        continue
                    side = "lie" if is_lie else "truth"
                    print(f"| {side} | `{w}` | {c[0]}/{c[1]} | {c[2]}/{c[3]} "
                          f"| {c[4]}/{c[5]} | {p:.4f} |")
                    digest.append((p, side, w, pname, band, c))
            print(f"\n## [{lens}] DIGEST {M['model']} (p<0.01, best address per token)")
            digest.sort()
            seen_w = set()
            print("| side | token | best address | lie/truth | p |")
            print("|---|---|---|---|---|")
            for p, side, w, pname, band, c in digest:
                if p >= 0.01 or (side, w) in seen_w:
                    continue
                seen_w.add((side, w))
                print(f"| {side} | `{w}` | {pname}·L{band[0]}-{band[1]} "
                      f"| {c[0]}/{c[1]} | {p:.5f} |")

if __name__ == "__main__":
    main()
