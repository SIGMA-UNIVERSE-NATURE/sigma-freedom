#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3R3_EVIDENCE_FIRST_SELF_VIEW_REPORTER_PREFLIGHT"
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

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigma"
EXPECTED_BLOB=c4dd4c3c0b71df46c6e75d3e1c8bc9a782af8f16
REPO_SRC="$REPO/$REL"
SRC="$E/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigma"
BC="$E/SIGMA_V4_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_V4C3R3.sigmab"

mkdir -p "$E" "$RAW" "$CORPUS" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R3_SELF_VIEW_REPORTER_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3R3_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_REPORT_SUMMARIZATION=NO\n'
printf 'HOST_REPORT_TRANSLATION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'FIXTURE_ROLE=MECHANICAL_DYNAMIC_STATE_AND_POST_VM_OPERATIONAL_ORACLE_ONLY\n'
printf 'SEMANTIC_SELF_ASSESSMENT_ORACLE=NO\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=REPORTER_SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(git -C "$REPO" hash-object "$REPO_SRC")
printf 'REPORTER_SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'REPORTER_SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=REPORTER_SOURCE_BLOB_MISMATCH\n'; exit 24; }

FORCED_LITERAL_COUNT=0
for TOKEN in \
    'NOT_PROVEN' \
    'NOT_UNDERSTOOD' \
    'UNDERSTOOD' \
    'CHUA_DUOC_CHUNG_MINH' \
    'SEMANTIC_UNDERSTANDING'
do
    C=$("$P/bin/grep" -F -c -- "$TOKEN" "$REPO_SRC" 2>/dev/null || true)
    FORCED_LITERAL_COUNT=$((FORCED_LITERAL_COUNT + C))
done
printf 'FORCED_SEMANTIC_VERDICT_LITERAL_COUNT=%s\n' "$FORCED_LITERAL_COUNT"
[ "$FORCED_LITERAL_COUNT" -eq 0 ] || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_LITERAL_PRESENT\n'; exit 25; }

