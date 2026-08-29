#!/usr/bin/env bash
set -euo pipefail

EXPECTED_COMPILER_SHA256="65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71"
EXPECTED_VM_SHA256="029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99"

ROOT_MARKER="BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_J4_SEMANTIC_RUNTIME"
PACK="$ROOT_MARKER/13_RUNTIME_REOPEN_20260829"
RUN_ONE="$PACK/run_one_capture.sh"
OUTPUT_BASE="$PACK/RAW_PHASE1"

if [ ! -f "./native/sigmac" ] || [ ! -f "./native/sigma-vm.v09_candidate" ]; then
    printf 'Run from ~/SIGMA/sigma_genesis1; required native binaries are absent in %s\n' "$PWD" >&2
    exit 66
fi

if [ ! -f "$RUN_ONE" ]; then
    printf 'J4 execution pack is absent: %s\n' "$RUN_ONE" >&2
    exit 66
fi

COMPILER_SHA256="$(sha256sum ./native/sigmac | awk '{print $1}')"
VM_SHA256="$(sha256sum ./native/sigma-vm.v09_candidate | awk '{print $1}')"
GATE_ID="$(date +%Y%m%d_%H%M%S)_$$"
GATE_DIR="$PACK/GATES"
GATE_RECORD="$GATE_DIR/gate_${GATE_ID}.txt"
mkdir -p "$GATE_DIR" "$OUTPUT_BASE" .sigma_exec

if [ "$COMPILER_SHA256" = "$EXPECTED_COMPILER_SHA256" ] && [ "$VM_SHA256" = "$EXPECTED_VM_SHA256" ]; then
    TOOLCHAIN_MATCH=YES
    CURRENT_RUNTIME_TESTS_AUTHORIZED=YES
    GATE_STATUS=MACHINE_PROVEN
else
    TOOLCHAIN_MATCH=NO
    CURRENT_RUNTIME_TESTS_AUTHORIZED=NO
    GATE_STATUS=HOLD_VERSION_SCOPE_CHANGED
fi

cat >"$GATE_RECORD" <<EOF
GATE_ID=$GATE_ID
COMPILER_PATH=./native/sigmac
EXPECTED_COMPILER_SHA256=$EXPECTED_COMPILER_SHA256
OBSERVED_COMPILER_SHA256=$COMPILER_SHA256
VM_PATH=./native/sigma-vm.v09_candidate
EXPECTED_VM_SHA256=$EXPECTED_VM_SHA256
OBSERVED_VM_SHA256=$VM_SHA256
CURRENT_TOOLCHAIN_IDENTITY_MATCH=$TOOLCHAIN_MATCH
CURRENT_RUNTIME_TESTS_AUTHORIZED=$CURRENT_RUNTIME_TESTS_AUTHORIZED
STATUS=$GATE_STATUS
SIGMA_SOURCE_IMPLEMENTATION_INSPECTED=NO
SIGMA_SOURCE_IMPLEMENTATION_MODIFIED=NO
CURRENT_COMPILER_MODIFIED=NO
CURRENT_VM_MODIFIED=NO
REBUILD_USED=NO
HOST_VM_EMULATION_USED=NO
SYNTHETIC_BYTECODE_CREATED=NO
PRE_VM_EXPECTED_ANSWER_ACCESS=NO
GPT_EXPECTED_MEANING_INJECTED=NO
EOF

if [ "$TOOLCHAIN_MATCH" != YES ]; then
    printf 'CURRENT_TOOLCHAIN_IDENTITY_MATCH=NO\nSTATUS=HOLD_VERSION_SCOPE_CHANGED\nGATE_RECORD=%s\n' "$GATE_RECORD" >&2
    exit 78
fi

SUMMARY="$PACK/phase1_capture_${GATE_ID}.tsv"
printf 'TEST_ID\tRUN_ID\tCOMPILE_RC\tVM_RC\tRECORD_PATH\n' >"$SUMMARY"

run_case() {
    bash "$RUN_ONE" "$@" "$OUTPUT_BASE" | tee -a "$SUMMARY"
}

run_case \
    "J4-B01" \
    "BOOL_LITERAL_RUNTIME" \
    "Does TRUE compile and execute with exact output?" \
    "TRUE_LITERAL_EXACT_CURRENT_RUNTIME" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/02_BOOL_TESTS/J4_BOOL_TRUE_DIRECT.sigma" \
    "Direct TRUE binding and print in this exact source." \
    "Internal BOOL type, general truthiness, and lowercase spellings." \
    "Only comparison output printed TRUE; direct literal runtime remained unproven."

