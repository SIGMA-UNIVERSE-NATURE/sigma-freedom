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
EXPECTED_VNM02_SOURCE=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
EXPECTED_VNM02_BYTECODE=bf6f3cac8aade9433f43c13d462a73465eceef0b1e5f5411336cad2e338b0aec
EXPECTED_VNM05_SOURCE=5158343391d7dce0046802162969211c8e7f73b873375a8bc376c0f6ea63c2b6
EXPECTED_VNM05_BYTECODE=a2b93c79733837b8e6c8b0c5a8d6368fc2f308bd71fc8ce0befded03c9b78912
EXPECTED_VNM06_SOURCE=067ab86267ca30167fd482e79486991d763062646a84173e5d55837de31dc5f5
EXPECTED_VNM06_BYTECODE=4cdfc778d5aa169a5c9a0b40482946f3e50b5bfa6c1c10f2f9c3bb48d31d09c1
EXPECTED_VNM07_SOURCE=8412ce07e6c9a53ae6bb27a88ec2847eadd54795a21dce35a3ff1ef29f75a57e

SRC02="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigma"
SRC05="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigma"
SRC06="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigma"
SRC07="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1.sigma"

ROOT="$HOME_SIGMA/SIGMA_VNM_07_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC02="$ROOT/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigmab"
BC05="$ROOT/SIGMA_VNM_05_NATIVE_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1.sigmab"
BC06="$ROOT/SIGMA_VNM_06_NATIVE_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab"
BC07="$ROOT/SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1.sigmab"

mkdir -p "$ROOT" "$LOG"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || { printf 'HOLD=VNM_07_PREFLIGHT_ALREADY_RUNNING\n'; exit 20; }

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_sigmac=$(sha_of "$SIGMAC")
actual_vm=$(sha_of "$VM")
actual_source02=$(sha_of "$SRC02")
actual_source05=$(sha_of "$SRC05")
actual_source06=$(sha_of "$SRC06")
actual_source07=$(sha_of "$SRC07")

