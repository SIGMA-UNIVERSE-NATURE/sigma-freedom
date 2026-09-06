# SIGMA TW1 — Native Weighted Tool Arbitration — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Purpose

Return the active Teacher-GPT work to the primary SIGMA-support axis: native weighted arbitration over a generic tool/capability registry, followed later by actual-capability registry binding and language-state integration.

TW1 is not an evidence-weight capability and is not V4-PK2. It is an operational tool-selection capability.

## Reused admitted/reference context

- V4-A.1 native productivity work arbiter is admitted in bounded tested scope, but arbitrates work-source classes (`RECEIVED`, `RETRYABLE`, `LOCAL`, `FETCH`) rather than a generic weighted tool registry.
- Historical DNA-12 Tool Intelligence preserves useful design intent (tool-use signals; tool output not automatically true), but its Python implementation is historical reference only and is not active SIGMA cognition.
- Language lane currently has LANG-01A..LANG-01G admitted in exact bounded structural scopes, with LANG-02A source ready/not admitted. TW1 does not yet derive tool demand from language states.

## Artifact identities

```text
BUNDLE_NAME=SIGMA_TW1_NATIVE_ADMISSION_V1_WEIGHTED_TOOL_ARBITRATION_BUNDLE.zip
BUNDLE_SHA256=b974f085dc1559457f51fdcdbfa94a887e9f82384cbe24c7190ae9b2c990f201
TW1_SOURCE_SHA256=3172fe929ca5808d3fee3b354cb497d535edfab827211e15f16a8498bcd43474
TW1_RUNNER_SHA256=9ef388f6c7f735e8333f2ae33b40961f45754a06a289017b94bd4c31d7015a83
LOCKED_SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
LOCKED_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Generic runtime registry contract

```text
TOOL||REGISTRY_ID||TOOL_ID||AVAILABLE||ADMITTED||
CURRENT_EXTERNAL_STATE||RETRIEVAL||EXACT_COMPUTATION||
OBSERVATION_MEASUREMENT||EXTERNAL_ACTION||
BASE_WEIGHT_BP||COST_BP||PRIOR_USE_PENALTY_BP||COMMIT||YES
```

The native source contains no current project tool names. Registry order is not a winner policy. Stable numeric `REGISTRY_ID` is the deterministic tie-break.

## Native scoring policy V1

```text
score =
    demanded_capability_coverage * 10000
    + BASE_WEIGHT_BP
    - COST_BP
    - prior_native_selection_count * PRIOR_USE_PENALTY_BP
```

Eligibility requires `AVAILABLE=1` and `ADMITTED=1`.

TW1 may select one or two tools. The second tool can be selected only to cover demand dimensions not covered by the first. Any final uncovered demand causes HOLD.

This is a bounded teacher-authored native operational policy. It is not claimed as a learned weighting policy.

## Planned locked-VM admission

```text
PLANNED_VM_INVOCATIONS=15
```

Coverage includes:

- weighted single-tool selection;
- registry reorder invariance;
- two-tool composition;
- availability gating;
- admission-readiness gating;
- cost-weight changes;
- persistent prior-use penalty changing later selection;
- no-demand HOLD;
- uncovered-demand HOLD;
- malformed registry refusal;
- duplicate stable registry-ID refusal;
- stable registry-ID tie-break;
- identical-prestate replay;
- high-entropy dynamic tool-ID source/bytecode leak audit;
- step-limit scan.

## Host boundary

```text
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
HOST_TOOL_COMPOSITION=NO
REGISTRY_ORDER_USED_AS_WINNER_POLICY=NO
```

Host/shell remains build/identity/fixture/VM/oracle only.

## Deliberately deferred

TW1 does not yet:

- bind every actual current SIGMA capability into the registry;
- derive demand from natural-language input;
- execute selected tools;
- update weights from exact tool-result feedback;
- classify tool output as truth or knowledge.

## Next sequence

```text
TW1 weighted arbitration runtime admission
-> TW2 actual admitted-capability registry binding
-> TW3 native language/cognitive-state -> tool-demand bridge
-> TW4 exact tool-result feedback -> native weighting/history
-> multi-tool execution/composition integration
```

V5K8A external-evidence-content-assessment remains source-ready but is intentionally frozen while this primary SIGMA-support axis is active.