run_case \
    "J4-B02" \
    "BOOL_LITERAL_RUNTIME" \
    "Does FALSE compile and execute with exact output?" \
    "FALSE_LITERAL_EXACT_CURRENT_RUNTIME" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/02_BOOL_TESTS/J4_BOOL_FALSE_DIRECT.sigma" \
    "Direct FALSE binding and print in this exact source." \
    "Internal BOOL type, general truthiness, and lowercase spellings." \
    "FALSE was grounded but direct current literal runtime remained unproven."

run_case \
    "J4-B03" \
    "BOOL_LITERAL_RUNTIME" \
    "Can TRUE serve directly as an IF condition?" \
    "TRUE_LITERAL_IF_CONDITION_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/02_BOOL_TESTS/J4_BOOL_TRUE_IF.sigma" \
    "TRUE used directly in one parenthesized IF condition." \
    "Universal IF truth rules and internal BOOL representation." \
    "Comparison conditions do not establish direct literal condition behavior."

run_case \
    "J4-B04" \
    "BOOL_LITERAL_RUNTIME" \
    "Can FALSE serve directly as an IF condition?" \
    "FALSE_LITERAL_IF_CONDITION_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/02_BOOL_TESTS/J4_BOOL_FALSE_IF.sigma" \
    "FALSE used directly in one parenthesized IF condition." \
    "Universal IF truth rules and internal BOOL representation." \
    "Comparison conditions do not establish direct literal condition behavior."

run_case \
    "J4-N01" \
    "LOWERCASE_NULL_RUNTIME" \
    "What is uppercase NULL behavior in the matched source context?" \
    "NULL_MATCHED_CONTROL_UPPER_EXACT_CASE" \
    "EXECUTION_OBSERVED_EXACT_CASE" \
    "$ROOT_MARKER/03_NULL_TESTS/J4_NULL_UPPER_MATCHED.sigma" \
    "Uppercase NULL in the matched print context." \
    "Internal NULL representation and all NULL contexts." \
    "Inherited uppercase and lowercase runs were not preserved as one newly matched source pair."

run_case \
    "J4-N02" \
    "LOWERCASE_NULL_RUNTIME" \
    "What is lowercase null behavior in the matched source context?" \
    "NULL_MATCHED_CONTROL_LOWER_EXACT_CASE" \
    "EXECUTION_OBSERVED_EXACT_CASE" \
    "$ROOT_MARKER/03_NULL_TESTS/J4_NULL_LOWER_MATCHED.sigma" \
    "Lowercase null in the matched print context." \
    "Universal lowercase mapping and internal symbol representation." \
    "Inherited uppercase and lowercase runs were not preserved as one newly matched source pair."

run_case \
    "J4-L01" \
    "AND_OR_ACTIVE_RUNTIME" \
    "Does grounded symbolic && compile and execute?" \
    "AND_ACCEPTED_SURFACE_AND_EXACT_RUNTIME" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/04_LOGICAL_TESTS/J4_LOGICAL_AND_SYMBOLIC.sigma" \
    "Exact symbolic && expression using grounded comparisons." \
    "General logical family, operand compatibility, precedence, and short-circuit." \
    "Uppercase AND rejection does not decide the grounded symbolic candidate."

run_case \
    "J4-L02" \
    "AND_OR_ACTIVE_RUNTIME" \
    "Does grounded symbolic || compile and execute?" \
    "OR_ACCEPTED_SURFACE_AND_EXACT_RUNTIME" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/04_LOGICAL_TESTS/J4_LOGICAL_OR_SYMBOLIC.sigma" \
    "Exact symbolic || expression using grounded comparisons." \
    "General logical family, operand compatibility, precedence, and short-circuit." \
    "Uppercase OR rejection does not decide the grounded symbolic candidate."

run_case \
    "J4-E01" \
    "EVALUATION_ORDER" \
    "Which marker executes first for two binary operands?" \
    "BINARY_OPERAND_ORDER_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/05_EVALUATION_ORDER_TESTS/J4_EVAL_BINARY.sigma" \
    "One subtraction expression with two source-defined marker calls." \
    "Universal operand order across operators and contexts." \
    "Source order and AST appearance are not runtime evaluation-order evidence."

run_case \
    "J4-E02" \
    "EVALUATION_ORDER" \
    "In what order are two function arguments evaluated?" \
    "FUNCTION_ARGUMENT_ORDER_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/05_EVALUATION_ORDER_TESTS/J4_EVAL_ARGUMENTS.sigma" \
    "One two-argument call with two source-defined marker calls." \
    "Universal argument order and higher arities." \
    "Call existence and argument binding do not prove argument evaluation order."

