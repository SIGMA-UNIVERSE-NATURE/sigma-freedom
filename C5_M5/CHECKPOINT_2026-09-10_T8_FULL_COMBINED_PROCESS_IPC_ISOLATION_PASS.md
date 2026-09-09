# SIGMA T8 Full Combined Process / IPC / Isolation — PASS

Date: 2026-09-10
Lane: offline native tool-substrate admission
Device: OPPO / Termux

## Result

- `T8_A_B_COMBINED_COMPATIBILITY=PASS`
- `T8_FULL_LAYER=PASS`
- `RESULT=T8_FULL_PASS`

## Frozen OPPO artifacts

T8A Process / IPC / Supervision:

- source SHA256 `dad5c93f0d6b4973e6b70b3400cfbaec51c2114707fe2e87c7d6a64edac9b839`
- binary SHA256 `040553529973cd6075d33bb83b4e124b8a4df4e09c3206a86acedd7f965ba87d`

T8B Capability Sandbox / Crash Recovery:

- source SHA256 `27f6d462605d91458a38b8bab518eae00c74ed4dc32071b85617656e500117fa`
- binary SHA256 `19cf4a0fc2b23f0783d795a0b3f17c107890eed2090810a153c9fe29b2f9ecbd`

Compiler:

- `/data/data/com.termux/files/usr/bin/clang++`

## Exact combined evidence

- `T8A_PRIOR_SUMMARY_RECOVERY=PASS`
- `T8A_SOURCE_LOCK=PASS`
- `T8B_SOURCE_LOCK=PASS`
- `T8A_DETERMINISTIC_COMPILE=PASS`
- `T8A_ADMITTED_BINARY_REBUILD_LOCK=PASS`
- `T8B_DETERMINISTIC_COMPILE=PASS`
- `T8B_ADMITTED_BINARY_REBUILD_LOCK=PASS`
- `T8A_ADMITTED_ARTIFACT_LOCK=PASS`
- `T8B_ADMITTED_ARTIFACT_LOCK=PASS`
- directed combined cases `16`
- randomized-after-freeze combined cases `32`
- replay combined cases `2`
- total combined cases `50`
- total native process invocations `121`
- mixed process/IPC/isolation oracle PASS
- spawn-to-FD-capability-sandbox compatibility PASS
- sandbox-to-Unix-IPC compatibility PASS
- IPC-frame-to-capability compatibility PASS
- exit/signal/timeout-to-recovery compatibility PASS
- cwd/output-bound isolation compatibility PASS
- crash-recovery counterfactual PASS
- source/binary no mutation PASS
- high-entropy literal leak audit PASS
- synthetic sandbox removal PASS

## Full admitted T8 mechanical scope

From T8A:

- fork + `execv(argv[])` without shell command construction;
- caller-supplied cwd;
- bounded stdin/stdout/stderr pipes;
- process-group timeout kill;
- exit/signal receipts;
- process supervision;
- Unix-domain socketpair IPC;
- length-prefixed IPC framing;
- output-bound enforcement.

From T8B:

- explicit pre-opened FD capability sandbox;
- ambient FD closure;
- caller-restricted cwd;
- `PR_SET_NO_NEW_PRIVS`;
- seccomp fail-closed for new path opens, socket creation/connect and exec after sandbox entry;
- allowed pre-opened capability remains readable;
- caller-bounded supervisor restart after exit or signal;
- restart exhaustion receipt;
- crash-recovery counterfactual behavior.

## Namespace evidence / boundary

OPPO/Termux reported:

- `USER_NAMESPACE_AVAILABLE=NO`
- `MOUNT_NAMESPACE_AVAILABLE=NO`
- `NETWORK_NAMESPACE_AVAILABLE=NO`
- `PID_NAMESPACE_AVAILABLE=NO`

Therefore:

- namespace capability probe PASS;
- no namespace-isolation claim is made;
- T8 full is admitted on the demonstrated FD-capability + seccomp isolation scope, not on unavailable namespace primitives.

## Anti-hardcoding / cognition boundary

- `NO_SHELL_COMMAND_CONSTRUCTION=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

Tool availability does not imply SIGMA knows when to spawn, isolate, restart, or use IPC. Native cognition must own those decisions later.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Next offline layer

`T9_INTEGRITY_IDENTITY_PROVENANCE`
