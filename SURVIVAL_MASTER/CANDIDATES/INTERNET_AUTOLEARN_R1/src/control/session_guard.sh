#!/usr/bin/env bash
set -euo pipefail
hold(){ printf 'HOLD=%s\n' "$1"; exit 2; }
field(){ printf '%s\n' "$2" | awk -F= -v K="$1" '$1==K{sub(/^[^=]*=/,"");print;exit}'; }
ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"
API="$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
[ -f "$API" ] || hold SESSION_API_NOT_FOUND
# shellcheck disable=SC1090
source "$API"
STATUS="$(sigma-session status 2>/dev/null || true)"
printf '%s\n' "$STATUS"
printf '%s\n' "$STATUS" | grep -Fqx 'SESSION=GRANTED' || hold SESSION_NOT_GRANTED
[ "$(field ACCESS "$STATUS")" = READ_PLUS_ARTIFACT_WRITE ] || hold SESSION_ACCESS_NOT_ARTIFACT_ONLY
for K in BRAIN_WRITE STATE_WRITE MODEL_WRITE LEARN COMMIT HEAD_CHANGE MODEL_GENERATION_CHANGE; do
  V="$(field "$K" "$STATUS")"
  [ "$V" = REJECT ] || hold "SESSION_${K}_NOT_REJECT"
done
HC="$(field HOST_COGNITION "$STATUS")"
[ -z "$HC" ] || [ "$HC" = NO ] || hold HOST_COGNITION_NOT_NO
printf 'SESSION_ARTIFACT_ONLY_GUARD=PASS\n'
