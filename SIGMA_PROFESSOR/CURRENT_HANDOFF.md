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
  - checkpoint commit `dca66b408fba5c21d081983d6ba15ca510e63c2c`
- V2.6 persisted fixed-window segment cursor restart: PASS.
  - checkpoint commit `81c8c72e66c30292e17c567d8c3824490dc00e7a`
- V2.6F complete 63-line fixture traversal: PASS.
  - checkpoint commit `97b2e047211d6606b0772daf451b6a9c16359946`
- V2.7 original structural grouping QA: PASS.
  - checkpoint commit `bce7ce2decca4f6b644e96be67df339429429066`
- V2.7P.1 persistent + bounded structural grouping: PASS.
  - bytecode SHA256 `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`
  - checkpoint commit `3c98031845c42792c3bd58ba049e13013c60160b`
- V2.8P.1 persistent structural curriculum priority: PASS.
  - persistent dispatch across fresh VM; dynamic/negative/tie/replay/partial-state/bounded gates PASS;
  - locked-VM `to_int` runtime PASS;
  - checkpoint commit `5e375d2ffa210852a042d833f061b6cc6c969ecf`
- V2.8R.1 actual 56-document survey -> native curriculum frontier: PASS.
  - source SHA256 `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
  - bytecode SHA256 `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
  - first real selected work `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
  - fresh VM next selected work `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`
  - checkpoint commit `ce7650b46026b6f4dc553618b198f48d1f1692d3`

Important distinction:
`DISPATCHED != COMPLETE`.

## Current frontier — V2.8D.1 selected real work -> deep re-learn

Goal:
Native curriculum selects the real document first; deep-relearn engine then consumes that selected work directly, resolves the frozen snapshot document natively, traverses bounded 8-line segments with persistent work-local cursor, and persists segment provenance evidence.

Candidate user-delivery identities after pre-runtime ABI hardening:

- source file: `SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma`
- source SHA256: `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
- runner file: `RUN_SIGMA_V28D1_SELECTED_WORK_DEEP_RELEARN_PREFLIGHT.sh`
- runner SHA256: `7b53912116383027bcba00fa6393ded61d2de0b74a7219af36148bfd2273353a`

Base source artifact commit before bool-render hardening:
`f2a55b9eb95af390ade88eb194b56f67cd8a1cd8`

Base runner artifact commit:
`5f8588849bfcb403777d6de94f1e3037a1175f44`

Bool-render hardening checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V28D1_FILE_EXISTS_BOOL_HARDENING.md`

Hardening commit:
`fbb345abe1399fd5c5f8aab951f9d12ea84f6712`

V2.8D.1 runtime admission targets:

1. re-run exact admitted V2.8R.1 on actual survey to produce first real selected work;
2. require selected work = `0ac783...66485b` under frozen survey;
3. native deep engine constructs `<snapshot>/<selected>.document` from selected ID + mechanical snapshot-dir config;
4. locked-VM `file_exists` exercised; its boolean is converted natively to numeric 0/1 before protocol use;
5. selected real 10-line document: segment 0 `[0,8)`, fresh VM segment 1 `[8,10)`, completion at segment index 2;
6. evidence record: `WORK + CURSOR + BEST_LOCAL_RELATION + COMMIT=YES`;
7. committed work/cursor evidence dedup before append;
8. deterministic evidence replay required;
9. empty selected-work negative must refuse mutation;
10. over-budget evidence state must refuse mutation;
11. actual V2.5 survey and selected snapshot document must remain immutable.

Current truth:

- V2.8D.1 compile/runtime/admission NOT PROVEN;
- semantic importance NOT PROVEN;
- semantic understanding NOT PROVEN;
- bounded file I/O NOT PROVEN;
- mid-append crash atomicity NOT PROVEN.

## Other lanes

54 DNA directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Advanced mathematics program:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Keep all 54 DNA; active cognition remains native `.sigma`; no Python cognition.

## NEXT ACTION

1. Keep V2.4 running.
2. Install the exact V2.8D.1 user-delivery source + runner using the hashes above.
3. Run on locked compiler/VM and preserve exact bridge/deep bytecode hashes and every VM_RC.
4. If any gate fails, preserve state and repair only the narrow failing gate.
5. If PASS, checkpoint before building deep-relearn completion -> revalidation.
6. Preserve all raw/done/log/history/failure evidence.
