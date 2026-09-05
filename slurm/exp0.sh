#!/bin/bash
#SBATCH --job-name=jld_exp0
#SBATCH --partition=short
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --output=slurm/logs/exp0_%j.out
#SBATCH --error=slurm/logs/exp0_%j.err
# Experiment 0, all four stages, for one model. Submitted BY THE USER:
#   MODEL=gemma-3-4b-it sbatch --export=ALL slurm/exp0.sh
#   MODEL=gemma-3-12b-it EXTRA="--n-facts 36" sbatch --export=ALL slurm/exp0.sh
#   MODEL=gemma-3-4b-it TAG=prefilled EXTRA="--response-source prefilled" sbatch --export=ALL slurm/exp0.sh
# Pass env vars via the shell prefix, never inside --export (comma-splitting).
# Needs a HF token with Gemma access at $HF_HOME/token.
#
# GPU override (sbatch CLI options beat the #SBATCH headers above):
#   27B needs an 80GB card — the SBATCH default gres l40s (48GB) will NOT load it:
#   MODEL=gemma-3-27b-it ... sbatch --gres=gpu:a100:1 --mem=120G --export=ALL slurm/exp0.sh
#   (clusters with both 40GB and 80GB A100 nodes: add the 80GB feature constraint
#    from `sinfo -o "%P %G %f"` if a plain a100 request can land on a 40GB card.
#    A mis-landed job fails at model load within minutes.)
set -euo pipefail
export PYTHONUNBUFFERED=1
ROOT="${JLENS_ROOT:?set JLENS_ROOT to the repo checkout on the cluster}"
export HF_HOME="${HF_HOME:-$ROOT/hf_cache}"
cd "$ROOT"
source env/bin/activate
[ -n "${SLURM_JOB_ID:-}" ] && python3 -c "import torch,sys; sys.exit(not torch.cuda.is_available())"
: "${MODEL:?set MODEL=<registry name, e.g. gemma-3-4b-it>}"
FROM="${FROM:-1}"
echo "MODEL=$MODEL FROM=$FROM EXTRA=${EXTRA:-} host=$(hostname) gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader)"
python3 src/run_exp0.py --model "$MODEL" --from "$FROM" --device cuda ${TAG:+--tag $TAG} ${EXTRA:-}
echo "EXP0 DONE ($MODEL)"
