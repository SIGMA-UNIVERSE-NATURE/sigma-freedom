# SIGMA V4-C1 continuous shadow controller composition

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Goal

Assemble admitted native V4 capabilities into one automatically running shadow successor while production V2.4 remains unchanged.

This is the first V4 lane whose subject is the automatic controller itself rather than an isolated capability.

## Non-negotiable execution boundary

- SIGMA capability/cognition remains native `.sigma` under the locked VM.
- Bash/host is only mechanical supervisor and exact native-event dispatcher.
- Host may not select context/work, choose retry, decide completion, choose stage, or perform learning.
- Exact native action dispatch is allowed only after the action/target were emitted by native SIGMA.

## Native components

1. V4-C1 native work manager
   - reads received-work queue;
   - owns active-context transition;
   - observes native V4-B3 progress/completion ledgers;
   - archives completed active-context evidence before resetting active ledgers;
   - records completed context IDs;
   - chooses the first queue context not already completed;
   - classifies active work as RECEIVED vs RETRYABLE from native persisted progress;
   - writes exact V4-A RECEIVED/RETRYABLE slots.

2. Admitted V4-A.1 native productivity/work arbiter
   - recovered continuation first;
   - otherwise structural source arbitration among received/retryable/local/fetch;
   - fetch not-due does not block productive local/retryable work.

3. Admitted V4-B3 native token-window learner
   - 16-token compute window;
   - persistent line/token cursor;
   - cross-window bigram continuity;
   - completion only after all windows;
   - exact real `49c16...` rc9 context already proven recoverable in isolated replay.

4. V4-C1 native bounded local-progress executor
   - admission-only structural local-work fixture;
   - proves exact local branch dispatch and persisted native progress;
   - does NOT yet claim integration with the full admitted curriculum lifecycle.

## Controller loop

For each fixed admission turn:

1. invoke native V4-C1 work manager;
2. invoke native V4-A arbiter;
3. host reads exact `ACTION` + `TARGET` emitted by V4-A;
4. host dispatches exactly one corresponding native module:
   - `LEARN_RECEIVED_CONTEXT` -> V4-B3 one native token window;
   - `RESUME_RETRYABLE_CONTEXT` -> V4-B3 one native token window;
   - `CONTINUE_LOCAL_CURRICULUM` -> V4-C1 native local-progress executor;
   - `WAIT_NO_ELIGIBLE_WORK` -> no capability dispatch;
5. repeat on a fixed turn budget; host never terminates early because of native status.

The admission fixture sets fetch not-before in the future, so any `DISPATCH_NATIVE_FETCH_REQUEST` is a failure of composition policy, not a host branch choice.

## Active-context compaction

V4-B3 currently has a bounded active progress ledger. V4-C1 therefore does not accumulate every context forever in the learner's active scan set.

When native V4-B3 marks the active context complete, the native work manager:

1. appends the exact active progress text to an archive stream with context boundary records;
2. appends `CTX=<id> || COMPLETE=YES` to the compact completed-context ledger;
3. clears only the active V4-B3 progress/completion/status files;
4. clears active-context ID;
5. selects the next not-completed queue item natively.

This keeps the active learner scan bounded without using host completion/work decisions.

## Admission workload

Use exact production raw context:

`49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`

as the received queue item, plus one native local-work fixture and a fetch request whose native not-before is in the future.

Expected behavior:

- received context begins automatically;
- after persisted progress exists it is natively classified RETRYABLE;
- V4-A interleaves local work under its admitted round-robin policy;
- local work completes natively and clears its own eligibility;
- V4-B3 eventually completes `49c16...`;
- work manager archives/compacts it natively;
- controller reaches true idle because fetch is not due and no local/received/retryable work remains;
- V2.4 remains same PID.

## Claim boundary after PASS

May admit only:

`V4_CONTINUOUS_SHADOW_CONTROLLER_COMPOSITION=PROVEN_IN_ONE_REAL_RC9_CONTEXT_PLUS_BOUNDED_LOCAL_WORK_SCOPE`

`NATIVE_CONTEXT_WORK_SELECTION_AND_RETRY_CLASSIFICATION=PROVEN_IN_TESTED_SCOPE`

`NATIVE_ACTIVE_CONTEXT_COMPACTION=PROVEN_IN_TESTED_SCOPE`

`RATE_LIMIT_WAIT_CONTINUES_PRODUCTIVE_NATIVE_WORK_IN_COMPOSED_CONTROLLER=PROVEN_IN_TESTED_SCOPE`

Still:

- full curriculum lifecycle integration NOT proven in V4-C1;
- fetch transport/result registration integration NOT proven in V4-C1;
- journal-wrapped controller continuation NOT proven in V4-C1;
- remaining four observed rc9 contexts NOT yet proven;
- bounded file I/O NOT proven;
- semantic understanding NOT proven;
- V4 production promotion NOT allowed.

## Next after V4-C1 PASS

V4-C2 replaces the bounded local fixture with the admitted native curriculum/lifecycle path, then adds real received-context registration and mechanical fetch transport while retaining native arbitration.
