#!/usr/bin/env bash
set -euo pipefail
umask 077
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
[ "$#" -eq 2 ] || { echo 'HOLD=USAGE_START_REQUIRES_DEPENDENCY_RECEIPT_AND_RECOVERY_DESCRIPTOR'; exit 2; }
export SIGMA_DEPENDENCY_RECEIPT="$1"
"$HERE/control/start_preflight.sh"
"$HERE/host/survival_supervisor.sh" "$2"
