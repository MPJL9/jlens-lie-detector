#!/usr/bin/env python3
"""UNIFIED family scoring pipeline (binding report format, plan §3).

One fixed computation for every model and family. Per family × cell ×
address (single position × layer band — never pooled), the row reports:
  n (lie/truth) · J AUROC · LL AUROC (identical address and vocabulary) ·
  J-visibility and LL-visibility (fraction of cell items whose top-16
  readout contains >=1 family word, either side) · per-source AUROCs ·
  response-answer companion · CV-AUROC (20 scenario-grouped half-splits,
  per-word Fisher p<.05 selection on the training half, presence score on
  the held-out half; mean±sd and split count).
Labels: judge_final_labels.json (judge verdict; ambiguous excluded).
Score: presence count — each word contributes at most 1 per item;
two-sided families score lie-side minus truth-side; higher = lie.

Usage: python3 families/score_families.py --spec <spec.json>
Spec: [{model, export, labels, transcripts, cells:[{name, formats,
answer_label|null, sources}], families:[{name, lie, truth,
addresses:[[pos, lo, hi], ...]}]}]
"""
import argparse, collections, json, math, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
        # slot0 is defined as the turn-end marker in every model's slot map;
        # anchor there (stray prompt-tail tokens can precede it in the crop —
        # observed on 12/924 gpt-oss items; on Gemma/Qwen the marker is always
        # at index 1, so this reproduces the old 1+N behavior exactly)
        u = seg(f, "user_prompt")
        start = u["end"] if u else 1
        anchor = start
        for i in range(start, r["start"]):
            if f["tokens"][i] in ("<end_of_turn>", "<|im_end|>", "<|end|>"):
                anchor = i
                break
        p = anchor + int(name[-1])
        return p if p < r["start"] else None
    if name.startswith("preans_slot"):
        p = g["start"] + int(name[-1])
        return p if p < g["end"] else None
    if name.startswith("think_slot"):
        p = g["start"] + 5 + int(name[-1])
        return p if p < g["end"] else None
    if name == "q_last":
        return q["end"] - 1 if q else None
    raise ValueError(name)

def era_of(pname):
    # trace = exists before the self-report question does; elicited = question onward
    return "trace" if pname.startswith(("preresp", "postresp")) else "elicited"

def auroc(pos, neg):
    if not pos or not neg:
        return None
    n = 0.0
    for a in pos:
        for b in neg:
            n += 1.0 if a > b else (0.5 if a == b else 0.0)
    return n / (len(pos) * len(neg))

def fisher_p(a, b, c, d):
    n, K, N1 = a + b + c + d, a + b, a + c
    hi = min(K, N1)
    denom = math.comb(n, N1)
    return sum(math.comb(K, x) * math.comb(n - K, N1 - x) for x in range(a, hi + 1)) / denom

def fmt(x):
    return "--" if x is None else f"{x:.3f}"

