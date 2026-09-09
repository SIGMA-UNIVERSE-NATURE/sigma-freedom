# SIGMA T8A Process / IPC / Supervision — PASS

Date: 2026-09-10
Lane: offline native tool-substrate admission
Device: OPPO / Termux

## Result

`T8A_PROCESS_IPC_SUPERVISION_ADMISSION=PASS`

This checkpoint closes the authoritative T8A artifact identity after the later T8 combined run recovered the exact prior OPPO T8A fingerprint from the existing T8A `evidence/SUMMARY.txt` and deterministically rebuilt the native binary to the same hash.

## Frozen OPPO artifact

- source SHA256 `dad5c93f0d6b4973e6b70b3400cfbaec51c2114707fe2e87c7d6a64edac9b839`
- binary SHA256 `040553529973cd6075d33bb83b4e124b8a4df4e09c3206a86acedd7f965ba87d`
- compiler `/data/data/com.termux/files/usr/bin/clang++`

## Admission evidence

Original T8A OPPO admission:

- directed cases `16`
- randomized-after-freeze cases `32`
- replay cases `2`
- total cases `50`
- native process invocations `53`
- deterministic compile PASS
- source/binary freeze PASS
- high-entropy literal leak audit PASS
- post-tool mechanical oracle PASS
- counterfactual behavior change PASS
- synthetic sandbox removal PASS

Exact artifact recovery/validation from T8 combined:

- `T8A_PRIOR_SUMMARY_RECOVERY=PASS`
- recovered source SHA256 exactly matches bundled T8A source
- recovered binary SHA256 `040553529973cd6075d33bb83b4e124b8a4df4e09c3206a86acedd7f965ba87d`
- `T8A_DETERMINISTIC_COMPILE=PASS`
- `T8A_ADMITTED_BINARY_REBUILD_LOCK=PASS`
- `T8A_ADMITTED_ARTIFACT_LOCK=PASS`

## Admitted mechanical scope

- `fork + execv(argv[])`;
- no shell command construction;
- caller-supplied cwd;
- bounded stdin/stdout/stderr pipes;
- process-group timeout kill;
- exact exit-code receipt;
- exact signal receipt;
- process supervision;
- Unix-domain `socketpair` IPC;
- 32-bit big-endian length-prefixed IPC framing;
- output-bound enforcement.

## Claim boundary

- `NO_SHELL_COMMAND_CONSTRUCTION=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`
- capability sandbox and crash recovery are separately admitted in T8B.
- namespace isolation is not implied by T8A.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

T8A supplies process/IPC mechanics only. It does not choose programs, commands, recovery policy, relevance, or semantic actions for SIGMA.
