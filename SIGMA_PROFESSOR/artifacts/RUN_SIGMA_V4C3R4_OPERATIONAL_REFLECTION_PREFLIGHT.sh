#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3R4_OPERATIONAL_REFLECTION_PREFLIGHT"
LOCK="$BASE/preflight.lock"
RUN_ID="$("$P/bin/date" +%s).$$"
STATE="$BASE/run.$RUN_ID"
COMPILE_BRAIN="$STATE/compile/BRAIN/EXTRA BRAIN_OPPO_24826"
COMPILE_E="$COMPILE_BRAIN/.sigma_exec"
LOG="$STATE/log"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigma"
EXPECTED_BLOB=7b826ace6c6f6559a10e6fbd7e7b2d96af1a75cf
REPO_SRC="$REPO/$REL"
SRC="$COMPILE_E/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigma"
BC="$COMPILE_E/SIGMA_V4_OPERATIONAL_REFLECTION_PLAN_CONTROLLER_V4C3R4.sigmab"

mkdir -p "$COMPILE_E" "$LOG"
exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R4_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() { "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }
blob1() { git -C "$REPO" hash-object "$1"; }

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3R4_OPERATIONAL_REFLECTION_PLAN_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'FIXTURE_ROLE=MECHANICAL_DYNAMIC_OPERATIONAL_STATE_ONLY\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=C3R4_SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(blob1 "$REPO_SRC")
printf 'C3R4_SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'C3R4_SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=C3R4_SOURCE_BLOB_MISMATCH\n'; exit 24; }

FORCED_COUNT=0
for TOKEN in \
    'SEMANTIC_UNDERSTANDING' \
    'UNDERSTANDING_PROXY' \
    'NOT_PROVEN' \
    'NOT_UNDERSTOOD' \
    'UNDERSTOOD' \
    'CHUA_DUOC_CHUNG_MINH'
do
    C=$("$P/bin/grep" -F -c -- "$TOKEN" "$REPO_SRC" 2>/dev/null || true)
    FORCED_COUNT=$((FORCED_COUNT + C))
done
printf 'FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=%s\n' "$FORCED_COUNT"
[ "$FORCED_COUNT" -eq 0 ] || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_LITERAL_PRESENT\n'; exit 25; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=C3R4_SOURCE_COPY_FAILED\n'; exit 26; }
INSTALLED_BLOB=$(blob1 "$SRC")
printf 'C3R4_INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=C3R4_INSTALLED_BLOB_MISMATCH\n'; exit 27; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'C3R4_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=C3R4_SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=C3R4_BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
BYTECODE_SHA=$(hash1 "$BC")
printf 'C3R4_BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

BYTECODE_FORCED_COUNT=0
for TOKEN in \
    'SEMANTIC_UNDERSTANDING' \
    'UNDERSTANDING_PROXY' \
    'NOT_PROVEN' \
    'NOT_UNDERSTOOD' \
    'UNDERSTOOD' \
    'CHUA_DUOC_CHUNG_MINH'
do
    if "$P/bin/grep" -a -F -- "$TOKEN" "$BC" >/dev/null 2>&1; then
        BYTECODE_FORCED_COUNT=$((BYTECODE_FORCED_COUNT + 1))
    fi
done
printf 'FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE_COUNT=%s\n' "$BYTECODE_FORCED_COUNT"
[ "$BYTECODE_FORCED_COUNT" -eq 0 ] || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE\n'; exit 34; }

