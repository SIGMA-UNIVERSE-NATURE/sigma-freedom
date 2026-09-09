# SIGMA C5 M5 — T8B Capability Sandbox / Crash Recovery PASS

Updated: 2026-09-10 after genuine OPPO admission PASS.

## Result

`T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_ADMISSION=PASS`

`RESULT=T8B_PASS`

T8 full remains pending exact T8A+T8B combined admission.

## Frozen OPPO artifact

- source SHA256 `27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa`
- binary SHA256 `19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

## Admission evidence

- deterministic compile PASS
- source hash freeze PASS
- binary hash freeze PASS
- high-entropy literal leak audit PASS
- directed cases `16`
- randomized-after-freeze cases `32`
- replay cases `2`
- total admission cases `50`
- total native process invocations `57`
- post-tool mechanical oracle PASS

## Exact admitted mechanical scope

- explicit pre-opened FD capability passed into sandboxed child;
- ambient file descriptor closure;
- caller-restricted working directory;
- `PR_SET_NO_NEW_PRIVS`;
- seccomp fail-closed after sandbox entry for new path open, socket creation, connect and exec;
- allowed pre-opened FD remains readable after sandbox entry;
- caller-bounded supervisor restart after child exit;
- caller-bounded supervisor restart after signal/crash;
- restart-exhaustion receipt;
- crash-recovery counterfactual behavior.

## Android / Termux namespace probe

The device reported:

- `USER_NAMESPACE_AVAILABLE=NO`
- `MOUNT_NAMESPACE_AVAILABLE=NO`
- `NETWORK_NAMESPACE_AVAILABLE=NO`
- `PID_NAMESPACE_AVAILABLE=NO`
- `NAMESPACE_CAPABILITY_PROBE=PASS`

Therefore T8B does **not** claim namespace isolation on this OPPO device. The admitted isolation scope is the exact FD-capability + ambient-FD-closure + no-new-privs + seccomp behavior demonstrated above.

## Anti-hardcoding / cognition boundary

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

This capability does not choose programs, capabilities, restart policy, recovery semantics, or cognitive actions for SIGMA. Those decisions remain caller/native-cognition owned.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## T8 current state

- T8A process/IPC/supervision behavioral admission: PASS on OPPO, but exact OPPO source/binary fingerprint lines are not yet recovered into this lane, so T8A is not yet published as an authoritative artifact checkpoint here.
- T8B capability sandbox/crash recovery: PASS and frozen above.
- `T8_FULL_LAYER=NOT_YET_ADMITTED`.

Before T8 combined can claim exact artifact locks, recover the T8A `SOURCE_SHA256` and `BINARY_SHA256` from its existing OPPO evidence summary. Then run exact T8A+T8B combined admission.
