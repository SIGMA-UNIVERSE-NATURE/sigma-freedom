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

EXPECTED_VNM04_SOURCE=9b2795403157617b4b1ae15baeaa60adce3deb59f2fdd7174a8b3182f1d3a7d0
EXPECTED_VNM03_SOURCE=c0d54fe4c36f59ac1b4a1cd431e2078333ee5d28b8fa2f2fb2d5f1813e6beb34
EXPECTED_VNM02_SOURCE=f2c5f266492fd990887a356bd353d545f480f51ad6bb1ba63ca5a727320bbac3
EXPECTED_VNM01_SOURCE=cd399793ebde7e5dfa4a10cf263bb97fd45d1379ce8dac02520d5277cf2ca788

EXPECTED_VNM03_BYTECODE=3cf35674bfaad6f76ba09f95eadca3e35dd0ce631b856444c57011bd823009db
EXPECTED_VNM02_BYTECODE=bf6f3cac8aade9433f43c13d462a73465eceef0b1e5f5411336cad2e338b0aec
EXPECTED_VNM01_BYTECODE=df323de291828d11cc7e46655f2ff5fbc326297200b1782f4c0c441389a27586

SRC4="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1.sigma"
SRC3="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigma"
SRC2="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigma"
SRC1="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma"

ROOT="$HOME_SIGMA/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"

BC4="$ROOT/SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1.sigmab"
BC3="$ROOT/SIGMA_VNM_03_NATIVE_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1.sigmab"
BC2="$ROOT/SIGMA_VNM_02_NATIVE_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1.sigmab"
BC1="$ROOT/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=VNM_04_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

sha_of() {
    "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'
}

actual_sigmac=$(sha_of "$SIGMAC")
actual_vm=$(sha_of "$VM")
actual_src4=$(sha_of "$SRC4")
actual_src3=$(sha_of "$SRC3")
actual_src2=$(sha_of "$SRC2")
actual_src1=$(sha_of "$SRC1")

