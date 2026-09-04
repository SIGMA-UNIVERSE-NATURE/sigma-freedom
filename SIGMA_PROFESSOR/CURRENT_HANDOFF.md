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

Proven in exact tested scope:

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

## Curriculum / re-learning design

Read:

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

## V2.5A QA

V2.5A original failed cleanly on H wrapper arity.

V2.5A.1 failed cleanly because direct `str(...)` compiled but locked VM returned `undefined function str`.

V2.5A.2 repaired both and PASSED on a 3-document QA corpus.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25A2_DOCUMENT_SURVEY_PREFLIGHT_PASS.md`

## V2.5B full-corpus survey — PASS

A frozen mechanical snapshot of the real raw corpus contains:

`SNAPSHOT_DOCUMENT_COUNT=56`

Host snapshot behavior was exact copy of all `*.document` files present at initialization. Host did not choose documents semantically.

Historical failures retained as evidence:

- initial V2.5B failed on incompatible `str_starts` runtime call pattern;
- V2.5B.1 later exposed empty-token contamination: `BEST_LOCAL_RELATION= =>`, support 110;
- V2.5B.1 state is tainted historical evidence and must not be promoted.

V2.5B.2 repaired this with a native empty-token relation gate and fresh derived survey namespace.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigma`

SOURCE_SHA256:
`b260544d4afdf8787a2653ee4b3350a6b76663c4377252623638db82e2502d3b`

Observed bytecode SHA256:
`5525f3f8475a14e37051c99a2108487c014ef0dd7927efedd932390aaba54c5c`

Final device evidence:

- final VM cycle `VM_RC=0`;
- `SURVEY_COMPLETE YES`;
- `RAW_FILE_COUNT 56`;
- `COMMITTED_SURVEY_COUNT 56`;
- `SNAPSHOT_DOCUMENT_COUNT=56`;
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

Important limit:

- native survey computation is bounded to 32 lines;
- current `read_text` still loads the whole file;
- `BOUNDED_FILE_IO=NOT_PROVEN`.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B2_FULL_CORPUS_SURVEY_PASS.md`

Checkpoint commit:
`dca66b408fba5c21d081983d6ba15ca510e63c2c`

## CURRENT FRONTIER — V2.6 bounded segment cursor restart preflight

Goal:

Prove SIGMA itself selects the next fixed-size segment from persistent cursor state and resumes the next segment after the supervising runner process is deliberately terminated and restarted.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_BOUNDED_SEGMENT_CURSOR_V2_6P.sigma`

SOURCE_SHA256:
`9cac5d9ddb10295b3ebf1f4300412e1b6dc3adceaf5f1de70eb83d0508f3b970`

Source artifact commit:
`dd4ceff9ae17c8de3a6f9d24e379577c3a4fca3d`

Local/device runner artifact to install:
`RUN_SIGMA_V26_BOUNDED_SEGMENT_CURSOR_RESTART_PREFLIGHT.sh`

Runner SHA256:
`e9304695d280fef406e0193a33103f212536cd8dac6e02d99629fd387279ca56`

QA fixture from frozen V2.5 snapshot:

`ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac.document`

Previously observed `LINE_TOTAL=63`, therefore it contains multiple 8-line segments.

V2.6 native policy:

- persistent cursor is a string of `|` markers;
- empty cursor -> segment index 0;
- SIGMA computes index from `str_split(cursor,"|")` and `list_len - 1`;
- fixed mechanical segment window = 8 consecutive lines;
- SIGMA computes start/end lines itself;
- SIGMA filters empty-token relations natively;
- after a successfully computed segment, SIGMA appends one `|` itself;
- host does not choose the next segment.

Restart admission protocol:

First invocation:

1. initialize isolated test state;
2. VM must process segment index 0, lines 0..7;
3. cursor must advance from 0 to 1 byte;
4. runner deliberately sends `TERM` to its own process AFTER the VM commit.

Second invocation of the SAME runner:

1. must detect persisted cursor byte count 1;
2. VM must resume segment index 1, lines 8..15;
3. cursor must advance to 2 bytes;
4. emit `V26_BOUNDED_SEGMENT_CURSOR_PREFLIGHT=PASS`.

Claim limits:

- this tests restart/resume BETWEEN committed VM cycles;
- kill during `append_text` is not tested;
- `MID_COMMIT_CRASH_ATOMICITY=NOT_PROVEN`;
- `BOUNDED_FILE_IO=NOT_PROVEN`;
- semantic understanding remains NOT PROVEN.

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

Native-admitted evidence currently exists in exact tested scope for:

- DNA-01
- DNA-02
- DNA-03
- DNA-04
- DNA-05
- DNA-06
- DNA-07
- DNA-50

Latest dependency frontier recorded by the 54-DNA lane:

`DNA-08 Learning World`

Do not infer semantic understanding from these admission labels beyond each exact test scope.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. Install V2.6 source + restart preflight runner.
3. Run the V2.6 runner once; expected result is deliberate process termination after segment 0 commit.
4. Run the SAME runner a second time; admission requires resume at segment index 1 and PASS.
5. If PASS, checkpoint V2.6 and build full-document segment cursor runner.
6. After V2.6: structural grouping, curriculum queue, consolidation, revalidation.
7. Keep all V2.2/V2.3/V2.4 raw/done/log/history state and tainted V2.5B.1 evidence.
