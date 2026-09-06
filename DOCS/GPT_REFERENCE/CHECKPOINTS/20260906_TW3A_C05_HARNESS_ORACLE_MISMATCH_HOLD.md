# TW3A C05 HARNESS ORACLE MISMATCH — HOLD / REPAIR REQUIRED

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## User-supplied machine evidence

```text
=== C05_UNCOVERED tw1 ===
VM_RC=0
DEMAND_COUNT 1
REGISTRY_VALID 1
REGISTRY_COUNT 1
SELECTED_TOOL_1
SELECTED_TOOL_2 NONE
FINAL_UNCOVERED_DEMAND_COUNT 1
STATE_MUTATED 0
EVENT_EMITTED 0
TW1_STATUS HOLD_NO_ELIGIBLE_TOOL
POST_VM_ALIGNMENT=FAIL
```

## Classification

```text
FAILURE_CLASS=MECHANICAL_HARNESS_ORACLE_MISMATCH
TW1_NATIVE_COGNITIVE_FAILURE=NOT_ESTABLISHED
TW2_NATIVE_COGNITIVE_FAILURE=NOT_ESTABLISHED
TW3A_NATIVE_COGNITIVE_FAILURE=NOT_ESTABLISHED
VM_RC=0
STEP_LIMIT_HIT=NO_EVIDENCE
```

## Root cause

The TW3A admission runner expected:

```text
TW1_STATUS HOLD_UNCOVERED_DEMAND
```

for `C05_UNCOVERED`.

But the C05 fixture binds candidate `I5A_WIKIPEDIA_DISCOVERY` while preserving an exact-computation demand. The resulting one-record TW2 registry contains no tool with positive coverage for that demand dimension. Under admitted TW1 V1 semantics:

- `HOLD_NO_ELIGIBLE_TOOL` is correct when `BEST1_FOUND=0` because no eligible registry record covers any active demand dimension.
- `HOLD_UNCOVERED_DEMAND` applies only after at least one tool is selected but final demand remains uncovered.

The machine output therefore matches TW1 semantics and proves the intended C05 property: demand was not rewritten to make the candidate fit.

## Repair scope

```text
REPAIR=RUNNER_ONLY
TW3A_SIGMA_SOURCE_CHANGE=NO
TW2_SIGMA_SOURCE_CHANGE=NO
TW1_SIGMA_SOURCE_CHANGE=NO
COGNITIVE_POLICY_CHANGE=NO
ORACLE_WEAKENED=NO
```

The runner expectation for C05 must change from `HOLD_UNCOVERED_DEMAND` to `HOLD_NO_ELIGIBLE_TOOL` while retaining the same fixture and the same `DEMAND_NOT_REWRITTEN_TO_FIT_CANDIDATE=PASS` gate.

## Admission state

```text
TW3A_ADMISSION=HOLD_PENDING_FIX1_RERUN
```
