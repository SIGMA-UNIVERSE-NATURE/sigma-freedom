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

- V2.5B.2 real frozen corpus survey: PASS, 56/56 documents.
  - checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`
- V2.6 persisted fixed-window segment cursor restart: PASS.
  - checkpoint `81c8c72e66c30292e17c567d8c3824490dc00e7a`
- V2.6F complete fixture traversal: PASS.
  - checkpoint `97b2e047211d6606b0772daf451b6a9c16359946`
- V2.7 original structural grouping QA: PASS.
  - checkpoint `bce7ce2decca4f6b644e96be67df339429429066`
- V2.7P.1 persistent + bounded structural grouping: PASS.
  - bytecode SHA256 `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`
  - checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`
- V2.8P.1 persistent structural curriculum priority: PASS.
  - locked-VM `to_int` runtime PASS;
  - checkpoint `5e375d2ffa210852a042d833f061b6cc6c969ecf`
- V2.8R.1 actual 56-document survey -> native curriculum frontier: PASS.
  - source SHA256 `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
  - bytecode SHA256 `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
  - first real selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
  - checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`
- V2.8D.1 selected real work -> deep re-learn: PASS.
  - source SHA256 `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
  - bytecode SHA256 `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`
  - deep evidence SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`
  - checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`
- V2.9R.1A oracle-repaired structural revalidation: PASS.
  - native source SHA256 `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`
  - runtime bytecode SHA256 `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`
  - repaired admission runner SHA256 `027288207db6e52e087d7d9cb2eea262989c6afdb657af01f37d1824fe9c7717`
  - real baseline `of => the`
  - real deep segment anchors `in => the`, `As => disagreements`
  - real result `NOT_REOBSERVED`
  - real revalidation state SHA256 `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac`
  - fresh-VM reuse PASS; deterministic replay PASS;
  - synthetic `REOBSERVED` branch PASS;
  - synthetic `NOT_REOBSERVED` branch PASS;
  - incomplete -> `PENDING` PASS;
  - partial evidence commit filter PASS;
  - state/evidence/survey bounded refusal PASS;
  - checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.

## Important failure evidence

The first V2.9 runner hardcoded the real baseline as `in => the` and expected `REOBSERVED`.
Runtime proved the real committed V2.5 baseline was `of => the`, so native SIGMA correctly returned `NOT_REOBSERVED`.
The native source was not weakened; only the test oracle was repaired.

Failure checkpoint:
`1cec7703a3cc9a730a5dd28155cb2d9c558441a8`

## Important distinctions

- `DISPATCHED != COMPLETE`.
- `REOBSERVED != SEMANTICALLY TRUE`.
- `NOT_REOBSERVED != SEMANTICALLY FALSE`.
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.10R.1 structural revisit vs archive-for-now

Goal:
Consume only committed native revalidation state and decide a lifecycle action structurally:

- `RESULT=NOT_REOBSERVED` -> `REVISIT`;
- `RESULT=REOBSERVED` -> `ARCHIVE_FOR_NOW`;
- missing/uncommitted/pending revalidation -> `WAIT_FOR_REVALIDATION` and no lifecycle commit.

This is a curriculum scheduling state transition only. It is NOT a truth judgment and does not delete raw documents, survey history, deep evidence, or revalidation evidence.

Required gates:

1. real admitted V2.9 result `NOT_REOBSERVED` must produce native `REVISIT`;
2. synthetic committed `REOBSERVED` must produce `ARCHIVE_FOR_NOW`;
3. incomplete/uncommitted revalidation must produce `WAIT_FOR_REVALIDATION` with no lifecycle mutation;
4. committed lifecycle state must survive fresh VM and deduplicate exact work/action;
5. deterministic replay;
6. partial lifecycle records ignored;
7. bounded revalidation/lifecycle state refusal before mutation;
8. no mutation to real survey, selected document, deep evidence or revalidation evidence.

Host boundary:

- `HOST_LIFECYCLE_DECISION=NO`
- `HOST_REVISIT_DECISION=NO`
- `HOST_ARCHIVE_DECISION=NO`
- `HOST_TRUTH_DECISION=NO`
- `HOST_LEARNING=NO`

Claim scope:

- structural lifecycle scheduling only;
- semantic truth NOT PROVEN;
- semantic understanding NOT PROVEN.

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 running unless real VM failure.
2. Build V2.10R.1 native structural lifecycle transition preflight.
3. Preserve V2.9 real `NOT_REOBSERVED` as evidence; do not transform it into semantic falsehood.
4. Prove both `REVISIT` and `ARCHIVE_FOR_NOW` branches, fresh-VM persistence, replay, partial-state filtering and boundedness.
5. Checkpoint PASS before considering consolidation/revisit execution policy.
6. Preserve all raw/done/log/history/failure/QA evidence.
