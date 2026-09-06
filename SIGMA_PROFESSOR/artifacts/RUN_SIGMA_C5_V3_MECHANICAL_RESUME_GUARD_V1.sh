#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

HOME_SIGMA="${HOME_SIGMA:-$HOME/SIGMA}"
ROOT="${SIGMA_ROOT:-$HOME_SIGMA/sigma_genesis1}"
STATE="${C5_STATE_ROOT:-$ROOT/.sigma_c5_real_shadow_v2}"
INSTALL="$ROOT/.sigma_c5"
RUNNER="$INSTALL/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
PIDFILE="$ROOT/C5_V3_CONTINUOUS.pid"
LOG="$ROOT/C5_V3_CONTINUOUS.log"

EXPECTED_RUNNER_SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb

hash1() { sha256sum "$1" | awk '{print $1}'; }

printf 'SIGMA_C5_V3_MECHANICAL_RESUME_GUARD_V1=BEGIN\n'
printf 'HOST_COGNITION=NO\nHOST_LEARNING=NO\nHOST_QUERY_GENERATION=NO\nHOST_WORK_SELECTION=NO\n'
printf 'RESUME_TARGET_STATE=%s\n' "$STATE"
printf 'GLOBAL_TURN_LIMIT=NONE_MAX_TURNS_ZERO\n'
printf 'GLOBAL_FETCH_LIMIT=NONE_MAX_FETCHES_ZERO\n'

[ -d "$ROOT" ] || { printf 'HOLD=SIGMA_ROOT_MISSING\n'; exit 20; }
[ -f "$RUNNER" ] || { printf 'HOLD=V3_RUNNER_MISSING path=%s\n' "$RUNNER"; exit 21; }
[ -f "$STATE/state/state.sqlite3" ] || { printf 'HOLD=C5_STATE_DB_MISSING\n'; exit 22; }
[ -f "$STATE/catalog/catalog_v2.sqlite3" ] || { printf 'HOLD=C5_CATALOG_DB_MISSING\n'; exit 23; }

RUNNER_SHA="$(hash1 "$RUNNER")"
printf 'V3_RUNNER_SHA256=%s\n' "$RUNNER_SHA"
[ "$RUNNER_SHA" = "$EXPECTED_RUNNER_SHA256" ] || { printf 'HOLD=V3_RUNNER_IDENTITY_MISMATCH\n'; exit 24; }

pid_is_exact_runner() {
    P="$1"
    [ -n "$P" ] || return 1
    case "$P" in *[!0-9]*) return 1 ;; esac
    kill -0 "$P" 2>/dev/null || return 1
    CMD="$(tr '\000' ' ' < "/proc/$P/cmdline" 2>/dev/null || true)"
    case "$CMD" in
      *RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh*) return 0 ;;
      *) return 1 ;;
    esac
}

OLD_PID=''
if [ -s "$PIDFILE" ]; then
    OLD_PID="$(cat "$PIDFILE" 2>/dev/null || true)"
fi

if pid_is_exact_runner "$OLD_PID"; then
    printf 'SIGMA_C5_V3_ALREADY_RUNNING=YES\n'
    printf 'SIGMA_C5_V3_PID=%s\n' "$OLD_PID"
    printf 'RESUME_ACTION=NONE_ALREADY_RUNNING\n'
    exit 0
fi

# Refuse to duplicate an exact runner if PID bookkeeping is stale.
FOUND_PID="$(pgrep -f 'RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh' 2>/dev/null | head -n 1 || true)"
if [ -n "$FOUND_PID" ] && pid_is_exact_runner "$FOUND_PID"; then
    printf 'HOLD=EXACT_V3_RUNNER_ACTIVE_WITH_STALE_OR_MISSING_PIDFILE pid=%s\n' "$FOUND_PID"
    printf 'RESUME_ACTION=NONE_AVOID_DUPLICATE\n'
    exit 25
fi

if command -v termux-wake-lock >/dev/null 2>&1; then
    termux-wake-lock >/dev/null 2>&1 || true
    printf 'TERMUX_WAKE_LOCK=REQUESTED\n'
else
    printf 'TERMUX_WAKE_LOCK_COMMAND=UNAVAILABLE\n'
fi

printf 'RESUME_ACTION=START_EXACT_V3_RUNNER\n'
nohup env \
  C5_STATE_ROOT="$STATE" \
  C5_MAX_TURNS=0 \
  C5_MAX_FETCHES=0 \
  C5_ENABLE_LIVE_NETWORK=YES \
  bash "$RUNNER" >> "$LOG" 2>&1 &
PID=$!
printf '%s\n' "$PID" > "$PIDFILE"
sleep 3

if ! pid_is_exact_runner "$PID"; then
    printf 'HOLD=V3_RESUME_PROCESS_DIED_OR_IDENTITY_NOT_OBSERVED pid=%s\n' "$PID"
    tail -n 120 "$LOG" 2>/dev/null || true
    exit 26
fi

printf 'SIGMA_C5_V3_RESUME_STARTED=YES\n'
printf 'SIGMA_C5_V3_PID=%s\n' "$PID"
printf 'SIGMA_C5_V3_STATE_ROOT=%s\n' "$STATE"
printf 'SIGMA_C5_V3_LOG=%s\n' "$LOG"
printf 'RESUME_GUARD_RESULT=PASS_PROCESS_ALIVE_AFTER_START\n'
printf 'POST_RESTART_LEARNING_PROGRESS=NOT_PROVEN_BY_START_CHECK_ALONE\n'
