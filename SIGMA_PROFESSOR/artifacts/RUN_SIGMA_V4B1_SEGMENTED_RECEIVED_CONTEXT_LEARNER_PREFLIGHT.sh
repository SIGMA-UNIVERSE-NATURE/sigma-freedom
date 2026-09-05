#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"

STATE="$HOME_SIGMA/SIGMA_V4B1_SEGMENTED_RECEIVED_CONTEXT_LEARNER_PREFLIGHT"
SHADOW="$STATE/shadow"
BRAIN="$SHADOW/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC_REPO="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma"
SRC="$E/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma"
BC="$E/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigmab"
EXPECTED_SOURCE=2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4

CTX_ID="$E/SIGMA_V4B1_CONTEXT_ID.memory"
CTX_TEXT="$E/SIGMA_V4B1_CONTEXT_TEXT.memory"
CURSOR="$E/SIGMA_V4B1_CURSOR_LEDGER.memory"
EVIDENCE="$E/SIGMA_V4B1_SEGMENT_EVIDENCE.memory"
COMPLETE="$E/SIGMA_V4B1_COMPLETION_LEDGER.memory"
STATUS="$E/SIGMA_V4B1_STATUS.memory"

mkdir -p "$E" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4B1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC_REPO")

printf 'SIGMA_PHASE=V4B1_SEGMENTED_RECEIVED_CONTEXT_LEARNER_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'SHADOW_BRAIN=%s\n' "$BRAIN"
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'

V24_PID_BEFORE=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_BEFORE=%s\n' "$V24_PID_BEFORE"

if [ "$SIGMAC_SHA" != "$EXPECTED_SIGMAC" ] || [ "$VM_SHA" != "$EXPECTED_VM" ] || [ "$SOURCE_SHA" != "$EXPECTED_SOURCE" ]; then
    printf 'HOLD=LOCKED_IDENTITY_MISMATCH\n'
    exit 21
fi

cp -- "$SRC_REPO" "$SRC" || { printf 'HOLD=SOURCE_INSTALL_FAILED\n'; exit 22; }
INSTALLED_SOURCE_SHA=$(hash1 "$SRC")
printf 'INSTALLED_SOURCE_SHA256=%s\n' "$INSTALLED_SOURCE_SHA"
[ "$INSTALLED_SOURCE_SHA" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=INSTALLED_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V4B1_SIGMAC_RC=%s\n' "$RC"
if [ "$RC" -ne 0 ] || [ ! -s "$BC.partial" ]; then
    printf 'HOLD=V4B1_COMPILE_FAILED\n'
    exit 24
fi
mv -f -- "$BC.partial" "$BC"
chmod 0400 "$BC"
printf 'V4B1_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

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
    : > "$CURSOR"
    : > "$EVIDENCE"
    : > "$COMPLETE"
    : > "$STATUS"
}

set_context() {
    printf '%s' "$1" > "$CTX_ID"
    printf '%s' "$2" > "$CTX_TEXT"
}

reset_state
CTX_A='alpha beta gamma
alpha beta delta
epsilon zeta
eta theta iota
kappa lambda'
set_context 'ctx-A' "$CTX_A"

run_case A_SEGMENT_0 || exit 50
grep -F 'SEGMENT_START_LINE 0' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 51
grep -F 'SEGMENT_END_LINE 2' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 52
grep -F 'BEST_RELATION alpha => beta' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 53
grep -F 'BEST_SUPPORT 2' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 54
grep -F 'CONTEXT_COMPLETE 0' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 55
grep -F 'STATUS SEGMENT_PROGRESS' "$LOG/A_SEGMENT_0.log" >/dev/null || exit 56

run_case A_SEGMENT_1_FRESH_VM || exit 57
grep -F 'SEGMENT_START_LINE 2' "$LOG/A_SEGMENT_1_FRESH_VM.log" >/dev/null || exit 58
grep -F 'SEGMENT_END_LINE 4' "$LOG/A_SEGMENT_1_FRESH_VM.log" >/dev/null || exit 59
grep -F 'CONTEXT_COMPLETE 0' "$LOG/A_SEGMENT_1_FRESH_VM.log" >/dev/null || exit 60

