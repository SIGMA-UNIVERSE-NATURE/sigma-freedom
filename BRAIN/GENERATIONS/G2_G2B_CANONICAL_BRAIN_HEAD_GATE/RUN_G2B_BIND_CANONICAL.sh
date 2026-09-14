#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

SIGMA_G2B_DIR="$(cd "$(dirname "$0")" && pwd)"
SIGMA_G2B_RUNTIME_ROOT="${1:-${HOME}/SIGMA/sigma_genesis1}"
if [ "$#" -gt 0 ]; then
  shift
fi

exec python "$SIGMA_G2B_DIR/g2b_bind_canonical_root.py" "$SIGMA_G2B_RUNTIME_ROOT" "$@"
