# V4-C3 T1 R2 — NATIVE CLOCK JSON SERIALIZATION REPAIR — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Preserved R1 failure

R1 remains canonical failure evidence:

- source blob `4d6cbf449108294d3a084fefa5167a5215e01748`;
- observed bytecode SHA256 `475dbbfe7d64d8e23fc984db6b4f4e32d29d27513eeea508985ae387ce30188d`;
- first locked VM invocation `RC=6`;
- exact first VM log: `SIGMA C VM: incompatible binary operands`;
- admission FAIL.

The first-run path initializes the previous-time file empty before VM invocation. In that path, the first mixed-type binary operation in R1 is `"" + NOW` immediately after native `time_now`. The VM error therefore localizes the R1 defect to unsupported mixed string/numeric binary addition on that path. Do not reinterpret this R1 failure as proof that `time_now` itself is absent.

## R2 repair

New native source:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1R2.sigma`

Create commit:

`4c700c0ba134fc4d995e341181d888d6dbae566e`

Git blob:

`ea2049170bcb072b9a12906b74d7bc3903d816a9`

R2 removes `"" + NOW` entirely. It serializes the native numeric timestamp mechanically using native-called host ABI `json_encode`, persists the exact JSON text through `write_text`, recovers it with `json_decode`, and performs the time comparison inside native SIGMA.

`HOST_TIME_DECISION=NO`

`HOST_NUMERIC_SERIALIZATION_DECISION=NO`

JSON encode/decode is a mechanical ABI candidate only; its exact locked-runtime behavior is not claimed until this R2 gate runs.

## R2 runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C3T1R2_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT.sh`

Create commit:

`7397cf273995e3ced3101fe8fe7243f365e5756d`

Git blob:

`24d1f93e9bb5ed8b07dbb3230b57077e92df7ed7`

The runner uses a fresh isolated R2 namespace and does not mutate or overwrite the R1 failure namespace. It equality-gates locked SIGMAC/VM identities and the R2 source blob, then performs two locked-VM observations separated only by a mechanical two-second host sleep fixture.

## Exact current status

`V4C3T1R2_SOURCE_READY=YES`

`V4C3T1R2_LOCKED_SIGMAC_COMPILE=NOT_RUN`

`V4C3T1R2_LOCKED_VM_RUNTIME=NOT_RUN`

`V4C3T1R2_ADMISSION=NOT_RUN`

`JSON_NUMERIC_ROUNDTRIP_LOCKED_RUNTIME=NOT_PROVEN`

`NATIVE_WALL_CLOCK_DUTY_CYCLE=NOT_PROVEN`

`ONE_HOUR_DUTY_CYCLE=NOT_PROVEN`

`THREE_MINUTE_OBSERVE_PAUSE=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

## Next action

Exact-install R2 source and runner on Termux, preserve device SHA256 identities, then execute the first R2 locked-runtime preflight once and preserve its first result. Failure remains evidence; do not weaken the gate.
