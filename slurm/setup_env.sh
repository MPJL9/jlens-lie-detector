#!/bin/bash
#SBATCH --job-name=jld_env
#SBATCH --partition=short
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:30:00
#SBATCH --output=slurm/logs/setup_env_%j.out
#SBATCH --error=slurm/logs/setup_env_%j.err
# One-time env build for the J-lens lie-detector project (mirrors jlens_mm's
# setup: venv on scratch, torch cu128 build for the CUDA-12.9 driver, jlens
# installed editable from a vendor clone). Rerunnable. Submitted BY THE USER.
set -euo pipefail
export PYTHONUNBUFFERED=1
ROOT="${JLENS_ROOT:?set JLENS_ROOT to the repo checkout on the cluster}"
export HF_HOME="${HF_HOME:-$ROOT/hf_cache}"
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-$ROOT/pip_cache}"
mkdir -p "$ROOT"/{vendor,runs,exports,slurm/logs} "$HF_HOME" "$PIP_CACHE_DIR"
cd "$ROOT"
module load miniconda/3
[ -d env ] || python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install torch --index-url https://download.pytorch.org/whl/cu128
pip install -r requirements.txt
[ -d vendor/jacobian-lens ] || git clone https://github.com/anthropics/jacobian-lens vendor/jacobian-lens
pip install -e vendor/jacobian-lens
python - <<'PY'
import torch, transformers, jlens
print("jlens OK:", jlens.__all__)
print("torch", torch.__version__, "cuda", torch.version.cuda, "avail", torch.cuda.is_available())
print("transformers", transformers.__version__)
PY
