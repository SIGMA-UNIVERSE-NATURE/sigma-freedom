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
EXPECTED_VNM05_SOURCE=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6
EXPECTED_VNM05_BYTECODE=a2b93c79733837b8e6c8b0c5a8d6368fc2f308bd71fc8ce0befded03c9b78912
EXPECTED_VNM06_SOURCE=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5

SRC05="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigma"
SRC06="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_VNM_06_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC05="$ROOT/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigmab"
BC06="$ROOT/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab"

mkdir -p "$ROOT" "$LOG"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || { printf 'HOLD=VNM_06_PREFLIGHT_ALREADY_RUNNING\n'; exit 20; }

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_sigmac=$(sha_of "$SIGMAC")
actual_vm=$(sha_of "$VM")
actual_source05=$(sha_of "$SRC05")
actual_source06=$(sha_of "$SRC06")

printf 'SIGMA_PHASE=VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_SPAN_CANDIDATE_GENERATION=NO\n'
printf 'HOST_SPAN_MATCHING=NO\n'
printf 'HOST_SPAN_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_BOUNDARY_INFERENCE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'ACTIVE_PYTHON_COGNITION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'VNM05_SOURCE_SHA256=%s\n' "$actual_source05"
printf 'VNM06_SOURCE_SHA256=%s\n' "$actual_source06"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source05" = "$EXPECTED_VNM05_SOURCE" ] || { printf 'HOLD=VNM05_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$actual_source06" = "$EXPECTED_VNM06_SOURCE" ] || { printf 'HOLD=VNM06_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }

for forbidden in 'summarize' 'classify_topic' 'semantic_similarity' 'choose_lesson' 'score_knowledge' 'detect_knowledge_gap' 'choose_research_goal' 'decide_truth' 'select_candidate'; do
    if "$P/bin/grep" -F "$forbidden" "$SRC06" >/dev/null 2>&1; then
        printf 'HOLD=FORBIDDEN_HOST_SEMANTIC_OPERATION_TOKEN\nTOKEN=%s\n' "$forbidden"
        exit 25
    fi
done

"$P/bin/rm" -f -- "$BC05.partial" "$BC05" "$BC06.partial" "$BC06"
"$SIGMAC" "$SRC05" "$BC05.partial"
CRC05=$?
printf 'VNM05_SIGMAC_RC=%s\n' "$CRC05"
[ "$CRC05" -eq 0 ] || exit 26
[ -s "$BC05.partial" ] || exit 27
"$P/bin/mv" -f -- "$BC05.partial" "$BC05" || exit 28
"$P/bin/chmod" 0400 "$BC05" || exit 29
VNM05_BYTECODE_SHA=$(sha_of "$BC05")
printf 'VNM05_BYTECODE_SHA256=%s\n' "$VNM05_BYTECODE_SHA"
[ "$VNM05_BYTECODE_SHA" = "$EXPECTED_VNM05_BYTECODE" ] || { printf 'HOLD=VNM05_BYTECODE_IDENTITY_MISMATCH\n'; exit 30; }

"$SIGMAC" "$SRC06" "$BC06.partial"
CRC06=$?
printf 'VNM06_SIGMAC_RC=%s\n' "$CRC06"
[ "$CRC06" -eq 0 ] || exit 31
[ -s "$BC06.partial" ] || exit 32
"$P/bin/mv" -f -- "$BC06.partial" "$BC06" || exit 33
"$P/bin/chmod" 0400 "$BC06" || exit 34
VNM06_BYTECODE_SHA=$(sha_of "$BC06")
printf 'VNM06_BYTECODE_SHA256=%s\n' "$VNM06_BYTECODE_SHA"

SOURCE05_BEFORE="$actual_source05"
SOURCE06_BEFORE="$actual_source06"
BC05_BEFORE="$VNM05_BYTECODE_SHA"
BC06_BEFORE="$VNM06_BYTECODE_SHA"

DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
A="điện-${DYN_TAG}"
B="mạch-${DYN_TAG}"
A2="học-${DYN_TAG_2}"
B2="sâu-${DYN_TAG_2}"
L1="L-${DYN_TAG}-1"
L2="L-${DYN_TAG}-2"
R1="R-${DYN_TAG}-1"
R2="R-${DYN_TAG}-2"
Q1="Q-${DYN_TAG_2}-1"
Q2="Q-${DYN_TAG_2}-2"
Z1="Z-${DYN_TAG_2}-1"
Z2="Z-${DYN_TAG_2}-2"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
LEAK_COUNT=0
for token in "$DYN_TAG" "$DYN_TAG_2"; do
    if "$P/bin/grep" -a -F "$token" "$SRC05" "$BC05" "$SRC06" "$BC06" >/dev/null 2>&1; then
        LEAK_COUNT=$((LEAK_COUNT + 1))
    fi
done
[ "$LEAK_COUNT" -eq 0 ] || { printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'; exit 35; }

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
VNM05_VM_INVOCATIONS=0
VNM06_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
INTEGRATION_PASS_COUNT=0
COUNTERFACTUAL_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE06=""
CANDIDATE_FILE=""
SEQUENCE_FILE=""
OUTPUT_FILE=""
LAST_LOG=""

fail_gate() {
    CODE="$1"
    REASON="$2"
    printf 'VNM_06_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
    printf 'FAILURE=%s\n' "$REASON"
    exit "$CODE"
}

prepare06() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE06="$SANDBOX/.sigma_exec/SIGMA_VNM_06_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1"
    CANDIDATE_FILE="$BASE06/input/candidate.memory"
    SEQUENCE_FILE="$BASE06/input/sequences.memory"
    OUTPUT_FILE="$BASE06/output/span_observations.memory"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$BASE06/input" "$BASE06/output"
    : > "$CANDIDATE_FILE"
    : > "$SEQUENCE_FILE"
    : > "$OUTPUT_FILE"
}

add_seq06() {
    if [ -s "$SEQUENCE_FILE" ]; then printf '\n' >> "$SEQUENCE_FILE"; fi
    printf 'SEQ||%s||UNITS||%s||SOURCE||%s' "$1" "$2" "$3" >> "$SEQUENCE_FILE"
}

add_raw06() {
    if [ -s "$SEQUENCE_FILE" ]; then printf '\n' >> "$SEQUENCE_FILE"; fi
    printf '%s' "$1" >> "$SEQUENCE_FILE"
}

set_candidate() {
    printf 'CANDIDATE||STATUS||%s||UNIT_A||%s||UNIT_B||%s||SUPPORT||%s' "$1" "$2" "$3" "$4" > "$CANDIDATE_FILE"
}

run06() {
    LABEL="$1"
    LAST_LOG="$LOG/${CASE_NAME}_${LABEL}.log"
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))
    VNM06_VM_INVOCATIONS=$((VNM06_VM_INVOCATIONS + 1))
    ( cd "$SANDBOX" || exit 90; "$VM" "$BC06" ) >"$LAST_LOG" 2>&1
    RC=$?
    printf '\n=== %s / %s ===\nVM_RC=%s\n' "$CASE_NAME" "$LABEL" "$RC"
    "$P/bin/cat" "$LAST_LOG"
    if [ "$RC" -ne 0 ]; then VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1)); fail_gate 50 VM_NONZERO; fi
    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1)); fail_gate 51 STEP_LIMIT_HIT; fi
}