printf 'SIGMA_PHASE=VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_PREFLIGHT\n'
printf 'ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_CANDIDATE_GENERATION=NO\n'
printf 'HOST_CANDIDATE_SELECTION=NO\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_EVIDENCE_GENERATION=NO\n'
printf 'HOST_WEIGHT_UPDATE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'ACTIVE_PYTHON_COGNITION=NO\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE_TEST=YES_VIA_DOWNSTREAM_VNM01_AND_VNM02\n'
printf 'RESTART_REPLAY_TEST=YES\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'VNM04_SOURCE_SHA256=%s\n' "$actual_src4"
printf 'VNM03_SOURCE_SHA256=%s\n' "$actual_src3"
printf 'VNM02_SOURCE_SHA256=%s\n' "$actual_src2"
printf 'VNM01_SOURCE_SHA256=%s\n' "$actual_src1"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_src4" = "$EXPECTED_VNM04_SOURCE" ] || { printf 'HOLD=VNM04_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$actual_src3" = "$EXPECTED_VNM03_SOURCE" ] || { printf 'HOLD=VNM03_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }
[ "$actual_src2" = "$EXPECTED_VNM02_SOURCE" ] || { printf 'HOLD=VNM02_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }
[ "$actual_src1" = "$EXPECTED_VNM01_SOURCE" ] || { printf 'HOLD=VNM01_SOURCE_IDENTITY_MISMATCH\n'; exit 26; }

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
    if "$P/bin/grep" -F "$forbidden" "$SRC4" >/dev/null 2>&1; then
        printf 'HOLD=FORBIDDEN_HOST_SEMANTIC_OPERATION_TOKEN\n'
        printf 'TOKEN=%s\n' "$forbidden"
        exit 27
    fi
done

compile_one() {
    SRC="$1"
    BC="$2"
    LABEL="$3"

    "$P/bin/rm" -f -- "$BC.partial" "$BC"
    "$SIGMAC" "$SRC" "$BC.partial"
    RC=$?
    printf '%s_SIGMAC_RC=%s\n' "$LABEL" "$RC"
    [ "$RC" -eq 0 ] || exit 30
    [ -s "$BC.partial" ] || exit 31
    "$P/bin/mv" -f -- "$BC.partial" "$BC" || exit 32
    "$P/bin/chmod" 0400 "$BC" || exit 33
    printf '%s_BYTECODE_SHA256=%s\n' "$LABEL" "$(sha_of "$BC")"
}

compile_one "$SRC3" "$BC3" VNM03
compile_one "$SRC2" "$BC2" VNM02
compile_one "$SRC1" "$BC1" VNM01
compile_one "$SRC4" "$BC4" VNM04

actual_bc3=$(sha_of "$BC3")
actual_bc2=$(sha_of "$BC2")
actual_bc1=$(sha_of "$BC1")
actual_bc4=$(sha_of "$BC4")

[ "$actual_bc3" = "$EXPECTED_VNM03_BYTECODE" ] || { printf 'HOLD=VNM03_ADMITTED_BYTECODE_REPRODUCIBILITY_MISMATCH\n'; exit 34; }
[ "$actual_bc2" = "$EXPECTED_VNM02_BYTECODE" ] || { printf 'HOLD=VNM02_ADMITTED_BYTECODE_REPRODUCIBILITY_MISMATCH\n'; exit 35; }
[ "$actual_bc1" = "$EXPECTED_VNM01_BYTECODE" ] || { printf 'HOLD=VNM01_ADMITTED_BYTECODE_REPRODUCIBILITY_MISMATCH\n'; exit 36; }

printf 'VNM04_BYTECODE_SHA256=%s\n' "$actual_bc4"

SOURCE4_BEFORE="$actual_src4"
SOURCE3_BEFORE="$actual_src3"
SOURCE2_BEFORE="$actual_src2"
SOURCE1_BEFORE="$actual_src1"
BC4_BEFORE="$actual_bc4"
BC3_BEFORE="$actual_bc3"
BC2_BEFORE="$actual_bc2"
BC1_BEFORE="$actual_bc1"

# Dynamic values are created only after all source/bytecode identities are frozen.
DYN_TAG="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"
DYN_TAG_2="${RANDOM}${RANDOM}${RANDOM}${RANDOM}"

A="điện-${DYN_TAG}"
B="dien-${DYN_TAG}"
C="động-${DYN_TAG}"
D="mạch-${DYN_TAG}"
E="nguồn-${DYN_TAG}"
F="dòng-${DYN_TAG}"

A2="học-${DYN_TAG_2}"
B2="hoc-${DYN_TAG_2}"
C2="đọc-${DYN_TAG_2}"

L1="L-${DYN_TAG}-1"
R1="R-${DYN_TAG}-1"
L2="L-${DYN_TAG}-2"
R2="R-${DYN_TAG}-2"
L3="L-${DYN_TAG}-3"
R3="R-${DYN_TAG}-3"
L4="L-${DYN_TAG}-4"
R4="R-${DYN_TAG}-4"

Q1="Q-${DYN_TAG_2}-1"
Z1="Z-${DYN_TAG_2}-1"
Q2="Q-${DYN_TAG_2}-2"
Z2="Z-${DYN_TAG_2}-2"

printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'DYNAMIC_TAG_SHA256=%s\n' "$(printf '%s' "$DYN_TAG" | "$P/bin/sha256sum" | "$P/bin/awk" '{print $1}')"

if "$P/bin/grep" -a -F "$DYN_TAG" "$SRC4" "$SRC3" "$SRC2" "$SRC1" "$BC4" "$BC3" "$BC2" "$BC1" >/dev/null 2>&1; then
    printf 'HOLD=DYNAMIC_TOKEN_LEAK_IN_SOURCE_OR_BYTECODE\n'
    exit 37
fi

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
VNM03_VM_INVOCATIONS=0
VNM02_VM_INVOCATIONS=0
VNM04_VM_INVOCATIONS=0
VNM01_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=0
PERSISTENCE_PASS_COUNT=0
FULL_CHAIN_PASS_COUNT=0

CASE_NAME=""
SANDBOX=""
B3=""
B2=""
B4=""
B1=""
V3_IN=""
V3_OUT=""
V2_IN=""
V2_STATE=""
V4_CANDIDATE=""
V4_OBS=""
V4_BUNDLE=""
V1_HYP=""
V1_EVID=""
V1_STATE=""
ACCUM=""
LAST_LOG=""

fail_gate() {
    CODE="$1"
    REASON="$2"
    printf 'VNM_04_PREFLIGHT=FAIL\n'
    printf 'FAILURE_CASE=%s\n' "$CASE_NAME"
    printf 'FAILURE=%s\n' "$REASON"
    exit "$CODE"
}

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"

    B3="$SANDBOX/.sigma_exec/SIGMA_VNM_03_LOCAL_CONTEXT_OBSERVATION_DERIVATION_V1"
    B2="$SANDBOX/.sigma_exec/SIGMA_VNM_02_SURFACE_FORM_PAIR_CANDIDATE_INDUCTION_V1"
    B4="$SANDBOX/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"
    B1="$SANDBOX/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"

    V3_IN="$B3/input/sequences.memory"
    V3_OUT="$B3/output/observations.memory"

    V2_IN="$B2/input/observations.memory"
    V2_STATE="$B2/state/pair_induction_state.memory"

    V4_CANDIDATE="$B4/input/candidate.memory"
    V4_OBS="$B4/input/observations.memory"
    V4_BUNDLE="$B4/output/vnm01_input_bundle.memory"

    V1_HYP="$B1/input/hypothesis.memory"
    V1_EVID="$B1/input/evidence.memory"
    V1_STATE="$B1/state/surface_form_weight_state.memory"

    ACCUM="$SANDBOX/accumulated_observations.memory"

    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p \
        "$B3/input" "$B3/output" \
        "$B2/input" "$B2/state" \
        "$B4/input" "$B4/output" \
        "$B1/input" "$B1/state"

    : > "$V3_IN"
    : > "$V2_IN"
    : > "$V2_STATE"
    : > "$V4_CANDIDATE"
    : > "$V4_OBS"
    : > "$V1_HYP"
    : > "$V1_EVID"
    : > "$V1_STATE"
    : > "$ACCUM"
}

clear_v3() {
    : > "$V3_IN"
}

add_seq() {
    printf 'SEQ||%s||UNITS||%s||SOURCE||%s\n' "$1" "$2" "$3" >> "$V3_IN"
}

run_stage() {
    STAGE="$1"
    LABEL="$2"
    BC="$3"
    LAST_LOG="$LOG/${CASE_NAME}_${LABEL}.log"

    TOTAL_VM_INVOCATIONS=$((TOTAL_VM_INVOCATIONS + 1))
    case "$STAGE" in
        VNM03) VNM03_VM_INVOCATIONS=$((VNM03_VM_INVOCATIONS + 1)) ;;
        VNM02) VNM02_VM_INVOCATIONS=$((VNM02_VM_INVOCATIONS + 1)) ;;
        VNM04) VNM04_VM_INVOCATIONS=$((VNM04_VM_INVOCATIONS + 1)) ;;
        VNM01) VNM01_VM_INVOCATIONS=$((VNM01_VM_INVOCATIONS + 1)) ;;
    esac

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
        fail_gate 50 "${STAGE}_VM_NONZERO"
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        fail_gate 51 "${STAGE}_STEP_LIMIT_HIT"
    fi
}

