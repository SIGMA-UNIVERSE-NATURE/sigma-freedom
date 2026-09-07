#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_SOURCE=c0d54fe4c36f59ac1b4a1cd431e2078333ee5d28b8fa2f2fb2d5f1813e6beb34
EXPECTED_VNM02_SOURCE=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigma"
VNM02_SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_VNM_03_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM_03_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
actual_vnm02=$("$P/bin/sha256sum" "$VNM02_SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_UNIT_SELECTION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_NORMALIZATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'ACTIVE_PYTHON_COGNITION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=NA\n'
printf 'RESTART_REPLAY_TEST=YES_PURE_CAPABILITY\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"
printf 'DOWNSTREAM_VNM02_SOURCE_SHA256=%s\n' "$actual_vnm02"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=VNM_03_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$actual_vnm02" = "$EXPECTED_VNM02_SOURCE" ] || { printf 'HOLD=VNM_02_DOWNSTREAM_COMPATIBILITY_IDENTITY_MISMATCH\n'; exit 24; }

for forbidden in \
    'summarize' \
    'classify_topic' \
    'semantic_similarity' \
    'choose_lesson' \
    'score_knowledge' \
    'detect_knowledge_gap' \
    'choose_research_goal' \
    'decide_truth' \
    'select_candidate'
do
    if "$P/bin/grep" -F "$forbidden" "$SRC" >/dev/null 2>&1; then
        printf 'HOLD=FORBIDDEN_HOST_SEMANTIC_OPERATION_TOKEN\n'
        printf 'TOKEN=%s\n' "$forbidden"
        exit 25
    fi
done

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 26
[ -s "$BC.partial" ] || exit 27
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 28
"$P/bin/chmod" 0400 "$BC" || exit 29

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

# All UTF-8 units, sequence IDs, sources and sentinels below are generated after bytecode freeze.
DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

U_LEFT="trước-${DYN_TAG}"
U_FORM="điện-${DYN_TAG}"
U_RIGHT="sau-${DYN_TAG}"
U_TAIL="cuối-${DYN_TAG}"
U_ALT="mình-${DYN_TAG}"
U_ALT2="tôi-${DYN_TAG}"

V_LEFT="đầu-${DYN_TAG_2}"
V_FORM="học-${DYN_TAG_2}"
V_RIGHT="giữa-${DYN_TAG_2}"
V_TAIL="hết-${DYN_TAG_2}"

SRC_A="nguồn-${DYN_TAG}"
SRC_B="nguồn-${DYN_TAG_2}"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'DYNAMIC_TAG_SHA256=%s\n' "$(printf '%s' "$DYN_TAG" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"

if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" >/dev/null 2>&1; then
    printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'
    exit 30
fi

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
PURE_REPLAY_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
OUT=""
LAST_LOG=""
CASE1_OUTPUT_SHA=""
CASE16_OUTPUT_SHA=""
REPLAY_A_LOG_SHA=""
REPLAY_A_OUTPUT_SHA=""

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_03_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1"
    IN="$BASE/input/sequences.memory"
    OUT="$BASE/output/observations.memory"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$BASE/input" "$BASE/output"
    : > "$IN"
    : > "$OUT"
}

set_sequences() {
    : > "$IN"
    FIRST=1
    for LINE in "$@"; do
        if [ "$FIRST" -eq 0 ]; then
            printf '\n' >> "$IN"
        fi
        printf '%s' "$LINE" >> "$IN"
        FIRST=0
    done
}

run_vm() {
    LABEL="$1"
    LAST_LOG="$LOG/$LABEL.log"
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))
    (
        cd "$SANDBOX" || exit 90
        "$VM" "$BC"
    ) >"$LAST_LOG" 2>&1
    RC=$?

    printf '\n=== %s ===\n' "$LABEL"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$LAST_LOG"
    if [ -f "$OUT" ]; then
        printf '%s_OUTPUT_FILE_SHA256=%s\n' "$LABEL" "$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')"
        printf '%s_OUTPUT_FILE_BEGIN\n' "$LABEL"
        "$P/bin/cat" "$OUT"
        printf '\n%s_OUTPUT_FILE_END\n' "$LABEL"
    fi

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=VM_NONZERO\n' "$LABEL"
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STEP_LIMIT_HIT\n' "$LABEL"
        exit 51
    fi
}

