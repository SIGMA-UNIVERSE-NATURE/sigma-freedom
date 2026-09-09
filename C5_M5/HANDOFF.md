# SIGMA C5 M5 — Window Handoff

Updated: 2026-09-10 after genuine OPPO T8B Capability Sandbox / Crash Recovery PASS.

## Operating split

- Online synchronization/test lanes consume genuine admitted checkpoints and own live/online validation.
- This window remains the offline tool-substrate lane and continues independently through T8 -> T11.
- Tool availability is distinct from SIGMA cognitive adoption/tool selection.
- Production binding from this offline lane remains NO.

## Native tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.

### T8A — behavioral PASS, artifact publication pending fingerprint recovery

OPPO behavioral evidence already passed:

- `fork + execv(argv[])`;
- caller cwd;
- bounded stdin/stdout/stderr pipes;
- process-group timeout kill;
- exit-code receipt;
- signal receipt;
- process supervision;
- Unix-domain socketpair IPC;
- length-prefixed IPC framing;
- output bound enforcement;
- no shell command construction;
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases / 53 native invocations;
- all anti-hardcoding gates PASS.

The exact T8A OPPO `SOURCE_SHA256` and `BINARY_SHA256` were outside the copied output segment in this lane. Do not infer them. Recover them from the already-written T8A `evidence/SUMMARY.txt` before authoritative T8A publication or combined artifact locking.

### T8B — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_PASS.md`

Frozen OPPO artifact:

- source `27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa`
- binary `19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

Admitted mechanical scope:

- explicit pre-opened FD capability;
- ambient FD closure;
- caller-restricted cwd;
- `PR_SET_NO_NEW_PRIVS`;
- seccomp fail-closed for new path open, socket creation/connect and exec after sandbox entry;
- allowed pre-opened capability remains readable;
- caller-bounded restart after child exit;
- caller-bounded restart after signal/crash;
- restart exhaustion receipt;
- crash recovery counterfactual behavior.

Admission evidence:

- deterministic compile/source/binary freeze PASS;
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases;
- 57 native process invocations;
- post-tool mechanical oracle PASS;
- all sandbox/recovery/anti-hardcoding gates PASS.

## Namespace capability boundary

OPPO/Termux reported:

- `USER_NAMESPACE_AVAILABLE=NO`
- `MOUNT_NAMESPACE_AVAILABLE=NO`
- `NETWORK_NAMESPACE_AVAILABLE=NO`
- `PID_NAMESPACE_AVAILABLE=NO`

Therefore no namespace-isolation claim is made. This does not invalidate the scoped FD-capability + seccomp sandbox.

## Anti-hardcoding doctrine

- no case-ID-dependent native behavior;
- no expected-output literals in native implementation;
- dynamic/high-entropy material only after freeze;
- external mechanical oracle only;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`;
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`.

## Current exact state

- `T4_FULL_LAYER=PASS`
- `T5_FULL_LAYER=PASS`
- `T6_FULL_LAYER=PASS`
- `T7_FULL_LAYER=PASS`
- `T8A_BEHAVIORAL_ADMISSION=PASS`
- `T8A_AUTHORITATIVE_ARTIFACT_PUBLICATION=PENDING_FINGERPRINT_RECOVERY`
- `T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_ADMISSION=PASS`
- `T8_COMBINED=PENDING_T8A_EXACT_ARTIFACT_LOCK`
- `T8_FULL_LAYER=NOT_YET_ADMITTED`
- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Next offline sequence

Recover the two T8A fingerprint lines from existing device evidence, publish T8A, then run exact T8 combined. Only a genuine combined PASS may advance `T8_FULL_LAYER=PASS`.

After T8 full: `T9 -> T10 -> T11`.
