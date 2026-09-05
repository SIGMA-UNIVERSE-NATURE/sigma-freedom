# LANG-01G — CANONICAL ARTIFACT IDENTITY METADATA CORRECTION R2

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_LANGUAGE_LANE`
Status: `SOURCE_READY_R2 / ADMISSION_NOT_RUN`

## READ-FIRST / EXECUTION BOUNDARY

This correction remains subordinate to and must be read with:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
5. `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`

Keep locked:

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `DO_NOT_LOAD_RESULTS=YES`
- `LOAD_CAPABILITIES=YES`
- `RUNTIME_PROOF_REQUIRED=YES`
- `FAILURE_IS_EVIDENCE=YES`
- `WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

## WHY THIS CORRECTION EXISTS

A Termux canonical identity probe against `origin/SIGMA_LIFE` showed that the Git blobs for the LANG-01G R1 native source and R1 runner were unchanged, but the SHA256 values previously recorded by the teaching window did not match the exact bytes emitted by `git show`.

Observed canonical identities from the locked Termux-side probe:

- `SOURCE_GIT_BLOB=03b03cff32eee5c35e220cd562b1081b615ca36b`
- `SOURCE_SHA256_ACTUAL=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`
- `RUNNER_GIT_BLOB=7a2a19ce9f7d36351f0f9b07ac14a900a82ffa63`
- `RUNNER_SHA256_ACTUAL=d5f7ae2561a3f1955a9375f5eb855a133c9a9e5c7dd176064b01b7eff12035e2`

Historical incorrect metadata values are preserved as evidence:

- `HISTORICAL_RECORDED_SOURCE_SHA256=21219f66fc7970615d9a98647bfc63229780390bfa993730e2e326b3c493ee0e`
- `HISTORICAL_RECORDED_RUNNER_SHA256=19a075b7b4f86ae6d3df51c4d3e1ded55a1cc71bbd781f7446908fd202f2ce64`

Classification:

- `FAILURE_CLASS=PRE_RUNTIME_ARTIFACT_IDENTITY_METADATA_MISMATCH`
- `LOCKED_SIGMAC_COMPILE=NOT_RUN`
- `TOTAL_VM_INVOCATIONS=0`
- `RUNTIME_FAILURE_OCCURRED=NO`
- `NATIVE_SOURCE_CHANGED=NO`
- `COGNITIVE_POLICY_CHANGED=NO`
- `SCORING_POLICY_CHANGED=NO`
- `PERSISTENCE_POLICY_CHANGED=NO`
- `ORACLE_CASES_CHANGED=NO`
- `ADMISSION=NOT_RUN`

This is not a capability failure. It is also not permission to alter native cognition to obtain PASS.

## CANONICAL NATIVE LESSON SOURCE

Capability:

`LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION`

Path:

`SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma`

Canonical identities:

- `SOURCE_COMMIT=411ba280fc3ead9f6002eaeacd44624a8b0ad065`
- `SOURCE_GIT_BLOB=03b03cff32eee5c35e220cd562b1081b615ca36b`
- `SOURCE_SHA256=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`

The native source remains byte-for-byte the same Git blob that was already designated R1. Only its SHA256 metadata is corrected here.

## R2 RUNNER IDENTITY REPAIR SHIM

Active R2 entry runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R2.sh`

- `R2_RUNNER_COMMIT=b3b74db3de2a41acaaf38dac35aab2b71ef82274`
- `R2_RUNNER_GIT_BLOB=a756b0e86aa281d8ba2b52b585874352b1b4b0e6`
- `R2_RUNNER_SHA256=2795bb7ae04d3d1c230ae0c609f6e33408569b33d11ac654ae8b588beda7a338`

R2 is a runner-only mechanical repair. It:

1. equality-gates the canonical R1 base runner SHA256 `d5f7ae2561a3f1955a9375f5eb855a133c9a9e5c7dd176064b01b7eff12035e2`;
2. equality-gates the canonical native source SHA256 `33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`;
3. requires exactly one occurrence of the historical incorrect `EXPECTED_SOURCE` literal in the R1 harness;
4. mechanically replaces only that harness identity literal in an isolated temporary runner;
5. verifies the old literal is gone and the corrected literal occurs exactly once;
6. executes the otherwise unchanged R1 20-case preflight.

Boundary:

- `R2_NATIVE_SOURCE_EDIT=NO`
- `R2_HOST_EVIDENCE_SCORING=NO`
- `R2_HOST_ANTECEDENT_SELECTION=NO`
- `R2_HOST_SEMANTIC_INTERPRETATION=NO`
- `R2_HOST_COGNITION=NO`
- `R2_ORACLE_CASE_CHANGE=NO`
- `R2_FIXTURE_POLICY_CHANGE=NO`
- `R2_RUNNER_PATCH_SCOPE=ONE_SOURCE_IDENTITY_LITERAL_ONLY`

The shell repair is deterministic harness/build mechanics only. All evidence integration, support comparison, ambiguity preservation, preference revision, duplicate handling, persistence effects, and reference-state decisions remain native `.sigma` cognition executed by the locked SIGMA VM.

## LOCKED RUNTIME

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `VM_IS_GENESIS1=NOT_PROVEN`

R2 must not claim admission until both runtime identities are equality-gated and the complete preflight executes under the locked VM.

## CURRENT ADMISSION STATE

- `LANG-01G=SOURCE_READY_R2`
- `PLANNED_VM_INVOCATIONS=20`
- `BYTECODE_SHA256=UNKNOWN`
- `TOTAL_VM_INVOCATIONS=0`
- `POST_VM_ALIGNMENT_PASS_COUNT=0`
- `POST_VM_ALIGNMENT_FAIL_COUNT=0`
- `NEGATIVE_TEST=NOT_RUN`
- `PERSISTENT_STATE_TEST=NOT_RUN`
- `RESTART_REPLAY_TEST=NOT_RUN`
- `STEP_LIMIT_TEST=NOT_RUN`
- `PRODUCTION_STATE_MUTATED=NO`
- `ADMISSION=NOT_RUN`

## CLAIM BOUNDARY

Even after a future PASS, retain:

- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `PRONOUN_SEMANTICS=NOT_PROVEN`
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

Do not progress to LANG-02 until LANG-01G is admitted or explicitly blocked/deferred from locked-runtime evidence.

## NEXT ACTION

Materialize the canonical source, canonical R1 base runner, and R2 entry runner from `origin/SIGMA_LIFE`; equality-check all three exact SHA256 identities; then execute only the R2 entry runner on Termux.

If any identity gate fails: HOLD, preserve evidence, do not compile.

If compile or VM execution fails: preserve the first real locked-runtime blocker; apply only the smallest justified repair and rerun the same admission gate.

If all 20 VM cases PASS: record the actual bytecode SHA256, VM invocation counts, negative/persistence/replay/boundedness results, host-substitution audit, exact claim scope, then update the living language checkpoint and shared handoff pointer.