expect_line() {
    KEY="$1"; VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'EXPECTED=%s %s\n' "$KEY" "$VALUE"
        fail_gate 60 MISSING_EXPECTED_OUTPUT
    fi
}

pass_common() {
    expect_line ARTIFACT_ORIGIN TEACHER_AUTHORED_BOOTSTRAP
    expect_line SPAN_CONTEXT_DERIVATION_OWNER SIGMA_NATIVE
    expect_line HOST_SPAN_MATCHING NO
    expect_line HOST_SPAN_CONTEXT_EXTRACTION NO
    expect_line HOST_BOUNDARY_INFERENCE NO
    expect_line HOST_LEARNING NO
    expect_line HOST_SEMANTIC_INTERPRETATION NO
    expect_line HOST_SEMANTIC_SUBSTITUTION NO
    expect_line PERSISTENT_STATE NO
    expect_line NATURAL_LANGUAGE_TOKENIZATION NOT_PROVEN
    expect_line WORD_BOUNDARY_DETECTION NOT_PROVEN
    expect_line PHRASE_BOUNDARY_DETECTION NOT_PROVEN
    expect_line PHRASE_SEMANTICS NOT_PROVEN
    expect_line VIETNAMESE_SEMANTIC_UNDERSTANDING NOT_PROVEN
    expect_line GENERAL_SEMANTIC_UNDERSTANDING NOT_PROVEN
    expect_line PRODUCTION_STATE_MUTATED NO
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

make_native_candidate() {
    NAME="$1"; UA="$2"; UB="$3"; LEFTA="$4"; RIGHTA="$5"; LEFTB="$6"; RIGHTB="$7"
    SBOX="$CASES/$NAME"
    BASE05="$SBOX/.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1"
    IN05="$BASE05/input/sequences.memory"
    STATE05="$BASE05/state/adjacent_span_state.memory"
    "$P/bin/rm" -rf -- "$SBOX"
    "$P/bin/mkdir" -p "$BASE05/input" "$BASE05/state"
    : > "$IN05"
    : > "$STATE05"
    printf 'SEQ||N1||UNITS||%s~%s~%s~%s||SOURCE||N-SRC-1\n' "$LEFTA" "$UA" "$UB" "$RIGHTA" > "$IN05"
    printf 'SEQ||N2||UNITS||%s~%s~%s~%s||SOURCE||N-SRC-2' "$LEFTB" "$UA" "$UB" "$RIGHTB" >> "$IN05"
    NLOG="$LOG/${NAME}_VNM05.log"
    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))
    VNM05_VM_INVOCATIONS=$((VNM05_VM_INVOCATIONS + 1))
    ( cd "$SBOX" || exit 90; "$VM" "$BC05" ) >"$NLOG" 2>&1
    NRC=$?
    printf '\n=== %s / VNM05_NATIVE_CANDIDATE ===\nVM_RC=%s\n' "$NAME" "$NRC"
    "$P/bin/cat" "$NLOG"
    if [ "$NRC" -ne 0 ]; then VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1)); CASE_NAME="$NAME"; fail_gate 52 VNM05_VM_NONZERO; fi
    if "$P/bin/grep" -F 'Step limit exceeded' "$NLOG" >/dev/null 2>&1; then STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1)); CASE_NAME="$NAME"; fail_gate 53 VNM05_STEP_LIMIT_HIT; fi

    N_STATUS=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_STATUS" {sub(/^SPAN_CANDIDATE_STATUS /,""); printf "%s",$0; exit}' "$NLOG")
    N_A=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_UNIT_A" {sub(/^SPAN_CANDIDATE_UNIT_A /,""); printf "%s",$0; exit}' "$NLOG")
    N_B=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_UNIT_B" {sub(/^SPAN_CANDIDATE_UNIT_B /,""); printf "%s",$0; exit}' "$NLOG")
    N_SUPPORT=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_SUPPORT" {sub(/^SPAN_CANDIDATE_SUPPORT /,""); printf "%s",$0; exit}' "$NLOG")

    [ "$N_STATUS" = ADJACENT_SPAN_CANDIDATE_INDUCED ] || { CASE_NAME="$NAME"; fail_gate 54 VNM05_DID_NOT_EMIT_INDUCED_CANDIDATE; }
    NATIVE_STATUS="$N_STATUS"
    NATIVE_A="$N_A"
    NATIVE_B="$N_B"
    NATIVE_SUPPORT="$N_SUPPORT"
}

