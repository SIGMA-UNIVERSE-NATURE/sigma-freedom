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
EXPECTED_SOURCE=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
EXPECTED_VNM01_SOURCE=cd399793ebde7e5dfa4a10cf263bb97fd45d1379ce8dac02520d5277cf2ca788

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigma"
VNM01_SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_VNM_02_PAIR_CANDIDATE_INDUCTION_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM_02_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
actual_vnm01=$("$P/bin/sha256sum" "$VNM01_SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_CANDIDATE_GENERATION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_CONTEXT_SCORING=NO\n'
printf 'HOST_NORMALIZATION=NO\n'
printf 'HOST_LEARNING=NO\n'
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
printf 'DOWNSTREAM_VNM01_SOURCE_SHA256=%s\n' "$actual_vnm01"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=VNM_02_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$actual_vnm01" = "$EXPECTED_VNM01_SOURCE" ] || { printf 'HOLD=VNM_01_DOWNSTREAM_COMPATIBILITY_IDENTITY_MISMATCH\n'; exit 24; }

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

# Dynamic UTF-8 forms and opaque structural contexts are generated only after bytecode freeze.
DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

FORM_A="điện-${DYN_TAG}"
FORM_B="dien-${DYN_TAG}"
FORM_C="động-${DYN_TAG}"

FORM_D="học-${DYN_TAG_2}"
FORM_E="hoc-${DYN_TAG_2}"

L1="L-${DYN_TAG}-1"
R1="R-${DYN_TAG}-1"
L2="L-${DYN_TAG}-2"
R2="R-${DYN_TAG}-2"
L3="L-${DYN_TAG}-3"
R3="R-${DYN_TAG}-3"
L4="L-${DYN_TAG}-4"
R4="R-${DYN_TAG}-4"

DL1="L-${DYN_TAG_2}-1"
DR1="R-${DYN_TAG_2}-1"
DL2="L-${DYN_TAG_2}-2"
DR2="R-${DYN_TAG_2}-2"

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
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_02_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1"
    IN="$BASE/input"
    STATE="$BASE/state/pair_induction_state.memory"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN" "$BASE/state"
    : > "$IN/observations.memory"
    : > "$STATE"
}

use_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_02_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1"
    IN="$BASE/input"
    STATE="$BASE/state/pair_induction_state.memory"
}

clear_observations() {
    : > "$IN/observations.memory"
}

add_observation() {
    printf 'OBS||%s||FORM||%s||LEFT||%s||RIGHT||%s||SOURCE||%s\n' \
        "$1" "$2" "$3" "$4" "$5" >> "$IN/observations.memory"
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
        printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=VM_NONZERO\n' "$LABEL"
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STEP_LIMIT_HIT\n' "$LABEL"
        exit 51
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_OUTPUT\nEXPECTED=%s %s\n' "$CASE_NAME" "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_SENTINEL\nEXPECTED=%s\n' "$CASE_NAME" "$VALUE"
        exit 61
    fi
}

