#!/usr/bin/env bash
set -euo pipefail
umask 077
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
[ "${SURVIVAL_REVIEW_VERDICT:-}" = APPROVE_FOR_OPPO_PREFLIGHT_ONLY ] || { echo 'HOLD=SURVIVAL_MASTER_PREFLIGHT_APPROVAL_MISSING'; exit 2; }
[ "$#" -eq 1 ] || { echo 'HOLD=RECOVERY_DESCRIPTOR_REQUIRED'; exit 2; }
"$HERE/control/session_guard.sh"
"$HERE/host/survival_supervisor.sh" "$1"