# Generate two native VNM-05 candidates after both bytecodes are frozen.
NATIVE_STATUS=""
NATIVE_A=""
NATIVE_B=""
NATIVE_SUPPORT=""
make_native_candidate NATIVE_CANDIDATE_1 "$A" "$B" "$L1" "$R1" "$L2" "$R2"
N1_STATUS="$NATIVE_STATUS"
N1_A="$NATIVE_A"
N1_B="$NATIVE_B"
N1_SUPPORT="$NATIVE_SUPPORT"
[ "$N1_A" = "$A" ] && [ "$N1_B" = "$B" ] || { CASE_NAME=NATIVE_CANDIDATE_1; fail_gate 55 VNM05_NATIVE_CANDIDATE_ALIGNMENT_FAIL; }

make_native_candidate NATIVE_CANDIDATE_2 "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2"
N2_STATUS="$NATIVE_STATUS"
N2_A="$NATIVE_A"
N2_B="$NATIVE_B"
N2_SUPPORT="$NATIVE_SUPPORT"
[ "$N2_A" = "$A2" ] && [ "$N2_B" = "$B2" ] || { CASE_NAME=NATIVE_CANDIDATE_2; fail_gate 56 VNM05_NATIVE_COUNTERFACTUAL_ALIGNMENT_FAIL; }