printf 'SIGMA_PHASE=VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_FORM_SERIALIZATION=NO\n'
printf 'HOST_OBSERVATION_ID_DERIVATION=NO\n'
printf 'HOST_PAIR_GENERATION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'ACTIVE_PYTHON_COGNITION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'VNM02_SOURCE_SHA256=%s\n' "$actual_source02"
printf 'VNM05_SOURCE_SHA256=%s\n' "$actual_source05"
printf 'VNM06_SOURCE_SHA256=%s\n' "$actual_source06"
printf 'VNM07_SOURCE_SHA256=%s\n' "$actual_source07"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source02" = "$EXPECTED_VNM02_SOURCE" ] || { printf 'HOLD=VNM02_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$actual_source05" = "$EXPECTED_VNM05_SOURCE" ] || { printf 'HOLD=VNM05_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }
[ "$actual_source06" = "$EXPECTED_VNM06_SOURCE" ] || { printf 'HOLD=VNM06_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }
[ "$actual_source07" = "$EXPECTED_VNM07_SOURCE" ] || { printf 'HOLD=VNM07_SOURCE_IDENTITY_MISMATCH\n'; exit 26; }

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
    if "$P/bin/grep" -F "$forbidden" "$SRC07" >/dev/null 2>&1; then
        printf 'HOLD=FORBIDDEN_HOST_SEMANTIC_OPERATION_TOKEN\n'
        printf 'TOKEN=%s\n' "$forbidden"
        exit 27
    fi
done

"$P/bin/rm" -f -- \
    "$BC02.partial" "$BC02" \
    "$BC05.partial" "$BC05" \
    "$BC06.partial" "$BC06" \
    "$BC07.partial" "$BC07"

compile_locked() {
    SRC="$1"
    OUT="$2"
    LABEL="$3"
    "$SIGMAC" "$SRC" "$OUT.partial"
    CRC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$CRC"
    [ "$CRC" -eq 0 ] || exit 30
    [ -s "$OUT.partial" ] || exit 31
    "$P/bin/mv" -f -- "$OUT.partial" "$OUT" || exit 32
    "$P/bin/chmod" 0400 "$OUT" || exit 33
}

compile_locked "$SRC02" "$BC02" VNM02
VNM02_BYTECODE_SHA=$(sha_of "$BC02")
printf 'VNM02_BYTECODE_SHA256=%s\n' "$VNM02_BYTECODE_SHA"
[ "$VNM02_BYTECODE_SHA" = "$EXPECTED_VNM02_BYTECODE" ] || { printf 'HOLD=VNM02_BYTECODE_IDENTITY_MISMATCH\n'; exit 34; }

compile_locked "$SRC05" "$BC05" VNM05
VNM05_BYTECODE_SHA=$(sha_of "$BC05")
printf 'VNM05_BYTECODE_SHA256=%s\n' "$VNM05_BYTECODE_SHA"
[ "$VNM05_BYTECODE_SHA" = "$EXPECTED_VNM05_BYTECODE" ] || { printf 'HOLD=VNM05_BYTECODE_IDENTITY_MISMATCH\n'; exit 35; }

compile_locked "$SRC06" "$BC06" VNM06
VNM06_BYTECODE_SHA=$(sha_of "$BC06")
printf 'VNM06_BYTECODE_SHA256=%s\n' "$VNM06_BYTECODE_SHA"
[ "$VNM06_BYTECODE_SHA" = "$EXPECTED_VNM06_BYTECODE" ] || { printf 'HOLD=VNM06_BYTECODE_IDENTITY_MISMATCH\n'; exit 36; }

compile_locked "$SRC07" "$BC07" VNM07
VNM07_BYTECODE_SHA=$(sha_of "$BC07")
printf 'VNM07_BYTECODE_SHA256=%s\n' "$VNM07_BYTECODE_SHA"

SOURCE02_BEFORE="$actual_source02"
SOURCE05_BEFORE="$actual_source05"
SOURCE06_BEFORE="$actual_source06"
SOURCE07_BEFORE="$actual_source07"
BC02_BEFORE="$VNM02_BYTECODE_SHA"
BC05_BEFORE="$VNM05_BYTECODE_SHA"
BC06_BEFORE="$VNM06_BYTECODE_SHA"
BC07_BEFORE="$VNM07_BYTECODE_SHA"

# Dynamic UTF-8-bearing values are generated only after all source/bytecode identities are frozen.
DYN_TAG_1="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_3="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

SPAN1_A="điện-${DYN_TAG_1}"
SPAN1_B="mạch-${DYN_TAG_1}"
SPAN2_A="học-${DYN_TAG_2}"
SPAN2_B="sâu-${DYN_TAG_2}"
CF_A="nhịp-${DYN_TAG_3}"
CF_B="tín-${DYN_TAG_3}"

GEN1_L="G1L-${DYN_TAG_1}"
GEN1_R="G1R-${DYN_TAG_1}"
GEN2_L="G2L-${DYN_TAG_1}"
GEN2_R="G2R-${DYN_TAG_1}"
GEN3_L="G3L-${DYN_TAG_2}"
GEN3_R="G3R-${DYN_TAG_2}"
GEN4_L="G4L-${DYN_TAG_2}"
GEN4_R="G4R-${DYN_TAG_2}"

CTX1_L="CTX-L-${DYN_TAG_3}-1"
CTX1_R="CTX-R-${DYN_TAG_3}-1"
CTX2_L="CTX-L-${DYN_TAG_3}-2"
CTX2_R="CTX-R-${DYN_TAG_3}-2"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
LEAK_COUNT=0
for token in "$DYN_TAG_1" "$DYN_TAG_2" "$DYN_TAG_3"; do
    if "$P/bin/grep" -a -F "$token" \
        "$SRC02" "$BC02" "$SRC05" "$BC05" "$SRC06" "$BC06" "$SRC07" "$BC07" \
        >/dev/null 2>&1; then
        LEAK_COUNT=$((LEAK_COUNT + 1))
    fi
done
[ "$LEAK_COUNT" -eq 0 ] || { printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'; exit 37; }

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
VNM02_VM_INVOCATIONS=0
VNM05_VM_INVOCATIONS=0
VNM06_VM_INVOCATIONS=0
VNM07_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
INTEGRATION_PASS_COUNT=0
COUNTERFACTUAL_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
BASE07=""
INPUT07=""
OUTPUT07=""
LAST_LOG=""

fail_gate() {
    CODE="$1"
    REASON="$2"
    printf 'VNM_07_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
    printf 'FAILURE=%s\n' "$REASON"
    exit "$CODE"
}

run_component_vm() {
    COMPONENT="$1"
    SANDBOX_ARG="$2"
    BYTECODE_ARG="$3"
    LOG_ARG="$4"

    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))
    if [ "$COMPONENT" = VNM02 ]; then VNM02_VM_INVOCATIONS=$((VNM02_VM_INVOCATIONS + 1)); fi
    if [ "$COMPONENT" = VNM05 ]; then VNM05_VM_INVOCATIONS=$((VNM05_VM_INVOCATIONS + 1)); fi
    if [ "$COMPONENT" = VNM06 ]; then VNM06_VM_INVOCATIONS=$((VNM06_VM_INVOCATIONS + 1)); fi
    if [ "$COMPONENT" = VNM07 ]; then VNM07_VM_INVOCATIONS=$((VNM07_VM_INVOCATIONS + 1)); fi

    (
        cd "$SANDBOX_ARG" || exit 90
        "$VM" "$BYTECODE_ARG"
    ) >"$LOG_ARG" 2>&1
    RC=$?

    printf '\n=== %s / %s ===\n' "$CASE_NAME" "$COMPONENT"
    printf 'VM_RC=%s\n' "$RC"
    "$P/bin/cat" "$LOG_ARG"

    if [ "$RC" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        fail_gate 50 "${COMPONENT}_VM_NONZERO"
    fi
    if "$P/bin/grep" -F 'Step limit exceeded' "$LOG_ARG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        fail_gate 51 "${COMPONENT}_STEP_LIMIT_HIT"
    fi
}

prepare07() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE07="$SANDBOX/.sigma_exec/SIGMA_VNM_07_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1"
    INPUT07="$BASE07/input/span_observations.memory"
    OUTPUT07="$BASE07/output/form_observations.memory"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$BASE07/input" "$BASE07/output"
    : > "$INPUT07"
    : > "$OUTPUT07"
}

add_span_obs07() {
    if [ -s "$INPUT07" ]; then printf '\n' >> "$INPUT07"; fi
    printf 'SPAN_OBS||%s||UNIT_A||%s||UNIT_B||%s||LEFT||%s||RIGHT||%s||SOURCE||%s' \
        "$1" "$2" "$3" "$4" "$5" "$6" >> "$INPUT07"
}

add_raw07() {
    if [ -s "$INPUT07" ]; then printf '\n' >> "$INPUT07"; fi
    printf '%s' "$1" >> "$INPUT07"
}

run07() {
    LABEL="$1"
    LAST_LOG="$LOG/${CASE_NAME}_${LABEL}.log"
    run_component_vm VNM07 "$SANDBOX" "$BC07" "$LAST_LOG"
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

expect_output_line() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$OUTPUT07" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'EXPECTED_OUTPUT_LINE=%s\n' "$VALUE"
        fail_gate 61 MISSING_EXPECTED_OUTPUT_FILE_LINE
    fi
}

pass_common() {
    expect_line ARTIFACT_ORIGIN TEACHER_AUTHORED_BOOTSTRAP
    expect_line FORM_SERIALIZATION_POLICY ORDERED_UNIT_A_TILDE_UNIT_B
    expect_line OBSERVATION_ID_POLICY VNM07_SEQID_AND_ORDERED_SPAN
    expect_line SPAN_FORM_SERIALIZATION_OWNER SIGMA_NATIVE
    expect_line OBSERVATION_ID_DERIVATION_OWNER SIGMA_NATIVE
    expect_line HOST_FORM_SERIALIZATION NO
    expect_line HOST_OBSERVATION_ID_DERIVATION NO
    expect_line HOST_SPAN_CONTEXT_EXTRACTION NO
    expect_line HOST_PAIR_SELECTION NO
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

# Produce an exact VNM-06 SPAN_OBS bundle from a native VNM-05 candidate.
# Host only invokes, exact-decodes native fields, and routes bytes/protocol fields.
NATIVE_BUNDLE_PATH=""
NATIVE_FORM=""
make_native_span_bundle() {
    NAME="$1"
    EXPECT_A="$2"
    EXPECT_B="$3"
    GLEFT1="$4"
    GRIGHT1="$5"
    GLEFT2="$6"
    GRIGHT2="$7"
    OBS_ID1="$8"
    OBS_ID2="$9"

    SBOX="$CASES/$NAME"
    "$P/bin/rm" -rf -- "$SBOX"

    BASE05="$SBOX/.sigma_exec/SIGMA_VNM_05_RECURRENT_ADJACENT_SPAN_CANDIDATE_INDUCTION_V1"
    IN05="$BASE05/input/sequences.memory"
    STATE05="$BASE05/state/adjacent_span_state.memory"
    "$P/bin/mkdir" -p "$BASE05/input" "$BASE05/state"
    : > "$STATE05"
    printf 'SEQ||G1||UNITS||%s~%s~%s~%s||SOURCE||GEN-SRC-1\n' \
        "$GLEFT1" "$EXPECT_A" "$EXPECT_B" "$GRIGHT1" > "$IN05"
    printf 'SEQ||G2||UNITS||%s~%s~%s~%s||SOURCE||GEN-SRC-2' \
        "$GLEFT2" "$EXPECT_A" "$EXPECT_B" "$GRIGHT2" >> "$IN05"

    CASE_NAME="$NAME"
    LOG05="$LOG/${NAME}_VNM05.log"
    run_component_vm VNM05 "$SBOX" "$BC05" "$LOG05"

    N_STATUS=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_STATUS" {sub(/^SPAN_CANDIDATE_STATUS /,""); printf "%s",$0; exit}' "$LOG05")
    N_A=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_UNIT_A" {sub(/^SPAN_CANDIDATE_UNIT_A /,""); printf "%s",$0; exit}' "$LOG05")
    N_B=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_UNIT_B" {sub(/^SPAN_CANDIDATE_UNIT_B /,""); printf "%s",$0; exit}' "$LOG05")
    N_SUPPORT=$("$P/bin/awk" '$1=="SPAN_CANDIDATE_SUPPORT" {sub(/^SPAN_CANDIDATE_SUPPORT /,""); printf "%s",$0; exit}' "$LOG05")

    [ "$N_STATUS" = ADJACENT_SPAN_CANDIDATE_INDUCED ] || fail_gate 62 VNM05_DID_NOT_INDUCE_CANDIDATE
    [ "$N_A" = "$EXPECT_A" ] || fail_gate 63 VNM05_CANDIDATE_A_MISMATCH
    [ "$N_B" = "$EXPECT_B" ] || fail_gate 64 VNM05_CANDIDATE_B_MISMATCH
    [ "$N_SUPPORT" = 2 ] || fail_gate 65 VNM05_CANDIDATE_SUPPORT_MISMATCH

    BASE06="$SBOX/.sigma_exec/SIGMA_VNM_06_SPAN_CONTEXT_OBSERVATION_DERIVATION_V1"
    CAND06="$BASE06/input/candidate.memory"
    SEQ06="$BASE06/input/sequences.memory"
    OUT06="$BASE06/output/span_observations.memory"
    "$P/bin/mkdir" -p "$BASE06/input" "$BASE06/output"
    printf 'CANDIDATE||STATUS||%s||UNIT_A||%s||UNIT_B||%s||SUPPORT||%s' \
        "$N_STATUS" "$N_A" "$N_B" "$N_SUPPORT" > "$CAND06"
    printf 'SEQ||%s||UNITS||%s~%s~%s~%s||SOURCE||OBS-SRC-%s\n' \
        "$OBS_ID1" "$CTX1_L" "$N_A" "$N_B" "$CTX1_R" "$OBS_ID1" > "$SEQ06"
    printf 'SEQ||%s||UNITS||%s~%s~%s~%s||SOURCE||OBS-SRC-%s' \
        "$OBS_ID2" "$CTX2_L" "$N_A" "$N_B" "$CTX2_R" "$OBS_ID2" >> "$SEQ06"
    : > "$OUT06"

    LOG06="$LOG/${NAME}_VNM06.log"
    run_component_vm VNM06 "$SBOX" "$BC06" "$LOG06"
    "$P/bin/grep" -F -x 'INTERIOR_CONTEXT_OBSERVATION_COUNT 2' "$LOG06" >/dev/null || fail_gate 66 VNM06_OBSERVATION_COUNT_MISMATCH
    "$P/bin/grep" -F -x 'DERIVATION_STATUS SPAN_CONTEXT_OBSERVATIONS_DERIVED' "$LOG06" >/dev/null || fail_gate 67 VNM06_DERIVATION_STATUS_MISMATCH
    [ -s "$OUT06" ] || fail_gate 68 VNM06_OUTPUT_EMPTY

    NATIVE_BUNDLE_PATH="$OUT06"
    NATIVE_FORM="$N_A~$N_B"
}

# Integration candidate/bundle 1.
make_native_span_bundle \
    NATIVE_PIPELINE_1 \
    "$SPAN1_A" "$SPAN1_B" \
    "$GEN1_L" "$GEN1_R" "$GEN2_L" "$GEN2_R" \
    X1 X2
BUNDLE1="$NATIVE_BUNDLE_PATH"
FORM1="$NATIVE_FORM"

# 01 — exact VNM-06 bundle 1 -> two VNM-02-compatible observations.
prepare07 CASE_001_NATIVE_VNM06_BUNDLE_1
"$P/bin/cp" -f -- "$BUNDLE1" "$INPUT07" || fail_gate 69 INPUT_COPY_FAILED
run07 CASE01
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 2
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
expect_line OUTPUT_MUTATED 1
expect_output_line "OBS||VNM07:X1~$SPAN1_A~$SPAN1_B||FORM||$FORM1||LEFT||$CTX1_L||RIGHT||$CTX1_R||SOURCE||OBS-SRC-X1"
expect_output_line "OBS||VNM07:X2~$SPAN1_A~$SPAN1_B||FORM||$FORM1||LEFT||$CTX2_L||RIGHT||$CTX2_R||SOURCE||OBS-SRC-X2"
pass_common
FORM_OBS_1="$ROOT/native_form_observations_1.memory"
"$P/bin/cp" -f -- "$OUTPUT07" "$FORM_OBS_1" || fail_gate 70 OUTPUT_COPY_FAILED
INTEGRATION_PASS_COUNT=$((INTEGRATION_PASS_COUNT + 1))

# Integration candidate/bundle 2.
make_native_span_bundle \
    NATIVE_PIPELINE_2 \
    "$SPAN2_A" "$SPAN2_B" \
    "$GEN3_L" "$GEN3_R" "$GEN4_L" "$GEN4_R" \
    Y1 Y2
BUNDLE2="$NATIVE_BUNDLE_PATH"
FORM2="$NATIVE_FORM"

# 02 — exact VNM-06 bundle 2 -> two VNM-02-compatible observations.
prepare07 CASE_002_NATIVE_VNM06_BUNDLE_2
"$P/bin/cp" -f -- "$BUNDLE2" "$INPUT07" || fail_gate 71 INPUT_COPY_FAILED
run07 CASE02
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 2
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
expect_line OUTPUT_MUTATED 1
expect_output_line "OBS||VNM07:Y1~$SPAN2_A~$SPAN2_B||FORM||$FORM2||LEFT||$CTX1_L||RIGHT||$CTX1_R||SOURCE||OBS-SRC-Y1"
expect_output_line "OBS||VNM07:Y2~$SPAN2_A~$SPAN2_B||FORM||$FORM2||LEFT||$CTX2_L||RIGHT||$CTX2_R||SOURCE||OBS-SRC-Y2"
pass_common
FORM_OBS_2="$ROOT/native_form_observations_2.memory"
"$P/bin/cp" -f -- "$OUTPUT07" "$FORM_OBS_2" || fail_gate 72 OUTPUT_COPY_FAILED
INTEGRATION_PASS_COUNT=$((INTEGRATION_PASS_COUNT + 1))

# Full downstream integration: exact VNM-07 bytes -> VNM-02 native pair induction.
CASE_NAME=INTEGRATION_VNM02_PAIR
SBOX02="$CASES/$CASE_NAME"
BASE02="$SBOX02/.sigma_exec/SIGMA_VNM_02_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1"
IN02="$BASE02/input/observations.memory"
STATE02="$BASE02/state/pair_induction_state.memory"
"$P/bin/rm" -rf -- "$SBOX02"
"$P/bin/mkdir" -p "$BASE02/input" "$BASE02/state"
: > "$STATE02"
{
    "$P/bin/cat" "$FORM_OBS_1"
    printf '\n'
    "$P/bin/cat" "$FORM_OBS_2"
} > "$IN02"
LOG02="$LOG/${CASE_NAME}_VNM02.log"
run_component_vm VNM02 "$SBOX02" "$BC02" "$LOG02"

"$P/bin/grep" -F -x 'PAIR_CANDIDATE_STATUS PAIR_CANDIDATE_INDUCED' "$LOG02" >/dev/null || fail_gate 73 VNM02_PAIR_NOT_INDUCED
"$P/bin/grep" -F -x 'PAIR_CANDIDATE_SUPPORT 2' "$LOG02" >/dev/null || fail_gate 74 VNM02_PAIR_SUPPORT_MISMATCH
PFA=$("$P/bin/awk" '$1=="PAIR_CANDIDATE_FORM_A" {sub(/^PAIR_CANDIDATE_FORM_A /,""); printf "%s",$0; exit}' "$LOG02")
PFB=$("$P/bin/awk" '$1=="PAIR_CANDIDATE_FORM_B" {sub(/^PAIR_CANDIDATE_FORM_B /,""); printf "%s",$0; exit}' "$LOG02")
PAIR_SET_MATCH=NO
if [ "$PFA" = "$FORM1" ] && [ "$PFB" = "$FORM2" ]; then PAIR_SET_MATCH=YES; fi
if [ "$PFA" = "$FORM2" ] && [ "$PFB" = "$FORM1" ]; then PAIR_SET_MATCH=YES; fi
[ "$PAIR_SET_MATCH" = YES ] || fail_gate 75 VNM02_PAIR_FORM_SET_MISMATCH
INTEGRATION_PASS_COUNT=$((INTEGRATION_PASS_COUNT + 1))
DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST=PASS

# 03 — one valid direct structural observation.
prepare07 CASE_003_SINGLE_VALID
add_span_obs07 S3 "$SPAN1_A" "$SPAN1_B" L3 R3 SRC3
run07 CASE03
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 1
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
expect_output_line "OBS||VNM07:S3~$SPAN1_A~$SPAN1_B||FORM||$FORM1||LEFT||L3||RIGHT||R3||SOURCE||SRC3"
pass_common
CASE03_OUTPUT_SHA=$(sha_of "$OUTPUT07")

# 04 — exact duplicate is idempotent.
prepare07 CASE_004_DUPLICATE_IDEMPOTENT
add_span_obs07 D1 "$SPAN1_A" "$SPAN1_B" DL DR DS
add_span_obs07 D1 "$SPAN1_A" "$SPAN1_B" DL DR DS
run07 CASE04
expect_line SPAN_OBSERVATION_LINE_COUNT 2
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 1
expect_line DUPLICATE_SPAN_OBSERVATION_COUNT 1
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 05 — same derived ID with different fingerprint is a refusal with no output mutation.
prepare07 CASE_005_OBSERVATION_ID_COLLISION
printf 'SENTINEL' > "$OUTPUT07"
add_span_obs07 C1 "$SPAN1_A" "$SPAN1_B" CL CR CS1
add_span_obs07 C1 "$SPAN1_A" "$SPAN1_B" CL CR2 CS2
BEFORE=$(sha_of "$OUTPUT07")
run07 CASE05
expect_line OBSERVATION_ID_COLLISION_COUNT 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line ADAPTER_STATUS REFUSED_OBSERVATION_ID_COLLISION
AFTER=$(sha_of "$OUTPUT07")
[ "$BEFORE" = "$AFTER" ] || fail_gate 76 REFUSAL_MUTATED_OUTPUT
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 06 — malformed record refusal.
prepare07 CASE_006_MALFORMED
printf 'SENTINEL' > "$OUTPUT07"
add_raw07 'BROKEN||SPAN'
BEFORE=$(sha_of "$OUTPUT07")
run07 CASE06
expect_line INVALID_SPAN_OBSERVATION_RECORD_COUNT 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line ADAPTER_STATUS REFUSED_SPAN_OBSERVATION_INVALID
AFTER=$(sha_of "$OUTPUT07")
[ "$BEFORE" = "$AFTER" ] || fail_gate 77 REFUSAL_MUTATED_OUTPUT
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 07 — empty unit field refusal.
prepare07 CASE_007_EMPTY_UNIT
add_span_obs07 E1 "" "$SPAN1_B" EL ER ES
run07 CASE07
expect_line INVALID_SPAN_OBSERVATION_RECORD_COUNT 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line ADAPTER_STATUS REFUSED_SPAN_OBSERVATION_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 08 — reserved '~' in sequence ID would make derived ID ambiguous and is refused.
prepare07 CASE_008_RESERVED_DELIMITER_SEQID
add_span_obs07 'BAD~ID' "$SPAN1_A" "$SPAN1_B" IL IR IS
run07 CASE08
expect_line RESERVED_DELIMITER_VIOLATION_COUNT 1
expect_line INVALID_SPAN_OBSERVATION_RECORD_COUNT 1
expect_line ADAPTER_STATUS REFUSED_SPAN_OBSERVATION_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 09 — reserved '~' in UNIT_A refused.
prepare07 CASE_009_RESERVED_DELIMITER_UNIT_A
add_span_obs07 RA "${SPAN1_A}~EXTRA" "$SPAN1_B" AL AR AS
run07 CASE09
expect_line RESERVED_DELIMITER_VIOLATION_COUNT 1
expect_line ADAPTER_STATUS REFUSED_SPAN_OBSERVATION_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 10 — reserved '~' in UNIT_B refused.
prepare07 CASE_010_RESERVED_DELIMITER_UNIT_B
add_span_obs07 RB "$SPAN1_A" "${SPAN1_B}~EXTRA" BL BR BS
run07 CASE10
expect_line RESERVED_DELIMITER_VIOLATION_COUNT 1
expect_line ADAPTER_STATUS REFUSED_SPAN_OBSERVATION_INVALID
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 11 — fifth unique span observation exceeds bounded adapter capacity.
prepare07 CASE_011_OBSERVATION_CAPACITY
add_span_obs07 K1 "$SPAN1_A" "$SPAN1_B" K1L K1R K1S
add_span_obs07 K2 "$SPAN1_A" "$SPAN1_B" K2L K2R K2S
add_span_obs07 K3 "$SPAN1_A" "$SPAN1_B" K3L K3R K3S
add_span_obs07 K4 "$SPAN1_A" "$SPAN1_B" K4L K4R K4S
add_span_obs07 K5 "$SPAN1_A" "$SPAN1_B" K5L K5R K5S
run07 CASE11
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 5
expect_line OBSERVATION_CAPACITY_EXCEEDED 1
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line ADAPTER_STATUS REFUSED_OBSERVATION_CAPACITY
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 12 — >8 raw lines refuses before record scan.
prepare07 CASE_012_INPUT_BOUND
for i in 1 2 3 4 5 6 7 8 9; do
    add_span_obs07 "B$i" "$SPAN1_A" "$SPAN1_B" "L$i" "R$i" "S$i"
done
run07 CASE12
expect_line INPUT_BOUND_EXCEEDED 1
expect_line SPAN_OBSERVATION_LINE_COUNT 0
expect_line OUTPUT_WRITE_ALLOWED 0
expect_line ADAPTER_STATUS REFUSED_INPUT_BOUND
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 13 — empty batch is a valid no-op structural transform.
prepare07 CASE_013_EMPTY_BATCH
run07 CASE13
expect_line SPAN_OBSERVATION_LINE_COUNT 0
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 0
expect_line OUTPUT_WRITE_ALLOWED 1
expect_line OUTPUT_WRITE_READBACK_MATCH 1
expect_line OUTPUT_MUTATED 0
expect_line ADAPTER_STATUS NO_SPAN_OBSERVATIONS
pass_common
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))

