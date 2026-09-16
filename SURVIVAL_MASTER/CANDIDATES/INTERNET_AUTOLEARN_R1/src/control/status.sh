#!/usr/bin/env bash
set -euo pipefail
[ "$#" -eq 1 ] || { echo 'HOLD=RECOVERY_DESCRIPTOR_REQUIRED'; exit 2; }
D="$1"
[ -f "$D" ] || { echo 'STATUS=DESCRIPTOR_MISSING'; exit 2; }
awk -F= '/^(WORK_ID|COMPLETION_RECEIPT|RECOVERY_LOCK_PATH|LAST_COMMITTED_CHECKPOINT|INFLIGHT_OP_ID|CANONICAL_MUTATION)=/{print}' "$D"
C="$(awk -F= '$1=="COMPLETION_RECEIPT"{sub(/^[^=]*=/,"");print;exit}' "$D")"
if [ -n "$C" ] && [ -f "$C" ]; then echo 'TASK_STATE=COMPLETE'; else echo 'TASK_STATE=UNFINISHED_OR_UNKNOWN'; fi