# 01 native candidate -> two interior span-context observations.
prepare06 CASE_001_NATIVE_CANDIDATE_TWO_INTERIOR
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 I1 "$L1~$A~$B~$R1" "SRC-${DYN_TAG}-1"
add_seq06 I2 "$L2~$A~$B~$R2" "SRC-${DYN_TAG}-2"
run06 CASE01
expect_line CANDIDATE_VALID 1
expect_line MATCHING_SPAN_OCCURRENCE_COUNT 2
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 2
expect_line EDGE_MATCH_WITHHELD_COUNT 0
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
expect_line OUTPUT_WRITE_READBACK_MATCH 1
pass_common
EXPECTED1="SPAN_OBS||I1||UNIT_A||$A||UNIT_B||$B||LEFT||$L1||RIGHT||$R1||SOURCE||SRC-${DYN_TAG}-1"
EXPECTED2="SPAN_OBS||I2||UNIT_A||$A||UNIT_B||$B||LEFT||$L2||RIGHT||$R2||SOURCE||SRC-${DYN_TAG}-2"
[ "$(sed -n '1p' "$OUTPUT_FILE")" = "$EXPECTED1" ] || fail_gate 61 OUTPUT_LINE1_MISMATCH
[ "$(sed -n '2p' "$OUTPUT_FILE")" = "$EXPECTED2" ] || fail_gate 62 OUTPUT_LINE2_MISMATCH
INTEGRATION_PASS_COUNT=$((INTEGRATION_PASS_COUNT + 1))

# 02 one interior occurrence.
prepare06 CASE_002_SINGLE_INTERIOR
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 S1 "$L1~$A~$B~$R1" S-SRC
run06 CASE02
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 1
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
pass_common

