# V4-A.1 NATIVE PRODUCTIVITY WORK ARBITER — ADMITTED PASS

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT=PASS`

`NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Production V2.4 remained running unchanged with PID `831` before and after this admission.

## Locked runtime identities

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

V4-A native source SHA256:
`12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2`

V4-A locked-runtime bytecode SHA256 observed in user transcript:
`be7a97147d840d79a4bc0745d4c192a3e29466fffb7c81905a7d7424b78a6961`

## Isolation

`SHADOW_STATE_NAMESPACE_ISOLATION=PASS`

`PRODUCTION_BRAIN_WRITE_TARGET=NO`

Shadow BRAIN used:
`/data/data/com.termux/files/home/SIGMA/SIGMA_V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT/shadow/BRAIN/EXTRA BRAIN_OPPO_24826`

## Runtime evidence

All observed cases returned `VM_RC=0`:

1. `RATE_LIMIT_LOCAL`
   - fetch not due;
   - local work eligible;
   - native action `CONTINUE_LOCAL_CURRICULUM`.

2. `RATE_LIMIT_RETRYABLE`
   - retryable + local eligible;
   - native action `RESUME_RETRYABLE_CONTEXT`.

3. `ROTATE_TO_LOCAL`
   - received + retryable + local eligible after previous retryable source;
   - native action `CONTINUE_LOCAL_CURRICULUM`.

4. `DUE_FETCH`
   - fetch due with all regular sources eligible;
   - native action `DISPATCH_NATIVE_FETCH_REQUEST`.

5. `POST_FETCH_RECEIVED`
   - native round-robin after FETCH selected `LEARN_RECEIVED_CONTEXT`.

6. `RECOVERED_FIRST`
   - recovered continuation preempted regular work;
   - exact target `work-X::|||::EXECUTE_REVISIT`.

7. `TRUE_IDLE`
   - no recovered/received/retryable/local work and fetch not due;
   - native action `WAIT_NO_ELIGIBLE_WORK`.

8. `FRESH_VM_LEDGER_REUSE`
   - persistent arbiter ledger reused across fresh VM invocation;
   - native action `LEARN_RECEIVED_CONTEXT`.

9. `MALFORMED_LEDGER_FILTER`
   - malformed record ignored;
   - `IGNORED_LEDGER_RECORD_COUNT 1`;
   - native action remained valid.

10. `LEDGER_LIMIT_REFUSAL`
   - 66 committed ledger records exceeded split bound 65;
   - native action `WAIT_LEDGER_LIMIT_EXCEEDED`.

## Final admitted gates

`RATE_LIMIT_WAIT_CONTINUES_LOCAL_WORK=PASS`

`RETRYABLE_CONTEXT_PROGRESS=PASS`

`ROUND_ROBIN_SOURCE_FAIRNESS=PASS`

`DUE_FETCH_PROGRESS=PASS`

`RECEIVED_CONTEXT_PROGRESS=PASS`

`RECOVERED_CONTINUATION_FIRST=PASS`

`TRUE_IDLE_ONLY_WHEN_NO_ELIGIBLE_WORK=PASS`

`FRESH_VM_LEDGER_REUSE=PASS`

`MALFORMED_LEDGER_FILTER=PASS`

`STEP_LIMIT_STATUS=BOUNDED`

`FETCHED_EQUALS_LEARNED=NO`

`HOST_WORK_SELECTION=NO`

`HOST_STAGE_DECISION=NO`

`HOST_RETRY_POLICY=NO`

`HOST_LEARNING=NO`

## Claim boundary

This proves only bounded structural work arbitration. It does not prove semantic importance, semantic understanding, general reasoning, bounded file I/O, production promotion, or received-context learning itself.

Keep:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next frontier

`V4-B = SEGMENTED_RECEIVED_CONTEXT_LEARNER`

Goal: replace V2.4 whole-context NEW learning pressure with persistent bounded-segment learning so a fetched context can progress segment by segment and resume after interruption instead of becoming permanently HOLD after `rc=9` pressure.

Required V4-B properties:

- native segment selection;
- persistent per-context cursor;
- exact context identity binding;
- bounded segment size;
- committed segment evidence separate from completion state;
- fresh-VM resume;
- duplicate segment idempotency;
- partial/torn state refusal where applicable;
- context is `LEARNED` only after all committed segments complete;
- no host segment choice, learning, completion decision, retry decision, or semantic interpretation;
- shadow isolation from production V2.4.
