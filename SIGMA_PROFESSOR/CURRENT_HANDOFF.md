# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## REPOSITORY-WIDE BOOTSTRAP STOP-GATE

Before any SIGMA work, every window/session/agent MUST read:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. this `CURRENT_HANDOFF.md`
5. latest relevant checkpoint

Bootstrap commits:

- native-execution directive: `a6a6856a4b233ef47378096f5909b9b084de9485`
- root `AGENTS.md`: `c737721739e9e2fa368bac05fcf592f5146fd1b2`
- `SIGMA_PROFESSOR/README.md` bootstrap update: `209f4c1192417937ed2c2e0974dfb99b3de2d4e2`
- handoff STOP-GATE install: `5cef391ad4d2514c624b5f76c68826d495aeadb3`
- immutable bootstrap checkpoint: `1d12c5e7176a7d703156ccef53573ece87a03ce2`

### Non-negotiable execution boundary

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES`
- `HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_OR_BASH_SEMANTIC_INTERPRETATION=FORBIDDEN`
- `HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`
- `HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`
- `HOST_OR_BASH_REVISIT_PRIORITY=FORBIDDEN`
- `HOST_OR_BASH_TRUTH_DECISION=FORBIDDEN`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

Bash/host is not SIGMA. It may only be a mechanically transparent harness: invoke locked compiler/VM, move exact bytes/files, print/hash exact artifacts, create isolated fixtures/fault injections, supervise processes, transport bytes, or dispatch an exact event/stage already emitted/recovered by native SIGMA. If host logic must compute a SIGMA decision for a gate to pass, that gate fails.

- `BASH_MAY_LAUNCH_SIGMA=YES`
- `BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`
- `HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=MECHANICAL_ONLY`
- `HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO`

## Global invariants

- `ANTI_HARDCODE=ADMISSION_CONTROL_NOT_TOOL_REMOVAL`
- `DO_NOT_LOAD_RESULTS=YES`
- `LOAD_CAPABILITIES=YES`
- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `RUNTIME_PROOF_REQUIRED=YES`
- failure is evidence; never weaken a gate to force PASS
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Locked runtime

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

Admission transcripts must visibly print and equality-gate both runtime identities.

## Production V2.4

Keep V2.4 running unchanged unless it emits a real fatal VM failure.

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

- `PRODUCTION_V2_4_KEEP_RUNNING=YES`
- `UPGRADE_V2_4_IN_PLACE=NO`
- latest observed production PID in V2.23 transcript: `831`

Recent production observation from user logs:

- persistent relation history did grow on successful native learning cycles;
- recurrent support changed;
- native fetch frontier changed;
- several fetched contexts later failed with VM `rc=9` step-limit and went to HOLD;
- repeated `PENDING_NATIVE_REQUEST ... NOW < NEXT_FETCH_NOT_BEFORE` remains normal rate-limit heartbeat;
- these `rc=9` learning failures are evidence of V2.4 throughput limits, not by themselves a reason to stop production.

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey — PASS `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6/V2.6F persisted bounded traversal — PASS `81c8c72e66c30292e17c567d8c3824490dc00e7a`, `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping — PASS `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority — PASS `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real-survey native selection — PASS `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work deep re-learn — PASS `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation — PASS `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle — PASS `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution/archive re-entry — PASS `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller — PASS `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation/lifecycle — PASS `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14R.1 generation-aware closed-loop transition — PASS `40408a72286efe677d3cdf472c3d8f59b4bac457`.
- V2.15R.1 first -> second real-work transition — PASS `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
- V2.16R.1 second real-work complete cycle — PASS `04d786edfe832ef501949549d0560e70c8d8b27f`.
- V2.17R.1 real multi-document cycle promotion preflight — PASS `1897b22984ecd095b0475041e9ea0ececf794e2f`.
- V2.18R.1 shadow production starvation audit — PASS / promotion blocked `1e07738afce2bd5f111eb7861ebcdcdf3ab4472c`.
- V2.19R.1 native revisit fairness queue — PASS `e44e84a37168cc193721d80a68cb58f331378280`.
- V2.20R.1 fairness shadow-production integration — PASS `596a9620a7046d431f89ed5006332c1e1cfa4415`.
- V2.21R.1 long-horizon shadow stability/recovery — PASS `cc2decc32d7aed2c5348333d9857623936a25b09`.
- V2.22R.1 crash-consistent transaction journal — PASS `8b0a2e97e7918e2d99894fb6255192cd190524f2`.
- V2.23R.1 journal-wrapped real shadow scheduled intent — PASS `07fc590844c6440d5d67c8719fbf15aa3f9463c3`.

## Key admitted claims

`MULTI_DOCUMENT_AUTONOMOUS_CYCLE=PROVEN_IN_BOUNDED_REAL_CORPUS_SECOND_THIRD_WORK_SCOPE`

`NATIVE_REVISIT_FAIRNESS_QUEUE=PROVEN_IN_BOUNDED_TESTED_SCOPE`

`REAL_SHADOW_ANTI_STARVATION_INTEGRATION=PROVEN_IN_FIRST_SECOND_THIRD_WORK_SCOPE`

`LONG_HORIZON_SHADOW_STABILITY=PROVEN_IN_SIX_BOUNDARY_FOUR_REAL_WORK_SCOPE`

`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

