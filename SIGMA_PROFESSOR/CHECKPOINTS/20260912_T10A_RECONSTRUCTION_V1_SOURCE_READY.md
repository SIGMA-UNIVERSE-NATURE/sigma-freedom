# T10A RECONSTRUCTION V1 — SOURCE READY

Date: 2026-09-12

## Authority and reason for reconstruction

Parent requirement: `C5_M5/R7_LANGUAGE_UNDERSTANDING_NATIVE_TOOL_REQUIREMENT_V2_SAFE_COMPACT.md` at `c25e73b9fe095513fc0ae920d0cdfaab019275ca`.

R7 requires `T10B_DOCUMENT_INPUT` to reuse T10A archive bounds, but the historical T10A exact source/runner/admission provenance was not recoverable from the connected repository evidence. Recovery was closed at commit `6065d62150ba6e9e012bacee46279955ef740489` with reconstruction required.

This artifact therefore defines NEW reconstruction bounds. It does not import or claim the historical T10A bounds.

## Reconstruction identity

```text
T10A_RECONSTRUCTION_ID=T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1
HISTORICAL_T10A_PROVENANCE_IMPORTED=NO
HISTORICAL_T10A_BOUNDS_IMPORTED=NO
RESOURCE_PROFILE_ID=T10A_RECONSTRUCTION_RESOURCE_PROFILE_V1
MAX_ENTRIES=8
MAX_ENTRY_DECLARED_BYTES=1048576
MAX_TOTAL_DECLARED_BYTES=4194304
```

## Native source

`SIGMA_PROFESSOR/artifacts/SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sigma`

```text
SOURCE_GIT_BLOB=c96dbc6e7b699c56634dd384922e925bd384c47e
SOURCE_SHA256=953df93174d314354542daae66842652e30e13d9b92950bc997d08fbb9e15ee4
```

The native source accepts explicit archive-manifest observations, validates bounded digit/flag inputs, checks manifest numeric consistency, applies the reconstruction resource profile, and fail-closes when an explicit hazard observation is present.

Mechanical host ABI used by the native source is limited to:

```text
read_text
str_replace
to_float
```

Host does not select semantic meaning, evidence, truth, curriculum, or capability outcome.

## Admission runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_T10A_BOUNDED_ARCHIVE_MANIFEST_GATE_RECONSTRUCTION_V1.sh`

```text
RUNNER_GIT_BLOB=baaa007aa8ac670b092d202d8890efa0e421a961
RUNNER_SHA256=12f4742ff4c32082f030d490e1746e29cc8752093d7d0faa0e53fafe3938a07a
STATIC_BASH_N=PASS
STATIC_SIGMA_PROFILE_SANITY=PASS
```

Runner design follows the native admission method: toolchain/source identity gate -> compile once -> freeze source/bytecode -> create fixtures only after freeze -> raw VM stdout/stderr before oracle -> directed/adversarial -> randomized post-freeze -> counterfactual -> replay -> step-limit/nonzero checks -> high-entropy source/bytecode leak audit -> source/bytecode unchanged -> hard final AND gate.

Planned exact suite:

```text
DIRECTED_AND_ADVERSARIAL_CASES=20
RANDOMIZED_POST_FREEZE_CASES=16
REPLAY_CASES=2
PLANNED_TOTAL_VM_INVOCATIONS=38
PERSISTENT_STATE=NA
```

Directed scope includes exact boundaries, each resource-bound violation, symlink/traversal/absolute/duplicate/encrypted/unsupported hazard observations, malformed flag/integer tokens, missing manifest identity, numeric inconsistency, and a one-variable resource counterfactual.

## Runtime status

No compile or VM execution is claimed by this checkpoint.

```text
T10A_RECONSTRUCTION_SOURCE=READY
T10A_RECONSTRUCTION_RUNNER=READY
T10A_LOCKED_SIGMAC_COMPILE=NOT_RUN
T10A_BYTECODE_SHA256=UNKNOWN_NOT_COMPILED
T10A_TOTAL_VM_INVOCATIONS_OBSERVED=0
T10A_RUNTIME_PROOF=NOT_RUN
T10A_ADMISSION=NOT_RUN
NO_NEW_CAPABILITY_PASS=YES
```

## Claim ceiling

Even if the runner later passes, the exact reconstruction scope remains a bounded native manifest gate over explicit observations. Keep:

```text
RAW_ARCHIVE_FORMAT_PARSING=NOT_PROVEN
ARCHIVE_HAZARD_DETECTION_FROM_RAW_BYTES=NOT_PROVEN
ACTUAL_ARCHIVE_EXTRACTION=NOT_EXECUTED
DOCUMENT_CONTENT_READING=NOT_PROVEN
DOCUMENT_UNDERSTANDING=NOT_PROVEN
FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
T10B_UNLOCKED=NO_PENDING_T10A_RECONSTRUCTION_RUNTIME_ADMISSION
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

A PASS here MUST NOT be renamed historical `T10A PASS`; it is `T10A_RECONSTRUCTION_V1 PASS_IN_EXACT_TESTED_RECONSTRUCTION_SCOPE` only.

## Next action

Run the exact source and runner on the locked native runtime:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Preserve the first compile/runtime result as evidence. Failure is evidence; do not weaken the gate to force PASS.