def run_block(block, primary="J"):
    twin = "LL" if primary == "J" else "J"
    exp = os.path.join(ROOT, block["export"])
    lab = {}
    for k, v in json.load(open(os.path.join(ROOT, block["labels"]))).items():
        lab[(k.split("|")[0], k.split("|")[1])] = v["label"]
    resp_ans = {}
    for l in open(os.path.join(ROOT, block["transcripts"])):
        r = json.loads(l)
        # "answer_said" is the parsed polarity of the model's first response;
        # "answer" in transcripts.jsonl is the scenario's HONEST answer (both
        # conditions carry the same value), so it must not be used here
        resp_ans[(r["fact_id"], r["condition"])] = r.get("answer_said")
    man = json.load(open(os.path.join(exp, "manifest.json")))
    layers = man["layers"]
    lidx = {L: i for i, L in enumerate(layers)}
    fam_vocab = {w.lower() for fam in block["families"]
                 for side in (fam["lie"], fam.get("truth", [])) for w in side}
    addr_list = sorted({(a[0], (a[1], a[2])) for fam in block["families"]
                        for a in fam["addresses"]})

    print(f"\n## {block['model']}  (export {block['export']}; judge labels; "
          f"primary lens {primary}, twin {twin})")
    for cell in block["cells"]:
        # stage semantics (corrected 2026-08-27): stage 1 = UNCONDITIONAL on
        # the self-report (answer_label must be null); stage 2 = conditioned
        # on the self-report answer (answer_label required; "no" = primary).
        stage = cell["stage"]
        if stage == 1 and cell.get("answer_label"):
            raise SystemExit(f"SPEC ERROR: stage-1 cell {cell['name']} must be "
                             "unconditional on the self-report (answer_label null)")
        if stage == 2 and not cell.get("answer_label"):
            raise SystemExit(f"SPEC ERROR: stage-2 cell {cell['name']} must "
                             "declare the self-report answer it conditions on")
        items = []
        n_amb = 0
        for it in man["items"]:
            if it["format"] not in cell["formats"]:
                continue
            if cell.get("answer_label") and it["answer_label"] != cell["answer_label"]:
                continue
            if cell.get("resp_answer") and \
               resp_ans.get((it["fact_id"], it["condition"])) != cell["resp_answer"]:
                continue
            src = "pf" if "provided_facts" in it["fact_id"] else "dd"
            if src not in cell["sources"]:
                continue
            v = lab.get((it["fact_id"], it["condition"]))
            if v not in ("lie", "truth"):
                n_amb += 1
                continue
            f = json.load(open(os.path.join(exp, it["seq_id"] + ".json")))
            vocab = {int(k): w for k, w in f["vocab"].items()}
            rec = {"label": v, "src": src, "scenario": it["fact_id"],
                   "resp_ans": resp_ans.get((it["fact_id"], it["condition"])),
                   "sets": {}}
            for pname, band in addr_list:
                p = pos_of(f, pname)
                if p is None or p >= len(f["tokens"]):
                    continue
                bidx = [lidx[L] for L in layers if band[0] <= L <= band[1]]
                for lens in ("J", "LL"):
                    R = f["readout"][lens]
                    seen = set()
                    for li in bidx:
                        for t, _pr in R[li][p]:
                            w = vocab[t].strip().lower()
                            if w in fam_vocab:
                                seen.add(w)
                    rec["sets"][(pname, band, lens)] = seen
            items.append(rec)
        nl = sum(r["label"] == "lie" for r in items)
        nt = len(items) - nl
        sl = len({r["scenario"] for r in items if r["label"] == "lie"})
        st = len({r["scenario"] for r in items if r["label"] == "truth"})
        cond = []
        if stage == 1:
            cond.append("UNCONDITIONAL on self-report; interpretation restricted "
                        "to trace addresses (P6), elicited rows diagnostic")
        else:
            cond.append(f"self-report answer = {cell['answer_label']} (constant in cell)")
        if cell.get("resp_answer"):
            cond.append(f"response answer = {cell['resp_answer']}")
        cond = "; ".join(cond)
        floor = "" if (nl >= 15 and nt >= 15) else \
            "  **→ BELOW ~15/side FLOOR — leads, not results**"
        print(f"\n### [stage {stage}] cell {cell['name']}: {nl} lie / {nt} truth items "
              f"from {sl} / {st} effective scenarios "
              f"(sources {'+'.join(cell['sources'])}; {n_amb} label-excluded; "
              f"conditioning: {cond}){floor}")
        multi_src = len(cell["sources"]) > 1
        src_hdr = "pf | dd | " if multi_src else ""
        print(f"| family | address | era | {primary} | {twin} | "
              f"{primary}-vis l/t | {twin}-vis l/t | "
              f"{src_hdr}companion | CV |")
        print("|---" * (9 + (2 if multi_src else 0)) + "|")
        rng = random.Random(20260827)
        for fam in block["families"]:
            lw = [w.lower() for w in fam["lie"]]
            tw = [w.lower() for w in fam.get("truth", [])]
            for a in fam["addresses"]:
                pname, band = a[0], (a[1], a[2])
                def sc(rec, lens):
                    s = rec["sets"].get((pname, band, lens), set())
                    return sum(w in s for w in lw) - sum(w in s for w in tw)
                def vis(rec, lens):
                    s = rec["sets"].get((pname, band, lens), set())
                    return any(w in s for w in lw + tw)
                aj = auroc([sc(r, primary) for r in items if r["label"] == "lie"],
                           [sc(r, primary) for r in items if r["label"] == "truth"])
                al = auroc([sc(r, twin) for r in items if r["label"] == "lie"],
                           [sc(r, twin) for r in items if r["label"] == "truth"])
                jv = [sum(vis(r, primary) for r in items if r["label"] == c) for c in ("lie", "truth")]
                lv = [sum(vis(r, twin) for r in items if r["label"] == c) for c in ("lie", "truth")]
                srcs = {}
                for s in ("pf", "dd"):
                    sub = [r for r in items if r["src"] == s]
                    srcs[s] = auroc([sc(r, primary) for r in sub if r["label"] == "lie"],
                                    [sc(r, primary) for r in sub if r["label"] == "truth"])
                comp = auroc([sc(r, primary) for r in items if r["resp_ans"] == "yes"],
                             [sc(r, primary) for r in items if r["resp_ans"] == "no"])
                scens = sorted({r["scenario"] for r in items})
                cvs = []
                for _ in range(20):
                    rng.shuffle(scens)
                    half = set(scens[: len(scens) // 2])
                    tr = [r for r in items if r["scenario"] in half]
                    te = [r for r in items if r["scenario"] not in half]
                    n_l = sum(r["label"] == "lie" for r in tr)
                    n_t = len(tr) - n_l
                    if n_l < 3 or n_t < 3 or not te:
                        continue
                    kl, kt = [], []
                    for w in lw + tw:
                        ca = sum(w in r["sets"].get((pname, band, primary), set())
                                 and r["label"] == "lie" for r in tr)
                        cc = sum(w in r["sets"].get((pname, band, primary), set())
                                 and r["label"] == "truth" for r in tr)
                        if w in lw and fisher_p(ca, n_l - ca, cc, n_t - cc) < 0.05:
                            kl.append(w)
                        if w in tw and fisher_p(cc, n_t - cc, ca, n_l - ca) < 0.05:
                            kt.append(w)
                    if not kl and not kt:
                        continue
                    def cvsc(r):
                        s = r["sets"].get((pname, band, primary), set())
                        return sum(w in s for w in kl) - sum(w in s for w in kt)
                    v = auroc([cvsc(r) for r in te if r["label"] == "lie"],
                              [cvsc(r) for r in te if r["label"] == "truth"])
                    if v is not None:
                        cvs.append(v)
                cvm = sum(cvs) / len(cvs) if cvs else None
                cvsd = (sum((x - cvm) ** 2 for x in cvs) / len(cvs)) ** 0.5 if cvs else None
                src_txt = f"{fmt(srcs['pf'])} | {fmt(srcs['dd'])} | " if multi_src else ""
                print(f"| {fam['name']} | {pname} L{band[0]}-{band[1]} | {era_of(pname)} "
                      f"| {fmt(aj)} | {fmt(al)} "
                      f"| {jv[0]}/{nl} {jv[1]}/{nt} | {lv[0]}/{nl} {lv[1]}/{nt} "
                      f"| {src_txt}{fmt(comp)} "
                      f"| {fmt(cvm)}±{fmt(cvsd) if cvsd is not None else '--'} [{len(cvs)}] |")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--primary-lens", default="J", choices=["J", "LL"],
                    help="lens whose readout drives score, CV, companion; "
                         "the other lens is the twin column")
    args = ap.parse_args()
    for block in json.load(open(args.spec)):
        run_block(block, args.primary_lens)

if __name__ == "__main__":
    main()
