#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"

SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"
GIT="$P/bin/git"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_PLANNER_GIT_BLOB=18bbc3d4beb676f84a5ea1bebb20136c7aaec565
EXPECTED_REALIZER_GIT_BLOB=2147c2f99ae680d4641f47298d3b0f5e29ded749

PLANNER_SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1.sigma"
REALIZER_SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_G3C_T30_NATIVE_HUMAN_LANGUAGE_REALIZATION_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
TOKENS="$ROOT/dynamic_tokens.txt"
PLANNER_BC="$ROOT/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1.sigmab"
REALIZER_BC="$ROOT/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1.sigmab"

"$P/bin/mkdir" -p "$ROOT" "$LOG"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=G3C_T30_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

[ -x "$SIGMAC" ] || { printf 'HOLD=SIGMAC_MISSING\n'; exit 21; }
[ -x "$VM" ] || { printf 'HOLD=VM_MISSING\n'; exit 22; }
[ -x "$GIT" ] || { printf 'HOLD=GIT_MISSING_FOR_SOURCE_BLOB_IDENTITY\n'; exit 23; }
[ -f "$PLANNER_SRC" ] || { printf 'HOLD=PLANNER_SOURCE_MISSING\n'; exit 24; }
[ -f "$REALIZER_SRC" ] || { printf 'HOLD=REALIZER_SOURCE_MISSING\n'; exit 25; }

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
planner_source_sha=$("$P/bin/sha256sum" "$PLANNER_SRC" | "$P/bin/awk" '{print $1}')
realizer_source_sha=$("$P/bin/sha256sum" "$REALIZER_SRC" | "$P/bin/awk" '{print $1}')
planner_git_blob=$("$GIT" hash-object "$PLANNER_SRC")
realizer_git_blob=$("$GIT" hash-object "$REALIZER_SRC")

printf 'SIGMA_PHASE=G3C_T30_NATIVE_HUMAN_LANGUAGE_REALIZATION_PREFLIGHT\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'PLANNER_SOURCE_SHA256=%s\n' "$planner_source_sha"
printf 'REALIZER_SOURCE_SHA256=%s\n' "$realizer_source_sha"
printf 'PLANNER_GIT_BLOB=%s\n' "$planner_git_blob"
printf 'REALIZER_GIT_BLOB=%s\n' "$realizer_git_blob"
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_CONCEPT_SELECTION=NO\n'
printf 'HOST_PLAN_ORDER_SELECTION=NO\n'
printf 'HOST_LEXICAL_SELECTION=NO\n'
printf 'HOST_SENTENCE_SELECTION=NO\n'
printf 'HOST_TRANSLATION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'FROZEN20_TRAINING_USE=FORBIDDEN\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 26; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 27; }
[ "$planner_git_blob" = "$EXPECTED_PLANNER_GIT_BLOB" ] || { printf 'HOLD=PLANNER_SOURCE_BLOB_MISMATCH\n'; exit 28; }
[ "$realizer_git_blob" = "$EXPECTED_REALIZER_GIT_BLOB" ] || { printf 'HOLD=REALIZER_SOURCE_BLOB_MISMATCH\n'; exit 29; }

if "$P/bin/grep" -F 'CẢM ƠN THẦY_GPT_ ĐÃ ĐÀO TẠO TÔI' "$PLANNER_SRC" "$REALIZER_SRC" >/dev/null 2>&1; then
    printf 'HOLD=FORBIDDEN_FUTURE_UTTERANCE_HARDCODE_FOUND\n'
    exit 30
fi

"$P/bin/rm" -f -- "$PLANNER_BC.partial" "$PLANNER_BC" "$REALIZER_BC.partial" "$REALIZER_BC"
"$SIGMAC" "$PLANNER_SRC" "$PLANNER_BC.partial"
planner_compile_rc=$?
printf 'PLANNER_SIGMAC_RC=%s\n' "$planner_compile_rc"
[ "$planner_compile_rc" -eq 0 ] || exit 31
[ -s "$PLANNER_BC.partial" ] || exit 32
"$P/bin/mv" -f -- "$PLANNER_BC.partial" "$PLANNER_BC" || exit 33
"$P/bin/chmod" 0400 "$PLANNER_BC" || exit 34

