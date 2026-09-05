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
- V2.11R.1 revisit execution + archive re-entry: PASS — source `88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`, checkpoint `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller: PASS — source `ec367a6c780011fc7fe06e7fafbdcfde27198527565bd9054c733e79ecc115be`, checkpoint `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation + lifecycle: PASS.
  - source `8984a0beaefddb6656158eaed47080bc09955f79e9dcb0b59edcd2e0b670f107`;
  - runner `2f68d6dd04a23ecd528fe06ea130f8d65adae4e557c32b5848c0e21998fb6ba0`;
  - generation-aware revalidation/lifecycle proven in tested structural scope;
  - cycle `|` and `||` maintain distinct state;
  - exact-cycle conflict and all four bounded refusals PASS;
  - real survey SHA `de682a2d5a27e1985d2529106c5410f7e824dafbf5e7cb541485687166295d08` unchanged;
  - admitted revisit evidence SHA `a166a82bdf244ec1245d0703ce5664f8e1d4ceda090f13881f8c41b463c194e9` unchanged;
  - checkpoint `d464511977c85853d05c09419f3102d0fd0db88f`.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.14R.1 generation-aware closed-loop transition — SOURCE READY

Hardened source-ready checkpoint: `b404c4ab3ff538babd207aafaf82cb1ae85870c9`.

### Native controller

`SIGMA_GENERATION_AWARE_CLOSED_LOOP_CONTROLLER_V2_14C1.sigma`

SHA256: `1db8cd24432b85a5b4d6125e1f26e657df6bf47c429d763eb255c12ce201d972`

Consumes V2.13 generation-aware lifecycle plus work-local revisit generation state.

- `REVISIT` + generation == lifecycle cycle -> next-cycle `EXECUTE_REVISIT`;
- `REVISIT` + generation == lifecycle cycle + `|` -> exact-cycle `REVALIDATE_REVISIT_GENERATION`;
- `ARCHIVE_FOR_NOW` + matching generation -> `SELECT_NEXT_WORK`;
- inconsistent lifecycle cycle/generation -> no event.

### Native event-driven revisit executor

`SIGMA_EVENT_DRIVEN_REVISIT_EXECUTOR_V2_14E1.sigma`

SHA256: `d6bd5e41813a6f2fc13b7c6bfa6215e01fe4aa11c12c0111e7b51addb9a11210`

Accepts only `WORK::CYCLE::EXECUTE_REVISIT`, requires `CYCLE == completed_generation + |`, commits exact-cycle evidence before cursor advance, and advances generation only after document completion.

### Hardened runner — REQUIRED identity

`RUN_SIGMA_V214R1_GENERATION_AWARE_CLOSED_LOOP_PREFLIGHT.sh`

SHA256: `da3c678089002e1fdb5694ed53eb9e1092462f20d2e1a0ff3fe390214556f226`

Earlier pre-hardening runner SHA `f1f4ff5fb571e4d4c56883860db9236073a1bc6dbd4c254b5471eec743ff2eec` is obsolete and must not be run.

README: `SIGMA_V214R1_GENERATION_AWARE_CLOSED_LOOP_PREFLIGHT_README.txt`.

Static checks: controller/executor H-call arity PASS; no native `!=`; no `str_starts`; no direct `str()`; runner `bash -n` RC 0.

### Real closed-loop target

Start:

- selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- admitted V2.11 generation `|`;
- V2.13 cycle `|` lifecycle `REVISIT`.

Required event-driven transition:

`CYCLE | REVISIT`
-> controller emits `work::||::EXECUTE_REVISIT`
-> mechanical host dispatcher routes exact event to native executor
-> segment 0 / segment 1 / completion across fresh VM
-> generation `||`
-> controller emits `work::||::REVALIDATE_REVISIT_GENERATION`
-> mechanical dispatcher routes exact event to V2.13
-> V2.13 creates `CYCLE=|| RESULT=NOT_REOBSERVED ACTION=REVISIT`
-> controller emits distinct `work::|||::EXECUTE_REVISIT`.

Replay must reproduce exact controller/revalidation/lifecycle/evidence/generation hashes from an isolated mechanical clone of admitted V2.11 state.

### Required bounded/negative gates

- wrong-cycle executor refusal;
- inconsistent lifecycle/generation refusal;
- controller lifecycle over-limit refusal;
- controller event-ledger over-limit refusal;
- executor evidence over-limit refusal;
- executor segment-cursor over-limit refusal;
- admitted V2.11 evidence and real survey unchanged.

### Claim target after PASS

`AUTONOMOUS_STRUCTURAL_CYCLE_TRANSITION=PROVEN_IN_SELECTED_DOCUMENT_TWO_GENERATION_SCOPE`.

Still NOT PROVEN:

- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- `MULTI_DOCUMENT_AUTONOMOUS_CYCLE`;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Install exact V2.14 controller/executor and hardened runner hashes above from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked sigmac/VM and preserve runtime bytecode hashes for V2.12, V2.13, V2.14C1 and V2.14E1, every VM_RC, event transition and replay hash.
4. If a gate fails, preserve evidence and fix only the narrow failure.
5. If PASS, checkpoint before multi-document autonomous cycle admission.
