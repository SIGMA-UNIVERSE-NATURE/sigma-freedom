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
EXPECTED_SOURCE=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM_05_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_sigmac=$(sha_of "$SIGMAC")
actual_vm=$(sha_of "$VM")
actual_source=$(sha_of "$SRC")

printf 'SIGMA_PHASE=VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_SPAN_GENERATION=NO\n'
printf 'HOST_SPAN_SELECTION=NO\n'
printf 'HOST_BOUNDARY_INFERENCE=NO\n'
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

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=VNM05_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

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

BYTECODE_SHA=$(sha_of "$BC")
printf 'BYTECODE_SHA256=%s\n' "$BYTECODE_SHA"

SOURCE_BEFORE="$actual_source"
BC_BEFORE="$BYTECODE_SHA"

# Dynamic UTF-8-bearing fixtures are created only after source/bytecode freeze.
DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

U_A="điện-${DYN_TAG}"
U_B="mạch-${DYN_TAG}"
U_C="nguồn-${DYN_TAG}"
U_D="động-${DYN_TAG}"

U_A2="học-${DYN_TAG_2}"
U_B2="sâu-${DYN_TAG_2}"

L1="L-${DYN_TAG}-1"
L2="L-${DYN_TAG}-2"
L3="L-${DYN_TAG}-3"
L4="L-${DYN_TAG}-4"
R1="R-${DYN_TAG}-1"
R2="R-${DYN_TAG}-2"
R3="R-${DYN_TAG}-3"
R4="R-${DYN_TAG}-4"

Q1="Q-${DYN_TAG_2}-1"
Q2="Q-${DYN_TAG_2}-2"
Z1="Z-${DYN_TAG_2}-1"
Z2="Z-${DYN_TAG_2}-2"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'DYNAMIC_TAG_SHA256=%s\n' "$(printf '%s' "$DYN_TAG" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"
printf 'DYNAMIC_TAG_2_SHA256=%s\n' "$(printf '%s' "$DYN_TAG_2" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"

LEAK_COUNT=0
if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC" "$BC" >/dev/null 2>&1; then
    LEAK_COUNT=$((LEAK_COUNT + 1))
fi
if "$P/bin/grep" -a -F "$DYN_TAG_2" "$SRC" "$BC" >/dev/null 2>&1; then
    LEAK_COUNT=$((LEAK_COUNT + 1))
fi
[ "$LEAK_COUNT" -eq 0 ] || {
    printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'
    exit 29
}

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
PERSISTENCE_PASS_COUNT=0
COUNTERFACTUAL_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
STATE=""
LAST_LOG=""

fail_gate() {
    CODE="$1"
    REASON="$2"
    printf 'VNM_05_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
    printf 'FAILURE=%s\n' "$REASON"
    exit "$CODE"
}

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1"
    IN="$BASE/input/sequences.memory"
    STATE="$BASE/state/adjacent_span_state.memory"

    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$BASE/input" "$BASE/state"
    : > "$IN"
    : > "$STATE"
}

use_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1"
    IN="$BASE/input/sequences.memory"
    STATE="$BASE/state/adjacent_span_state.memory"
}

clear_input() {
    : > "$IN"
}

add_seq() {
    if [ -s "$IN" ]; then
        printf '\n' >> "$IN"
    fi
    printf 'SEQ||%s||UNITS||%s||SOURCE||%s' "$1" "$2" "$3" >> "$IN"
}

add_raw_line() {
    if [ -s "$IN" ]; then
        printf '\n' >> "$IN"
    fi
    printf '%s' "$1" >> "$IN"
}

run_vm() {
    LABEL="$1"
    LAST_LOG="$LOG/${CASE_NAME}_${LABEL}.log"
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))

    (
        cd "$SANDBOX" || exit 90
        "$VM" "$BC"
    ) >"$LAST_LOG" 2>&1
    RC=$?

    printf '\n=== %s / %s ===\n' "$CASE_NAME" "$LABEL"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$LAST_LOG"

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        fail_gate 50 VM_NONZERO
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        fail_gate 51 STEP_LIMIT_HIT
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'EXPECTED=%s %s\n' "$KEY" "$VALUE"
        fail_gate 60 MISSING_EXPECTED_OUTPUT
    fi
}

