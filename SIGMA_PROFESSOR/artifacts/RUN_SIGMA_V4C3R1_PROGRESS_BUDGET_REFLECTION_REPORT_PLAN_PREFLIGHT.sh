#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3R1_PROGRESS_BUDGET_REFLECTION_PREFLIGHT"
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

mkdir -p "$E" "$RAW" "$CORPUS" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R1_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3R1_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_PERCENT_CALCULATION=NO\n'
printf 'HOST_SLEEP=NO\n'
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

# Mechanical dynamic fixtures. No expected report/plan bytes are loaded into SIGMA.
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
printf '%s' '||' > "$E/SIGMA_V4C3R1_PROGRESS_BUDGET.memory"
printf '%s' '||' > "$E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"

run_vm() {
    LABEL="$1"
    OUT="$LOG/$LABEL.log"
    (
        cd "$BRAIN" || exit 50
        "$VM" "$BC"
    ) > "$OUT" 2>&1
    RC=$?
    printf '%s_VM_RC=%s LOG=%s\n' "$LABEL" "$RC" "$OUT"
    "$P/bin/cat" "$OUT"
    [ "$RC" -eq 0 ] || return "$RC"
    return 0
}

run_vm BASELINE || { printf 'HOLD=BASELINE_VM_FAILED\n'; exit 40; }
"$P/bin/grep" -F -x 'V4C3R1_STATUS BASELINE_ESTABLISHED' "$LOG/BASELINE.log" >/dev/null 2>&1 || {
    printf 'HOLD=BASELINE_NOT_ESTABLISHED\n'
    exit 41
}

printf '%s' '|' > "$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
run_vm PROGRESS1 || { printf 'HOLD=PROGRESS1_VM_FAILED\n'; exit 42; }
"$P/bin/grep" -F -x 'V4C3R1_STATUS LEARN_PROGRESS_ACCUMULATING' "$LOG/PROGRESS1.log" >/dev/null 2>&1 || {
    printf 'HOLD=FIRST_PROGRESS_NOT_ACCUMULATING\n'
    exit 43
}

printf '%s' '||' > "$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
run_vm REFLECT || { printf 'HOLD=REFLECTION_VM_FAILED\n'; exit 44; }
"$P/bin/grep" -F -x 'V4C3R1_STATUS OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=OBSERVE_PAUSE_RESUME_NOT_PROVEN\n'
    exit 45
}
"$P/bin/grep" -F -x 'NEXT_NATIVE_PLAN PLAN_RESUME_ACTIVE_DOCUMENT' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_PLAN_NOT_OBSERVED\n'
    exit 46
}
"$P/bin/grep" -F -x 'REPORT_COMMIT YES' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_REPORT_COMMIT_NOT_OBSERVED\n'
    exit 47
}
"$P/bin/grep" -F -x 'DISCOVERED_DOCUMENT_COUNT 3' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_DISCOVERED_COUNT_MISMATCH\n'
    exit 48
}
"$P/bin/grep" -F -x 'COMPLETE_DOCUMENT_COUNT 1' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_COMPLETE_COUNT_MISMATCH\n'
    exit 49
}
"$P/bin/grep" -F -x 'PAUSE_SECONDS 2' "$LOG/REFLECT.log" >/dev/null 2>&1 || {
    printf 'HOLD=NATIVE_PAUSE_SECONDS_MISMATCH\n'
    exit 50
}

REPORT=$("$P/bin/cat" "$E/SIGMA_V4C3R1_LAST_REPORT.memory")
PLAN=$("$P/bin/cat" "$E/SIGMA_V4C3R1_PLAN.memory")
FINAL_STATUS=$("$P/bin/cat" "$E/SIGMA_V4C3R1_STATUS.memory")
FINAL_PROGRESS=$("$P/bin/cat" "$E/SIGMA_V4C3R1_PROGRESS.memory")

printf 'PERSISTED_REPORT=%s\n' "$REPORT"
printf 'PERSISTED_PLAN=%s\n' "$PLAN"
printf 'PERSISTED_STATUS=%s\n' "$FINAL_STATUS"
printf 'PERSISTED_PROGRESS_AFTER_PAUSE=%s\n' "$FINAL_PROGRESS"

[ "$PLAN" = 'PLAN_RESUME_ACTIVE_DOCUMENT' ] || { printf 'HOLD=PERSISTED_PLAN_MISMATCH\n'; exit 51; }
[ "$FINAL_STATUS" = 'OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' ] || { printf 'HOLD=PERSISTED_STATUS_MISMATCH\n'; exit 52; }
[ -z "$FINAL_PROGRESS" ] || { printf 'HOLD=PROGRESS_NOT_RESET_AFTER_PAUSE\n'; exit 53; }
case "$REPORT" in
    *'COMMIT=YES'*) ;;
    *) printf 'HOLD=PERSISTED_REPORT_COMMIT_MISSING\n'; exit 54 ;;
esac

printf '\nV4C3R1_PROGRESS_BUDGET_REFLECTION_REPORT_PLAN_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_PROGRESS_BUDGET_DECISION=PASS_IN_THREE_INVOCATION_FIXTURE_SCOPE\n'
printf 'NATIVE_CORPUS_STATE_SELF_ASSESSMENT=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_REPORT_COMMIT=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_NEXT_PLAN_SELECTION=PASS_IN_FIXTURE_SCOPE\n'
printf 'NATIVE_OBSERVE_PAUSE_RESUME=PASS_IN_TWO_SECOND_FIXTURE_SCOPE\n'
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_PERCENT_CALCULATION=NO\n'
printf 'HOST_SLEEP=NO\n'
printf 'UNDERSTANDING_PROXY_PERCENT=NOT_COMPUTABLE_FROM_CURRENT_MACHINE_EVIDENCE\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'REAL_180_SECOND_OBSERVE_PAUSE=NOT_YET_PROVEN\n'
printf 'REAL_C2R2_CONTINUOUS_INTEGRATION=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=RUN_REAL_180_SECOND_NATIVE_PAUSE_GATE_THEN_INTEGRATE_WITH_PERSISTENT_C2R2_SHADOW\n'
