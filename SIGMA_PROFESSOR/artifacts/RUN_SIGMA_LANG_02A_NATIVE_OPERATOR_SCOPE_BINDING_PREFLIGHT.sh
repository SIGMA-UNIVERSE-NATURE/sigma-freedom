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
EXPECTED_SOURCE=7a40e92e11c7c89574d3b975bb3210a7a7a23690251951da68be9e7edbfe292b

SRC="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_V1.sigma"
ROOT="$HOME_SIGMA/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_V1_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC="$ROOT/SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_V1.sigmab"

mkdir -p "$ROOT" "$LOG"

exec 9>"$LOCK"
"$P/bin/flock" -n 9 || {
    printf 'HOLD=LANG_02A_PREFLIGHT_ALREADY_RUNNING\n'
    exit 20
}

actual_sigmac=$("$P/bin/sha256sum" "$SIGMAC" | "$P/bin/awk" '{print $1}')
actual_vm=$("$P/bin/sha256sum" "$VM" | "$P/bin/awk" '{print $1}')
actual_source=$("$P/bin/sha256sum" "$SRC" | "$P/bin/awk" '{print $1}')

printf 'SIGMA_PHASE=LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_PREFLIGHT\n'
printf 'HOST_SCOPE_SELECTION=NO\n'
printf 'HOST_OPERATOR_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'DYNAMIC_INPUT_TEST=YES\n'
printf 'NEGATIVE_TEST=YES\n'
printf 'PERSISTENT_STATE=NA\n'
printf 'RESTART_REPLAY_TEST=YES\n'
printf 'SIGMAC_SHA256=%s\n' "$actual_sigmac"
printf 'VM_SHA256=%s\n' "$actual_vm"
printf 'SOURCE_SHA256=%s\n' "$actual_source"