# 03 left-edge occurrence is withheld.
prepare06 CASE_003_LEFT_EDGE_WITHHELD
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 E1 "$A~$B~$R1" E-SRC-1
run06 CASE03
expect_line MATCHING_SPAN_OCCURRENCE_COUNT 1
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 0
expect_line EDGE_MATCH_WITHHELD_COUNT 1
expect_line DERIVATION_STATUS NO_INTERIOR_SPAN_CONTEXT_OBSERVATION
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 04 right-edge occurrence is withheld.
prepare06 CASE_004_RIGHT_EDGE_WITHHELD
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 E2 "$L1~$A~$B" E-SRC-2
run06 CASE04
expect_line MATCHING_SPAN_OCCURRENCE_COUNT 1
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 0
expect_line EDGE_MATCH_WITHHELD_COUNT 1
expect_line DERIVATION_STATUS NO_INTERIOR_SPAN_CONTEXT_OBSERVATION
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 05 reversed order does not match.
prepare06 CASE_005_ORDERED_NONMATCH
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 O1 "$L1~$B~$A~$R1" O-SRC
run06 CASE05
expect_line MATCHING_SPAN_OCCURRENCE_COUNT 0
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 0
expect_line DERIVATION_STATUS NO_INTERIOR_SPAN_CONTEXT_OBSERVATION
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 06 mixed interior + edge evidence.
prepare06 CASE_006_MIXED_INTERIOR_EDGE
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 M1 "$L1~$A~$B~$R1" M-SRC-1
add_seq06 M2 "$A~$B~$R2" M-SRC-2
run06 CASE06
expect_line MATCHING_SPAN_OCCURRENCE_COUNT 2
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 1
expect_line EDGE_MATCH_WITHHELD_COUNT 1
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 07 exact duplicate sequence is idempotent.
prepare06 CASE_007_DUPLICATE_IDEMPOTENT
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 D1 "$L1~$A~$B~$R1" D-SRC
add_seq06 D1 "$L1~$A~$B~$R1" D-SRC
run06 CASE07
expect_line DUPLICATE_SEQUENCE_COUNT 1
expect_line UNIQUE_SEQUENCE_COUNT 1
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 1
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 08 same sequence ID different fingerprint refuses without output mutation.
prepare06 CASE_008_ID_COLLISION
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
printf 'SENTINEL' > "$OUTPUT_FILE"
add_seq06 C1 "$L1~$A~$B~$R1" C-SRC-1
add_seq06 C1 "$L2~$A~$B~$R2" C-SRC-2
BEFORE=$(sha_of "$OUTPUT_FILE")
run06 CASE08
expect_line SEQUENCE_ID_COLLISION_COUNT 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_ID_COLLISION
AFTER=$(sha_of "$OUTPUT_FILE")
[ "$BEFORE" = "$AFTER" ] || fail_gate 63 REFUSAL_MUTATED_OUTPUT
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 09 malformed sequence refuses.
prepare06 CASE_009_MALFORMED
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
printf 'SENTINEL' > "$OUTPUT_FILE"
add_raw06 'BROKEN||SEQ'
BEFORE=$(sha_of "$OUTPUT_FILE")
run06 CASE09
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_RECORD_INVALID
AFTER=$(sha_of "$OUTPUT_FILE")
[ "$BEFORE" = "$AFTER" ] || fail_gate 64 REFUSAL_MUTATED_OUTPUT
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 10 two-unit sequence refuses.
prepare06 CASE_010_TOO_FEW_UNITS
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 F2 "$A~$B" F-SRC
run06 CASE10
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_RECORD_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 11 five-unit sequence refuses.
prepare06 CASE_011_TOO_MANY_UNITS
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 F5 "$L1~$A~$B~$R1~EXTRA" F5-SRC
run06 CASE11
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_RECORD_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 12 empty unit refuses.
prepare06 CASE_012_EMPTY_UNIT
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 EU "$L1~~$B~$R1" EU-SRC
run06 CASE12
expect_line INVALID_SEQUENCE_RECORD_COUNT 1
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_RECORD_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 13 fifth unique sequence exceeds capacity.
prepare06 CASE_013_SEQUENCE_CAPACITY
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
add_seq06 K1 "$L1~$A~$B~$R1" K-SRC-1
add_seq06 K2 "$L2~$A~$B~$R2" K-SRC-2
add_seq06 K3 "X1~X2~X3" K-SRC-3
add_seq06 K4 "Y1~Y2~Y3" K-SRC-4
add_seq06 K5 "Z1~Z2~Z3" K-SRC-5
run06 CASE13
expect_line SEQUENCE_CAPACITY_EXCEEDED 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line DERIVATION_STATUS REFUSED_SEQUENCE_CAPACITY
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 14 >8 raw lines refuses before scan.
prepare06 CASE_014_INPUT_BOUND
set_candidate "$N1_STATUS" "$N1_A" "$N1_B" "$N1_SUPPORT"
for i in 1 2 3 4 5 6 7 8 9; do add_seq06 "B$i" "X${i}a~X${i}b~X${i}c" "B-SRC-$i"; done
run06 CASE14
expect_line INPUT_BOUND_EXCEEDED 1
expect_line NEW_SEQUENCE_LINE_COUNT 0
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line DERIVATION_STATUS REFUSED_INPUT_BOUND
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 15 malformed candidate refuses without output mutation.
prepare06 CASE_015_MALFORMED_CANDIDATE
printf 'BROKEN_CANDIDATE' > "$CANDIDATE_FILE"
printf 'SENTINEL' > "$OUTPUT_FILE"
add_seq06 MC "$L1~$A~$B~$R1" MC-SRC
BEFORE=$(sha_of "$OUTPUT_FILE")
run06 CASE15
expect_line CANDIDATE_VALID 0
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line DERIVATION_STATUS REFUSED_CANDIDATE_INVALID
AFTER=$(sha_of "$OUTPUT_FILE")
[ "$BEFORE" = "$AFTER" ] || fail_gate 65 REFUSAL_MUTATED_OUTPUT
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 16 non-induced candidate status refuses; host does not reinterpret ambiguity as a candidate.
prepare06 CASE_016_NON_INDUCED_STATUS
set_candidate AMBIGUOUS_ADJACENT_SPAN_CANDIDATE "$A" "$B" 2
add_seq06 NI "$L1~$A~$B~$R1" NI-SRC
run06 CASE16
expect_line CANDIDATE_VALID 0
expect_line DERIVATION_STATUS REFUSED_CANDIDATE_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 17 materially different native VNM-05 candidate changes VNM-06 output.
prepare06 CASE_017_COUNTERFACTUAL_NATIVE_CANDIDATE
set_candidate "$N2_STATUS" "$N2_A" "$N2_B" "$N2_SUPPORT"
add_seq06 RPA1 "$Q1~$A2~$B2~$Z1" REPLAY-SRC-1
add_seq06 RPA2 "$Q2~$A2~$B2~$Z2" REPLAY-SRC-2
run06 CASE17
expect_line CANDIDATE_UNIT_A "$A2"
expect_line CANDIDATE_UNIT_B "$B2"
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 2
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
pass_common
REPLAY_A_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_A_OUTPUT_SHA=$(sha_of "$OUTPUT_FILE")
COUNTERFACTUAL_PASS_COUNT=$((COUNTERFACTUAL_PASS_COUNT + 1))
INTEGRATION_PASS_COUNT=$((INTEGRATION_PASS_COUNT + 1))