pass_common() {
    expect_line ARTIFACT_ORIGIN TEACHER_AUTHORED_BOOTSTRAP
    expect_line SUPPORT_UNIT DISTINCT_SEQUENCE_ID
    expect_line SPAN_ORDER_POLICY ORDERED_ADJACENCY
    expect_line SPAN_CANDIDATE_GENERATION_OWNER SIGMA_NATIVE
    expect_line HOST_SPAN_GENERATION NO
    expect_line HOST_SPAN_SELECTION NO
    expect_line HOST_BOUNDARY_INFERENCE NO
    expect_line HOST_LEARNING NO
    expect_line HOST_SEMANTIC_INTERPRETATION NO
    expect_line HOST_SEMANTIC_SUBSTITUTION NO
    expect_line NATURAL_LANGUAGE_TOKENIZATION NOT_PROVEN
    expect_line WORD_BOUNDARY_DETECTION NOT_PROVEN
    expect_line PHRASE_BOUNDARY_DETECTION NOT_PROVEN
    expect_line PHRASE_SEMANTICS NOT_PROVEN
    expect_line VIETNAMESE_SEMANTIC_UNDERSTANDING NOT_PROVEN
    expect_line GENERAL_SEMANTIC_UNDERSTANDING NOT_PROVEN
    expect_line PRODUCTION_STATE_MUTATED NO
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

# 01 — one experience: recurrence threshold must not yet be met.
prepare_case CASE_001_SINGLE_SEQUENCE_INSUFFICIENT
add_seq S1 "$L1~$U_A~$U_B~$R1" "SRC-${DYN_TAG}-1"
run_vm CASE01
expect_line PREVIOUS_STATE_VALID 0
expect_line NEW_UNIQUE_SEQUENCE_COUNT 1
expect_line TOTAL_SEQUENCE_COUNT 1
expect_line SPAN_CANDIDATE_STATUS INSUFFICIENT_RECURRENT_SPAN_EVIDENCE
expect_line QUALIFIED_SPAN_COUNT 0
expect_line STATE_MUTATED 1
pass_common

# 02 — fresh VM, second distinct sequence makes the ordered span recurrent.
use_case CASE_001_SINGLE_SEQUENCE_INSUFFICIENT
clear_input
add_seq S2 "$L2~$U_A~$U_B~$R2" "SRC-${DYN_TAG}-2"
run_vm CASE02
expect_line PREVIOUS_STATE_VALID 1
expect_line PRIOR_SEQUENCE_COUNT 1
expect_line TOTAL_SEQUENCE_COUNT 2
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B"
expect_line SPAN_CANDIDATE_SUPPORT 2
expect_line STATE_MUTATED 1
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# 03 — state-only fresh VM must retain the learned candidate.
use_case CASE_001_SINGLE_SEQUENCE_INSUFFICIENT
clear_input
run_vm CASE03
expect_line PREVIOUS_STATE_VALID 1
expect_line PRIOR_SEQUENCE_COUNT 2
expect_line NEW_UNIQUE_SEQUENCE_COUNT 0
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B"
expect_line SPAN_CANDIDATE_SUPPORT 2
expect_line STATE_MUTATED 0
pass_common
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# 04 — one competing recurrent-span family observation is insufficient to displace the leader.
use_case CASE_001_SINGLE_SEQUENCE_INSUFFICIENT
clear_input
add_seq S3 "$L3~$U_C~$U_D~$R3" "SRC-${DYN_TAG}-3"
run_vm CASE04
expect_line TOTAL_SEQUENCE_COUNT 3
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B"
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common

# 05 — second competing sequence creates a genuine support tie, so selection is withheld.
use_case CASE_001_SINGLE_SEQUENCE_INSUFFICIENT
clear_input
add_seq S4 "$L4~$U_C~$U_D~$R4" "SRC-${DYN_TAG}-4"
run_vm CASE05
expect_line TOTAL_SEQUENCE_COUNT 4
expect_line QUALIFIED_SPAN_COUNT 2
expect_line SPAN_CANDIDATE_STATUS AMBIGUOUS_ADJACENT_SPAN_CANDIDATE
expect_line SPAN_CANDIDATE_UNIT_A NONE
expect_line SPAN_CANDIDATE_UNIT_B NONE
expect_line SPAN_CANDIDATE_SUPPORT 2
expect_line STATE_MUTATED 1
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))