[ "$actual_sigmac" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$actual_vm" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$actual_source" = "$EXPECTED_SOURCE" ] || { printf 'HOLD=LANG_02A_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }

if "$P/bin/grep" -F 'CẢM ƠN THẦY_GPT_ ĐÃ ĐÀO TẠO TÔI' "$SRC" >/dev/null 2>&1; then
    printf 'HOLD=FORBIDDEN_FUTURE_UTTERANCE_HARDCODE_FOUND\n'
    exit 24
fi

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

"$P/bin/rm" -rf -- "$CASES"
"$P/bin/mkdir" -p "$CASES"

TOTAL_VM_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=0
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
CASE_NAME=""
SANDBOX=""
BASE=""
IN=""
LAST_LOG=""

prepare_case() {
    CASE_NAME="$1"
    SANDBOX="$CASES/$CASE_NAME"
    BASE="$SANDBOX/.sigma_exec/SIGMA_LANG_02A_OPERATOR_SCOPE_BINDING_V1"
    IN="$BASE/input"
    "$P/bin/rm" -rf -- "$SANDBOX"
    "$P/bin/mkdir" -p "$IN"
    printf '%s' 'LANG-01A_NATIVE_DISTRIBUTIONAL_EVENT_FRAME_HYPOTHESIS_INDUCTION' > "$IN/dependency_capability.txt"
    printf '%s' 'ADMITTED_IN_EXACT_TESTED_SCOPE' > "$IN/dependency_status.txt"
    : > "$IN/scopes.memory"
    : > "$IN/operators.memory"
}

set_operator() {
    printf 'OPERATOR||%s||%s||CLASS||SCOPE_OPERATOR||SOURCE||%s\n' "$1" "$2" "$3" > "$IN/operators.memory"
}

add_scope() {
    printf 'SCOPE||%s||%s||%s||SOURCE||%s\n' "$1" "$2" "$3" "$4" >> "$IN/scopes.memory"
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
        printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=VM_NONZERO\n' "$LABEL"
        exit 50
    fi

    if "$P/bin/grep" -F 'Step limit exceeded' "$LAST_LOG" >/dev/null 2>&1; then
        STEP_LIMIT_HIT_COUNT=$((STEP_LIMIT_HIT_COUNT + 1))
        printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=STEP_LIMIT_HIT\n' "$LABEL"
        exit 51
    fi
}

expect_line() {
    KEY="$1"
    VALUE="$2"
    if ! "$P/bin/grep" -F -x "$KEY $VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_OUTPUT\nEXPECTED=%s %s\n' "$CASE_NAME" "$KEY" "$VALUE"
        exit 60
    fi
}

expect_exact() {
    VALUE="$1"
    if ! "$P/bin/grep" -F -x "$VALUE" "$LAST_LOG" >/dev/null; then
        POST_VM_ALIGNMENT_FAIL_COUNT=$((POST_VM_ALIGNMENT_FAIL_COUNT + 1))
        printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=MISSING_EXPECTED_SENTINEL\nEXPECTED=%s\n' "$CASE_NAME" "$VALUE"
        exit 61
    fi
}

pass_case() {
    expect_exact 'SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING'
    expect_line 'DEPENDENCY_BINDING_VALID' '1'
    expect_line 'SMALLEST_ENCLOSING_SCOPE_POLICY' 'NATIVE_MINIMUM_WIDTH'
    expect_line 'SCOPE_ENCLOSURE_BOUNDARY' 'INCLUSIVE'
    expect_line 'HOST_SCOPE_SELECTION' 'NO'
    expect_line 'HOST_OPERATOR_INTERPRETATION' 'NO'
    expect_line 'HOST_LEARNING' 'NO'
    expect_line 'HOST_SEMANTIC_INTERPRETATION' 'NO'
    expect_line 'PERSISTENT_STATE' 'NA'
    expect_line 'SURFACE_NEGATION_RECOGNITION' 'NOT_PROVEN'
    expect_line 'LOGICAL_NEGATION' 'NOT_PROVEN'
    expect_line 'SEMANTIC_SCOPE' 'NOT_PROVEN'
    expect_line 'SEMANTIC_UNDERSTANDING' 'NOT_PROVEN'
    expect_line 'PRODUCTION_STATE_MUTATED' 'NO'
    POST_VM_ALIGNMENT_PASS_COUNT=$((POST_VM_ALIGNMENT_PASS_COUNT + 1))
}

# 001: one enclosing scope.
prepare_case CASE_001_SINGLE
set_operator OP-A 5 CTX-OP-A
add_scope S-A 0 10 CTX-S-A
run_vm CASE_001_SINGLE
expect_line 'INPUT_ACCEPTED' '1'
expect_line 'ENCLOSING_SCOPE_COUNT' '1'
expect_line 'SCOPE_BINDING_STATUS' 'SELECTED_STRUCTURAL_SCOPE'
expect_line 'SELECTED_SCOPE_ID' 'S-A'
expect_line 'SELECTED_SCOPE_WIDTH' '10'
pass_case

# 002: two nested scopes; smaller enclosing scope wins natively.
prepare_case CASE_002_TWO_NESTED
set_operator OP-B 6 CTX-OP-B
add_scope S-OUT 0 20 CTX-OUT
add_scope S-IN 4 8 CTX-IN
run_vm CASE_002_TWO_NESTED
expect_line 'ENCLOSING_SCOPE_COUNT' '2'
expect_line 'SELECTED_SCOPE_ID' 'S-IN'
expect_line 'SELECTED_SCOPE_WIDTH' '4'
pass_case

# 003: three nested scopes.
prepare_case CASE_003_THREE_NESTED
set_operator OP-C 10 CTX-OP-C
add_scope S-WIDE 0 30 CTX-W
add_scope S-MID 5 20 CTX-M
add_scope S-TIGHT 9 11 CTX-T
run_vm CASE_003_THREE_NESTED
expect_line 'ENCLOSING_SCOPE_COUNT' '3'
expect_line 'SELECTED_SCOPE_ID' 'S-TIGHT'
expect_line 'SELECTED_SCOPE_WIDTH' '2'
pass_case

# 004: reverse encounter order; same structural winner identity.
prepare_case CASE_004_REVERSED_ORDER
set_operator OP-C2 10 CTX-OP-C2
add_scope S-TIGHT 9 11 CTX-T
add_scope S-MID 5 20 CTX-M
add_scope S-WIDE 0 30 CTX-W
run_vm CASE_004_REVERSED_ORDER
expect_line 'SELECTED_SCOPE_ID' 'S-TIGHT'
expect_line 'CANDIDATE_ENCOUNTER_ORDER_IS_WINNER_POLICY' 'NO'
pass_case

# 005: irrelevant disjoint scope does not affect binding.
prepare_case CASE_005_DISJOINT_IRRELEVANT
set_operator OP-D 5 CTX-OP-D
add_scope S-FAR 50 60 CTX-FAR
add_scope S-NEAR 1 9 CTX-NEAR
run_vm CASE_005_DISJOINT_IRRELEVANT
expect_line 'ENCLOSING_SCOPE_COUNT' '1'
expect_line 'SELECTED_SCOPE_ID' 'S-NEAR'
pass_case

# 006: equal minimum width across distinct scopes => ambiguity.
prepare_case CASE_006_EQUAL_MIN_TIE
set_operator OP-E 3 CTX-OP-E
add_scope S-A 1 5 CTX-A
add_scope S-B 1 5 CTX-B
add_scope S-OUT 0 10 CTX-O
run_vm CASE_006_EQUAL_MIN_TIE
expect_line 'ENCLOSING_SCOPE_COUNT' '3'
expect_line 'MINIMUM_WIDTH_TIED' '1'
expect_line 'SCOPE_BINDING_STATUS' 'AMBIGUOUS_SCOPE_BINDING'
expect_line 'SELECTED_SCOPE_ID' 'NONE'
pass_case

# 007: no enclosing scope => no fabricated binding.
prepare_case CASE_007_NO_ENCLOSING
set_operator OP-F 5 CTX-OP-F
add_scope S-L 0 3 CTX-L
add_scope S-R 7 9 CTX-R
run_vm CASE_007_NO_ENCLOSING
expect_line 'ENCLOSING_SCOPE_COUNT' '0'
expect_line 'SCOPE_BINDING_STATUS' 'NO_ENCLOSING_SCOPE'
expect_line 'SELECTED_SCOPE_ID' 'NONE'
pass_case

# 008: inclusive left boundary.
prepare_case CASE_008_LEFT_BOUNDARY
set_operator OP-G 5 CTX-OP-G
add_scope S-LEFT 5 9 CTX-LB
run_vm CASE_008_LEFT_BOUNDARY
expect_line 'SELECTED_SCOPE_ID' 'S-LEFT'
expect_line 'SELECTED_SCOPE_WIDTH' '4'
pass_case

# 009: inclusive right boundary.
prepare_case CASE_009_RIGHT_BOUNDARY
set_operator OP-H 5 CTX-OP-H
add_scope S-RIGHT 1 5 CTX-RB
run_vm CASE_009_RIGHT_BOUNDARY
expect_line 'SELECTED_SCOPE_ID' 'S-RIGHT'
expect_line 'SELECTED_SCOPE_WIDTH' '4'
pass_case

# 010: invalid structural range is refused.
prepare_case CASE_010_INVALID_RANGE
set_operator OP-I 5 CTX-OP-I
add_scope S-BAD 9 3 CTX-BAD
run_vm CASE_010_INVALID_RANGE
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'INVALID_SCOPE_COUNT' '1'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_INVALID_SCOPE_RECORD'
pass_case

# 011: identical duplicate is idempotent.
prepare_case CASE_011_IDENTICAL_DUPLICATE
set_operator OP-J 5 CTX-OP-J
add_scope S-DUP 0 10 CTX-DUP
add_scope S-DUP 0 10 CTX-DUP
run_vm CASE_011_IDENTICAL_DUPLICATE
expect_line 'UNIQUE_SCOPE_COUNT' '1'
expect_line 'DUPLICATE_SCOPE_COUNT' '1'
expect_line 'SELECTED_SCOPE_ID' 'S-DUP'
expect_line 'DUPLICATE_SCOPE_DOUBLE_COUNT' 'NO'
pass_case

# 012: same scope ID with different fingerprint is collision/refusal.
prepare_case CASE_012_SCOPE_ID_COLLISION
set_operator OP-K 5 CTX-OP-K
add_scope S-COLLIDE 0 10 CTX-C
add_scope S-COLLIDE 0 9 CTX-C
run_vm CASE_012_SCOPE_ID_COLLISION
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'SCOPE_ID_COLLISION_COUNT' '1'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_SCOPE_ID_COLLISION'
expect_line 'SCOPE_ID_COLLISION_MUTATES_STATE' 'NO'
pass_case

# 013: exactly one operator is required.
prepare_case CASE_013_MULTIPLE_OPERATORS
set_operator OP-L1 5 CTX-OP-L1
printf 'OPERATOR||OP-L2||6||CLASS||SCOPE_OPERATOR||SOURCE||CTX-OP-L2\n' >> "$IN/operators.memory"
add_scope S-ONE 0 10 CTX-ONE
run_vm CASE_013_MULTIPLE_OPERATORS
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'OPERATOR_COUNT' '2'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_OPERATOR_COUNT'
pass_case

# 014: malformed scope record is refused.
prepare_case CASE_014_MALFORMED_SCOPE
set_operator OP-M 5 CTX-OP-M
printf 'SCOPE||BROKEN||0||10||SOURCE\n' > "$IN/scopes.memory"
run_vm CASE_014_MALFORMED_SCOPE
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'INVALID_SCOPE_COUNT' '1'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_INVALID_SCOPE_RECORD'
pass_case

# 015: malformed operator record is refused.
prepare_case CASE_015_MALFORMED_OPERATOR
printf 'OPERATOR||BROKEN||5||CLASS||SCOPE_OPERATOR||SOURCE\n' > "$IN/operators.memory"
add_scope S-ONE 0 10 CTX-ONE
run_vm CASE_015_MALFORMED_OPERATOR
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'OPERATOR_COUNT' '1'
expect_line 'OPERATOR_RECORD_VALID' '0'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_INVALID_OPERATOR_RECORD'
pass_case

# 016: ninth unique scope exceeds bounded capacity atomically.
prepare_case CASE_016_CAPACITY
set_operator OP-N 4 CTX-OP-N
add_scope S1 0 20 C1
add_scope S2 0 19 C2
add_scope S3 0 18 C3
add_scope S4 0 17 C4
add_scope S5 0 16 C5
add_scope S6 0 15 C6
add_scope S7 0 14 C7
add_scope S8 0 13 C8
add_scope S9 0 12 C9
run_vm CASE_016_CAPACITY
expect_line 'INPUT_ACCEPTED' '0'
expect_line 'UNIQUE_SCOPE_COUNT' '9'
expect_line 'SCOPE_CAPACITY_EXCEEDED' '1'
expect_line 'SCOPE_BINDING_STATUS' 'REFUSED_SCOPE_CAPACITY'
pass_case

# 017: opaque high-entropy identities, dynamic coordinates.
prepare_case CASE_017_OPAQUE_DYNAMIC_A
set_operator OP-8f0c72d5 731 SRC-op-2c91
add_scope SC-3f9a91 700 760 SRC-1a4e
add_scope SC-e71b02 724 739 SRC-8dd3
add_scope SC-98c6aa 100 120 SRC-62b9
run_vm CASE_017_OPAQUE_DYNAMIC_A
expect_line 'ENCLOSING_SCOPE_COUNT' '2'
expect_line 'SELECTED_SCOPE_ID' 'SC-e71b02'
expect_line 'SELECTED_SCOPE_WIDTH' '15'
pass_case

# 018: same opaque structural evidence in another encounter order.
prepare_case CASE_018_OPAQUE_DYNAMIC_B
set_operator OP-8f0c72d5 731 SRC-op-2c91
add_scope SC-98c6aa 100 120 SRC-62b9
add_scope SC-e71b02 724 739 SRC-8dd3
add_scope SC-3f9a91 700 760 SRC-1a4e
run_vm CASE_018_OPAQUE_DYNAMIC_B
expect_line 'ENCLOSING_SCOPE_COUNT' '2'
expect_line 'SELECTED_SCOPE_ID' 'SC-e71b02'
expect_line 'CANDIDATE_ENCOUNTER_ORDER_IS_WINNER_POLICY' 'NO'
pass_case

# 019: deterministic replay A in a fresh VM process.
prepare_case CASE_019_REPLAY_A
set_operator OP-R 42 CTX-OP-R
add_scope S-R1 0 100 CTX-R1
add_scope S-R2 40 44 CTX-R2
add_scope S-R3 41 43 CTX-R3
run_vm CASE_019_REPLAY_A
expect_line 'SELECTED_SCOPE_ID' 'S-R3'
expect_line 'SELECTED_SCOPE_WIDTH' '2'
pass_case

# 020: byte-identical input, fresh VM process, replay B.
prepare_case CASE_020_REPLAY_B
set_operator OP-R 42 CTX-OP-R
add_scope S-R1 0 100 CTX-R1
add_scope S-R2 40 44 CTX-R2
add_scope S-R3 41 43 CTX-R3
run_vm CASE_020_REPLAY_B
expect_line 'SELECTED_SCOPE_ID' 'S-R3'
expect_line 'SELECTED_SCOPE_WIDTH' '2'
pass_case

if ! "$P/bin/cmp" -s "$LOG/CASE_019_REPLAY_A.log" "$LOG/CASE_020_REPLAY_B.log"; then
    printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=REPLAY_OUTPUT_MISMATCH\n'
    exit 70
fi

[ "$TOTAL_VM_INVOCATIONS" -eq 20 ] || { printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=INVOCATION_COUNT\n'; exit 71; }
[ "$POST_VM_ALIGNMENT_PASS_COUNT" -eq 20 ] || { printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=PASS_COUNT\n'; exit 72; }
[ "$POST_VM_ALIGNMENT_FAIL_COUNT" -eq 0 ] || { printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=ALIGNMENT_FAIL_COUNT\n'; exit 73; }
[ "$VM_NONZERO_COUNT" -eq 0 ] || { printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=VM_NONZERO_COUNT\n'; exit 74; }
[ "$STEP_LIMIT_HIT_COUNT" -eq 0 ] || { printf 'LANG_02A_PREFLIGHT=FAIL\nFAILURE=STEP_LIMIT_COUNT\n'; exit 75; }

printf '\n=== LANG-02A SUMMARY ===\n'
printf 'TOTAL_VM_INVOCATIONS=%s\n' "$TOTAL_VM_INVOCATIONS"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\n' "$POST_VM_ALIGNMENT_PASS_COUNT"
printf 'POST_VM_ALIGNMENT_FAIL_COUNT=%s\n' "$POST_VM_ALIGNMENT_FAIL_COUNT"
printf 'VM_NONZERO_COUNT=%s\n' "$VM_NONZERO_COUNT"
printf 'STEP_LIMIT_HIT_COUNT=%s\n' "$STEP_LIMIT_HIT_COUNT"
printf 'NEGATIVE_TEST=PASS\n'
printf 'PERSISTENT_STATE=NA\n'
printf 'RESTART_REPLAY_TEST=PASS\n'
printf 'IDENTICAL_INPUT_REPLAY=YES\n'
printf 'NATIVE_SCOPE_BINDING=PASS_IN_PREFLIGHT_SCOPE\n'
printf 'SMALLEST_ENCLOSING_SCOPE_POLICY=NATIVE_MINIMUM_WIDTH\n'
printf 'TIED_MINIMAL_SCOPE_WITHHELD_AS_AMBIGUITY=YES\n'
printf 'NO_ENCLOSING_SCOPE_FABRICATED=NO\n'
printf 'DUPLICATE_SCOPE_DOUBLE_COUNT=NO\n'
printf 'SCOPE_ID_COLLISION_MUTATES_STATE=NO\n'
printf 'CANDIDATE_ENCOUNTER_ORDER_IS_WINNER_POLICY=NO\n'
printf 'SCOPE_CAPACITY=8\n'
printf 'HOST_SCOPE_SELECTION=NO\n'
printf 'HOST_OPERATOR_INTERPRETATION=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_INTERPRETATION=NO\n'
printf 'HOST_POST_VM_TEST_ORACLE_ONLY=YES\n'
printf 'NUMERIC_TEXT_GENERAL_VALIDATION=NOT_PROVEN\n'
printf 'SURFACE_NEGATION_RECOGNITION=NOT_PROVEN\n'
printf 'LOGICAL_NEGATION=NOT_PROVEN\n'
printf 'PROPOSITION_TRUTH=NOT_PROVEN\n'
printf 'SEMANTIC_SCOPE=NOT_PROVEN\n'
printf 'SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'PRODUCTION_STATE_MUTATED=NO\n'
printf 'LANG_02A_PREFLIGHT=PASS\n'
printf 'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
