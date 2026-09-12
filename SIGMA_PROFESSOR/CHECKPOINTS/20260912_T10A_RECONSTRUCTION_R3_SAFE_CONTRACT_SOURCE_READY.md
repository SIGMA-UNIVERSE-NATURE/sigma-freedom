# T10A RECONSTRUCTION V1 R3 — SAFE CONTRACT SOURCE READY

Date: 2026-09-12

## Purpose

R3 supersedes R2 before any locked-runtime execution. R2 static audit found transport-framing, oracle parsing, full output-schema, ABI-identity, forbidden-API-scan, and claim-scope defects. Those findings are preserved in `20260912_T10A_RECONSTRUCTION_R2_STATIC_AUDIT_SUPERSEDED.md`.

No native runtime PASS is claimed here.

## Locked native runtime identity

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Native source identity — unchanged

Path:
`SIGMA_PROFESSOR/artifacts/SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigma`

```text
SOURCE_GIT_BLOB=c96dbc6e7b699c56634dd384922e925bd384c47e
SOURCE_SHA256=953df93174d314354542daae66842652e30e13d9b92950bc997d08fbb9e15ee4
NATIVE_SOURCE_CHANGED_BY_R3=NO
```

## R3 runner identity

Path:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1_R3.sh`

```text
RUNNER_GIT_BLOB=ad341a7f02269f55e2ff7c313caac2f90cb14454
RUNNER_SHA256=36aa079b1d4bc171da2fb90fb04da5c6c7aac174407c24dd01b2c259b4504956
STATIC_BASH_N=PASS
```

The GitHub runner blob exactly matched local `git hash-object` before this checkpoint was written.

## Frozen R3 contracts

### Execution envelope V2

```text
PATH=SIGMA_PROFESSOR/artifacts/PROFILES/T10A_RECONSTRUCTION_EXECUTION_ENVELOPE_V2.txt
GIT_BLOB=86ff9b0af1ff5773e336db7e74c0fbe6d890bdb3
SHA256=e31e59fcf2f2348cea8d071eb7fb4758c55f3c509321e2f8c8dbffbeb1381376
MAX_ENTRIES=8
MAX_ENTRY_DECLARED_BYTES=1048576
MAX_TOTAL_DECLARED_BYTES=4194304
MAX_ID_TOKEN_BYTES=128
MAX_NUMERIC_TOKEN_BYTES=32
MAX_FLAG_TOKEN_BYTES=8
MAX_TOTAL_INPUT_BYTES=1024
MAX_INPUT_FILES=12
```

### Input schema V2

```text
PATH=SIGMA_PROFESSOR/artifacts/SCHEMAS/T10A_RECONSTRUCTION_INPUT_SCHEMA_V2.txt
GIT_BLOB=9b1bc481efaa18dbe6dd23feab66e0f517edf267
SHA256=2831c11c6a49e179adf85e90ddf2201edddf183642655852768b156ab06e6dc9
FIELD_COUNT=12
OPAQUE_ID_LINE_BREAK_ALLOWED=NO
```

Opaque ID transport bytes are restricted mechanically to ASCII alphanumeric plus `. _ : -`; semantic/content authority is not transferred to the host.

### Output schema V2

```text
PATH=SIGMA_PROFESSOR/artifacts/SCHEMAS/T10A_RECONSTRUCTION_OUTPUT_SCHEMA_V2.txt
GIT_BLOB=e5684c3c652dde340979c16bb5fb1eeb01645acb
SHA256=94cdcfa86eb5ec40434523a1ef005efde5295fc5462337ea72410bfe6babafdc
OUTPUT_KEY_COUNT=36
FORMAT=ORDERED_SENTINEL_THEN_TWO_LINE_KEY_VALUE_PAIRS
```

Static audit confirmed every declared key occurs exactly once in the native source and in schema order.

### Host ABI V1

```text
PATH=SIGMA_PROFESSOR/artifacts/CONTRACTS/T10A_RECONSTRUCTION_HOST_ABI_V1.txt
GIT_BLOB=f53970c0a95b2fd4ecded70396e0993da20f0b3f
SHA256=b1f9229a23a366ea2ef8339725bf66b7013c8924d3dac629b610d74d509abf97
ABI_VERSION=T10A_RECONSTRUCTION_HOST_ABI_V1
HOST_OPERATION_SET=read_text,str_replace,to_float
```

`HOST_ABI_RUNTIME_SUPPORT=NOT_PROVEN_UNTIL_R3_RUNTIME`. R3 must fail if the locked runtime does not support the exact required mechanical ABI.

### Build recipe V2

```text
PATH=SIGMA_PROFESSOR/artifacts/CONTRACTS/T10A_RECONSTRUCTION_BUILD_RECIPE_V2.txt
GIT_BLOB=d180fcd74515c4978ed185945f5b2b2acee8c885
SHA256=06819e07c5280eba57b0681264df55697d3eb30feaa7414705a8789cc3b111a6
COMPILE_ONCE_BEFORE_DYNAMIC_FIXTURES=YES
```

## R3 static hardening

R3 adds or hardens all of the following before any capability claim:

```text
COMPLETE_R7_V3_FORBIDDEN_API_STATIC_SCAN=YES
FORBIDDEN_API_SCAN_AVOIDS_CLAIM_CEILING_FALSE_POSITIVES=YES
SOURCE_TO_INPUT_SCHEMA_ALIGNMENT=YES
SOURCE_TO_OUTPUT_SCHEMA_EXACT_KEY_COUNT=YES
SOURCE_TO_OUTPUT_SCHEMA_ORDER=YES
ABI_VERSION_HASH_LOCK=YES
BUILD_RECIPE_HASH_LOCK=YES
RESOURCE_PROFILE_HASH_LOCK=YES
PRE_VM_ID_TRANSPORT_SAFETY_GATE=YES
POSITIONAL_TWO_LINE_POST_VM_PARSER=YES
FULL_RUNTIME_OUTPUT_SCHEMA_ORDER_GATE=YES
FULL_EVIDENCE_CRITICAL_VALUE_ALIGNMENT=YES
```

The post-VM parser treats each output value as a value, not as a new key, preventing evidence-key confusion when an opaque value equals a key token.

## Planned pre-VM refusal matrix

These cases MUST be rejected mechanically before VM invocation:

```text
1 OVERSIZE_NUMERIC_TOKEN
2 OVERSIZE_ID_TOKEN
3 OVERSIZE_FLAG_TOKEN
4 ID_LINE_BREAK_INJECTION
5 EXTRA_INPUT_FILE
```

Expected:

```text
PRE_VM_RESOURCE_REFUSAL_CASES=5
PRE_VM_RESOURCE_REFUSAL_PASS_COUNT=5
```

These gates are transport/resource safety only. They do not choose semantic meaning or capability outcomes.

## Planned VM matrix

```text
DIRECTED_AND_ADVERSARIAL_CASES=20
RANDOMIZED_POST_FREEZE_CASES=16
REPLAY_CASES=2
PLANNED_TOTAL_VM_INVOCATIONS=38
PERSISTENT_STATE=NA
```

The 38 VM cases preserve boundary/resource/hazard/malformed/counterfactual/randomized/replay evidence from the earlier reconstruction suite, with stronger exact output-schema and evidence-value alignment.

## R7 admission separation

A successful R3 run may prove only the exact reconstruction resource-profile / bounded-manifest-gate scope tested by R3.

It MUST NOT be renamed full R7 family admission because the wider R7 standard still requires prior-layer regression and later combined compatibility.

```text
PRIOR_LAYER_REGRESSION=NOT_RUN
COMBINED_COMPATIBILITY=NOT_RUN
R7_FAMILY_ADMISSION=NOT_RUN
```

A successful R3 transcript may state only:

```text
T10A_NATIVE_BOUNDED_ARCHIVE_MANIFEST_GATE=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R3_SCOPE
T10A_EXECUTION_ENVELOPE=PASS_IN_EXACT_TESTED_R3_SCOPE
T10A_RECONSTRUCTION_RESOURCE_PROFILE_ADMISSION=PASS_IN_EXACT_TESTED_R3_SCOPE
T10A_RECONSTRUCTION_R3_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_RECONSTRUCTION_R3_SCOPE
```

A separate machine-evidence receipt is required before T10B may consume the R3 resource-profile admission as a dependency.

## Current machine-evidence state

```text
T10A_R2_SUPERSEDED_BEFORE_RUNTIME=YES
T10A_R3_SOURCE_READY=YES
T10A_R3_CONTRACT_READY=YES
T10A_R3_LOCKED_SIGMAC_COMPILE=NOT_RUN
T10A_R3_BYTECODE_SHA256=UNKNOWN_NOT_COMPILED
T10A_R3_TOTAL_VM_INVOCATIONS_OBSERVED=0
T10A_R3_RUNTIME_PROOF=NOT_RUN
T10A_R3_ADMISSION=NOT_RUN
T10B_RUNTIME_ADMISSION=BLOCKED
NO_NEW_CAPABILITY_PASS=YES
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

## Claim ceiling

Keep all of these regardless of static readiness:

```text
RAW_ARCHIVE_FORMAT_PARSING=NOT_PROVEN
ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES=NOT_PROVEN
ACTUAL_ARCHIVE_EXTRACTION=NOT_EXECUTED
DOCUMENT_CONTENT_READING=NOT_PROVEN
DOCUMENT_UNDERSTANDING=NOT_PROVEN
FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
```

## Branch-scope audit

Relative to base `894d9ae509583ce45161ef9a1340e3d654d06ce1`, the R7 grant branch was audited before this checkpoint: all observed changes were additive candidate grant/contract/schema/profile/runner/checkpoint artifacts. No production/native toolchain file was modified.

## Next machine action

Run exact R3 on the locked Termux runtime and preserve the full first transcript, PASS or FAIL. Failure is evidence. Do not run superseded R2 and do not weaken R3 gates to force PASS.
