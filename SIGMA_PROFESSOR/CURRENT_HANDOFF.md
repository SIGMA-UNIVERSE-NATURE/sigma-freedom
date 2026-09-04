# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## READ FIRST

Mandatory global standard:
`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`

Core invariants:

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- teach reusable capabilities, not precomputed answers;
- compile success is not runtime proof;
- dynamic/negative/persistence/replay/boundedness evidence is required as applicable;
- failures are evidence;
- claim scope must not exceed proof;
- dependency-first/capability-first ordering.

Still NOT PROVEN:

- semantic understanding;
- semantic curiosity;
- general autonomous reasoning;
- general autonomous mathematical research.

## Locked runtime identities

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

## Production learner

V2.4 remains the production continuous learner. Keep it running unless it emits a real VM failure.

Production source:
`SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

Proven in tested scope:

- dynamic structural relations;
- persistent recurrence;
- native self-selection;
- cross-context support;
- native gap/query generation;
- Internet transport/decode -> native learning;
- long-context V2.4 execution without reproducing V2.3 step-limit failure.

## Curriculum / re-learning admitted chain

Design:
`SIGMA_PROFESSOR/DESIGN/SIGMA_CURRICULUM_RELEARNING_V1.md`

Lifecycle:

RAW_DOCUMENT
-> SURVEY
-> BOUNDED SEGMENT
-> STRUCTURAL PROFILE
-> GROUP
-> CURRICULUM PRIORITY
-> DEEP RE-LEARN
-> CONSOLIDATE
-> REVALIDATE
-> REVISIT

### V2.5B.2 full-corpus survey — PASS

- frozen snapshot = 56 real documents;
- committed survey = 56/56;
- native survey resume across invocations proven;
- empty-token contamination repaired;
- production raw/memory not mutated.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B2_FULL_CORPUS_SURVEY_PASS.md`

Commit:
`dca66b408fba5c21d081983d6ba15ca510e63c2c`

### V2.6 segment cursor restart — PASS

- fixed 8-line native segment windows;
- persisted cursor survives process termination between committed VM cycles;
- fresh run resumes next segment;
- segment computation bounded;
- bounded file I/O still NOT PROVEN.

Checkpoint commit:
`81c8c72e66c30292e17c567d8c3824490dc00e7a`

### V2.6F full-document traversal — PASS

63-line real frozen fixture traversed completely:
segments 0..7, completion at segment index 8.

Admitted:
`NATIVE_COMPLETE_FIXED_WINDOW_TRAVERSAL=PROVEN_IN_FIXTURE_SCOPE`

Checkpoint commit:
`97b2e047211d6606b0772daf451b6a9c16359946`

### V2.7 original structural grouping QA — PASS

Admitted in QA scope:

- native exact-anchor grouping;
- distinct doc-anchor dedup;
- dynamic input dependence;
- negative counterexample;
- deterministic replay;
- persisted assignments.

Checkpoint commit:
`bce7ce2decca4f6b644e96be67df339429429066`

### V2.7P.1 persistent + bounded grouping — PASS

Locked runtime evidence:

- source SHA256: `3142d5f5bcc75f7a7c3640be2352de373604713a39f977ef54ba14c414455163`;
- bytecode SHA256: `ec5d6fe79c07e97817c717da9a8c9634f3c0caa6e2bec1c1dcaeca8f0ba9fc49`;
- fresh VM process reuses committed grouping state;
- same-doc duplicate does not inflate support;
- different anchor remains singleton;
- partial/uncommitted state ignored;
- state/input over-budget refuse mutation;
- `STEP_LIMIT_STATUS=BOUNDED`.

Admitted:
`NATIVE_INCREMENTAL_STRUCTURAL_GROUPING=PROVEN_IN_QA_SCOPE`

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V27P1_PERSISTENT_STRUCTURAL_GROUPING_PASS.md`

Commit:
`3c98031845c42792c3bd58ba049e13013c60160b`

Still NOT PROVEN:
semantic grouping; bounded file I/O; mid-append crash atomicity.

### V2.8P.1 persistent curriculum priority — PASS

Admitted in QA scope:

- native structural curriculum priority;
- persistent dispatch state influences later fresh VM runs;
- fresh VM reuse;
- dynamic input dependence;
- all-complete negative case;
- deterministic first-encounter tie;
- deterministic replay;
- partial-state commit filter;
- bounded state/input refusal;
- locked-VM `to_int` runtime support proven.

Important invariant:
`DISPATCHED != COMPLETE`.

Checkpoint commit:
`5e375d2ffa210852a042d833f061b6cc6c969ecf`

### V2.8R.1 REAL 56-document survey -> curriculum bridge — PASS

Source SHA256:
`8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`

Observed bytecode SHA256:
`0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`

Real survey evidence:

- committed real documents = 56;
- distinct nonempty anchors = 31;
- first native selection:
  `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`;
- first selected anchor support = 15;
- fresh VM with persisted dispatch chose a different real document:
  `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`;
- deterministic replay reproduced exact first selection/state hashes;
- partial dispatch state ignored;
- state/survey over-budget refusal proven;
- real survey SHA unchanged.

Admitted:
`NATIVE_REAL_SURVEY_STRUCTURAL_FRONTIER=PROVEN_IN_FROZEN_SNAPSHOT_SCOPE`

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PASS.md`

