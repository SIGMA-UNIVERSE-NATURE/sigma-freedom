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

V2.5B.2 final device evidence:

- final `VM_RC=0`;
- `SURVEY_COMPLETE YES`;
- `COMMITTED_SURVEY_COUNT=56`;
- `SURVEY_COMPLETE_SENTINEL=1`;
- `PRODUCTION_RAW_MUTATED=NO`;
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`;
- `HOST_LEARNING=NO`;
- `HOST_DOCUMENT_SELECTION=NO`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `V25B_2_FULL_CORPUS_SURVEY=PASS`.

Proven claim scope:

`NATIVE_STRUCTURAL_FULL_CORPUS_SURVEY=PROVEN_FOR_FROZEN_56_DOCUMENT_SNAPSHOT`

`PERSISTENT_SURVEY_RESUME_ACROSS_RUNNER_INVOCATIONS=PROVEN_IN_TESTED_SCOPE`

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B2_FULL_CORPUS_SURVEY_PASS.md`

Checkpoint commit:
`dca66b408fba5c21d081983d6ba15ca510e63c2c`

Historical failures retained as evidence:

- original V2.5B: `str_starts` runtime incompatibility;
- V2.5B.1: empty-token contamination (`BEST_LOCAL_RELATION= =>`, support 110);
- tainted V2.5B.1 state must not be promoted.

## V2.6 bounded segment cursor restart preflight — PASS

Fixture:

`ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac.document`

Observed line count: 63.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_BOUNDED_SEGMENT_CURSOR_V2_6P.sigma`

Source SHA256:
`9cac5d9ddb10295b3ebf1f4300412e1b6dc3adceaf5f1de70eb83d0508f3b970`

Observed bytecode SHA256:
`e850848a9b0fc8905ae50ddf609e28235a1c431fe045011bd88d9fc0c39e33b2`

Phase 1 evidence:

- `VM_RC=0`;
- `SEGMENT_INDEX 0`;
- `SEGMENT_START_LINE 0`;
- `SEGMENT_END_LINE 8`;
- `CURSOR_APPEND_RC 0`;
- `CURSOR_BYTES_AFTER=1`;
- runner deliberately terminated its own process after the commit.

Phase 2 fresh runner invocation:

- `V26_INITIALIZATION=REUSE_PERSISTED_CURSOR`;
- `CURSOR_BYTES_BEFORE=1`;
- `RECOVERY_DETECTED=YES`;
- `VM_RC=0`;
- `SEGMENT_INDEX 1`;
- `SEGMENT_START_LINE 8`;
- `SEGMENT_END_LINE 16`;
- `CURSOR_APPEND_RC 0`;
- `CURSOR_BYTES_AFTER=2`;
- `V26_BOUNDED_SEGMENT_CURSOR_PREFLIGHT=PASS`;
- `PERSISTED_CURSOR_RESUME_AFTER_PROCESS_TERMINATION=PASS`.

Proven claim scope:

- SIGMA derives the next fixed 8-line segment from persistent cursor state;
- host does not select the next segment;
- restart between committed VM cycles resumes the next segment;
- segment computation is bounded.

Not proven:

- bounded file I/O (`read_text` still loads whole file);
- atomic recovery from kill during `append_text`;
- semantic understanding.

Important observation:

Segment 1 produced zero valid relations and many skipped empty relations. This does not invalidate cursor proof. Future grouping/curriculum must tolerate evidence-empty segments rather than forcing every segment to yield knowledge.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V26_SEGMENT_CURSOR_RESTART_PREFLIGHT_PASS.md`

Checkpoint commit:
`81c8c72e66c30292e17c567d8c3824490dc00e7a`

## CURRENT FRONTIER — V2.6F complete full-document segment traversal

Goal:

Prove complete traversal of the 63-line fixture using persistent native cursor before moving to structural grouping.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_FULL_DOCUMENT_SEGMENT_CURSOR_V2_6F.sigma`

SOURCE_SHA256:
`adfadcb91e71a38272d09dfc27997faf915ab71666993c67e9288e69b5b3a366`

Source artifact commit:
`0194c6278c8d83a3625a54e3a946bb87996cf1cd`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V26F_FULL_DOCUMENT_SEGMENT_CURSOR_BATCHED.sh`

RUNNER_SHA256:
`506f606dd110141b2f78b90ec96df4dfb01ea1f8340824ea0ebbf20d1693a15f`

Runner artifact commit:
`c6cacaa6fd9ef1bb630270f817a830c460a65df9`

Policy:

- fresh V2.6F derived cursor namespace;
- fixed 8-line windows;
- SIGMA derives segment index from persistent cursor;
- one successful non-complete VM cycle must advance cursor exactly one byte;
- batch limit = 3 VM cycles per invocation;
- same runner resumes next batch;
- evidence-empty segments are permitted;
- host does not select segments.

Expected fixture traversal:

- segment 0: `[0,8)`;
- segment 1: `[8,16)`;
- segment 2: `[16,24)`;
- segment 3: `[24,32)`;
- segment 4: `[32,40)`;
- segment 5: `[40,48)`;
- segment 6: `[48,56)`;
- segment 7: `[56,63)`;
- next native invocation: `DOCUMENT_SEGMENTS_COMPLETE YES`, `SEGMENT_INDEX 8`.

PASS requires:

- all VM cycles `RC=0`;
- cursor advances exactly one marker for every processed segment;
- `CURSOR_BYTES_AT_END=8`;
- `DOCUMENT_COMPLETE_SENTINEL=1`;
- completion log contains `SEGMENT_INDEX 8`;
- `V26F_FULL_DOCUMENT_TRAVERSAL=PASS`;
- `HOST_SEGMENT_SELECTION=NO`;
- `HOST_LEARNING=NO`;
- production learner memory not mutated.

After PASS:

`NEXT_ACTION=BUILD_V27_STRUCTURAL_GROUPING_PREFLIGHT`

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

Do not infer semantic understanding from DNA admission labels beyond each exact runtime test scope.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. Install V2.6F source + batched runner.
3. Run same V2.6F runner batch-by-batch until native `DOCUMENT_SEGMENTS_COMPLETE YES` at `SEGMENT_INDEX 8` and cursor bytes = 8.
4. If V2.6F PASSes, checkpoint it.
5. Then build V2.7 structural grouping preflight.
6. After grouping: curriculum queue, consolidation, revalidation.
7. Preserve all prior raw/done/log/history state and failure evidence.