run_case \
    "J4-E03" \
    "EVALUATION_ORDER" \
    "What marker order occurs in one nested expression?" \
    "NESTED_EXPRESSION_ORDER_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/05_EVALUATION_ORDER_TESTS/J4_EVAL_NESTED.sigma" \
    "One nested arithmetic expression with three source-defined marker calls." \
    "Universal nested evaluation rules." \
    "No inherited order-sensitive nested runtime output exists."

run_case \
    "J4-E04" \
    "EVALUATION_ORDER" \
    "Does the nested left call chain complete before the marked other operand?" \
    "CALL_BEFORE_OPERATOR_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/05_EVALUATION_ORDER_TESTS/J4_EVAL_CALL_OPERATOR.sigma" \
    "One nested left call chain combined with a marked right operand." \
    "Universal call/operator sequencing." \
    "Caller continuation evidence does not expose this expression sequencing."

run_case \
    "J4-C01" \
    "COERCION" \
    "What is the exact accepted or rejected reverse mixed-numeric direction?" \
    "MIXED_NUMERIC_DIRECTIONAL_SYMMETRY_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/07_COERCION_TESTS/J4_COERCION_REVERSE_MIXED_NUMERIC.sigma" \
    "Exact expression 1.5 + 1." \
    "INT-to-FLOAT coercion, result type, and general numeric conversion." \
    "The inherited 1 + 1.5 output does not establish reverse direction or conversion."

run_case \
    "J4-F01" \
    "FLOORDIV_COMMENT_BOUNDARY" \
    "What is the exact compiler and runtime treatment of line-leading double slash?" \
    "LINE_LEADING_DOUBLE_SLASH_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/08_FLOORDIV_BOUNDARY_TESTS/J4_FLOORDIV_LINE_LEADING.sigma" \
    "One line-leading double-slash line inside an addressed block." \
    "Universal comment grammar and current runtime FLOORDIV." \
    "Infix rejection and trailing comment-like behavior do not decide line-leading form."

run_case \
    "J4-P01-U" \
    "PRECEDENCE_GAPS" \
    "What output occurs for the ungrouped unary-minus and exponentiation form?" \
    "UNARY_MINUS_VS_EXPONENTIATION_UNGROUPED_EXACT_CASE" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/09_PRECEDENCE_ASSOCIATIVITY_TESTS/J4_PRECEDENCE_UNARY_POWER_UNGROUPED.sigma" \
    "Exact ungrouped expression -2 ** 2." \
    "Precedence conclusion before matched external comparison." \
    "Both surfaces are grounded but their relative precedence remains open."

run_case \
    "J4-P01-L" \
    "PRECEDENCE_GAPS" \
    "What output occurs for the left-grouped unary-minus and exponentiation control?" \
    "UNARY_MINUS_VS_EXPONENTIATION_LEFT_GROUPED_CONTROL" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/09_PRECEDENCE_ASSOCIATIVITY_TESTS/J4_PRECEDENCE_UNARY_POWER_LEFT_GROUPED.sigma" \
    "Exact left-grouped expression (-2) ** 2." \
    "Precedence conclusion before matched external comparison." \
    "Matched grouping output is required to interpret the ungrouped form."

run_case \
    "J4-P01-R" \
    "PRECEDENCE_GAPS" \
    "What output occurs for the right-grouped unary-minus and exponentiation control?" \
    "UNARY_MINUS_VS_EXPONENTIATION_RIGHT_GROUPED_CONTROL" \
    "NOT_PROVEN" \
    "$ROOT_MARKER/09_PRECEDENCE_ASSOCIATIVITY_TESTS/J4_PRECEDENCE_UNARY_POWER_RIGHT_GROUPED.sigma" \
    "Exact right-grouped expression -(2 ** 2)." \
    "Precedence conclusion before matched external comparison." \
    "Matched grouping output is required to interpret the ungrouped form."

cat >"$PACK/phase1_capture_complete_${GATE_ID}.txt" <<EOF
PHASE=J4_PHASE1_UNCONDITIONAL
GATE_RECORD=$GATE_RECORD
SUMMARY=$SUMMARY
TARGETED_EXECUTIONS_REQUESTED=17
SHORT_CIRCUIT_EXECUTIONS_RUN=0
SHORT_CIRCUIT_REASON=DEFERRED_UNTIL_ACCEPTED_LOGICAL_SURFACE_IS_EXTERNALLY_ESTABLISHED
DUPLICATE_CAPABILITY_TESTS_RUN=0
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
PRE_VM_EXPECTED_ANSWER_ACCESS=NO
GPT_EXPECTED_MEANING_INJECTED=NO
EXTERNAL_SEMANTIC_EVALUATION_APPLIED=NO
EOF

printf 'J4_PHASE1_RAW_CAPTURE_COMPLETE=YES\nGATE_RECORD=%s\nSUMMARY=%s\n' "$GATE_RECORD" "$SUMMARY"
