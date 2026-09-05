#!/usr/bin/env python3
"""Fetch the external assets used by the "Did You Lie" (DYL) probe baseline.

Neither asset is redistributed in this repository:
  * the released per-model probes (huggingface ai-safety-institute/dyl-<model>,
    MIT) -> data/dyl_probes/<repo-name>/{probe.pt, sweep.json, README.md};
    probe.pt is the checkpoint named `default_filename` in that repo's sweep.json;
  * AISI's lie-detection rollouts (huggingface dataset
    ai-safety-institute/lie-detection-rollouts, licence "other") ->
    data/dyl_rollouts/<config>__<split>.parquet, plus the 120-row samples
    (60 lie + 60 honest) that baselines/dyl_probe_replication_check.py reads,
    rebuilt row-for-row from data/dyl_rollouts_sample_index.json.

Usage: python3 baselines/download_dyl_data.py [--probes-only | --rollouts-only]
"""
import argparse, json, os, shutil

from huggingface_hub import hf_hub_download

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBES = ["dyl-qwen-qwen3.6-27b", "dyl-google-gemma-3-27b-it",
          "dyl-google-gemma-3-12b-it", "dyl-openai-gpt-oss-20b"]
ROLLOUTS = "ai-safety-institute/lie-detection-rollouts"
CONFIGS = ["google-gemma-3-12b-it", "google-gemma-3-27b-it", "qwen-qwen3.6-27b", "openai-gpt-oss-20b"]
SPLITS = ["dyl_train_city_countries", "dyl_validate_varied_deception"]


def fetch_probes():
    for name in PROBES:
        out = os.path.join(ROOT, "data", "dyl_probes", name)
        os.makedirs(out, exist_ok=True)
        repo = f"ai-safety-institute/{name}"
        for fn in ("README.md", "sweep.json"):
            shutil.copy(hf_hub_download(repo, fn), os.path.join(out, fn))
        default = json.load(open(os.path.join(out, "sweep.json")))["default_filename"]
        if not default.endswith(".pt"):
            default += ".pt"
        shutil.copy(hf_hub_download(repo, default), os.path.join(out, "probe.pt"))
        print(f"{name}: probe.pt = {default}")


def fetch_rollouts():
    import pandas as pd
    index = json.load(open(os.path.join(ROOT, "data", "dyl_rollouts_sample_index.json")))
    out_dir = os.path.join(ROOT, "data", "dyl_rollouts")
    os.makedirs(out_dir, exist_ok=True)
    for cfg in CONFIGS:
        for split in SPLITS:
            key = f"{cfg}__{split}"
            pq = os.path.join(out_dir, f"{key}.parquet")
            if not os.path.exists(pq):
                shutil.copy(hf_hub_download(ROLLOUTS, f"{cfg}/{split}.parquet", repo_type="dataset"), pq)
            write_sample(pq, index[key], os.path.join(out_dir, f"{key}__sample120.jsonl"))
            print(f"{key}: parquet + sample120 ({len(index[key])} rows)")


def _as_dict(m):
    """One chat message as stored by pyarrow: a dict, a mapping-like struct, or JSON text."""
    if isinstance(m, dict):
        return {k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in m.items()}
    if isinstance(m, str):
        return json.loads(m)
    if hasattr(m, "items"):
        return {k: v for k, v in m.items()}
    return json.loads(json.dumps(m, default=str))


def write_sample(parquet_path, rows, out_path):
    """rows = [[row_index, 'lie'|'honest'], ...] in the order the sample was drawn."""
    import pandas as pd
    df = pd.read_parquet(parquet_path)
    with open(out_path, "w") as f:
        for row_index, label in rows:
            r = df.iloc[row_index]
            # is_lie is stored as a bool in some splits and as "lie"/"honest" text in others
            got = "lie" if str(r["is_lie"]).strip().lower() in ("true", "lie", "1") else "honest"
            assert got == label, (parquet_path, row_index, got, label)
            msgs = r["messages"]
            if isinstance(msgs, str):      # the column holds the message list as JSON text
                msgs = json.loads(msgs)
            msgs = [_as_dict(m) for m in msgs]
            f.write(json.dumps({"row_index": int(row_index), "is_lie": label,
                                "lie_reason": r["lie_reason"], "messages": msgs},
                               ensure_ascii=False) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--probes-only", action="store_true")
    ap.add_argument("--rollouts-only", action="store_true")
    a = ap.parse_args()
    if not a.rollouts_only:
        fetch_probes()
    if not a.probes_only:
        fetch_rollouts()