# 14 — materially different high-entropy ordered span changes serialized FORM.
prepare07 CASE_014_COUNTERFACTUAL
add_span_obs07 CF1 "$CF_A" "$CF_B" CFL CFR CFS
run07 CASE14
CF_FORM="$CF_A~$CF_B"
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 1
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
expect_output_line "OBS||VNM07:CF1~$CF_A~$CF_B||FORM||$CF_FORM||LEFT||CFL||RIGHT||CFR||SOURCE||CFS"
pass_common
REPLAY_A_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_A_OUTPUT_SHA=$(sha_of "$OUTPUT07")
[ "$CASE03_OUTPUT_SHA" != "$REPLAY_A_OUTPUT_SHA" ] || fail_gate 78 OUTPUT_DID_NOT_CHANGE_WITH_INPUT
COUNTERFACTUAL_PASS_COUNT=$((COUNTERFACTUAL_PASS_COUNT + 1))

# 15 — ordered serialization preserves A->B versus B->A distinction.
prepare07 CASE_015_ORDER_REVERSAL
add_span_obs07 O15 "$SPAN1_B" "$SPAN1_A" OL OR OS
run07 CASE15
REVERSED_FORM="$SPAN1_B~$SPAN1_A"
expect_output_line "OBS||VNM07:O15~$SPAN1_B~$SPAN1_A||FORM||$REVERSED_FORM||LEFT||OL||RIGHT||OR||SOURCE||OS"
pass_common
[ "$REVERSED_FORM" != "$FORM1" ] || fail_gate 79 ORDERED_SERIALIZATION_COLLAPSED_DIRECTION
ORDERED_SPAN_SERIALIZATION_TEST=PASS

