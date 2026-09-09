#!/data/data/com.termux/files/usr/bin/bash
set -u

# C5V3 exact runner contract extract R1.
# Reads one exact runner file only after hash lock.
# No directory walk, no find, no recursive grep, no state/log read,
# no VM/core execution, no network, no writes except stdout.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
RUNNER="$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh"
EXPECTED_RUNNER_SHA256="092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847"

hash1() {
  sha256sum "$1" 2>/dev/null | awk '{print $1}'
}

printf '%s\n' '=== C5V3 EXACT RUNNER CONTRACT EXTRACT R1 ==='
printf 'ROOT=%s\n' "$ROOT"
printf 'RUNNER=%s\n' "$RUNNER"
printf 'SCOPE=ONE_EXACT_FILE_ONLY\n'
printf 'DIRECTORY_WALK=NO\n'
printf 'FIND=NO\n'
printf 'GREP_RECURSIVE=NO\n'
printf 'STATE_TREE_READ=NO\n'
printf 'LOG_READ=NO\n'
printf 'VM_EXECUTION=NO\n'
printf 'CORE_EXECUTION=NO\n'
printf 'NETWORK=NO\n'
printf 'PRODUCTION_WRITE=NO\n'

printf '%s\n' '=== 1. RUNNER IDENTITY ==='
if [ ! -f "$RUNNER" ]; then
  printf 'RUNNER_IDENTITY=HOLD_MISSING\n'
  printf '%s\n' '=== END ==='
  exit 0
fi
RUNNER_SHA=$(hash1 "$RUNNER")
printf 'RUNNER_SHA256=%s\n' "$RUNNER_SHA"
if [ "$RUNNER_SHA" != "$EXPECTED_RUNNER_SHA256" ]; then
  printf 'RUNNER_IDENTITY=HOLD_MISMATCH\n'
  printf 'CONTRACT_EXTRACTION=SKIPPED_FAIL_CLOSED\n'
  printf '%s\n' '=== END ==='
  exit 0
fi
printf 'RUNNER_IDENTITY=PASS\n'

printf '%s\n' '=== 2. PATH / STATE / LOG BINDING LINES ==='
grep -nE '(^|[^A-Za-z0-9_])(HOME_SIGMA|ROOT|INSTALL|C5|RUNTIME|SIGMAC|VM|SRC|BIN|REVIEW_SRC|REVIEW_BIN|REVIEW_BASE|EXTERNAL_ROOT|DECODED_ROOT|ARCHIVE|LOG|STATE|CURRENT_REQUEST_BYTES)[A-Za-z0-9_]*=|C5_STATE_ROOT|C5_V3_CONTINUOUS|\.sigma_c5|\.sigma_exec' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 3. EXACT FILESYSTEM MUTATION COMMAND LINES ==='
grep -nE '(^|[;&|[:space:]])(mkdir|cp|mv|rm|touch|truncate|tee|cat)[[:space:]]|>[[:space:]]*"?\$|>>[[:space:]]*"?\$' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 4. COMPILER / VM INVOCATION LINES ==='
grep -nE '\$SIGMAC|\$VM|"\$SIGMAC"|"\$VM"|SIGMAC_RC|VM_RC' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 5. LOOP / LIFECYCLE LINES ==='
grep -nE 'while[[:space:]]|until[[:space:]]|for[[:space:]]|sleep[[:space:]]|trap[[:space:]]|exec[[:space:]]|kill[[:space:]]|wait([[:space:]]|$)|exit[[:space:]]' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 6. EXACT INSTALL / C5 / RUNTIME REFERENCES ==='
grep -nE '\$INSTALL|\$C5([^A-Za-z0-9_]|$)|\$RUNTIME|\$SRC([^A-Za-z0-9_]|$)|\$BIN([^A-Za-z0-9_]|$)|\$REVIEW_SRC|\$REVIEW_BIN|\$REVIEW_BASE' "$RUNNER" 2>/dev/null || true

printf '%s\n' '=== 7. DECISION BOUNDARY ==='
printf 'RUNNER_CONTRACT_EXTRACTION=PASS_READ_ONLY_IF_OUTPUT_COMPLETE\n'
printf 'SHADOW_RUNNER_BUILD_NOT_EXECUTED=YES\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