expect_line_file() {
    FILE="$1"
    KEY="$2"
    VALUE="$3"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$FILE" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'EXPECTED=%s %s\n' "$KEY" "$VALUE"
        fail_gate 60 MISSING_EXPECTED_OUTPUT
    fi
}

expect_last() {
    expect_line_file "$LAST_LOG" "$1" "$2"
}

mark_case_pass() {
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
    printf 'CASE_%s_POST_VM_ALIGNMENT=YES\n' "$CASE_NAME"
}

append_v3_output() {
    [ -s "$V3_OUT" ] || fail_gate 61 VNM03_OUTPUT_MISSING
    if [ -s "$ACCUM" ]; then
        printf '\n' >> "$ACCUM"
    fi
    "$P/bin/cat" "$V3_OUT" >> "$ACCUM"
}

route_v3_to_v2() {
    [ -f "$V3_OUT" ] || fail_gate 62 VNM03_OUTPUT_NOT_FOUND_FOR_VNM02
    "$P/bin/cp" -f -- "$V3_OUT" "$V2_IN" || fail_gate 63 VNM03_TO_VNM02_COPY_FAILED
}

decode_v2_candidate() {
    V2LOG="$1"

    for KEY in \
        PAIR_CANDIDATE_STATUS \
        PAIR_CANDIDATE_FORM_A \
        PAIR_CANDIDATE_FORM_B \
        PAIR_CANDIDATE_SUPPORT
    do
        COUNT=$("$P/bin/grep" -c "^${KEY} " "$V2LOG")
        [ "$COUNT" -eq 1 ] || fail_gate 64 VNM02_PROTOCOL_FIELD_COUNT_INVALID
    done

    STATUS=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_STATUS //p' "$V2LOG")
    FORM_A=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_FORM_A //p' "$V2LOG")
    FORM_B=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_FORM_B //p' "$V2LOG")
    SUPPORT=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_SUPPORT //p' "$V2LOG")

    printf 'CANDIDATE||%s||FORM_A||%s||FORM_B||%s||SUPPORT||%s' \
        "$STATUS" "$FORM_A" "$FORM_B" "$SUPPORT" > "$V4_CANDIDATE"
}

expect_v2_pair_unordered() {
    V2LOG="$1"
    X="$2"
    Y="$3"

    FA=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_FORM_A //p' "$V2LOG")
    FB=$("$P/bin/sed" -n 's/^PAIR_CANDIDATE_FORM_B //p' "$V2LOG")

    OK=NO
    if [ "$FA" = "$X" ] && [ "$FB" = "$Y" ]; then OK=YES; fi
    if [ "$FA" = "$Y" ] && [ "$FB" = "$X" ]; then OK=YES; fi

    [ "$OK" = YES ] || fail_gate 65 VNM02_PAIR_NOT_EXPECTED_UNORDERED_PAIR
}

route_accum_to_v4() {
    "$P/bin/cp" -f -- "$ACCUM" "$V4_OBS" || fail_gate 66 OBSERVATION_ROUTE_TO_VNM04_FAILED
}

route_v4_bundle_to_v1() {
    [ -s "$V4_BUNDLE" ] || fail_gate 67 VNM04_BUNDLE_MISSING
    "$P/bin/sed" -n '1p' "$V4_BUNDLE" > "$V1_HYP"
    "$P/bin/tail" -n +2 "$V4_BUNDLE" > "$V1_EVID"
    [ -s "$V1_HYP" ] || fail_gate 68 VNM04_HYPOTHESIS_ROUTE_EMPTY
    [ -s "$V1_EVID" ] || fail_gate 69 VNM04_EVIDENCE_ROUTE_EMPTY
}

