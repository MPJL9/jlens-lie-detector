#!/usr/bin/env python3
"""Stage 4 — aggregate the per-sequence exports into the Experiment-0 summary
(plan §7, §11): layer x position heatmaps of the Yes-vs-No score for truthful
vs deceptive transcripts, per-layer AUROC at P0 / P2 / P3 for J-lens vs logit
lens, behavioral self-report accuracy, and top-k J-lens tokens for a handful of
transcripts.

Reads  exports/<slug>/manifest.json + <seq_id>.json
Writes exports/<slug>/aggregate.json   (consumed by viewer/index.html)
       exports/<slug>/figures/*.png
       exports/<slug>/REPORT.md

Aggregation columns. Sequences differ in length (different facts/responses),
so heatmaps are aligned on the self-report segment, which is token-identical
within a format: columns = [P0] + tokens from the start of the self-report
question through P2 (gen-prompt end) + [P3]. The score s at P2 of the FINAL
layer is the model's own output logit difference (baseline 1).
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import MODELS, model_slug  # noqa: E402
from prompts import LIE_MEANS  # noqa: E402

LENSES = ["J", "LL"]


def auroc(pos: list[float], neg: list[float]) -> float | None:
    """AUROC of score for pos (lie) vs neg (truth); None if a class is empty."""
    if not pos or not neg:
        return None
    from sklearn.metrics import roc_auc_score
    y = [1] * len(pos) + [0] * len(neg)
    s = list(pos) + list(neg)
    if len(set(s)) < 2:
        return 0.5
    return float(roc_auc_score(y, s))


def nan_to_none(x):
    """Recursively replace float NaN/inf with None so the JSON is browser-valid."""
    if isinstance(x, float):
        return None if (math.isnan(x) or math.isinf(x)) else x
    if isinstance(x, dict):
        return {k: nan_to_none(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [nan_to_none(v) for v in x]
    return x


def ans_label(it) -> str:
    t = it["answer_text"].strip().lower().lstrip("*\"'")
    return "yes" if t.startswith("yes") else ("no" if t.startswith("no") else "other")


def cohens_d(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """per-cell Cohen's d of a (lie) minus b (truth); arrays [n, L, C]."""
    ma, mb = a.mean(0), b.mean(0)
    va, vb = a.var(0, ddof=1) if len(a) > 1 else 0 * ma, b.var(0, ddof=1) if len(b) > 1 else 0 * mb
    na, nb = len(a), len(b)
    sp = np.sqrt(((na - 1) * va + (nb - 1) * vb) / max(na + nb - 2, 1)) + 1e-6
    return (ma - mb) / sp


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="gemma-3-4b-it", choices=sorted(MODELS))
    ap.add_argument("--tag", default="", help="suffix for runs/exports dirs: <slug>__<tag>")
    ap.add_argument("--exports", default=None)
    ap.add_argument("--n-examples", type=int, default=10)
    ap.add_argument("--no-figures", action="store_true")
    args = ap.parse_args()
    slug = model_slug(args.model) + (f"__{args.tag}" if args.tag else "")
    exp = args.exports or f"exports/{slug}"
    mf = json.load(open(f"{exp}/manifest.json"))
    layers = mf["layers"]
    items = [json.load(open(f"{exp}/{m['seq_id']}.json")) for m in mf["items"]]
    by_fmt = defaultdict(list)
    for it in items:
        by_fmt[it["format"]].append(it)

    agg = dict(model=mf["model"], slug=slug, layers=layers, lenses=LENSES,
               yes_tokens=mf["yes_tokens"], no_tokens=mf["no_tokens"], formats={})
    report = [f"# Experiment 0 report — {mf['model']}\n",
              f"layers {layers[0]}–{layers[-1]} · {len(items)} sequences · "
              f"Yes tokens {list(mf['yes_tokens'])} · No tokens {list(mf['no_tokens'])}\n"]

    for fmt, its in sorted(by_fmt.items()):
        if LIE_MEANS.get(fmt, "yes") is None:
            # free-text / prefilled formats (R_open, P_stem, P_punct, B1_prefill):
            # no Yes/No self-report semantics — readout-only, analyzed offline
            n_t = sum(it["condition"] == "truth" for it in its)
            n_l = sum(it["condition"] == "lie" for it in its)
            report.append(f"\n## format {fmt}\n\n{n_l} lie / {n_t} truth sequences — "
                          f"readout-only format (no Yes/No analysis; see OBSERVATIONS.md).\n")
            agg["formats"][fmt] = dict(self_q=its[0].get("self_q"), lie_means=None,
                                       n=dict(truth=n_t, lie=n_l))
            continue
        sign = 1.0 if LIE_MEANS.get(fmt, "yes") == "yes" else -1.0   # orient: higher = "I lied"
        # --- aligned columns -------------------------------------------
        seg_lens = {it["P2"] - it["P1"][0] + 1 for it in its}
        n_cols_q = min(seg_lens)
        if len(seg_lens) > 1:
            print(f"[{fmt}] WARNING self-report segment lengths differ {sorted(seg_lens)}; "
                  f"right-aligning on P2 with {n_cols_q} columns")
        ref = its[0]
        q_cols = list(range(ref["P2"] - n_cols_q + 1, ref["P2"] + 1))
        col_labels = ["P0"] + [ref["tokens"][c] for c in q_cols] + ["P3"]
        col_kind = ["P0"] + ["q"] * n_cols_q + ["P3"]
        col_kind[n_cols_q] = "P2"     # last q column is P2

        def cols_of(it):
            qs = list(range(it["P2"] - n_cols_q + 1, it["P2"] + 1))
            return [it["P0"]] + qs + [it["P3"]]

        fd = dict(self_q=ref["self_q"], lie_means=LIE_MEANS.get(fmt, "yes"),
                  col_labels=col_labels, col_kind=col_kind, n={}, lenses={},
                  behavior={}, examples=[])
        truth = [it for it in its if it["condition"] == "truth"]
        lie = [it for it in its if it["condition"] == "lie"]
        fd["n"] = dict(truth=len(truth), lie=len(lie))

        # --- behavioral self-report (baseline 1) -----------------------
        lm = LIE_MEANS.get(fmt, "yes")
        not_lm = "no" if lm == "yes" else "yes"
        beh = dict(
            lie_says_lied=sum(it["answer_label"] == lm for it in lie),
            truth_says_truthful=sum(it["answer_label"] == not_lm for it in truth),
            other=sum(it["answer_label"] == "other" for it in its),
            p3_missing=sum(it["P3"] is None for it in its),
            model_logit_auroc=auroc([sign * it["model_yes_minus_no"] for it in lie],
                                    [sign * it["model_yes_minus_no"] for it in truth]),
        )
        fd["behavior"] = beh

        # --- heatmaps + AUROC per lens ---------------------------------
        for lens in LENSES:
            def mat(it):
                cols = cols_of(it)
                S = np.array(it["scores"][lens], dtype=float)          # [L, T]
                M = np.full((len(layers), len(cols)), np.nan)
                for j, c in enumerate(cols):
                    if c is not None:
                        M[:, j] = S[:, c]
                return sign * M
            A_t = np.stack([mat(it) for it in truth]) if truth else np.zeros((0, len(layers), len(col_labels)))
            A_l = np.stack([mat(it) for it in lie]) if lie else np.zeros((0, len(layers), len(col_labels)))
            with np.errstate(invalid="ignore"):
                mt = np.nanmean(A_t, 0) if len(A_t) else np.full(A_t.shape[1:], np.nan)
                ml = np.nanmean(A_l, 0) if len(A_l) else np.full(A_l.shape[1:], np.nan)
            # per-cell AUROC (lie vs truth) and Cohen's d
            L_, C_ = mt.shape
            AU = np.full((L_, C_), np.nan)
            for li in range(L_):
                for cj in range(C_):
                    p = [v for v in A_l[:, li, cj] if not np.isnan(v)]
                    n = [v for v in A_t[:, li, cj] if not np.isnan(v)]
                    a = auroc(p, n)
                    AU[li, cj] = np.nan if a is None else a
            # Cohen's d ignoring NaN rows (P3 missing)
            D = np.full((L_, C_), np.nan)
            for cj in range(C_):
                a = A_l[~np.isnan(A_l[:, 0, cj]), :, cj]
                b = A_t[~np.isnan(A_t[:, 0, cj]), :, cj]
                if len(a) and len(b):
                    D[:, cj] = cohens_d(a[:, :, None], b[:, :, None])[:, 0]
            key_cols = {"P0": 0, "P2": n_cols_q, "P3": len(col_labels) - 1}
            # AUROC-by-layer for three explicit targets (viewer: aggregate tab)
            li_of = {l: i for i, l in enumerate(layers)}
            def tcurves(subset, target):
                out = {}
                for k, posname in (("P0", "P0"), ("P2", "P2"), ("P3", "P3")):
                    curve = []
                    for l in layers:
                        pos_s, ys = [], []
                        for it in subset:
                            p = it[posname]
                            if p is None:
                                continue
                            v = it["scores"][lens][li_of[l]][p]
                            if v is None:
                                continue
                            pos_s.append(sign * v); ys.append(target(it))
                        a = auroc([sv for sv, yv in zip(pos_s, ys) if yv],
                                  [sv for sv, yv in zip(pos_s, ys) if not yv])
                        curve.append(None if a is None else round(a, 4))
                    out[k] = curve
                return out
            answered = [it for it in its if ans_label(it) != "other"]
            said_no = [it for it in answered if ans_label(it) == "no"]
            targets = {
                "lied": dict(n_pos=len(lie), n_neg=len(truth),
                             desc="lie vs truth condition (all items)",
                             **tcurves(its, lambda it: it["condition"] == "lie")),
                "says_yes": dict(n_pos=sum(ans_label(it) == "yes" for it in answered),
                                 n_neg=sum(ans_label(it) == "no" for it in answered),
                                 desc="generated answer is Yes vs No (answered items)",
                                 **tcurves(answered, lambda it: ans_label(it) == "yes")),
                "lied_within_said_no": dict(
                    n_pos=sum(it["condition"] == "lie" for it in said_no),
                    n_neg=sum(it["condition"] == "truth" for it in said_no),
                    desc="lie vs truth among items whose answer was No (answer-controlled)",
                    **tcurves(said_no, lambda it: it["condition"] == "lie")),
            }
            fd["lenses"][lens] = dict(
                truth_mean=np.round(mt, 4).tolist(), lie_mean=np.round(ml, 4).tolist(),
                diff=np.round(ml - mt, 4).tolist(), cohens_d=np.round(D, 3).tolist(),
                auroc=np.round(AU, 4).tolist(),
                auroc_by_layer={k: [None if np.isnan(AU[li, c]) else round(float(AU[li, c]), 4)
                                    for li in range(L_)] for k, c in key_cols.items()},
                best={k: (None if np.all(np.isnan(AU[:, c])) else
                          dict(layer=layers[int(np.nanargmax(AU[:, c]))],
                               auroc=round(float(np.nanmax(AU[:, c])), 4)))
                      for k, c in key_cols.items()},
                targets=targets,
            )
        # --- surface-form confounds at P0 (plan §3.2 / §17) ----------------
        from collections import Counter
        import statistics
        conf = {}
        for cond, grp in (("truth", truth), ("lie", lie)):
            if not grp:
                continue
            lens_chars = [len(it["response"]) for it in grp]
            p0_tok = Counter(it["tokens"][it["P0"]] for it in grp)
            first = Counter(it["response"].split(" ")[0] for it in grp)
            conf[cond] = dict(n=len(grp), resp_chars_median=statistics.median(lens_chars),
                              resp_chars_min=min(lens_chars), resp_chars_max=max(lens_chars),
                              p0_token_top=p0_tok.most_common(5), first_word_top=first.most_common(3))
        # AUROC of sequence length alone (lie vs truth): if this is far from 0.5,
        # any position-dependent readout can separate the classes without
        # reading deception (this killed the first gemma-3-4b run: 1.0).
        # orig_T = full pre-crop length (campaign-2 exports); fall back to token count
        seq_len = lambda it: it.get("orig_T") or len(it["tokens"])
        conf["length_auroc"] = auroc([seq_len(it) for it in lie], [seq_len(it) for it in truth])
        # answer-identity confound (jspace): does WHICH answer the response gives
        # already predict the label? score = response starts with yes
        said_yes = lambda it: 1.0 if it["response"].strip().lower().lstrip('*"\'').startswith("yes") else 0.0
        conf["response_says_yes_auroc"] = auroc([said_yes(it) for it in lie], [said_yes(it) for it in truth])
        fd["confounds"] = conf

        # --- examples: top-k J tokens at P0 and P2 at quartile layers ----
        qlayers = sorted({layers[len(layers) // 4], layers[len(layers) // 2],
                          layers[3 * len(layers) // 4], layers[-2], layers[-1]})
        for it in its[:args.n_examples]:
            ex = dict(seq_id=it["seq_id"], condition=it["condition"],
                      answer_text=it["answer_text"], positions={})
            for pname in ("P0", "P2"):
                p = it[pname]
                ex["positions"][pname] = {
                    str(l): {lens: [[it["vocab"][str(tid)], pr]
                                    for tid, pr in it["readout"][lens][layers.index(l)][p]]
                             for lens in LENSES}
                    for l in qlayers}
            fd["examples"].append(ex)
        agg["formats"][fmt] = fd

        # --- report text -----------------------------------------------
        report.append(f"\n## {fmt} — “{ref['self_q']}”  (lie ⇒ {lm})\n")
        report.append(f"n truth = {len(truth)}, n lie = {len(lie)}\n")
        report.append(f"Behavioral self-report: lies that say “{lm}”: {beh['lie_says_lied']}/{len(lie)} · "
                      f"truths that say “{not_lm}”: {beh['truth_says_truthful']}/{len(truth)} · "
                      f"other: {beh['other']} · P3 missing: {beh['p3_missing']} · "
                      f"model Yes−No logit AUROC at P2: {beh['model_logit_auroc']}\n")
        report.append("\n| lens | best AUROC @P0 (layer) | @P2 (layer) | @P3 (layer) |\n|---|---|---|---|")
        for lens in LENSES:
            b = fd["lenses"][lens]["best"]
            cell = lambda k: "—" if b[k] is None else f"{b[k]['auroc']:.3f} (L{b[k]['layer']})"
            report.append(f"| {lens} | {cell('P0')} | {cell('P2')} | {cell('P3')} |")
        report.append("\nSurface-form check at P0 (response length / last token / first word by condition — "
                      "if these differ, a P0 signal may be style, not deception):\n")
        report.append(f"- **AUROC of sequence length alone (lie vs truth): {conf['length_auroc']}** — "
                      "must be near 0.5 for any position-dependent readout to be interpretable")
        report.append(f"- AUROC of response answer-identity (says-yes) alone: {conf['response_says_yes_auroc']}")
        for cond, c in conf.items():
            if not isinstance(c, dict):
                continue
            report.append(f"- **{cond}** (n={c['n']}): response chars median {c['resp_chars_median']} "
                          f"[{c['resp_chars_min']}–{c['resp_chars_max']}] · P0 token {c['p0_token_top']} · "
                          f"first word {c['first_word_top']}")
        report.append("\nAUROC by layer (J / LL):\n")
        report.append("| layer | P0 J | P0 LL | P2 J | P2 LL | P3 J | P3 LL |\n|---|---|---|---|---|---|---|")
        for li, l in enumerate(layers):
            vals = []
            for k in ("P0", "P2", "P3"):
                for lens in LENSES:
                    v = fd["lenses"][lens]["auroc_by_layer"][k][li]
                    vals.append("—" if v is None else f"{v:.2f}")
            report.append(f"| {l} | " + " | ".join(vals) + " |")
        report.append("\n### Top-k tokens (J-lens | logit lens) at P2 for example transcripts\n")
        for ex in fd["examples"][:6]:
            report.append(f"**{ex['seq_id']}** → answered {ex['answer_text']!r}\n")
            for l, d in ex["positions"]["P2"].items():
                j = ", ".join(f"{t!r}" for t, _ in d["J"][:8])
                ll = ", ".join(f"{t!r}" for t, _ in d["LL"][:8])
                report.append(f"- L{l}: J: {j}  ·  LL: {ll}")
            report.append("")

    json.dump(nan_to_none(agg), open(f"{exp}/aggregate.json", "w"))
    open(f"{exp}/REPORT.md", "w").write("\n".join(report) + "\n")
    print(f"ANALYZE DONE -> {exp}/aggregate.json, {exp}/REPORT.md")

    if not args.no_figures:
        make_figures(agg, f"{exp}/figures")


def make_figures(agg, fig_dir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    os.makedirs(fig_dir, exist_ok=True)
    layers = agg["layers"]
    for fmt, fd in agg["formats"].items():
        if "col_labels" not in fd:      # readout-only formats (R_open, prefills)
            continue
        labels = fd["col_labels"]
        fig, axes = plt.subplots(2, 4, figsize=(4.2 * len(labels) / 8 + 12, 8), constrained_layout=True)
        for r, lens in enumerate(LENSES):
            d = fd["lenses"][lens]
            mats = [("truth mean s", np.array(d["truth_mean"], float), "RdBu_r", True),
                    ("lie mean s", np.array(d["lie_mean"], float), "RdBu_r", True),
                    ("lie − truth", np.array(d["diff"], float), "PuOr_r", True),
                    ("AUROC lie>truth", np.array(d["auroc"], float), "viridis", False)]
            for c, (title, M, cmap, sym) in enumerate(mats):
                ax = axes[r, c]
                if sym:
                    v = np.nanmax(np.abs(M)) if np.isfinite(M).any() else 1
                    im = ax.imshow(M, aspect="auto", cmap=cmap, vmin=-v, vmax=v, origin="lower")
                else:
                    im = ax.imshow(M, aspect="auto", cmap=cmap, vmin=0, vmax=1, origin="lower")
                ax.set_title(f"{lens}: {title}", fontsize=9)
                ax.set_xticks(range(len(labels)))
                ax.set_xticklabels([t.replace("\n", "⏎") for t in labels], rotation=90, fontsize=6)
                ax.set_yticks(range(0, len(layers), max(1, len(layers) // 8)))
                ax.set_yticklabels([layers[i] for i in range(0, len(layers), max(1, len(layers) // 8))], fontsize=7)
                for j, k in enumerate(fd["col_kind"]):
                    if k in ("P0", "P2", "P3"):
                        ax.axvline(j, color="k", lw=0.6, ls=":")
                plt.colorbar(im, ax=ax, fraction=0.04)
        fig.suptitle(f"{agg['model']} · {fmt} · “{fd['self_q']}” · n={fd['n']}", fontsize=10)
        fig.savefig(f"{fig_dir}/heatmap_{fmt}.png", dpi=130)
        plt.close(fig)

        fig, axes = plt.subplots(1, 3, figsize=(12, 3.4), constrained_layout=True, sharey=True)
        for ax, k in zip(axes, ("P0", "P2", "P3")):
            for lens, st in (("J", "-"), ("LL", "--")):
                y = fd["lenses"][lens]["auroc_by_layer"][k]
                ax.plot(layers, [np.nan if v is None else v for v in y], st, label=lens)
            ax.axhline(0.5, color="gray", lw=0.6)
            ax.set_title(f"AUROC at {k}"); ax.set_xlabel("layer"); ax.set_ylim(0, 1.02)
            ax.legend(fontsize=8)
        fig.suptitle(f"{agg['model']} · {fmt}", fontsize=10)
        fig.savefig(f"{fig_dir}/auroc_{fmt}.png", dpi=130)
        plt.close(fig)
    print(f"figures -> {fig_dir}/")


if __name__ == "__main__":
    main()
