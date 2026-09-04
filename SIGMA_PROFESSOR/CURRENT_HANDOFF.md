# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## READ THIS FIRST

Before substantive SIGMA teaching/development, read:

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`

Global invariants:

- teach capabilities, not precomputed answers;
- active cognition is native `.sigma` only;
- Python may remain historical/reference only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- compile success is not runtime proof;
- dynamic-input evidence is required;
- failures are evidence;
- claim scope must not exceed proof;
- dependency-first/capability-first ordering.

Still NOT PROVEN:

- semantic understanding;
- semantic curiosity;
- general autonomous reasoning.

## Locked runtime identities

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

## V2.4 production learner

Keep V2.4 running unless it emits a real VM failure.

Proven in tested scope:

- dynamic structural relation generation;
- persistent recurrence;
- native self-selection;
- cross-context support;
- native gap/query generation;
- Internet transport/decode -> native `mode=NEW` learning;
- previously failing long context completes without reproducing V2.3 step-limit failure.

Production source:
`SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma`

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

## Curriculum / re-learning lifecycle

Read:
`SIGMA_PROFESSOR/DESIGN/SIGMA_CURRICULUM_RELEARNING_V1.md`

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

## V2.5 full-corpus survey — PASS

Frozen mechanical snapshot:

`SNAPSHOT_DOCUMENT_COUNT=56`

Final proof:

- `SURVEY_COMPLETE YES`;
- `COMMITTED_SURVEY_COUNT=56`;
- `SURVEY_COMPLETE_SENTINEL=1`;
- `PRODUCTION_RAW_MUTATED=NO`;
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`;
- `HOST_LEARNING=NO`;
- `HOST_DOCUMENT_SELECTION=NO`;
- `V25B_2_FULL_CORPUS_SURVEY=PASS`.

Admitted claim:

`NATIVE_STRUCTURAL_FULL_CORPUS_SURVEY=PROVEN_FOR_FROZEN_56_DOCUMENT_SNAPSHOT`

`PERSISTENT_SURVEY_RESUME_ACROSS_RUNNER_INVOCATIONS=PROVEN_IN_TESTED_SCOPE`

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B2_FULL_CORPUS_SURVEY_PASS.md`

Commit:
`dca66b408fba5c21d081983d6ba15ca510e63c2c`

Historical failure evidence retained:

- original V2.5B: `str_starts` runtime incompatibility;
- V2.5B.1: empty-token contamination (`BEST_LOCAL_RELATION= =>`, support 110);
- tainted V2.5B.1 state must not be promoted.

## V2.6 persisted segment cursor restart — PASS

Fixture:

`ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac.document`

Observed line count: 63.

Phase 1:

- `SEGMENT_INDEX 0`;
- `SEGMENT_START_LINE 0`;
- `SEGMENT_END_LINE 8`;
- `CURSOR_APPEND_RC 0`;
- `CURSOR_BYTES_AFTER=1`;
- runner deliberately terminated after committed VM cycle.

Fresh runner invocation:

- `V26_INITIALIZATION=REUSE_PERSISTED_CURSOR`;
- `CURSOR_BYTES_BEFORE=1`;
- `RECOVERY_DETECTED=YES`;
- `SEGMENT_INDEX 1`;
- `SEGMENT_START_LINE 8`;
- `SEGMENT_END_LINE 16`;
- `CURSOR_BYTES_AFTER=2`;
- `PERSISTED_CURSOR_RESUME_AFTER_PROCESS_TERMINATION=PASS`.

Admitted claim:

- SIGMA derives next fixed segment from persisted cursor;
- host does not select segment;
- restart between committed VM cycles resumes the next segment;
- segment computation is bounded.

Not proven:

- bounded file I/O;
- atomic recovery from kill during `append_text`;
- semantic understanding.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V26_SEGMENT_CURSOR_RESTART_PREFLIGHT_PASS.md`

Commit:
`81c8c72e66c30292e17c567d8c3824490dc00e7a`

## V2.6F complete full-document segment traversal — PASS

Same 63-line frozen fixture traversed with fixed 8-line native cursor windows.

Expected windows were completed:

- segment 0 `[0,8)`;
- segment 1 `[8,16)`;
- segment 2 `[16,24)`;
- segment 3 `[24,32)`;
- segment 4 `[32,40)`;
- segment 5 `[40,48)`;
- segment 6 `[48,56)`;
- segment 7 `[56,63)`;
- completion sentinel at segment index 8.

Final device proof:

