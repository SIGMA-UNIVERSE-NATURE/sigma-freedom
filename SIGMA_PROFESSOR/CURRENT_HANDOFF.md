# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## REPOSITORY-WIDE BOOTSTRAP STOP-GATE

Before any SIGMA work, every window/session/agent MUST read:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. this `CURRENT_HANDOFF.md`
5. latest relevant checkpoint

Non-negotiable:

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

Bash/host is not SIGMA. It may only be a mechanically transparent harness: invoke locked compiler/VM, move exact bytes/files, print/hash artifacts, create isolated fixtures/fault injections, supervise processes, transport bytes, or dispatch exact events already emitted/recovered by native SIGMA. If host logic must compute a SIGMA decision for a gate to pass, the gate fails.

- `BASH_MAY_LAUNCH_SIGMA=YES`
- `BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`
- `HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=MECHANICAL_ONLY`
- `HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO`

Interactive Termux safety: copy-paste helper blocks must not use top-level `exit/logout` to signal ordinary install/audit errors. Test runner scripts may use `exit` internally only when launched as their own process, never via `source` / `.`.

## Global invariants

- `ANTI_HARDCODE=ADMISSION_CONTROL_NOT_TOOL_REMOVAL`
- `DO_NOT_LOAD_RESULTS=YES`
- `LOAD_CAPABILITIES=YES`
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

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

Admission transcripts must visibly print and equality-gate both identities.

## Production V2.4

Keep V2.4 running unchanged while V4 successor is built and proven in shadow.

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

- `PRODUCTION_V2_4_KEEP_RUNNING=YES`
- `UPGRADE_V2_4_IN_PLACE=NO`
- latest observed production PID in V4-B transcript: `831`

Observed V2.4 limitations from real logs:

- real structural memory does grow on successful cycles;
- recurrent support/frontier changes are real;
- repeated pending request lines are rate-limit heartbeat, not learning;
- several fetched contexts failed native learning with VM `rc=9` and were quarantined;
- V2.4 marks a request fetched before proving the fetched document was learned;
- whole-context NEW learning therefore has low throughput under step pressure;
- legacy reconsider traversal can repeatedly revisit an earlier context.

These are reasons to build the V4 successor, not reasons to kill running V2.4.

## Admitted continual-learning chain through V2.23

- V2.5B.2 frozen survey — PASS `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6/V2.6F persisted traversal — PASS `81c8c72e66c30292e17c567d8c3824490dc00e7a`, `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7 grouping — PASS `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P priority — PASS `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R selector — PASS `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D deep learn — PASS `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9 revalidation — PASS `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10 lifecycle — PASS `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11 revisit/archive — PASS `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12 controller — PASS `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13 generation-aware lifecycle — PASS `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14 closed loop — PASS `40408a72286efe677d3cdf472c3d8f59b4bac457`.
- V2.15 transition — PASS `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
- V2.16 second real work cycle — PASS `04d786edfe832ef501949549d0560e70c8d8b27f`.
- V2.17 multi-document promotion preflight — PASS `1897b22984ecd095b0475041e9ea0ececf794e2f`.
- V2.18 starvation audit — PASS / promotion blocked `1e07738afce2bd5f111eb7861ebcdcdf3ab4472c`.
- V2.19 native fairness queue — PASS `e44e84a37168cc193721d80a68cb58f331378280`.
- V2.20 fairness shadow integration — PASS `596a9620a7046d431f89ed5006332c1e1cfa4415`.
- V2.21 long-horizon shadow stability — PASS `cc2decc32d7aed2c5348333d9857623936a25b09`.
- V2.22 crash-consistent transaction journal — PASS `8b0a2e97e7918e2d99894fb6255192cd190524f2`.
- V2.23 journal-wrapped real scheduled intent — PASS `07fc590844c6440d5d67c8719fbf15aa3f9463c3`.

Key admitted claims:

- `NATIVE_REVISIT_FAIRNESS_QUEUE=PROVEN_IN_BOUNDED_TESTED_SCOPE`
- `LONG_HORIZON_SHADOW_STABILITY=PROVEN_IN_SIX_BOUNDARY_FOUR_REAL_WORK_SCOPE`
- `CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`
- `REAL_SHADOW_SCHEDULED_INTENT_JOURNAL_INTEGRATION=PROVEN_IN_DEFER_RESUME_REDEFER_SCOPE`
- `CRASH_CONSISTENT_SCHEDULED_INTENT_RECOVERY=PROVEN_UNDER_INJECTED_TORN_PREPARE_COMMIT_FAULTS`

## V2.24 host-assisted migration draft — BLOCKED

The old V2.24R.1 migration/rollback runner is historical draft only.

