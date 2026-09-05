#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3R1_REAL_180_SECOND_OBSERVE_PAUSE_PREFLIGHT"
LOCK="$BASE/preflight.lock"
RUN_ID="$("$P/bin/date" +%s).$$"
STATE="$BASE/run.$RUN_ID"
BRAIN="$STATE/BRAIN/EXTRA BRAIN_OPPO_24826"
E="$BRAIN/.sigma_exec"
RAW="$STATE/raw"
CORPUS="$STATE/corpus_state"
LOG="$STATE/log"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_CONTROLLER_V4C3R1.sigma"
EXPECTED_BLOB=cb3470fbd9ac4acebeaaaa149be0fadb8aebf13b
REPO_SRC="$REPO/$REL"
SRC="$E/SIGMA_V4_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_CONTROLLER_V4C3R1.sigma"
BC="$E/SIGMA_V4_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_CONTROLLER_V4C3R1.sigmab"
REPORT_FILE="$E/SIGMA_V4C3R1_LAST_REPORT.memory"
PLAN_FILE="$E/SIGMA_V4C3R1_PLAN.memory"
STATUS_FILE="$E/SIGMA_V4C3R1_STATUS.memory"
PROGRESS_FILE="$E/SIGMA_V4C3R1_PROGRESS.memory"

mkdir -p "$E" "$RAW" "$CORPUS" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R1_REAL_180_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3R1_REAL_180_SECOND_NATIVE_OBSERVE_PAUSE_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_PERCENT_CALCULATION=NO\n'
printf 'HOST_PAUSE_SLEEP=NO\n'
printf 'HOST_OBSERVATION_POLL_SLEEP=YES_MECHANICAL_ONLY\n'
printf 'OBSERVE_PAUSE_TARGET_SECONDS=180\n'
printf 'FIXTURE_ROLE=MECHANICAL_DYNAMIC_STATE_ONLY\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(git -C "$REPO" hash-object "$REPO_SRC")
printf 'SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=SOURCE_BLOB_MISMATCH\n'; exit 24; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=SOURCE_COPY_FAILED\n'; exit 25; }
INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
printf 'INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=INSTALLED_BLOB_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
printf 'BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

# Isolated dynamic corpus-state fixture. No report or next-plan answer is loaded.
printf 'a\n' > "$RAW/doc_a.document"
printf 'b\n' > "$RAW/doc_b.document"
printf 'c\n' > "$RAW/doc_c.document"
: > "$CORPUS/doc_a.profile"
: > "$CORPUS/doc_b.profile"
: > "$CORPUS/doc_a.complete"
: > "$CORPUS/doc_a.evidence"
: > "$CORPUS/doc_b.evidence"

for F in \
    SIGMA_V4C2R2_RAW_DIR.memory \
    SIGMA_V4C2R2_STATE_DIR.memory \
    SIGMA_V4C2R2_PHASE.memory \
    SIGMA_V4C2R2_ACTIVE_DOC.memory \
    SIGMA_V4C2R2_STATUS.memory \
    SIGMA_V4B4R2_CONTEXT_ID.memory \
    SIGMA_V4B4R2_TOKEN_CURSOR.memory \
    SIGMA_V4B4R2_STATUS.memory \
    SIGMA_V4B4R2_BEST_WIDTH.memory \
    SIGMA_V4B4R2_BEST_SUPPORT.memory \
    SIGMA_V4C3R1_INITIALIZED.memory \
    SIGMA_V4C3R1_LAST_SEEN_PROGRESS_KEY.memory \
    SIGMA_V4C3R1_PROGRESS.memory \
    SIGMA_V4C3R1_CYCLE.memory \
    SIGMA_V4C3R1_PROGRESS_BUDGET.memory \
    SIGMA_V4C3R1_PAUSE_SECONDS.memory \
    SIGMA_V4C3R1_LAST_REPORT.memory \
    SIGMA_V4C3R1_PLAN.memory \
    SIGMA_V4C3R1_STATUS.memory
do
    : > "$E/$F"
done