# 16 — identical pure replay of case 14.
prepare07 CASE_016_REPLAY_B
add_span_obs07 CF1 "$CF_A" "$CF_B" CFL CFR CFS
run07 CASE16
expect_line UNIQUE_SPAN_OBSERVATION_COUNT 1
expect_line ADAPTER_STATUS FORM_OBSERVATIONS_DERIVED
expect_output_line "OBS||VNM07:CF1~$CF_A~$CF_B||FORM||$CF_FORM||LEFT||CFL||RIGHT||CFR||SOURCE||CFS"
pass_common
REPLAY_B_LOG_SHA=$(sha_of "$LAST_LOG")
REPLAY_B_OUTPUT_SHA=$(sha_of "$OUTPUT07")

REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=NO
if [ "$REPLAY_A_LOG_SHA" = "$REPLAY_B_LOG_SHA" ] \
    && [ "$REPLAY_A_OUTPUT_SHA" = "$REPLAY_B_OUTPUT_SHA" ]; then
    REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
fi
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 80 REPLAY_MISMATCH

SOURCE02_AFTER=$(sha_of "$SRC02")
SOURCE05_AFTER=$(sha_of "$SRC05")
SOURCE06_AFTER=$(sha_of "$SRC06")
SOURCE07_AFTER=$(sha_of "$SRC07")
BC02_AFTER=$(sha_of "$BC02")
BC05_AFTER=$(sha_of "$BC05")
BC06_AFTER=$(sha_of "$BC06")
BC07_AFTER=$(sha_of "$BC07")

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
if [ "$SOURCE02_BEFORE" = "$SOURCE02_AFTER" ] \
    && [ "$SOURCE05_BEFORE" = "$SOURCE05_AFTER" ] \
    && [ "$SOURCE06_BEFORE" = "$SOURCE06_AFTER" ] \
    && [ "$SOURCE07_BEFORE" = "$SOURCE07_AFTER" ]; then
    SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi
