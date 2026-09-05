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

VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

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
- V2.14R.1 generation-aware closed-loop transition: PASS — checkpoint `40408a72286efe677d3cdf472c3d8f59b4bac457`.
  - controller source SHA256 `1db8cd24432b85a5b4d6125e1f26e657df6bf47c429d763eb255c12ce201d972`;
  - executor source SHA256 `d6bd5e41813a6f2fc13b7c6bfa6215e01fe4aa11c12c0111e7b51addb9a11210`;
  - hardened runner SHA256 `da3c678089002e1fdb5694ed53eb9e1092462f20d2e1a0ff3fe390214556f226`;
  - real selected-document transition proved `cycle | -> cycle || -> distinct cycle ||| event`;
  - fresh-VM resume, deterministic replay, wrong-cycle refusal, inconsistent lifecycle/generation refusal, controller/executor bounded gates PASS;
  - `AUTONOMOUS_STRUCTURAL_CYCLE_TRANSITION=PROVEN_IN_SELECTED_DOCUMENT_TWO_GENERATION_SCOPE`;
  - real survey unchanged at `de682a2d5a27e1985d2529106c5410f7e824dafbf5e7cb541485687166295d08`;
  - admitted V2.11 evidence unchanged at `a166a82bdf244ec1245d0703ce5664f8e1d4ceda090f13881f8c41b463c194e9`;
  - user-provided tail did not include V2.14 bytecode SHA values; do not invent them.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.15R.1 event-driven real next-work transition — SOURCE READY

This is a composition/admission step; no new cognitive native source is introduced.

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V215R1_EVENT_DRIVEN_REAL_NEXT_WORK_TRANSITION_PREFLIGHT.sh`

Runner SHA256:
`3b54dc2fce2d408c9ffb9f4cedead91a2b82f69ec8a1688d6518837e9e02e687`

Runner artifact commit:
`b38d8def194c70669abe961cbaa9e3655b05a36c`

README commit:
`bb8fa73ec87d791b010405c1096b0c1f7069a7ca`

Source-ready checkpoint:
`ece60cb9f61603280e6b04e7cc88f22a34337aa5`

### Capability contract

Target composition:

1. exact admitted V2.8R.1 selects and persists the first real work;
2. admitted V2.13 receives a structural matching TEST fixture and itself decides `REOBSERVED -> ARCHIVE_FOR_NOW`;
3. admitted V2.14C1 consumes that lifecycle and emits exact `SELECT_NEXT_WORK`;
4. host mechanically routes only that exact event stage to V2.8R.1;
5. V2.8R.1 selects a different second real work from the same frozen 56-document survey;
6. admitted V2.8D.1 resolves the second real snapshot document and starts bounded learning;
7. a fresh VM continuation must reuse persisted work/cursor state.

Expected deterministic selector sequence already observed in admitted V2.8R.1:

- first: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- second: `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`.

### Required gates

- first real work native selection;
- V2.13 native `ARCHIVE_FOR_NOW` from structural test evidence;
- V2.14 native `SELECT_NEXT_WORK` event;
- second real work native selection;
- second work differs from first;
- second real document resolves;
- native segment 0 learning starts on second work;
- fresh VM uses persisted second-work cursor;
- a native non-selection event does not invoke the selector;
- deterministic first->second selector replay;
- real survey and second document remain immutable.

### Host boundary

- `HOST_WORK_SELECTION=NO`;
- `HOST_STAGE_DECISION=NO`;
- `HOST_ARCHIVE_DECISION=NO`;
- `HOST_DOCUMENT_SELECTION=NO`;
- `HOST_LEARNING=NO`;
- mechanical event routing only.

### Claim limits

The archive-producing evidence is a test fixture. Therefore even after V2.15 PASS:

- `MULTI_DOCUMENT_AUTONOMOUS_CYCLE=NOT_PROVEN`;
- `SECOND_WORK_COMPLETE_CYCLE=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`.

A PASS may establish only real event-driven first->second work transition plus native learning start on the second real work.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Install exact V2.15 runner SHA above from repo root `~/SIGMA/sigma-freedom-write`; no new `.sigma` file is required.
3. Preserve exact V2.13/V2.14 recompiled bytecode SHA values, selector/deep pinned bytecode checks, every VM_RC, selected IDs and state hashes.
4. If a gate fails, preserve evidence and fix only the narrow failure.
5. If V2.15 PASS, checkpoint before building a complete real cycle on the second selected work.