printf '%s' "$RAW" > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$CORPUS" > "$E/SIGMA_V4C2R2_STATE_DIR.memory"
printf '%s' 'LEARN' > "$E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' 'doc_b' > "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' 'NATIVE_EXACT_CORPUS_LINE_READ_REQUEST_EMITTED' > "$E/SIGMA_V4C2R2_STATUS.memory"
printf '%s' 'doc_b:line_1' > "$E/SIGMA_V4B4R2_CONTEXT_ID.memory"
printf '%s' '' > "$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
printf '%s' 'TOKEN_WINDOW_PROGRESS' > "$E/SIGMA_V4B4R2_STATUS.memory"
printf '%s' '||||' > "$E/SIGMA_V4B4R2_BEST_WIDTH.memory"
printf '%s' '||' > "$E/SIGMA_V4B4R2_BEST_SUPPORT.memory"

# One committed learner-key change triggers this gate. The 180-second value is a
# fixed mechanical test configuration represented in the controller's admitted unary format.
printf '%s' '|' > "$E/SIGMA_V4C3R1_PROGRESS_BUDGET.memory"
PAUSE_U=''
I=0
while [ "$I" -lt 180 ]; do
    PAUSE_U="${PAUSE_U}|"
    I=$((I + 1))
done
printf '%s' "$PAUSE_U" > "$E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"
printf 'PAUSE_UNARY_LENGTH=%s\n' "${#PAUSE_U}"
[ "${#PAUSE_U}" -eq 180 ] || { printf 'HOLD=MECHANICAL_PAUSE_FIXTURE_LENGTH_MISMATCH\n'; exit 34; }

BASELINE_LOG="$LOG/baseline.log"
(
    cd "$BRAIN" || exit 50
    "$VM" "$BC"
) > "$BASELINE_LOG" 2>&1
BASELINE_RC=$?
printf 'BASELINE_VM_RC=%s LOG=%s\n' "$BASELINE_RC" "$BASELINE_LOG"
"$P/bin/cat" "$BASELINE_LOG"
[ "$BASELINE_RC" -eq 0 ] || { printf 'HOLD=BASELINE_VM_FAILED\n'; exit 40; }
"$P/bin/grep" -F -x 'V4C3R1_STATUS BASELINE_ESTABLISHED' "$BASELINE_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=BASELINE_NOT_ESTABLISHED\n'
    exit 41
}

printf '%s' '|' > "$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
REFLECT_LOG="$LOG/reflect.log"
printf 'REFLECT_VM_LAUNCH=BEGIN_NATIVE_REPORT_PLAN_AND_180_SECOND_PAUSE\n'
(
    cd "$BRAIN" || exit 51
    "$VM" "$BC"
) > "$REFLECT_LOG" 2>&1 &
REFLECT_PID=$!
printf 'REFLECT_VM_PID=%s\n' "$REFLECT_PID"

# Mechanical observation only: expose the exact native report as soon as it is
# committed, while the same VM process remains alive inside native time_sleep.
REPORT_SEEN=0
while "$P/bin/kill" -0 "$REFLECT_PID" >/dev/null 2>&1; do
    if [ -s "$REPORT_FILE" ]; then
        REPORT_SEEN=1
        break
    fi
    "$P/bin/sleep" 1
done

[ "$REPORT_SEEN" -eq 1 ] || {
    wait "$REFLECT_PID"
    REFLECT_RC=$?
    "$P/bin/cat" "$REFLECT_LOG"
    printf 'HOLD=REPORT_NOT_OBSERVED_BEFORE_REFLECT_VM_EXIT RC=%s\n' "$REFLECT_RC"
    exit 42
}

"$P/bin/kill" -0 "$REFLECT_PID" >/dev/null 2>&1 || {
    wait "$REFLECT_PID"
    REFLECT_RC=$?
    "$P/bin/cat" "$REFLECT_LOG"
    printf 'HOLD=REFLECT_VM_NOT_RUNNING_WHEN_REPORT_OBSERVED RC=%s\n' "$REFLECT_RC"
    exit 43
}

printf 'REPORT_OBSERVED_WHILE_NATIVE_VM_RUNNING=YES\n'
printf 'NATIVE_REPORT_DURING_OBSERVE_PAUSE_BEGIN\n'
"$P/bin/cat" "$REPORT_FILE"
printf '\nNATIVE_REPORT_DURING_OBSERVE_PAUSE_END\n'
printf 'HUMAN_OBSERVER_CAN_READ_REPORT_DURING_NATIVE_PAUSE=YES_IN_THIS_GATE\n'
printf 'WAITING_FOR_NATIVE_180_SECOND_PAUSE_COMPLETION=YES\n'

