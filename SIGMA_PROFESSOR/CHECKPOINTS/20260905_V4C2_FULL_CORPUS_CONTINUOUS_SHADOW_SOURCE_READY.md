# V4-C2 FULL-CORPUS CONTINUOUS SHADOW — SOURCE READY / NOT RUN

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4C2_FULL_CORPUS_CONTINUOUS_SHADOW_SOURCE_READY=YES`

`V4C2_FULL_CORPUS_SHADOW_PREFLIGHT=NOT_RUN`

`V4C2_FULL_CORPUS_CONTINUOUS_SHADOW_RUNTIME=NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Production discipline remains:

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

The new program is an isolated shadow successor. It must not be treated as admitted merely because source exists.

## Motivation

The next V4 controller must learn from SIGMA's already stored real `.document` corpus rather than depend on host-created 12/16-token lesson fixtures.

Two long-horizon blockers in the previously admitted components were also removed in source design:

- V4-A.1 had a bounded growing arbiter ledger and refused after the ledger limit;
- V4-B3 had a bounded growing progress ledger and refused after the progress limit.

V4-C2 therefore uses compact persistent controller/learner continuation state.

The existing-corpus program does **not** mean that SIGMA receives only 16 tokens as its source document. The native corpus manager reads real stored documents, selects a native bounded segment, and the learner advances through that segment in 16-token compute windows with persisted continuation.

## Native source 1 — V4-A2 compact arbiter

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A2.sigma`

`V4A2_GIT_BLOB=59e95ea8271b15411a7c1856d2fc1af2fbfb9465`

`V4A2_SOURCE_SHA256=72fa9dee55fa350c68482ad110d431b090efb1d41fe5ecb76a623ea8518d406e`

Design:

- preserves recovered-first / received-retryable-local-fetch arbitration policy;
- replaces the growing decision ledger with one compact persisted `LAST_SOURCE` state;
- host does not select work or stage.

Admission state:

`V4A2_RUNTIME_PROOF=NOT_RUN`

## Native source 2 — V4-B4 compact span learner

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_COMPACT_TOKEN_WINDOW_SPAN_LEARNER_V4B4R1.sigma`

`V4B4_GIT_BLOB=8fd5e828861a43ca99b5ff77658504157e915ece`

`V4B4_SOURCE_SHA256=c4a9828a45964917b75df23ec9b33885462119d26b7d1cfe37923c61c40b852c`

Design:

- 16-token native compute window;
- one compact persisted line/token cursor instead of a growing progress ledger;
- structural 2-token, 3-token and 4-token span candidates per executed window;
- longer span wins an equal-support tie so learning output is not restricted to a single two-token relation;
- completion only after all native windows of the supplied context complete;
- host does not choose window, retry or completion.

Claim limit:

`STRUCTURAL_SPAN_LEARNING_ONLY=YES`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

Admission state:

`V4B4_RUNTIME_PROOF=NOT_RUN`

## Native source 3 — V4-C2 existing-corpus work manager

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_CORPUS_WORK_MANAGER_V4C2R1.sigma`

`V4C2_GIT_BLOB=d06a6de1d5d0055dc9485a3608871252d2763346`

`V4C2_SOURCE_SHA256=bb7153866c65dddaaee2d426dd6276fe925b16f564f6f4b7395816953b3a914a`

Design:

- reads the existing production raw `.document` directory as read-only source;
- uses native directory listing + sorted corpus cursor;
- scans at most 32 directory entries per native invocation;
- selects the first native-eligible document not marked complete or held;
- keeps per-document native segment cursor state in the shadow corpus state directory;
- uses a 4-line native segment budget;
- installs exact native segment text into V4-B4 without host document/segment selection;
- classifies new segment as RECEIVED and persisted B4 continuation as RETRYABLE;
- archives native window evidence per document;
- marks completed documents in per-document compact state;
- holds a document after an explicit native B4 refusal and continues corpus traversal;
- external fetch is disabled in this version so the stored corpus is the primary work source.

Admission state:

`V4C2_RUNTIME_PROOF=NOT_RUN`

`REAL_CORPUS_DIRECTORY_SCALE_STEP_LIMIT=NOT_PROVEN`

`FULL_CORPUS_COMPLETION=NOT_PROVEN`

## Canonical real-corpus preflight runner

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C2_FULL_CORPUS_SHADOW_PREFLIGHT.sh`

