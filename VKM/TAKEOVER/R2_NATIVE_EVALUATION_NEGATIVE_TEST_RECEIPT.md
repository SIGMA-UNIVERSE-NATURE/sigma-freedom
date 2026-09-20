# SIGMA VKM R2 — Native Evaluation Negative-Test Receipt

## Status

R2_WORKSPACE_WRITABLE=YES
R2_TRUE_INVALID_CANDIDATE_REJECT=PASS
UNKNOWN_PREDICATE_REJECT=PASS
REJECT_CANONICAL_MUTATION=NO
READY_FOR_R2_TEST_B=YES
TERMUX_SHELL_CONTINUES=YES

## Evaluator receipt

SCHEMA=SIGMA_VKM_NATIVE_EVALUATION_R2
CANONICAL_RELATIONS=52
CANDIDATE_RELATIONS=53
ADDED_RELATIONS=1
DELETED_RELATIONS=0
UNKNOWN_PREDICATES=1
INVALID_LINES=0
DECISION=REJECT
RESULT=PASS
EVALUATOR_RC=0

## Canonical immutability proof

CANONICAL_BEFORE=49d2f7ced9280e9b3f9fc86993420314f25ea8f4355b2ee957dd05489a6b90a6
CANONICAL_AFTER=49d2f7ced9280e9b3f9fc86993420314f25ea8f4355b2ee957dd05489a6b90a6

The deliberately invalid candidate added one relation containing UNKNOWN_R2_PREDICATE. The native evaluator detected one unknown predicate, rejected the candidate, returned RC=0 for the completed evaluation, and canonical state remained byte-identical by SHA-256.

## Evidence identities

- canonical.memory: 49d2f7ced9280e9b3f9fc86993420314f25ea8f4355b2ee957dd05489a6b90a6
- candidate_bad.memory: 12d45764ad6e72782a8f6cd8c54f58dd6ffc5df7fcae7ad5cfd242974acd3dc7
- bad.evaluate: 9ca2717ffaa2c5ad3fb4d9d550596224fed92b2059bde51261a7edc6b5629b74

## Important correction captured in evidence

The first attempted bad-candidate append failed with Permission denied, so that preliminary run contained 52 candidate relations, zero additions and zero unknown predicates. It is not used as proof of unknown-predicate rejection.

The candidate was then rebuilt via a writable temporary file, verified at 53 lines with UNKNOWN_R2_PREDICATE present, moved into place, made read-only, and the true negative test was rerun successfully.

## Takeover boundary

This receipt proves the R2 native evaluator's negative path: detection and rejection of an unknown predicate without canonical mutation. It does not yet prove the complete R2 evaluation/rollback capability and therefore does not migrate EVALUATION_OWNER or ROLLBACK_OWNER yet.

NEXT=R2_TEST_B
