#!/data/data/com.termux/files/usr/bin/bash
set -u
umask 077

# SIGMA V927 SAFE AUTONOMOUS AUTOLEARN GOVERNOR
# Reuses the existing V926 learner/supervisor and current SIA registry.
# This file does NOT create a new learner/VM/SIGMA and does not mutate HEAD.
# All semantic choice must remain inside native SIGMA capability/learner execution.

ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"
R="${RUNTIME:-$ROOT/.sigma_ail/SIGMA_VKM_V926_SURVIVAL_AUTOLEARN_R10}"
STATE="$R/state"
LOG="$R/log"
BIN="$R/bin"
LOCK="$STATE/V927_SINGLE_WRITER.lock"
STOP="$STATE/STOP"
HOLD="$STATE/HOLD"
REGISTRY="$ROOT/.sigma_ail/SIA_CORE_A/canonical_consumer_R3/by_sha256/24e6718435a777bdf74bad28493e6c85e7895418edd9855cb30a86b92e45b7dc/registry.json"

mkdir -p "$STATE" "$LOG"

hold() {
  printf '%s\n' "STATUS=HOLD" "REASON=$1" "FAKE_PASS=NO" "HOST_LEARNING=NO" "BASH_LEARNING=NO"
  exit 2
}

# Exactly one V927 supervisor/training writer.
exec 9>"$LOCK" || hold LOCK_OPEN_FAILED
flock -n 9 || hold SECOND_WRITER_REJECTED

# Never continue through a pre-existing safety hold.
[ -f "$HOLD" ] && hold EXISTING_RUNTIME_HOLD

# Dynamic SIA capability discovery: count/read registry entries at runtime.
[ -f "$REGISTRY" ] || hold SIA_REGISTRY_MISSING
CAP_COUNT="$(python - "$REGISTRY" <<'PY'
import json,sys
p=sys.argv[1]
d=json.load(open(p,encoding='utf-8'))
caps=d.get("capabilities") or d.get("records") or d.get("items")
if not isinstance(caps,list) or not caps:
    raise SystemExit(2)
print(len(caps))
PY
)" || hold SIA_REGISTRY_INVALID
[ "$CAP_COUNT" -gt 0 ] || hold SIA_NO_ACTIVE_CAPABILITIES

# Android/background support: use the existing runtime start path only.
if command -v termux-wake-lock >/dev/null 2>&1; then
  termux-wake-lock >/dev/null 2>&1 || true
fi

[ -x "$BIN/start_runtime.sh" ] || hold EXISTING_START_RUNTIME_MISSING
[ -x "$BIN/status.sh" ] || hold EXISTING_STATUS_MISSING
[ -x "$BIN/supervisor.sh" ] || hold EXISTING_SUPERVISOR_MISSING

# Do not create a second supervisor. Existing launcher owns the process tree.
"$BIN/start_runtime.sh" >>"$LOG/V927_start.log" 2>&1 || hold EXISTING_SUPERVISOR_START_FAILED

printf '%s\n' \
  'V927_STATUS=STARTED_EXISTING_AUTOLEARN' \
  "V927_DYNAMIC_SIA_CAPABILITY_COUNT=$CAP_COUNT" \
  'V927_CAPABILITY_SELECTION_OWNER=SIGMA_NATIVE' \
  'V927_HOST_SEMANTIC_SELECTION=NO' \
  'V927_HOST_SCORING=NO' \
  'V927_HOST_LEARNING=NO' \
  'V927_NEW_LEARNER=NO' \
  'V927_NEW_VM=NO' \
  'V927_NEW_SIGMA=NO' \
  'V927_SINGLE_WRITER=PASS' \
  'V927_BACKGROUND=YES' \
  'V927_HEAD_MUTATION=NO' \
  'V927_CANONICAL_MUTATION=NO' \
  'V927_NOTE=Existing worker remains authoritative; any native HOLD blocks learning rather than fabricating PASS.'