set_bundle_sentinel() {
    printf '%s' "$1" > "$V4_BUNDLE"
}

bundle_sha() {
    sha_of "$V4_BUNDLE"
}

build_support2_native() {
    X="$1"
    Y="$2"
    LEFT_A="$3"
    RIGHT_A="$4"
    LEFT_B="$5"
    RIGHT_B="$6"
    PREFIX="$7"
    SRC_PREFIX="$8"

    clear_v3
    add_seq "${PREFIX}1" "${LEFT_A}~${X}~${RIGHT_A}" "${SRC_PREFIX}1"
    add_seq "${PREFIX}2" "${LEFT_A}~${Y}~${RIGHT_A}" "${SRC_PREFIX}2"
    add_seq "${PREFIX}3" "${LEFT_B}~${X}~${RIGHT_B}" "${SRC_PREFIX}3"
    add_seq "${PREFIX}4" "${LEFT_B}~${Y}~${RIGHT_B}" "${SRC_PREFIX}4"

    run_stage VNM03 "${PREFIX}_V3" "$BC3"
    expect_last RESULT_STATUS LOCAL_CONTEXT_OBSERVATIONS_DERIVED
    expect_last DERIVED_OBSERVATION_COUNT 4
    append_v3_output

    route_v3_to_v2
    run_stage VNM02 "${PREFIX}_V2" "$BC2"
    V2LOG="$LAST_LOG"
    expect_line_file "$V2LOG" PAIR_CANDIDATE_STATUS PAIR_CANDIDATE_INDUCED
    expect_line_file "$V2LOG" PAIR_CANDIDATE_SUPPORT 2
    expect_v2_pair_unordered "$V2LOG" "$X" "$Y"
    decode_v2_candidate "$V2LOG"
}

run_v4_ready() {
    LABEL="$1"
    route_accum_to_v4
    run_stage VNM04 "$LABEL" "$BC4"
    expect_last BRIDGE_STATUS BRIDGE_READY
    expect_last OUTPUT_ALLOWED 1
    expect_last BUNDLE_WRITE_READBACK_MATCH 1
    expect_last OUTPUT_MUTATED 1
}

run_v1_from_bundle() {
    LABEL="$1"
    route_v4_bundle_to_v1
    run_stage VNM01 "$LABEL" "$BC1"
}

# CASE 01 — complete VNM03 -> VNM02 -> VNM04 -> VNM01 support chain
prepare_case CASE_001_FULL_CHAIN_SUPPORT2
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" S1 "SRC-${DYN_TAG}-"
run_v4_ready CASE01_V4
expect_last SUPPORT_PAIR_COUNT 2
expect_last COMPETING_RAW_PAIR_COUNT 0
expect_last ELIGIBLE_EVIDENCE_COUNT 2
run_v1_from_bundle CASE01_V1
expect_last NEW_SUPPORT_COUNT 2
expect_last NEW_COMPETING_COUNT 0
expect_last WEIGHT_BEFORE 0
expect_last WEIGHT_AFTER 2
expect_last HOST_LEARNING NO
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
mark_case_pass

# CASE 02 — materially different unseen UTF-8 forms
prepare_case CASE_002_DIFFERENT_DYNAMIC_PAIR
build_support2_native "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2" T1 "SRC2-${DYN_TAG_2}-"
run_v4_ready CASE02_V4
expect_last SUPPORT_PAIR_COUNT 2
run_v1_from_bundle CASE02_V1
expect_last WEIGHT_AFTER 2
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
mark_case_pass

# CASE 03 — insufficient VNM02 recurrence must not become a bridge result
prepare_case CASE_003_INSUFFICIENT_CANDIDATE
clear_v3
add_seq I1 "$L1~$A~$R1" "I-SRC-1"
add_seq I2 "$L1~$B~$R1" "I-SRC-2"
run_stage VNM03 CASE03_V3 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 2
append_v3_output
route_v3_to_v2
run_stage VNM02 CASE03_V2 "$BC2"
V2LOG="$LAST_LOG"
expect_line_file "$V2LOG" PAIR_CANDIDATE_STATUS INSUFFICIENT_RECURRENT_EVIDENCE
decode_v2_candidate "$V2LOG"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE03-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE03_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_CANDIDATE_INVALID
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 70 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 04 — native VNM02 ambiguity must remain withheld from the bridge
prepare_case CASE_004_AMBIGUOUS_NATIVE_CANDIDATE
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" A1 "AMB-A-"
clear_v3
add_seq A21 "$L3~$D~$R3" "AMB-D-1"
add_seq A22 "$L3~$E~$R3" "AMB-E-1"
add_seq A23 "$L4~$D~$R4" "AMB-D-2"
add_seq A24 "$L4~$E~$R4" "AMB-E-2"
run_stage VNM03 CASE04_V3_SECOND "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 4
append_v3_output
route_v3_to_v2
run_stage VNM02 CASE04_V2_SECOND "$BC2"
V2LOG="$LAST_LOG"
expect_line_file "$V2LOG" PAIR_CANDIDATE_STATUS AMBIGUOUS_PAIR_CANDIDATE
decode_v2_candidate "$V2LOG"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE04-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE04_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_CANDIDATE_INVALID
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 71 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 05 — exact duplicate observation is idempotently suppressed
prepare_case CASE_005_DUPLICATE_OBSERVATION
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" D1 "DUP-"
FIRST_LINE=$("$P/bin/sed" -n '1p' "$ACCUM")
printf '\n%s' "$FIRST_LINE" >> "$ACCUM"
run_v4_ready CASE05_V4
expect_last DUPLICATE_OBSERVATION_COUNT 1
expect_last UNIQUE_OBSERVATION_COUNT 4
expect_last SUPPORT_PAIR_COUNT 2
mark_case_pass

