#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BRAIN="$REPO/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

SRC="$E/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A1.sigma"
BC="$E/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A1.sigmab"
EXPECTED_SOURCE=12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2

REC="$E/SIGMA_V4A1_RECOVERED_EVENT.memory"
RCV="$E/SIGMA_V4A1_RECEIVED_WORK.memory"
RET="$E/SIGMA_V4A1_RETRYABLE_WORK.memory"
LOC="$E/SIGMA_V4A1_LOCAL_WORK.memory"
REQ="$E/SIGMA_V4A1_FETCH_REQUEST.memory"
NEXT="$E/SIGMA_V4A1_NEXT_FETCH_NOT_BEFORE.memory"
LEDGER="$E/SIGMA_V4A1_ARBITER_LEDGER.memory"
ACTION="$E/SIGMA_V4A1_ACTION.memory"
TARGET="$E/SIGMA_V4A1_TARGET.memory"

STATE="$HOME_SIGMA/SIGMA_V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT"
LOG="$STATE/log"
LOCK="$STATE/preflight.lock"
mkdir -p "$STATE" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4A1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
SOURCE_SHA=$(hash1 "$SRC")

printf 'SIGMA_PHASE=V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'SOURCE_SHA256=%s\n' "$SOURCE_SHA"
printf 'HOST_WORK_SELECTION=NO\n'
printf 'HOST_STAGE_DECISION=NO\n'
printf 'HOST_RETRY_POLICY=NO\n'
printf 'HOST_LEARNING=NO\n'

if [ "$SIGMAC_SHA" != "$EXPECTED_SIGMAC" ] || [ "$VM_SHA" != "$EXPECTED_VM" ] || [ "$SOURCE_SHA" != "$EXPECTED_SOURCE" ]; then
    printf 'HOLD=LOCKED_IDENTITY_MISMATCH\n'
    exit 21
fi

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'V4A1_SIGMAC_RC=%s\n' "$RC"
if [ "$RC" -ne 0 ] || [ ! -s "$BC.partial" ]; then
    printf 'HOLD=V4A1_COMPILE_FAILED\n'
    exit 22
fi

mv -f -- "$BC.partial" "$BC"
chmod 0400 "$BC"
printf 'V4A1_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

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

set_inputs() {
    printf '%s' "$1" > "$REC"
    printf '%s' "$2" > "$RCV"
    printf '%s' "$3" > "$RET"
    printf '%s' "$4" > "$LOC"
    printf '%s' "$5" > "$REQ"
    printf '%s' "$6" > "$NEXT"
}

: > "$LEDGER"

set_inputs '' '' '' 'local-A' 'query-A' '4102444800'
run_case RATE_LIMIT_LOCAL || exit 50
[ "$(cat "$ACTION")" = 'CONTINUE_LOCAL_CURRICULUM' ] || exit 51

set_inputs '' '' 'retry-B' 'local-A' 'query-A' '4102444800'
run_case RATE_LIMIT_RETRYABLE || exit 52
[ "$(cat "$ACTION")" = 'RESUME_RETRYABLE_CONTEXT' ] || exit 53

set_inputs '' 'received-C' 'retry-B' 'local-A' 'query-A' '4102444800'
run_case ROTATE_TO_LOCAL || exit 54
[ "$(cat "$ACTION")" = 'CONTINUE_LOCAL_CURRICULUM' ] || exit 55

set_inputs '' 'received-C' 'retry-B' 'local-A' 'query-D' '0'
run_case DUE_FETCH || exit 56
[ "$(cat "$ACTION")" = 'DISPATCH_NATIVE_FETCH_REQUEST' ] || exit 57

set_inputs '' 'received-E' 'retry-B' 'local-A' 'query-E' '0'
run_case POST_FETCH_RECEIVED || exit 58
[ "$(cat "$ACTION")" = 'LEARN_RECEIVED_CONTEXT' ] || exit 59

set_inputs 'work-X::|||::EXECUTE_REVISIT' 'received-E' 'retry-B' 'local-A' 'query-E' '0'
run_case RECOVERED_FIRST || exit 60
[ "$(cat "$ACTION")" = 'EXECUTE_RECOVERED_EVENT' ] || exit 61
[ "$(cat "$TARGET")" = 'work-X::|||::EXECUTE_REVISIT' ] || exit 62

set_inputs '' '' '' '' 'query-G' '4102444800'
run_case TRUE_IDLE || exit 63
[ "$(cat "$ACTION")" = 'WAIT_NO_ELIGIBLE_WORK' ] || exit 64

set_inputs '' 'received-H' '' 'local-H' '' ''
run_case FRESH_VM_LEDGER_REUSE || exit 65
[ "$(cat "$ACTION")" = 'LEARN_RECEIVED_CONTEXT' ] || exit 66

printf 'BROKEN_RECORD\n' >> "$LEDGER"
set_inputs '' '' 'retry-I' 'local-I' '' ''
run_case MALFORMED_LEDGER_FILTER || exit 67
grep -F 'IGNORED_LEDGER_RECORD_COUNT 1' "$LOG/MALFORMED_LEDGER_FILTER.log" >/dev/null || exit 68

: > "$LEDGER"
I=0
while [ "$I" -lt 66 ]; do
    printf 'SOURCE=LOCAL || COMMIT=YES\n' >> "$LEDGER"
    I=$((I + 1))
done
set_inputs '' 'received-J' 'retry-J' 'local-J' 'query-J' '0'
run_case LEDGER_LIMIT_REFUSAL || exit 69
[ "$(cat "$ACTION")" = 'WAIT_LEDGER_LIMIT_EXCEEDED' ] || exit 70

printf '\nV4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT=PASS\n'
printf 'RATE_LIMIT_WAIT_CONTINUES_LOCAL_WORK=PASS\n'
printf 'RETRYABLE_CONTEXT_PROGRESS=PASS\n'
printf 'ROUND_ROBIN_SOURCE_FAIRNESS=PASS\n'
printf 'DUE_FETCH_PROGRESS=PASS\n'
printf 'RECEIVED_CONTEXT_PROGRESS=PASS\n'
printf 'RECOVERED_CONTINUATION_FIRST=PASS\n'
printf 'TRUE_IDLE_ONLY_WHEN_NO_ELIGIBLE_WORK=PASS\n'
printf 'FRESH_VM_LEDGER_REUSE=PASS\n'
printf 'MALFORMED_LEDGER_FILTER=PASS\n'
printf 'STEP_LIMIT_STATUS=BOUNDED\n'
printf 'FETCHED_EQUALS_LEARNED=NO\n'
printf 'HOST_WORK_SELECTION=NO\n'
printf 'HOST_STAGE_DECISION=NO\n'
printf 'HOST_RETRY_POLICY=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE\n'
printf 'V4_PRODUCTION_PROMOTION_ALLOWED=NO\n'
printf 'NEXT_ACTION=CHECKPOINT_V4A1_THEN_TEACH_SEGMENTED_RECEIVED_CONTEXT_LEARNER\n'
