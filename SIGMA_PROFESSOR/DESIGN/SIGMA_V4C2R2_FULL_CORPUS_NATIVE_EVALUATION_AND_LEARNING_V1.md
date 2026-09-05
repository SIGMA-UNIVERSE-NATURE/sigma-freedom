# SIGMA V4-C2 R2 — FULL-CORPUS NATIVE EVALUATION + LEARNING

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`DESIGN_ONLY=YES`

`RUNTIME_PROOF=NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

This design supersedes V4-C2 R1 for future implementation. R1 remains blocked provenance and must not be run.

## Goal

Build a shadow successor that learns from SIGMA's existing stored `.document` corpus without host-created lesson fragments and without loading a complete raw document into the native controller before bounded learning begins.

The desired automatic loop is:

`PROFILE STORED CORPUS -> NATIVE GLOBAL PRIORITY PASS -> LEARN SELECTED DOCUMENT THROUGH PERSISTED LINE/TOKEN CONTINUATION -> COMPLETE/HOLD -> RE-EVALUATE CORPUS -> LOOP`

Production V2.4 remains unchanged and running during proof.

## Locked runtime

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`SIGMA_VM_V0_9_CANDIDATE_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

Every source must compile with that exact SIGMAC and execute through that exact VM before any capability claim.

## Host boundary

Native SIGMA owns:

- corpus phase;
- document eligibility;
- document profile state;
- global priority comparison;
- selected document;
- line cursor;
- token window cursor;
- retry classification;
- completion/hold decision;
- learning evidence and profile updates.

Host may only:

- launch compiler/VM;
- verify exact identities;
- transport the exact corpus-read request already emitted by native SIGMA;
- return the exact requested line and mechanical FOUND/NOT_FOUND result;
- preserve evidence and supervise processes.

Locked invariants:

`HOST_DOCUMENT_SELECTION=NO`

`HOST_SEGMENT_SELECTION=NO`

`HOST_LINE_SELECTION=NO`

`HOST_WINDOW_SELECTION=NO`

`HOST_CORPUS_PRIORITY=NO`

`HOST_RETRY_DECISION=NO`

`HOST_COMPLETION_DECISION=NO`

`HOST_LEARNING=NO`

## Why mechanical line transport is used in R2

The repository ABI inventory proves source presence of `read_bytes` and `read_text`, but explicitly records the offset/count semantics of `read_bytes` as unknown and says bounded file-range/line read may still be required if existing primitives read whole files.

R2 therefore MUST NOT guess an undocumented `read_bytes` signature.

Instead, native SIGMA emits an exact request containing:

- exact document ID;
- exact native line cursor;
- exact purpose (`PROFILE` or `LEARN`);
- exact request ID.

The host mechanically returns only that exact requested line. It does not choose the document or line. The raw corpus remains read-only.

This removes whole-document `read_text` from the native manager critical path while preserving the execution boundary.

Keep claim discipline:

`BOUNDED_VM_CORPUS_INPUT_PER_TRANSPORT=ONE_REQUESTED_LINE`

`BOUNDED_FILE_IO=NOT_PROVEN`

because the underlying host line lookup I/O complexity is not yet admitted as a bounded VM ABI primitive.

If locked-runtime testing later proves a bounded offset/count signature for `read_bytes`, the mechanical transport can be replaced by that primitive without changing native corpus selection or priority policy.

## Native component A — V4-A3 compact arbiter

V4-A3 extends compact A2 arbitration with a native `CORPUS_READ` source.

Native action set in this R2 lane:

- `LEARN_RECEIVED_CONTEXT`
- `RESUME_RETRYABLE_CONTEXT`
- `DISPATCH_NATIVE_CORPUS_READ_REQUEST`
- `WAIT_NO_ELIGIBLE_WORK`

Local/fetch slots may remain structurally available but are disabled by the corpus manager in this revision.

Arbiter state remains one compact `LAST_SOURCE`, not an ever-growing decision ledger.

## Native component B — V4-B4R2 compact span learner

Input is one exact non-empty line transported from the native-selected corpus position.

Learning properties:

- 16-token compute window;
- compact persisted token cursor;
- 2-token, 3-token, and 4-token structural span candidates;
- cross-window spans preserved because the learner uses the absolute token offset in the complete transported line;
- longer span wins an equal-support tie;
- completion only after all token windows of the current line are processed;
- per-window evidence emitted for native profile aggregation.

A line exceeding the admitted selected-line token bound must be refused natively and the document held; host must not split that line to rescue the run.

