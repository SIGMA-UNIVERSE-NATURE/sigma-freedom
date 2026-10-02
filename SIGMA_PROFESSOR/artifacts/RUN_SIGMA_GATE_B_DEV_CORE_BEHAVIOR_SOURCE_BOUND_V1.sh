#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

HERE=$(cd "$(dirname "$0")" && pwd)
PYTHON="${PYTHON:-/data/data/com.termux/files/usr/bin/python3}"
MANIFEST="${SIGMA_GATE_B_MANIFEST:-$HERE/SIGMA_GATE_B_DEV_CORE_BEHAVIOR_SOURCE_BOUND_PREREQUISITES_V1.json}"
RUN_ROOT="${SIGMA_GATE_B_RUN_ROOT:-$HOME/SIGMA_GATE_B_DEV_CORE_BEHAVIOR_PROOF}"

if [ ! -x "$PYTHON" ]; then
    printf 'HOLD=PYTHON3_MISSING_OR_NOT_EXECUTABLE\n'
    exit 20
fi

exec "$PYTHON" "$HERE/run_sigma_gate_b_dev_core_behavior_v1.py" \
  --manifest "$MANIFEST" \
  --run-root "$RUN_ROOT"