if [ "$BC02_BEFORE" = "$BC02_AFTER" ] \
    && [ "$BC05_BEFORE" = "$BC05_AFTER" ] \
    && [ "$BC06_BEFORE" = "$BC06_AFTER" ] \
    && [ "$BC07_BEFORE" = "$BC07_AFTER" ]; then
    BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi

printf '\n=== VNM-07 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER\n'
printf 'CAPABILITY_NAME=Native ordered-span structural serialization into VNM-02-compatible form observations\n'
printf 'TEACHING_GOAL=SIGMA natively serializes VNM-06 span observations into collision-audited ordered span FORM observations that can enter admitted VNM-02 pair induction without host FORM or observation-ID generation\n'
printf 'DEPENDENCIES=VNM06_VNM05_VNM02_ADMITTED_EXACT_SOURCES_AND_BYTECODES_PLUS_LOCKED_SIGMAC_VM_AND_EXISTING_MECHANICAL_STRING_FILE_MAP_LIST_ABI\n'
printf 'SOURCE_SHA256=%s\n' "$SOURCE07_AFTER"
printf 'BYTECODE_SHA256=%s\n' "$BC07_AFTER"
printf 'VNM06_SOURCE_SHA256=%s\n' "$SOURCE06_AFTER"
printf 'VNM06_BYTECODE_SHA256=%s\n' "$BC06_AFTER"
printf 'VNM05_SOURCE_SHA256=%s\n' "$SOURCE05_AFTER"
printf 'VNM05_BYTECODE_SHA256=%s\n' "$BC05_AFTER"
printf 'VNM02_SOURCE_SHA256=%s\n' "$SOURCE02_AFTER"
printf 'VNM02_BYTECODE_SHA256=%s\n' "$BC02_AFTER"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'VNM05_VM_INVOCATIONS=%s\n' "$VNM05_VM_INVOCATIONS"
printf 'VNM06_VM_INVOCATIONS=%s\n' "$VNM06_VM_INVOCATIONS"
printf 'VNM07_VM_INVOCATIONS=%s\n' "$VNM07_VM_INVOCATIONS"
printf 'VNM02_VM_INVOCATIONS=%s\n' "$VNM02_VM_INVOCATIONS"
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
printf 'PERSISTENT_STATE=NO_FOR_VNM07_PURE_ADAPTER;YES_IN_DOWNSTREAM_VNM02_INTEGRATION\n'
printf 'PERSISTENT_STATE_TEST=PASS_IN_DOWNSTREAM_VNM02_INTEGRATION\n'
printf 'RESTART_REPLAY_TEST=PASS_PURE_CAPABILITY\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=%s\n' "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION"
printf 'ORDERED_SPAN_SERIALIZATION_TEST=%s\n' "$ORDERED_SPAN_SERIALIZATION_TEST"
printf 'DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST=%s\n' "$DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST"
printf 'VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'VNM06_SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE\n'
printf 'VNM07_SPAN_FORM_SERIALIZATION_OWNER=SIGMA_NATIVE\n'
printf 'VNM07_OBSERVATION_ID_DERIVATION_OWNER=SIGMA_NATIVE\n'
printf 'VNM02_PAIR_INDUCTION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_FORM_SERIALIZATION=NO\n'
printf 'HOST_OBSERVATION_ID_DERIVATION=NO\n'
printf 'HOST_PAIR_GENERATION=NO\n'
printf 'HOST_PAIR_SELECTION=NO\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$LEAK_COUNT"
printf 'STEP_LIMIT_STATUS=PASS_IN_21_INVOCATION_BOUNDED_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN\n'
printf 'WORD_BOUNDARY_DETECTION=NOT_PROVEN\n'
printf 'PHRASE_BOUNDARY_DETECTION=NOT_PROVEN\n'
printf 'PHRASE_SEMANTICS=NOT_PROVEN\n'
printf 'WORD_MEANING=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded VNM-06 SPAN_OBS records over delimiter-defined UTF-8 units; native ordered UNIT_A~UNIT_B structural FORM serialization and derived observation identity in a reserved-tilde ID/unit scope; exact VNM-02-compatible OBS output; duplicate suppression/collision/malformed/reserved-delimiter/capacity/input-bound refusal; native VNM-05->VNM-06->VNM-07->VNM-02 integration proof; no natural-language boundary or phrase-semantics claim\n'

