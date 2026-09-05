#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="$HOME_SIGMA/sigma-freedom-write"
BASE="$HOME_SIGMA/SIGMA_V4C3R2_HUMAN_OBSERVER_REPORTER_PREFLIGHT"
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

REL="SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_HUMAN_OBSERVER_REPORTER_V4C3R2.sigma"
EXPECTED_BLOB=37301874ec69dc5616bd91a08c9b0efdb29d17a2
REPO_SRC="$REPO/$REL"
SRC="$E/SIGMA_V4_NATIVE_HUMAN_OBSERVER_REPORTER_V4C3R2.sigma"
BC="$E/SIGMA_V4_NATIVE_HUMAN_OBSERVER_REPORTER_V4C3R2.sigmab"

mkdir -p "$E" "$RAW" "$CORPUS" "$LOG"

exec 9>"$LOCK"
if ! "$P/bin/flock" -n 9; then
    printf 'HOLD=V4C3R2_HUMAN_REPORTER_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
fi

hash1() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

SIGMAC_SHA=$(hash1 "$SIGMAC")
VM_SHA=$(hash1 "$VM")
printf 'SIGMA_PHASE=V4C3R2_NATIVE_HUMAN_OBSERVER_REPORTER_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$SIGMAC_SHA"
printf 'VM_SHA256=%s\n' "$VM_SHA"
printf 'HOST_REPORT_SUMMARIZATION=NO\n'
printf 'HOST_REPORT_TRANSLATION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'FIXTURE_ROLE=MECHANICAL_DYNAMIC_STATE_AND_POST_VM_ORACLE_ONLY\n'

[ "$SIGMAC_SHA" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$VM_SHA" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ -f "$REPO_SRC" ] || { printf 'HOLD=REPORTER_SOURCE_MISSING\n'; exit 23; }

ACTUAL_BLOB=$(git -C "$REPO" hash-object "$REPO_SRC")
printf 'REPORTER_SOURCE_GIT_BLOB=%s\n' "$ACTUAL_BLOB"
printf 'REPORTER_SOURCE_SHA256=%s\n' "$(hash1 "$REPO_SRC")"
[ "$ACTUAL_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=REPORTER_SOURCE_BLOB_MISMATCH\n'; exit 24; }

cp -- "$REPO_SRC" "$SRC" || { printf 'HOLD=REPORTER_SOURCE_COPY_FAILED\n'; exit 25; }
INSTALLED_BLOB=$(git -C "$REPO" hash-object "$SRC")
printf 'REPORTER_INSTALLED_GIT_BLOB=%s\n' "$INSTALLED_BLOB"
[ "$INSTALLED_BLOB" = "$EXPECTED_BLOB" ] || { printf 'HOLD=REPORTER_INSTALLED_BLOB_MISMATCH\n'; exit 26; }

rm -f -- "$BC.partial"
"$SIGMAC" "$SRC" "$BC.partial"
RC=$?
printf 'REPORTER_SIGMAC_RC=%s\n' "$RC"
[ "$RC" -eq 0 ] || { printf 'HOLD=REPORTER_SIGMAC_FAILED\n'; exit 30; }
[ -s "$BC.partial" ] || { printf 'HOLD=REPORTER_BYTECODE_EMPTY\n'; exit 31; }
mv -f -- "$BC.partial" "$BC" || exit 32
chmod 0400 "$BC" || exit 33
printf 'REPORTER_BYTECODE_SHA256=%s\n' "$(hash1 "$BC")"

# Isolated dynamic corpus fixture.
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

run_vm CASE_A || { printf 'HOLD=REPORTER_CASE_A_VM_FAILED\n'; exit 40; }
A="$LOG/CASE_A.log"
"$P/bin/grep" -F -x 'REPORTER_STATUS HUMAN_OBSERVER_REPORT_EMITTED' "$A" >/dev/null 2>&1 || { printf 'HOLD=REPORTER_STATUS_NOT_EMITTED\n'; exit 41; }
"$P/bin/grep" -F -x 'Chu ky tu danh gia 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=CYCLE_INDEX_MISMATCH\n'; exit 42; }
"$P/bin/grep" -F -x 'Tai lieu dang hoc doc_b' "$A" >/dev/null 2>&1 || { printf 'HOLD=ACTIVE_DOCUMENT_MISMATCH\n'; exit 43; }
"$P/bin/grep" -F -x 'Context dang xu ly doc_b:line_7' "$A" >/dev/null 2>&1 || { printf 'HOLD=CONTEXT_ID_MISMATCH\n'; exit 44; }
"$P/bin/grep" -F 'Trich doan context alpha beta beta gamma delta epsilon' "$A" >/dev/null 2>&1 || { printf 'HOLD=BOUNDED_TEXT_PREVIEW_NOT_OBSERVED\n'; exit 45; }
"$P/bin/grep" -F -x 'Structural span noi bat alpha beta beta gamma' "$A" >/dev/null 2>&1 || { printf 'HOLD=BEST_SPAN_EXTRACTION_MISMATCH\n'; exit 46; }
"$P/bin/grep" -F -x 'Do rong span - so token 4' "$A" >/dev/null 2>&1 || { printf 'HOLD=SPAN_WIDTH_MISMATCH\n'; exit 47; }
"$P/bin/grep" -F -x 'So lan structural support trong cua so 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=STRUCTURAL_SUPPORT_MISMATCH\n'; exit 48; }
"$P/bin/grep" -F -x 'Document da phat hien 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=DISCOVERED_COUNT_MISMATCH\n'; exit 49; }
"$P/bin/grep" -F -x 'Document da profile 2' "$A" >/dev/null 2>&1 || { printf 'HOLD=PROFILE_COUNT_MISMATCH\n'; exit 50; }
"$P/bin/grep" -F -x 'Document da complete 1' "$A" >/dev/null 2>&1 || { printf 'HOLD=COMPLETE_COUNT_MISMATCH\n'; exit 51; }
"$P/bin/grep" -F -x 'Document dang HOLD 0' "$A" >/dev/null 2>&1 || { printf 'HOLD=HOLD_COUNT_MISMATCH\n'; exit 52; }
"$P/bin/grep" -F -x 'Document co evidence 2' "$A" >/dev/null 2>&1 || { printf 'HOLD=EVIDENCE_COUNT_MISMATCH\n'; exit 53; }
"$P/bin/grep" -F -x 'Ma ke hoach native PLAN_RESUME_ACTIVE_DOCUMENT' "$A" >/dev/null 2>&1 || { printf 'HOLD=NATIVE_PLAN_CODE_MISMATCH\n'; exit 54; }
"$P/bin/grep" -F -x 'Giai thich de nguoi doc Tiep tuc tai lieu dang hoc do van con cong viec chua xong.' "$A" >/dev/null 2>&1 || { printf 'HOLD=NATIVE_PLAN_EXPLANATION_MISMATCH\n'; exit 55; }
"$P/bin/grep" -F -x 'So giay pause native 3' "$A" >/dev/null 2>&1 || { printf 'HOLD=PAUSE_SECONDS_MISMATCH\n'; exit 56; }
"$P/bin/grep" -F -x 'SEMANTIC_UNDERSTANDING NOT_PROVEN' "$A" >/dev/null 2>&1 || { printf 'HOLD=SEMANTIC_CLAIM_LIMIT_MISSING\n'; exit 57; }