oracle_start() {
    printf '%s_POST_VM_TEST_ORACLE_STARTED=YES\n' "$1"
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_OUTPUT\nEXPECTED=%s %s\n' "$CASE_NAME" "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact_output() {
    EXPECTED="$1"
    ACTUAL=$("$P/bin/cat" "$OUT")
    if [ "$ACTUAL" != "$EXPECTED" ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=OUTPUT_BYTES_MISMATCH\n' "$CASE_NAME"
        printf 'EXPECTED_OUTPUT=%s\n' "$EXPECTED"
        printf 'ACTUAL_OUTPUT=%s\n' "$ACTUAL"
        exit 61
    fi
}

pass_case() {
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
    printf '%s_POST_VM_ALIGNMENT=YES\n' "$1"
}

prefill_sentinel() {
    printf 'KEEP-%s-%s' "$DYN_TAG" "$1" > "$OUT"
}

expect_output_unchanged() {
    BEFORE="$1"
    AFTER=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
    if [ "$BEFORE" != "$AFTER" ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=REFUSAL_MUTATED_OUTPUT\n' "$CASE_NAME"
        exit 62
    fi
}

# 01 — valid 3-unit sequence -> exactly one derived local-context observation.
prepare_case CASE_001
SEQ1="seq-${DYN_TAG}-001"
set_sequences "SEQ||${SEQ1}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}||SOURCE||${SRC_A}"
run_vm CASE_001
oracle_start CASE_001
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
expect_line UNIQUE_SEQUENCE_COUNT 1
expect_line DERIVED_OBSERVATION_COUNT 1
expect_line CONTEXT_DERIVATION_OWNER SIGMA_NATIVE
EXPECT1="OBS||${SEQ1}:1||FORM||${U_FORM}||LEFT||${U_LEFT}||RIGHT||${U_RIGHT}||SOURCE||${SRC_A}"
expect_exact_output "$EXPECT1"
CASE1_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
pass_case CASE_001

# 02 — valid 4-unit sequence -> two interior observations, each context derived natively.
prepare_case CASE_002
SEQ2="seq-${DYN_TAG}-002"
set_sequences "SEQ||${SEQ2}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}~${U_TAIL}||SOURCE||${SRC_A}"
run_vm CASE_002
oracle_start CASE_002
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
expect_line DERIVED_OBSERVATION_COUNT 2
EXPECT2A="OBS||${SEQ2}:1||FORM||${U_FORM}||LEFT||${U_LEFT}||RIGHT||${U_RIGHT}||SOURCE||${SRC_A}"
EXPECT2B="OBS||${SEQ2}:2||FORM||${U_RIGHT}||LEFT||${U_FORM}||RIGHT||${U_TAIL}||SOURCE||${SRC_A}"
expect_exact_output "${EXPECT2A}
${EXPECT2B}"
pass_case CASE_002

# 03 — multiple sequences -> deterministic accumulation without host context extraction.
prepare_case CASE_003
SEQ3A="seq-${DYN_TAG}-003a"
SEQ3B="seq-${DYN_TAG}-003b"
set_sequences \
    "SEQ||${SEQ3A}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}~${U_TAIL}||SOURCE||${SRC_A}" \
    "SEQ||${SEQ3B}||UNITS||${V_LEFT}~${V_FORM}~${V_RIGHT}~${V_TAIL}||SOURCE||${SRC_B}"
run_vm CASE_003
oracle_start CASE_003
expect_line UNIQUE_SEQUENCE_COUNT 2
expect_line DERIVED_OBSERVATION_COUNT 4
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
pass_case CASE_003

# 04 — exact duplicate sequence ID+fingerprint is idempotent.
prepare_case CASE_004
SEQ4="seq-${DYN_TAG}-004"
LINE4="SEQ||${SEQ4}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}~${U_TAIL}||SOURCE||${SRC_A}"
set_sequences "$LINE4" "$LINE4"
run_vm CASE_004
oracle_start CASE_004
expect_line UNIQUE_SEQUENCE_COUNT 1
expect_line DUPLICATE_SEQUENCE_COUNT 1
expect_line DERIVED_OBSERVATION_COUNT 2
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
pass_case CASE_004

# 05 — same sequence ID with different fingerprint refuses atomically.
prepare_case CASE_005
SEQ5="seq-${DYN_TAG}-005"
set_sequences \
    "SEQ||${SEQ5}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}||SOURCE||${SRC_A}" \
    "SEQ||${SEQ5}||UNITS||${U_LEFT}~${U_ALT}~${U_RIGHT}||SOURCE||${SRC_A}"
prefill_sentinel CASE_005
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_005
oracle_start CASE_005
expect_line RESULT_STATUS REFUSED_SEQUENCE_ID_COLLISION
expect_line SEQUENCE_ID_COLLISION_COUNT 1
expect_line OUTPUT_MUTATED 0
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_005

# 06 — malformed outer record refuses.
prepare_case CASE_006
set_sequences "SEQ||bad-${DYN_TAG}||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}"
prefill_sentinel CASE_006
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_006
oracle_start CASE_006
expect_line RESULT_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_006

# 07 — fewer than three delimiter-defined units refuses.
prepare_case CASE_007
set_sequences "SEQ||seq-${DYN_TAG}-007||UNITS||${U_LEFT}~${U_FORM}||SOURCE||${SRC_A}"
prefill_sentinel CASE_007
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_007
oracle_start CASE_007
expect_line RESULT_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_007

# 08 — more than four delimiter-defined units refuses.
prepare_case CASE_008
set_sequences "SEQ||seq-${DYN_TAG}-008||UNITS||${U_LEFT}~${U_FORM}~${U_RIGHT}~${U_TAIL}~x-${DYN_TAG}||SOURCE||${SRC_A}"
prefill_sentinel CASE_008
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_008
oracle_start CASE_008
expect_line RESULT_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_008

# 09 — empty interior unit refuses.
prepare_case CASE_009
set_sequences "SEQ||seq-${DYN_TAG}-009||UNITS||${U_LEFT}~~${U_RIGHT}||SOURCE||${SRC_A}"
prefill_sentinel CASE_009
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_009
oracle_start CASE_009
expect_line RESULT_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_009

# 10 — empty batch yields no derived observation and does not overwrite output.
prepare_case CASE_010
prefill_sentinel CASE_010
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_010
oracle_start CASE_010
expect_line RESULT_STATUS NO_DERIVED_OBSERVATIONS
expect_line DERIVED_OBSERVATION_COUNT 0
expect_line OUTPUT_MUTATED 0
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_010

# 11 — exact sequence capacity four, one derived observation each.
prepare_case CASE_011
set_sequences \
    "SEQ||seq-${DYN_TAG}-011a||UNITS||a-${DYN_TAG}~b-${DYN_TAG}~c-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-011b||UNITS||d-${DYN_TAG}~e-${DYN_TAG}~f-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-011c||UNITS||g-${DYN_TAG}~h-${DYN_TAG}~i-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-011d||UNITS||j-${DYN_TAG}~k-${DYN_TAG}~l-${DYN_TAG}||SOURCE||${SRC_A}"
run_vm CASE_011
oracle_start CASE_011
expect_line UNIQUE_SEQUENCE_COUNT 4
expect_line SEQUENCE_CAPACITY_EXCEEDED 0
expect_line DERIVED_OBSERVATION_COUNT 4
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
pass_case CASE_011

# 12 — fifth unique sequence exceeds sequence capacity but not derived-observation capacity.
prepare_case CASE_012
set_sequences \
    "SEQ||seq-${DYN_TAG}-012a||UNITS||a1-${DYN_TAG}~b1-${DYN_TAG}~c1-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-012b||UNITS||a2-${DYN_TAG}~b2-${DYN_TAG}~c2-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-012c||UNITS||a3-${DYN_TAG}~b3-${DYN_TAG}~c3-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-012d||UNITS||a4-${DYN_TAG}~b4-${DYN_TAG}~c4-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-012e||UNITS||a5-${DYN_TAG}~b5-${DYN_TAG}~c5-${DYN_TAG}||SOURCE||${SRC_A}"
prefill_sentinel CASE_012
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_012
oracle_start CASE_012
expect_line SEQUENCE_CAPACITY_EXCEEDED 1
expect_line OBSERVATION_CAPACITY_EXCEEDED 0
expect_line RESULT_STATUS REFUSED_SEQUENCE_CAPACITY
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_012

# 13 — raw split-line input bound refuses before sequence scan.
prepare_case CASE_013
set_sequences \
    "x1-${DYN_TAG}" "x2-${DYN_TAG}" "x3-${DYN_TAG}" \
    "x4-${DYN_TAG}" "x5-${DYN_TAG}" "x6-${DYN_TAG}" \
    "x7-${DYN_TAG}" "x8-${DYN_TAG}" "x9-${DYN_TAG}"
prefill_sentinel CASE_013
BEFORE=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
run_vm CASE_013
oracle_start CASE_013
expect_line INPUT_BOUND_EXCEEDED 1
expect_line UNIQUE_SEQUENCE_COUNT 0
expect_line RESULT_STATUS REFUSED_INPUT_BOUND
expect_output_unchanged "$BEFORE"
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
pass_case CASE_013

# 14 — exact derived-observation structural maximum: four sequences x two interior units = eight.
prepare_case CASE_014
set_sequences \
    "SEQ||seq-${DYN_TAG}-014a||UNITS||l1-${DYN_TAG}~f1-${DYN_TAG}~r1-${DYN_TAG}~t1-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-014b||UNITS||l2-${DYN_TAG}~f2-${DYN_TAG}~r2-${DYN_TAG}~t2-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-014c||UNITS||l3-${DYN_TAG}~f3-${DYN_TAG}~r3-${DYN_TAG}~t3-${DYN_TAG}||SOURCE||${SRC_A}" \
    "SEQ||seq-${DYN_TAG}-014d||UNITS||l4-${DYN_TAG}~f4-${DYN_TAG}~r4-${DYN_TAG}~t4-${DYN_TAG}||SOURCE||${SRC_A}"
run_vm CASE_014
oracle_start CASE_014
expect_line UNIQUE_SEQUENCE_COUNT 4
expect_line DERIVED_OBSERVATION_COUNT 8
expect_line OBSERVATION_CAPACITY_EXCEEDED 0
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
pass_case CASE_014

# 15 — exact UTF-8 source provenance is carried into the derived observation.
prepare_case CASE_015
SEQ15="seq-${DYN_TAG_2}-015"
set_sequences "SEQ||${SEQ15}||UNITS||${V_LEFT}~${V_FORM}~${V_RIGHT}||SOURCE||${SRC_B}"
run_vm CASE_015
oracle_start CASE_015
expect_line DERIVED_OBSERVATION_COUNT 1
EXPECT15="OBS||${SEQ15}:1||FORM||${V_FORM}||LEFT||${V_LEFT}||RIGHT||${V_RIGHT}||SOURCE||${SRC_B}"
expect_exact_output "$EXPECT15"
pass_case CASE_015

# 16 — materially different dynamic sequence changes native output bytes.
prepare_case CASE_016
SEQ16="seq-${DYN_TAG}-016"
set_sequences "SEQ||${SEQ16}||UNITS||${U_LEFT}~${U_ALT2}~${U_RIGHT}||SOURCE||${SRC_A}"
run_vm CASE_016
oracle_start CASE_016
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
CASE16_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
[ "$CASE1_OUTPUT_SHA" != "$CASE16_OUTPUT_SHA" ] || {
    printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_016\nFAILURE=OUTPUT_DID_NOT_CHANGE_WITH_DYNAMIC_INPUT\n'
    exit 63
}
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
pass_case CASE_016

# 17 — pure replay A.
prepare_case CASE_017
SEQ17="seq-${DYN_TAG_2}-017"
REPLAY_LINE="SEQ||${SEQ17}||UNITS||${V_LEFT}~${V_FORM}~${V_RIGHT}~${V_TAIL}||SOURCE||${SRC_B}"
set_sequences "$REPLAY_LINE"
run_vm CASE_017
oracle_start CASE_017
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
REPLAY_A_LOG_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
REPLAY_A_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
pass_case CASE_017

# 18 — pure replay B in a fresh namespace with identical input -> identical native stdout and output bytes.
prepare_case CASE_018
set_sequences "$REPLAY_LINE"
run_vm CASE_018
oracle_start CASE_018
expect_line RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
REPLAY_B_LOG_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')
REPLAY_B_OUTPUT_SHA=$("$P/bin/sha256sum" "$OUT" | "$P/bin/awk" '{print $1}')
[ "$REPLAY_A_LOG_SHA" = "$REPLAY_B_LOG_SHA" ] || {
    printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_018\nFAILURE=REPLAY_STDOUT_MISMATCH\n'
    exit 64
}
[ "$REPLAY_A_OUTPUT_SHA" = "$REPLAY_B_OUTPUT_SHA" ] || {
    printf 'VNM_03_PREFLIGHT=FAIL\nFAILURE_CASE=CASE_018\nFAILURE=REPLAY_OUTPUT_MISMATCH\n'
    exit 65
}
PURE_REPLAY_PASS_COUNT=$((PURE_REPLAY_PASS_COUNT + 1))
printf 'REPLAY_IDENTICAL_INPUT_DECISION=YES\n'
pass_case CASE_018

SOURCE_AFTER=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
BYTECODE_AFTER=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
[ "$SOURCE_AFTER" = "$EXPECTED_SOURCE" ] && SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
[ "$BYTECODE_AFTER" = "$BYTECODE_SHA" ] && BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES

LEAK_COUNT=$("$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" 2>/dev/null | "$P/bin/wc" -l | "$P/bin/tr" -d ' ')
[ -n "$LEAK_COUNT" ] || LEAK_COUNT=0

printf '\n=== VNM-03 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION\n'
printf 'CAPABILITY_NAME=Native local-context observation derivation from delimiter-defined UTF-8 sequences\n'
printf 'TEACHING_GOAL=SIGMA natively derives bounded FORM/LEFT/RIGHT observation records from dynamic delimiter-defined sequences without host context extraction\n'
printf 'DEPENDENCIES=VNM02_ADMITTED_DOWNSTREAM_PAIR_INDUCTION_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
printf 'SOURCE_SHA256=%s\n' "$actual_source"
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_PASS_COUNT=%s\n' "$NEGATIVE_PASS_COUNT"
printf 'INPUT_DYNAMIC=YES\n'
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=NO\n'
printf 'PERSISTENT_STATE_TEST=NA\n'
printf 'RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES\n'
printf 'CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_UNIT_SELECTION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_NORMALIZATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$LEAK_COUNT"
printf 'STEP_LIMIT_STATUS=PASS_IN_18_INVOCATION_BOUNDED_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN\n'
printf 'PHRASE_BOUNDARY_DETECTION=NOT_PROVEN\n'
printf 'WORD_MEANING=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded records containing 3-or-4 externally delimiter-defined UTF-8 units; native derivation of each interior unit into VNM-02-compatible FORM/LEFT/RIGHT observations; duplicate suppression; collision/malformed/sequence-capacity/input-bound refusal; exact provenance preservation; pure replay; no natural-language tokenization or semantic-context claim\n'

if [ "$TOTAL_VM_INVOCATIONS" -eq 18 ] \
    && [ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 18 ] \
    && [ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] \
    && [ "$VM_NONZERO_COUNT" -eq 0 ] \
    && [ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] \
    && [ "$NEGATIVE_PASS_COUNT" -eq 8 ] \
    && [ "$PURE_REPLAY_PASS_COUNT" -eq 1 ] \
    && [ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] \
    && [ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] \
    && [ "$LEAK_COUNT" -eq 0 ]
then
    printf 'VNM_03_PREFLIGHT=PASS\n'
    printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
    exit 0
fi

printf 'VNM_03_PREFLIGHT=FAIL\n'
printf 'ADMISSION=FAIL\n'
exit 70