Correction checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V224R1_HOST_ASSISTED_MIGRATION_BLOCKED_NATIVE_ONLY_CORRECTION.md`

Keep:

- `V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT=NOT_ADMITTED`
- `NATIVE_PRODUCTION_STATE_MIGRATION=NOT_PROVEN`
- `NATIVE_PRODUCTION_STATE_ROLLBACK=NOT_PROVEN`
- do NOT run/admit that host-assisted draft as SIGMA capability.

## V4 production-successor program

V4 is the active efficiency-upgrade lane. V2.4 remains production baseline until V4 continuous shadow execution, durability, real-input recovery, and reversible cutover are proven.

### V4-A.1 native productivity/work arbiter — ADMITTED PASS

Checkpoint:
`b9f23d3a6a94116818581458fbdb8e788deb2804`

Native source SHA256:
`12c32f07d39bacedf8dd1a2371f9b33801106d256d6166fed03fbaa224416ed2`

Observed bytecode SHA256:
`be7a97147d840d79a4bc0745d4c192a3e29466fffb7c81905a7d7424b78a6961`

Admitted:

- `NATIVE_PRODUCTIVITY_WORK_ARBITRATION=PROVEN_IN_BOUNDED_TESTED_SCOPE`
- rate-limit wait continues local/retryable work;
- round-robin source fairness passed;
- due fetch progress passed;
- received context progress passed;
- recovered continuation has priority;
- true WAIT only when no eligible work;
- fresh-VM ledger reuse passed;
- malformed ledger filtering passed;
- `FETCHED_EQUALS_LEARNED=NO`;
- host work/stage/retry/learning decisions all NO;
- shadow isolation passed;
- V2.4 remained PID `831`.

### V4-B.1 segmented received-context learner — ADMITTED PASS

Checkpoint:
`6c1d7f4ea3414ed7416d6dfd5834129df6d79aa6`

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma`

Source SHA256:
`2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`

Runner Git blob:
`4faf37671c591f7201c930bc5f000a542d377d8a`

Runner SHA256 canonical Termux observation:
`3e601c8a6fae5d1e5b93909d150f90e7918e4cd72936176e05b6de908e512f03`

The user-provided final V4-B runtime tail did not include the V4-B bytecode SHA line. Do not invent it.

Admitted:

- `SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE`
- two lines per native invocation;
- fresh-VM cursor resume;
- malformed cursor filtering;
- completion only after all segments;
- already-complete idempotency;
- evidence-only crash retry without duplicate evidence;
- foreign-context cursor ignored;
- token/context line bound refusals;
- final-cursor missing-completion recovery;
- out-of-range cursor refusal with mutation disabled;
- `FETCHED_EQUALS_LEARNED=NO`;
- host segment/completion/retry/learning decisions all NO;
- shadow isolation passed;
- V2.4 remained PID `831`.

Still not proven after V4-B.1:
`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`.

## CURRENT FRONTIER — V4-B.2 real V2.4 rc=9 held-context replay — SOURCE READY

Checkpoint:
`27273b9614b33c4aff53d1e7e251136cdc9e3035`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT.sh`

Runner commit:
`ca9bb3148e0e40ec4fc09fc49df9c8c9930bf3f8`

Runner Git blob:
`6ea6a0269bcbe00ca44238a66c60c61d9b603e65`

Runner SHA256:
`NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX`

Production storage verified from V2.4 runner:

- raw: `$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/raw/<SHA>.document`
- hold evidence: `$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/hold/<SHA>.hold`

V4-B2 requires exact document SHA and exact V2.4 hold evidence `VM_RC=9`, then copies exact bytes into isolated V4-B shadow state.

Five real observed rc=9 contexts:

- `49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`
- `59cd0bc563b1dc8566c88623366403b53f4e9094ca98ef4fe2d9e6531dc5a774`
- `0d911059d92f2af2601f39420c7aa0865fb24fbbc96aca96961d53b19260d8c3`
- `c12f847d694599d12cf35b5f489f1061e79a3fe3cf2f648684da55d387a2b16b`
- `ee5aca6dbe12ffcdd7e5b4aefeb3b5f8bb418b7d9eb4f59404c76b661bc086ba`

Dispatch discipline:

- 35 fixed VM invocations per context;
- host does not inspect status to choose segment or retry;
- native V4-B chooses cursor/segment/completion/refusal;
- production raw is read-only source;
- production BRAIN is not a write target;
- V2.4 must stay running with same PID.

Future PASS may admit only:
`REAL_V24_RC9_CONTEXT_RECOVERY=PROVEN_IN_FIVE_OBSERVED_HELD_CONTEXT_SCOPE`.

After that, next step is to integrate V4-A + V4-B into an isolated continuous V4 shadow controller. Do not promote V4 yet.

## Promotion status

`PRODUCTION_PROMOTION_ALLOWED=NO`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

Still keep:

- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
- `PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## TEACHER_GPT language lane pointer