# Dynamic input: plan/context change must alter observer output without changing source.
printf '%s' 'PRIORITY' > "$E/SIGMA_V4C2R2_PHASE.memory"
printf '%s' '' > "$E/SIGMA_V4C2R2_ACTIVE_DOC.memory"
printf '%s' 'other_doc:line_2' > "$E/SIGMA_V4B4R2_CONTEXT_ID.memory"
printf '%s' 'new evidence changes the human readable view' > "$E/SIGMA_V4B4R2_CONTEXT_TEXT.memory"
printf '%s' 'PLAN_REEVALUATE_CORPUS' > "$E/SIGMA_V4C3R1_PLAN.memory"
run_vm CASE_B || { printf 'HOLD=REPORTER_CASE_B_VM_FAILED\n'; exit 58; }
B="$LOG/CASE_B.log"
"$P/bin/grep" -F -x 'Giai doan corpus PRIORITY' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_PHASE_CHANGE_NOT_OBSERVED\n'; exit 59; }
"$P/bin/grep" -F -x 'Context dang xu ly other_doc:line_2' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_CONTEXT_CHANGE_NOT_OBSERVED\n'; exit 60; }
"$P/bin/grep" -F -x 'Ma ke hoach native PLAN_REEVALUATE_CORPUS' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_PLAN_CHANGE_NOT_OBSERVED\n'; exit 61; }
"$P/bin/grep" -F -x 'Giai thich de nguoi doc Quet lai corpus de tim cong viec native con hop le.' "$B" >/dev/null 2>&1 || { printf 'HOLD=DYNAMIC_PLAN_EXPLANATION_NOT_OBSERVED\n'; exit 62; }

# Negative input: remove native raw-dir path and require reporter refusal.
: > "$E/SIGMA_V4C2R2_RAW_DIR.memory"
run_vm NEGATIVE || { printf 'HOLD=REPORTER_NEGATIVE_VM_FAILED\n'; exit 63; }
N="$LOG/NEGATIVE.log"
"$P/bin/grep" -F -x 'REPORTER_STATUS REFUSE_MISSING_NATIVE_CORPUS_PATHS' "$N" >/dev/null 2>&1 || { printf 'HOLD=NEGATIVE_REFUSAL_NOT_OBSERVED\n'; exit 64; }

printf '\nV4C3R2_NATIVE_HUMAN_OBSERVER_REPORTER_PREFLIGHT=PASS\n'
printf 'LOCKED_SIGMAC_EXECUTION=PASS\n'
printf 'LOCKED_VM_EXECUTION=PASS\n'
printf 'NATIVE_HUMAN_READABLE_REPORT=PASS_IN_THREE_CASE_FIXTURE_SCOPE\n'
printf 'NATIVE_BOUNDED_CONTEXT_PREVIEW=PASS_IN_CASE_A_SCOPE\n'
printf 'NATIVE_STRUCTURAL_BEST_SPAN_EXTRACTION=PASS_IN_CASE_A_SCOPE\n'
printf 'NATIVE_CORPUS_COUNT_DISPLAY=PASS_IN_CASE_A_SCOPE\n'
printf 'NATIVE_PLAN_CODE_EXPLANATION=PASS_IN_DYNAMIC_CASES_SCOPE\n'
printf 'DYNAMIC_INPUT_OUTPUT_CHANGE=PASS\n'
printf 'NEGATIVE_INPUT_REFUSAL=PASS\n'
printf 'HOST_REPORT_SUMMARIZATION=NO\n'
printf 'HOST_REPORT_TRANSLATION=NO\n'
printf 'HOST_SELF_ASSESSMENT=NO\n'
printf 'HOST_NEXT_WORK_SELECTION=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'REPORTER_LEARNING=NO\n'
printf 'REPORTER_WORK_SELECTION=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'REAL_C2R2_CONTINUOUS_HUMAN_REPORT_INTEGRATION=NOT_YET_PROVEN\n'
printf 'NEXT_ACTION=INTEGRATE_ADMITTED_REPORTER_AT_NATIVE_C3_REFLECTION_BOUNDARY\n'
