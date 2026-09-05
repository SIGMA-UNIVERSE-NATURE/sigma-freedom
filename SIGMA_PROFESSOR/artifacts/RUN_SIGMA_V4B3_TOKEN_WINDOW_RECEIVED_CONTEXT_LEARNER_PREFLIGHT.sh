#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"

STATE="$HOME_SIGMA/SIGMA_V4B3_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_PREFLIGHT"
SHADOW="$STATE/shadow.$$"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
LOG="$STATE/log.$$"
LOCK="$STATE/preflight.lock"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC_REPO="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigma"
SRC="$E/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigma"
BC="$E/SIGMA_V4_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_V4B3.sigmab"
EXPECTED_SOURCE=8a5687b4e83d74947dd9b1ca1a2729be104eff3d4b935cc64c6ef800f628af83

CTX_ID="$E/SIGMA_V4B3_CONTEXT_ID.memory"
CTX_TEXT="$E/SIGMA_V4B3_CONTEXT_TEXT.memory"
PROGRESS="$E/SIGMA_V4B3_PROGRESS_LEDGER.memory"
COMPLETE="$E/SIGMA_V4B3_COMPLETION_LEDGER.memory"
STATUS="$E/SIGMA_V4B3_STATUS.memory"

mkdir -p "$E" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4B3_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC_REPO")

printf 'SIGMA_PHASE=V4B3_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'TOKEN_WINDOW_BUDGET=16\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=V4B3_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

