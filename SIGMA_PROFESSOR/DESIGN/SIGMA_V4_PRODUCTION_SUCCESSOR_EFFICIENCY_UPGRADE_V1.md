# SIGMA V4 PRODUCTION SUCCESSOR — EFFICIENCY UPGRADE V1

Status: DESIGN LOCK / NATIVE-FIRST / NOT PRODUCTION
Date: 2026-09-05

## Purpose

Build a production successor to legacy V2.4 because live evidence shows real structural learning progress but degraded learning throughput and repeated scheduling/revisit inefficiency.

This is NOT an in-place rewrite of the running V2.4 process.

`V2_4_PRODUCTION_KEEP_RUNNING=YES`

`V4_PRODUCTION_CANDIDATE_BUILD_IN_PARALLEL=YES`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Non-negotiable execution boundary

All cognition, work arbitration, curriculum choice, fairness, learning, revalidation, lifecycle action, retry policy, and recovery validity must execute in native `.sigma` bytecode under the locked SIGMA VM.

`HOST_OR_BASH_COGNITION=FORBIDDEN`

`HOST_OR_BASH_LEARNING=FORBIDDEN`

`HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`

`HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`

`HOST_OR_BASH_RETRY_POLICY=FORBIDDEN`

Host may only launch the locked compiler/VM, transport exact bytes, supervise processes, inject isolated faults, and dispatch an exact event already emitted/recovered by native SIGMA.

## Live V2.4 deficiencies motivating V4

Observed in production evidence:

1. large/new fetched contexts can fail native learning with VM `rc=9` step limit;
2. fetched transport success and native learned success are not the same state;
3. multiple new fetches can enter HOLD while DONE/history stop advancing;
4. one older context can repeatedly produce new gaps/reconsideration turns;
5. rate-limit waiting currently produces repeated heartbeat cycles rather than useful local curriculum work;
6. legacy runner semantics still contain host-side traversal/scheduling mechanics that must not exist in the successor;
7. direct append/write durability remains non-atomic physically, so critical continuation intent must use the admitted native V2.22/V2.23 journal protocol.

These are structural/runtime observations only. They do not prove semantic understanding.

## V4 required architecture

### A. Separate transport from learning completion

Required state distinction:

`FETCH_REQUEST_EMITTED`

`FETCH_TRANSPORT_RECEIVED`

`NATIVE_LEARNING_PENDING`

`NATIVE_LEARNING_COMMITTED`

`NATIVE_LEARNING_RETRYABLE`

Transport receipt MUST NOT mark a request learned.

### B. Bounded segmented learning

New material must enter bounded native segment traversal instead of requiring one whole-document learning pass.

A VM step-limit failure on a material item must not permanently lose the item. The item remains resumable/retryable at a persisted segment cursor.

Use admitted bounded structural traversal/deep-relearn patterns as capability provenance; do not hardcode expected relations or outcomes.

### C. Native anti-idle work arbitration

When a fetch request is rate-limited or transport is pending, SIGMA must continue useful native local work if eligible local curriculum work exists.

No host decision may choose between online/offline work.

Required candidate actions are structural execution actions only, for example:

- `CONTINUE_LOCAL_CURRICULUM`
- `LEARN_RECEIVED_CONTEXT`
- `RESUME_RETRYABLE_CONTEXT`
- `DISPATCH_NATIVE_FETCH_REQUEST`
- `RESUME_PENDING_REVISIT`
- `WAIT_NO_ELIGIBLE_WORK`

The exact arbitration policy must be native and runtime-proven.

### D. Native fairness

Admitted V2.19 fairness semantics remain required:

- immediate consecutive revisit cannot starve undispatched work;
- oldest mature pending revisit resumes after different-work progress;
- exact event identity is preserved;
- no revisit evidence is deleted.

### E. Native curriculum lifecycle

The successor must retain the admitted structural lifecycle:

`SURVEY -> SEGMENT -> STRUCTURAL_PROFILE -> GROUP -> CURRICULUM_PRIORITY -> DEEP_LEARN -> REVALIDATE -> REVISIT_OR_ARCHIVE_FOR_NOW`

with persisted stage/cursor and recovery.

### F. Journal-wrapped continuation intent

All critical scheduled continuation intent must be persisted through the admitted native transaction/recovery protocol from V2.22/V2.23.

Direct host interpretation of a scheduled event is forbidden.

### G. Production efficiency scorecard

V4 is not promoted merely because it stays alive.

Promotion comparison against V2.4 must include bounded observed metrics such as:

- native learning completions per fetched context;
- HOLD/retryable ratio;
- number of contexts that advance after initial `rc=9`-class pressure;
- local curriculum progress during fetch-rate-limit windows;
- number of real distinct works receiving scheduling turns;
- pending revisit age / starvation absence;
- committed structural history growth per accepted input;
- restart/recovery exactness;
- no host cognitive substitution.

No semantic-quality claim may be inferred from these throughput metrics.

## V4 build sequence

### V4-A — Native productivity/work arbiter

Teach native SIGMA to choose between received context, retryable context, local curriculum, pending revisit/fairness continuation, fetch dispatch, or true wait.

Primary target:

`RATE_LIMIT_WAIT_DOES_NOT_FORCE_IDLE_WHEN_LOCAL_WORK_EXISTS`

### V4-B — Segmented received-context learner

Teach received fetched contexts to enter persisted bounded segment learning so a whole-context `rc=9` does not mean permanent HOLD.

Primary target:

`FETCHED_CONTEXT_CAN_RESUME_AFTER_BOUNDED_SEGMENT_PROGRESS`

### V4-C — Learned-vs-fetched commit protocol

Request becomes learned only after native learning commit.

Primary target:

`FETCHED_DOES_NOT_EQUAL_LEARNED`

### V4-D — Fairness/lifecycle/journal composition

Compose V4-A/B/C with admitted V2.19 + V2.10-14 + V2.22/23 behavior.

### V4-E — Shadow productivity comparison

Run V2.4 and V4 candidate in isolated namespaces against equivalent admitted input scope and compare runtime efficiency metrics without changing V2.4 production.

### V4-F — Restart/recovery and reversible cutover admission

Only after the candidate proves superior runtime efficiency and safe restart/recovery may a reversible supervisor cutover gate be designed.

## Immediate frontier

Build `V4-A` first.

`NEXT_ACTION=TEACH_NATIVE_PRODUCTIVITY_WORK_ARBITER`

Do NOT resume the blocked host-assisted V2.24 migration design as a production capability.

## Claim limits

Keep:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

`GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

`PRODUCTION_PROMOTION_ALLOWED=NO`