`STRUCTURAL_SPAN_LEARNING_ONLY=YES`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Native component C — V4-C2R2 corpus evaluator/controller

### Persistent global state

Compact global files only:

- phase: `PROFILE` / `PRIORITY` / `LEARN`;
- bounded corpus scan cursor;
- active document and purpose;
- exact pending read request;
- compact global priority tournament candidate;
- native status.

No global append-only work ledger is required.

### Persistent per-document state

Each document owns small independent state:

- `<doc>.line_cursor` — next line position;
- `<doc>.profile` — compact best observed structural width/support;
- `<doc>.evidence` — evidence archive, provenance only, not scanned globally for scheduling;
- `<doc>.complete`;
- `<doc>.hold`.

The controller never needs to scan a growing evidence archive to resume work.

## Phase 1 — PROFILE the whole stored corpus

The manager incrementally scans at most a fixed number of directory entries per invocation.

For each eligible document without a profile:

1. native SIGMA chooses the document;
2. native SIGMA emits exact line-read requests beginning at the persisted line cursor;
3. blank lines are skipped by native cursor progression;
4. first non-empty line is processed by V4-B4R2 through as many 16-token windows as necessary;
5. native SIGMA commits a compact document profile from observed structural evidence;
6. the line cursor advances so profile work also counts as real learning rather than a disposable fixture;
7. native SIGMA continues to the next unprofiled document.

When the native scan reaches the end with no unprofiled eligible document, it transitions to `PRIORITY`.

This means the stored corpus itself supplies admission/runtime work. No host lesson text is injected.

## Phase 2 — native global PRIORITY pass

The manager performs a bounded tournament scan over document profiles.

Eligibility excludes native `.complete` and `.hold` documents.

Priority policy for R2 is structural and explicit:

1. higher best observed span width first (`4 > 3 > 2 > 0`);
2. for equal width, higher observed support first;
3. equal width/support keeps the first candidate in the native corpus traversal order.

The best candidate is persisted compactly between bounded scan invocations.

If an unprofiled eligible document appears during the priority pass because production V2.4 appended a new document, native SIGMA returns to `PROFILE` before deep selection.

Host does not choose or score the candidate.

## Phase 3 — LEARN selected document deeply

After the full native priority pass chooses a document:

1. native SIGMA resumes that document's persisted line cursor;
2. native SIGMA requests the exact next line;
3. non-empty line is learned by V4-B4R2 in 16-token windows;
4. manager archives evidence and updates the document's compact profile;
5. line cursor advances only after native learner completion;
6. repeat until an exact native line request returns mechanical NOT_FOUND;
7. native SIGMA marks the document complete;
8. return to `PRIORITY`.

A learner refusal creates a native document hold and returns control to corpus evaluation. Host never edits cursor/hold/completion state to force progress.

## Production raw-corpus race rule

V2.4 is allowed to append new `.document` files during shadow proof.

Admission must therefore snapshot the identities of documents existing at preflight start and later require:

- every pre-existing document still exists;
- every pre-existing document retains identical bytes;
- new documents may be appended;
- mutation/deletion of a pre-existing document is a failure.

Do not require the whole directory manifest or total count to remain identical.

## Admission evidence required before continuous shadow launch

The fixed-turn real-corpus preflight must prove at least:

- exact SIGMAC identity;
- exact VM identity;
- all R2 source identities;
- at least one native corpus-read request;
- at least one native received-context dispatch;
- at least one native retryable dispatch when a line requires multiple windows, when naturally present;
- at least one committed per-document profile;
- native archived evidence;
- observed pair occurrence > 0 before claiming pair learning;
- observed triple occurrence > 0 before claiming triple learning;
- observed quad occurrence > 0 before claiming quad learning;
- no host document/line/window/priority/retry/completion/learning decision;
- all pre-existing raw documents preserve exact bytes;
- production V2.4 remains the same PID.

Global priority selection may only be admitted if the transcript actually reaches and completes a native priority pass. If the fixed turn budget is insufficient for the real corpus size, preserve that as evidence and do not widen the claim.

## Continuous shadow

Only after a PASS checkpoint may a persistent shadow runner loop:

`C2R2 manager -> A3 arbiter -> exact native-event dispatch -> B4R2 learner or mechanical exact line transport -> LOOP`

It must persist shadow state across process restart.

External network fetch remains disabled in R2 while stored eligible corpus work exists.

## Claim limits

Even after successful R2 preflight, keep unless separately proven:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`CRASH_ATOMICITY=NOT_PROVEN`

`FULL_CORPUS_COMPLETION=NOT_PROVEN_UNTIL_OBSERVED`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`