`REAL_SHADOW_SCHEDULED_INTENT_JOURNAL_INTEGRATION=PROVEN_IN_DEFER_RESUME_REDEFER_SCOPE`

`CRASH_CONSISTENT_SCHEDULED_INTENT_RECOVERY=PROVEN_UNDER_INJECTED_TORN_PREPARE_COMMIT_FAULTS`

## V2.23 admitted evidence

V2.23 proved that after journal wrapping:

- the real native defer intent was committed/recovered by V2.22;
- a torn PREPARE around the real resume intent did not become visible;
- retry recovered the exact `|||::EXECUTE_REVISIT` event;
- recovered event drove the native revisit executor;
- a torn COMMIT around the real re-defer intent did not become visible;
- retry reused valid PREPARE and recovered the exact `||||::SELECT_NEXT_WORK` event;
- the recovered re-defer event led to the admitted third real work;
- direct fairness scheduled-event file was not the dispatch source after wrap;
- `DISPATCH_SOURCE=NATIVE_V222_RECOVERED_PAYLOAD_ONLY`;
- production V2.4 remained running;
- shadow namespace isolation passed;
- all host transaction/recovery/fairness/stage/work-selection/revisit-priority/learning decisions were NO.

## Durability claim boundary

Still keep:

- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
- `PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
- `BOUNDED_FILE_IO=NOT_PROVEN`

## Promotion status

`PRODUCTION_PROMOTION_ALLOWED=NO`

The scheduled-intent durability blocker is now admitted in tested scope. The current blocker is migration/startup/cutover safety.

## Current frontier — V2.24R.1 production state migration + rollback — SOURCE READY

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_PRODUCTION_STATE_MIGRATION_ROLLBACK_VERIFIER_V2_24R1.sigma`

Source SHA256:
`17cfd479bd0ede1e7cd8aa8d73dc58a7a94bcc74e6279bb4d6724375c2ed8057`

