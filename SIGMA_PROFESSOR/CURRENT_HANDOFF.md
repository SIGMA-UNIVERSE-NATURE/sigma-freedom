# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## Mandatory standard

Read first: `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`.

Global invariants:

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- teach reusable capabilities, not precomputed answers;
- runtime proof is required; compile/file existence alone is insufficient;
- failures are evidence; never weaken an admission gate to force PASS;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_CURIOSITY=NOT_PROVEN`;
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

Production source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Do not upgrade V2.4 in place while the newer continual-learning chain is still under admission.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey: PASS — checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted segment cursor restart: PASS — `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F full fixture traversal: PASS — `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping: PASS — runtime bytecode `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`, checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority: PASS — `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real survey -> native selected frontier: PASS; source `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`, bytecode `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`, checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work -> deep re-learn: PASS; source `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`, bytecode `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`, deep evidence `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`, checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation: PASS; source `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`, bytecode `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`, real baseline `of => the`, real result `NOT_REOBSERVED`, state `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`, PASS checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle decision: PASS; source `67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993`, bytecode `527bf0513082af49343f39b5ae23fd63b5c25f4034e019e934ca1d425890ef87`, real `NOT_REOBSERVED -> REVISIT`, lifecycle state `f34678fd6c85394ee659b6a710920bed8cc5ea07f8cbba0414cbb3bc116c79fb`; synthetic `REOBSERVED -> ARCHIVE_FOR_NOW`; missing/conflicting -> WAIT; archive deletes no evidence — checkpoint `220fa78bce0d9873533cb8acce102fc411107924`.

Important distinctions:

- `DISPATCHED != COMPLETE`;
- `REOBSERVED != SEMANTICALLY_TRUE`;
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`;
- `REVISIT != SEMANTICALLY_FALSE`;
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`;
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.11R.1 revisit execution + archive re-entry

Native source remains unchanged:

`SIGMA_REVISIT_EXECUTION_ARCHIVE_REENTRY_V2_11R1.sigma`

SHA256:
`88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`

### Runtime evidence already observed

The first V2.11 run produced valid native evidence for:

- `ARCHIVE_FOR_NOW` hold with no deletion;
- later committed `REVISIT` re-entering archived work;
- fresh-VM archive-reentry completion;
- no lifecycle action -> `WAIT_FOR_LIFECYCLE`;
- lifecycle over-limit refusal;
- evidence over-limit refusal.

Host remained non-cognitive: `HOST_REVISIT_EXECUTION=NO`, `HOST_ARCHIVE_REENTRY_DECISION=NO`, `HOST_DOCUMENT_SELECTION=NO`, `HOST_SEGMENT_SELECTION=NO`, `HOST_LEARNING=NO`.

### Admission failure preserved

V2.11 did NOT PASS admission in that run.

Failure checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V211R1_RUNNER_PRINTF_BOUND_SETUP_FAILURE.md`

Failure commit:
`f05ca0b5029a8436e95a9caecdfb93fc4cb32b9e`

Cause: the runner attempted to construct 65-pipe cursor fixtures with `printf '%0.s|' {1..65}`. Termux `printf` returned `invalid conversion specification`, so the intended generation-cursor limit fixture was not created. The native engine correctly treated the resulting ordinary cursor as executable work. This is a runner-fixture failure, not a native-logic failure.

### Repaired runner — REQUIRED NEXT RUN

Use:
`RUN_SIGMA_V211R1A_REVISIT_EXECUTION_ARCHIVE_REENTRY_PREFLIGHT.sh`

SHA256:
`31005526c5ec1a4c33ec1759965b9810e19198fae08235dc1ca16d8c5c739907`

Artifact commit:
`81a280e5b4836ad431ecb1feedcfa92d79b98eac`

Repair-ready checkpoint:
`3b285253abee2b0259682e3cca2551b71c7672dc`

Repair is runner-only:

- native source unchanged;
- admission criteria unchanged;
- bad `%0.s` format removed;
- generation-cursor bound fixture uses an explicit deterministic 65-iteration mechanical shell loop;
- segment-cursor bound fixture uses the same deterministic construction;
- `bash -n` RC = 0.

### Work-local revisit schema

For selected `<work>` inside a mechanical state directory:

- `<work>.generation` — one `|` per completed revisit generation;
- `<work>.cursor` — one `|` per committed segment in current generation;
- `<work>.evidence` — `WORK + GEN + CURSOR + BEST_LOCAL_RELATION + COMMIT=YES`.

Native policy:

- pending committed `REVISIT` -> execute bounded revisit;
- evidence commits before segment-cursor advance;
- generation advances only after document completion;
- latest `ARCHIVE_FOR_NOW` -> hold/no delete;
- later committed `REVISIT` -> archive re-entry;
- no committed lifecycle action -> wait.

Current archive re-entry proof scope:

- later committed `REVISIT` trigger: candidate/runtime partial evidence observed;
- time-based re-entry: `NOT_PROVEN`;
- semantic-novelty re-entry: `NOT_PROVEN`.

Important schema limitation:

V2.10 lifecycle records still lack unique event/epoch identity, so unrestricted repeated identical revisit epochs are NOT yet proven. Explicit event/generation identity remains a dependency for the autonomous cycle controller.

Current V2.11 admission truth:

- source compile/runtime partial evidence exists;
- final admission = `NOT_PROVEN` until repaired runner completes;
- generation-cursor bounded refusal = `NOT_PROVEN` for the failed run;
- segment-cursor bounded refusal = `NOT_PROVEN` for the failed run;
- semantic understanding = `NOT_PROVEN`;
- bounded file I/O = `NOT_PROVEN`;
- mid-append crash atomicity = `NOT_PROVEN`.

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. From repo root `~/SIGMA/sigma-freedom-write`, keep the exact V2.11 native source SHA above.
3. Replace only the runner with exact repaired V2.11R.1A runner SHA `31005526c5ec1a4c33ec1759965b9810e19198fae08235dc1ca16d8c5c739907`.
4. Run locked compiler/VM and preserve all VM_RC, V2.11 bytecode SHA, revisit evidence hashes, generation/cursor hashes and final bounded-refusal outputs.
5. If PASS, checkpoint before building autonomous cycle controller + explicit event/generation identity.
6. Preserve all raw/done/log/history/failure/QA evidence.
