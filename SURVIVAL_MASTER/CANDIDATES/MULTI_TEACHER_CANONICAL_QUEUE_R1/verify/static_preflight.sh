#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

bash -n "$HERE/teacher/seal_candidate.sh"
bash -n "$HERE/canonical/drain_once.sh"
bash -n "$HERE/canonical/daemon.sh"

grep -Fq 'ONE_CANONICAL_WRITER_AT_A_TIME=YES' "$HERE/CONTRACT.md"
grep -Fq 'HOST_WEIGHT_MERGE=NO' "$HERE/CONTRACT.md"
grep -Fq 'SIGMA_NATIVE_LEARNING_OWNER=YES' "$HERE/CONTRACT.md"

# Fail if executable queue scripts contain obvious direct canonical-control mutation.
if grep -En '(rm[[:space:]].*WRITER\.lock|rm[[:space:]].*CANONICAL_LEARNER_LEASE|>[[:space:]]*[^#]*BRAIN_HEAD|>[[:space:]]*[^#]*MODEL_GENERATION)' \
  "$HERE/teacher/seal_candidate.sh" "$HERE/canonical/drain_once.sh" "$HERE/canonical/daemon.sh"; then
  echo 'STATIC_PREFLIGHT=FAIL_DIRECT_CANONICAL_CONTROL_MUTATION_PATTERN'
  exit 2
fi

# Queue host must not contain generic semantic merge/score implementation hooks.
if grep -En '(merge_weights|semantic_score|choose_best_candidate|host_accept|host_reject)' \
  "$HERE/teacher/seal_candidate.sh" "$HERE/canonical/drain_once.sh" "$HERE/canonical/daemon.sh"; then
  echo 'STATIC_PREFLIGHT=FAIL_HOST_COGNITION_PATTERN'
  exit 2
fi

echo 'STATIC_PREFLIGHT=PASS'
echo 'OPPO_RUNTIME_PROOF=NOT_RUN_BY_STATIC_PREFLIGHT'
echo 'MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_BY_STATIC_PREFLIGHT'
