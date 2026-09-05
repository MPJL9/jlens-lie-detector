#!/bin/bash
# Download and unpack the full readout exports (one tar.gz per export dir) into exports/.
# Every scorer in families/ and baselines/ reads exports/<slug>/manifest.json plus the
# per-transcript JSONs; the viewer lists whatever is unpacked here.
#
#   bash exports/fetch_full_exports.sh            # everything (about 1.7 GB compressed)
#   bash exports/fetch_full_exports.sh qwen3_6_27b__c3_g0_k16 gemma_3_12b_it__c3_g0_k16
#
# The archives are hosted on a Hugging Face dataset repo; override BASE_URL for a mirror.
set -euo pipefail
HF_REPO="${HF_REPO:-Sakarein/jlens-lie-detector-exports}"
BASE_URL="${BASE_URL:-https://huggingface.co/datasets/$HF_REPO/resolve/main}"
ALL="qwen3_6_27b__c3_g0_k16 gemma_3_12b_it__c3_g0_k16 gemma_3_27b_it__c3_g0_k16 gpt_oss_20b \
     qwen3_6_27b__c3_q9 gemma_3_12b_it__c3_q9 gemma_3_27b_it__c3_q9"
cd "$(dirname "$0")"
for slug in ${@:-$ALL}; do
  if [ -f "$slug/manifest.json" ]; then echo "$slug: already present"; continue; fi
  echo "fetching $slug.tar.gz"
  curl -L --fail --progress-bar -o "$slug.tar.gz" "$BASE_URL/$slug.tar.gz"
  tar -xzf "$slug.tar.gz" && rm "$slug.tar.gz"
  echo "$slug: $(ls "$slug"/*.json | wc -l | tr -d ' ') files"
done
# refresh the viewer's model list
python3 - <<'PY'
import json, os
idx = sorted(d for d in os.listdir(".") if os.path.exists(os.path.join(d, "manifest.json")))
json.dump(idx, open("index.json", "w")); print("exports/index.json:", idx)
PY
