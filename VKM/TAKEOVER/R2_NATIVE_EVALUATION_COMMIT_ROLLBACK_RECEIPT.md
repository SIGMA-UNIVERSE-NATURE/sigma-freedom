# SIGMA VKM R2 — Native Evaluation / Commit / Rollback Receipt

## Final gate

SIGMA_R2_NATIVE_EVALUATION_COMMIT_ROLLBACK=PASS
READY_TO_FINALIZE_R2_OWNERSHIP=YES
CURRENT_GENERATION=3
TERMUX_SHELL_CONTINUES=YES

## Test B — valid candidate

BASE_GENERATION=2
BASE_CANONICAL_SHA256=49d2f7ced9280e9b3f9fc86993420314f25ea8f4355b2ee957dd05489a6b90a6

SCHEMA=SIGMA_VKM_NATIVE_EVALUATION_R2
CANONICAL_RELATIONS=52
CANDIDATE_RELATIONS=53
ADDED_RELATIONS=1
DELETED_RELATIONS=0
UNKNOWN_PREDICATES=0
INVALID_LINES=0
DECISION=ACCEPT
RESULT=PASS
EVALUATOR_RC=0

R2_VALID_CANDIDATE_EVALUATION=PASS

## CAS guard

R2_CANONICAL_CAS=PASS
R2_GENERATION_CAS=PASS

Both canonical SHA-256 and generation remained equal to their captured base values immediately before commit.

## Native accept / commit

R2_NATIVE_ACCEPT_COMMIT=PASS
NEW_GENERATION=3
NEW_CANONICAL_SHA256=61ed6a6d8316a35c5b62093cb050cb75a1662b22d3a71fd26bd63f4136296320

The pre-commit canonical state was snapshotted before replacement. The committed canonical SHA-256 matched candidate_good.memory.

## Post-commit verification

SCHEMA=SIGMA_VKM_NATIVE_EVALUATION_R2
CANONICAL_RELATIONS=52
CANDIDATE_RELATIONS=53
ADDED_RELATIONS=1
DELETED_RELATIONS=0
UNKNOWN_PREDICATES=0
INVALID_LINES=0
DECISION=ACCEPT
RESULT=PASS

R2_POST_COMMIT_VERIFY=PASS

## Rollback self-test

Rollback was tested on a disposable mirror of the committed canonical state. A corruption marker was injected, producing a different SHA-256; restoration from the mirror snapshot then restored the expected SHA-256.

R2_ROLLBACK_SELFTEST=PASS

## Current state identities

- canonical.memory: 61ed6a6d8316a35c5b62093cb050cb75a1662b22d3a71fd26bd63f4136296320
- generation.txt: 1121cfccd5913f0a63fec40a6ffd44ea64f9dc135c66634ba001d10bcf4302a2
- candidate_good.memory: 61ed6a6d8316a35c5b62093cb050cb75a1662b22d3a71fd26bd63f4136296320
- pre_commit.snapshot: 49d2f7ced9280e9b3f9fc86993420314f25ea8f4355b2ee957dd05489a6b90a6

## Scope / ownership boundary

Together with the previously recorded R2 negative-path receipt, this evidence establishes:
- invalid candidate / unknown predicate rejection without canonical mutation;
- valid candidate native evaluation and acceptance;
- canonical + generation CAS guards;
- native accept/commit to generation 3;
- post-commit verification;
- rollback restoration mechanics demonstrated on a disposable mirror.

The execution output states READY_TO_FINALIZE_R2_OWNERSHIP=YES. This receipt records that gate. A separate ownership-finalization record should perform the actual R2 ownership transition so the transition remains explicit and non-duplicative.