PLAN_EXPLANATION_COUNT=$("$P/bin/grep" -F -c -- 'plan_explanation' "$REPO_SRC" 2>/dev/null || true)
printf 'TEACHER_PLAN_EXPLANATION_FUNCTION_COUNT=%s\n' "$PLAN_EXPLANATION_COUNT"
[ "$PLAN_EXPLANATION_COUNT" -eq 0 ] || { printf 'HOLD=TEACHER_PLAN_EXPLANATION_PRESENT\n'; exit 26; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=REPORTER_SOURCE_COPY_FAILED\n'; exit 27; }
INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
printf 'REPORTER_INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=REPORTER_INSTALLED_BLOB_MISMATCH\n'; exit 28; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'REPORTER_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=REPORTER_SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=REPORTER_BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
printf 'REPORTER_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

# Dynamic fixture initialization occurs only after source/bytecode freeze.
printf 'doc a\n' > "$RAW/doc_a.document"
printf 'doc b\n' > "$RAW/doc_b.document"
printf 'doc c\n' > "$RAW/doc_c.document"
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
    SIGMA_V4B4R2_CONTEXT_TEXT.memory \
    SIGMA_V4B4R2_STATUS.memory \
    SIGMA_V4B4R2_BEST_WIDTH.memory \
    SIGMA_V4B4R2_BEST_SUPPORT.memory \
    SIGMA_V4B4R2_LAST_EVIDENCE.memory \
    SIGMA_V4C3R1_CYCLE.memory \
    SIGMA_V4C3R1_PLAN.memory \
    SIGMA_V4C3R1_PAUSE_SECONDS.memory \
    SIGMA_V4C3R1_STATUS.memory
do
    : > "$E/$F"
done

printf '%s' "$RAW" > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
printf '%s' "$CORPUS" > "$E/SIGMA_V4C2R2_STATE_DIR.memory"
printf '%s' 'LEARN' > "$E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' 'doc_b' > "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' 'NATIVE_EXACT_CORPUS_LINE_READ_REQUEST_EMITTED' > "$E/SIGMA_V4C2R2_STATUS.memory"
printf '%s' 'doc_b:line_7' > "$E/SIGMA_V4B4R2_CONTEXT_ID.memory"
printf '%s' 'alpha beta beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi omicron pi rho sigma tau upsilon phi chi psi omega extra' > "$E/SIGMA_V4B4R2_CONTEXT_TEXT.memory"
printf '%s' 'TOKEN_WINDOW_PROGRESS' > "$E/SIGMA_V4B4R2_STATUS.memory"
printf '%s' '||||' > "$E/SIGMA_V4B4R2_BEST_WIDTH.memory"
printf '%s' '|||' > "$E/SIGMA_V4B4R2_BEST_SUPPORT.memory"
printf '%s' 'CTX=doc_b:line_7 || TOK=| || NEXTTOK=|| || BEST2=beta beta || BEST3=alpha beta beta || BEST4=alpha beta beta gamma || BEST=alpha beta beta gamma || WIDTH=|||| || SUPPORT=||| || PAIR_OCC=|||| || TRIPLE_OCC=||| || QUAD_OCC=|| || COMMIT=YES' > "$E/SIGMA_V4B4R2_LAST_EVIDENCE.memory"
printf '%s' '|||' > "$E/SIGMA_V4C3R1_CYCLE.memory"
printf '%s' 'PLAN_RESUME_ACTIVE_DOCUMENT' > "$E/SIGMA_V4C3R1_PLAN.memory"
printf '%s' '|||' > "$E/SIGMA_V4C3R1_PAUSE_SECONDS.memory"
printf '%s' 'REPORT_AND_PLAN_COMMITTED_BEFORE_PAUSE' > "$E/SIGMA_V4C3R1_STATUS.memory"

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

assert_no_forced_semantic_verdict() {
    OUT="$1"
    if "$P/bin/grep" -E 'NOT_PROVEN|NOT_UNDERSTOOD|UNDERSTOOD|CHUA_DUOC_CHUNG_MINH|SEMANTIC_UNDERSTANDING' "$OUT" >/dev/null 2>&1; then
        return 1
    fi
    return 0
}

# CASE_A: native operational self-view must derive active learning from runtime evidence.
run_vm CASE_A || { printf 'HOLD=REPORTER_CASE_A_VM_FAILED\n'; exit 40; }
A="$LOG/CASE_A.log"
"$P/bin/grep" -F -x 'REPORTER_STATUS EVIDENCE_FIRST_SELF_VIEW_REPORT_EMITTED' "$A" >/dev/null 2>&1 || { printf 'HOLD=REPORTER_STATUS_NOT_EMITTED\n'; exit 41; }
"$P/bin/grep" -F -x 'Chu ky 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=CYCLE_INDEX_MISMATCH\n'; exit 42; }
"$P/bin/grep" -F -x 'Tai lieu dang xu ly doc_b' "$A" >/dev/null 2>&1 || { printf 'HOLD=ACTIVE_DOCUMENT_MISMATCH\n'; exit 43; }
"$P/bin/grep" -F -x 'Context dang xu ly doc_b:line_7' "$A" >/dev/null 2>&1 || { printf 'HOLD=CONTEXT_ID_MISMATCH\n'; exit 44; }
"$P/bin/grep" -F 'Trich doan context alpha beta beta gamma delta epsilon' "$A" >/dev/null 2>&1 || { printf 'HOLD=BOUNDED_TEXT_PREVIEW_NOT_OBSERVED\n'; exit 45; }
"$P/bin/grep" -F -x 'Structural span alpha beta beta gamma' "$A" >/dev/null 2>&1 || { printf 'HOLD=BEST_SPAN_EXTRACTION_MISMATCH\n'; exit 46; }
"$P/bin/grep" -F -x 'Do rong span 4' "$A" >/dev/null 2>&1 || { printf 'HOLD=SPAN_WIDTH_MISMATCH\n'; exit 47; }
"$P/bin/grep" -F -x 'Structural support 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=STRUCTURAL_SUPPORT_MISMATCH\n'; exit 48; }
"$P/bin/grep" -F -x 'Trang thai structural signal REPEATED_STRUCTURAL_SIGNAL' "$A" >/dev/null 2>&1 || { printf 'HOLD=STRUCTURAL_SIGNAL_MISMATCH\n'; exit 49; }
"$P/bin/grep" -F -x 'Document da phat hien 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=DISCOVERED_COUNT_MISMATCH\n'; exit 50; }
"$P/bin/grep" -F -x 'Document da complete 1' "$A" >/dev/null 2>&1 || { printf 'HOLD=COMPLETE_COUNT_MISMATCH\n'; exit 51; }
"$P/bin/grep" -F -x 'Document con mo 2' "$A" >/dev/null 2>&1 || { printf 'HOLD=OPEN_COUNT_MISMATCH\n'; exit 52; }
"$P/bin/grep" -F -x 'Trang thai evidence EVIDENCE_PRESENT' "$A" >/dev/null 2>&1 || { printf 'HOLD=EVIDENCE_STATE_MISMATCH\n'; exit 53; }
"$P/bin/grep" -F -x 'Native self view ACTIVE_LEARNING_CONTINUES' "$A" >/dev/null 2>&1 || { printf 'HOLD=ACTIVE_SELF_VIEW_MISMATCH\n'; exit 54; }
"$P/bin/grep" -F -x 'Native plan PLAN_RESUME_ACTIVE_DOCUMENT' "$A" >/dev/null 2>&1 || { printf 'HOLD=NATIVE_PLAN_DISPLAY_MISMATCH\n'; exit 55; }
assert_no_forced_semantic_verdict "$A" || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_IN_CASE_A\n'; exit 56; }