# 18 identical pure replay.
prepare06 CASE_018_REPLAY_B
set_candidate "$N2_STATUS" "$N2_A" "$N2_B" "$N2_SUPPORT"
add_seq06 RPA1 "$Q1~$A2~$B2~$Z1" REPLAY-SRC-1
add_seq06 RPA2 "$Q2~$A2~$B2~$Z2" REPLAY-SRC-2
run06 CASE18
expect_line CANDIDATE_UNIT_A "$A2"
expect_line CANDIDATE_UNIT_B "$B2"
expect_line INTERIOR_CONTEXT_OBSERVATION_COUNT 2
expect_line DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED
pass_common
REPLAY_B_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_B_OUTPUT_SHA=$(sha_of "$OUTPUT_FILE")

REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=NO
if [ "$REPLAY_A_LOG_SHA" = "$REPLAY_B_LOG_SHA" ] && [ "$REPLAY_A_OUTPUT_SHA" = "$REPLAY_B_OUTPUT_SHA" ]; then
    REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
fi
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 80 REPLAY_MISMATCH

SOURCE05_AFTER=$(sha_of "$SRC05")
SOURCE06_AFTER=$(sha_of "$SRC06")
BC05_AFTER=$(sha_of "$BC05")
BC06_AFTER=$(sha_of "$BC06")
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
if [ "$SOURCE05_BEFORE" = "$SOURCE05_AFTER" ] && [ "$SOURCE06_BEFORE" = "$SOURCE06_AFTER" ]; then SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES; fi
if [ "$BC05_BEFORE" = "$BC05_AFTER" ] && [ "$BC06_BEFORE" = "$BC06_AFTER" ]; then BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES; fi

