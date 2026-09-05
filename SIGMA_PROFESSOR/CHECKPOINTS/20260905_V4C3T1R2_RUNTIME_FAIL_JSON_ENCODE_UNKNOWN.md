# V4-C3 T1 R2 — runtime failure

Date: 2026-09-05 Asia/Ho_Chi_Minh

Observed first locked-runtime result:

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `CLOCK_SOURCE_GIT_BLOB=ea2049170bcb072b9a12906b74d7bc3903d816a9`
- `CLOCK_SOURCE_DEVICE_SHA256=ddf295510ff78e6aa559f8423addb9908e0a98cff9fc7da2252118a9dcbc312b`
- `CLOCK_BYTECODE_SHA256=a1b3af249f7366b4f4f97748fd4f616f20fc5074b8b477403e5e60a860563dc0`
- `CLOCK_FIRST_VM_RC=26`
- exact VM error: `SIGMA host: unknown operation json_encode`
- `V4C3T1R2_PROCESS_RC=41`

Therefore:

`V4C3T1R2_ADMISSION=FAIL_NOT_ADMITTED`

`JSON_ENCODE_AVAILABLE_IN_LOCKED_VM=NO_IN_OBSERVED_SCOPE`

`NATIVE_CLOCK_PERSISTENCE_ACROSS_FRESH_VM=NOT_PROVEN`

The host ABI source inventory is only source evidence and is now directly shown to differ from the locked candidate binary for `json_encode`.

Next direction: avoid guessed serialization operations; test native `time_sleep` directly with numeric `time_now` comparisons in a new R3 artifact. R1 and R2 failures remain preserved evidence.