Dedicated living checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`

Admitted language chain:
`LANG-01A -> LANG-01B -> LANG-01C -> LANG-01D -> LANG-01E -> LANG-01F -> LANG-01G`

Current language frontier:
`LANG-02A_NATIVE_OPERATOR_SCOPE_BINDING=SELECTED_SOURCE_READY_R1_NOT_ADMITTED`

Current language status:

- `LANG-01A..LANG-01G=ADMITTED_IN_EXACT_TESTED_STRUCTURAL_SCOPES`;
- LANG-01F source SHA256 `1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`;
- LANG-01F bytecode SHA256 `60edd9ace13f54b826adcd7e89362acddcfaea9a1649845006f52c99dce77a81`;
- LANG-01F final runtime `21/21` PASS;
- `LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION=ADMITTED_IN_EXACT_TESTED_PREFLIGHT_SCOPE`;
- LANG-01G canonical source Git blob `03b03cff32eee5c35e220cd562b1081b615ca36b`;
- LANG-01G canonical source SHA256 `33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`;
- LANG-01G R3 runner Git blob `6b51762246b348935d15816aa2a0c054e766432f`;
- LANG-01G R3 runner SHA256 `8d89cc504f36ce1190b7d364eac9cc76b0fe718824c54f484cf6b4da9561271c`;
- LANG-01G living checkpoint admission update commit `7336afb587f3b6909d73a2c5c45b0839c4b11ea0`;
- LANG-01G final R3 runtime `20/20` PASS;
- `LANG-01G_POST_VM_ALIGNMENT_FAIL_COUNT=0`;
- `LANG-01G_VM_NONZERO_COUNT=0`;
- `LANG-01G_STEP_LIMIT_HIT_COUNT=0`;
- `LANG-01G_NEGATIVE_TEST=PASS`;
- `LANG-01G_PERSISTENT_STATE_TEST=PASS`;
- `LANG-01G_RESTART_REPLAY_TEST=PASS`;
- `LANG-01G_PRODUCTION_STATE_MUTATED=NO`;
- `LANG-01G_R3_BYTECODE_SHA256=UNKNOWN_NOT_IN_SUPPLIED_R3_TAIL` — do not infer from the historical R2 failed-run bytecode;
- historical R2 `CASE_001_TIE` `VM_RC=22` / `SIGMA host: string required` remains failure evidence;
- R3 repair was runner-only zero-length fresh-state fixture initialization; native source, cognition, persistence policy, and 20-case oracle were unchanged;
- `LANG-02_NEGATION_AND_SCOPE_FOUNDATION=DECOMPOSED_NOT_ADMITTED`;
- `LANG-02A_NATIVE_OPERATOR_SCOPE_BINDING=SELECTED_SOURCE_READY_R1`;
- LANG-02A source `SIGMA_PROFESSOR/artifacts/SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_V1.sigma`;
- LANG-02A source commit `32df3e826656f6c06ec6379b8bc3a378ce446bf4`;
- LANG-02A source Git blob `226b06c337c09f3e0dc3f35a44c3ba22d73affaf`;
- LANG-02A source SHA256 `7a40e92e11c7c89574d3b975bb3210a7a7a23690251951da68be9e7edbfe292b`;
- LANG-02A runner `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_02A_NATIVE_OPERATOR_SCOPE_BINDING_PREFLIGHT.sh`;
- LANG-02A runner commit `685eba8fa2f6fbe74ccc5c0c4c1934f4cc5d7e06`;
- LANG-02A runner Git blob `269b7cc0f44f2d442cabd9ae079f0bad97efd69a`;
- LANG-02A runner SHA256 `720148bb4d22acb23e47118139095b4e73816491029ea2555448641779fc5bc4`;
- `LANG-02A_PLANNED_VM_INVOCATIONS=20`;
- `LANG-02A_SCOPE_CAPACITY=8`;
- `LANG-02A_PERSISTENT_STATE=NA`;
- `LANG-02A_LOCKED_SIGMAC_COMPILE=NOT_RUN`;
- `LANG-02A_BYTECODE_SHA256=UNKNOWN`;
- `LANG-02A_TOTAL_VM_INVOCATIONS=0`;
- `LANG-02A_RUNTIME_PROOF=NOT_RUN`;
- `LANG-02A_ADMISSION=NOT_RUN`;
- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`;
- `SURFACE_NEGATION_RECOGNITION=NOT_PROVEN`;
- `LOGICAL_NEGATION=NOT_PROVEN`;
- `PROPOSITION_TRUTH=NOT_PROVEN`;
- `SEMANTIC_SCOPE=NOT_PROVEN`;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `COREFERENCE_RESOLUTION=NOT_PROVEN`;
- `PRONOUN_SEMANTICS=NOT_PROVEN`;
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`.

Language next action:
`RUN_LANG_02A_R1_ON_LOCKED_TERMUX_SIGMAC_AND_VM`

This language lane does not change continual-learning/V4 production-promotion status.

## NEXT ACTION

1. Keep V2.4 running unchanged.
2. Fetch exact V4-B2 replay runner from `origin/SIGMA_LIFE` by Git blob `6ea6a0269bcbe00ca44238a66c60c61d9b603e65`; do not merge/rebase the diverged local branch.
3. Record canonical Termux SHA256 of that exact runner.
4. Run V4-B2 as its own process, never via `source` / `.`.
5. Preserve every real-document identity check, V2.4 `VM_RC=9` hold proof, every V4-B native VM RC, final completion status, and V2.4 PID before/after.
6. If any real context is missing, no longer held with rc9 evidence, natively refused by V4-B bounds, or fails VM execution, preserve that as failure evidence; do not weaken the gate.
7. If all five complete, checkpoint V4-B2 and then build isolated continuous V4 shadow controller integrating V4-A + V4-B.