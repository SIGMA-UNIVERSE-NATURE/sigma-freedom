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
EXPECTED_SOURCE=638078331f21fccf392b6456f81a76713010a59b641026962bcaf28e2ac3814a

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM_01_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_WEIGHT_UPDATE=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'ACTIVE_PYTHON_COGNITION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=YES\n'
printf 'RESTART_REPLAY_TEST=YES\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=VNM_01_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

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
        exit 24
    fi
done

"$P/bin/rm" -f -- "$BC.partial" "$BC"
"$SIGMAC" "$SRC" "$BC.partial"
CRC=$?
printf 'SIGMAC_RC=%s\n' "$CRC"
[ "$CRC" -eq 0 ] || exit 25
[ -s "$BC.partial" ] || exit 26
"$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 27
"$P/bin/chmod" 0400 "$BC" || exit 28

BYTECODE_SHA=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

# Dynamic Vietnamese-bearing fixtures are created only after source/bytecode freeze.
DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

FORM_A="điện-${DYN_TAG}"
FORM_B="dien-${DYN_TAG}"
ALT_FORM="động-${DYN_TAG}"
UNRELATED_A="mây-${DYN_TAG}"
UNRELATED_B="troi-${DYN_TAG}"

FORM_C="học-${DYN_TAG_2}"
FORM_D="hoc-${DYN_TAG_2}"
ALT_FORM_2="đọc-${DYN_TAG_2}"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'DYNAMIC_TAG_SHA256=%s\n' "$(printf '%s' "$DYN_TAG" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"

if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" >/dev/null 2>&1; then
    printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'
    exit 29
fi

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
PERSISTENCE_PASS_COUNT=0
CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
STATE=""
LAST_LOG=""

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"
    IN="$BASE/input"
    STATE="$BASE/state/surface_form_weight_state.memory"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN" "$BASE/state"
    : > "$IN/hypothesis.memory"
    : > "$IN/evidence.memory"
    : > "$STATE"
}

use_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"
    IN="$BASE/input"
    STATE="$BASE/state/surface_form_weight_state.memory"
}

set_hypothesis() {
    printf 'HYPOTHESIS||%s||FORM_A||%s||FORM_B||%s' "$1" "$2" "$3" > "$IN/hypothesis.memory"
}

clear_evidence() {
    : > "$IN/evidence.memory"
}

add_evidence() {
    printf 'EVIDENCE||%s||%s||%s||SOURCE||%s\n' "$1" "$2" "$3" "$4" >> "$IN/evidence.memory"
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

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=VM_NONZERO\n' "$LABEL"
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STEP_LIMIT_HIT\n' "$LABEL"
        exit 51
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_OUTPUT\nEXPECTED=%s %s\n' "$CASE_NAME" "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_SENTINEL\nEXPECTED=%s\n' "$CASE_NAME" "$VALUE"
        exit 61
    fi
}

