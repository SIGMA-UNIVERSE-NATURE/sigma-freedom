# SIGMA I4 Fix1 — runtime RC6 checkpoint

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: COMPILE_PASS / CANONICAL_RUNTIME_FAIL / I4_NOT_ADMITTED

## User machine evidence

```text
I4_COMPILE_RC=0
I4_BYTECODE_SHA256=40e55ebe56210482e8ef16c6bec0f17c6101a2f97a385f17d527db4c5f60b8d3
CANONICAL_SOURCE_FAMILY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
I3C_CANONICAL_REPLAY_VM_RC=0
I3C_EVENT_ORIGIN=SIGMA_NATIVE_VM
I3C_NATIVE_ACTION=DIVERSIFY_EVIDENCE_SOURCE
I3C_NATIVE_STRATEGY=SOURCE_DIVERSITY
HOST_DISPATCHED_EXACT_I3C_EVENT=YES

=== C01_CANONICAL ===
VM_RC=6
POST_VM_ALIGNMENT=FAIL
```

## Classification

The failure occurs after locked compile and successful canonical I3C replay, at the first I4 VM invocation.

```text
FAILURE_CLASS=NATIVE_I4_RUNTIME_FAILURE
I3C_FAILURE=NO
HOST_DISPATCH_FAILURE=NO
I4_COGNITIVE_RESULT=NOT_OBTAINED
NATIVE_SOURCE_FAMILY_SELECTION=NOT_PROVEN
I4_ADMISSION=FAIL_HOLD_PENDING_ROOT_CAUSE_REPAIR
```

No source-family result was emitted before the VM failure, so no source-selection claim is admitted.

## Static root-cause hypothesis

Exact Fix1 source inspection found `select_family()` numerically converts catalog `FAMILY_ID` and `PRIOR_SELECTION_COUNT` via `to_float`, then concatenates those numeric values directly into a string return value:

```text
RETURN BEST_NAME + "|" + BEST_DISC + "|" + BEST_FETCH + "|" + BEST_ID + "|" + BEST_USE;
```

This is a runtime type-boundary defect candidate: the locked VM may not support direct string concatenation with numeric values. The failure occurs before end-of-program prints, which is consistent with a failure inside `select_family()`.

This is currently a hypothesis until the same gate is rerun after a representation-only repair.

```text
ROOT_CAUSE_HYPOTHESIS=STRING_CONCAT_WITH_NUMERIC_SELECTOR_FIELDS
POLICY_CHANGE_REQUIRED=NO
CATALOG_CHANGE_REQUIRED=NO
CANONICAL_ORACLE_CHANGE_REQUIRED=NO
SMALLEST_REPAIR=PRESERVE_TEXT_FOR_SERIALIZATION_AND_NUMERIC_COPY_FOR_COMPARISON
```

## Repair discipline

Fix2 must:

1. preserve the exact I4 source-family selection policy;
2. preserve numeric comparisons for prior count/readiness/stable id;
3. preserve original text forms of family id/prior count for protocol serialization;
4. remove direct numeric-to-string concatenation;
5. keep concrete family names absent from native source/bytecode;
6. keep canonical expected family absent from runner;
7. rerun the same 14-invocation admission plan from clean state.

Keep:

```text
HOST_SOURCE_SELECTION=NO
HOST_CATALOG_RANKING=NO
HOST_RESOURCE_SELECTION=NO
CANONICAL_EXPECTED_SOURCE_FAMILY_PREWRITTEN_IN_RUNNER=NO
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
```