wait "$REFLECT_PID"
REFLECT_RC=$?
printf 'REFLECT_VM_RC=%s LOG=%s\n' "$REFLECT_RC" "$REFLECT_LOG"
"$P/bin/cat" "$REFLECT_LOG"
[ "$REFLECT_RC" -eq 0 ] || { printf 'HOLD=REFLECT_VM_FAILED\n'; exit 44; }

"$P/bin/grep" -F -x 'PAUSE_SECONDS 180' "$REFLECT_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_180_SECOND_PAUSE_VALUE_NOT_OBSERVED\n'
    exit 45
}
"$P/bin/grep" -F -x 'V4C3R1_STATUS OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' "$REFLECT_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_180_SECOND_PAUSE_COMPLETION_NOT_PROVEN\n'
    exit 46
}
"$P/bin/grep" -F -x 'REPORT_COMMIT YES' "$REFLECT_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_REPORT_COMMIT_NOT_OBSERVED\n'
    exit 47
}
"$P/bin/grep" -F -x 'NEXT_NATIVE_PLAN PLAN_RESUME_ACTIVE_DOCUMENT' "$REFLECT_LOG" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_PLAN_NOT_OBSERVED\n'
    exit 48
}

PLAN=$("$P/bin/cat" "$PLAN_FILE")
FINAL_STATUS=$("$P/bin/cat" "$STATUS_FILE")
FINAL_PROGRESS=$("$P/bin/cat" "$PROGRESS_FILE")
FINAL_REPORT=$("$P/bin/cat" "$REPORT_FILE")

printf 'PERSISTED_PLAN=%s\n' "$PLAN"
printf 'PERSISTED_STATUS=%s\n' "$FINAL_STATUS"
printf 'PERSISTED_PROGRESS_AFTER_180_PAUSE=%s\n' "$FINAL_PROGRESS"
printf 'PERSISTED_REPORT=%s\n' "$FINAL_REPORT"

[ "$PLAN" = 'PLAN_RESUME_ACTIVE_DOCUMENT' ] || { printf 'HOLD=PERSISTED_PLAN_MISMATCH\n'; exit 49; }
[ "$FINAL_STATUS" = 'OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' ] || { printf 'HOLD=PERSISTED_STATUS_MISMATCH\n'; exit 50; }
[ -z "$FINAL_PROGRESS" ] || { printf 'HOLD=PROGRESS_NOT_RESET_AFTER_180_PAUSE\n'; exit 51; }
case "$FINAL_REPORT" in
    *'COMMIT=YES'*) ;;
    *) printf 'HOLD=PERSISTED_REPORT_COMMIT_MISSING\n'; exit 52 ;;
esac

printf '\nV4C3R1_REAL_180_SECOND_OBSERVE_PAUSE_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_REPORT_COMMITTED_BEFORE_PAUSE_COMPLETION=PASS_IN_OBSERVED_GATE_SCOPE\n'
printf 'REPORT_VISIBLE_TO_HUMAN_DURING_NATIVE_PAUSE=PASS_IN_OBSERVED_GATE_SCOPE\n'
printf 'NATIVE_180_SECOND_OBSERVE_PAUSE=PASS_IN_OBSERVED_GATE_SCOPE\n'
printf 'NATIVE_PLAN_PERSISTED_ACROSS_PAUSE=PASS_IN_OBSERVED_GATE_SCOPE\n'
printf 'NATIVE_RESUME_AFTER_180_SECOND_PAUSE=PASS_IN_OBSERVED_GATE_SCOPE\n'
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_PERCENT_CALCULATION=NO\n'
printf 'HOST_PAUSE_SLEEP=NO\n'
printf 'HOST_OBSERVATION_POLL_SLEEP=YES_MECHANICAL_ONLY\n'
printf 'UNDERSTANDING_PROXY_PERCENT=NOT_COMPUTABLE_FROM_CURRENT_MACHINE_EVIDENCE\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'REAL_C2R2_CONTINUOUS_INTEGRATION=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=INTEGRATE_V4C3R1_WITH_PERSISTENT_C2R2_CONTINUOUS_SHADOW\n'
