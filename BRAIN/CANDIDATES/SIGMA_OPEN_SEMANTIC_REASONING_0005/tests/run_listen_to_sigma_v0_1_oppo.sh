#!/data/data/com.termux/files/usr/bin/bash
set -u

ROOT="${SIGMA_ROOT:-$HOME/SIGMA/sigma_genesis1}"
CANDIDATE="BRAIN/CANDIDATES/SIGMA_OPEN_SEMANTIC_REASONING_0005"
SRC="$ROOT/$CANDIDATE/src/sigma_open_semantic_reasoner_v0_1.sigma"
QUESTION_FILE="$ROOT/SIGMA_OPEN_SEMANTIC_QUESTION_INPUT.txt"
BYTECODE="$ROOT/$CANDIDATE/evidence/sigma_open_semantic_reasoner_v0_1.sigmab"
STDOUT_FILE="$ROOT/$CANDIDATE/evidence/SIGMA_OPEN_SEMANTIC_RESPONSE_V0_1.stdout.txt"
STDERR_FILE="$ROOT/$CANDIDATE/evidence/SIGMA_OPEN_SEMANTIC_RESPONSE_V0_1.stderr.txt"
META_FILE="$ROOT/$CANDIDATE/evidence/SIGMA_OPEN_SEMANTIC_RESPONSE_V0_1.machine.txt"

cd "$ROOT" || exit 90
mkdir -p "$ROOT/$CANDIDATE/evidence" || exit 91

printf 'Nhập đúng một câu hỏi thật để nghe SIGMA truy hồi và dựng response capsule:\n> '
IFS= read -r QUESTION