pass_common() {
    expect_exact 'SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING'
    expect_line 'ARTIFACT_ORIGIN' 'TEACHER_AUTHORED_BOOTSTRAP'
    expect_line 'INPUT_DYNAMIC_REQUIRED' 'YES'
    expect_line 'HOST_LEARNING' 'NO'
    expect_line 'HOST_WEIGHT_UPDATE' 'NO'
    expect_line 'HOST_SEMANTIC_INTERPRETATION' 'NO'
    expect_line 'HOST_SEMANTIC_SUBSTITUTION' 'NO'
    expect_line 'SURFACE_FORM_PAIR_GENERATION' 'NOT_PROVEN'
    expect_line 'SEMANTIC_EQUIVALENCE' 'NOT_PROVEN'
    expect_line 'VIETNAMESE_SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'GENERAL_SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'PRODUCTION_STATE_MUTATED' 'NO'
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

# Persistent dynamic chain: support -> support -> duplicate -> competing -> unrelated -> collision -> malformed -> support.
prepare_case CASE_001_CHAIN
set_hypothesis "H-${DYN_TAG}" "$FORM_A" "$FORM_B"
add_evidence "E1-${DYN_TAG}" "$FORM_A" "$FORM_B" "CTX1-${DYN_TAG}"
run_vm CASE_001_SUPPORT
expect_line 'HYPOTHESIS_VALID' '1'
expect_line 'FORM_A' "$FORM_A"
expect_line 'FORM_B' "$FORM_B"
expect_line 'WEIGHT_BEFORE' '0'
expect_line 'PROPOSED_WEIGHT' '1'
expect_line 'WEIGHT_AFTER' '1'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_UP'
expect_line 'STATE_MUTATED' '1'
pass_common

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E2-${DYN_TAG}" "$FORM_B" "$FORM_A" "CTX2-${DYN_TAG}"
run_vm CASE_002_RESTART_SECOND_SUPPORT
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '2'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_UP'
expect_line 'STATE_MUTATED' '1'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E2-${DYN_TAG}" "$FORM_B" "$FORM_A" "CTX2-${DYN_TAG}"
run_vm CASE_003_DUPLICATE_REPLAY
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'DUPLICATE_EVIDENCE_COUNT' '1'
expect_line 'NEW_QUALIFIED_EVIDENCE_COUNT' '0'
expect_line 'WEIGHT_BEFORE' '2'
expect_line 'WEIGHT_AFTER' '2'
expect_line 'NATIVE_UPDATE_REASON' 'NO_NEW_QUALIFIED_EVIDENCE'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E3-${DYN_TAG}" "$FORM_A" "$ALT_FORM" "CTX3-${DYN_TAG}"
run_vm CASE_004_COMPETING_DECREASE
expect_line 'NEW_COMPETING_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '2'
expect_line 'PROPOSED_WEIGHT' '1'
expect_line 'WEIGHT_AFTER' '1'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_DOWN'
expect_line 'STATE_MUTATED' '1'
pass_common

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E4-${DYN_TAG}" "$UNRELATED_A" "$UNRELATED_B" "CTX4-${DYN_TAG}"
run_vm CASE_005_UNRELATED_NO_UPDATE
expect_line 'NEW_UNRELATED_COUNT' '1'
expect_line 'NEW_QUALIFIED_EVIDENCE_COUNT' '0'
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '1'
expect_line 'NATIVE_UPDATE_REASON' 'NO_NEW_QUALIFIED_EVIDENCE'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E1-${DYN_TAG}" "$FORM_A" "$ALT_FORM" "COLLIDE-${DYN_TAG}"
run_vm CASE_006_ID_COLLISION_REFUSAL
expect_line 'EVIDENCE_ID_COLLISION_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '1'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_ID_COLLISION'
expect_line 'LEARNING_STATUS' 'REFUSED_EVIDENCE_ID_COLLISION'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
printf 'EVIDENCE||BROKEN||%s||%s||SOURCE\n' "$FORM_A" "$FORM_B" > "$IN/evidence.memory"
run_vm CASE_007_MALFORMED_REFUSAL
expect_line 'INVALID_EVIDENCE_RECORD_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '1'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_RECORD_INVALID'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_evidence
add_evidence "E5-${DYN_TAG}" "$FORM_A" "$FORM_B" "CTX5-${DYN_TAG}"
run_vm CASE_008_SUPPORT_AFTER_NEGATIVES
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '2'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_UP'
expect_line 'STATE_MUTATED' '1'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# Mixed qualified evidence can persist with zero net weight change.
prepare_case CASE_009_MIXED
set_hypothesis "HM-${DYN_TAG}" "$FORM_A" "$FORM_B"
add_evidence "M1-${DYN_TAG}" "$FORM_A" "$FORM_B" "MCTX1-${DYN_TAG}"
add_evidence "M2-${DYN_TAG}" "$FORM_A" "$ALT_FORM" "MCTX2-${DYN_TAG}"
run_vm CASE_009_OFFSETTING_BATCH
expect_line 'NEW_SUPPORT_COUNT' '1'
expect_line 'NEW_COMPETING_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '0'
expect_line 'PROPOSED_WEIGHT' '0'
expect_line 'WEIGHT_AFTER' '0'
expect_line 'NATIVE_UPDATE_REASON' 'OFFSETTING_EVIDENCE_NO_NET_WEIGHT_CHANGE'
expect_line 'STATE_MUTATED' '1'
pass_common

use_case CASE_009_MIXED
clear_evidence
run_vm CASE_010_MIXED_RESTART
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_SUPPORT_COUNT' '1'
expect_line 'PRIOR_COMPETING_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '0'
expect_line 'WEIGHT_AFTER' '0'
expect_line 'STATE_MUTATED' '0'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# A second unseen Vietnamese-bearing pair produces a different native weight direction.
prepare_case CASE_011_SECOND_PAIR
set_hypothesis "H2-${DYN_TAG_2}" "$FORM_C" "$FORM_D"
add_evidence "Q1-${DYN_TAG_2}" "$FORM_C" "$ALT_FORM_2" "QCTX-${DYN_TAG_2}"
run_vm CASE_011_SECOND_PAIR_COMPETING
expect_line 'FORM_A' "$FORM_C"
expect_line 'FORM_B' "$FORM_D"
expect_line 'NEW_COMPETING_COUNT' '1'
expect_line 'WEIGHT_BEFORE' '0'
expect_line 'WEIGHT_AFTER' '-1'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_DOWN'
expect_line 'STATE_MUTATED' '1'
pass_common

# Same-form hypothesis is invalid and cannot mutate state.
prepare_case CASE_012_INVALID_HYPOTHESIS
set_hypothesis "BAD-${DYN_TAG}" "$FORM_A" "$FORM_A"
add_evidence "BAD1-${DYN_TAG}" "$FORM_A" "$FORM_A" "BADCTX-${DYN_TAG}"
run_vm CASE_012_INVALID_HYPOTHESIS
expect_line 'HYPOTHESIS_VALID' '0'
expect_line 'NATIVE_UPDATE_REASON' 'HYPOTHESIS_INVALID'
expect_line 'LEARNING_STATUS' 'REFUSED_HYPOTHESIS_INVALID'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# Capacity boundary: eight qualified records pass; ninth is refused atomically.
prepare_case CASE_013_CAPACITY
set_hypothesis "CAP-${DYN_TAG}" "$FORM_A" "$FORM_B"
I=1
while [ "$I" -le 8 ]; do
    add_evidence "CAP${I}-${DYN_TAG}" "$FORM_A" "$FORM_B" "CAPCTX${I}-${DYN_TAG}"
    I=$((I + 1))
done
run_vm CASE_013_CAPACITY_EIGHT
expect_line 'NEW_QUALIFIED_EVIDENCE_COUNT' '8'
expect_line 'EVIDENCE_CAPACITY_EXCEEDED' '0'
expect_line 'WEIGHT_AFTER' '8'
expect_line 'STATE_MUTATED' '1'
pass_common

use_case CASE_013_CAPACITY
clear_evidence
add_evidence "CAP9-${DYN_TAG}" "$FORM_A" "$FORM_B" "CAPCTX9-${DYN_TAG}"
run_vm CASE_014_CAPACITY_NINTH_REFUSAL
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'WEIGHT_BEFORE' '8'
expect_line 'EVIDENCE_CAPACITY_EXCEEDED' '1'
expect_line 'WEIGHT_AFTER' '8'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_CAPACITY_EXCEEDED'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# Raw batch bound is refused without persistence.
prepare_case CASE_015_INPUT_BOUND
set_hypothesis "BOUND-${DYN_TAG}" "$FORM_A" "$FORM_B"
I=1
while [ "$I" -le 17 ]; do
    add_evidence "B${I}-${DYN_TAG}" "$UNRELATED_A" "$UNRELATED_B" "BCTX${I}-${DYN_TAG}"
    I=$((I + 1))
done
run_vm CASE_015_INPUT_BOUND
expect_line 'INPUT_BOUND_EXCEEDED' '1'
expect_line 'NATIVE_UPDATE_REASON' 'INPUT_BOUND_EXCEEDED'
expect_line 'LEARNING_STATUS' 'REFUSED_INPUT_BOUND'
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# Replay proof: identical prestate bytes + identical input bytes -> identical native stdout.
prepare_case CASE_016_REPLAY_SEED
set_hypothesis "R-${DYN_TAG_2}" "$FORM_C" "$FORM_D"
add_evidence "R1-${DYN_TAG_2}" "$FORM_C" "$FORM_D" "RCTX1-${DYN_TAG_2}"
run_vm CASE_016_REPLAY_SEED
expect_line 'WEIGHT_AFTER' '1'
expect_line 'STATE_MUTATED' '1'
pass_common

"$P/bin/cp" -a "$CASES/CASE_016_REPLAY_SEED" "$CASES/CASE_017_REPLAY_A"
"$P/bin/cp" -a "$CASES/CASE_016_REPLAY_SEED" "$CASES/CASE_018_REPLAY_B"

use_case CASE_017_REPLAY_A
clear_evidence
add_evidence "R2-${DYN_TAG_2}" "$FORM_C" "$ALT_FORM_2" "RCTX2-${DYN_TAG_2}"
PRESTATE_A=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
INPUT_A=$("$P/bin/sha256sum" "$IN/hypothesis.memory" "$IN/evidence.memory" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')
run_vm CASE_017_REPLAY_A
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '0'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_DOWN'
pass_common
LOG_A_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')

use_case CASE_018_REPLAY_B
clear_evidence
add_evidence "R2-${DYN_TAG_2}" "$FORM_C" "$ALT_FORM_2" "RCTX2-${DYN_TAG_2}"
PRESTATE_B=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
INPUT_B=$("$P/bin/sha256sum" "$IN/hypothesis.memory" "$IN/evidence.memory" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')
run_vm CASE_018_REPLAY_B
expect_line 'WEIGHT_BEFORE' '1'
expect_line 'WEIGHT_AFTER' '0'
expect_line 'NATIVE_UPDATE_REASON' 'EVIDENCE_SHIFTED_WEIGHT_DOWN'
pass_common
LOG_B_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')

[ "$PRESTATE_A" = "$PRESTATE_B" ] || { printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=REPLAY_PRESTATE_MISMATCH\n'; exit 70; }
[ "$INPUT_A" = "$INPUT_B" ] || { printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=REPLAY_INPUT_MISMATCH\n'; exit 71; }
[ "$LOG_A_SHA" = "$LOG_B_SHA" ] || { printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=REPLAY_NATIVE_OUTPUT_MISMATCH\n'; exit 72; }

SOURCE_AFTER=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
BYTECODE_AFTER=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')

[ "$SOURCE_AFTER" = "$actual_source" ] || { printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=SOURCE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 73; }
[ "$BYTECODE_AFTER" = "$BYTECODE_SHA" ] || { printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=BYTECODE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 74; }

if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" >/dev/null 2>&1; then
    printf 'VNM_01_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_TOKEN_LEAK_AFTER_SUITE\n'
    exit 75
fi

printf '\n=== VNM-01 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING\n'
printf 'CAPABILITY_NAME=Native Vietnamese-bearing surface-form evidence weighting\n'
printf 'TEACHING_GOAL=SIGMA natively updates a bounded persistent structural association weight from dynamic surface-form evidence\n'
printf 'DEPENDENCIES=LOCKED_SIGMAC_LOCKED_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
printf 'SOURCE_SHA256=%s\n' "$SOURCE_AFTER"
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_AFTER"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_PASS_COUNT=%s\n' "$NEGATIVE_PASS_COUNT"
printf 'PERSISTENCE_PASS_COUNT=%s\n' "$PERSISTENCE_PASS_COUNT"
printf 'INPUT_DYNAMIC=YES\n'
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=YES\n'
printf 'PERSISTENT_STATE_TEST=PASS\n'
printf 'RESTART_REPLAY_TEST=PASS\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_WEIGHT_UPDATE=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0\n'
printf 'STEP_LIMIT_STATUS=PASS_IN_18_INVOCATION_BOUNDED_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SURFACE_FORM_PAIR_GENERATION=NOT_PROVEN\n'
printf 'SEMANTIC_EQUIVALENCE=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded externally-supplied UTF-8 surface-form pair hypothesis; native support/competing classification; persistent weight update; duplicate/collision refusal; dynamic Vietnamese-bearing strings only\n'
printf 'VNM_01_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