Commit:
`ce7650b46026b6f4dc553618b198f48d1f1692d3`

Still NOT PROVEN:
semantic importance; semantic understanding; bounded file I/O; mid-append crash atomicity.

## CURRENT FRONTIER — V2.8D.1 selected real work -> deep re-learn

Goal:
connect native real curriculum selection directly to bounded deep re-learning of the selected real snapshot document.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma`

SOURCE_SHA256:
`3dfc25c5f6e9cdbabd193bb7c3d8845ba025cb12e1b3824430a1a6ec280ec74f`

Source commit:
`f2a55b9eb95af390ade88eb194b56f67cd8a1cd8`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V28D1_SELECTED_WORK_DEEP_RELEARN_PREFLIGHT.sh`

RUNNER_SHA256:
`461f4ca50add41e067a9402a64e2f7451b47c4491d08f3cc7b5f51b1c987f059`

Runner commit:
`5f8588849bfcb403777d6de94f1e3037a1175f44`

README commit:
`5f2ff35c8a355b4d5161c1a540c0b169f56c0c52`

Source-ready checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V28D1_SELECTED_WORK_DEEP_RELEARN_SOURCE_READY.md`

Checkpoint commit:
`74c76822b20a0f810db56cab6b70b6e54f64d7ce`

V2.8D.1 admission design:

1. re-run exact admitted V2.8R.1 natively on the real survey to produce a real selected work;
2. require first selection = `0ac783...66485b` under the frozen survey;
3. native deep engine reads selected work directly;
4. host provides snapshot directory path only as mechanical config;
5. SIGMA constructs selected document path itself;
6. native `file_exists` is exercised as a locked-VM mechanical ABI gate;
7. selected 10-line real document must traverse segment 0 `[0,8)`, fresh VM segment 1 `[8,10)`, then completion at segment index 2;
8. work-local cursor persisted;
9. deep evidence persisted with `WORK + CURSOR + BEST_LOCAL_RELATION + COMMIT=YES` provenance;
10. committed work/cursor evidence deduplicated before append;
11. deterministic evidence replay required;
12. empty selected-work negative case must refuse mutation;
13. over-budget evidence state must refuse mutation;
14. real survey and selected snapshot document must remain immutable.

Static source-ready checks:

- H-call arity PASS;
- no native `!=` dependency;
- no `str_starts` dependency;
- no direct `str()` dependency;
- runner `bash -n` RC=0.

Current truth:

- `V28D1_COMPILE_PASS=NOT_PROVEN`;
- `V28D1_RUNTIME_PASS=NOT_PROVEN`;
- deep bytecode SHA unknown until device compile;
- `V28D1_ADMISSION=NOT_PROVEN`;
- semantic importance NOT PROVEN;
- semantic understanding NOT PROVEN;
- bounded file I/O NOT PROVEN;
- mid-append crash atomicity NOT PROVEN.

## Advanced mathematics + beyond

Program design:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

MATH-R0..R8 are dependency/program identifiers only, not admission claims.
Do not load theorem-answer caches or Python cognition.

## 54 DNA

Directive:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Keep all 54 DNA. Active DNA cognition is native `.sigma`. Work dependency-first/capability-first.

## NEXT ACTION

1. Keep V2.4 production learner running unless real VM failure occurs.
2. Install exact V2.8D.1 source + runner.
3. Verify exact SHA256 identities.
4. Run V2.8D.1 on locked compiler/VM.
5. Preserve bridge bytecode identity, deep bytecode identity, every VM_RC, selected work, evidence/cursor hashes and refusal-test evidence.
6. If any gate fails, preserve state and repair only the narrow failing gate; do not weaken PASS criteria.
7. If V2.8D.1 passes, checkpoint it before building deep-relearn completion -> revalidation.
8. Preserve all prior raw/done/log/history/failure evidence.