setup_case() {
    NAME="$1"; PHASE="$2"; ACTIVE_DOC="$3"; B4_STATUS="$4"; HOLD_FLAG="$5"
    CASE_ROOT="$STATE/$NAME"
    CASE_BRAIN="$CASE_ROOT/BRAIN/EXTRA BRAIN_OPPO_24826"
    CASE_E="$CASE_BRAIN/.sigma_exec"
    CASE_RAW="$CASE_ROOT/raw"
    CASE_CORPUS="$CASE_ROOT/corpus_state"
    mkdir -p "$CASE_E" "$CASE_RAW" "$CASE_CORPUS"
    cp -- "$BC" "$CASE_E/controller.sigmab" || return 1

    printf 'doc a\n' > "$CASE_RAW/doc_a.document"
    printf 'doc b\n' > "$CASE_RAW/doc_b.document"
    printf 'doc c\n' > "$CASE_RAW/doc_c.document"
    : > "$CASE_CORPUS/doc_a.profile"
    : > "$CASE_CORPUS/doc_b.profile"
    : > "$CASE_CORPUS/doc_a.complete"
    : > "$CASE_CORPUS/doc_a.evidence"
    : > "$CASE_CORPUS/doc_b.evidence"
    if [ "$HOLD_FLAG" = YES ]; then : > "$CASE_CORPUS/doc_b.hold"; fi

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
        : > "$CASE_E/$F"
    done

    printf '%s' "$CASE_RAW" > "$CASE_E/SIGMA_V4C2R2_RAW_DIR.memory"
    printf '%s' "$CASE_CORPUS" > "$CASE_E/SIGMA_V4C2R2_STATE_DIR.memory"
    printf '%s' "$PHASE" > "$CASE_E/SIGMA_V4C2R2_PHASE.memory"
    printf '%s' "$ACTIVE_DOC" > "$CASE_E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
    printf '%s' 'NATIVE_EXACT_CORPUS_LINE_READ_REQUEST_EMITTED' > "$CASE_E/SIGMA_V4C2R2_STATUS.memory"
    printf '%s' 'doc_b:line_7' > "$CASE_E/SIGMA_V4B4R2_CONTEXT_ID.memory"
    : > "$CASE_E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
    printf '%s' "$B4_STATUS" > "$CASE_E/SIGMA_V4B4R2_STATUS.memory"
    printf '%s' '||||' > "$CASE_E/SIGMA_V4B4R2_BEST_WIDTH.memory"
    printf '%s' '|||' > "$CASE_E/SIGMA_V4B4R2_BEST_SUPPORT.memory"
    printf '%s' '|' > "$CASE_E/SIGMA_V4C3R1_PROGRESS_BUDGET.memory"
    printf '%s' '||' > "$CASE_E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"

    printf '%s\n' "$CASE_BRAIN"
}

run_case_vm() {
    LABEL="$1"; BRAIN="$2"; OUT="$3"
    (
        cd "$BRAIN" || exit 70
        "$VM" ".sigma_exec/controller.sigmab"
    ) > "$OUT" 2>&1
    RC=$?
    printf '%s_VM_RC=%s LOG=%s\n' "$LABEL" "$RC" "$OUT"
    "$P/bin/cat" "$OUT"
    return "$RC"
}

assert_no_forced_output() {
    OUT="$1"
    if "$P/bin/grep" -E 'SEMANTIC_UNDERSTANDING|UNDERSTANDING_PROXY|NOT_PROVEN|NOT_UNDERSTOOD|UNDERSTOOD|CHUA_DUOC_CHUNG_MINH' "$OUT" >/dev/null 2>&1; then
        return 1
    fi
    return 0
}