- `VM_RC=0`;
- `DOCUMENT_SEGMENTS_COMPLETE YES`;
- `LINE_TOTAL 63`;
- `SEGMENT_INDEX 8`;
- `SEGMENT_START_LINE 64`;
- `CURSOR_BYTES_AT_START=6`;
- `CURSOR_BYTES_AT_END=8`;
- `DOCUMENT_COMPLETE_SENTINEL=1`;
- `HOST_SEGMENT_SELECTION=NO`;
- `HOST_LEARNING=NO`;
- `SEGMENT_COMPUTATION_BOUNDED=YES`;
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`;
- `V26F_FULL_DOCUMENT_TRAVERSAL=PASS`.

Admitted claim:

`NATIVE_COMPLETE_FIXED_WINDOW_TRAVERSAL=PROVEN_IN_FIXTURE_SCOPE`

Evidence-empty segments are valid and must not force fabricated knowledge.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V26F_FULL_DOCUMENT_SEGMENT_TRAVERSAL_PASS.md`

Commit:
`97b2e047211d6606b0772daf451b6a9c16359946`

## V2.7 original structural grouping package — SOURCE READY, RUNTIME PASS NOT CHECKPOINTED

Goal:

Prove native structural grouping without topic taxonomy or host semantic classification.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_STRUCTURAL_GROUPING_V2_7P.sigma`

SOURCE_SHA256:
`ab6eb3bf5e8796f2ec4b772159d70c648458fd85895f59f521407ab4209d6419`

Source artifact latest commit:
`5e19321003c600982d57771dec8c024cfc0d0541`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V27_STRUCTURAL_GROUPING_PREFLIGHT.sh`

RUNNER_SHA256:
`420ae29866f39cc087cc95f28b8c1099785d0faf7af51c88727ef3b0bcc325fd`

Runner artifact latest commit:
`7f8e8cc777e8a1a06fcb7e154ca0646ffff6443d`

README latest commit:
`9506073238eafc2967ca57d3fdb9d17ced138314`

V2.7 policy:

- profile input shape: `DOC=<id> || ANCHOR=<structural relation>`;
- SIGMA deduplicates exact document-anchor pairs;
- repeated same doc-anchor pair must not inflate cross-document support;
- exact anchor support >1 across distinct admitted doc-anchor pairs -> `GROUP=SHARED`;
- support 1 -> `GROUP=SINGLETON`;
- assignments are written by native SIGMA to `.sigma_exec/SIGMA_V27T_GROUP_ASSIGNMENTS.memory`;
- host supplies QA bytes and mechanically checks protocol/hash only;
- host does not choose groups or classify topics.

Same bytecode admission cases prepared:

### Positive

- two shared-anchor groups;
- 4 grouped documents;
- 1 singleton;
- 1 duplicate profile ignored.

### Negative / counterexample

- no shared anchor across distinct documents;
- 0 groups;
- 0 grouped documents;
- 5 singletons;
- duplicate within same document must still not create a group.

### Replay

Exact positive input must reproduce exact assignment SHA.

Static checks recorded:

- `H_CALL_ARITY_AUDIT=PASS`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `DIRECT_STR_DEPENDENCY=NONE`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- runner `bash -n=PASS`;
- runner failure RC propagation audit PASS.

No durable runtime PASS checkpoint for this package was found during the latest bootstrap. Source/runner existence must not be treated as admission.

## ADVANCED MATHEMATICS + BEYOND PROGRAM — INITIALIZED

Read:
`SIGMA_PROFESSOR/DESIGN/SIGMA_ADVANCED_MATHEMATICS_BEYOND_CAPABILITY_PROGRAM_V1.md`

Program commit:
`0ee78a4981e73d50f0fc928cd62ef04f8213b3df`

Mission:
transform advanced mathematics and beyond into native reusable capability families, not theorem-answer caches or host-selected lessons.

Program families:

- `MATH-R0`: representation, domain/preconditions, exactness, evidence, counterexamples;
- `MATH-R1`: arithmetic/algebra/discrete structures;
- `MATH-R2`: linear algebra/geometry substrate;
- `MATH-R3`: calculus and real/complex analysis;
- `MATH-R4`: differential equations, dynamics, probability, optimization;
- `MATH-R5`: abstract algebra, topology, measure, functional analysis;
- `MATH-R6`: advanced geometry and number theory;
- `MATH-R7`: category/homological/compositional and higher abstractions;
- `MATH-R8`: proof, theorem discovery, and research behavior.

These IDs are program/dependency identifiers only. They are NOT admission claims.

`GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## CURRENT FRONTIER — V2.7P.1 strict persistent + bounded structural grouping

The global teaching standard requires persistent-state/restart evidence for curriculum capabilities and boundedness evidence for history/corpus scans. Therefore the next admission gate is the strict P1 package, not a source-existence inference from V2.7.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_STRUCTURAL_GROUPING_V2_7P_1.sigma`

