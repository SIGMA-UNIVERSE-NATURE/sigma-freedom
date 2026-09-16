#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
fail(){ printf 'STATIC_AUDIT=FAIL\nREASON=%s\n' "$1"; exit 2; }
cd "$HERE"

find . -type f -name '*.sh' -print0 | sort -z | while IFS= read -r -d '' f; do bash -n "$f" || exit 91; done || fail SHELL_SYNTAX
python3 - <<'PYCODE' || fail PYTHON_SYNTAX
from pathlib import Path
for p in sorted(Path('host').glob('*.py')):
    compile(p.read_bytes(), str(p), 'exec')
PYCODE

# Historical runtime answer tokens must never be embedded in active native/host code.
if grep -R -n -E '(^|[^A-Za-z])(19378|1373231762)([^A-Za-z]|$)|SIGMA_NATIVE_CANONICAL_SELECTED_TITLE=Mind' native host control 2>/dev/null; then
  fail HISTORICAL_SEMANTIC_RESULT_TOKEN_FOUND
fi
# Reject obvious host-side semantic implementation hooks.
if grep -R -n -E 'def[[:space:]]+(rank_relevance|summarize|choose_source|choose_resource|generate_query|decide_truth)|class[[:space:]]+(SemanticRanker|Summarizer)' host control 2>/dev/null; then
  fail HOST_SEMANTIC_IMPLEMENTATION_PATTERN_FOUND
fi
# Canonical mutation commands/lock overrides are forbidden in active scripts.
if grep -R -n -E 'BRAIN_HEAD.*>|MODEL_GENERATION.*>|rm[[:space:]].*WRITER|flock.*writer\.lock' host control 2>/dev/null; then
  fail CANONICAL_MUTATION_PATTERN_FOUND
fi

grep -Fq 'UNRESOLVED_EXACT_NATIVE_CONTROLLER_INTERFACE' host/artifact_worker.sh || fail FAIL_CLOSED_CONTROLLER_INTERFACE_GATE_MISSING
grep -Fq 'SURVIVAL_MASTER_PREFLIGHT_APPROVAL_MISSING' control/start_preflight.sh || fail REVIEW_GATE_MISSING
grep -Fq 'EXACT_NATIVE_DEPENDENCY_RECEIPT_REQUIRED' control/start_preflight.sh || fail DEPENDENCY_GATE_MISSING
grep -Fq 'READ_PLUS_ARTIFACT_WRITE' control/session_guard.sh || fail SESSION_R4_ARTIFACT_ONLY_GUARD_MISSING
grep -Fq 'MAX_REQUESTS_PER_CYCLE=32' host/resource_budget.py || fail RESOURCE_REQUEST_BOUND_MISSING
grep -Fq 'MAX_TOTAL_BYTES_PER_CYCLE=64*1024*1024' host/resource_budget.py || fail RESOURCE_BYTE_BOUND_MISSING
grep -Fq 'DISK_HIGH_WATER_MARK_PERCENT=85.0' host/resource_budget.py || fail RESOURCE_DISK_BOUND_MISSING

printf '%s\n' \
  'STATIC_AUDIT=PASS' \
  'SHELL_SYNTAX=PASS' \
  'NO_HARDCODED_CURRENT_QUERY=PASS' \
  'NO_HARDCODED_CURRENT_EXPECTED_WEBSITE=PASS' \
  'NO_HARDCODED_CURRENT_RESOURCE=PASS' \
  'NO_HARDCODED_CURRENT_SUMMARY=PASS' \
  'NO_HOST_SEMANTIC_RANKER=PASS' \
  'NO_HOST_QUERY_COMPOSER=PASS' \
  'NO_HOST_SOURCE_SELECTOR=PASS' \
  'NO_HOST_SUMMARY_WRITER=PASS' \
  'NO_DEFAULT_CANONICAL_MUTATION=PASS' \
  'RECOVERY_STATE_IS_MECHANICAL_ONLY=PASS' \
  'ONE_WRITER_GUARD_PRESENT=PASS' \
  'SESSION_R4_INTEGRATION_PRESENT=PASS'