run_dynamic_case() {
    NAME="$1"; PHASE="$2"; ACTIVE_DOC="$3"; B4_STATUS="$4"; HOLD_FLAG="$5"; EXPECTED_PLAN="$6"
    BRAIN=$(setup_case "$NAME" "$PHASE" "$ACTIVE_DOC" "$B4_STATUS" "$HOLD_FLAG") || return 80
    E="$BRAIN/.sigma_exec"
    BASELOG="$LOG/$NAME.baseline.log"
    REFLOG="$LOG/$NAME.reflect.log"

    run_case_vm "${NAME}_BASELINE" "$BRAIN" "$BASELOG" || return 81
    "$P/bin/grep" -F -x 'V4C3R4_STATUS BASELINE_ESTABLISHED' "$BASELOG" >/dev/null 2>&1 || return 82
    assert_no_forced_output "$BASELOG" || return 83

    printf '%s' '|' > "$E/SIGMA_V4B4R2_TOKEN_CURSOR.memory"
    run_case_vm "${NAME}_REFLECT" "$BRAIN" "$REFLOG" || return 84
    "$P/bin/grep" -F -x "NEXT_NATIVE_PLAN $EXPECTED_PLAN" "$REFLOG" >/dev/null 2>&1 || return 85
    "$P/bin/grep" -F -x 'REPORT_COMMIT YES' "$REFLOG" >/dev/null 2>&1 || return 86
    "$P/bin/grep" -F -x 'PAUSE_SECONDS 2' "$REFLOG" >/dev/null 2>&1 || return 87
    "$P/bin/grep" -F -x 'V4C3R4_STATUS OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' "$REFLOG" >/dev/null 2>&1 || return 88
    [ "$(cat "$E/SIGMA_V4C3R1_PLAN.memory")" = "$EXPECTED_PLAN" ] || return 89
    [ "$(cat "$E/SIGMA_V4C3R1_STATUS.memory")" = 'OBSERVE_PAUSE_COMPLETE_RESUME_LEARN' ] || return 90
    [ ! -s "$E/SIGMA_V4C3R1_PROGRESS.memory" ] || return 91
    REPORT_TEXT=$(cat "$E/SIGMA_V4C3R1_LAST_REPORT.memory")
    case "$REPORT_TEXT" in *"NEXT_PLAN=$EXPECTED_PLAN"*'COMMIT=YES'*) ;; *) return 92 ;; esac
    assert_no_forced_output "$REFLOG" || return 93
    if printf '%s' "$REPORT_TEXT" | "$P/bin/grep" -E 'SEMANTIC_UNDERSTANDING|UNDERSTANDING_PROXY|NOT_PROVEN|NOT_UNDERSTOOD|UNDERSTOOD|CHUA_DUOC_CHUNG_MINH' >/dev/null 2>&1; then return 94; fi
    return 0
}

run_dynamic_case CASE_ACTIVE LEARN doc_b TOKEN_WINDOW_PROGRESS NO PLAN_RESUME_ACTIVE_DOCUMENT || { RC=$?; printf 'HOLD=CASE_ACTIVE_FAILED RC=%s\n' "$RC"; exit 40; }
run_dynamic_case CASE_PRIORITY PRIORITY '' CONTEXT_COMPLETE NO PLAN_CONTINUE_NATIVE_GLOBAL_PRIORITY || { RC=$?; printf 'HOLD=CASE_PRIORITY_FAILED RC=%s\n' "$RC"; exit 41; }
run_dynamic_case CASE_HOLD PRIORITY '' TOKEN_WINDOW_PROGRESS YES PLAN_NATIVE_HOLD_RECOVERY_REQUIRED || { RC=$?; printf 'HOLD=CASE_HOLD_FAILED RC=%s\n' "$RC"; exit 42; }

