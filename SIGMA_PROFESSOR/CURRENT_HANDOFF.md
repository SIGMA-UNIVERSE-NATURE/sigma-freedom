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

From V2.16 onward, every admission runner must print both runtime SHA values explicitly near the start of the transcript and equality-gate them.

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
- V2.15R.1 event-driven real first -> second work transition: PASS — `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
  - first work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
  - second work `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
  - second document 8 lines;
  - second initial best relation `of => the`, support 3;
  - second initial evidence SHA `8cbd66050013d4061086f2d774b60a632fe98e3263427592f8806fa25c56d2b5`;
  - selector replay PASS.
- V2.16R.1 second real work complete cycle: PASS — `04d786edfe832ef501949549d0560e70c8d8b27f`.
  - locked sigmac + VM v09 identity visibility PASS;
  - second real work initial deep completion PASS;
  - native second revalidation PASS;
  - native second lifecycle PASS;
  - branch was not hardcoded;
  - real runtime branch = `REOBSERVED -> ARCHIVE_FOR_NOW`;
  - native selector then selected third real work `3b137f0203e0a54dec145abd721e7fb709c305d47e7eaef3aa21a63305f7d0bc`;
  - persistent revalidation/lifecycle fresh-VM reuse PASS;
  - deterministic second revalidation/lifecycle replay PASS;
  - `SECOND_WORK_COMPLETE_CYCLE=PROVEN_IN_REAL_SELECTED_DOCUMENT_SCOPE`;
  - `REAL_SECOND_TO_THIRD_WORK_TRANSITION=PROVEN_IN_FROZEN_56_DOCUMENT_SURVEY_SCOPE`;
  - real survey/second document/second initial evidence immutable.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.17R.1 real multi-document cycle promotion — SOURCE READY

No new cognitive native source is introduced. This is a promotion/admission composition gate over already-admitted native capabilities.

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V217R1_REAL_MULTI_DOCUMENT_CYCLE_PROMOTION_PREFLIGHT.sh`

Runner SHA256:
`df6d423c7d1ff10cea9f374fb94cda07769f6c8ed9945f5b1d71db582516414d`

Runner commit:
`a7eed505cd133074e8e36f21fba410fa28e39f97`

README commit:
`0500ea0f592be4d1bb74b9db2cfa9d2d78223686`

Source-ready checkpoint:
`384aea5de582443b764923d1f61d6fb80e23c9cc`

### Promotion contract

The V2.17 gate replays the admitted real second-work branch and second -> third transition, then completes a real cycle on the third selected work.

Real chain entering the gate:

- first: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- second: `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
- third: `3b137f0203e0a54dec145abd721e7fb709c305d47e7eaef3aa21a63305f7d0bc`.

Runner requirements:

1. visibly print + equality-gate locked sigmac and VM v09 hashes;
2. replay second real complete cycle and require its admitted `REOBSERVED -> ARCHIVE_FOR_NOW` branch;
3. replay native second -> third work selection;
4. complete third initial deep learning across bounded fresh-VM invocations, max 64;
5. let native V2.9/V2.10 decide third revalidation/lifecycle without oracle hardcoding;
6. require third fresh-VM revalidation/lifecycle reuse and deterministic replay;
7. mechanically dispatch the native third branch:
   - `ARCHIVE_FOR_NOW` -> `SELECT_NEXT_WORK` -> fourth real work;
   - `REVISIT` -> complete real revisit generation -> V2.13 exact-cycle revalidation/lifecycle -> V2.14 next event;
8. real survey, second document, third document and third initial evidence must remain immutable.

### Promotion claim allowed only after runtime PASS

`MULTI_DOCUMENT_AUTONOMOUS_CYCLE=PROVEN_IN_BOUNDED_REAL_CORPUS_SECOND_THIRD_WORK_SCOPE`.

This is a bounded structural claim only.

Still NOT PROVEN automatically:

- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

## NEXT ACTION

1. Keep V2.4 production learner running unchanged.
2. Install exact V2.17 runner SHA above from repo root `~/SIGMA/sigma-freedom-write`; no new `.sigma` source is required.
3. Run locked sigmac/VM and preserve printed runtime identities, bytecode hashes, every VM_RC, third result/action/event, selector IDs and state hashes.
4. If any gate fails, preserve evidence and repair only the narrow failure.
5. If V2.17 PASS, checkpoint before building a shadow-production promotion preflight; do not upgrade V2.4 in place yet.
