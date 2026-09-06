# TW1 FIX1 Weighted Tool Arbitration — Native Admission PASS

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Status

```text
TW1_NATIVE_WEIGHTED_TOOL_ARBITRATION_V1=PASS
WEIGHTED_TOOL_ARBITRATION=PASS_IN_EXACT_TESTED_SCOPE
RESULT=PASS_IN_EXACT_TESTED_SCOPE
NEXT_STAGE=TW2_ACTUAL_CAPABILITY_REGISTRY_BINDING
```

## Exact artifact identities

```text
BUNDLE_SHA256=7db10a49a07915a49337715dde276c7cbfaa02d629028470d3c9892107b96199
TW1_SOURCE_SHA256=a91420c832c88156cf9dba1e8437931627df3d1a83d2495d16da6edf7d9456da
TW1_RUNNER_SHA256=68e39bf8665f9fef98216aa9bd36bd5c6ab3350f34a65c2baa02e4546f5b8f45
```

## User-supplied machine evidence

```text
TOTAL_VM_INVOCATIONS=15
POST_VM_ALIGNMENT_PASS_COUNT=15
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
WEIGHTED_TOOL_SELECTION=NATIVE_SIGMA_TESTED
TWO_TOOL_COMPOSITION=PASS
REGISTRY_REORDER_INVARIANCE=PASS
AVAILABILITY_AFFECTS_SELECTION=YES
ADMISSION_READINESS_AFFECTS_SELECTION=YES
COST_WEIGHT_AFFECTS_SELECTION=YES
PERSISTENT_PRIOR_USE_AFFECTS_SELECTION=YES
NO_DEMAND_HOLD=TESTED
UNCOVERED_DEMAND_HOLD=TESTED
MALFORMED_REGISTRY_REFUSAL=TESTED
DUPLICATE_REGISTRY_ID_REFUSAL=TESTED
STABLE_REGISTRY_ID_TIEBREAK=PASS
REPLAY_IDENTICAL_SELECTION_OUTPUT=YES
REPLAY_IDENTICAL_EVENT=YES
REPLAY_IDENTICAL_MEMORY=YES
FINAL_SELECTION_RECORD_COUNT=1
FINAL_SELECTION_LEDGER_SHA256=dce5eb7b62fdc864ece000e8bc5e0b74b5c07bd7aa75a7d16544df5dc4da7bdc
REGISTRY_ORDER_USED_AS_WINNER_POLICY=NO
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
HOST_TOOL_COMPOSITION=NO
```

## Admitted scope

This machine run admits bounded native weighted arbitration over a runtime-supplied generic tool registry. Native SIGMA applies demand coverage, base weight, cost, persistent prior-use penalty, eligibility gates, stable registry-ID tie-break, one/two-tool composition, uncovered-demand hold, registry validation, persistence and replay determinism.

No host/GPT tool selection, ranking or composition is part of the active decision path.

## Frontier

TW2 must bind real admitted SIGMA executable capability/tool surfaces into the generic registry without turning host-authored ordering into winner policy. Registry capacity and the distinction between internal cognition modules and externally invokable tool surfaces must be handled explicitly rather than claiming every repository capability fits one TW1 V1 page.
