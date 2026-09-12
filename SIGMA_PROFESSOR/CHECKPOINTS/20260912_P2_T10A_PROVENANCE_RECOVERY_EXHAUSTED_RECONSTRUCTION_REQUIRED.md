# P2 / T10A PROVENANCE RECOVERY — EXHAUSTED; RECONSTRUCTION REQUIRED

Date: 2026-09-12 (Asia/Ho_Chi_Minh)
Branch: `candidate/p1-lang02a-r2-20260912`

## Status

`T10A_PROVENANCE_RECOVERY=EXHAUSTED_WITHIN_CONNECTED_GITHUB_EVIDENCE`

`T10A_DECLARED_PASS=YES`

`T10A_EXACT_PROVENANCE_RECOVERED=NO`

`T10A_RECONSTRUCTION_REQUIRED=YES`

`T10B_REMAINS_HOLD=YES`

`P2_SOURCE_READY=NO`

`NO_NEW_CAPABILITY_PASS=YES`

`PRODUCTION_BINDING=NO`

`PRODUCTION_MUTATION=NO`

## Why this gate exists

The current R7 language-understanding native-tool requirement declares `T10A PASS` and `T10B/T10 combined/T11 pending`, but T10B is explicitly required to reuse T10A archive bounds and then pass exact T10A+T10B combined admission.

A later prose declaration of `T10A PASS` is not sufficient to bind a new T10B implementation to an exact historical capability identity or to safely inherit unspecified archive bounds.

## Recovery scope searched

The connected GitHub audit searched the available repository evidence through multiple independent paths, including:

- current/default code and content indexes;
- commit history for `T10A`, archive-bound, archive/input and related terminology;
- pull-request history;
- branch names and specialized branches;
- issue history;
- the R7 requirement introduction commit, its parent, and nearby commit history;
- the recursive tree of `c5-m5-core-replacement-live`;
- behavioral and naming variants including `T10A`, `T10 A`, `T10B`, `T10 B`, `DOCUMENT_INPUT`, `document input`, `archive`, `extract`, ZIP/TAR terminology, `symlink`, `traversal`, `decompress`, `sandbox`, `EPUB`, `multipart`, parser/input terminology, and archive/container bounds.

The R7 declaration was recovered. An exact T10A implementation/admission chain sufficient for dependency equality-gating was not recovered from the connected GitHub evidence searched.

## Minimum provenance still missing

The audit did not recover one authoritative chain binding T10A to all identities needed for safe reuse, including at minimum:

- exact capability/artifact path;
- source identity and source hash;
- binary identity and binary hash where applicable;
- ABI version/hash where applicable;
- input-schema identity/hash;
- output-schema identity/hash;
- resource-profile identity/hash;
- admission root and/or exact runtime evidence receipt;
- exact archive bounds that T10B is required to reuse.

## Evidence interpretation

This checkpoint does **not** prove that T10A never existed.

It proves only that enough exact provenance was not recovered from the connected GitHub evidence searched to import the historical `T10A PASS` declaration as a safely reusable dependency identity.

Accordingly:

`T10A_HISTORICAL_PASS_IMPORTABLE_AS_EXACT_DEPENDENCY=NO`

`T10A_HISTORICAL_BOUNDS_SAFE_TO_INFER=NO`

`T10B_MAY_INVENT_OR_ASSUME_T10A_BOUNDS=NO`

## Required path forward

Reconstruct and re-admit a **new explicitly versioned T10A** under the current native admission law before T10B is opened.

The reconstruction must:

1. define its own explicit bounded mechanical archive/container-input contract;
2. freeze all implementation, ABI/schema and resource-profile identities required by the current capability gate;
3. label all numeric/resource bounds as **new reconstruction bounds**, not recovered or inherited historical T10A bounds;
4. remain mechanical only — no host or tool semantic interpretation, cognition, evidence choice, meaning choice, or learning;
5. pass directed, randomized-after-freeze, replay, malformed/adversarial, resource-limit, high-entropy/leakage and host-substitution admission tests as applicable;
6. produce an exact admission root/receipt chain;
7. only after that admission, reopen T10B against the new exact T10A identity and bounds.

Until then:

`T10A_RECONSTRUCTION=NOT_RUN`

`T10A_RECONSTRUCTION_ADMISSION=NOT_RUN`

`T10B_DOCUMENT_INPUT=NOT_PROVEN`

## Claim ceiling

This checkpoint grants no new capability PASS.

`FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN`

`HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN`

`SIGMA_AUTONOMOUS_READING=NOT_PROVEN`

`SIGMA_AUTONOMOUS_LEARNING=NOT_PROVEN`

The controlling invariants remain:

`COMBINED_TOOL_PASS != LANGUAGE_UNDERSTANDING`

`CLAIM <= MACHINE EVIDENCE`