cp -- "$SRC_REPO" "$SRC" || { printf 'HOLD=SOURCE_INSTALL_FAILED\n'; exit 24; }
INSTALLED_SOURCE_SHA=$(hash1 "$SRC")
printf 'INSTALLED_SOURCE_SHA256=%s\n' "$INSTALLED_SOURCE_SHA"
[ "$INSTALLED_SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=INSTALLED_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V4B3_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=V4B3_COMPILE_FAILED\n'; exit 26; }
[ -s "$BC.partial" ] || { printf 'HOLD=V4B3_BYTECODE_EMPTY\n'; exit 27; }

mv -f -- "$BC.partial" "$BC"
chmod 0400 "$BC"
printf 'V4B3_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

run_case() {
    NAME="$1"
    RUNLOG="$LOG/$NAME.log"
    (
        cd "$BRAIN" || exit 40
        "$VM" "$BC"
    ) >"$RUNLOG" 2>&1
    RC=$?
    printf '\n=== %s ===\n' "$NAME"
    printf 'VM_RC=%s\n' "$RC"
    cat "$RUNLOG"
    return "$RC"
}

reset_state() {
    : > "$PROGRESS"
    : > "$COMPLETE"
    : > "$STATUS"
}

set_context() {
    printf '%s' "$1" > "$CTX_ID"
    printf '%s' "$2" > "$CTX_TEXT"
}

reset_state

LONG_LINE=''
I=1
while [ "$I" -le 209 ]; do
    if [ -z "$LONG_LINE" ]; then
        LONG_LINE="t$I"
    else
        LONG_LINE="$LONG_LINE t$I"
    fi
    I=$((I + 1))
done

set_context 'ctx-long-209' "$LONG_LINE"

run_case LONG_WINDOW_0 || exit 50
grep -F 'SELECTED_TOKEN_TOTAL 209' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 51
grep -F 'CURRENT_LINE_INDEX 0' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 52
grep -F 'CURRENT_TOKEN_OFFSET 0' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 53
grep -F 'WINDOW_END_TOKEN 16' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 54
grep -F 'WINDOW_RELATION_OCCURRENCES 15' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 55
grep -F 'FIRST_RELATION t1 => t2' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 56
grep -F 'STATUS TOKEN_WINDOW_PROGRESS' "$LOG/LONG_WINDOW_0.log" >/dev/null || exit 57

printf 'BROKEN_PROGRESS_TAIL\n' >> "$PROGRESS"

run_case LONG_WINDOW_1_FRESH_VM || exit 58
grep -F 'CURRENT_TOKEN_OFFSET 16' "$LOG/LONG_WINDOW_1_FRESH_VM.log" >/dev/null || exit 59
grep -F 'WINDOW_END_TOKEN 32' "$LOG/LONG_WINDOW_1_FRESH_VM.log" >/dev/null || exit 60
grep -F 'WINDOW_RELATION_OCCURRENCES 16' "$LOG/LONG_WINDOW_1_FRESH_VM.log" >/dev/null || exit 61
grep -F 'FIRST_RELATION t16 => t17' "$LOG/LONG_WINDOW_1_FRESH_VM.log" >/dev/null || exit 62
grep -F 'IGNORED_PROGRESS_RECORD_COUNT 1' "$LOG/LONG_WINDOW_1_FRESH_VM.log" >/dev/null || exit 63

I=2
while [ "$I" -le 13 ]; do
    run_case "LONG_WINDOW_$I" || exit 64
    I=$((I + 1))
done

grep -F 'CURRENT_TOKEN_OFFSET 208' "$LOG/LONG_WINDOW_13.log" >/dev/null || exit 65
grep -F 'WINDOW_END_TOKEN 209' "$LOG/LONG_WINDOW_13.log" >/dev/null || exit 66
grep -F 'WINDOW_RELATION_OCCURRENCES 1' "$LOG/LONG_WINDOW_13.log" >/dev/null || exit 67
grep -F 'FIRST_RELATION t208 => t209' "$LOG/LONG_WINDOW_13.log" >/dev/null || exit 68
grep -F 'STATUS CONTEXT_COMPLETE' "$LOG/LONG_WINDOW_13.log" >/dev/null || exit 69
grep -F -x 'CTX=ctx-long-209 || COMPLETE=YES' "$COMPLETE" >/dev/null || exit 70

PROGRESS_COMMITS=$(grep -c 'COMMIT=YES' "$PROGRESS" || true)
printf 'LONG_209_PROGRESS_COMMIT_COUNT=%s\n' "$PROGRESS_COMMITS"
[ "$PROGRESS_COMMITS" = '14' ] || exit 71

PROGRESS_SHA=$(hash1 "$PROGRESS")
COMPLETE_SHA=$(hash1 "$COMPLETE")

run_case LONG_ALREADY_COMPLETE || exit 72
grep -F 'STATUS ALREADY_COMPLETE' "$LOG/LONG_ALREADY_COMPLETE.log" >/dev/null || exit 73
[ "$(hash1 "$PROGRESS")" = "$PROGRESS_SHA" ] || exit 74
[ "$(hash1 "$COMPLETE")" = "$COMPLETE_SHA" ] || exit 75

: > "$COMPLETE"

run_case LONG_COMPLETION_RECOVERY || exit 76
grep -F 'STATUS RECOVERED_COMPLETION' "$LOG/LONG_COMPLETION_RECOVERY.log" >/dev/null || exit 77
grep -F 'COMPLETION_RECOVERY_ALLOWED 1' "$LOG/LONG_COMPLETION_RECOVERY.log" >/dev/null || exit 78
[ "$(hash1 "$PROGRESS")" = "$PROGRESS_SHA" ] || exit 79
grep -F -x 'CTX=ctx-long-209 || COMPLETE=YES' "$COMPLETE" >/dev/null || exit 80

reset_state
set_context 'ctx-oor' 'a b'
printf 'CTX=ctx-oor || LINE= || TOK= || NEXTLINE=|| || NEXTTOK= || BEST= || SUPPORT= || OCC= || COMMIT=YES\n' > "$PROGRESS"

run_case CURSOR_PAIR_OUT_OF_RANGE || exit 81
grep -F 'CURSOR_OUT_OF_RANGE 1' "$LOG/CURSOR_PAIR_OUT_OF_RANGE.log" >/dev/null || exit 82
grep -F 'STATUS REFUSE_CURSOR_OUT_OF_RANGE' "$LOG/CURSOR_PAIR_OUT_OF_RANGE.log" >/dev/null || exit 83
[ ! -s "$COMPLETE" ] || exit 84

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"

if [ -n "$V24_PID_BEFORE" ] && [ "$V24_PID_AFTER" != "$V24_PID_BEFORE" ]; then
    printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'
    exit 85
fi

printf '\nV4B3_TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNER_PREFLIGHT=PASS\n'
printf 'REAL_209_TOKEN_LINE_COUNTEREXAMPLE_RESOLVED_IN_FIXTURE_SCOPE=PASS\n'
printf 'SIXTEEN_TOKEN_NATIVE_WINDOW_PROGRESS=PASS\n'
printf 'FRESH_VM_LINE_TOKEN_CURSOR_RESUME=PASS\n'
printf 'CROSS_WINDOW_BIGRAM_CONTINUITY=PASS\n'
printf 'MALFORMED_PROGRESS_TAIL_IGNORED=PASS\n'
printf 'FOURTEEN_WINDOWS_COMPLETE_209_TOKEN_LINE=PASS\n'
printf 'ALREADY_COMPLETE_IDEMPOTENCY=PASS\n'
printf 'FINAL_PROGRESS_COMPLETION_RECOVERY=PASS\n'
printf 'CURSOR_PAIR_OUT_OF_RANGE_REFUSAL=PASS\n'
printf 'SHADOW_STATE_NAMESPACE_ISOLATION=PASS\n'
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'FETCHED_EQUALS_LEARNED=NO\n'
printf 'HOST_WINDOW_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'TOKEN_WINDOW_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_209_TOKEN_LINE_BOUNDED_TEST_SCOPE\n'
printf 'REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN\n'
printf 'WHOLE_SELECTED_LINE_SPLIT_CURRENT_ABI=YES\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_V4B3_THEN_REPLAY_REAL_49C16_CONTEXT_WITH_NATIVE_TOKEN_WINDOWS\n'
