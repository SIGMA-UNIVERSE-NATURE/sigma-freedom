# TW2 Actual Capability Registry Binding — Source Ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Dependency

TW1 FIX1 is machine-admitted:

```text
TW1_NATIVE_WEIGHTED_TOOL_ARBITRATION_V1=PASS
WEIGHTED_TOOL_ARBITRATION=PASS_IN_EXACT_TESTED_SCOPE
TOTAL_VM_INVOCATIONS=15
POST_VM_ALIGNMENT_PASS_COUNT=15
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
TWO_TOOL_COMPOSITION=PASS
REGISTRY_REORDER_INVARIANCE=PASS
PERSISTENT_PRIOR_USE_AFFECTS_SELECTION=YES
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
HOST_TOOL_COMPOSITION=NO
```

TW1 exact source:
`a91420c832c88156cf9dba1e8437931627df3d1a83d2495d16da6edf7d9456da`

TW1 PASS checkpoint:
`DOCS/GPT_REFERENCE/CHECKPOINTS/20260906_TW1_FIX1_WEIGHTED_TOOL_ARBITRATION_PASS.md`

## Native DNA-12 dependency discovery

The repository also contains admitted native DNA-12 Tool Intelligence:

```text
DNA12_SOURCE_SHA256=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
DNA12_BYTECODE_SHA256=7dc7cceab5442938a0846c811e98e8c367ab6beedfdefc7c281355f305f7fe70
DNA12_TOTAL_VM_INVOCATIONS=56
DNA12_ADMISSION=PASS
```

Its bounded runtime scope already handles native tool-use signals, tool/evidence gap modes, dynamic candidate-tool binding, and classifies supplied tool output as unverified evidence rather than automatic truth.

TW3 should reuse this native capability rather than recreate historical Python DNA-12 cognition.

## TW2 artifact identities

```text
BUNDLE_NAME=SIGMA_TW2_NATIVE_ADMISSION_V1_ACTUAL_CAPABILITY_REGISTRY_BINDING_BUNDLE.zip
BUNDLE_SHA256=3d0fdd94afe36c6fdb2aec71b9a8ae79f638156b844200a57ac33b18c796479c
TW2_SOURCE_SHA256=500f24fb457590d89fa7d9dc5c23c84a457b97f035595286d7fdbc0c8e4df109
TW2_RUNNER_SHA256=8bd392dd4916510b67bbbafb589a604479c9d31af3b918a59e5c56f33246e410
TW1_DEPENDENCY_SOURCE_SHA256=a91420c832c88156cf9dba1e8437931627df3d1a83d2495d16da6edf7d9456da
ACTUAL_CATALOG_SHA256=28810830b6da04bdfe92606f1ffb88ff5b28cc4ff99b81be16f8c0cf08054758
```

Repository artifacts:

- `SIGMA_PROFESSOR/artifacts/SIGMA_TW2_NATIVE_ACTUAL_CAPABILITY_REGISTRY_BINDER_V1.sigma`
- `SIGMA_PROFESSOR/artifacts/SIGMA_TW2_SUPPORT_AXIS_CAPABILITY_CATALOG_V1.txt`

## Catalog scope

```text
CATALOG_SCOPE=SUPPORT_AXIS_RELEVANT_V1
ACTUAL_CATALOG_RECORD_COUNT=30
TW1_BINDING_READY_ACTUAL_SURFACE_COUNT=4
FULL_REPOSITORY_CAPABILITY_INVENTORY_COMPLETE=NO
```

The V1 catalog deliberately does not claim to represent every repository file/module. It inventories 30 relevant tool/language/research/knowledge capabilities around the current support axis.

The four actual TW1-ready surfaces are scope-bounded:

```text
CONTROLLED_INFERENCE
COPY_EXACT
CORPUS_EVIDENCE_ASSESSMENT
WIKIPEDIA_DISCOVERY
```

The exact capability identity is not selected by Bash. Native TW2 performs exact catalog validation and exact scope-ID filtering; native TW1 then ranks/composes the emitted eligible registry surfaces.

## Scope-safety rule

TW1's five demand dimensions are too coarse by themselves to safely expose every actual capability for every request.

Therefore TW2 requires exact structural scope-request records:

```text
SCOPE||SCOPE_ID||COMMIT||YES
```

TW2 does not infer scope from natural language.

```text
HOST_SCOPE_INFERENCE=NO
HOST_TOOL_FILTERING=NO
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
SCOPE_REQUEST_OWNER_FOR_FUTURE_RUNTIME=SIGMA_NATIVE_TW3
```

V5-K2 Wikipedia exact fetch remains inventory-only because TW1 V1 does not yet model its required native-selected resource-identity precondition. V5-K3 arXiv remains inventory-only and unadmitted.

## Bootstrap weighting

Every TW2-emitted TW1 registry surface initially receives the same operational bootstrap values:

```text
BASE_WEIGHT_BP=5000
COST_BP=0
PRIOR_USE_PENALTY_BP=500
```

This does not remove TW1 weighting. TW1 already proved dynamic cost/base/prior-use effects. A later feedback stage will replace bootstrap values with native runtime feedback.

## Planned admission

```text
TOTAL_VM_INVOCATIONS=18
TW2_VM_INVOCATIONS=13
TW1_INTEGRATION_VM_INVOCATIONS=5
```

Coverage includes:

- two actual scope surfaces composed through exact admitted TW1;
- catalog reorder invariance;
- actual Wikipedia discovery binding;
- actual corpus evidence-assessment binding;
- actual COPY_EXACT action binding;
- malformed catalog refusal;
- duplicate registry-ID refusal;
- duplicate capability-ID refusal;
- rejection of TW1-ready entries with unknown source identity;
- >32 matching surface HOLD without silent truncation;
- unseen high-entropy capability/scope input;
- byte-identical TW2 replay;
- source/bytecode token leak audit;
- locked runtime identity and step-limit audit.

Expected final status on machine PASS:

```text
TW2_NATIVE_ACTUAL_CAPABILITY_REGISTRY_BINDING_V1=PASS
ACTUAL_CAPABILITY_TO_TW1_REGISTRY=PASS_IN_EXACT_TESTED_SCOPE
RESULT=PASS_IN_EXACT_TESTED_SCOPE
NEXT_STAGE=TW3_DNA12_LANGUAGE_TO_SCOPE_AND_TOOL_DEMAND_BRIDGE
```

## Next support-axis target

TW3 must make native SIGMA emit both:

1. exact TW2 scope-request record(s), and
2. TW1 demand vector.

The intended dependency is native DNA-12 Tool Intelligence plus admitted language/cognitive state. The host may mechanically dispatch exact native outputs but may not infer scope, demand, tool identity, rank or composition.
