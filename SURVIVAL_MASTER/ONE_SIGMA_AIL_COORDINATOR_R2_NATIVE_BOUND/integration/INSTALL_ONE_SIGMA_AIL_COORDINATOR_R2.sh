#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="${1:?ROOT required}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DST="$ROOT/.sigma_ail/coordination/control"
R1_CANON="$ROOT/.sigma_ail/coordination/CANONICAL"
if [ -s "$R1_CANON/BRAIN_HEAD" ] || [ -s "$R1_CANON/MODEL_GENERATION" ]; then
  echo "INSTALL=REJECT"
  echo "REASON=PARALLEL_R1_CANONICAL_STATE_PRESENT"
  echo "NO_STATE_FORK=MANDATORY"
  exit 90
fi
mkdir -p "$DST"
cp "$HERE/control/SIGMA_AIL_BRAIN_COORDINATOR_R2.sh" "$DST/SIGMA_AIL_BRAIN_COORDINATOR_R2.sh"
chmod 755 "$DST/SIGMA_AIL_BRAIN_COORDINATOR_R2.sh"
printf '%s\n' '2' > "$ROOT/.sigma_ail/coordination/COORDINATOR_VERSION"
echo "ONE_SIGMA_AIL_COORDINATOR_R2_INSTALL=PASS"
echo "COORDINATOR=$DST/SIGMA_AIL_BRAIN_COORDINATOR_R2.sh"
echo "CANONICAL_HEAD_SOURCE=$ROOT/.sigma_ail/BRAIN_HEAD"
echo "CANONICAL_WRITER_SOURCE=$ROOT/.sigma_ail/WRITER.lock"
echo "CANONICAL_MODEL_GENERATION_SOURCE=$ROOT/.sigma_ail/MODEL_GENERATION"
echo "AUTO_START=NO"
echo "HOST_COGNITION=NO"
echo "NO_STATE_FORK=MANDATORY"
