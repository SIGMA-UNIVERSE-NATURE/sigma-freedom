#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

SIGMA_G5B_DIR="$(cd "$(dirname "$0")" && pwd)"
SIGMA_RUNTIME_ROOT="${1:-${HOME}/SIGMA/sigma_genesis1}"
if [ "$#" -gt 0 ]; then
  shift
fi

exec python "$SIGMA_G5B_DIR/runner/g5b_mechanical_audit.py" "$SIGMA_G5B_DIR" "$SIGMA_RUNTIME_ROOT" "$@"
