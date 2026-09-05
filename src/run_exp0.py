#!/usr/bin/env python3
"""Run Experiment 0 end to end (stages 1-4) for one model.

    python3 src/run_exp0.py --model gemma-3-4b-it
    python3 src/run_exp0.py --model gpt2 --n-facts 3          # smoke test

Stages can be restarted individually: --from {1,2,3,4}. Stage scripts are
plain CLIs (src/build_transcripts.py, cache_activations.py, readout.py,
analyze.py) — see each file's docstring for its outputs.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *extra):
    cmd = [sys.executable, os.path.join(HERE, script), *extra]
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--model", default="gemma-3-4b-it")
    ap.add_argument("--n-facts", type=int, default=None)
    ap.add_argument("--truth-style", default="bare")
    ap.add_argument("--lie-styles", nargs="+", default=None)
    ap.add_argument("--response-source", default="generated", choices=["generated", "prefilled"])
    ap.add_argument("--no-concise", dest="concise", action="store_false")
    ap.add_argument("--concise-style", default="sentence")
    ap.add_argument("--tag", default="")
    ap.add_argument("--source", default="facts")
    ap.add_argument("--scenarios", default=None)
    ap.add_argument("--samples", type=int, default=6)
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--system-suffix", default=None, help="mask arm key (prompts.SYSTEM_SUFFIXES)")
    ap.add_argument("--beliefs-cache", default=None)
    ap.add_argument("--scenario-ids", default=None)
    ap.add_argument("--formats", nargs="+", default=None)
    ap.add_argument("--variant-formats", nargs="*", default=None)
    ap.add_argument("--variant-scenarios", default=None)
    ap.add_argument("--variant-n", type=int, default=150,
                    help="if --variant-scenarios does not exist yet, derive it from "
                         "stage-1 transcripts with this cap (src/make_subset.py)")
    ap.add_argument("--cache-layers", default=None)
    ap.add_argument("--crop-from-segment", default=None)
    ap.add_argument("--append-seqs", action="store_true")
    ap.add_argument("--inversion-n", type=int, default=5)
    ap.add_argument("--top-k", type=int, default=8)
    ap.add_argument("--layer-stride", type=int, default=1)
    ap.add_argument("--device", default=None)
    ap.add_argument("--from", dest="start", type=int, default=1, choices=[1, 2, 3, 4])
    args = ap.parse_args()
    dev = ["--device", args.device] if args.device else []
    tag = ["--tag", args.tag] if args.tag else []
    opt = lambda flag, v: [flag, v] if v else []
    if args.start <= 1:
        run("build_transcripts.py", "--model", args.model, "--truth-style", args.truth_style,
            "--source", args.source, "--samples", str(args.samples), "--temperature", str(args.temperature),
            *(["--n-facts", str(args.n_facts)] if args.n_facts else []),
            *(["--lie-styles", *args.lie_styles] if args.lie_styles else []),
            *opt("--scenarios", args.scenarios), *opt("--system-suffix", args.system_suffix),
            *opt("--beliefs-cache", args.beliefs_cache), *opt("--scenario-ids", args.scenario_ids),
            "--response-source", args.response_source, "--concise-style", args.concise_style,
            *([] if args.concise else ["--no-concise"]), *tag, *dev)
    if args.variant_scenarios and not os.path.exists(args.variant_scenarios):
        from common import model_slug
        slug = model_slug(args.model) + (f"__{args.tag}" if args.tag else "")
        run("make_subset.py", "--transcripts", f"runs/{slug}/transcripts.jsonl",
            "--n", str(args.variant_n), "--out", args.variant_scenarios)
    if args.start <= 2:
        run("cache_activations.py", "--model", args.model, "--inversion-n", str(args.inversion_n),
            *(["--formats", *args.formats] if args.formats else []),
            *(["--variant-formats", *args.variant_formats] if args.variant_formats else []),
            *opt("--variant-scenarios", args.variant_scenarios),
            *opt("--cache-layers", args.cache_layers),
            *opt("--crop-from-segment", args.crop_from_segment),
            *(["--append"] if args.append_seqs else []), *tag, *dev)
    if args.start <= 3:
        run("readout.py", "--model", args.model, "--top-k", str(args.top_k),
            "--layer-stride", str(args.layer_stride), *tag, *dev)
    if args.start <= 4:
        run("analyze.py", "--model", args.model, *tag)


if __name__ == "__main__":
    main()
