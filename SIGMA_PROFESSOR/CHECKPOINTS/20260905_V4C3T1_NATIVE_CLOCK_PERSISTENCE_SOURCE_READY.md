# V4-C3 T1 NATIVE CLOCK PERSISTENCE — SOURCE READY / NOT RUN

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`V4C3T1_SOURCE_READY=YES`

`V4C3T1_LOCKED_SIGMAC_COMPILE=NOT_RUN`

`V4C3T1_LOCKED_VM_RUNTIME=NOT_RUN`

`V4C3T1_ADMISSION=NOT_RUN`

`NATIVE_WALL_CLOCK_DUTY_CYCLE=NOT_PROVEN`

`ONE_HOUR_DUTY_CYCLE=NOT_PROVEN`

`TEN_MINUTE_REST_CYCLE=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Design

`SIGMA_PROFESSOR/DESIGN/SIGMA_V4C3_SELF_DIRECTED_LEARNING_DUTY_CYCLE_AND_ACQUISITION_V1.md`

Design create commit:

`c8de209df2dabce552358ddb5b68d6b8c70b7abe`

Target loop:

`DISCOVER -> LEARN -> CONSOLIDATE -> FRONTIER -> REPORT -> REST -> DISCOVER`

Future acquisition path:

`FRONTIER -> ACQUIRE_REQUEST -> MECHANICAL_TRANSPORT -> PROFILE -> LEARN`

## Clock probe source

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1.sigma`

`GIT_BLOB=4d6cbf449108294d3a084fefa5167a5215e01748`

Create commit:

`26708585ca6421a1790b3ef0ed854de18735b454`

The source asks the locked VM for native `time_now`, converts the result to persisted text, parses it back natively, compares a later native observation against the persisted prior observation, and emits a native status.

`HOST_TIME_DECISION=NO`

## Preflight runner

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C3T1_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT.sh`

`GIT_BLOB=b87607ff1fb3abfa66d40a1be93152d8622a180b`

Create commit:

`72db37b218a8f00f402023fd8d43356a8472334c`

The runner:

- hard-gates locked SIGMAC and VM identities;
- hard-gates exact clock-probe Git blob;
- compiles with locked SIGMAC;
- runs the probe in an isolated shadow brain;
- makes two VM observations separated by a mechanical 2-second fixture sleep;
- does not compare timestamps on the host;
- requires the native source itself to emit `CLOCK_PROGRESS_PROVEN` on the second observation.

Host sleep creates test-time passage only. It does not decide a learning/report/rest stage.

## Claim boundary

The ABI inventory provides source evidence that `time_now` exists and returns `time(NULL)`, but runtime admission is still required.

Until the preflight is run successfully:

`SOURCE READY / NOT RUN`

Do not build a production one-hour / ten-minute duty-cycle claim from source evidence alone.

## Next action

`NEXT_ACTION=INSTALL_EXACT_V4C3T1_SOURCE_AND_PREFLIGHT_THEN_PRESERVE_FIRST_LOCKED_RESULT`
