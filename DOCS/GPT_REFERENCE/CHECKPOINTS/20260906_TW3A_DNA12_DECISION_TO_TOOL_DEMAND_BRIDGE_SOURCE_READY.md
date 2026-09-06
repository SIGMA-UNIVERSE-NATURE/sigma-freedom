# TW3A DNA-12 Decision Contract -> Tool Demand Bridge — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_NOT_YET_PROVEN

## Dependency state

```text
TW1_NATIVE_WEIGHTED_TOOL_ARBITRATION_V1=PASS_IN_EXACT_TESTED_SCOPE
TW2_NATIVE_ACTUAL_CAPABILITY_REGISTRY_BINDING_V1=PASS_IN_EXACT_TESTED_SCOPE
DNA12_NATIVE_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
DNA12_EXACT_NATIVE_SOURCE_BYTES_AVAILABLE_TO_THIS_BUNDLE=NO
DIRECT_DNA12_RUNTIME_BINDING=NOT_PROVEN
```

The artifact-retention limitation and TW3A scope are locked in:

`DOCS/GPT_REFERENCE/CHECKPOINTS/20260906_TW3_DNA12_ABI_RETENTION_AUDIT_TW3A_SCOPE.md`

## Exact bundle identities

```text
BUNDLE_NAME=SIGMA_TW3A_NATIVE_ADMISSION_V1_DNA12_DECISION_TO_TOOL_DEMAND_BRIDGE_BUNDLE.zip
BUNDLE_SHA256=28011cfda28245ddcaad600263aee8aebd4c7fe13fef3f83a914c9ce1ab772f3
TW3A_SOURCE_SHA256=63322defcf6b599bd6a0bdbfd1763d400b5a9bbaae4246ced25f804cf4d594f0
TW3A_RUNNER_SHA256=ecd687615b566874a8a6ce52ee8e571f8d673bb2cf68bb075e2ee3ac39f0f4b3
TW3A_BINDING_SHA256=153014c76b3a1af05446d9be10ff0a3bf12f05275fa512dafb92473aebf43921
MANIFEST_SHA256=b33c668deb56e5ef19af163949c6435387d6fa7ba15413491d326b49547ac9b9
TW2_SOURCE_SHA256=500f24fb457590d89fa7d9dc5c23c84a457b97f035595286d7fdbc0c8e4df109
TW2_CATALOG_SHA256=28810830b6da04bdfe92606f1ffb88ff5b28cc4ff99b81be16f8c0cf08054758
TW1_SOURCE_SHA256=a91420c832c88156cf9dba1e8437931627df3d1a83d2495d16da6edf7d9456da
DNA12_ADMITTED_SOURCE_SHA256_REFERENCE=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
```

Locked runtime identities required by the runner:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Native TW3A contract

Input record:

```text
DNA12_DECISION||RUN_ID||MODE||CANDIDATE_TOOL||TOOL_AVAILABLE||INTERNAL_REASONING_SUFFICIENT||CURRENT_EXTERNAL_STATE||RETRIEVAL||EXACT_COMPUTATION||OBSERVATION_OR_MEASUREMENT||EXTERNAL_ACTION||COMMIT||YES
```

The five demand positions are the five canonical DNA-12 tool-use signal dimensions. TW3A copies them exactly; it does not rewrite them to make a candidate tool fit.

Binding metadata:

```text
BIND||CANDIDATE_TOOL||SCOPE_ID||COMMIT||YES
```

Successful native scope output:

```text
SCOPE||SCOPE_ID||COMMIT||YES
```

Current binding contract contains the four TW2/TW1-ready surfaces:

```text
V4PK4_CONTROLLED_INFERENCE -> CONTROLLED_INFERENCE
V4PK5_COPY_EXACT_BRIDGE -> COPY_EXACT
I3B_V6R1_EVIDENCE_ASSESSOR -> CORPUS_EVIDENCE_ASSESSMENT
I5A_WIKIPEDIA_DISCOVERY -> WIKIPEDIA_DISCOVERY
```

These are static capability bindings, not query-specific semantic decisions. The TW3A `.sigma` source contains none of these actual candidate-tool or scope literals; they are data records in the binding contract.

## Planned runtime admission

```text
PLANNED_TOTAL_VM_INVOCATIONS=23
PLANNED_TW3A_VM_INVOCATIONS=13
PLANNED_TW2_INTEGRATION_VM_INVOCATIONS=5
PLANNED_TW1_INTEGRATION_VM_INVOCATIONS=5
```

Planned coverage:

- Wikipedia discovery binding through TW3A -> TW2 -> TW1;
- corpus evidence-assessment binding through TW3A -> TW2 -> TW1;
- COPY_EXACT action binding through TW3A -> TW2 -> TW1;
- controlled-inference binding through TW3A -> TW2 -> TW1;
- candidate/demand mismatch proving demand is not rewritten to fit the candidate;
- explicit tool-gap visibility with no invented scope;
- unknown candidate HOLD;
- incoherent DNA-12 decision-contract refusal;
- duplicate candidate binding refusal;
- binding reorder invariance;
- dynamic unseen high-entropy candidate/scope binding;
- exact replay;
- source/bytecode anti-hardcode audit;
- locked compiler/VM identity and immutability checks;
- step-limit audit.

## Host boundary

```text
HOST_SCOPE_INFERENCE=NO
HOST_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```

The admission runner supplies explicit structural fixtures only, copies exact native output bytes into TW2/TW1, launches the locked compiler/VM, and performs post-VM structural/oracle checks.

## Claim boundary

```text
TW3A_SOURCE=SOURCE_READY
TW3A_COMPILE=NOT_RUN_ON_USER_MACHINE
TW3A_VM=NOT_RUN_ON_USER_MACHINE
TW3A_ADMISSION=NOT_PROVEN
DIRECT_DNA12_RUNTIME_BINDING=NOT_PROVEN
DNA12_NATIVE_EVENT_ABI_REPLAY=NOT_PROVEN
GENERAL_TOOL_CHOICE_FROM_ARBITRARY_NATURAL_LANGUAGE=NOT_PROVEN
LANG01G_AS_TOOL_INTENT_CLASSIFIER=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
```

Static/source readiness is not runtime capability proof.

## Next on PASS

```text
NEXT_STAGE=TW3B_EXACT_NATIVE_DNA12_RUNTIME_EVENT_BINDING_AFTER_ARTIFACT_RETENTION
```

TW3B must recover/retain the exact admitted native DNA-12 source and runner bytes and replace the TW3A structural decision fixture with exact native DNA-12 runtime output. No host semantic mapper is permitted.
