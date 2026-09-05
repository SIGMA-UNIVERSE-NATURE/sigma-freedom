# SIGMA V4-C3 / V4-D1 — SELF-DIRECTED LEARNING DUTY CYCLE, NATIVE REPORTING, AND FRONTIER ACQUISITION

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`DESIGN_READY=YES`

`V4C3_DUTY_CYCLE_IMPLEMENTATION=NOT_RUN`

`V4D1_FRONTIER_ACQUISITION_IMPLEMENTATION=NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

This design extends the admitted V4-C2 R2 real-corpus learning lane without overwriting its evidence or claiming semantic understanding.

## Motivation from observed V2.4 behavior

The V2.4 source forms adjacent-token relations `LEFT => RIGHT`, selects the highest-support relation, and constructs a fetch query from an unrequested low-support adjacent-token pair. The observed runtime showed high-support generic bigram reuse and `NEW_CONTEXT_RELATION_COUNT 0` in shown contexts.

That evidence does NOT prove that the repeated words are hardcoded or preinstalled. It does prove that the V2.4 learning unit is structurally narrow and can saturate.

V4 must therefore become the primary learner from persisted corpus evidence rather than merely repeat the V2.4 bigram policy faster.

## Existing admitted foundation

V4-C2 R2 preflight admitted, in observed real-corpus scope:

- native document profiling;
- native global corpus structural priority;
- exact native line-request transport;
- persistent line/token continuation;
- 2-token / 3-token / 4-token structural span evidence;
- zero host document/line/window/priority/retry/completion/learning decisions;
- production raw bytes preserved.

Still locked:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_CURIOSITY=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`CRASH_ATOMICITY=NOT_PROVEN`

`FULL_CORPUS_COMPLETION=NOT_PROVEN`

## Target operating loop

Canonical native phase plan:

`DISCOVER -> LEARN -> CONSOLIDATE -> FRONTIER -> REPORT -> REST -> DISCOVER`

When a new acquisition is justified by native structural frontier state:

`FRONTIER -> ACQUIRE_REQUEST -> MECHANICAL_TRANSPORT -> PROFILE -> LEARN`

The process may remain alive indefinitely. `REST` pauses learning work; it is not process termination.

## Native duty-cycle mode

First operational mode requested for admission:

- learning interval: 3600 seconds;
- report transition: exactly one native machine report commit after the learning interval boundary;
- rest interval: 600 seconds;
- after rest deadline: native transition back to learning.

The native duty-cycle controller, not Bash, owns phase transition decisions.

Planned native actions:

- `RUN_NATIVE_LEARNING_STEP`
- `RUN_NATIVE_FRONTIER_STEP`
- `EMIT_NATIVE_LEARNING_REPORT`
- `DISPATCH_NATIVE_ACQUISITION_REQUEST`
- `WAIT_NATIVE_REST`

Bash/host may dispatch the exact action already emitted by native SIGMA and may sleep mechanically during `WAIT_NATIVE_REST`. Bash must not decide that one hour or ten minutes has elapsed for a phase transition.

## Clock admission prerequisite

The ABI inventory records source evidence that `time_now` exists and returns `time(NULL)`, but this is not yet locked-VM runtime proof.

Before V4-C3 can claim a real one-hour / ten-minute native duty cycle, a dedicated locked-runtime clock probe must prove:

- `.sigma` can invoke `time_now` through the locked VM;
- the timestamp can be persisted and parsed by native SIGMA;
- a later locked-VM invocation observes strictly later native time;
- native code, not Bash, decides clock progression validity.

Until that probe passes:

`NATIVE_WALL_CLOCK_DUTY_CYCLE=NOT_PROVEN`

## No fake relearning

V4 must NOT obtain apparent activity by deleting `.complete`, resetting line cursors, or rereading completed documents without a new native reason.

Completed-document evidence remains committed.

A completed document becomes eligible again only under a separately admitted native revisit/revalidation policy with explicit provenance. Replaying the same bytes merely to increase counters is forbidden.

## Native learning agenda

Work priority must remain native and evidence-derived.

Initial agenda order:

1. new/unprofiled stored documents;
2. active incomplete line/token continuation;
3. incomplete profiled documents selected by native corpus priority;
4. native structural frontier requiring more evidence;
5. rest/wait when no eligible frontier exists.

`HOST_WORK_SELECTION=NO`

`HOST_FRONTIER_SELECTION=NO`

`HOST_REVISIT_DECISION=NO`

## Compact per-document frontier

Do not globally rescan large append-only evidence archives for every scheduling decision.

A later B4/C2 revision will maintain one compact frontier record per document, derived natively from the current line/window evidence.

Candidate record shape:

`DOC=<id> || QUERY=<pattern> || WIDTH=<unary> || SUPPORT=<unary> || PROVENANCE=<context-id> || FRONTIER=YES`

Structural frontier policy for the first admission candidate:

`UNREQUESTED -> WIDTH_DESC -> SUPPORT_ASC -> FIRST_NATIVE_TRAVERSAL_TIE`

The intent is to prefer a wider unseen 4-token or 3-token phrase over a generic adjacent bigram. This remains structural selection.

`SEMANTIC_IMPORTANCE=NOT_PROVEN`

## Native acquisition lane

Current V4-C2 R2 continuous shadow has `EXTERNAL_FETCH_ENABLED=NO`, so it cannot yet replace V2.4's new-input acquisition role.

V4-D1 will add:

`NATIVE FRONTIER -> NATIVE EXACT QUERY -> TRANSPORT -> V4-OWNED RAW DOCUMENT -> PROFILE -> LEARN`

The query must be emitted by native SIGMA from compact frontier evidence and native request history.

The host may initially perform only mechanical HTTP/query transport and protocol decoding of the exact native request, with no summarization, topic choice, semantic filtering, query rewriting, result ranking, or lesson generation.

`HOST_QUERY_GENERATION=NO`

`HOST_SEMANTIC_INTERPRETATION=NO`

`HOST_LEARNING=NO`

Direct native `net_fetch` may replace mechanical host transport only after its exact locked-runtime ABI semantics are separately admitted.

## Native machine report

The report is an evidence report, not an understanding claim.

Minimum native report fields:

- cycle id;
- native phase;
- native timestamp / interval state;
- active or last selected document;
- compact profile/complete/hold/evidence counts produced by native traversal;
- learner/evidence commit count for the cycle where available;
- current structural frontier and provenance;
- acquisition request state;
- next native action;
- explicit claim boundary: semantic understanding not proven.

Report commit must be native and persistent. Host may display exact report bytes.

## Retirement path for V2.4

Do not keep V2.4 indefinitely merely because it is old production.

Retirement gate is capability-based, not calendar-based.

Required successor evidence before V2.4 can be stopped:

1. V4-C2 R2 real-corpus learning PASS — already observed;
2. V4-C3 native clock/duty-cycle PASS;
3. V4-C3 persistent restart/resume PASS;
4. V4-C3 native report commit PASS;
5. V4-D1 native frontier request generation PASS;
6. V4-D1 exact acquisition transport + new V4-owned document learning PASS;
7. cutover/rollback gate proving V4 no longer depends on V2.4 PID or V2.4 writer state.

Only after that gate may policy change to:

`PRODUCTION_V2_4_KEEP_RUNNING=NO`

Until then:

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

## Next engineering action

`NEXT_ACTION=ADMIT_LOCKED_NATIVE_TIME_NOW_PERSISTENCE_THEN_IMPLEMENT_V4C3_DUTY_CYCLE_AND_NATIVE_REPORTER`

After the clock gate passes, build the duty-cycle controller and report source as new V4 revisions. Do not modify or erase the admitted R2 artifacts.