`V4C2_PREFLIGHT_RUNNER_GIT_BLOB=593cdd043941e6ecb27550be8f4929a8cef792b7`

`V4C2_PREFLIGHT_RUNNER_SHA256=d75efa83fe953efe8d888aacfa379c2cfaf0efc97bc64a21db18d3d442dc34b6`

Properties:

- fixed 256 controller turns;
- uses the real stored production raw corpus as a read-only source;
- creates an isolated fresh shadow namespace;
- host only invokes VM and mechanically dispatches exact native A2 `ACTION + TARGET`;
- no host document/segment/window/retry/completion/learning decisions;
- verifies the raw corpus manifest before/after;
- requires production V2.4 to remain the same PID throughout the preflight;
- full-corpus completion is not required for this fixed-turn admission gate.

Preflight proof state:

`V4C2_PREFLIGHT_LOCKED_SIGMAC_COMPILE=NOT_RUN`

`V4C2_PREFLIGHT_LOCKED_VM_RUNTIME=NOT_RUN`

`V4C2_PREFLIGHT_ADMISSION=NOT_RUN`

## Persistent continuous shadow runner

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C2_FULL_CORPUS_CONTINUOUS_SHADOW.sh`

`V4C2_CONTINUOUS_RUNNER_GIT_BLOB=dd36c6b81f640cd1f426d9847dab81c7a4e82ae9`

`V4C2_CONTINUOUS_RUNNER_SHA256=c871b32560b871b7b327499fb31f341a25f2302bcdad0696093c9c4f6b75e247`

The continuous runner preserves shadow state across restart and loops:

`native C2 corpus manager -> native A2 arbiter -> exact host dispatch -> native B4 learner -> LOOP`

It remains shadow-only and hard-gates production V2.4 presence/PID health.

Do not launch this runner as a production replacement before the real-corpus preflight passes and a PASS checkpoint is written.

## Required execution order

1. Keep V2.4 production running unchanged.
2. Install exact source/runner from `SIGMA_LIFE`.
3. Run `RUN_SIGMA_V4C2_FULL_CORPUS_SHADOW_PREFLIGHT.sh` once and preserve the complete transcript.
4. Any compile error, VM nonzero RC, `HOLD=`, source/hash mismatch, production PID change, raw corpus manifest change, or unsupported native action is evidence and blocks promotion.
5. Only after preflight PASS: write a PASS checkpoint, then launch the persistent continuous shadow runner.
6. Keep V2.4 running while V4-C2 processes the corpus in shadow and compare observed throughput/holds/restart behavior before any cutover gate.

## Claim boundary

Even after source-ready:

`EXISTING_STORED_CORPUS_NATIVE_SELECTION=NOT_PROVEN_UNTIL_RUNTIME`

`COMPACT_ARBITER_LONG_HORIZON_RUNTIME=NOT_PROVEN_UNTIL_RUNTIME`

`COMPACT_LEARNER_LONG_HORIZON_RUNTIME=NOT_PROVEN_UNTIL_RUNTIME`

`MULTI_SPAN_STRUCTURAL_LEARNING=NOT_PROVEN_UNTIL_RUNTIME`

`FULL_CORPUS_AUTONOMOUS_COMPLETION=NOT_PROVEN`

`JOURNAL_WRAPPED_CRASH_ATOMICITY=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next action

`NEXT_ACTION=RUN_EXACT_V4C2_REAL_CORPUS_SHADOW_PREFLIGHT_AND_PRESERVE_FIRST_RESULT_AS_EVIDENCE`
