# V4-C3 T1 NATIVE CLOCK PERSISTENCE — FIRST LOCKED-VM FAILURE RC=6

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Evidence status

This checkpoint preserves the first device-side locked-runtime result for V4-C3 T1.

`FAILURE_IS_EVIDENCE=YES`

`V4C3T1_EXACT_INSTALL=PASS`

`V4C3T1_LOCKED_SIGMAC_COMPILE=PASS_FOR_THIS_FIRST_OBSERVED_RUN`

`V4C3T1_LOCKED_VM_RUNTIME=FAIL_FIRST_INVOCATION_RC_6`

`V4C3T1_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT=FAIL`

`V4C3T1_ADMISSION=FAIL_NOT_ADMITTED`

`NATIVE_WALL_CLOCK_DUTY_CYCLE=NOT_PROVEN`

`ONE_HOUR_LEARNING_INTERVAL=NOT_PROVEN`

`THREE_MINUTE_OBSERVE_PAUSE=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Do not rerun blindly and do not weaken the gate. Preserve this first failure as canonical evidence.

## Exact installed identities observed on device

Remote SIGMA_LIFE snapshot used for exact install:

`REMOTE_SIGMA_LIFE=c37675d234d160183483019ed34893c9b52684d9`

Native clock probe:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1.sigma`

`CLOCK_SOURCE_GIT_BLOB=4d6cbf449108294d3a084fefa5167a5215e01748`

`CLOCK_SOURCE_DEVICE_SHA256=eee3a8ccb5b7d2ebadb972eb9f33900ef3a77c952347d331a6bbaf64ac45e1f0`

Preflight runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C3T1_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT.sh`

`CLOCK_RUNNER_GIT_BLOB=b87607ff1fb3abfa66d40a1be93152d8622a180b`

`CLOCK_RUNNER_DEVICE_SHA256=96c5e83f23a8d4ef2b08b9e1eda016f8c3877665966707d20f325399b65f7a3f`

## First compile/runtime transcript evidence

Observed compile result:

`CLOCK_SIGMAC_RC=0`

Observed bytecode identity:

`CLOCK_BYTECODE_SHA256=475dbbfe7d64d8e23fc984db6b4f4e32d29d27513eeea508985ae387ce30188d`

First locked VM invocation:

`CLOCK_FIRST_VM_RC=6`

Runner stop gate:

`HOLD=CLOCK_FIRST_VM_FAILED`

Outer runner process result:

`V4C3T1_PROCESS_RC=41`

First VM log path reported by device:

`/data/data/com.termux/files/home/SIGMA/SIGMA_V4C3T1_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT/run.1788605600.26319/log/first.log`

Top-level captured transcript:

`/data/data/com.termux/files/home/SIGMA/V4C3T1_CLOCK_FIRST_20260905_175320.log`

## What this evidence proves

- the exact source/runner install matched their pinned Git blobs before execution;
- the clock probe compiled successfully under the locked SIGMAC in this observed run;
- a concrete bytecode SHA-256 was produced and is now preserved;
- the first locked-VM invocation returned nonzero `RC=6`;
- the gate correctly failed closed before a second observation or any clock-progress claim.

## What is NOT yet known

The exact runtime cause of `RC=6` is **not established by the supplied outer transcript alone**.

The source inventory previously recorded `time_now` as present in inspected VM source and returning `time(NULL)` according to that source excerpt, but source presence is not locked-binary/runtime proof. Therefore this failure must not be reinterpreted as either `time_now unsupported` or `probe bug` without the exact first VM log.

Keep:

`TIME_NOW_LOCKED_RUNTIME_SEMANTICS=NOT_PROVEN`

`RC6_ROOT_CAUSE=NOT_YET_LOCALIZED`

`HOST_TIME_DECISION=NO`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Required next action

Read and preserve the exact bytes/text of:

`.../run.1788605600.26319/log/first.log`

Then localize the first native/runtime failure from that log. If a source repair is required, create a new revision/artifact identity and a new runner pin. Do not mutate this first-failure evidence and do not claim PASS until the repaired revision independently compiles and executes under the locked VM.
