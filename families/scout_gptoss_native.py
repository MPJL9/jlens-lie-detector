#!/usr/bin/env python3
"""P4 scouting pass for gpt-oss-20b (native vocabulary, not the frozen
cross-model core). One table per position x band x lens over ALL
judge-labeled provided_facts items (unconditional on the self-report;
the said-Yes/said-No split columns required by P4 are UNAVAILABLE on
this model — self-report answers were unrecoverable from the c3 run).

Positions from the verified slot map (OBSERVATIONS, gpt-oss section):
preresp = 6 template tokens anchored at the turn-end marker <|end|>
(= response.start-6 except for items with stray prompt-tail tokens),
postresp = 4 tokens <|end|> <|start|> user <|message|> at response.end,
preans = gen_prompt tokens <|end|> <|start|> assistant, q_last.
Bands (label-blind P1): early L0-8, workspace L9-18, motor L19-23.

Output: results/scout_gptoss_native.md
"""
import json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT = os.path.join(ROOT, "exports/gpt_oss_20b")
LABELS = os.path.join(ROOT, "runs/gpt_oss_20b/judge_final_labels.json")
OUT = os.path.join(ROOT, "results/scout_gptoss_native.md")
BANDS = [("early", 0, 8), ("workspace", 9, 18), ("motor", 19, 23)]
TURN_END = {"<|end|>", "<|im_end|>", "<end_of_turn>"}

def seg(f, n):
    for s in f["segments"]:
        if s["name"] == n:
            return s

def pos_of(f, name):
    r, q, g = seg(f, "response"), seg(f, "self_q"), seg(f, "gen_prompt")
    if name.startswith("postresp_slot"):
        p = r["end"] + int(name[-1])
        return p if q is None or p < q["start"] else None
    if name.startswith("preresp_slot"):
        u = seg(f, "user_prompt")
        anchor = None
        for i in range(u["end"], r["start"]):
            if f["tokens"][i] in TURN_END:
                anchor = i
                break
        if anchor is None:
            anchor = r["start"] - 6
        p = anchor + int(name[-1])
        return p if p < r["start"] else None
    if name.startswith("preans_slot"):
        p = g["start"] + int(name[-1])
        return p if p < g["end"] else None
    if name == "q_last":
        return q["end"] - 1 if q else None
    raise ValueError(name)

POSITIONS = ([f"preresp_slot{i}" for i in range(6)]
             + [f"postresp_slot{i}" for i in range(4)]
             + [f"preans_slot{i}" for i in range(3)] + ["q_last"])

lab = {}
for k, v in json.load(open(LABELS)).items():
    lab[(k.split("|")[0], k.split("|")[1])] = v["label"]
man = json.load(open(os.path.join(EXPORT, "manifest.json")))
layers = man["layers"]
lidx = {L: i for i, L in enumerate(layers)}

items = []
for it in man["items"]:
    if it["format"] != "Q1_bare" or "provided_facts" not in it["fact_id"]:
        continue
    v = lab.get((it["fact_id"], it["condition"]))
    if v in ("lie", "truth"):
        items.append((it["seq_id"], v))
nl = sum(1 for _, v in items if v == "lie")
nt = len(items) - nl

# counts[(pos, band, lens)][token] = [n lie items, n truth items]
counts = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
ctx = {}  # (pos) -> (own token, next 3 tokens) from first item where defined
for seq_id, v in items:
    f = json.load(open(os.path.join(EXPORT, seq_id + ".json")))
    vocab = {int(k): w for k, w in f["vocab"].items()}
    ci = 0 if v == "lie" else 1
    for pname in POSITIONS:
        p = pos_of(f, pname)
        if p is None or p >= len(f["tokens"]):
            continue
        if pname not in ctx:
            ctx[pname] = (f["tokens"][p], f["tokens"][p + 1:p + 4])
        for bname, lo, hi in BANDS:
            bidx = [lidx[L] for L in layers if lo <= L <= hi]
            for lens in ("J", "LL"):
                R = f["readout"][lens]
                seen = set()
                for li in bidx:
                    for tid, _pr in R[li][p]:
                        seen.add(vocab[tid].strip().lower())
                seen.discard("")
                for w in seen:
                    counts[(pname, bname, lens)][w][ci] += 1

with open(OUT, "w") as out:
    out.write("# gpt-oss-20b native scout (P4)\n\n")
    out.write(f"Population: stage-1 provided_facts, judge labels, Q1_bare "
              f"sequences — {nl} lie / {nt} truth items (one kept response per "
              f"scenario x condition; 51/49 effective scenarios). Unconditional "
              f"on the self-report; the P4 said-Yes/said-No split columns are "
              f"unavailable (self-report answers unrecoverable on this model).\n\n"
              f"Count = items whose top-16 readout at the position contains the "
              f"token at >=1 band layer. NEXT-TOKEN AWARENESS: each address "
              f"header lists the own token and the next three tokens; a "
              f"candidate matching any of them (or a >=3-char shared-prefix "
              f"variant, plus the documented rule holes: cross-script, "
              f"punctuation-prefixed, <3-char, prefix-added) is routing, not "
              f"content.\n\n")
    for pname in POSITIONS:
        if pname not in ctx:
            continue
        own, nxt = ctx[pname]
        for bname, lo, hi in BANDS:
            for lens in ("J", "LL"):
                tab = counts.get((pname, bname, lens))
                if not tab:
                    continue
                sep = sorted(tab.items(),
                             key=lambda kv: (-abs(kv[1][0] - kv[1][1]),
                                             -(kv[1][0] + kv[1][1])))
                top = sorted(tab.items(),
                             key=lambda kv: -(kv[1][0] + kv[1][1]))[:15]
                out.write(f"## {pname} · {bname} L{lo}-{hi} · {lens} "
                          f"(own {own!r}; next {nxt!r})\n\n")
                out.write(f"most separating (token: lie/{nl} truth/{nt}): "
                          + " ".join(f"{w}:{c[0]}/{c[1]}"
                                     for w, c in sep[:25]
                                     if abs(c[0] - c[1]) >= 5) + "\n\n")
                out.write("most frequent: "
                          + " ".join(f"{w}:{c[0]}/{c[1]}" for w, c in top)
                          + "\n\n")
print(f"wrote {OUT} ({nl} lie / {nt} truth)")