# CASE 06 — observation-ID collision fault injection refuses atomically
prepare_case CASE_006_OBSERVATION_ID_COLLISION
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" C1 "COL-"
printf '\nOBS||C11:1||FORM||%s||LEFT||%s||RIGHT||%s||SOURCE||COLLISION-FAULT' "$C" "$L1" "$R1" >> "$ACCUM"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE06-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE06_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_OBSERVATION_ID_COLLISION
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 72 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 07 — malformed observation fault injection refuses atomically
prepare_case CASE_007_MALFORMED_OBSERVATION
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" M1 "MAL-"
printf '\nBROKEN||OBSERVATION' >> "$ACCUM"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE07-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE07_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_OBSERVATION_RECORD_INVALID
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 73 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 08 — mechanically corrupted native support field is detected
prepare_case CASE_008_CANDIDATE_SUPPORT_FAULT
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" F1 "SUPFAULT-"
"$P/bin/sed" 's/||SUPPORT||2$/||SUPPORT||3/' "$V4_CANDIDATE" > "$V4_CANDIDATE.fault"
"$P/bin/mv" -f -- "$V4_CANDIDATE.fault" "$V4_CANDIDATE"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE08-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE08_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_CANDIDATE_SUPPORT_MISMATCH
expect_last SUPPORT_MATCH 0
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 74 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 09 — malformed candidate protocol refuses
prepare_case CASE_009_MALFORMED_CANDIDATE
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" G1 "CANDMAL-"
printf 'BROKEN||CANDIDATE' > "$V4_CANDIDATE"
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE09-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE09_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_CANDIDATE_INVALID
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 75 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 10 — >8 observations, all extra observations still derived natively by VNM03
prepare_case CASE_010_OBSERVATION_CAPACITY
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" H1 "CAP-BASE-"
clear_v3
add_seq H21 "$L3~$C~$R3" "CAP-X1"
add_seq H22 "$L3~$D~$R3" "CAP-X2"
add_seq H23 "$L4~$E~$R4" "CAP-X3"
add_seq H24 "$L4~$F~$R4" "CAP-X4"
run_stage VNM03 CASE10_V3_EXTRA4 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 4
append_v3_output
clear_v3
add_seq H31 "$Q1~$C2~$Z1" "CAP-X5"
run_stage VNM03 CASE10_V3_EXTRA1 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 1
append_v3_output
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE10-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE10_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_OBSERVATION_CAPACITY
expect_last OBSERVATION_CAPACITY_EXCEEDED 1
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 76 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 11 — >16 raw observation lines; VNM04 must fail closed before scan
prepare_case CASE_011_RAW_INPUT_BOUND
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" J1 "BOUND-BASE-"
clear_v3
add_seq J21 "X1~X2~X3~X4" "BND-1"
add_seq J22 "X5~X6~X7~X8" "BND-2"
add_seq J23 "X9~X10~X11~X12" "BND-3"
add_seq J24 "X13~X14~X15~X16" "BND-4"
run_stage VNM03 CASE11_V3_EXTRA8 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 8
append_v3_output
clear_v3
add_seq J31 "Y1~Y2~Y3~Y4" "BND-5"
add_seq J32 "Y5~Y6~Y7~Y8" "BND-6"
add_seq J33 "Y9~Y10~Y11" "BND-7"
run_stage VNM03 CASE11_V3_EXTRA5 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 5
append_v3_output
RAW_COUNT=$("$P/bin/awk" 'END {print NR}' "$ACCUM")
[ "$RAW_COUNT" -eq 17 ] || fail_gate 77 RAW_BOUND_FIXTURE_NOT_17_LINES
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE11-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE11_V4 "$BC4"
expect_last BRIDGE_STATUS REFUSED_INPUT_BOUND
expect_last INPUT_BOUND_EXCEEDED 1
expect_last UNIQUE_OBSERVATION_COUNT 0
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 78 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 12 — native-derived observations can exceed VNM01 evidence capacity; bridge refuses
prepare_case CASE_012_EVIDENCE_CAPACITY
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" K1 "EVCAP-BASE-"
clear_v3
add_seq K21 "$L1~$C~$R1" "EVCAP-C"
add_seq K22 "$L1~$D~$R1" "EVCAP-D"
add_seq K23 "$L1~$E~$R1" "EVCAP-E"
add_seq K24 "$L1~$F~$R1" "EVCAP-F"
run_stage VNM03 CASE12_V3_EXTRA4 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 4
append_v3_output
route_accum_to_v4
set_bundle_sentinel "SENTINEL-CASE12-$DYN_TAG"
SENT_BEFORE=$(bundle_sha)
run_stage VNM04 CASE12_V4 "$BC4"
expect_last SUPPORT_PAIR_COUNT 2
expect_last SUPPORT_MATCH 1
expect_last EVIDENCE_CAPACITY_EXCEEDED 1
expect_last BRIDGE_STATUS REFUSED_EVIDENCE_CAPACITY
expect_last OUTPUT_ALLOWED 0
SENT_AFTER=$(bundle_sha)
[ "$SENT_BEFORE" = "$SENT_AFTER" ] || fail_gate 79 REFUSAL_MUTATED_BUNDLE
NEGATIVE_PASS_COUNT=$((NEGATIVE_PASS_COUNT + 1))
mark_case_pass

