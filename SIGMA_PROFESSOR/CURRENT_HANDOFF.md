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

Current target: **native continuous learning + curriculum/re-learning**.

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

V2.4 remains the production continuous learner and should continue running unless it emits a real VM failure.

Proven in tested scope:

- dynamic structural relation learning;
- persistent recurrence;
- native self-selection;
- cross-context support;
- native gap/query generation;
- Internet transport/decode -> native `mode=NEW` learning;
- previously failing long context now completes without reproducing the V2.3 step-limit failure.

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

## V2.5A document-survey QA

V2.5A original failed cleanly on H wrapper arity.

V2.5A.1 failed cleanly because direct `str(...)` compiled but locked VM returned `undefined function str`.

V2.5A.2 repaired both issues and PASSED on the locked VM using a 3-document QA corpus.

V2.5A.2 proof scope:

- native selection of first unsurveyed sorted `.document`;
- native structural survey;
- native map/list relation counting;
- persistent survey state;
- fourth invocation produced `SURVEY_COMPLETE YES`;
- production learner namespace not mutated;
- `HOST_LEARNING=NO`;
- semantic understanding NOT PROVEN.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25A2_DOCUMENT_SURVEY_PREFLIGHT_PASS.md`

## V2.5B full-corpus progression

A frozen mechanical snapshot of the real raw corpus was created:

`SNAPSHOT_DOCUMENT_COUNT=56`

Host snapshot behavior is exact mechanical copy of all `*.document` files present at initialization. Host does not select documents semantically.

### V2.5B initial full-corpus run — FAIL

Cycle 1 returned:

- `VM_RC=22`
- `SIGMA host: integer required`

D1 diagnostic isolated the exact failing call to:

`host("str_starts", OLD_RECORD, DOC_PREFIX, NULL)`

All earlier diagnostic stages passed, including listdir, list_sort, list_len, str_split, list_get, str_ends, and str_replace.

V2.5B.1 removed `str_starts` and replaced record matching with native `str_split + list_len + list_get + equality`.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B_D1_STR_STARTS_DIAGNOSIS_AND_V25B1_REPAIR.md`

### V2.5B.1 — DO NOT RESUME / DO NOT PROMOTE

V2.5B.1 progressed successfully through many VM cycles. User stopped after cycle 47.

Critical observed output at cycle 47:

- `VM_RC=0`
- `COMMITTED_SURVEY_COUNT_BEFORE=46`
- `LINE_TOTAL=63`
- `SURVEY_LINE_LIMIT=32`
- `BEST_LOCAL_RELATION= =>`
- `BEST_LOCAL_SUPPORT=110`

Interpretation:

`str_split(line, " ")` can emit empty tokens from repeated/leading spaces. Empty-token relations can dominate the structural profile.

Therefore:

`V25B1_STRUCTURAL_PROFILE_QUALITY=FAIL`

Existing V2.5B.1 survey state must be preserved as tainted evidence. Do not delete it, do not resume it, and do not use it as admitted structural knowledge.

Checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B1_EMPTY_TOKEN_CONTAMINATION_AND_V25B2_REPAIR.md`

## CURRENT FRONTIER — V2.5B.2 FILTERED + BATCHED

V2.5B.2 repairs the empty-token contamination and starts a fresh derived survey state while reusing the same frozen 56-document snapshot.

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigma`

SOURCE_SHA256:
`b260544d4afdf8787a2653ee4b3350a6b76663c4377252623638db82e2502d3b`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V25B_2_FULL_CORPUS_SURVEY_BATCHED.sh`

RUNNER_SHA256:
`6ec22ed2b0df2ac2fe854daccd1f9821f20e96ab164050303a64a8e05c8f6364`

Changes:

1. Native empty-token relation gate:
   - if `LEFT == ""` or `RIGHT == ""`, skip the relation;
   - track `SKIPPED_EMPTY_RELATIONS`.
2. Fresh derived survey namespace:
   `.sigma_exec/SIGMA_V25B2_DOCUMENT_SURVEY.memory`
3. Reuse frozen 56-document snapshot; production raw remains untouched.
4. Fixed batch limit: at most 5 VM cycles per invocation to avoid output flooding.
5. Rerun the same runner for the next batch.
6. Crash-isolating append framing:
   - each committed record starts on a new line;
   - valid record ends `|| COMMIT=YES`;
   - a partial interrupted append cannot silently merge into the next valid record.
7. `append_text` remains plain stdio; fully atomic persistence remains NOT PROVEN.

Static checks:

- `H_CALL_ARITY_AUDIT=PASS`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- `BASH_N_RC=0`

V2.5B.2 admission requires:

- every VM cycle `RC=0`;
- no empty-token `BEST_LOCAL_RELATION`;
- repeated batches eventually produce committed survey count = 56;
- SIGMA emits `SURVEY_COMPLETE YES`;
- production raw not mutated;
- V2.4 learner memory not mutated;
- `HOST_LEARNING=NO`;
- `HOST_DOCUMENT_SELECTION=NO`.

Claim after PASS must remain structural only.

## Host ABI status

Source inventory found 93 host operations. Important exact findings:

- `read_bytes` reads whole file into O_BYTES;
- `write_text` / `append_text` are plain stdio, not atomic;
- `crypto_digest` hashes VM strings via OpenSSL EVP;
- `net_fetch` is libcurl body transport with redirect follow + 5s timeout;
- JSON decode currently routes through `json_decode_scalar_text`; nested structured JSON is NOT proven;
- `list_sort` is in-place ascending and approximately O(n^2);
- Unicode-aware normalization is NOT proven;
- locked-VM runtime behavior for `str_starts` is incompatible with the V2.5B call pattern; do not use it without a dedicated ABI characterization.

Do not add broad host tools without native failure evidence.

## 54 DNA

Read:
`SIGMA_PROFESSOR/DIRECTIVES/54_DNA_NATIVE_ONLY_PRIORITY_DIRECTIVE_V2.md`

Keep all 54 DNA. Active DNA cognition must be native `.sigma`. Numeric order is not required; work dependency-first/capability-first.

## NEXT ACTION

1. Keep V2.4 production learner running unless it emits a real VM failure.
2. Do NOT resume V2.5B.1.
3. Install V2.5B.2 source + batched runner.
4. Run one 5-cycle batch and inspect:
   - `VM_RC`;
   - `SKIPPED_EMPTY_RELATIONS`;
   - `BEST_LOCAL_RELATION`;
   - committed count.
5. If clean, rerun the same runner batch-by-batch until native `SURVEY_COMPLETE YES` and committed count = 56.
6. Then checkpoint full-corpus survey PASS.
7. Next capability: V2.6 bounded segment cursor + deliberate kill/restart/resume test.
8. After V2.6: structural grouping, curriculum queue, consolidation, revalidation.

Do not delete V2.2/V2.3/V2.4 raw/done/log/history state or tainted V2.5B.1 evidence.