# 06 — one four-unit sequence yields three adjacent occurrences but no recurrent candidate.
prepare_case CASE_006_THREE_OCCURRENCES_ONE_SEQUENCE
add_seq F1 "$L1~$U_A~$U_B~$R1" F-SRC
run_vm CASE06
expect_line ADJACENT_OCCURRENCE_COUNT 3
expect_line CANDIDATE_SPAN_COUNT 3
expect_line QUALIFIED_SPAN_COUNT 0
expect_line SPAN_CANDIDATE_STATUS INSUFFICIENT_RECURRENT_SPAN_EVIDENCE
pass_common

# 07 — A->B and B->A are distinct ordered spans and must not pool support.
prepare_case CASE_007_ORDER_DIRECTION_NEGATIVE
add_seq O1 "$L1~$U_A~$U_B~$R1" O-SRC-1
add_seq O2 "$L2~$U_B~$U_A~$R2" O-SRC-2
run_vm CASE07
expect_line QUALIFIED_SPAN_COUNT 0
expect_line SPAN_CANDIDATE_STATUS INSUFFICIENT_RECURRENT_SPAN_EVIDENCE
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 08 — repeated A->B twice inside one sequence counts as one distinct-sequence support.
prepare_case CASE_008_SAME_SEQUENCE_NO_SUPPORT_INFLATION
add_seq D1 "$U_A~$U_B~$U_A~$U_B" D-SRC
run_vm CASE08
expect_line ADJACENT_OCCURRENCE_COUNT 3
expect_line CANDIDATE_SPAN_COUNT 2
expect_line QUALIFIED_SPAN_COUNT 0
expect_line SPAN_CANDIDATE_STATUS INSUFFICIENT_RECURRENT_SPAN_EVIDENCE
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 09 — unique strongest recurrent ordered span is selected.
prepare_case CASE_009_UNIQUE_STRONGEST
add_seq U1 "$L1~$U_A~$U_B~$R1" U-SRC-1
add_seq U2 "$L2~$U_A~$U_B~$R2" U-SRC-2
add_seq U3 "$L3~$U_C~$U_D~$R3" U-SRC-3
run_vm CASE09
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B"
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common