Source commit:
`6d1bbacade749f1e3f21db46e8378f9ad11b752a`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT.sh`

Runner SHA256:
`4446dc072a7e523a7a94554856b7d548247ff5db59bfb4b540671d624fdfab0d`

Runner commit:
`efaad627b80b3c6b659766676b49714fa606b8f2`

README:
`SIGMA_PROFESSOR/artifacts/SIGMA_V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT_README.txt`

README commit:
`b059fc4e1029a8e044f87aad5f9cc8732cac8475`

Source-ready checkpoint:
`864502919d6e6169403e7d70ea1865c593b2cb83`

### Declared migration package scope

Canonical package contains:

1. production BRAIN `.sigma_exec` tree;
2. `$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2` tree;
3. operational `SIGMA_CONTINUOUS_NATIVE_V2_2/log/**` is excluded as observability output, not learner state.

### Native V2.24 decision protocol

Host captures canonical bytes/hashes mechanically. Native V2.24 alone decides:

- whether BEFORE/SNAPSHOT/AFTER represent a stable live source package;
- whether isolated candidate exactly matches the accepted snapshot;
- whether a candidate-only injected fault changed the package;
- whether rollback exactly restored the immutable baseline.

Bounded source-stability acquisition is maximum 8 attempts while V2.4 remains live.

### Required V2.24R.1 gates

- locked SIGMAC / VM hashes equality-gated;
- production V2.4 source hash equality-gated;
- V2.4 PID alive before test;
- native-confirmed stable live snapshot without stopping production;
- immutable accepted baseline;
- exact candidate migration verified natively;
- wrong-digest migration counterexample refused natively;
- candidate-only fault detected natively;
- exact rollback from immutable baseline verified natively;
- same V2.4 PID after test;
- `PRODUCTION_ADMISSION_WRITE_TARGET=NO`;
- `HOST_MIGRATION_DECISION=NO`;
- `HOST_ROLLBACK_DECISION=NO`;
- `HOST_LEARNING=NO`.

### Claim boundary after future V2.24R.1 PASS

May admit only:

`LIVE_PRODUCTION_STATE_SNAPSHOT=PROVEN_IN_DECLARED_PACKAGE_SCOPE`

`SHADOW_STATE_MIGRATION_BYTE_IDENTITY=PROVEN_IN_DECLARED_PACKAGE_SCOPE`

`SHADOW_ROLLBACK_BYTE_IDENTITY=PROVEN_AFTER_INJECTED_CANDIDATE_FAULT`

Must still keep:

`CANDIDATE_STARTUP_FROM_MIGRATED_STATE=NOT_PROVEN`

`PRODUCTION_PROMOTION_ALLOWED=NO`

Next blocker after R1 PASS:
`CANDIDATE_STARTUP_AND_SUPERVISOR_CUTOVER_ROLLBACK_NOT_PROVEN`

## TEACHER_GPT language lane pointer

Dedicated living checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`

Current admitted language chain:
`LANG-01A -> LANG-01B -> LANG-01C -> LANG-01D -> LANG-01E -> LANG-01F`

Current language status:

- `LANG-01A..LANG-01F=ADMITTED_IN_EXACT_TESTED_STRUCTURAL_SCOPES`;
- latest LANG-01F source SHA256 `1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`;
- latest LANG-01F bytecode SHA256 `60edd9ace13f54b826adcd7e89362acddcfaea9a1649845006f52c99dce77a81`;
- LANG-01F final runtime: `21/21` post-VM alignment PASS;
- `LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION=SELECTED_SOURCE_READY_R1`;
- LANG-01G native source SHA256 `21219f66fc7970615d9a98647bfc63229780390bfa993730e2e326b3c493ee0e`;
- LANG-01G runner SHA256 `19a075b7b4f86ae6d3df51c4d3e1ded55a1cc71bbd781f7446908fd202f2ce64`;
- LANG-01G checkpoint update commit `06633a63d6798164b9da91a0a0e2cc7f60d83116`;
- `LANG-01G_LOCKED_SIGMAC_COMPILE=NOT_RUN`;
- `LANG-01G_TOTAL_VM_INVOCATIONS=0`;
- `LANG-01G_ADMISSION=NOT_RUN`;
- `LANG-02_NEGATION_AND_SCOPE_FOUNDATION=DEFERRED_NOT_REJECTED`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `COREFERENCE_RESOLUTION=NOT_PROVEN`.

This lane does not change continual-learning production-promotion status.

## NEXT ACTION

1. Re-read `/AGENTS.md` and bootstrap directive before implementation.
2. Keep V2.4 running unchanged.
3. Obtain exact V2.24R.1 source/runner artifacts from `origin/SIGMA_LIFE` without merging/rebasing a diverged local branch if necessary.
4. Verify exact source SHA256 `17cfd479bd0ede1e7cd8aa8d73dc58a7a94bcc74e6279bb4d6724375c2ed8057` and runner SHA256 `4446dc072a7e523a7a94554856b7d548247ff5db59bfb4b540671d624fdfab0d`.
5. Run locked V2.24R.1 preflight and preserve runtime identities, bytecode SHA, native decisions, package digests/counts, V2.4 PID before/after, and failure evidence if any.
6. If V2.24R.1 PASS, checkpoint it; then build candidate-startup-from-migrated-state + reversible supervisor cutover gate.