NEG_ROOT="$STATE/NEGATIVE"
NEG_BRAIN="$NEG_ROOT/BRAIN/EXTRA BRAIN_OPPO_24826"
NEG_E="$NEG_BRAIN/.sigma_exec"
NEG_RAW="$NEG_ROOT/raw"
NEG_CORPUS="$NEG_ROOT/corpus_state"
mkdir -p "$NEG_E" "$NEG_RAW" "$NEG_CORPUS"
cp -- "$BC" "$NEG_E/controller.sigmab" || exit 43
for F in \
    SIGMA_V4C2R2_RAW_DIR.memory SIGMA_V4C2R2_STATE_DIR.memory SIGMA_V4C2R2_PHASE.memory SIGMA_V4C2R2_ACTIVE_DOC.memory SIGMA_V4C2R2_STATUS.memory \
    SIGMA_V4B4R2_CONTEXT_ID.memory SIGMA_V4B4R2_TOKEN_CURSOR.memory SIGMA_V4B4R2_STATUS.memory SIGMA_V4B4R2_BEST_WIDTH.memory SIGMA_V4B4R2_BEST_SUPPORT.memory \
    SIGMA_V4C3R1_INITIALIZED.memory SIGMA_V4C3R1_LAST_SEEN_PROGRESS_KEY.memory SIGMA_V4C3R1_PROGRESS.memory SIGMA_V4C3R1_CYCLE.memory SIGMA_V4C3R1_PROGRESS_BUDGET.memory SIGMA_V4C3R1_PAUSE_SECONDS.memory SIGMA_V4C3R1_LAST_REPORT.memory SIGMA_V4C3R1_PLAN.memory SIGMA_V4C3R1_STATUS.memory
do : > "$NEG_E/$F"; done
printf '%s' "$NEG_RAW" > "$NEG_E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$NEG_CORPUS" > "$NEG_E/SIGMA_V4C2R2_STATE_DIR.memory"
printf '%s' LEARN > "$NEG_E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' doc_b > "$NEG_E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' TOKEN_WINDOW_PROGRESS > "$NEG_E/SIGMA_V4B4R2_STATUS.memory"
printf '%s' X > "$NEG_E/SIGMA_V4C3R1_PROGRESS_BUDGET.memory"
printf '%s' '||' > "$NEG_E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"
NEGLOG="$LOG/NEGATIVE.log"
run_case_vm NEGATIVE "$NEG_BRAIN" "$NEGLOG" || { printf 'HOLD=NEGATIVE_VM_NONZERO\n'; exit 44; }
"$P/bin/grep" -F -x 'V4C3R4_STATUS REFUSE_INVALID_REFLECTION_STATE' "$NEGLOG" >/dev/null 2>&1 || { printf 'HOLD=NEGATIVE_REFUSAL_MISSING\n'; exit 45; }
assert_no_forced_output "$NEGLOG" || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_IN_NEGATIVE_OUTPUT\n'; exit 46; }

printf '\nV4C3R4_OPERATIONAL_REFLECTION_PLAN_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'FORCED_SEMANTIC_VERDICT_LITERAL_IN_SOURCE=NO\n'
printf 'FORCED_SEMANTIC_VERDICT_TOKEN_IN_BYTECODE=NO\n'
printf 'FORCED_SEMANTIC_VERDICT_IN_VM_OUTPUT=NO\n'
printf 'NATIVE_PROGRESS_BUDGET_DECISION=PASS_IN_DYNAMIC_FIXTURE_SCOPE\n'
printf 'NATIVE_OPERATIONAL_PLAN_CHANGES_WITH_RUNTIME_STATE=PASS_IN_THREE_STATE_SCOPE\n'
printf 'NATIVE_OPERATIONAL_REPORT_COMMIT=PASS_IN_THREE_STATE_SCOPE\n'
printf 'NATIVE_OBSERVE_PAUSE_RESUME=PASS_IN_TWO_SECOND_FIXTURE_SCOPE\n'
printf 'NEGATIVE_INVALID_STATE_REFUSAL=PASS\n'
printf 'STATE_SCHEMA_COMPATIBILITY_WITH_C3R1_NAMESPACE=YES_BY_EXACT_FILE_NAMES\n'
printf 'HOST_REFLECTION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'REAL_C2R2_CONTINUOUS_R3_REPORT_INTEGRATION=NOT_YET_PROVEN\n'
printf 'AUTONOMOUS_SELF_LEARNING_ADAPTATION=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=INTEGRATE_C3R4_AND_ADMITTED_R3_REPORTER_WITH_REAL_PERSISTENT_C2R2_CONTINUOUS_SHADOW\n'
