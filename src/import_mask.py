#!/usr/bin/env python3
"""Import cais/MASK (binary splits) into data/mask_<split>.jsonl.

MASK (Model Alignment between Statements and Knowledge) rows carry a pressure
system prompt, a user question that forces a one-word yes/no answer, a neutral
belief-elicitation question with <final_answer> tags, the proposition and its
ground truth. We keep the fields needed by build_transcripts --source mask.
Only rows with type == "binary" are kept.
"""

from __future__ import annotations

import argparse
import io
import json
import urllib.request

BASE = "https://huggingface.co/datasets/cais/MASK/resolve/main/{split}/test-00000-of-00001.parquet"

# short names -> actual MASK config names (checked 2026-08-24)
ALIASES = {"doubling_down": "doubling_down_known_facts"}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--splits", nargs="+", default=["known_facts"])
    args = ap.parse_args()
    import pandas as pd
    for split in args.splits:
        split = ALIASES.get(split, split)
        df = pd.read_parquet(io.BytesIO(urllib.request.urlopen(BASE.format(split=split)).read()))
        rows = []
        for _, r in df.iterrows():
            if r.get("type") != "binary":
                continue
            row = dict(
                id=f"mask_{split}_{r['task_id']}",
                system=r["system_prompt"], user_prompt=r["user_prompt"],
                belief_q=r["belief_elicit_1"] if "belief_elicit_1" in df.columns else None,
                proposition=r["proposition"],
                ground_truth=r["ground_truth"],
                formatted_ground_truth=r.get("formatted_ground_truth"),
            )
            # doubling_down: turn-1 user prompt + scripted assistant lie precede
            # the pressured turn-2 question
            if "dd_turn_1_prompt" in df.columns:
                row["prior_turns"] = [
                    {"role": "user", "content": r["dd_turn_1_prompt"]},
                    {"role": "assistant", "content": r["dd_turn_1_response"]},
                ]
            rows.append(row)
        if not rows:
            print(f"{split}: no binary scenarios — skipped")
            continue
        out = f"data/mask_{split}.jsonl"
        with open(out, "w") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"{split}: {len(rows)} binary scenarios -> {out}")


if __name__ == "__main__":
    main()
