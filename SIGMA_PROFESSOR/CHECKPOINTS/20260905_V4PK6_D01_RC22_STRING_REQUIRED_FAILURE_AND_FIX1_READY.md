# V4-PK6 Verified Evolution V1 — D01 rc22 failure and Fix1 ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Machine failure evidence

The user-observed locked-device run compiled the V4-PK6 native source successfully and reached the first directed case, then failed immediately:

```text
V4PK6_COMPILE_RC=0
V4PK6_BYTECODE_SHA256=54b38574cb62b7467d9991b134319eaaef7d55a89b57e0d79cdca7a99fc17f40
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
LIVE_V4PK1_DEPENDENCY_RUNTIME=PASS
LIVE_V4PK2_DEPENDENCY_RUNTIME=PASS
LIVE_V4PK4_FORMAL_DEPENDENCY_RUNTIME=PASS
LIVE_V4PK4_COMPLETION_DEPENDENCY_RUNTIME=PASS
V4PK5_ADMITTED_DEPENDENCY_CHECKPOINT=PASS

=== D01_PLAN_APPLY ===
VM_RC=22
SIGMA host: string required
POST_VM_ALIGNMENT=FAIL
```

Therefore:

```text
V4PK6_V1_ADMISSION=FAIL
V4PK6_RESULT=NOT_ADMITTED
V5_EXTERNAL_KNOWLEDGE_ACQUISITION_UNLOCKED=NO
```

## Control-flow diagnosis

The V1 runner removed several optional text paths before each transaction:

- `state/transaction.memory`
- `state/evolution_event.txt`
- `io/before.txt`
- `io/trial.txt`
- `io/after.txt`

The native source reads these paths before phase-specific work. A missing-file read under the locked host ABI can yield a non-string / NULL-like value, while the source later applies string parsing to journal/trial/after state. This is consistent with the observed `SIGMA host: string required` failure.

This is a root-cause hypothesis until rerun evidence confirms it.

## Fix1

Native source remains byte-identical:

```text
NATIVE_SOURCE_SHA256=49d1490c34e89f4d9108c7d6e3efcb18bfb1d44668a56c9a63280dc84621fe85
NATIVE_SOURCE_CHANGED=NO
```

Fix1 changes only mechanical harness initialization:

- optional native read targets are explicit zero-byte text files rather than missing paths;
- `clear_event` truncates to empty instead of removing the event file;
- replay reset does the same;
- a mechanical preflight requires all five optional files to exist and be empty before D01;
- no evolution decision, test decision, commit/rollback decision, threshold, authorization policy, or evidence gate moves into Bash.

Fix1 bundle identity prepared by the teaching session:

```text
BUNDLE_SHA256=0ccdc6e6000aea6c4f0f74455ed34b44183e948bc68a954543e931bd9f6fb505
RUNNER_SHA256=ffff7c0282c8cf4036b9672d7f0f4b73cf4dda7b5b986039c0d71b07a5302429
NATIVE_SOURCE_SHA256=49d1490c34e89f4d9108c7d6e3efcb18bfb1d44668a56c9a63280dc84621fe85
BASH_SYNTAX=PASS
TOTAL_PLANNED_VM_INVOCATIONS=50
```

## Governance

```text
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_EVOLUTION_DECISION=NO
HOST_TEST_DECISION=NO
HOST_COMMIT_ROLLBACK_DECISION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
FAILURE_IS_EVIDENCE=YES
GATE_WEAKENED=NO
```

If Fix1 still produces `VM_RC=22`, the hypothesis is falsified and the failure remains evidence. Do not weaken the admission gate.