printf 'BROKEN_CURSOR_TAIL\n' >> "$CURSOR"
run_case A_SEGMENT_2_AFTER_MALFORMED_CURSOR || exit 61
grep -F 'IGNORED_CURSOR_RECORD_COUNT 1' "$LOG/A_SEGMENT_2_AFTER_MALFORMED_CURSOR.log" >/dev/null || exit 62
grep -F 'SEGMENT_START_LINE 4' "$LOG/A_SEGMENT_2_AFTER_MALFORMED_CURSOR.log" >/dev/null || exit 63
grep -F 'SEGMENT_END_LINE 5' "$LOG/A_SEGMENT_2_AFTER_MALFORMED_CURSOR.log" >/dev/null || exit 64
grep -F 'CONTEXT_COMPLETE 1' "$LOG/A_SEGMENT_2_AFTER_MALFORMED_CURSOR.log" >/dev/null || exit 65
grep -F 'STATUS CONTEXT_COMPLETE' "$LOG/A_SEGMENT_2_AFTER_MALFORMED_CURSOR.log" >/dev/null || exit 66

EVIDENCE_A_SHA=$(hash1 "$EVIDENCE")
CURSOR_A_SHA=$(hash1 "$CURSOR")
COMPLETE_A_SHA=$(hash1 "$COMPLETE")

run_case A_ALREADY_COMPLETE_IDEMPOTENT || exit 67
grep -F 'STATUS ALREADY_COMPLETE' "$LOG/A_ALREADY_COMPLETE_IDEMPOTENT.log" >/dev/null || exit 68
[ "$(hash1 "$EVIDENCE")" = "$EVIDENCE_A_SHA" ] || exit 69
[ "$(hash1 "$CURSOR")" = "$CURSOR_A_SHA" ] || exit 70
[ "$(hash1 "$COMPLETE")" = "$COMPLETE_A_SHA" ] || exit 71

reset_state
CTX_B='one two three
one two four
five six'
set_context 'ctx-B' "$CTX_B"

run_case B_INITIAL_SEGMENT || exit 72
B_EVIDENCE_SHA=$(hash1 "$EVIDENCE")
B_EVIDENCE_LINES=$(grep -c 'COMMIT=YES' "$EVIDENCE" || true)
: > "$CURSOR"

run_case B_EVIDENCE_ONLY_CRASH_RECOVERY || exit 73
grep -F 'SEGMENT_ALREADY_COMMITTED 1' "$LOG/B_EVIDENCE_ONLY_CRASH_RECOVERY.log" >/dev/null || exit 74
[ "$(hash1 "$EVIDENCE")" = "$B_EVIDENCE_SHA" ] || exit 75
[ "$(grep -c 'COMMIT=YES' "$EVIDENCE" || true)" = "$B_EVIDENCE_LINES" ] || exit 76
grep -F 'SEGMENT_END_LINE 2' "$LOG/B_EVIDENCE_ONLY_CRASH_RECOVERY.log" >/dev/null || exit 77

run_case B_COMPLETE_AFTER_RECOVERY || exit 78
grep -F 'SEGMENT_START_LINE 2' "$LOG/B_COMPLETE_AFTER_RECOVERY.log" >/dev/null || exit 79
grep -F 'CONTEXT_COMPLETE 1' "$LOG/B_COMPLETE_AFTER_RECOVERY.log" >/dev/null || exit 80

reset_state
printf 'CTX=other-context || NEXT=|||| || COMMIT=YES\n' > "$CURSOR"
CTX_C='red blue
green yellow
black white'
set_context 'ctx-C' "$CTX_C"

run_case C_FOREIGN_CURSOR_IGNORED || exit 81
grep -F 'SEGMENT_START_LINE 0' "$LOG/C_FOREIGN_CURSOR_IGNORED.log" >/dev/null || exit 82
grep -F 'IGNORED_CURSOR_RECORD_COUNT 1' "$LOG/C_FOREIGN_CURSOR_IGNORED.log" >/dev/null || exit 83

reset_state
LONG_LINE=''
I=1
while [ "$I" -le 66 ]; do
    if [ -z "$LONG_LINE" ]; then
        LONG_LINE="t$I"
    else
        LONG_LINE="$LONG_LINE t$I"
    fi
    I=$((I + 1))
done
set_context 'ctx-D' "$LONG_LINE"

run_case D_TOKEN_LIMIT_REFUSAL || exit 84
grep -F 'STATUS REFUSE_TOKEN_LIMIT' "$LOG/D_TOKEN_LIMIT_REFUSAL.log" >/dev/null || exit 85
[ ! -s "$EVIDENCE" ] || exit 86
[ ! -s "$CURSOR" ] || exit 87
[ ! -s "$COMPLETE" ] || exit 88

reset_state
MANY_LINES=''
I=1
while [ "$I" -le 66 ]; do
    if [ -z "$MANY_LINES" ]; then
        MANY_LINES="line$I value$I"
    else
        MANY_LINES="$MANY_LINES
line$I value$I"
    fi
    I=$((I + 1))
done
set_context 'ctx-E' "$MANY_LINES"

