#!/data/data/com.termux/files/usr/bin/bash
set -u

# ONLINE VERIFICATION: exact R10 shadow execution precheck R1.
# Reads ONLY the exact materialized shadow runner after SHA256 lock.
# No directory walk, no find, no recursive grep, no state/log/archive read,
# no VM/core/cataloger execution, no network, no production write.

ROOT="${1:-$HOME/SIGMA/sigma_genesis1}"
STAGE_ROOT="$ROOT/.sigma_c5v3_sync/C5V3_R10_SUCCESSOR_STAGE_R1"
SHADOW_RUNNER="$STAGE_ROOT/control/RUN_SIGMA_C5V3_R10_SHADOW_R1.sh"
EXPECTED_SHADOW_RUNNER_SHA256="e6aae2cb9d70b57ee5d2e58c0573ab465721289b0b044d77348936d29a2d595d"

hash1() {
  sha256sum "$1" 2>/dev/null | awk '{print $1}'
}

printf '%s\n' '=== C5V3 ONLINE R10 SHADOW EXECUTION PRECHECK R1 ==='
printf 'ROLE=ONLINE_VERIFICATION\n'
printf 'ROOT=%s\n' "$ROOT"
printf 'TARGET=%s\n' "$SHADOW_RUNNER"
printf 'SCOPE=ONE_EXACT_SHADOW_RUNNER_FILE_ONLY\n'
printf 'DIRECTORY_WALK=NO\n'
printf 'FIND=NO\n'
printf 'GREP_RECURSIVE=NO\n'
printf 'STATE_TREE_READ=NO\n'
printf 'LOG_READ=NO\n'
printf 'ARCHIVE_READ=NO\n'
printf 'VM_EXECUTION=NO\n'
printf 'CORE_EXECUTION=NO\n'
printf 'CATALOGER_EXECUTION=NO\n'
printf 'NETWORK=NO\n'
printf 'PRODUCTION_WRITE=NO\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'

if [ ! -f "$SHADOW_RUNNER" ]; then
  printf 'SHADOW_RUNNER_IDENTITY=HOLD_MISSING\n'
  printf 'SHADOW_EXECUTION_PREFLIGHT=HOLD\n'
  printf '%s\n' '=== END ==='
  exit 0
fi

SHA=$(hash1 "$SHADOW_RUNNER")
printf 'SHADOW_RUNNER_SHA256=%s\n' "$SHA"
if [ "$SHA" != "$EXPECTED_SHADOW_RUNNER_SHA256" ]; then
  printf 'SHADOW_RUNNER_IDENTITY=HOLD_MISMATCH\n'
  printf 'SHADOW_EXECUTION_PREFLIGHT=HOLD\n'
  printf '%s\n' '=== END ==='
  exit 0
fi
printf 'SHADOW_RUNNER_IDENTITY=PASS\n'

printf '%s\n' '=== A. EXACT SHARED ROOT REFERENCES ==='
SHARED_NATIVE_COUNT=$(grep -Ec '\$ROOT/\.sigma_native|\$HOME_SIGMA/\.sigma_native|/\.sigma_native/' "$SHADOW_RUNNER" 2>/dev/null || true)
printf 'SHARED_SIGMA_NATIVE_REFERENCE_COUNT=%s\n' "$SHARED_NATIVE_COUNT"
grep -nE '\$ROOT/\.sigma_native|\$HOME_SIGMA/\.sigma_native|/\.sigma_native/' "$SHADOW_RUNNER" 2>/dev/null || true

printf '%s\n' '=== B. EXACT CATALOG CONTRACT LINES ==='
grep -nE 'CATALOG|catalog|archive-root|archive_root|cataloger|knowledge_v2/HEAD|HOME_SIGMA' "$SHADOW_RUNNER" 2>/dev/null || true

printf '%s\n' '=== C. EXACT NETWORK/FETCH CONTRACT LINES ==='
grep -nE 'SEARCH_ENDPOINT|MAX_FETCHES|MIN_FETCH_INTERVAL|FETCH_FAILURE|RATE_LIMIT|fetch_external|dispatch_external_fetch|FETCH_EXTERNAL|FETCH_REVIEW_EVIDENCE|curl|CURL|https?://|gsrsearch|external_request' "$SHADOW_RUNNER" 2>/dev/null || true

printf '%s\n' '=== D. EXACT SHADOW BINDINGS ==='
grep -nE '^(INSTALL|C5|SRC|BIN|BRIDGE|REVIEW_SRC|REVIEW_BIN|REVIEW_BRIDGE|RUNTIME|BASE|STATE_MEM|STATE_DB|CATALOG_DB|EXTERNAL_ROOT|DECODED_ROOT|LOG|LOCK|CATALOG_LOCK|REVIEW_BASE|ERROR_VAULT|REVIEW_REPORT_DIR)=' "$SHADOW_RUNNER" 2>/dev/null || true

printf '%s\n' '=== E. BROAD-TRAVERSAL TOKENS IN ONE FILE ==='
# Static token audit only; nothing here is executed.
BROAD_TOKEN_COUNT=$(grep -Ec 'find[[:space:]]+"?\$HOME_SIGMA|find[[:space:]]+"?\$ROOT|find[[:space:]]+/data/data|grep[[:space:]]+-R|grep[[:space:]]+--recursive|du[[:space:]]+-a|ls[[:space:]]+-R' "$SHADOW_RUNNER" 2>/dev/null || true)
printf 'BROAD_TRAVERSAL_TOKEN_COUNT=%s\n' "$BROAD_TOKEN_COUNT"
grep -nE 'find[[:space:]]+"?\$HOME_SIGMA|find[[:space:]]+"?\$ROOT|find[[:space:]]+/data/data|grep[[:space:]]+-R|grep[[:space:]]+--recursive|du[[:space:]]+-a|ls[[:space:]]+-R' "$SHADOW_RUNNER" 2>/dev/null || true

printf '%s\n' '=== F. DECISION BOUNDARY ==='
printf 'PRECHECK_IS_STATIC_ONLY=YES\n'
printf 'HOST_CAPABILITY_DEMAND_GENERATION=NO\n'
printf 'HOST_TOOL_SELECTION=NO\n'
printf 'HOST_QUERY_GENERATION=NO\n'
printf 'HOST_SOURCE_SELECTION=NO\n'
printf 'HOST_URL_SELECTION=NO\n'
printf 'HOST_REASONING=NO\n'
printf 'HOST_LEARNING=NO\n'
printf 'HOST_SEMANTIC_SUBSTITUTION=NO\n'

if [ "$BROAD_TOKEN_COUNT" -ne 0 ]; then
  printf 'SHADOW_EXECUTION_PREFLIGHT=HOLD_BROAD_TRAVERSAL_TOKEN_PRESENT\n'
elif [ "$SHARED_NATIVE_COUNT" -ne 0 ]; then
  printf 'SHADOW_EXECUTION_PREFLIGHT=HOLD_SHARED_SIGMA_NATIVE_REFERENCE_PRESENT\n'
else
  printf 'SHADOW_EXECUTION_PREFLIGHT=REQUIRES_CATALOG_NETWORK_RECONCILIATION\n'
fi

printf 'C5V3_NATIVE_CAPABILITY_UTILIZATION_EXECUTION=NO_FROM_PRECHECK_ALONE\n'
printf 'PRODUCTION_BINDING=NO\n'
printf 'PRODUCTION_MUTATION=NO\n'
printf '%s\n' '=== END ==='