printf '\n=== VNM-06 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION\n'
printf 'CAPABILITY_NAME=Native outer-context observation derivation around an induced ordered adjacent span\n'
printf 'TEACHING_GOAL=SIGMA natively matches an exact VNM-05 induced ordered span inside bounded delimiter-defined sequences and derives full LEFT/RIGHT outer-context observations without host span matching or context extraction\n'
printf 'DEPENDENCIES=VNM05_ADMITTED_NATIVE_SPAN_CANDIDATE_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
printf 'SOURCE_SHA256=%s\n' "$SOURCE06_AFTER"
printf 'BYTECODE_SHA256=%s\n' "$BC06_AFTER"
printf 'VNM05_SOURCE_SHA256=%s\n' "$SOURCE05_AFTER"
printf 'VNM05_BYTECODE_SHA256=%s\n' "$BC05_AFTER"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'VNM05_VM_INVOCATIONS=%s\n' "$VNM05_VM_INVOCATIONS"
printf 'VNM06_VM_INVOCATIONS=%s\n' "$VNM06_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_PASS_COUNT=%s\n' "$NEGATIVE_PASS_COUNT"
printf 'INTEGRATION_PASS_COUNT=%s\n' "$INTEGRATION_PASS_COUNT"
printf 'COUNTERFACTUAL_PASS_COUNT=%s\n' "$COUNTERFACTUAL_PASS_COUNT"
printf 'INPUT_DYNAMIC=YES\n'
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=NO\n'
printf 'PERSISTENT_STATE_TEST=NA\n'
printf 'RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=%s\n' "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION"
printf 'VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_SPAN_CANDIDATE_GENERATION=NO\n'
printf 'HOST_SPAN_MATCHING=NO\n'
printf 'HOST_SPAN_CONTEXT_EXTRACTION=NO\n'
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
printf 'CLAIM_SCOPE=Bounded exact native VNM-05 induced ordered width-2 span candidate mechanically routed into VNM-06; native matching inside 3-or-4 externally delimiter-defined UTF-8 unit sequences; full outer LEFT/RIGHT context derived only for interior span occurrences; edge matches withheld; duplicate/collision/malformed/capacity/input-bound refusal; no natural-language boundary or phrase-semantics claim\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 20 ] || fail_gate 90 TOTAL_VM_INVOCATIONS_MISMATCH
[ "$VNM05_VM_INVOCATIONS" -eq 2 ] || fail_gate 91 VNM05_VM_INVOCATIONS_MISMATCH
[ "$VNM06_VM_INVOCATIONS" -eq 18 ] || fail_gate 92 VNM06_VM_INVOCATIONS_MISMATCH
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 18 ] || fail_gate 93 ALIGNMENT_PASS_COUNT_MISMATCH
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || fail_gate 94 ALIGNMENT_FAIL_COUNT_NONZERO
[ "$VM_NONZERO_COUNT" -eq 0 ] || fail_gate 95 VM_NONZERO_COUNT_NONZERO
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || fail_gate 96 STEP_LIMIT_HIT_COUNT_NONZERO
[ "$NEGATIVE_PASS_COUNT" -eq 14 ] || fail_gate 97 NEGATIVE_PASS_COUNT_MISMATCH
[ "$INTEGRATION_PASS_COUNT" -eq 2 ] || fail_gate 98 INTEGRATION_PASS_COUNT_MISMATCH
[ "$COUNTERFACTUAL_PASS_COUNT" -eq 1 ] || fail_gate 99 COUNTERFACTUAL_PASS_COUNT_MISMATCH
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 100 REPLAY_DECISION_NOT_YES
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 101 SOURCE_CHANGED
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 102 BYTECODE_CHANGED
[ "$LEAK_COUNT" -eq 0 ] || fail_gate 103 DYNAMIC_TOKEN_LEAK_NONZERO

printf 'VNM_06_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
