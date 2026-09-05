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
- compile/file existence is not runtime proof;
- dynamic/negative/persistence/replay/boundedness evidence as applicable;
- failure is evidence;
- claim scope must not exceed proof;
- dependency-first/capability-first.

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

## Admitted curriculum / continual-learning chain

- V2.5B.2 real frozen corpus survey: PASS, 56/56 docs — checkpoint `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6 persisted fixed-window segment cursor restart: PASS — checkpoint `81c8c72e66c30292e17c567d8c3824490dc00e7a`.
- V2.6F full fixture traversal: PASS — checkpoint `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7 structural grouping QA: PASS — checkpoint `bce7ce2decca4f6b644e96be67df339429429066`.
- V2.7P.1 persistent + bounded structural grouping: PASS; bytecode `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49` — checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 persistent structural curriculum priority: PASS; locked-VM `to_int` PASS — checkpoint `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real 56-doc survey -> native curriculum frontier: PASS; source `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`, bytecode `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5` — checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected real work -> deep re-learn: PASS; source `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`, bytecode `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`, real deep evidence `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a` — checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A oracle-repaired structural revalidation: PASS; native source `94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`, runtime bytecode `c4fc06df3a1eb8f928a31e22d9d55090fc2fd53524d7e7c2e7c8265833d6a1f8`, real baseline `of => the`, real result `NOT_REOBSERVED`, state SHA `bb3fe964522fc68c716f0d3efc5d889acb637b473da4837df750d6db6c8305ac` — failure-oracle checkpoint `1cec7703a3cc9a730a5dd28155cb2d9c558441a8`, PASS checkpoint `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 structural lifecycle decision: PASS; source `67fb7234c0cd9e84c602a6dadb55f6e1ced6265406745ba6b3b9a7a95e0c4993`, runtime bytecode `527bf0513082af49343f39b5ae23fd63b5c25f4034e019e934ca1d425890ef87`, real `NOT_REOBSERVED -> REVISIT`, lifecycle state SHA `f34678fd6c85394ee659b6a710920bed8cc5ea07f8cbba0414cbb3bc116c79fb`; synthetic `REOBSERVED -> ARCHIVE_FOR_NOW`; missing/conflicting -> WAIT; archive deletes no evidence — checkpoint `220fa78bce0d9873533cb8acce102fc411107924`.

## Important distinctions

- `DISPATCHED != COMPLETE`.
- `REOBSERVED != SEMANTICALLY_TRUE`.
- `NOT_REOBSERVED != SEMANTICALLY_FALSE`.
- `REVISIT != SEMANTICALLY_FALSE`.
- `ARCHIVE_FOR_NOW != SEMANTICALLY_TRUE`.
- `ARCHIVE_FOR_NOW != FORGET`.

## Current frontier — V2.11R.1 revisit execution + archive re-entry — SOURCE READY

Goal:
Turn an admitted V2.10 `REVISIT` lifecycle action into a new bounded real learning generation, with work-local state and persistent fresh-VM segment resume. Keep `ARCHIVE_FOR_NOW` as a non-deleting hold state, and prove initial archive re-entry only when a later committed `REVISIT` lifecycle action exists.

User-delivery candidate:

- source: `SIGMA_REVISIT_EXECUTION_ARCHIVE_REENTRY_V2_11R1.sigma`
- source SHA256: `88568071e657cb94845d97d94237688ec62d88121f6ff90dc8cbc96cbe685d9e`
- runner: `RUN_SIGMA_V211R1_REVISIT_EXECUTION_ARCHIVE_REENTRY_PREFLIGHT.sh`
- runner SHA256: `47ba6cb8e1f6c93adb080a99a6cd3fb9c28d17ccf86f555dd04263265705030a`
- source-ready checkpoint: `1efe1f0e153a41d65e9c09b24aff2684b09f9cef`.

Static:

- `H_CALL_ARITY_AUDIT=PASS`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `DIRECT_STR_DEPENDENCY=NONE`;
- runner `bash -n` RC = 0;
- lifecycle/evidence/generation-cursor/segment-cursor bounds present and runtime admission tests prepared.

V2.11 work-local state:

For selected `<work>` in a mechanical state directory, SIGMA constructs:

- `<work>.generation` — one `|` per completed revisit generation;
- `<work>.cursor` — one `|` per committed segment in the current pending generation;
- `<work>.evidence` — `WORK + GEN + CURSOR + BEST_LOCAL_RELATION + COMMIT=YES`.

Native execution policy:

- latest committed `REVISIT` and revisit-event-count > completed-generation-count -> execute pending revisit;
- evidence commit precedes segment-cursor advance;
- generation advances only after document completion;
- segment cursor resets after generation completion;
- latest committed `ARCHIVE_FOR_NOW` -> hold, no evidence deletion;
- later committed `REVISIT` after archive -> re-enter active revisit execution;
- no committed lifecycle action -> wait.

Real admission target:

Regenerate exact admitted chain V2.8R.1 -> V2.8D.1 -> V2.9R.1 -> V2.10R.1 first, then execute the real REVISIT for selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`:

- generation token `|`;
- segment 0 `[0,8)` best relation `in => the`;
- fresh VM segment 1 `[8,10)` best relation `As => disagreements`;
- fresh VM completion -> generation cursor `|`, current segment cursor empty;
- post-completion fresh VM -> no pending revisit for the already executed lifecycle event;
- deterministic revisit-evidence replay required.

Archive gates:

- archive-only -> hold/no delete;
- archive then later committed revisit -> re-entry;
- time-based archive re-entry = NOT_PROVEN;
- semantic-novelty archive re-entry = NOT_PROVEN.

Important schema limitation:

V2.10 lifecycle records do not yet carry a unique epoch/event ID. Repeated identical REVISIT decisions for the same work/result are deduplicated upstream. V2.11R.1 proves execution of admitted lifecycle events, not unrestricted repeated identical revisit epochs. Explicit cycle/event identity is a required dependency for the later autonomous cycle controller.

Current runtime truth:

- V2.11 compile/runtime/admission = NOT_PROVEN;
- V2.11 bytecode SHA256 = UNKNOWN;
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
2. Install exact V2.11R.1 source + runner from repo root `~/SIGMA/sigma-freedom-write`.
3. Run locked compiler/VM; preserve V2.11 bytecode SHA, all VM_RC and work-local state/evidence hashes.
4. If any gate fails, preserve state and repair only the narrow failing gate.
5. If PASS, checkpoint before building the autonomous cycle controller with explicit event/generation identity.
6. Preserve all raw/done/log/history/failure/QA evidence.
