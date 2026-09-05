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
- failures are evidence; never weaken a gate to force PASS;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## Locked runtime

SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

Every admission runner from V2.16 onward must visibly print and equality-gate both runtime identities.

## Production V2.4

Keep V2.4 running unchanged unless it emits a real VM failure.

Production source: `SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`

Production source SHA256: `6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Production runner: `RUN_SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sh`

Production state namespace: `$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2` plus `SIGMA_CL22_*` memory files under the production `.sigma_exec`.

Do NOT upgrade V2.4 in place before shadow-production promotion gates pass.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey — PASS, checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6/V2.6F persisted bounded traversal — PASS, checkpoints `81c8c72e66c30292e17c567d8c3824490dc00e7a`, `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping — PASS, `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority — PASS, `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real-survey native selection — PASS, `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected real work -> deep re-learn — PASS, `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation — PASS, `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle decision — PASS, `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution/archive re-entry — PASS, `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller — PASS, `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation/lifecycle — PASS, `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14R.1 generation-aware closed-loop transition — PASS, `40408a72286efe677d3cdf472c3d8f59b4bac457`.
- V2.15R.1 first -> second real-work transition — PASS, `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
- V2.16R.1 second real-work complete cycle — PASS, `04d786edfe832ef501949549d0560e70c8d8b27f`.
- V2.17R.1 real multi-document cycle promotion — PASS, checkpoint `1897b22984ecd095b0475041e9ea0ececf794e2f`.

## V2.17 admitted runtime result

Real chain:

- second work: `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
- third work: `3b137f0203e0a54dec145abd721e7fb709c305d47e7eaef3aa21a63305f7d0bc`;
- fourth work selected after third archive: `5c97c10b8997fb0799282a3d15fc37d9c5fe6af3ccb1bd7dce37e2589ccf36ad`.

Third work runtime:

- 14 lines;
- baseline `of => the`;
- committed deep segments 2;
- matching baseline segments 1;
- native result `REOBSERVED`;
- native lifecycle `ARCHIVE_FOR_NOW`;
- persistent fresh-VM reuse PASS;
- deterministic replay PASS;
- native `SELECT_NEXT_WORK` -> fourth real work PASS.

Promoted bounded claim:

`MULTI_DOCUMENT_AUTONOMOUS_CYCLE=PROVEN_IN_BOUNDED_REAL_CORPUS_SECOND_THIRD_WORK_SCOPE`.

Still NOT PROVEN:

- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

## Current frontier — V2.18R.1 shadow-production starvation audit — RUNNER READY

Runner user-delivery file:

`RUN_SIGMA_V218R1_SHADOW_PRODUCTION_STARVATION_AUDIT.sh`

Runner SHA256:

`d694efe8e4dc6988f872c8c4710b37885a0f8d2af704dc2c24ece2664ff05ddc`

README:

`SIGMA_V218R1_SHADOW_PRODUCTION_STARVATION_AUDIT_README.txt`

### Why this gate exists

V2.17 is sufficient for a bounded multi-document structural claim, but it is NOT sufficient for production promotion.

The first real selected work is known to produce repeated `NOT_REOBSERVED -> REVISIT` cycles. V2.14 proved at least the transition `cycle | -> cycle || -> cycle |||` on that work. The current controller schedules another revisit immediately after an unresolved revisit cycle.

Before production promotion, this must be tested as a fairness/starvation risk without synthetic archive evidence.

### Shadow audit contract

- V2.4 must be alive before and after the audit;
- shadow VM working directory is separate from production BRAIN;
- all mutable shadow `.sigma_exec` files live under `$HOME/SIGMA/SIGMA_V218R1_SHADOW_PRODUCTION_AUDIT/...`;
- real survey/corpus snapshot are read-only inputs;
- no synthetic archive evidence is allowed;
- run the first real work through initial deep/revalidation/lifecycle and two real revisit generations;
- if native controller again emits `<work>::|||::EXECUTE_REVISIT`, record the promotion blocker rather than forcing `SELECT_NEXT_WORK`.

Expected honest audit result if current admitted behavior reproduces:

- `V218R1_SHADOW_PRODUCTION_STARVATION_AUDIT=PASS`;
- `SHADOW_PRODUCTION_PROMOTION=BLOCKED`;
- `PROMOTION_BLOCKER=IMMEDIATE_CONSECUTIVE_REVISIT_STARVATION_RISK`;
- `PRODUCTION_PROMOTION_ALLOWED=NO`;
- next teaching goal: native revisit fairness / anti-starvation scheduler.

Production V2.4 memory hashes may change during the audit because V2.4 remains live; equality is intentionally not a gate. State isolation is provided by the separate shadow BRAIN namespace.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Install/run exact V2.18 shadow-audit runner SHA above from repo root `~/SIGMA/sigma-freedom-write`.
3. Preserve printed locked runtime hashes, V2.4 PID before/after, shadow bytecode hashes and native cycle outputs.
4. Do not treat `SHADOW_PRODUCTION_STARVATION_AUDIT=PASS` as production promotion; inspect `SHADOW_PRODUCTION_PROMOTION` separately.
5. If the expected blocker reproduces, checkpoint it and teach a native fairness/anti-starvation scheduler before any production candidate is built.
