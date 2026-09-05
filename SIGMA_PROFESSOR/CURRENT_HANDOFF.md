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

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

## Production

Keep V2.4 production learner running unless it emits a real VM failure.
Do not upgrade V2.4 in place while the newer chain remains under admission.

Production V2.4 source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey: PASS — `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted segment cursor restart: PASS — `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F full fixture traversal: PASS — `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping: PASS — `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority: PASS — `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real survey -> native selected work: PASS — source `8d4fee26...430e8`, bytecode `0244d7a6...c1eb5`, checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work -> deep re-learn: PASS — source `3da9195d...e8ce`, bytecode `e23fd92e...2ff`, checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation: PASS — real baseline `of => the`, real result `NOT_REOBSERVED`, checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle: PASS — real `NOT_REOBSERVED -> REVISIT`, checkpoint `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution + archive re-entry: PASS — source `88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`, repaired runner `31005526c5ec1a4c33ec1759965b9810e19198fae08235dc1ca16d8c5c739907`, checkpoint `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 native cycle event controller: PASS.
  - source SHA256 `ec367a6c780011fc7fe06e7fafbdcfde27198527565bd9054c733e79ecc115be`;
  - runner SHA256 `02be167cd7d302c72735e384532310a347edbaf0d1827ec748f4b635a660910c`;
  - `NATIVE_STAGE_DECISION=PROVEN_IN_TESTED_STRUCTURAL_SCOPE`;
  - explicit event identity `WORK + CYCLE + NEXT_STAGE` PASS;
  - distinct revisit generations produce distinct event IDs PASS;
  - persistent event reuse + deterministic replay PASS;
  - archive/select-next, wait/no-lifecycle, inconsistent-state refusal, partial lifecycle filter PASS;
  - lifecycle/controller/generation/segment bounded refusal PASS;
  - user-provided tail did not include the V2.12 bytecode SHA, so do not invent it;
  - checkpoint `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.

## Important distinctions

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.13R.1 generation-aware revalidation + lifecycle — SOURCE READY

Canonical user-delivery source:
`SIGMA_GENERATION_AWARE_REVALIDATION_LIFECYCLE_V2_13R1.sigma`

Canonical source SHA256:
`8984a0beaefddb6656158eaed47080bc09955f79e9dcb0b59edcd2e0b670f107`

Runner:
`RUN_SIGMA_V213R1_GENERATION_AWARE_REVALIDATION_LIFECYCLE_PREFLIGHT.sh`

Runner SHA256:
`2f68d6dd04a23ecd528fe06ea130f8d65adae4e557c32b5848c0e21998fb6ba0`

Source-ready checkpoint:
`a3e2ae18ec17e8bd51056fd2709523d2f823a291`

A temporary noncanonical compact rendering was removed in commit `ae3b9a4cae2844a7c430b371076f30e06aa9e3a3`; never use it as the candidate identity.

### Capability contract

Controller input:
`WORK::CYCLE::REVALIDATE_REVISIT_GENERATION`

Exact-cycle revisit evidence:
`WORK=<id> || GEN=<cycle> || CURSOR=<segment-cursor> || BEST_LOCAL_RELATION=<relation> || COMMIT=YES`

Generation-aware revalidation state:
`WORK=<id> || CYCLE=<cycle> || RESULT=<REOBSERVED|NOT_REOBSERVED> || BASELINE=<anchor> || COMMIT=YES`

Generation-aware lifecycle state:
`WORK=<id> || CYCLE=<cycle> || ACTION=<REVISIT|ARCHIVE_FOR_NOW> || FROM_RESULT=<result> || COMMIT=YES`

Policy:

- compare survey baseline only against committed revisit evidence for the exact cycle;
- exact-cycle recurrence -> `REOBSERVED`;
- exact-cycle evidence without recurrence -> `NOT_REOBSERVED`;
- `NOT_REOBSERVED -> REVISIT`;
- `REOBSERVED -> ARCHIVE_FOR_NOW`.

### Real expected branch

- selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- V2.12 regenerates event `work::|::REVALIDATE_REVISIT_GENERATION`;
- cycle `|` evidence: `in => the`, `As => disagreements`;
- survey baseline: `of => the`;
- expected V2.13 result: `CYCLE=| -> NOT_REOBSERVED -> REVISIT`.

### Admission gates

- real V2.12 event regeneration;
- real cycle `|` revalidation/lifecycle;
- fresh VM reuse/no duplicate append;
- deterministic replay;
- cycle `||` coexists with seeded cycle `|` state;
- synthetic cycle `||` `REOBSERVED -> ARCHIVE_FOR_NOW`;
- partial/uncommitted matching evidence ignored;
- wrong controller stage refuses mutation;
- exact-cycle conflict blocks mutation;
- survey/evidence/revalidation/lifecycle bounded refusal;
- real survey and revisit evidence immutable.

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `DIRECT_STR_DEPENDENCY=NONE`;
- runner `bash -n` RC = 0.

### Current claim limits

- V2.13 runtime admission = `NOT_PROVEN`;
- `GENERATION_AWARE_REVALIDATION=NOT_PROVEN` until locked-VM PASS;
- `GENERATION_AWARE_LIFECYCLE=NOT_PROVEN` until locked-VM PASS;
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`.

## NEXT ACTION

1. Keep V2.4 running.
2. Install exact canonical V2.13 source/runner hashes above from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked sigmac/VM and preserve V2.12 regenerated bytecode SHA, V2.13 bytecode SHA, all VM_RC and state hashes.
4. If a gate fails, preserve evidence and fix only the narrow failure.
5. If V2.13 PASS, checkpoint before upgrading the controller to consume generation-aware lifecycle records and proving the first closed recurrent cycle.
