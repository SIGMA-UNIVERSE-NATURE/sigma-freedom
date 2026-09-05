# V4-A.1 PRODUCTIVITY WORK ARBITER — SOURCE READY

Date: 2026-09-05
Status: SOURCE READY / NOT YET ADMITTED

## Production policy

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

`V4_PRODUCTION_CANDIDATE_BUILD_IN_PARALLEL=YES`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Motivation

Live V2.4 evidence shows real structural progress but degraded throughput under repeated whole-context VM `rc=9`, fetched-vs-learned ambiguity, repeated reconsideration, and rate-limit heartbeat idle behavior.

V4-A begins the successor upgrade by teaching native SIGMA structural work arbitration rather than changing the running V2.4 process.

## Native source

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_PRODUCTIVITY_WORK_ARBITER_V4A1.sigma`

SHA256:
`12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2`

Source commit:
`4acb78266263bb847c2e30a49c7ab80f4bcf7897`

## Admission harness

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4A1_PRODUCTIVITY_WORK_ARBITER_PREFLIGHT.sh`

SHA256:
`58387b5843f8b58b3321564a4e9356478eba19f1ae9553baa4c33bf2c8aefcbb`

Runner commit:
`ef369402d7bb24d805f6b7ad4ace980dbb0887bb`

README commit:
`631c7f96a5caa1b3a0b5712b3577ce74580b5db4`

## Static readiness

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC = 0

## Intended native policy

1. recovered continuation first;
2. otherwise structural round-robin over RECEIVED / RETRYABLE / LOCAL / FETCH using last committed source;
3. fetch becomes eligible only when native `time_now` reaches `NEXT_FETCH_NOT_BEFORE`;
4. rate-limit waiting must not force idle if received/retryable/local work exists;
5. WAIT only when no productive source is eligible;
6. fetched transport receipt does not equal learned completion.

No semantic ranking is performed.

## Required runtime gates

- rate-limit + local work -> `CONTINUE_LOCAL_CURRICULUM`;
- retryable work progresses;
- source rotation progresses across local/fetch/received;
- recovered continuation preempts ordinary arbitration;
- true WAIT only with no eligible work;
- fresh VM reuses committed ledger;
- malformed ledger record ignored;
- >65 ledger lines produces bounded refusal;
- `HOST_WORK_SELECTION=NO`;
- `HOST_STAGE_DECISION=NO`;
- `HOST_RETRY_POLICY=NO`;
- `HOST_LEARNING=NO`.

## Claim boundary after future PASS

May admit only:

`NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE`

Still keep:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`BOUNDED_FILE_IO=NOT_PROVEN`

`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next after PASS

`NEXT_ACTION=TEACH_V4B_SEGMENTED_RECEIVED_CONTEXT_LEARNER`