[ "$TOTAL_VM_INVOCATIONS" -eq 21 ] || fail_gate 90 TOTAL_VM_INVOCATIONS_MISMATCH
[ "$VNM05_VM_INVOCATIONS" -eq 2 ] || fail_gate 91 VNM05_VM_INVOCATIONS_MISMATCH
[ "$VNM06_VM_INVOCATIONS" -eq 2 ] || fail_gate 92 VNM06_VM_INVOCATIONS_MISMATCH
[ "$VNM07_VM_INVOCATIONS" -eq 16 ] || fail_gate 93 VNM07_VM_INVOCATIONS_MISMATCH
[ "$VNM02_VM_INVOCATIONS" -eq 1 ] || fail_gate 94 VNM02_VM_INVOCATIONS_MISMATCH
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 16 ] || fail_gate 95 ALIGNMENT_PASS_COUNT_MISMATCH
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || fail_gate 96 ALIGNMENT_FAIL_COUNT_NONZERO
[ "$VM_NONZERO_COUNT" -eq 0 ] || fail_gate 97 VM_NONZERO_COUNT_NONZERO
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || fail_gate 98 STEP_LIMIT_HIT_COUNT_NONZERO
[ "$NEGATIVE_PASS_COUNT" -eq 10 ] || fail_gate 99 NEGATIVE_PASS_COUNT_MISMATCH
[ "$INTEGRATION_PASS_COUNT" -eq 3 ] || fail_gate 100 INTEGRATION_PASS_COUNT_MISMATCH
[ "$COUNTERFACTUAL_PASS_COUNT" -eq 1 ] || fail_gate 101 COUNTERFACTUAL_PASS_COUNT_MISMATCH
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 102 REPLAY_DECISION_NOT_YES
[ "$ORDERED_SPAN_SERIALIZATION_TEST" = PASS ] || fail_gate 103 ORDERED_SERIALIZATION_TEST_FAIL
[ "$DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST" = PASS ] || fail_gate 104 DOWNSTREAM_PAIR_INDUCTION_TEST_FAIL
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 105 SOURCE_CHANGED
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 106 BYTECODE_CHANGED
[ "$LEAK_COUNT" -eq 0 ] || fail_gate 107 DYNAMIC_TOKEN_LEAK_NONZERO

printf 'VNM_07_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'