if [ -z "$QUESTION" ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_EMPTY_QUESTION"
    exit 2
fi

printf '%s\n' "$QUESTION" > "$QUESTION_FILE" || exit 3

if grep -Fq -- "$QUESTION" "$SRC"; then
    echo "QUESTION_ABSENT_FROM_SIGMA_SOURCE=FAIL"
    echo "OPEN_SEMANTIC_V0_1=HOLD_QUESTION_FOUND_IN_SOURCE"
    exit 4
fi

echo "QUESTION_ABSENT_FROM_SIGMA_SOURCE=PASS"
echo "QUESTION_SHA256=$(sha256sum "$QUESTION_FILE" | awk '{print $1}')"
echo "SOURCE_SHA256=$(sha256sum "$SRC" | awk '{print $1}')"

COMPILE_ERR="$ROOT/$CANDIDATE/evidence/SIGMA_OPEN_SEMANTIC_RESPONSE_V0_1.compile.stderr.txt"
: > "$COMPILE_ERR"
"$ROOT/native/sigmac" "$SRC" "$BYTECODE" 2> "$COMPILE_ERR"
COMPILE_RC=$?
COMPILE_ERR_BYTES=$(wc -c < "$COMPILE_ERR")

echo "COMPILE_RC=$COMPILE_RC"
echo "COMPILE_STDERR_BYTES=$COMPILE_ERR_BYTES"

if [ "$COMPILE_RC" -ne 0 ] || [ "$COMPILE_ERR_BYTES" -ne 0 ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_COMPILE"
    cat "$COMPILE_ERR"
    exit 5
fi

echo "BYTECODE_SHA256=$(sha256sum "$BYTECODE" | awk '{print $1}')"

: > "$STDOUT_FILE"
: > "$STDERR_FILE"
"$ROOT/native/sigma-hostvm" "$BYTECODE" > "$STDOUT_FILE" 2> "$STDERR_FILE"
RUN_RC=$?
RUN_ERR_BYTES=$(wc -c < "$STDERR_FILE")

echo "RUN_RC=$RUN_RC"
echo "RUN_STDERR_BYTES=$RUN_ERR_BYTES"

if [ "$RUN_RC" -ne 0 ] || [ "$RUN_ERR_BYTES" -ne 0 ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_RUNTIME"
    cat "$STDERR_FILE"
    exit 6
fi

echo "STDOUT_SHA256=$(sha256sum "$STDOUT_FILE" | awk '{print $1}')"
echo "===== SIGMA RAW OUTPUT BEGIN ====="
cat "$STDOUT_FILE"
echo "===== SIGMA RAW OUTPUT END ====="

STATUS=$(awk '$1=="CANDIDATE_RESPONSE_STATUS" {sub(/^CANDIDATE_RESPONSE_STATUS /,""); print; exit}' "$STDOUT_FILE")
TOP_COUNT=$(awk '$1=="TOP_CANDIDATE_COUNT" {print $2; exit}' "$STDOUT_FILE")
SOURCE_PATH=$(awk '$1=="EVIDENCE_SOURCE" {sub(/^EVIDENCE_SOURCE /,""); print; exit}' "$STDOUT_FILE")
EVIDENCE_LINE=$(awk '$1=="EVIDENCE_LINE" {sub(/^EVIDENCE_LINE /,""); print; exit}' "$STDOUT_FILE")
VALUE=$(awk '$1=="CANDIDATE_RESPONSE_VALUE" {sub(/^CANDIDATE_RESPONSE_VALUE /,""); print; exit}' "$STDOUT_FILE")

EVIDENCE_BINDING="NOT_APPLICABLE"
if [ "${TOP_COUNT:-0}" = "1" ] && [ -n "${SOURCE_PATH:-}" ] && [ -n "${EVIDENCE_LINE:-}" ]; then
    if [ -f "$ROOT/$SOURCE_PATH" ] && grep -Fqx -- "$EVIDENCE_LINE" "$ROOT/$SOURCE_PATH"; then
        EVIDENCE_BINDING="PASS"
    else
        EVIDENCE_BINDING="FAIL"
    fi
fi

{
    echo "QUESTION_SHA256=$(sha256sum "$QUESTION_FILE" | awk '{print $1}')"
    echo "SOURCE_SHA256=$(sha256sum "$SRC" | awk '{print $1}')"
    echo "BYTECODE_SHA256=$(sha256sum "$BYTECODE" | awk '{print $1}')"
    echo "STDOUT_SHA256=$(sha256sum "$STDOUT_FILE" | awk '{print $1}')"
    echo "COMPILE_RC=$COMPILE_RC"
    echo "COMPILE_STDERR_BYTES=$COMPILE_ERR_BYTES"
    echo "RUN_RC=$RUN_RC"
    echo "RUN_STDERR_BYTES=$RUN_ERR_BYTES"
    echo "CANDIDATE_RESPONSE_STATUS=${STATUS:-MISSING}"
    echo "TOP_CANDIDATE_COUNT=${TOP_COUNT:-MISSING}"
    echo "CANDIDATE_RESPONSE_VALUE=${VALUE:-MISSING}"
    echo "EVIDENCE_BINDING=$EVIDENCE_BINDING"
    echo "GENERAL_LANGUAGE_UNDERSTANDING=HOLD_NOT_PROVEN"
    echo "SELF_GENERATED_DESIRE=HOLD_NOT_PROVEN"
} | tee "$META_FILE"

if [ "$EVIDENCE_BINDING" = "FAIL" ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_EVIDENCE_BINDING_FAILURE"
    exit 7
fi

if [ "${STATUS:-}" = "EVIDENCE_BOUND_SINGLE_CANDIDATE" ] && [ "$EVIDENCE_BINDING" = "PASS" ]; then
    echo "OPEN_SEMANTIC_V0_1=PASS_WITH_DEFINED_SCOPE_EVIDENCE_BOUND_RESPONSE_CAPSULE"
    echo "SIGMA_OPEN_SEMANTIC_RESPONSE_V0_1_MACHINE_PASS"
    exit 0
fi

if [ "${STATUS:-}" = "HOLD_AMBIGUOUS_TOP_CANDIDATES" ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_AMBIGUITY_PRESERVED"
    exit 8
fi

if [ "${STATUS:-}" = "HOLD_NO_MATCHED_EVIDENCE" ]; then
    echo "OPEN_SEMANTIC_V0_1=HOLD_UNKNOWN_PRESERVED"
    exit 9
fi

echo "OPEN_SEMANTIC_V0_1=HOLD_UNCLASSIFIED_RESULT"
exit 10
