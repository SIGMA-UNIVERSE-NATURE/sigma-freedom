# T10A RECONSTRUCTION R2 — STATIC AUDIT / SUPERSEDED BEFORE RUNTIME

Date: 2026-09-12

## Scope

Artifact audited:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1_R2.sh`

The R2 runner was created to add exact contract identities and a mechanical pre-VM byte gate. It has NOT been executed on the locked SIGMA runtime.

## Positive findings preserved

```text
LOCKED_SIGMAC_SHA256=YES
LOCKED_VM_SHA256=YES
LOCKED_SOURCE_SHA256=YES
RESOURCE_PROFILE_SHA256_LOCK=YES
INPUT_SCHEMA_SHA256_LOCK=YES
OUTPUT_SCHEMA_SHA256_LOCK=YES
BUILD_RECIPE_SHA256_LOCK=YES
COMPILE_BEFORE_DYNAMIC_FIXTURES=YES
PRE_VM_OVERSIZE_BYTE_REFUSAL=DESIGNED
RAW_VM_EVIDENCE_BEFORE_POST_VM_ORACLE=YES
COUNTERFACTUAL=DESIGNED
RANDOMIZED_AFTER_FREEZE=DESIGNED
REPLAY=DESIGNED
SOURCE_BYTECODE_REHASH=DESIGNED
SEMANTIC_CLAIM_CEILING=PRESERVED
```

## Defects found before runtime

### 1. Opaque-ID transport framing was underbounded

R2 bounded ID byte length but did not mechanically reject newline/control bytes in `case_id`, `archive_id`, or `manifest_id` before VM execution.

Those values are printed as raw two-line protocol values. A line-breaking token could make evidence framing ambiguous even though it is not semantic content.

Required fix: freeze a line-safe opaque-token transport rule and fail closed before VM for transport-unsafe IDs.

### 2. Post-VM `val()` parser was key-scan based

R2 searched any line equal to a key and returned the next line. An opaque value equal to an output key could therefore be mistaken for a key by the test oracle.

Required fix: parse the output as an ordered sentinel + two-line key/value pair protocol, so values are never reinterpreted as keys.

### 3. Full output-schema conformance was not runtime-gated

R2 statically checked that declared keys appear in source, but the runtime oracle checked only a subset of output fields and did not require the exact ordered key sequence.

Required fix: exact ordered runtime schema check plus value checks for all evidence-critical fields.

### 4. ABI identity was represented as an operation set, not a frozen ABI artifact

R7 V3 requires an explicit `ABI_VERSION` binding. R2 checked the host operation set but did not bind a separate versioned ABI artifact/hash.

Required fix: freeze `T10A_RECONSTRUCTION_HOST_ABI_V1` and equality-gate its exact SHA256.

### 5. Forbidden semantic-oracle scan was narrower than the R7 V3 forbidden API surface

R2 scanned a useful subset but not the complete V3 API denylist.

Required fix: scan exact API/function/host-operation tokens from the complete V3 denylist without false-positive matching claim-ceiling strings such as `SEMANTIC_UNDERSTANDING`.

### 6. Exact reconstruction proof must not be confused with full R7 family admission

R7 V3 additionally requires prior-layer regression and later combined compatibility. R2's intended exact reconstruction PASS cannot by itself be named full R7 family admission.

Required fix: separate `RECONSTRUCTION_RESOURCE_PROFILE_ADMISSION` from `R7_FAMILY_ADMISSION` and keep prior-layer/combined gates explicit.

## Decision

```text
T10A_R2_STATIC_AUDIT=FAIL_FOR_RUNTIME_READINESS
T10A_R2_RUNTIME_EXECUTION=NOT_RUN
T10A_R2_ADMISSION=NOT_RUN
T10A_R2_SUPERSEDED_BEFORE_RUNTIME=YES
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=NO
NATIVE_SOURCE_CHANGED_BY_THIS_AUDIT=NO
PRODUCTION_STATE_MUTATED=NO
```

R3 MUST preserve the native source claim ceiling, add the missing transport/schema/ABI/oracle gates, and remain offline/candidate-only.
