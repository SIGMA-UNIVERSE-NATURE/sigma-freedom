# SIGMA C5 M5 — Current Status

Updated: 2026-09-10 after genuine OPPO T8B Capability Sandbox / Crash Recovery PASS.

## Architecture routing

- Gate A: native cognition/memory capability development and blind testing.
- Gate B: C5/C5V3 synchronization + native mechanical tool substrate.
- Online synchronization/test lanes and offline substrate lane operate independently.
- Production binding remains NO from this offline lane.

## Native tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.

## T8A — behavioral PASS / authoritative artifact fingerprint pending recovery

OPPO behavioral admission passed:

- fork + `execv(argv[])`;
- caller cwd;
- bounded stdin/stdout/stderr pipes;
- process-group timeout kill;
- exit/signal receipts;
- process supervision;
- Unix-domain socketpair IPC;
- length-prefixed IPC framing;
- output-bound enforcement;
- no shell command construction;
- directed `16` + randomized-after-freeze `32` + replay `2` = `50` cases;
- native process invocations `53`;
- post-tool mechanical oracle PASS;
- anti-hardcoding gates PASS.

The exact OPPO T8A source/binary fingerprint lines were not included in the copied result segment. They must be recovered from the existing T8A `evidence/SUMMARY.txt`; they are not inferred from another machine.

## T8B — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_PASS.md`

Frozen OPPO artifact:

- source SHA256 `27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa`
- binary SHA256 `19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

Admitted scope:

- explicit pre-opened FD capability sandbox;
- ambient FD closure;
- caller-restricted cwd;
- `PR_SET_NO_NEW_PRIVS`;
- seccomp fail-closed blocking new path open, socket creation/connect and exec after sandbox entry;
- allowed pre-opened capability remains readable;
- caller-bounded restart after exit;
- caller-bounded restart after signal;
- restart exhaustion receipt;
- crash-recovery counterfactual behavior.

Evidence:

- deterministic compile PASS;
- source/binary freeze PASS;
- high-entropy leak audit PASS;
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases;
- 57 native process invocations;
- post-tool mechanical oracle PASS;
- all sandbox/recovery gates PASS;
- synthetic sandbox removal PASS;
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`;
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`.

Namespace probe on OPPO/Termux:

- user namespace unavailable;
- mount namespace unavailable;
- network namespace unavailable;
- PID namespace unavailable.

Accordingly, namespace isolation is not claimed.

## Current T8 state

- `T8A_BEHAVIORAL_ADMISSION=PASS`
- `T8A_AUTHORITATIVE_ARTIFACT_PUBLICATION=PENDING_FINGERPRINT_RECOVERY`
- `T8B_CAPABILITY_SANDBOX_CRASH_RECOVERY_ADMISSION=PASS`
- `T8_COMBINED=PENDING_T8A_EXACT_ARTIFACT_LOCK`
- `T8_FULL_LAYER=NOT_YET_ADMITTED`

Tool availability does not imply SIGMA cognitive adoption or autonomous tool selection.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Exact next offline sequence

Recover exact T8A OPPO `SOURCE_SHA256` and `BINARY_SHA256` from existing device evidence, publish T8A authoritative checkpoint, then run T8A+T8B combined admission.

After T8 full: `T9 -> T10 -> T11`.