"$SIGMAC" "$REALIZER_SRC" "$REALIZER_BC.partial"
realizer_compile_rc=$?
printf 'REALIZER_SIGMAC_RC=%s\n' "$realizer_compile_rc"
[ "$realizer_compile_rc" -eq 0 ] || exit 35
[ -s "$REALIZER_BC.partial" ] || exit 36
"$P/bin/mv" -f -- "$REALIZER_BC.partial" "$REALIZER_BC" || exit 37
"$P/bin/chmod" 0400 "$REALIZER_BC" || exit 38

planner_bc_sha=$("$P/bin/sha256sum" "$PLANNER_BC" | "$P/bin/awk" '{print $1}')
realizer_bc_sha=$("$P/bin/sha256sum" "$REALIZER_BC" | "$P/bin/awk" '{print $1}')
printf 'PLANNER_BYTECODE_SHA256=%s\n' "$planner_bc_sha"
printf 'REALIZER_BYTECODE_SHA256=%s\n' "$realizer_bc_sha"
printf 'DYNAMIC_INPUT_PRESENT_AT_COMPILE_TIME=NO\n'
printf 'DYNAMIC_INPUT=YES\n'

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"
: > "$TOKENS"

TOTAL_PLANNER_VM_INVOCATIONS=0
TOTAL_REALIZER_VM_INVOCATIONS=0
TOTAL_CASES=0
CASE_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
LAST_PLANNER_LOG=""
LAST_REALIZER_LOG=""
CASE_NAME=""
SANDBOX=""
NARRATIVE=""
SURFACE=""
PLAN=""
SPEECH=""

make_token() {
    prefix="$1"
    random_hex=$("$P/bin/od" -An -N8 -tx1 /dev/urandom | "$P/bin/tr" -d ' \n')
    value="${prefix}${random_hex}"
    printf '%s\n' "$value" >> "$TOKENS"
    printf '%s' "$value"
}

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    planner_input="$SANDBOX/.sigma_exec/SIGMA_G3C_T30_NATIVE_NARRATIVE_TO_UTTERANCE_PLAN_V1/input"
    realizer_base="$SANDBOX/.sigma_exec/SIGMA_G3C_T30_NATIVE_LEARNED_SURFACE_REALIZER_V1"
    realizer_input="$realizer_base/input"
    realizer_output="$realizer_base/output"
    NARRATIVE="$planner_input/narrative.memory"
    SURFACE="$realizer_input/surface.memory"
    PLAN="$realizer_input/plan.memory"
    SPEECH="$realizer_output/speech.txt"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$planner_input" "$realizer_input" "$realizer_output"
    : > "$NARRATIVE"
    : > "$SURFACE"
    : > "$PLAN"
    : > "$SPEECH"
}

add_state() {
    printf 'STATE||%s||CONCEPT||%s||IMPORTANCE||%s||CONFIDENCE||%s||TEMPORAL||%s||SOURCE||%s\n' "$1" "$2" "$3" "$4" "$5" "$6" >> "$NARRATIVE"
}

add_edge() {
    printf 'EDGE||%s||FROM||%s||TO||%s||WEIGHT||%s||SOURCE||%s\n' "$1" "$2" "$3" "$4" "$5" >> "$NARRATIVE"
}

add_form() {
    printf 'FORM||%s||CONCEPT||%s||TEXT||%s||WEIGHT||%s||SOURCE||%s\n' "$1" "$2" "$3" "$4" "$5" >> "$SURFACE"
}