# CASE 13 — noncandidate/noncandidate same-context pair is ignored
prepare_case CASE_013_NONCANDIDATE_PAIR_IGNORED
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" N1 "IGNORE-BASE-"
clear_v3
add_seq N21 "$L3~$C~$R3" "IGNORE-C"
add_seq N22 "$L3~$D~$R3" "IGNORE-D"
run_stage VNM03 CASE13_V3_EXTRA2 "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 2
append_v3_output
run_v4_ready CASE13_V4
expect_last ELIGIBLE_EVIDENCE_COUNT 2
expect_last SUPPORT_PAIR_COUNT 2
expect_last COMPETING_RAW_PAIR_COUNT 0
mark_case_pass

# CASE 14 — later native observations create raw competing evidence; VNM01 updates weight
prepare_case CASE_014_COMPETING_RAW_EVIDENCE_FULL_CHAIN
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" P1 "COMP-BASE-"
clear_v3
add_seq P21 "$L3~$A~$R3" "COMP-A"
add_seq P22 "$L3~$C~$R3" "COMP-C"
run_stage VNM03 CASE14_V3_SECOND "$BC3"
expect_last DERIVED_OBSERVATION_COUNT 2
append_v3_output
route_v3_to_v2
run_stage VNM02 CASE14_V2_SECOND "$BC2"
V2LOG="$LAST_LOG"
expect_line_file "$V2LOG" PAIR_CANDIDATE_STATUS PAIR_CANDIDATE_INDUCED
expect_line_file "$V2LOG" PAIR_CANDIDATE_SUPPORT 2
expect_v2_pair_unordered "$V2LOG" "$A" "$B"
decode_v2_candidate "$V2LOG"
run_v4_ready CASE14_V4
expect_last SUPPORT_PAIR_COUNT 2
expect_last COMPETING_RAW_PAIR_COUNT 1
expect_last ELIGIBLE_EVIDENCE_COUNT 3
run_v1_from_bundle CASE14_V1
expect_last NEW_SUPPORT_COUNT 2
expect_last NEW_COMPETING_COUNT 1
expect_last WEIGHT_AFTER 1
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))
mark_case_pass

# CASE 15 — fresh VNM02 invocation reuses persisted native candidate state
prepare_case CASE_015_VNM02_PERSISTENT_REUSE
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" R1 "PERSIST2-"
: > "$V2_IN"
run_stage VNM02 CASE15_V2_STATE_ONLY "$BC2"
V2LOG="$LAST_LOG"
expect_line_file "$V2LOG" PREVIOUS_STATE_VALID 1
expect_line_file "$V2LOG" PAIR_CANDIDATE_STATUS PAIR_CANDIDATE_INDUCED
expect_line_file "$V2LOG" PAIR_CANDIDATE_SUPPORT 2
decode_v2_candidate "$V2LOG"
run_v4_ready CASE15_V4
run_v1_from_bundle CASE15_V1
expect_last WEIGHT_AFTER 2
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))
mark_case_pass

# CASE 16 — VNM01 learned weight survives a fresh invocation with no new evidence
prepare_case CASE_016_VNM01_PERSISTENT_WEIGHT_REUSE
build_support2_native "$A" "$B" "$L1" "$R1" "$L2" "$R2" W1 "PERSIST1-"
run_v4_ready CASE16_V4
run_v1_from_bundle CASE16_V1_FIRST
expect_last WEIGHT_AFTER 2
: > "$V1_EVID"
run_stage VNM01 CASE16_V1_STATE_ONLY "$BC1"
expect_last PREVIOUS_STATE_VALID 1
expect_last WEIGHT_BEFORE 2
expect_last WEIGHT_AFTER 2
expect_last NATIVE_UPDATE_REASON NO_NEW_QUALIFIED_EVIDENCE
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
PERSISTENCE_PASS_COUNT=$((PERSISTENCE_PASS_COUNT + 1))
mark_case_pass

