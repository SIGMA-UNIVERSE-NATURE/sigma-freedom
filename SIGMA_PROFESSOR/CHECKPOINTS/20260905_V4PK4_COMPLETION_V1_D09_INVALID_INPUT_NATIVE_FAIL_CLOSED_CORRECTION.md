# V4-PK4 Completion V1 — D09 Invalid-Input Native Lifecycle Correction

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Observed machine evidence

The user ran the V4-PK4 Completion Native Admission V1 bundle on the locked runtime.

Observed D09 output included:

```text
INPUT_CASE_ID=
INPUT_VALID=0
CANDIDATE_EXISTS=1
PREMISE_GRAPH_COMPLETE=1
EVIDENCE_COMPLETE=1
DEPENDENCY_COMPLETE=1
V4PK4C_LIFECYCLE_STATE=SUPPORTED_INFERENCE
WRITE_ATTEMPTED=0
STATE_MUTATED=0
V4PK4C_STATUS=REFUSE_INVALID_INPUT
POST_VM_ALIGNMENT=FAIL
```

## Diagnosis

The refusal status was correct, and no persistent mutation occurred. However the native lifecycle state was still computed from otherwise-valid candidate/dependency evidence and remained `SUPPORTED_INFERENCE` even though the request input itself was invalid.

This violates the intended fail-closed lifecycle contract for invalid evaluation input. Invalid input must not surface an affirmative inference lifecycle classification.

Therefore this is a native source logic defect, not a host-oracle defect.

## Required correction

For V4-PK4 Completion Fix1:

```text
IF INPUT_VALID == 0
THEN V4PK4C_LIFECYCLE_STATE=UNRESOLVED
```

The refusal remains:

```text
V4PK4C_STATUS=REFUSE_INVALID_INPUT
WRITE_ATTEMPTED=0
STATE_MUTATED=0
```

The entire 50-invocation admission suite must be rerun from a clean directory after the native source correction.

## Governance

```text
FAILURE_IS_EVIDENCE=YES
GATE_WEAKENED=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_ORACLE_CORRECT=YES
NATIVE_SOURCE_CORRECTION_REQUIRED=YES
V4PK4_COMPLETION_V1_ADMISSION=FAIL_AT_D09
FULL_V4PK4_CONTROLLED_INFERENCE=NOT_YET_ADMITTED
V4PK5_UNLOCKED=NO
```

No claim is promoted from the failed V1 completion run.
