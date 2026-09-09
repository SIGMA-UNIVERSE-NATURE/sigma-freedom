# SIGMA C5 M5 — Window Handoff

Updated: 2026-09-10 after genuine OPPO T8 FULL combined Process / IPC / Isolation PASS.

## Operating split

- Online synchronization/test lanes consume only genuine admitted checkpoints and own live/online validation.
- This window remains the offline tool-substrate lane and continues independently through T9 -> T11.
- Tool availability is distinct from SIGMA cognitive adoption/tool selection.
- Production binding from this offline lane remains NO.

## Native tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.

### T8A — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T8A_PROCESS_IPC_SUPERVISION_PASS.md`

Frozen OPPO artifact:

- source `dad5c93f0d6b4973e6b70b3400cfbaec51c2114707fe2e87c7d6a64edac9b839`
- binary `040553529973cd6075d33bb83b4e124b8a4df4e09c3206a86acedd7f965ba87d`

Admitted mechanical scope: `fork + execv(argv[])`, caller cwd, bounded stdin/stdout/stderr, process-group timeout kill, exit/signal receipts, process supervision, Unix-domain socketpair IPC, length-prefixed framing, output bounds, no shell command construction.

### T8B — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_PASS.md`

Frozen OPPO artifact:

- source `27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa`
- binary `19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

Admitted scoped isolation/recovery:

- explicit pre-opened FD capability;
- ambient FD closure;
- caller-restricted cwd;
- `PR_SET_NO_NEW_PRIVS`;
- seccomp fail-closed for new path open, socket creation/connect and exec after sandbox entry;
- caller-bounded restart after exit or signal;
- restart exhaustion receipt;
- crash-recovery counterfactual.

Namespace probe on OPPO reported user/mount/network/PID namespaces all unavailable; therefore no namespace-isolation claim is made.

### T8 FULL — PASS

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T8_FULL_COMBINED_PROCESS_IPC_ISOLATION_PASS.md`

Combined evidence:

- exact T8A prior-summary fingerprint recovery PASS;
- exact T8A/T8B source and deterministic binary rebuild locks PASS;
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 combined cases;
- 121 native process invocations;
- process/IPC/isolation mixed oracle PASS;
- spawn-to-capability-sandbox, sandbox-to-IPC, frame-to-capability, exit/signal/timeout-to-recovery and cwd/output-bound compatibility PASS;
- counterfactual, source/binary no-mutation, high-entropy leak and sandbox-removal gates PASS;
- `T8_A_B_COMBINED_COMPATIBILITY=PASS`;
- `T8_FULL_LAYER=PASS`.

## Anti-hardcoding doctrine

- capability, not answers;
- no case-ID-dependent native behavior;
- no expected-output literals in native implementation;
- dynamic/high-entropy material only after source/binary freeze;
- expected values only in external mechanical oracle;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`;
- no test cognition imported into SIGMA state;
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Current exact state

- `T4_FULL_LAYER=PASS`
- `T5_FULL_LAYER=PASS`
- `T6_FULL_LAYER=PASS`
- `T7_FULL_LAYER=PASS`
- `T8_FULL_LAYER=PASS`
- T9/T10/T11: PENDING

## Next offline sequence

`T9 -> T10 -> T11`

Immediate next layer: **T9 Integrity / Identity / Provenance**. Hashing, HMAC, signature verification, CSPRNG, content IDs, Merkle roots, receipts and provenance must remain mechanical; hash alone must never be mislabeled as provenance.