# 10 — two independent recurrent spans at equal support remain ambiguous.
prepare_case CASE_010_BATCH_TIE
add_seq T1 "$L1~$U_A~$U_B~$R1" T-SRC-1
add_seq T2 "$L2~$U_A~$U_B~$R2" T-SRC-2
add_seq T3 "$L3~$U_C~$U_D~$R3" T-SRC-3
add_seq T4 "$L4~$U_C~$U_D~$R4" T-SRC-4
run_vm CASE10
expect_line QUALIFIED_SPAN_COUNT 2
expect_line SPAN_CANDIDATE_STATUS AMBIGUOUS_ADJACENT_SPAN_CANDIDATE
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 11 — exact duplicate sequence ID+fingerprint is idempotent and cannot inflate support.
prepare_case CASE_011_DUPLICATE_IDEMPOTENT
add_seq X1 "$L1~$U_A~$U_B~$R1" X-SRC-1
add_seq X1 "$L1~$U_A~$U_B~$R1" X-SRC-1
add_seq X2 "$L2~$U_A~$U_B~$R2" X-SRC-2
run_vm CASE11
expect_line DUPLICATE_SEQUENCE_COUNT 1
expect_line NEW_UNIQUE_SEQUENCE_COUNT 2
expect_line TOTAL_SEQUENCE_COUNT 2
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 12 — same sequence ID with a different fingerprint is a refusal with no state mutation.
prepare_case CASE_012_SEQUENCE_ID_COLLISION
add_seq C1 "$L1~$U_A~$U_B~$R1" C-SRC-1
add_seq C1 "$L2~$U_C~$U_D~$R2" C-SRC-2
STATE_BEFORE=$(sha_of "$STATE")
run_vm CASE12
expect_line SEQUENCE_ID_COLLISION_COUNT 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_ID_COLLISION
expect_line STATE_COMMIT_ALLOWED 0
expect_line STATE_MUTATED 0
STATE_AFTER=$(sha_of "$STATE")
[ "$STATE_BEFORE" = "$STATE_AFTER" ] || fail_gate 70 REFUSAL_MUTATED_STATE
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 13 — malformed record refusal.
prepare_case CASE_013_MALFORMED
add_raw_line 'BROKEN||SEQ'
STATE_BEFORE=$(sha_of "$STATE")
run_vm CASE13
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_line STATE_MUTATED 0
STATE_AFTER=$(sha_of "$STATE")
[ "$STATE_BEFORE" = "$STATE_AFTER" ] || fail_gate 71 REFUSAL_MUTATED_STATE
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 14 — two-unit sequences are outside the admitted 3/4-unit ABI.
prepare_case CASE_014_TOO_FEW_UNITS
add_seq F2 "$U_A~$U_B" FEW-SRC
run_vm CASE14
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_line STATE_MUTATED 0
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 15 — five-unit sequences are outside the bounded ABI.
prepare_case CASE_015_TOO_MANY_UNITS
add_seq M5 "$L1~$U_A~$U_B~$R1~EXTRA" MANY-SRC
run_vm CASE15
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_line STATE_MUTATED 0
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 16 — empty unit is invalid; delimiter presence is not itself a valid boundary observation.
prepare_case CASE_016_EMPTY_UNIT
add_seq E1 "$U_A~~$U_B" EMPTY-SRC
run_vm CASE16
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_RECORD_INVALID
expect_line STATE_MUTATED 0
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 17 — fifth unique sequence exceeds persistent sequence capacity and must fail closed.
prepare_case CASE_017_SEQUENCE_CAPACITY
add_seq K1 "$L1~$U_A~$U_B~$R1" K-SRC-1
add_seq K2 "$L2~$U_A~$U_B~$R2" K-SRC-2
add_seq K3 "$L3~$U_C~$U_D~$R3" K-SRC-3
add_seq K4 "$L4~$U_C~$U_D~$R4" K-SRC-4
add_seq K5 "$Q1~$U_A2~$U_B2~$Z1" K-SRC-5
run_vm CASE17
expect_line SEQUENCE_CAPACITY_EXCEEDED 1
expect_line SPAN_CANDIDATE_STATUS REFUSED_SEQUENCE_CAPACITY
expect_line STATE_MUTATED 0
expect_line ADJACENT_OCCURRENCE_COUNT 0
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 18 — raw line bound (>8) fails before record scan.
prepare_case CASE_018_RAW_INPUT_BOUND
add_seq B1 "$L1~$U_A~$U_B~$R1" B-SRC-1
add_seq B2 "$L2~$U_A~$U_B~$R2" B-SRC-2
add_seq B3 "$L3~$U_C~$U_D~$R3" B-SRC-3
add_seq B4 "$L4~$U_C~$U_D~$R4" B-SRC-4
add_seq B5 "$Q1~$U_A2~$U_B2~$Z1" B-SRC-5
add_seq B6 "$Q2~$U_A2~$U_B2~$Z2" B-SRC-6
add_seq B7 "X1~X2~X3" B-SRC-7
add_seq B8 "Y1~Y2~Y3" B-SRC-8
add_seq B9 "Z1~Z2~Z3" B-SRC-9
run_vm CASE18
expect_line INPUT_BOUND_EXCEEDED 1
expect_line NEW_SEQUENCE_LINE_COUNT 0
expect_line SPAN_CANDIDATE_STATUS REFUSED_INPUT_BOUND
expect_line STATE_MUTATED 0
expect_line ADJACENT_OCCURRENCE_COUNT 0
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 19 — materially different high-entropy UTF-8 pair, replay A.
prepare_case CASE_019_REPLAY_A
add_seq RPA1 "$Q1~$U_A2~$U_B2~$Z1" REPLAY-SRC-1
add_seq RPA2 "$Q2~$U_A2~$U_B2~$Z2" REPLAY-SRC-2
run_vm CASE19
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A2"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B2"
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common
REPLAY_A_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_A_STATE_SHA=$(sha_of "$STATE")
COUNTERFACTUAL_PASS_COUNT=$((COUNTERFACTUAL_PASS_COUNT + 1))

# 20 — identical full input/prestate replay B must be byte-identical.
prepare_case CASE_020_REPLAY_B
add_seq RPA1 "$Q1~$U_A2~$U_B2~$Z1" REPLAY-SRC-1
add_seq RPA2 "$Q2~$U_A2~$U_B2~$Z2" REPLAY-SRC-2
run_vm CASE20
expect_line SPAN_CANDIDATE_STATUS ADJACENT_SPAN_CANDIDATE_INDUCED
expect_line SPAN_CANDIDATE_UNIT_A "$U_A2"
expect_line SPAN_CANDIDATE_UNIT_B "$U_B2"
expect_line SPAN_CANDIDATE_SUPPORT 2
pass_common
REPLAY_B_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_B_STATE_SHA=$(sha_of "$STATE")

REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=NO
if [ "$REPLAY_A_LOG_SHA" = "$REPLAY_B_LOG_SHA" ] \
    && [ "$REPLAY_A_STATE_SHA" = "$REPLAY_B_STATE_SHA" ]; then
    REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
fi
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 80 REPLAY_MISMATCH

SOURCE_AFTER=$(sha_of "$SRC")
BC_AFTER=$(sha_of "$BC")

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
if [ "$SOURCE_BEFORE" = "$SOURCE_AFTER" ]; then
    SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi
if [ "$BC_BEFORE" = "$BC_AFTER" ]; then
    BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi

printf '\n=== VNM-05 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION\n'
printf 'CAPABILITY_NAME=Native recurrent ordered adjacent-span candidate induction over delimiter-defined UTF-8 units\n'
printf 'TEACHING_GOAL=SIGMA natively induces a bounded ordered width-2 adjacent-span candidate from recurrent distinct-sequence evidence and persistent state\n'
printf 'DEPENDENCIES=VNM04_ADMITTED_FULL_STRUCTURAL_CHAIN_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
printf 'SOURCE_SHA256=%s\n' "$SOURCE_AFTER"
printf 'BYTECODE_SHA256=%s\n' "$BC_AFTER"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_PASS_COUNT=%s\n' "$NEGATIVE_PASS_COUNT"
printf 'PERSISTENCE_PASS_COUNT=%s\n' "$PERSISTENCE_PASS_COUNT"
printf 'COUNTERFACTUAL_PASS_COUNT=%s\n' "$COUNTERFACTUAL_PASS_COUNT"
printf 'INPUT_DYNAMIC=YES\n'
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=YES\n'
printf 'PERSISTENT_STATE_TEST=PASS\n'
printf 'RESTART_REPLAY_TEST=PASS\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=%s\n' "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION"
printf 'DISTINCT_SEQUENCE_SUPPORT_TEST=PASS\n'
printf 'ORDERED_ADJACENCY_TEST=PASS\n'
printf 'TIE_AMBIGUITY_TEST=PASS\n'
printf 'SPAN_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_SPAN_GENERATION=NO\n'
printf 'HOST_SPAN_SELECTION=NO\n'
printf 'HOST_BOUNDARY_INFERENCE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$LEAK_COUNT"
printf 'STEP_LIMIT_STATUS=PASS_IN_20_INVOCATION_BOUNDED_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN\n'
printf 'WORD_BOUNDARY_DETECTION=NOT_PROVEN\n'
printf 'PHRASE_BOUNDARY_DETECTION=NOT_PROVEN\n'
printf 'PHRASE_SEMANTICS=NOT_PROVEN\n'
printf 'WORD_MEANING=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded 3-or-4 externally delimiter-defined UTF-8 unit sequences; native ordered width-2 adjacent-span generation; support by distinct sequence ID; persistent recurrence accumulation; strongest-candidate selection; tie ambiguity; duplicate/collision/malformed/capacity/input-bound refusal; no natural-language boundary or semantic phrase claim\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 20 ] || fail_gate 90 TOTAL_VM_INVOCATIONS_MISMATCH
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 20 ] || fail_gate 91 ALIGNMENT_PASS_COUNT_MISMATCH
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || fail_gate 92 ALIGNMENT_FAIL_COUNT_NONZERO
[ "$VM_NONZERO_COUNT" -eq 0 ] || fail_gate 93 VM_NONZERO_COUNT_NONZERO
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || fail_gate 94 STEP_LIMIT_HIT_COUNT_NONZERO
[ "$NEGATIVE_PASS_COUNT" -eq 11 ] || fail_gate 95 NEGATIVE_PASS_COUNT_MISMATCH
[ "$PERSISTENCE_PASS_COUNT" -eq 3 ] || fail_gate 96 PERSISTENCE_PASS_COUNT_MISMATCH
[ "$COUNTERFACTUAL_PASS_COUNT" -eq 1 ] || fail_gate 97 COUNTERFACTUAL_PASS_COUNT_MISMATCH
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 98 REPLAY_DECISION_NOT_YES
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 99 SOURCE_CHANGED
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 100 BYTECODE_CHANGED
[ "$LEAK_COUNT" -eq 0 ] || fail_gate 101 DYNAMIC_TOKEN_LEAK_NONZERO

printf 'VNM_05_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