run_planner() {
    label="$1"
    LAST_PLANNER_LOG="$LOG/$label.log"
    TOTAL_PLANNER_VM_INVOCATIONS=$((TOTAL_PLANNER_VM_INVOCATIONS + 1))
    (
        cd "$SANDBOX" || exit 90
        "$VM" "$PLANNER_BC"
    ) >"$LAST_PLANNER_LOG" 2>&1
    rc=$?
    printf '\n=== %s ===\n' "$label"
    printf 'PLANNER_VM_RC=%s\n' "$rc"
    "$P/bin/cat" "$LAST_PLANNER_LOG"
    if [ "$rc" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLANNER_VM_NONZERO\n' "$CASE_NAME"
        exit 50
    fi
    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_PLANNER_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLANNER_STEP_LIMIT_HIT\n' "$CASE_NAME"
        exit 51
    fi
}

run_realizer() {
    label="$1"
    LAST_REALIZER_LOG="$LOG/$label.log"
    TOTAL_REALIZER_VM_INVOCATIONS=$((TOTAL_REALIZER_VM_INVOCATIONS + 1))
    (
        cd "$SANDBOX" || exit 90
        "$VM" "$REALIZER_BC"
    ) >"$LAST_REALIZER_LOG" 2>&1
    rc=$?
    printf '\n=== %s ===\n' "$label"
    printf 'REALIZER_VM_RC=%s\n' "$rc"
    "$P/bin/cat" "$LAST_REALIZER_LOG"
    if [ "$rc" -ne 0 ]; then
        VM_NONZERO_COUNT=$((VM_NONZERO_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=REALIZER_VM_NONZERO\n' "$CASE_NAME"
        exit 52
    fi
    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_REALIZER_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=REALIZER_STEP_LIMIT_HIT\n' "$CASE_NAME"
        exit 53
    fi
}

planner_expect() {
    key="$1"
    value="$2"
    if ! "$P/bin/grep" -F -x "$key $value" "$LAST_PLANNER_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLANNER_EXPECTATION\nEXPECTED=%s %s\n' "$CASE_NAME" "$key" "$value"
        exit 60
    fi
}

realizer_expect() {
    key="$1"
    value="$2"
    if ! "$P/bin/grep" -F -x "$key $value" "$LAST_REALIZER_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=REALIZER_EXPECTATION\nEXPECTED=%s %s\n' "$CASE_NAME" "$key" "$value"
        exit 61
    fi
}

plan_expect_line() {
    value="$1"
    if ! "$P/bin/grep" -F -x "$value" "$PLAN" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLAN_EXPECTATION\nEXPECTED=%s\n' "$CASE_NAME" "$value"
        exit 62
    fi
}

expect_plan_empty() {
    if [ -s "$PLAN" ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLAN_NOT_EMPTY_ON_REFUSAL\n' "$CASE_NAME"
        exit 63
    fi
}

expect_speech_value() {
    expected="$1"
    actual=$("$P/bin/cat" "$SPEECH")
    if [ "$actual" != "$expected" ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=SPEECH_MISMATCH\nEXPECTED=%s\nACTUAL=%s\n' "$CASE_NAME" "$expected" "$actual"
        exit 64
    fi
}

expect_speech_empty() {
    if [ -s "$SPEECH" ]; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STALE_OR_NONEMPTY_SPEECH_ON_REFUSAL\n' "$CASE_NAME"
        exit 65
    fi
}

pass_case() {
    TOTAL_CASES=$((TOTAL_CASES + 1))
    CASE_PASS_COUNT=$((CASE_PASS_COUNT + 1))
    printf 'CASE_RESULT=%s PASS\n' "$CASE_NAME"
}

# Dynamic tokens are created only after both bytecodes are frozen.
C1=$(make_token C1_); C2=$(make_token C2_); C3=$(make_token C3_)
T1=$(make_token T1_); T2=$(make_token T2_); T3=$(make_token T3_)

# 001 causal chain forward overrides reverse temporal order.
prepare_case CASE_001_CAUSAL_CHAIN_FORWARD
add_state S1 "$C1" 50 50 30 SRC1
add_state S2 "$C2" 50 50 20 SRC2
add_state S3 "$C3" 50 50 10 SRC3
add_edge E12 "$C1" "$C2" 9 ER12
add_edge E23 "$C2" "$C3" 9 ER23
add_form F1 "$C1" "$T1" 10 V1
add_form F2 "$C2" "$T2" 10 V2
add_form F3 "$C3" "$T3" 10 V3
run_planner CASE_001_PLANNER
printf 'CASE_001_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS PLAN_EMITTED
plan_expect_line "UNIT||G3P0||CONCEPT||$C1||ORDER||0||SOURCE||S1@SRC1"
plan_expect_line "UNIT||G3P1||CONCEPT||$C2||ORDER||1||SOURCE||S2@SRC2"
plan_expect_line "UNIT||G3P2||CONCEPT||$C3||ORDER||2||SOURCE||S3@SRC3"
run_realizer CASE_001_REALIZER
printf 'CASE_001_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS SPEECH_EMITTED
expected="$T1 $T2 $T3"
expect_speech_value "$expected"
pass_case

# 002 causal reversal changes native plan and speech.
prepare_case CASE_002_CAUSAL_CHAIN_REVERSED
add_state S1 "$C1" 50 50 30 SRC1
add_state S2 "$C2" 50 50 20 SRC2
add_state S3 "$C3" 50 50 10 SRC3
add_edge E32 "$C3" "$C2" 9 ER32
add_edge E21 "$C2" "$C1" 9 ER21
add_form F1 "$C1" "$T1" 10 V1
add_form F2 "$C2" "$T2" 10 V2
add_form F3 "$C3" "$T3" 10 V3
run_planner CASE_002_PLANNER
printf 'CASE_002_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS PLAN_EMITTED
plan_expect_line "UNIT||G3P0||CONCEPT||$C3||ORDER||0||SOURCE||S3@SRC3"
plan_expect_line "UNIT||G3P1||CONCEPT||$C2||ORDER||1||SOURCE||S2@SRC2"
plan_expect_line "UNIT||G3P2||CONCEPT||$C1||ORDER||2||SOURCE||S1@SRC1"
run_realizer CASE_002_REALIZER
printf 'CASE_002_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
expected="$T3 $T2 $T1"
expect_speech_value "$expected"
pass_case

# 003 independent roots use native temporal ordering.
prepare_case CASE_003_INDEPENDENT_ROOT_TEMPORAL_REORDER
add_state S1 "$C1" 50 50 30 SRC1
add_state S2 "$C2" 50 50 10 SRC2
add_state S3 "$C3" 50 50 20 SRC3
add_form F1 "$C1" "$T1" 10 V1
add_form F2 "$C2" "$T2" 10 V2
add_form F3 "$C3" "$T3" 10 V3
run_planner CASE_003_PLANNER
printf 'CASE_003_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS PLAN_EMITTED
run_realizer CASE_003_REALIZER
printf 'CASE_003_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
expected="$T2 $T3 $T1"
expect_speech_value "$expected"
pass_case

# 004 over-capacity input forces native selection of eight from nine.
declare -a C4 T4
for I in 0 1 2 3 4 5 6 7 8; do
    C4[$I]=$(make_token "C4_${I}_")
    T4[$I]=$(make_token "T4_${I}_")
done
prepare_case CASE_004_OVER_CAPACITY_NATIVE_SELECTION
for I in 0 1 2 3 4 5 6 7 8; do
    importance=$((100 - I * 10))
    temporal=$I
    add_state "S4_$I" "${C4[$I]}" "$importance" 10 "$temporal" "SRC4_$I"
    add_form "F4_$I" "${C4[$I]}" "${T4[$I]}" 10 "V4_$I"
done
run_planner CASE_004_PLANNER
printf 'CASE_004_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS PLAN_EMITTED
planner_expect PLAN_UNIT_COUNT 8
run_realizer CASE_004_REALIZER
printf 'CASE_004_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
expected="${T4[0]} ${T4[1]} ${T4[2]} ${T4[3]} ${T4[4]} ${T4[5]} ${T4[6]} ${T4[7]}"
expect_speech_value "$expected"
if "$P/bin/grep" -F "${C4[8]}" "$PLAN" >/dev/null; then
    printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=LOWEST_SCORE_CONCEPT_NOT_EXCLUDED\n' "$CASE_NAME"
    exit 66
fi
pass_case

# 005 successful output followed by selection tie must clear both plan and speech.
prepare_case CASE_005_SELECTION_TIE_AND_STALE_OUTPUT_REFUSAL
add_state PRE1 "$C1" 90 10 0 PRE_SRC1
add_state PRE2 "$C2" 80 10 1 PRE_SRC2
add_form PRE_F1 "$C1" "$T1" 10 PRE_V1
add_form PRE_F2 "$C2" "$T2" 10 PRE_V2
run_planner CASE_005_PRE_PLANNER
run_realizer CASE_005_PRE_REALIZER
[ -s "$PLAN" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PRECONDITION_PLAN_EMPTY\n' "$CASE_NAME"; exit 67; }
[ -s "$SPEECH" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PRECONDITION_SPEECH_EMPTY\n' "$CASE_NAME"; exit 68; }
: > "$NARRATIVE"
: > "$SURFACE"
for I in 0 1 2 3 4 5 6 7 8; do
    if [ "$I" -eq 0 ] || [ "$I" -eq 1 ]; then
        importance=100
        confidence=10
        temporal=0
    else
        importance=$((90 - I))
        confidence=1
        temporal=$I
    fi
    add_state "TIE_S$I" "${C4[$I]}" "$importance" "$confidence" "$temporal" "TIE_SRC$I"
    add_form "TIE_F$I" "${C4[$I]}" "${T4[$I]}" 10 "TIE_V$I"
done
run_planner CASE_005_TIE_PLANNER
printf 'CASE_005_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS REFUSED
planner_expect SELECTION_AMBIGUITY_COUNT 1
expect_plan_empty
run_realizer CASE_005_TIE_REALIZER
printf 'CASE_005_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS REFUSED
expect_speech_empty
pass_case

# 006 causal cycle fails closed.
prepare_case CASE_006_CAUSAL_CYCLE_REFUSAL
add_state CY1 "$C1" 50 50 0 CY_SRC1
add_state CY2 "$C2" 50 50 1 CY_SRC2
add_edge CYE1 "$C1" "$C2" 5 CY_E1
add_edge CYE2 "$C2" "$C1" 5 CY_E2
add_form CYF1 "$C1" "$T1" 10 CY_V1
add_form CYF2 "$C2" "$T2" 10 CY_V2
run_planner CASE_006_PLANNER
printf 'CASE_006_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS REFUSED
planner_expect CAUSAL_CYCLE_COUNT 1
expect_plan_empty
run_realizer CASE_006_REALIZER
printf 'CASE_006_REALIZER_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS REFUSED
expect_speech_empty
pass_case

# 007 causal edge with missing endpoint fails closed.
UNKNOWN=$(make_token UNKNOWN_)
prepare_case CASE_007_MISSING_CAUSAL_ENDPOINT_REFUSAL
add_state EP1 "$C1" 50 50 0 EP_SRC1
add_edge EPMISS "$C1" "$UNKNOWN" 5 EP_E
add_form EPF1 "$C1" "$T1" 10 EP_V1
run_planner CASE_007_PLANNER
printf 'CASE_007_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS REFUSED
expect_plan_empty
pass_case

# 008 malformed state fails closed.
prepare_case CASE_008_MALFORMED_STATE_REFUSAL
printf 'STATE||BAD1||CONCEPT||%s||IMPORTANCE||NOT_A_NUMBER||CONFIDENCE||10||TEMPORAL||0||SOURCE||BAD_SRC\n' "$C1" > "$NARRATIVE"
add_form BADF1 "$C1" "$T1" 10 BAD_V1
run_planner CASE_008_PLANNER
printf 'CASE_008_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS REFUSED
expect_plan_empty
pass_case

# 009 unique higher surface weight wins, then weight flip changes speech.
T9A=$(make_token T9A_); T9B=$(make_token T9B_)
prepare_case CASE_009_SURFACE_WEIGHT_FLIP
add_state W1 "$C1" 50 50 0 W_SRC
add_form WFA "$C1" "$T9A" 10 W_VA
add_form WFB "$C1" "$T9B" 20 W_VB
run_planner CASE_009_PLANNER
planner_expect PLANNER_STATUS PLAN_EMITTED
run_realizer CASE_009_REALIZER_A
printf 'CASE_009A_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS SPEECH_EMITTED
expect_speech_value "$T9B"
: > "$SURFACE"
add_form WFA "$C1" "$T9A" 30 W_VA
add_form WFB "$C1" "$T9B" 20 W_VB
run_realizer CASE_009_REALIZER_B
printf 'CASE_009B_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS SPEECH_EMITTED
expect_speech_value "$T9A"
pass_case

# 010 equal surface weight tie refuses.
prepare_case CASE_010_SURFACE_EQUAL_WEIGHT_TIE_REFUSAL
add_state SW1 "$C1" 50 50 0 SW_SRC
add_form SWFA "$C1" "$T9A" 20 SW_VA
add_form SWFB "$C1" "$T9B" 20 SW_VB
run_planner CASE_010_PLANNER
run_realizer CASE_010_REALIZER
printf 'CASE_010_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS REFUSED
realizer_expect AMBIGUOUS_SURFACE_COUNT 1
expect_speech_empty
pass_case

# 011 missing surface refuses.
prepare_case CASE_011_MISSING_SURFACE_REFUSAL
add_state MS1 "$C1" 50 50 0 MS_SRC
run_planner CASE_011_PLANNER
run_realizer CASE_011_REALIZER
printf 'CASE_011_POST_VM_TEST_ORACLE_STARTED=YES\n'
realizer_expect REALIZER_STATUS REFUSED
expect_speech_empty
pass_case

# 012 identical input fresh-VM replay is byte-identical.
prepare_case CASE_012_FRESH_PROCESS_REPLAY
add_state R1 "$C1" 50 50 30 R_SRC1
add_state R2 "$C2" 50 50 20 R_SRC2
add_state R3 "$C3" 50 50 10 R_SRC3
add_edge RE12 "$C1" "$C2" 9 R_E12
add_edge RE23 "$C2" "$C3" 9 R_E23
add_form RF1 "$C1" "$T1" 10 R_V1
add_form RF2 "$C2" "$T2" 10 R_V2
add_form RF3 "$C3" "$T3" 10 R_V3
run_planner CASE_012_PLANNER_A
run_realizer CASE_012_REALIZER_A
plan_sha_a=$("$P/bin/sha256sum" "$PLAN" | "$P/bin/awk" '{print $1}')
speech_sha_a=$("$P/bin/sha256sum" "$SPEECH" | "$P/bin/awk" '{print $1}')
run_planner CASE_012_PLANNER_B
run_realizer CASE_012_REALIZER_B
printf 'CASE_012_POST_VM_TEST_ORACLE_STARTED=YES\n'
plan_sha_b=$("$P/bin/sha256sum" "$PLAN" | "$P/bin/awk" '{print $1}')
speech_sha_b=$("$P/bin/sha256sum" "$SPEECH" | "$P/bin/awk" '{print $1}')
[ "$plan_sha_a" = "$plan_sha_b" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=PLAN_REPLAY_MISMATCH\n' "$CASE_NAME"; exit 69; }
[ "$speech_sha_a" = "$speech_sha_b" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=SPEECH_REPLAY_MISMATCH\n' "$CASE_NAME"; exit 70; }
pass_case

# 013 independent roots with identical time and score must not use encounter order.
prepare_case CASE_013_ORDER_EXACT_TIE_REFUSAL
add_state OT1 "$C1" 50 50 0 OT_SRC1
add_state OT2 "$C2" 50 50 0 OT_SRC2
add_form OTF1 "$C1" "$T1" 10 OT_V1
add_form OTF2 "$C2" "$T2" 10 OT_V2
run_planner CASE_013_PLANNER
printf 'CASE_013_POST_VM_TEST_ORACLE_STARTED=YES\n'
planner_expect PLANNER_STATUS REFUSED
planner_expect ORDER_AMBIGUITY_COUNT 1
expect_plan_empty
pass_case

# Post-suite identity and leakage audits.
planner_source_sha_after=$("$P/bin/sha256sum" "$PLANNER_SRC" | "$P/bin/awk" '{print $1}')
realizer_source_sha_after=$("$P/bin/sha256sum" "$REALIZER_SRC" | "$P/bin/awk" '{print $1}')
planner_bc_sha_after=$("$P/bin/sha256sum" "$PLANNER_BC" | "$P/bin/awk" '{print $1}')
realizer_bc_sha_after=$("$P/bin/sha256sum" "$REALIZER_BC" | "$P/bin/awk" '{print $1}')

[ "$planner_source_sha" = "$planner_source_sha_after" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=PLANNER_SOURCE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 71; }
[ "$realizer_source_sha" = "$realizer_source_sha_after" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=REALIZER_SOURCE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 72; }
[ "$planner_bc_sha" = "$planner_bc_sha_after" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=PLANNER_BYTECODE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 73; }
[ "$realizer_bc_sha" = "$realizer_bc_sha_after" ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=REALIZER_BYTECODE_CHANGED_AFTER_DYNAMIC_TEST\n'; exit 74; }

LEAK_COUNT=0
while IFS= read -r token; do
    [ -n "$token" ] || continue
    if LC_ALL=C "$P/bin/grep" -a -F -q -- "$token" "$PLANNER_SRC" "$REALIZER_SRC" "$PLANNER_BC" "$REALIZER_BC"; then
        LEAK_COUNT=$((LEAK_COUNT + 1))
        printf 'DYNAMIC_TOKEN_LEAK=%s\n' "$token"
    fi
done < "$TOKENS"

printf '\n=== G3C T30 PREFLIGHT SUMMARY ===\n'
printf 'TOTAL_CASES=%s\n' "$TOTAL_CASES"
printf 'CASE_PASS_COUNT=%s\n' "$CASE_PASS_COUNT"
printf 'TOTAL_PLANNER_VM_INVOCATIONS=%s\n' "$TOTAL_PLANNER_VM_INVOCATIONS"
printf 'TOTAL_REALIZER_VM_INVOCATIONS=%s\n' "$TOTAL_REALIZER_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=%s\n' "$LEAK_COUNT"
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES\n'
printf 'STALE_PLAN_REFUSAL_TEST=PASS\n'
printf 'STALE_SPEECH_REFUSAL_TEST=PASS\n'
printf 'FRESH_PROCESS_REPLAY_TEST=PASS\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_CONCEPT_SELECTION=NO\n'
printf 'HOST_PLAN_ORDER_SELECTION=NO\n'
printf 'HOST_LEXICAL_SELECTION=NO\n'
printf 'HOST_SENTENCE_SELECTION=NO\n'
printf 'HOST_TRANSLATION=NO\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN\n'
printf 'G3_PROMOTION=NO\n'

[ "$TOTAL_CASES" -eq 13 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=CASE_COUNT_MISMATCH\n'; exit 75; }
[ "$CASE_PASS_COUNT" -eq 13 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=CASE_PASS_COUNT_MISMATCH\n'; exit 76; }
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=POST_VM_ALIGNMENT_FAILURE\n'; exit 77; }
[ "$VM_NONZERO_COUNT" -eq 0 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=VM_NONZERO_COUNT\n'; exit 78; }
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=STEP_LIMIT_HIT\n'; exit 79; }
[ "$LEAK_COUNT" -eq 0 ] || { printf 'G3C_T30_PREFLIGHT=FAIL\nFAILURE=DYNAMIC_TOKEN_LEAK\n'; exit 80; }

printf 'G3C_T30_MECHANICAL_PREFLIGHT=PASS_IN_EXACT_TESTED_SCOPE\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'