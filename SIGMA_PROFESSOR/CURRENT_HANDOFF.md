# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## Mandatory standard

Read first: `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`.

Global invariants:

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- runtime proof required;
- failures are evidence; never weaken gates to force PASS;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## Locked runtime

SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

From V2.16 onward, every admission runner must print both `SIGMAC_SHA256` and `VM_SHA256` explicitly near the start of the transcript, in addition to equality-gating them.

## Production

Keep V2.4 production learner running unless it emits a real VM failure. Do not upgrade V2.4 in place while the newer chain remains under admission.

Production V2.4 source SHA256: `6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey: PASS — `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted segment cursor restart: PASS — `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F full fixture traversal: PASS — `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping: PASS — `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority: PASS — `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real survey -> native selected work: PASS — `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work -> deep re-learn: PASS — `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation: PASS — `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle: PASS — `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution + archive re-entry: PASS — `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller: PASS — `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation + lifecycle: PASS — `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14R.1 generation-aware closed-loop transition: PASS — `40408a72286efe677d3cdf472c3d8f59b4bac457`.
  - controller source `1db8cd24432b85a5b4d6125e1f26e657df6bf47c429d763eb255c12ce201d972`;
  - executor source `d6bd5e41813a6f2fc13b7c6bfa6215e01fe4aa11c12c0111e7b51addb9a11210`;
  - hardened runner `da3c678089002e1fdb5694ed53eb9e1092462f20d2e1a0ff3fe390214556f226`;
  - `AUTONOMOUS_STRUCTURAL_CYCLE_TRANSITION=PROVEN_IN_SELECTED_DOCUMENT_TWO_GENERATION_SCOPE`.
- V2.15R.1 event-driven real first -> second work transition: PASS — checkpoint `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
  - runner SHA256 `3b54dc2fce2d408c9ffb9f4cedead91a2b82f69ec8a1688d6518837e9e02e687`;
  - first native work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
  - second native work `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
  - first selector-state SHA `3225092993410c1b7ed77c5a668439e7d9fc78b0e572b394d0ece8a51417279e`;
  - second selector-state SHA `16134eff08cd5fe385897f2ec689febab4e719f224470d296ebccc3ad118037d`;
  - second real document has 8 lines;
  - second segment-0 best relation `of => the`, support 3;
  - second deep evidence SHA `8cbd66050013d4061086f2d774b60a632fe98e3263427592f8806fa25c56d2b5`;
  - fresh VM reached second-work completion at segment index 1;
  - selector replay PASS; real survey and second document immutable;
  - observed V2.13 bytecode `ef3ea3e54a9d9d4c1858c877fc9046f9a66227fb150bd5a3c0d9847246ce609d`;
  - observed V2.14C1 bytecode `9d7b120c7f51939c6679d55629d46816f041679164ff5c4afa8feb5af278d4f5`.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.16R.1 second real work complete cycle — SOURCE READY

No new cognitive native source is introduced. This is a composition/admission gate over admitted native components.

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V216R1_SECOND_REAL_WORK_COMPLETE_CYCLE_PREFLIGHT.sh`

Runner SHA256:
`5e76462247a745145bc49c1fd1e8727741e1efa348047856973356677c84a6f7`

Runner commit:
`e2bce5924fe7934d14896be7cbb19dc9403cfdf4`

README commit:
`5084dec0da8f0ace9fd0c91a4ba821f46d4acfa4`

Source-ready checkpoint:
`35f38d9009e8f95845bbda325a921a1d28a3492f`

### Core anti-hardcode contract

V2.16 does NOT predeclare whether the second real work must yield `REOBSERVED` or `NOT_REOBSERVED`.

It regenerates the real second work and its real deep evidence, then lets:

1. V2.9 decide structural revalidation;
2. V2.10 decide lifecycle;
3. host mechanically route the exact native lifecycle branch.

Mapping consistency is checked only after native output:

- `REOBSERVED -> ARCHIVE_FOR_NOW`;
- `NOT_REOBSERVED -> REVISIT`.

### Branch A — native ARCHIVE_FOR_NOW

- V2.12 must emit `SELECT_NEXT_WORK`;
- the already-admitted selector must choose a third real work distinct from first and second;
- if successful, admit conditional real second -> third transition proof.

### Branch B — native REVISIT

- V2.11 executes a complete revisit generation on the 8-line second document;
- V2.12 emits exact-cycle revalidation event;
- V2.13 performs generation-aware revalidation/lifecycle;
- V2.14 emits the exact next stage;
- if next stage is `SELECT_NEXT_WORK`, select a third real work;
- if next stage is `EXECUTE_REVISIT`, preserve that event as the next native action.

### Admission gates

- runtime hashes visible in transcript and equality-gated;
- deterministic first -> second real selection;
- second real initial deep completion;
- native second-work revalidation/lifecycle without result hardcoding;
- fresh-VM revalidation/lifecycle state reuse;
- deterministic revalidation/lifecycle replay;
- branch-specific event routing;
- survey/document/real second initial evidence immutability.

### Target claim

On PASS:
`SECOND_WORK_COMPLETE_CYCLE=PROVEN_IN_REAL_SELECTED_DOCUMENT_SCOPE`.

Conditional additional claim if a distinct third work is selected:
`REAL_SECOND_TO_THIRD_WORK_TRANSITION=PROVEN_IN_FROZEN_56_DOCUMENT_SURVEY_SCOPE`.

Still NOT PROVEN automatically:

- `MULTI_DOCUMENT_AUTONOMOUS_CYCLE`;
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

## NEXT ACTION

1. Keep V2.4 production learner running unchanged.
2. Install exact V2.16 runner SHA above from repo root `~/SIGMA/sigma-freedom-write`; no new `.sigma` source is required.
3. Run locked sigmac/VM and preserve all printed runtime SHA values, bytecode SHA values, every VM_RC, native result/action/event, and state hashes.
4. If a gate fails, preserve evidence and fix only the narrow failure.
5. If V2.16 PASS, checkpoint before the real multi-document cycle promotion gate.
