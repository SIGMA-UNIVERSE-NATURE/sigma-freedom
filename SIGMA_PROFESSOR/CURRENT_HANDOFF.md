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
- failures are evidence; never weaken admission gates;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## Locked runtime

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

Every admission runner from V2.16 onward must visibly print and equality-gate both runtime identities.

## Production V2.4

Keep V2.4 running unchanged unless it emits a real VM failure.

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Do NOT upgrade V2.4 in place before shadow-production promotion gates pass.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey — PASS `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6/V2.6F persisted bounded traversal — PASS `81c8c72e66c30292e17c567d8c3824490dc00e7a`, `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping — PASS `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority — PASS `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real-survey native selection — PASS `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work deep re-learn — PASS `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation — PASS `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle — PASS `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution/archive re-entry — PASS `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller — PASS `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation/lifecycle — PASS `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14R.1 generation-aware closed-loop transition — PASS `40408a72286efe677d3cdf472c3d8f59b4bac457`.
- V2.15R.1 first -> second real-work transition — PASS `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
- V2.16R.1 second real-work complete cycle — PASS `04d786edfe832ef501949549d0560e70c8d8b27f`.
- V2.17R.1 real multi-document cycle promotion — PASS `1897b22984ecd095b0475041e9ea0ececf794e2f`.

V2.17 bounded admitted claim:

`MULTI_DOCUMENT_AUTONOMOUS_CYCLE=PROVEN_IN_BOUNDED_REAL_CORPUS_SECOND_THIRD_WORK_SCOPE`.

Real selected chain reached:

- first `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- second `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
- third `3b137f0203e0a54dec145abd721e7fb709c305d47e7eaef3aa21a63305f7d0bc`;
- fourth `5c97c10b8997fb0799282a3d15fc37d9c5fe6af3ccb1bd7dce37e2589ccf36ad`.

Still NOT PROVEN generally:

- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION`;
- semantic truth validation;
- semantic understanding;
- bounded file I/O;
- mid-append crash atomicity.

## V2.18R.1 shadow-production starvation audit — PASS / promotion blocked

Checkpoint:
`1e07738afce2bd5f111eb7861ebcdcdf3ab4472c`

Observed first-work real shadow sequence:

`... -> generation || -> NOT_REOBSERVED -> REVISIT -> 0ac783...::|||::EXECUTE_REVISIT`

Result:

- audit PASS;
- promotion BLOCKED;
- blocker = immediate consecutive revisit starvation risk;
- synthetic archive used = NO;
- production V2.4 remained running;
- shadow namespace isolation PASS.

## V2.19R.1 native revisit fairness / anti-starvation scheduler — PASS

Native source:
`SIGMA_REVISIT_FAIRNESS_ANTI_STARVATION_SCHEDULER_V2_19R1.sigma`

Source SHA256:
`e0734dbbdb6f0bad3d6577f9a9b20eb3a13dd9c3489caebd7f6f58bb15200ad0`

Runner SHA256:
`e390445d0fd7439043ea3fb75c90661d78fb0321245b2c81d959f508370dd8e1`

PASS checkpoint:
`e44e84a37168cc193721d80a68cb58f331378280`

Admitted claim:

`NATIVE_REVISIT_FAIRNESS_QUEUE=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Policy:

- immediate revisit is deferred while undispatched work exists;
- exact revisit event is persisted as PENDING;
- pending event matures only after selector dispatch progress plus a turn from a different work;
- oldest mature pending revisit resumes first;
- current revisit is queued before older pending event resumes, enabling rotation;
- no alternative work -> revisit executes rather than being lost;
- revisit evidence is never deleted;
- host decides neither fairness nor priority.

Admission evidence includes real V2.18 starvation-event deferral, fresh-VM defer reuse, A/B/C rotation, deterministic ledger replay, selector/survey inconsistency refusal, partial commit filtering and bounded refusals.

## V2.20R.1 fairness shadow-production integration — PASS

PASS checkpoint:
`596a9620a7046d431f89ed5006332c1e1cfa4415`

Real integrated sequence:

1. first real work reaches `|||::EXECUTE_REVISIT`;
2. V2.19 defers exact event and schedules other work;
3. real second work selected and completes real `REOBSERVED -> ARCHIVE_FOR_NOW` cycle;
4. V2.19 resumes exact pending first `|||::EXECUTE_REVISIT`;
5. clean fresh host process recovers persisted resume intent;
6. generation `|||` executes completely;
7. first work remains unresolved and emits `||||::EXECUTE_REVISIT`;
8. V2.19 defers it again;
9. real third work is selected.

Admitted claim:

`REAL_SHADOW_ANTI_STARVATION_INTEGRATION=PROVEN_IN_FIRST_SECOND_THIRD_WORK_SCOPE`

Also PASS:

- cycle identity preserved on resumed revisit;
- clean supervisor restart recovers defer and resume intents from fully committed files;
- shadow namespace isolation;
- production V2.4 remained running with same observed PID during test;
- host fairness/stage/work/revisit-priority decisions = NO.

Promotion remains:

`PRODUCTION_PROMOTION_ALLOWED=NO`

because long-horizon stability and mid-append crash atomicity are not yet proven.

## Current frontier — V2.21R.1 long-horizon shadow stability/recovery — SOURCE READY

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V221R1_LONG_HORIZON_SHADOW_STABILITY_RECOVERY_PREFLIGHT.sh`

Runner SHA256:
`c6ab9129af4692c4e134c39b088917c047864ccbf977a5314c0dc0f9322b0f3d`

Runner commit:
`266575729ef2ef2fdcbf473341ced8b4b684932b`

README commit:
`ac7c0adcc306711dabb29b050853b56e1df74079`

Source-ready checkpoint:
`826b87134ced237ac430cb1e2cafdb51fed786e1`

### Admission target

Extend the admitted V2.20 real shadow chain through six fairness scheduling boundaries and at least four real works.

Required sequence:

- first starvation defer;
- second real work complete cycle -> resume exact first `|||`;
- first `|||` complete -> redefer `||||` -> third work;
- admitted third real work `REOBSERVED -> ARCHIVE_FOR_NOW` -> resume first `||||`;
- first `||||` completes; its new branch is NOT hardcoded, but fairness must result in `SELECT_NEXT_WORK` so fourth work is reached;
- fourth real work completes initial deep/revalidation/lifecycle with NO branch oracle;
- fourth terminal event passes through fairness and persists the next continuation intent.

Fresh-host recovery is required at every extended persisted-event boundary.

PASS requires at least:

- 4 selector dispatch records;
- 2 PENDING fairness records;
- 2 RESUMED fairness records;
- exact event identity preserved;
- production V2.4 same runner PID before/after;
- shadow namespace isolation.

Allowed claim after locked-runtime PASS only:

`LONG_HORIZON_SHADOW_STABILITY=PROVEN_IN_SIX_BOUNDARY_FOUR_REAL_WORK_SCOPE`

### Promotion status after V2.21

Even after PASS:

`PRODUCTION_PROMOTION_ALLOWED=NO`

Remaining blocker:

`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

Current host `write_text` / `append_text` semantics are not proven crash-atomic.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Install exact V2.21 runner SHA from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked sigmac + VM v09; preserve runtime identities, all VM_RC, first generation-|||| branch, fourth-work result/action, fairness ledger counts and persisted recovery events.
4. If any gate fails, preserve evidence and repair only the narrow failure.
5. If V2.21 PASS, checkpoint it and then teach/admit a crash-consistent transactional state protocol before any production promotion.
