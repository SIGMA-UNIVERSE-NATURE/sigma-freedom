# C5V3 — R4 R1 static PASS / R2 exact-schema native-capability-choice correction

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## R4 R1 operator static audit

Machine output:

```text
LEARNING_STATE_SHA256=05807ba4a1534323c2358a7362af8f4ad370a47a676f61d96d51161113bb11cc
LEARNING_TRANSITIONS_SHA256=cad80440430a8aa83babb4a336050d3089e51242bc5ef74f41d84d8b56166f58
LEARNING_STATE_IDENTITY=PASS
LEARNING_TRANSITIONS_IDENTITY=PASS
LEARNING_STATE_DEF_COUNT=23
LEARNING_TRANSITIONS_DEF_COUNT=12
R4_LEARNING_COMBINED_DEF_COUNT=35
FORBIDDEN_LEFT_EQ_COUNT=0
FORBIDDEN_RIGHT_EQ_COUNT=0
FORBIDDEN_legacy_analyze_segment_COUNT=0
FORBIDDEN_legacy_merge_evidence_COUNT=0
FORBIDDEN_write_text_COUNT=0
FORBIDDEN_read_text_COUNT=0
MAX_DEF_ARITY=6
MULTILINE_DEF_SIGNATURE_COUNT=0
R4_LEARNING_COMBINED_SHA256=f3847c082e27c7fb2cca9f79b6f1963ad5da2205b58e1e410cb54c600598a791
R4_LEARNING_STATIC_GOVERNANCE=PASS
R4_NATIVE_LEARNING_SOURCE_AUDIT=PASS
RUNTIME_ADMISSION=NO
```

R1 static PASS remains valid in exact tested scope.

## Pre-runtime architecture correction

Before runtime admission, two R1 design issues were found:

1. `c5l_field` used substring replacement rather than exact `KEY=VALUE` field parsing.
2. `c5l_capability_registry_select` selected the first admitted capability for a family, which could move capability choice out of native cognition.

R1 is therefore retained as provenance but superseded before runtime admission.

```text
R4_R1_RUNTIME_ADMISSION=NO
R4_R1_ROLE=STATIC_SOURCE_PROVENANCE_ONLY
```

## R4 R2 source target

State R2:

```text
PATH=C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_STATE_R2.sigma.inc
COMMIT=ca6d9504f5e75c4d5ccf48ab7c574614a8b019be
SHA256=83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33
DEF_COUNT=28
```

Transitions R2:

```text
PATH=C5_M5/R4_NATIVE_LEARNING/C5_NATIVE_LEARNING_TRANSITIONS_R2.sigma.inc
COMMIT=3debd57e8f0ac3dce7bba540cb912c0ffbadef29
SHA256=3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9
DEF_COUNT=12
```

Gate-A adapter R2:

```text
PATH=C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R2.sigma.inc
COMMIT=59e656106cd8a5c497ecda2780efa0958a252afa
SHA256=43e22c9b9140dfb0b1882d34d85ffd1e460854f20bd61420f93098052cd0aa89
DEF_COUNT=12
```

Deterministic concatenation identity:

```text
R4_R2_COMBINED_DEF_COUNT=52
R4_R2_COMBINED_SHA256=84d064435fdba01ccd6c700f5efd266b39e297f51fedc7cfddbf9c05489fe209
MAX_DEF_ARITY=6
MULTILINE_DEF_SIGNATURE_COUNT=0
```

## R2 corrections

```text
EXACT_FIELD_SCHEMA=KEY_EQUALS_VALUE_FIXED_ORDER
SAFE_ATOM_REJECTS_EQUALS=YES
RECORD_FIELD_COUNT_EXACT=YES
RECORD_BYTE_BOUNDS=YES
MEMORY_BYTE_BOUND=65536
CAPABILITY_SELECTION_PLANE=NATIVE_SIGMA
SUBSTRATE_CAPABILITY_AUTO_SELECT=NO
SUBSTRATE_CAPABILITY_ID_VALIDATION=YES
DIRECT_READ_TEXT=NO
DIRECT_WRITE_TEXT=NO
LEFT_RIGHT_COGNITION=NO
```

`c5l2_capability_registry_has(registry, capability_id, need_family)` validates a capability ID already supplied by native SIGMA. It does not choose a capability.

## Gate-A adapter scope

The adapter only exposes exact admitted Gate-A narrow behavior into R4 state:

```text
relation-discrimination gap signal
native gap evidence request payload
source-consistency stance
consistent source authority counts
scoped provisional truth posture
competing-configuration incompatibility posture
```

It does not claim general truth, whole-work understanding or arbitrary semantic evaluation.

## Exact next machine action

```text
C5_M5/RUN_C5V3_R4_NATIVE_LEARNING_R2_SOURCE_AUDIT.sh
COMMIT=4f68a82c77b651fe9d5af9877d53a32e035a3112
```

After R2 static PASS, continue writing the one-cycle native learning main and later compose with P0 trust + exact Gate-A pure donor + exact T1/T2/T3.

## Claim boundary

```text
R4_R1_STATIC_SOURCE_AUDIT=PASS
R4_R1_RUNTIME_ADMISSION=NO
R4_R2_SOURCE_WRITTEN=YES
R4_R2_STATIC_MACHINE_AUDIT=PENDING
R4_RUNTIME_LEARNING=NOT_ADMITTED
GENERAL_SEMANTIC_LEARNING=NOT_PROVEN
WHOLE_WORK_UNDERSTANDING=FAIL
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```

`CLAIM <= EVIDENCE`
