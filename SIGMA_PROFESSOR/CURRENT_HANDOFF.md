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
- V2.6F complete 63-line fixture traversal: PASS.
  - checkpoint `97b2e047211d6606b0772daf451b6a9c16359946`
- V2.7 original structural grouping QA: PASS.
  - checkpoint `bce7ce2decca4f6b644e96be67df339429429066`
- V2.7P.1 persistent + bounded structural grouping: PASS.
  - bytecode SHA256 `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`
  - checkpoint `3c98031845c42792c3bd58ba049e13013c60160b`
- V2.8P.1 persistent structural curriculum priority: PASS.
  - persistent dispatch across fresh VM; dynamic/negative/tie/replay/partial-state/bounded gates PASS;
  - locked-VM `to_int` runtime PASS;
  - checkpoint `5e375d2ffa210852a042d833f061b6cc6c969ecf`
- V2.8R.1 actual 56-document survey -> native curriculum frontier: PASS.
  - source SHA256 `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
  - bytecode SHA256 `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
  - first real selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
  - fresh VM next selected work `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`
  - checkpoint `ce7650b46026b6f4dc553618b198f48d1f1692d3`
- V2.8D.1 selected real work -> deep re-learn: PASS.
  - source SHA256 `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
  - bytecode SHA256 `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`
  - real selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
  - segment 0 `[0,8)` best relation `in => the`, support 6;
  - fresh VM segment 1 `[8,10)` best relation `As => disagreements`, support 1;
  - fresh VM completion at segment index 2;
  - two committed deep-evidence records;
  - deep evidence SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`;
  - deterministic replay exact hash PASS;
  - empty-selection negative PASS;
  - over-budget evidence refusal PASS;
  - locked-VM `file_exists` runtime PASS;
  - real survey and selected document immutable;
  - checkpoint `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.

Important distinctions:

- `DISPATCHED != COMPLETE`.
- `REOBSERVED != SEMANTICALLY TRUE`.

## Current frontier — V2.9R.1 deep re-learn completion -> structural revalidation

Goal:
Only after native deep re-learning is complete, compare the old committed V2.5 survey anchor with committed V2.8D.1 deep segment best-anchor evidence.

Candidate source:
`SIGMA_PROFESSOR/artifacts/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigma`

Source SHA256:
`94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`

Source commit:
`36cb16d33eeb08d048c182499d4fc1e1a1ad0c53`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V29R1_DEEP_RELEARN_STRUCTURAL_REVALIDATION_PREFLIGHT.sh`

Runner SHA256:
`c87fdcd46587b3e0200eed4be1f631ee5c2d5b270c1ef2a10141bd94e1ad4ce7`

Runner commit:
`be85ac96d98ece276295601c82a094ead19d88b4`

README commit:
`89d9cd584e9b65a052c55cd7af6b97ea73defa27`

Source-ready checkpoint:
`699a0b53ab85266037d85efdb6b2cad87c9fc1cf`

### Intended real positive

Selected work:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

Old V2.5 baseline anchor:
`in => the`

Committed deep segment anchors:

- cursor `""`: `in => the`
- cursor `"|"`: `As => disagreements`

Expected V2.9 result:

- `DEEP_RELEARN_COMPLETE 1`
- `ACTIVE_WORK_MATCH 1`
- `BASELINE_FOUND 1`
- `COMMITTED_DEEP_SEGMENT_COUNT 2`
- `MATCHING_BASELINE_SEGMENT_COUNT 1`
- `DISTINCT_DEEP_ANCHOR_COUNT 2`
- `REVALIDATION_READY 1`
- `REVALIDATION_RESULT REOBSERVED`

This is only structural recurrence evidence. No semantic truth is claimed.

### Critical D1 terminal-state handling

The admitted V2.8D.1 runner ended with a synthetic over-limit evidence fixture as part of its boundedness test. Therefore the terminal D1 evidence file must NOT be consumed as real deep evidence.

The V2.9R.1 runner must:

1. preserve terminal D1 QA state as reference;
2. rerun exact admitted V2.8R.1 to regenerate real selected work;
3. rerun exact admitted V2.8D.1 through segment 0, segment 1, completion;
4. require regenerated deep evidence SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`;
5. only then invoke V2.9R.1.

### Admission gates prepared

- real positive -> `REOBSERVED`;
- fresh VM persistent revalidation state reuse, no duplicate append;
- deterministic replay;
- synthetic completed counterexample -> `NOT_REOBSERVED`;
- incomplete deep traversal -> `PENDING` with no state mutation;
- partial/uncommitted matching evidence ignored;
- state/evidence/survey over-budget refusal;
- real survey/document/regenerated deep evidence immutable.

Static source-ready truth:

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

Current admission truth:

- `COMPILE_PASS=NOT_PROVEN`
- `RUNTIME_PASS=NOT_PROVEN`
- `BYTECODE_SHA256=UNKNOWN`
- `ADMISSION=NOT_PROVEN`
- `STRUCTURAL_REVALIDATION_ONLY=YES`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 running unless real VM failure.
2. Install exact V2.9R.1 source + runner above.
3. Run on locked compiler/VM; preserve exact revalidation bytecode SHA, every VM_RC, state/evidence hashes and logs.
4. If any gate fails, preserve state and repair only the narrow failing gate.
5. If PASS, checkpoint before building `REVALIDATION -> REVISIT_OR_ARCHIVE_FOR_NOW`.
6. Preserve raw/done/log/history/failure/QA reference evidence.
