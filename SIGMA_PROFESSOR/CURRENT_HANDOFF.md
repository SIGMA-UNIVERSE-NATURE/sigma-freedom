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

Observed real shadow chain on the first work:

- generation `||` completed;
- exact-cycle `||` result `NOT_REOBSERVED`;
- lifecycle `REVISIT`;
- next native event `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b::|||::EXECUTE_REVISIT`.

Audit result:

- `V218R1_SHADOW_PRODUCTION_STARVATION_AUDIT=PASS`;
- `SHADOW_PRODUCTION_PROMOTION=BLOCKED`;
- `PROMOTION_BLOCKER=IMMEDIATE_CONSECUTIVE_REVISIT_STARVATION_RISK`;
- synthetic archive used = NO;
- production V2.4 remained running = PASS;
- shadow state namespace isolation = PASS;
- `PRODUCTION_PROMOTION_ALLOWED=NO`.

This does not invalidate the bounded V2.17 multi-document claim. It blocks production promotion because revisit fairness governance is missing.

## Current frontier — V2.19R.1 native revisit fairness / anti-starvation scheduler — SOURCE READY

New native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_REVISIT_FAIRNESS_ANTI_STARVATION_SCHEDULER_V2_19R1.sigma`

Source SHA256:
`e0734dbbdb6f0bad3d6577f9a9b20eb3a13dd9c3489caebd7f6f58bb15200ad0`

Source artifact commit:
`a03ec1d456c2e75b1ac251fbfdf0c7c0f03f0823`

User-delivery runner:
`RUN_SIGMA_V219R1_REVISIT_FAIRNESS_ANTI_STARVATION_PREFLIGHT.sh`

Runner SHA256:
`e390445d0fd7439043ea3fb75c90661d78fb0321245b2c81d959f508370dd8e1`

Source-ready checkpoint:
`dd4f05712073d7f360ff02bd9ef6e211e70cc108`

### Capability contract

Persistent fairness ledger:

`EVENT=<exact event> || STATUS=<PENDING|RESUMED> || AT=<dispatch-token> || COMMIT=YES`

Policy is structural and does NOT use a hardcoded revisit-count quota:

- if terminal stage is `EXECUTE_REVISIT` and committed survey work remains undispatched, persist the exact revisit event as PENDING and schedule `SELECT_NEXT_WORK`;
- native dispatch token = one `|` per unique committed selector dispatch;
- pending revisit matures only after selector dispatch progress plus a scheduling turn from a different work;
- oldest mature pending revisit resumes first;
- if the different work also requests revisit, persist that current event before the older event resumes, allowing queue rotation;
- if no undispatched alternative exists, revisit executes instead of being lost;
- revisit evidence is never deleted;
- host chooses neither fairness decision nor revisit priority.

### Admission gates

- exact real V2.18 starvation event against real frozen 56-document survey -> defer to `SELECT_NEXT_WORK`;
- fresh-VM same selector progress -> no duplicate pending record;
- synthetic A/B/C oldest-pending rotation;
- current revisit preserved while older pending revisit resumes;
- deterministic full queue replay with exact fairness-ledger hash;
- selector/survey inconsistency refusal with no fairness mutation;
- no-alternative revisit execution;
- `SELECT_NEXT_WORK` passthrough;
- partial fairness commit filter;
- invalid stage refusal;
- survey/selector/fairness bounded refusals.

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `DIRECT_STR_DEPENDENCY=NONE`;
- runner `bash -n` RC = 0.

### Claim limits before runtime admission

- `NATIVE_REVISIT_FAIRNESS_QUEUE=NOT_PROVEN`;
- `REAL_SHADOW_ANTI_STARVATION_INTEGRATION=NOT_PROVEN`;
- `PRODUCTION_PROMOTION_ALLOWED=NO`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Install exact V2.19 source SHA `e0734dbb...200ad0` and runner SHA `e390445d...dd8e1` from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked sigmac + VM v09 and preserve printed runtime identities, bytecode SHA, every VM_RC, scheduled events and fairness-state hashes.
4. If any gate fails, preserve evidence and repair only the narrow failure.
5. If V2.19 PASS, checkpoint before integrating fairness into the real V2.18 shadow-production chain; production promotion remains blocked until that integration passes.
