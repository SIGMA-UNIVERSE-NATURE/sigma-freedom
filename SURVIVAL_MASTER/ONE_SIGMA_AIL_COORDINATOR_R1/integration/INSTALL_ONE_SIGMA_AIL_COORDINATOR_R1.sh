#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail
ROOT="${1:?ROOT required}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
DST="$ROOT/.sigma_ail/coordination/control"
mkdir -p "$DST"
cp "$HERE/control/SIGMA_AIL_BRAIN_COORDINATOR_R1.sh" "$DST/SIGMA_AIL_BRAIN_COORDINATOR_R1.sh"
chmod 700 "$DST/SIGMA_AIL_BRAIN_COORDINATOR_R1.sh"
echo "ONE_SIGMA_AIL_COORDINATOR_INSTALL=PASS"
echo "COORDINATOR=$DST/SIGMA_AIL_BRAIN_COORDINATOR_R1.sh"
echo "AUTO_START=NO"
echo "HOST_COGNITION=NO"
echo "NO_STATE_FORK=MANDATORY"