# CASE_B: a runtime HOLD changes native operational self-view without source change.
: > "$CORPUS/doc_b.hold"
printf '%s' 'PRIORITY' > "$E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' '' > "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' 'WAITING_NATIVE_RECOVERY' > "$E/SIGMA_V4B4R2_STATUS.memory"
printf '%s' 'PLAN_NATIVE_HOLD_RECOVERY_REQUIRED' > "$E/SIGMA_V4C3R1_PLAN.memory"
run_vm CASE_B || { printf 'HOLD=REPORTER_CASE_B_VM_FAILED\n'; exit 57; }
B="$LOG/CASE_B.log"
"$P/bin/grep" -F -x 'Document dang HOLD 1' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_HOLD_COUNT_NOT_OBSERVED\n'; exit 58; }
"$P/bin/grep" -F -x 'Native self view RECOVERY_NEEDED' "$B" >/dev/null 2>&1 || { printf 'HOLD=RECOVERY_SELF_VIEW_MISMATCH\n'; exit 59; }
"$P/bin/grep" -F -x 'Native plan PLAN_NATIVE_HOLD_RECOVERY_REQUIRED' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_PLAN_NOT_OBSERVED\n'; exit 60; }
assert_no_forced_semantic_verdict "$B" || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_IN_CASE_B\n'; exit 61; }