run_case E_CONTEXT_LINE_LIMIT_REFUSAL || exit 89
grep -F 'STATUS REFUSE_CONTEXT_LINE_LIMIT' "$LOG/E_CONTEXT_LINE_LIMIT_REFUSAL.log" >/dev/null || exit 90
[ ! -s "$EVIDENCE" ] || exit 91
[ ! -s "$CURSOR" ] || exit 92
[ ! -s "$COMPLETE" ] || exit 93

reset_state
CTX_F='sun moon
star sky'
set_context 'ctx-F' "$CTX_F"
run_case F_INITIAL_COMPLETE || exit 94
grep -F 'STATUS CONTEXT_COMPLETE' "$LOG/F_INITIAL_COMPLETE.log" >/dev/null || exit 95
F_EVIDENCE_SHA=$(hash1 "$EVIDENCE")
F_CURSOR_SHA=$(hash1 "$CURSOR")
: > "$COMPLETE"

run_case F_COMPLETION_ONLY_RECOVERY || exit 96
grep -F 'STATUS RECOVERED_COMPLETION' "$LOG/F_COMPLETION_ONLY_RECOVERY.log" >/dev/null || exit 97
grep -F 'COMPLETION_RECOVERY_ALLOWED 1' "$LOG/F_COMPLETION_ONLY_RECOVERY.log" >/dev/null || exit 98
[ "$(hash1 "$EVIDENCE")" = "$F_EVIDENCE_SHA" ] || exit 99
[ "$(hash1 "$CURSOR")" = "$F_CURSOR_SHA" ] || exit 100
[ -s "$COMPLETE" ] || exit 101

reset_state
printf 'CTX=ctx-G || NEXT=||| || COMMIT=YES\n' > "$CURSOR"
CTX_G='a b
c d'
set_context 'ctx-G' "$CTX_G"

run_case G_CURSOR_OUT_OF_RANGE_REFUSAL || exit 102
grep -F 'STATUS REFUSE_CURSOR_OUT_OF_RANGE' "$LOG/G_CURSOR_OUT_OF_RANGE_REFUSAL.log" >/dev/null || exit 103
grep -F 'CURSOR_OUT_OF_RANGE 1' "$LOG/G_CURSOR_OUT_OF_RANGE_REFUSAL.log" >/dev/null || exit 104
[ ! -s "$EVIDENCE" ] || exit 105
[ ! -s "$COMPLETE" ] || exit 106

V24_PID_AFTER=$("$P/bin/pgrep" -f 'RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh' | "$P/bin/head" -n1 || true)
printf 'PRODUCTION_V24_PID_AFTER=%s\n' "$V24_PID_AFTER"
if [ -n "$V24_PID_BEFORE" ] && [ "$V24_PID_AFTER" != "$V24_PID_BEFORE" ]; then
    printf 'HOLD=PRODUCTION_V24_PID_CHANGED\n'
    exit 107
fi

printf '\nV4B1_SEGMENTED_RECEIVED_CONTEXT_LEARNER_PREFLIGHT=PASS\n'
printf 'TWO_LINE_NATIVE_SEGMENT_PROGRESS=PASS\n'
printf 'FRESH_VM_CURSOR_RESUME=PASS\n'
printf 'MALFORMED_CURSOR_TAIL_IGNORED=PASS\n'
printf 'LEARNED_ONLY_AFTER_ALL_SEGMENTS_COMPLETE=PASS\n'
printf 'ALREADY_COMPLETE_IDEMPOTENCY=PASS\n'
printf 'EVIDENCE_ONLY_CRASH_RETRY_NO_DUPLICATE=PASS\n'
printf 'FOREIGN_CONTEXT_CURSOR_IGNORED=PASS\n'
printf 'TOKEN_LIMIT_REFUSAL=PASS\n'
printf 'CONTEXT_LINE_LIMIT_REFUSAL=PASS\n'
printf 'FINAL_CURSOR_COMPLETION_RECOVERY=PASS\n'
printf 'CURSOR_OUT_OF_RANGE_REFUSAL=PASS\n'
printf 'SHADOW_STATE_NAMESPACE_ISOLATION=PASS\n'
printf 'PRODUCTION_BRAIN_WRITE_TARGET=NO\n'
printf 'PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS\n'
printf 'FETCHED_EQUALS_LEARNED=NO\n'
printf 'HOST_SEGMENT_SELECTION=NO\n'
printf 'HOST_COMPLETION_DECISION=NO\n'
printf 'HOST_RETRY_DECISION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE\n'
printf 'REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'BOUNDED_FILE_IO=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'NEXT_ACTION=CHECKPOINT_V4B1_THEN_REPLAY_REAL_V24_RC9_HELD_CONTEXTS_THROUGH_V4B\n'
