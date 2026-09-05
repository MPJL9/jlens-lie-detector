#!/usr/bin/env python3
"""Derive the variant-arm scenario subset from a completed G0 stage-1 run.

Selection rule (deterministic): scenarios with a same-prompt truth/lie PAIR
first, then scenarios with any kept row, each group sorted by id, capped at
--n. The output JSON id list is consumed by build_transcripts --scenario-ids
(arms G1-G4) and cache_activations --variant-scenarios (G0 variant formats).

    python3 src/make_subset.py --transcripts runs/<slug>/transcripts.jsonl \
        --n 150 --out runs/<slug>/variant_scenarios.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import read_jsonl  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--transcripts", required=True)
    ap.add_argument("--n", type=int, default=150)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    rows = [r for r in read_jsonl(args.transcripts) if r.get("keep")]
    paired = sorted({r["fact_id"] for r in rows if r.get("paired")})
    single = sorted({r["fact_id"] for r in rows} - set(paired))
    ids = (paired + single)[:args.n]
    json.dump(ids, open(args.out, "w"), indent=0)
    print(f"SUBSET: {len(paired)} paired + {len(single)} single kept scenarios "
          f"-> {len(ids)} selected (cap {args.n}) -> {args.out}")


if __name__ == "__main__":
    main()