Durable exact identity:
`SOURCE_SHA256=3142d5f5bcc75f7a7c3640be2352de373604713a39f977ef54ba14c414455163`
`GIT_BLOB_SHA1=88e52075c8d1025d2034da7c732c30f8eda86d35`

Source commit:
`b56190825a5aaff9436d1b2994ee58922459363a`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT.sh`

Runner exact identity:
`RUNNER_SHA256=9ff2269fb1450f3d128200e52b89ce1c800fa427a000131a9f9f91823054e3f5`
`GIT_BLOB_SHA1=4dec69928adf701062a3ffa5694dbd8e301b275d`

Runner pin-fix commit:
`37bc7138afce4ba75f005e7997250ba7761feb94`

README:
`SIGMA_PROFESSOR/artifacts/SIGMA_V27P1_PERSISTENT_STRUCTURAL_GROUPING_PREFLIGHT_README.txt`

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_ADVANCED_MATH_BEYOND_PROGRAM_V27P1_SOURCE_READY.md`

Checkpoint commit:
`3dfa40edeb0863f3d8031af764ac8dc22ac497a3`

P1 native policy:

- prior state is reused only from complete `COMMIT=YES` records;
- malformed/uncommitted state is ignored;
- exact doc-anchor pairs are deduplicated;
- second fresh VM process must be able to turn A/X singleton into A+B/X shared by reading prior committed state;
- same-document duplicate must not inflate support;
- different anchor remains singleton;
- state split-line budget = 65;
- input split-line budget = 16;
- over-budget state/input must refuse mutation before record scan.

Static source-ready audit:

- `H_CALLS=56`;
- `H_CALL_ARITY_AUDIT=PASS`;
- `STR_STARTS_DEPENDENCY=NONE`;
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`;
- runner `bash -n` RC = 0;
- durable byte identity checks PASS.

Current admission truth:

- `COMPILE_PASS=NOT_PROVEN`;
- `RUNTIME_PASS=NOT_PROVEN`;
- `BYTECODE_SHA256=UNKNOWN`;
- `VM_RC=UNKNOWN`;
- `OUTPUT_DEPENDS_ON_INPUT=NOT_PROVEN`;
- `NEGATIVE_TEST=NOT_PROVEN`;
- `PERSISTENT_STATE_TEST=NOT_PROVEN`;
- `RESTART_REPLAY_TEST=NOT_PROVEN`;
- `STEP_LIMIT_STATUS=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`;
- `ADMISSION=NOT_PROVEN`;
- `PRODUCTION_STATE_MUTATED=NO`.

Claim scope is structural exact-anchor grouping in the bounded synthetic QA protocol only. No semantic grouping, semantic understanding, curriculum priority, mathematical understanding, or production readiness is claimed.

After a real locked-runtime P1 admission PASS:

`NEXT_ACTION=BUILD_V28_CURRICULUM_PRIORITY_PREFLIGHT`

Only after declared dependencies are admitted should the smallest `MATH-R0` native mathematical cognition capabilities begin admission.

## Host ABI status

Source inventory found 93 host operations. Important exact findings:

- `read_bytes` reads whole file into O_BYTES;
- `write_text` / `append_text` are plain stdio, not atomic;
- `crypto_digest` hashes VM strings via OpenSSL EVP;
- `net_fetch` is libcurl body transport with redirect follow + 5s timeout;
- JSON decode currently routes through `json_decode_scalar_text`; nested structured JSON is NOT proven;
- `list_sort` is in-place ascending and approximately O(n^2);
- Unicode-aware normalization is NOT proven;
- do not use `str_starts` without dedicated ABI characterization.

Do not add broad host tools without native failure evidence.

## 54 DNA lane

Read:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Keep all 54 DNA. Active DNA cognition must be native `.sigma`. Work dependency-first/capability-first.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. Install the exact V2.7P.1 source + runner into an isolated Termux preflight namespace.
3. Run V2.7P.1 with the locked compiler/VM; preserve exact source/bytecode/runtime hashes, every VM_RC, logs and state hashes.
4. If any case fails, preserve state and repair the narrowest failing gate; do not weaken PASS criteria.
5. If P1 passes all dynamic, negative, persistence and boundedness gates in its claim scope, checkpoint the exact admission evidence.
6. Then build V2.8 persistent native curriculum priority/resume.
7. Begin `MATH-R0` capability admission only when its declared dependencies are satisfied; do not load precomputed advanced-math results.
8. Preserve all prior raw/done/log/history state and all failure evidence.