# CASE 17 — exact full-chain replay A
prepare_case CASE_017_REPLAY_A
build_support2_native "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2" Z1 "REPLAY-"
V2_REPLAY_A="$LAST_LOG"
run_v4_ready CASE17_V4
V4_REPLAY_A="$LAST_LOG"
BUNDLE_A_SHA=$(bundle_sha)
run_v1_from_bundle CASE17_V1
V1_REPLAY_A="$LAST_LOG"
V1_STATE_A_SHA=$(sha_of "$V1_STATE")
V3_REPLAY_A="$LOG/${CASE_NAME}_Z1_V3.log"
CHAIN_A="$SANDBOX/chain_a.log"
"$P/bin/cat" "$V3_REPLAY_A" "$V2_REPLAY_A" "$V4_REPLAY_A" "$V1_REPLAY_A" > "$CHAIN_A"
CHAIN_A_SHA=$(sha_of "$CHAIN_A")
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
mark_case_pass

# CASE 18 — exact full-chain replay B
prepare_case CASE_018_REPLAY_B
build_support2_native "$A2" "$B2" "$Q1" "$Z1" "$Q2" "$Z2" Z1 "REPLAY-"
V2_REPLAY_B="$LAST_LOG"
run_v4_ready CASE18_V4
V4_REPLAY_B="$LAST_LOG"
BUNDLE_B_SHA=$(bundle_sha)
run_v1_from_bundle CASE18_V1
V1_REPLAY_B="$LAST_LOG"
V1_STATE_B_SHA=$(sha_of "$V1_STATE")
V3_REPLAY_B="$LOG/${CASE_NAME}_Z1_V3.log"
CHAIN_B="$SANDBOX/chain_b.log"
"$P/bin/cat" "$V3_REPLAY_B" "$V2_REPLAY_B" "$V4_REPLAY_B" "$V1_REPLAY_B" > "$CHAIN_B"
CHAIN_B_SHA=$(sha_of "$CHAIN_B")

REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=NO
if [ "$CHAIN_A_SHA" = "$CHAIN_B_SHA" ] \
    && [ "$BUNDLE_A_SHA" = "$BUNDLE_B_SHA" ] \
    && [ "$V1_STATE_A_SHA" = "$V1_STATE_B_SHA" ]; then
    REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
fi
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 80 FULL_CHAIN_REPLAY_MISMATCH
FULL_CHAIN_PASS_COUNT=$((FULL_CHAIN_PASS_COUNT + 1))
mark_case_pass

SOURCE4_AFTER=$(sha_of "$SRC4")
SOURCE3_AFTER=$(sha_of "$SRC3")
SOURCE2_AFTER=$(sha_of "$SRC2")
SOURCE1_AFTER=$(sha_of "$SRC1")
BC4_AFTER=$(sha_of "$BC4")
BC3_AFTER=$(sha_of "$BC3")
BC2_AFTER=$(sha_of "$BC2")
BC1_AFTER=$(sha_of "$BC1")

SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO

if [ "$SOURCE4_BEFORE" = "$SOURCE4_AFTER" ] \
    && [ "$SOURCE3_BEFORE" = "$SOURCE3_AFTER" ] \
    && [ "$SOURCE2_BEFORE" = "$SOURCE2_AFTER" ] \
    && [ "$SOURCE1_BEFORE" = "$SOURCE1_AFTER" ]; then
    SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi

if [ "$BC4_BEFORE" = "$BC4_AFTER" ] \
    && [ "$BC3_BEFORE" = "$BC3_AFTER" ] \
    && [ "$BC2_BEFORE" = "$BC2_AFTER" ] \
    && [ "$BC1_BEFORE" = "$BC1_AFTER" ]; then
    BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
fi

TOKEN_LEAK_COUNT=0
for FROZEN in "$SRC4" "$SRC3" "$SRC2" "$SRC1" "$BC4" "$BC3" "$BC2" "$BC1"
do
    if "$P/bin/grep" -a -F "$DYN_TAG" "$FROZEN" >/dev/null 2>&1; then
        TOKEN_LEAK_COUNT=$((TOKEN_LEAK_COUNT + 1))
    fi
    if "$P/bin/grep" -a -F "$DYN_TAG_2" "$FROZEN" >/dev/null 2>&1; then
        TOKEN_LEAK_COUNT=$((TOKEN_LEAK_COUNT + 1))
    fi
done

