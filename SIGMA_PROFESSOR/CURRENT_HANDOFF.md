# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## Mandatory first read

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`

Global invariants:

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- teach reusable capabilities, not precomputed answers;
- dynamic/negative/persistence/replay/boundedness evidence as applicable;
- failures are evidence;
- claim scope must not exceed proof;
- dependency-first/capability-first ordering.

Still NOT PROVEN:

- semantic understanding;
- semantic curiosity;
- semantic truth validation;
- general autonomous reasoning;
- general autonomous mathematical research.

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

## Admitted curriculum chain

- V2.5B.2 real frozen corpus survey: PASS, 56/56 documents — checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted fixed-window segment cursor restart: PASS — checkpoint `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F complete fixture traversal: PASS — checkpoint `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7 structural grouping QA: PASS — checkpoint `bce7ce2decca4f6b644e96be67df339429429066`.
- V2.7P.1 persistent + bounded structural grouping: PASS — bytecode `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`, checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 persistent structural curriculum priority: PASS; locked-VM `to_int` PASS — checkpoint `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 actual 56-document survey -> native curriculum frontier: PASS; source `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`, bytecode `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`, checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected real work -> deep re-learn: PASS; source `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`, bytecode `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`, deep evidence `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`, checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A oracle-repaired structural revalidation: PASS.
  - native source `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`
  - runtime bytecode `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`
  - real baseline `of => the`
  - real result `NOT_REOBSERVED`
  - revalidation state `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`
  - fresh VM reuse/replay PASS; synthetic REOBSERVED and NOT_REOBSERVED branches PASS; incomplete -> PENDING; partial-evidence filter PASS; bounded refusal PASS.
  - failure oracle checkpoint `1cec7703a3cc9a730a5dd28155cb2d9c558441a8`
  - PASS checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.

## Important distinctions

- `DISPATCHED != COMPLETE`.
- `REOBSERVED != SEMANTICALLY TRUE`.
- `NOT_REOBSERVED != SEMANTICALLY FALSE`.
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.10R.1 structural revisit vs archive-for-now — SOURCE READY

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_REVALIDATION_TO_REVISIT_ARCHIVE_V2_10R1.sigma`

Source SHA256:
`67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993`

Source commit:
`dda94d592e6369ae54f2146f2150890b8c9e55c0`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V210R1_REVALIDATION_TO_REVISIT_ARCHIVE_PREFLIGHT.sh`

Runner SHA256:
`6a0f9749c640cf9477815daa7387765ba461b5822296a40bdb9fbd7ea905b6d2`

Runner commit:
`4fedebfc1641107bfafc4d65630c4a37dd406c81`

README commit:
`d2e4735c793fe90a24a4c3465d07a5ea57605a11`

Source-ready checkpoint:
`baca04cff585a85f7f6ec5b82c667ebec0d89b36`

Native lifecycle policy:

- committed `RESULT=NOT_REOBSERVED` -> `REVISIT`;
- committed `RESULT=REOBSERVED` -> `ARCHIVE_FOR_NOW`;
- no valid committed result -> `WAIT_FOR_REVALIDATION`;
- conflicting committed results -> `WAIT_FOR_REVALIDATION`;
- `ARCHIVE_FOR_NOW` deletes no evidence.

Lifecycle record:
`WORK=<id> || ACTION=<REVISIT|ARCHIVE_FOR_NOW> || FROM_RESULT=<result> || COMMIT=YES`

Admission runner regenerates the exact admitted real native chain first:

V2.8R.1 selection -> V2.8D.1 deep evidence -> V2.9R.1 revalidation -> V2.10 lifecycle.

Expected real structural branch under frozen current corpus:

- selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- revalidation `NOT_REOBSERVED`;
- native lifecycle action `REVISIT`.

Other required gates:

- synthetic `REOBSERVED` -> `ARCHIVE_FOR_NOW`;
- uncommitted revalidation -> WAIT/no mutation;
- conflicting revalidation -> WAIT/no mutation;
- fresh VM lifecycle-state reuse;
- deterministic replay;
- partial lifecycle record ignored;
- lifecycle/revalidation over-budget refusal;
- immutable real survey/document/deep-evidence/revalidation inputs.

Static source-ready truth:

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

Current admission truth:

- compile/runtime PASS = NOT_PROVEN;
- lifecycle bytecode SHA256 = UNKNOWN;
- admission = NOT_PROVEN;
- semantic truth validation = NOT_PROVEN;
- semantic understanding = NOT_PROVEN;
- bounded file I/O = NOT_PROVEN;
- mid-append crash atomicity = NOT_PROVEN.

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 running unless real VM failure.
2. Install exact V2.10R.1 source + runner above from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked compiler/VM; preserve lifecycle bytecode SHA and all VM_RC/state hashes.
4. If any gate fails, preserve evidence and repair only the narrow failing gate.
5. If PASS, checkpoint before building revisit execution + archive re-entry policy.
6. Preserve all raw/done/log/history/failure/QA evidence.
