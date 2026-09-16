#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
ROOT="${ROOT:-$HOME/SIGMA/sigma_genesis1}"

printf 'STATIC_PREFLIGHT=START\n'
printf 'BASH_ROLE=MECHANICAL_ONLY\n'
printf 'BASH_LEARNING=NO\n'
printf 'RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME\n'
printf 'GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO\n'
printf 'GIT_PULL_REQUIRED=NO\n'
printf 'GIT_CHECKOUT_REQUIRED=NO\n'

for F in \
  "$HERE/teacher/seal_candidate.sh" \
  "$HERE/canonical/drain_once.sh" \
  "$HERE/canonical/daemon.sh"; do
  [ -f "$F" ] || { echo "STATIC_PREFLIGHT=FAIL_MISSING_FILE:$F"; exit 2; }
  bash -n "$F"
done

[ -f "$ROOT/.sigma_ail/BRAIN_HEAD" ] || { echo 'STATIC_PREFLIGHT=FAIL_OPPO_BRAIN_HEAD_MISSING'; exit 2; }
[ -f "$ROOT/.sigma_ail/MODEL_GENERATION" ] || { echo 'STATIC_PREFLIGHT=FAIL_OPPO_MODEL_GENERATION_MISSING'; exit 2; }
printf 'OPPO_BRAIN_HEAD=%s\n' "$(cat "$ROOT/.sigma_ail/BRAIN_HEAD")"
printf 'OPPO_MODEL_GENERATION=%s\n' "$(cat "$ROOT/.sigma_ail/MODEL_GENERATION")"

grep -Fq 'ONE_CANONICAL_WRITER_AT_A_TIME=YES' "$HERE/CONTRACT.md"
grep -Fq 'HOST_WEIGHT_MERGE=NO' "$HERE/CONTRACT.md"
grep -Fq 'SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES' "$HERE/CONTRACT.md"
grep -Fq 'NATIVE_LEARNING_SOURCE_PATH=' "$HERE/PACKET_FORMAT.md"
grep -Fq 'NATIVE_LEARNING_BYTECODE_PATH=' "$HERE/PACKET_FORMAT.md"
grep -Fq 'NATIVE_DECISION_RECEIPT_PATH=' "$HERE/PACKET_FORMAT.md"
grep -Fq 'HOST_RESULT_DIFFERS_FROM_NATIVE_DECISION' "$HERE/canonical/drain_once.sh"

# Queue host must not directly mutate canonical-control files.
if grep -En '(rm[[:space:]].*WRITER\.lock|rm[[:space:]].*CANONICAL_LEARNER_LEASE|>[[:space:]]*[^#]*BRAIN_HEAD|>[[:space:]]*[^#]*MODEL_GENERATION)' \
  "$HERE/teacher/seal_candidate.sh" "$HERE/canonical/drain_once.sh" "$HERE/canonical/daemon.sh"; then
  echo 'STATIC_PREFLIGHT=FAIL_DIRECT_CANONICAL_CONTROL_MUTATION_PATTERN'
  exit 2
fi

# Runtime staging must not alter the Oppo repo/branch.
if grep -En '(^|[;&|[:space:]])git[[:space:]]+(pull|checkout|reset|merge|rebase)' \
  "$HERE/teacher/seal_candidate.sh" "$HERE/canonical/drain_once.sh" "$HERE/canonical/daemon.sh"; then
  echo 'STATIC_PREFLIGHT=FAIL_GIT_RUNTIME_MUTATION_PATTERN'
  exit 2
fi

# Queue host must not contain generic host-side learning/semantic merge hooks.
if grep -En '(merge_weights|semantic_score|choose_best_candidate|host_accept|host_reject|apply_weight_delta)' \
  "$HERE/teacher/seal_candidate.sh" "$HERE/canonical/drain_once.sh" "$HERE/canonical/daemon.sh"; then
  echo 'STATIC_PREFLIGHT=FAIL_HOST_COGNITION_PATTERN'
  exit 2
fi

echo 'STATIC_PREFLIGHT=PASS'
echo 'OPPO_RUNTIME_PROOF=NATIVE_REPLAY_NOT_RUN_BY_STATIC_PREFLIGHT'
echo 'MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_BY_STATIC_PREFLIGHT'
