# SIGMA I4 Fix2 — wrong-action preselection contract failure

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: RUNTIME_FAIL_AT_D11 / NATIVE_PRESELECTION_BEFORE_ACTION_GATE

## User machine evidence

Fix2 progressed through canonical and dynamic runtime cases at least through D10, proving the previous VM_RC=6 type-boundary hypothesis was repaired sufficiently for I4 native execution to continue.

Observed tail:

```text
=== D10_MALFORMED ===
VM_RC=0
CATALOG_VALID 0
SELECTED_SOURCE_FAMILY
I4_STATUS REFUSE_INVALID_CATALOG
STATE_MUTATED 0
EVENT_EMITTED 0
POST_VM_ALIGNMENT=PASS

=== D11_WRONG_ACTION ===
VM_RC=0
RESEARCH_ACTION CONTINUE_RESEARCH
RESEARCH_STRATEGY EXTEND_EVIDENCE
CATALOG_VALID 1
SELECTED_FAMILY_ID 17
SELECTED_SOURCE_FAMILY SRC_B_20426828
I4_STATUS HOLD_NOT_DISPATCHED
STATE_MUTATED 0
EVENT_EMITTED 0
POST_VM_ALIGNMENT=FAIL
```

## Root cause

The Fix2 native source computes `select_family(CATALOG_TEXT)` before checking that the incoming research action/strategy are exactly:

```text
DIVERSIFY_EVIDENCE_SOURCE
SOURCE_DIVERSITY
```

Therefore an invalid/wrong action still causes SIGMA to compute and expose a candidate source family, even though the state is not mutated and no event is emitted.

The admission contract intentionally requires **no source-family selection at all** outside the valid I4 dispatch gate.

```text
ROOT_CAUSE=NATIVE_SELECTION_EVALUATED_BEFORE_ACTION_STRATEGY_GATE
FAILURE_CLASS=NATIVE_CONTROL_FLOW_CONTRACT
HOST_SOURCE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
I4_COGNITIVE_POLICY_RANKING_FAILURE=NO
I4_ACTION_GATE_ENFORCEMENT_FAILURE=YES
```

## Repair discipline

Fix3 must move source-family selection evaluation behind the exact action/strategy gate:

```text
present RUN_ID
AND ACTION=DIVERSIFY_EVIDENCE_SOURCE
AND STRATEGY=SOURCE_DIVERSITY
AND catalog valid
-> only then call native select_family()
```

For wrong action/strategy:

```text
SELECTED_SOURCE_FAMILY=<empty>
STATE_MUTATED=0
EVENT_EMITTED=0
I4_STATUS=HOLD_NOT_DISPATCHED
```

Do not weaken D11 oracle. Do not alter canonical catalog. Do not add a canonical expected selected family. Do not change source-family ranking policy.

## Proof state

```text
I4_FIX2_COMPILE=PASS
I4_FIX2_BYTECODE_SHA256=40e55ebe56210482e8ef16c6bec0f17c6101a2f97a385f17d527db4c5f60b8d3
I3C_CANONICAL_REPLAY=PASS
I4_FIX2_CANONICAL_AND_DYNAMIC_RUNTIME_PROGRESS=OBSERVED_THROUGH_D10
I4_FIX2_D11=FAIL
I4_ADMISSION=NOT_PROVEN
NATIVE_SOURCE_FAMILY_SELECTION=NOT_PROVEN
```