[ "$TOTAL_VM_INVOCATIONS" -eq 73 ] || fail_gate 81 TOTAL_VM_INVOCATION_COUNT_MISMATCH
[ "$VNM03_VM_INVOCATIONS" -eq 26 ] || fail_gate 82 VNM03_VM_INVOCATION_COUNT_MISMATCH
[ "$VNM02_VM_INVOCATIONS" -eq 21 ] || fail_gate 83 VNM02_VM_INVOCATION_COUNT_MISMATCH
[ "$VNM04_VM_INVOCATIONS" -eq 18 ] || fail_gate 84 VNM04_VM_INVOCATION_COUNT_MISMATCH
[ "$VNM01_VM_INVOCATIONS" -eq 8 ] || fail_gate 85 VNM01_VM_INVOCATION_COUNT_MISMATCH
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 18 ] || fail_gate 86 ALIGNMENT_PASS_COUNT_MISMATCH
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || fail_gate 87 ALIGNMENT_FAILURE_PRESENT
[ "$VM_NONZERO_COUNT" -eq 0 ] || fail_gate 88 VM_NONZERO_PRESENT
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || fail_gate 89 STEP_LIMIT_PRESENT
[ "$NEGATIVE_PASS_COUNT" -eq 9 ] || fail_gate 90 NEGATIVE_PASS_COUNT_MISMATCH
[ "$PERSISTENCE_PASS_COUNT" -eq 3 ] || fail_gate 91 PERSISTENCE_PASS_COUNT_MISMATCH
[ "$FULL_CHAIN_PASS_COUNT" -eq 7 ] || fail_gate 92 FULL_CHAIN_PASS_COUNT_MISMATCH
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 93 SOURCE_MUTATED
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail_gate 94 BYTECODE_MUTATED
[ "$TOKEN_LEAK_COUNT" -eq 0 ] || fail_gate 95 DYNAMIC_TOKEN_LEAK
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail_gate 96 REPLAY_MISMATCH

printf '\n=== VNM-04 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE\n'
printf 'CAPABILITY_NAME=Native pair-candidate to VNM-01 weight-input bridge with full VNM-03->02->04->01 integration evidence\n'
printf 'TEACHING_GOAL=SIGMA natively converts a native VNM-02 pair candidate plus native VNM-03 observations into bounded VNM-01 hypothesis/evidence input without host candidate/evidence generation\n'
printf 'DEPENDENCIES=VNM03_VNM02_VNM01_ADMITTED_EXACT_SOURCES_AND_BYTECODES_PLUS_LOCKED_SIGMAC_VM\n'
printf 'SOURCE_SHA256=%s\n' "$SOURCE4_AFTER"
printf 'BYTECODE_SHA256=%s\n' "$BC4_AFTER"
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'VNM03_VM_INVOCATIONS=%s\n' "$VNM03_VM_INVOCATIONS"
printf 'VNM02_VM_INVOCATIONS=%s\n' "$VNM02_VM_INVOCATIONS"
printf 'VNM04_VM_INVOCATIONS=%s\n' "$VNM04_VM_INVOCATIONS"
printf 'VNM01_VM_INVOCATIONS=%s\n' "$VNM01_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_PASS_COUNT=%s\n' "$NEGATIVE_PASS_COUNT"
printf 'PERSISTENCE_PASS_COUNT=%s\n' "$PERSISTENCE_PASS_COUNT"
printf 'FULL_CHAIN_PASS_COUNT=%s\n' "$FULL_CHAIN_PASS_COUNT"
printf 'INPUT_DYNAMIC=YES\n'
printf 'OUTPUT_DEPENDS_ON_INPUT=YES\n'
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=NO_FOR_VNM04_PURE_BRIDGE;YES_IN_DOWNSTREAM_VNM02_VNM01_CHAIN\n'
printf 'PERSISTENT_STATE_TEST=PASS_IN_INTEGRATION_CHAIN\n'
printf 'RESTART_REPLAY_TEST=PASS\n'
printf 'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=%s\n' "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION"
printf 'BRIDGE_DECISION_OWNER=SIGMA_NATIVE\n'
printf 'HYPOTHESIS_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'EVIDENCE_GENERATION_OWNER=SIGMA_NATIVE\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\n'
printf 'HOST_CANDIDATE_GENERATION=NO\n'
printf 'HOST_CANDIDATE_SELECTION=NO\n'
printf 'HOST_CONTEXT_EXTRACTION=NO\n'
printf 'HOST_EVIDENCE_GENERATION=NO\n'
printf 'HOST_WEIGHT_UPDATE=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\n' "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$TOKEN_LEAK_COUNT"
printf 'STEP_LIMIT_STATUS=PASS_IN_BOUNDED_INTEGRATION_SUITE\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN\n'
printf 'SEMANTIC_EQUIVALENCE=NOT_PROVEN\n'
printf 'WORD_MEANING=NOT_PROVEN\n'
printf 'VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded mechanically-routed native chain from delimiter-defined UTF-8 sequences through VNM-03 observations, VNM-02 structural pair induction, VNM-04 hypothesis/raw-evidence bridge and VNM-01 persistent structural weight update; exact protocol decode only on host; no tokenization or semantic-equivalence claim\n'
printf 'VNM_04_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