# CASE_C: same source, different runtime evidence -> all discovered docs complete.
rm -f -- "$CORPUS/doc_b.hold"
: > "$CORPUS/doc_b.complete"
: > "$CORPUS/doc_c.complete"
printf '%s' 'PRIORITY' > "$E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' '' > "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' 'CONTEXT_COMPLETE' > "$E/SIGMA_V4B4R2_STATUS.memory"
printf '%s' 'PLAN_REEVALUATE_CORPUS' > "$E/SIGMA_V4C3R1_PLAN.memory"
run_vm CASE_C || { printf 'HOLD=REPORTER_CASE_C_VM_FAILED\n'; exit 62; }
C="$LOG/CASE_C.log"
"$P/bin/grep" -F -x 'Document da complete 3' "$C" >/dev/null 2>&1 || { printf 'HOLD=ALL_COMPLETE_COUNT_NOT_OBSERVED\n'; exit 63; }
"$P/bin/grep" -F -x 'Document con mo 0' "$C" >/dev/null 2>&1 || { printf 'HOLD=ALL_COMPLETE_OPEN_COUNT_MISMATCH\n'; exit 64; }
"$P/bin/grep" -F -x 'Native self view CURRENT_CORPUS_COMPLETE' "$C" >/dev/null 2>&1 || { printf 'HOLD=COMPLETE_SELF_VIEW_MISMATCH\n'; exit 65; }
assert_no_forced_semantic_verdict "$C" || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_IN_CASE_C\n'; exit 66; }

# NEGATIVE: missing native corpus path must refuse without semantic verdict injection.
: > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
run_vm NEGATIVE || { printf 'HOLD=REPORTER_NEGATIVE_VM_FAILED\n'; exit 67; }
N="$LOG/NEGATIVE.log"
"$P/bin/grep" -F -x 'REPORTER_STATUS REFUSE_INVALID_NATIVE_EVIDENCE_STATE' "$N" >/dev/null 2>&1 || { printf 'HOLD=NEGATIVE_REFUSAL_NOT_OBSERVED\n'; exit 68; }
assert_no_forced_semantic_verdict "$N" || { printf 'HOLD=FORCED_SEMANTIC_VERDICT_IN_NEGATIVE\n'; exit 69; }

SOURCE_AFTER=$(git -C "$REPO" hash-object "$REPO_SRC")
BYTECODE_AFTER=$(hash1 "$BC")
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$([ "$SOURCE_AFTER" = "$EXPECTED_BLOB" ] && printf YES || printf NO)"
printf 'BYTECODE_SHA256_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_AFTER"
[ "$SOURCE_AFTER" = "$EXPECTED_BLOB" ] || { printf 'HOLD=SOURCE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 70; }

printf '\nV4C3R3_NATIVE_EVIDENCE_FIRST_SELF_VIEW_REPORTER_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_HUMAN_READABLE_EVIDENCE_REPORT=PASS_IN_FOUR_CASE_FIXTURE_SCOPE\n'
printf 'NATIVE_OPERATIONAL_SELF_VIEW=PASS_IN_THREE_DYNAMIC_EVIDENCE_STATES_SCOPE\n'
printf 'NATIVE_SELF_VIEW_OUTPUT_DEPENDS_ON_RUNTIME_EVIDENCE=PASS\n'
printf 'NATIVE_BOUNDED_CONTEXT_PREVIEW=PASS_IN_CASE_A_SCOPE\n'
printf 'NATIVE_STRUCTURAL_BEST_SPAN_EXTRACTION=PASS_IN_CASE_A_SCOPE\n'
printf 'FORCED_SEMANTIC_VERDICT_IN_NATIVE_SOURCE=NO\n'
printf 'FORCED_SEMANTIC_VERDICT_IN_VM_OUTPUT=NO\n'
printf 'TEACHER_PLAN_EXPLANATION_IN_NATIVE_SOURCE=NO\n'
printf 'HOST_REPORT_SUMMARIZATION=NO\n'
printf 'HOST_REPORT_TRANSLATION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'BASH_LEARNING=NO\n'
printf 'GPT_AS_SIGMA_COGNITION=NO\n'
printf 'REPORTER_LEARNING=NO\n'
printf 'REPORTER_WORK_SELECTION=NO\n'
printf 'REPOSITORY_SEMANTIC_UNDERSTANDING_CLAIM=NOT_PROVEN\n'
printf 'REAL_C2R2_CONTINUOUS_R3_REPORT_INTEGRATION=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=INTEGRATE_R3_REPORTER_AT_NATIVE_C3_REFLECTION_BOUNDARY_THEN_BUILD_DNA15_DNA25_SELF_ADAPTATION_CONTROLLER\n'