expect_pair_unordered() {
    A="$1"
    B="$2"
    ACT_A=$("$P/bin/awk" '$1=="PAIR_CANDIDATE_FORM_A"{sub($1 FS,"");print;exit}' "$LAST_LOG")
    ACT_B=$("$P/bin/awk" '$1=="PAIR_CANDIDATE_FORM_B"{sub($1 FS,"");print;exit}' "$LAST_LOG")

    PAIR_OK=NO
    if [ "$ACT_A" = "$A" ] && [ "$ACT_B" = "$B" ]; then
        PAIR_OK=YES
    fi
    if [ "$ACT_A" = "$B" ] && [ "$ACT_B" = "$A" ]; then
        PAIR_OK=YES
    fi

    if [ "$PAIR_OK" != YES ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=UNORDERED_PAIR_MISMATCH\nEXPECTED_PAIR=%s|%s\nACTUAL_PAIR=%s|%s\n' \
            "$CASE_NAME" "$A" "$B" "$ACT_A" "$ACT_B"
        exit 62
    fi
}

pass_common() {
    expect_exact 'SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION'
    expect_line 'INPUT_DYNAMIC_REQUIRED' 'YES'
    expect_line 'PAIR_GENERATION_OWNER' 'SIGMA_NATIVE'
    expect_line 'PAIR_ORIENTATION_SEMANTIC' 'NO'
    expect_line 'HOST_CANDIDATE_GENERATION' 'NO'
    expect_line 'HOST_PAIR_SELECTION' 'NO'
    expect_line 'HOST_CONTEXT_SCORING' 'NO'
    expect_line 'HOST_NORMALIZATION' 'NO'
    expect_line 'HOST_LEARNING' 'NO'
    expect_line 'HOST_SEMANTIC_INTERPRETATION' 'NO'
    expect_line 'HOST_SEMANTIC_SUBSTITUTION' 'NO'
    expect_line 'SEMANTIC_EQUIVALENCE' 'NOT_PROVEN'
    expect_line 'DIACRITIC_EQUIVALENCE' 'NOT_PROVEN'
    expect_line 'WORD_MEANING' 'NOT_PROVEN'
    expect_line 'VIETNAMESE_SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'GENERAL_SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'PRODUCTION_STATE_MUTATED' 'NO'
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

# 1-6: persistent A/B induction chain and negative robustness.
prepare_case CASE_001_CHAIN
add_observation "A1-${DYN_TAG}" "$FORM_A" "$L1" "$R1" "S-A1-${DYN_TAG}"
add_observation "B1-${DYN_TAG}" "$FORM_B" "$L1" "$R1" "S-B1-${DYN_TAG}"
run_vm CASE_001_SINGLE_SHARED_CONTEXT
expect_line 'PAIR_CANDIDATE_STATUS' 'INSUFFICIENT_RECURRENT_EVIDENCE'
expect_line 'CANDIDATE_PAIR_COUNT' '1'
expect_line 'QUALIFIED_PAIR_COUNT' '0'
expect_line 'STATE_MUTATED' '1'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_observations
add_observation "A2-${DYN_TAG}" "$FORM_A" "$L2" "$R2" "S-A2-${DYN_TAG}"
add_observation "B2-${DYN_TAG}" "$FORM_B" "$L2" "$R2" "S-B2-${DYN_TAG}"
run_vm CASE_002_RESTART_SECOND_SHARED_CONTEXT
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_OBSERVATION_COUNT' '2'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_A" "$FORM_B"
expect_line 'STATE_MUTATED' '1'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_observations
add_observation "B2-${DYN_TAG}" "$FORM_B" "$L2" "$R2" "S-B2-${DYN_TAG}"
run_vm CASE_003_DUPLICATE_IDEMPOTENT
expect_line 'DUPLICATE_OBSERVATION_COUNT' '1'
expect_line 'NEW_UNIQUE_OBSERVATION_COUNT' '0'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_A" "$FORM_B"
expect_line 'STATE_MUTATED' '0'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_observations
PRE_COLLISION=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
add_observation "A1-${DYN_TAG}" "$FORM_C" "$L3" "$R3" "COLLIDE-${DYN_TAG}"
run_vm CASE_004_ID_COLLISION_REFUSAL
POST_COLLISION=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
expect_line 'OBSERVATION_ID_COLLISION_COUNT' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'REFUSED_OBSERVATION_ID_COLLISION'
expect_line 'STATE_MUTATED' '0'
[ "$PRE_COLLISION" = "$POST_COLLISION" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=COLLISION_MUTATED_STATE\n'; exit 63; }
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
PRE_MALFORMED=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
printf 'OBS||BROKEN||FORM||%s||LEFT||%s\n' "$FORM_A" "$L1" > "$IN/observations.memory"
run_vm CASE_005_MALFORMED_REFUSAL
POST_MALFORMED=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
expect_line 'INVALID_OBSERVATION_RECORD_COUNT' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'REFUSED_OBSERVATION_RECORD_INVALID'
expect_line 'STATE_MUTATED' '0'
[ "$PRE_MALFORMED" = "$POST_MALFORMED" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=MALFORMED_MUTATED_STATE\n'; exit 64; }
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_001_CHAIN
clear_observations
run_vm CASE_006_STATE_ONLY_RESTART
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_OBSERVATION_COUNT' '4'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_A" "$FORM_B"
expect_line 'STATE_MUTATED' '0'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# 7-8: evidence that must not induce a pair.
prepare_case CASE_007_MISMATCH
add_observation "M1-${DYN_TAG}" "$FORM_A" "$L1" "$R1" "SM1-${DYN_TAG}"
add_observation "M2-${DYN_TAG}" "$FORM_B" "$L2" "$R2" "SM2-${DYN_TAG}"
run_vm CASE_007_CONTEXT_MISMATCH
expect_line 'CANDIDATE_PAIR_COUNT' '0'
expect_line 'PAIR_CANDIDATE_STATUS' 'INSUFFICIENT_RECURRENT_EVIDENCE'
expect_line 'STATE_MUTATED' '1'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

prepare_case CASE_008_SAME_FORM
add_observation "SF1-${DYN_TAG}" "$FORM_A" "$L1" "$R1" "SSF1-${DYN_TAG}"
add_observation "SF2-${DYN_TAG}" "$FORM_A" "$L1" "$R1" "SSF2-${DYN_TAG}"
run_vm CASE_008_SAME_FORM_CONTEXT
expect_line 'CANDIDATE_PAIR_COUNT' '0'
expect_line 'PAIR_CANDIDATE_STATUS' 'INSUFFICIENT_RECURRENT_EVIDENCE'
expect_line 'STATE_MUTATED' '1'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 9: second unseen dynamic pair; copy its persisted state for replay cases 17-18.
prepare_case CASE_009_SECOND_PAIR
add_observation "D1-${DYN_TAG_2}" "$FORM_D" "$DL1" "$DR1" "SD1-${DYN_TAG_2}"
add_observation "E1-${DYN_TAG_2}" "$FORM_E" "$DL1" "$DR1" "SE1-${DYN_TAG_2}"
add_observation "D2-${DYN_TAG_2}" "$FORM_D" "$DL2" "$DR2" "SD2-${DYN_TAG_2}"
add_observation "E2-${DYN_TAG_2}" "$FORM_E" "$DL2" "$DR2" "SE2-${DYN_TAG_2}"
run_vm CASE_009_SECOND_DYNAMIC_PAIR
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_D" "$FORM_E"
expect_line 'STATE_MUTATED' '1'
pass_common

"$P/bin/cp" -a "$CASES/CASE_009_SECOND_PAIR" "$CASES/CASE_017_REPLAY_A"
"$P/bin/cp" -a "$CASES/CASE_009_SECOND_PAIR" "$CASES/CASE_018_REPLAY_B"

# 10-12: tie ambiguity followed by native revision after later evidence.
prepare_case CASE_010_TIE
# Context 1: A, B, C -> AB/AC/BC each receive one support.
add_observation "T-A1-${DYN_TAG}" "$FORM_A" "$L1" "$R1" "TSA1-${DYN_TAG}"
add_observation "T-B1-${DYN_TAG}" "$FORM_B" "$L1" "$R1" "TSB1-${DYN_TAG}"
add_observation "T-C1-${DYN_TAG}" "$FORM_C" "$L1" "$R1" "TSC1-${DYN_TAG}"
# Context 2: A, B -> AB support becomes 2.
add_observation "T-A2-${DYN_TAG}" "$FORM_A" "$L2" "$R2" "TSA2-${DYN_TAG}"
add_observation "T-B2-${DYN_TAG}" "$FORM_B" "$L2" "$R2" "TSB2-${DYN_TAG}"
# Context 3: A, C -> AC support becomes 2.
add_observation "T-A3-${DYN_TAG}" "$FORM_A" "$L3" "$R3" "TSA3-${DYN_TAG}"
add_observation "T-C3-${DYN_TAG}" "$FORM_C" "$L3" "$R3" "TSC3-${DYN_TAG}"
run_vm CASE_010_TIED_PAIR_CANDIDATES
expect_line 'TOTAL_OBSERVATION_COUNT' '7'
expect_line 'QUALIFIED_PAIR_COUNT' '2'
expect_line 'PAIR_CANDIDATE_STATUS' 'AMBIGUOUS_PAIR_CANDIDATE'
expect_line 'PAIR_CANDIDATE_SUPPORT' '0'
expect_line 'STATE_MUTATED' '1'
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

use_case CASE_010_TIE
clear_observations
# Add B to context 3: AB=3, AC=2, BC=2. Native SIGMA must select AB.
add_observation "T-B3-${DYN_TAG}" "$FORM_B" "$L3" "$R3" "TSB3-${DYN_TAG}"
run_vm CASE_011_TIE_BREAK_RESTART
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_OBSERVATION_COUNT' '7'
expect_line 'TOTAL_OBSERVATION_COUNT' '8'
expect_line 'QUALIFIED_PAIR_COUNT' '3'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '3'
expect_pair_unordered "$FORM_A" "$FORM_B"
expect_line 'STATE_MUTATED' '1'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

use_case CASE_010_TIE
clear_observations
run_vm CASE_012_TIE_BREAK_STATE_ONLY
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'PRIOR_OBSERVATION_COUNT' '8'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '3'
expect_pair_unordered "$FORM_A" "$FORM_B"
expect_line 'STATE_MUTATED' '0'
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# 13-14: exact capacity boundary and atomic ninth-record refusal.
prepare_case CASE_013_CAPACITY
I=1
while [ "$I" -le 8 ]; do
    add_observation "CAP${I}-${DYN_TAG}" "$FORM_A" "CL-${DYN_TAG}-${I}" "CR-${DYN_TAG}-${I}" "CS-${DYN_TAG}-${I}"
    I=$((I + 1))
done
run_vm CASE_013_CAPACITY_EIGHT
expect_line 'TOTAL_OBSERVATION_COUNT' '8'
expect_line 'OBSERVATION_CAPACITY_EXCEEDED' '0'
expect_line 'PAIR_CANDIDATE_STATUS' 'INSUFFICIENT_RECURRENT_EVIDENCE'
expect_line 'STATE_MUTATED' '1'
pass_common

use_case CASE_013_CAPACITY
clear_observations
PRE_CAPACITY=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
add_observation "CAP9-${DYN_TAG}" "$FORM_B" "$L4" "$R4" "CS9-${DYN_TAG}"
run_vm CASE_014_CAPACITY_NINTH_REFUSAL
POST_CAPACITY=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
expect_line 'OBSERVATION_CAPACITY_EXCEEDED' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'REFUSED_OBSERVATION_CAPACITY'
expect_line 'STATE_MUTATED' '0'
[ "$PRE_CAPACITY" = "$POST_CAPACITY" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=CAPACITY_REFUSAL_MUTATED_STATE\n'; exit 65; }
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 15: raw split bound. Seventeen identical records avoid unrelated capacity/collision confounds.
prepare_case CASE_015_INPUT_BOUND
I=1
while [ "$I" -le 17 ]; do
    add_observation "BOUND-${DYN_TAG}" "$FORM_A" "$L4" "$R4" "BS-${DYN_TAG}"
    I=$((I + 1))
done
PRE_BOUND=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
run_vm CASE_015_INPUT_BOUND
POST_BOUND=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
expect_line 'INPUT_BOUND_EXCEEDED' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'REFUSED_INPUT_BOUND'
expect_line 'STATE_MUTATED' '0'
[ "$PRE_BOUND" = "$POST_BOUND" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=INPUT_BOUND_REFUSAL_MUTATED_STATE\n'; exit 66; }
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 16: malformed prior state refuses without mutation.
prepare_case CASE_016_INVALID_STATE
printf 'BROKEN_STATE||%s\n' "$DYN_TAG" > "$STATE"
clear_observations
PRE_BAD_STATE=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
run_vm CASE_016_INVALID_PREVIOUS_STATE
POST_BAD_STATE=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
expect_line 'PREVIOUS_STATE_INVALID' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'REFUSED_PREVIOUS_STATE_INVALID'
expect_line 'STATE_MUTATED' '0'
[ "$PRE_BAD_STATE" = "$POST_BAD_STATE" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=INVALID_PRESTATE_MUTATED_STATE\n'; exit 67; }
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 17-18: identical persisted prestate + identical dynamic duplicate input -> identical native stdout.
use_case CASE_017_REPLAY_A
clear_observations
add_observation "E2-${DYN_TAG_2}" "$FORM_E" "$DL2" "$DR2" "SE2-${DYN_TAG_2}"
PRESTATE_A=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
INPUT_A=$(cd "$IN" && "$P/bin/sha256sum" observations.memory | "$P/bin/sha256sum" | "$P/bin/head" -c 64)
run_vm CASE_017_REPLAY_A
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'DUPLICATE_OBSERVATION_COUNT' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_D" "$FORM_E"
expect_line 'STATE_MUTATED' '0'
pass_common
LOG_A_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')

use_case CASE_018_REPLAY_B
clear_observations
add_observation "E2-${DYN_TAG_2}" "$FORM_E" "$DL2" "$DR2" "SE2-${DYN_TAG_2}"
PRESTATE_B=$("$P/bin/sha256sum" "$STATE" | "$P/bin/awk" '{print $1}')
INPUT_B=$(cd "$IN" && "$P/bin/sha256sum" observations.memory | "$P/bin/sha256sum" | "$P/bin/head" -c 64)
run_vm CASE_018_REPLAY_B
expect_line 'PREVIOUS_STATE_VALID' '1'
expect_line 'DUPLICATE_OBSERVATION_COUNT' '1'
expect_line 'PAIR_CANDIDATE_STATUS' 'PAIR_CANDIDATE_INDUCED'
expect_line 'PAIR_CANDIDATE_SUPPORT' '2'
expect_pair_unordered "$FORM_D" "$FORM_E"
expect_line 'STATE_MUTATED' '0'
pass_common
LOG_B_SHA=$("$P/bin/sha256sum" "$LAST_LOG" | "$P/bin/awk" '{print $1}')

[ "$PRESTATE_A" = "$PRESTATE_B" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=REPLAY_PRESTATE_MISMATCH\n'; exit 70; }
[ "$INPUT_A" = "$INPUT_B" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=REPLAY_INPUT_MISMATCH\n'; exit 71; }
[ "$LOG_A_SHA" = "$LOG_B_SHA" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=REPLAY_NATIVE_OUTPUT_MISMATCH\n'; exit 72; }

SOURCE_AFTER=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')
BYTECODE_AFTER=$("$P/bin/sha256sum" "$BC" | "$P/bin/awk" '{print $1}')

[ "$SOURCE_AFTER" = "$actual_source" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=SOURCE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 73; }
[ "$BYTECODE_AFTER" = "$BYTECODE_SHA" ] || { printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=BYTECODE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 74; }

if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" >/dev/null 2>&1; then
    printf 'VNM_02_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_TOKEN_LEAK_AFTER_SUITE\n'
    exit 75
fi

printf '\n=== VNM-02 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION\n'
printf 'CAPABILITY_NAME=Native surface-form pair candidate induction from recurring opaque structural context\n'
printf 'TEACHING_GOAL=SIGMA natively generates a bounded surface-form pair candidate from dynamic observation recurrence without host pair selection\n'
printf 'DEPENDENCIES=VNM01_ADMITTED_DOWNSTREAM_WEIGHTING_SUBSTRATE_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
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
printf 'PAIR_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_CANDIDATE_GENERATION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_CONTEXT_SCORING=NO\n'
printf 'HOST_NORMALIZATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0\n'
printf 'STEP_LIMIT_STATUS=PASS_IN_18_INVOCATION_BOUNDED_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SEMANTIC_EQUIVALENCE=NOT_PROVEN\n'
printf 'DIACRITIC_EQUIVALENCE=NOT_PROVEN\n'
printf 'WORD_MEANING=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded observation records with externally supplied opaque structural LEFT/RIGHT context fields; native unordered surface-form pair hypothesis induction by recurrent exact context compatibility; tie ambiguity; persistence; duplicate/collision/malformed/capacity/input-bound refusal; no semantic equivalence claim\n'
printf 'VNM_02_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
