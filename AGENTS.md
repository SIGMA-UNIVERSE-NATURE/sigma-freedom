# SIGMA REPOSITORY BOOTSTRAP — READ BEFORE ANY WORK

This file is the repository-wide entry flag for every development window/session/agent.

## Mandatory first reads

Before inspecting, modifying, testing, teaching, integrating, or promoting SIGMA, read in this order:

1. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
3. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
4. latest relevant file in `SIGMA_PROFESSOR/CHECKPOINTS/`

Do not begin implementation before those files are understood.

## CURRENT CRITICAL OVERRIDE — V2.24R.1 HOST-ASSISTED DRAFT BLOCKED

Read this correction before doing any V2.24 work:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V224R1_HOST_ASSISTED_MIGRATION_BLOCKED_NATIVE_ONLY_CORRECTION.md`

The previously prepared V2.24R.1 production-state migration/rollback runner is **DRAFT/BLOCKED** because Bash/host still performs material migration/rollback mechanics. It MUST NOT be run or admitted as a native SIGMA migration capability.

Keep locked:

`V224R1_PRODUCTION_STATE_MIGRATION_ROLLBACK_PREFLIGHT=NOT_ADMITTED`

`NATIVE_PRODUCTION_STATE_MIGRATION=NOT_PROVEN`

`NATIVE_PRODUCTION_STATE_ROLLBACK=NOT_PROVEN`

`PRODUCTION_PROMOTION_ALLOWED=NO`

If `CURRENT_HANDOFF.md` still says V2.24R.1 is SOURCE READY, this correction checkpoint supersedes that frontier text until the handoff is reconciled.

## CURRENT LANGUAGE-LANE FLAG — LANG-01G R3 ADMITTED

Read the living language checkpoint before any further language work:

`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`

LANG-01G has now completed its original 20-case locked-VM admission gate after a runner-only fresh-state fixture repair.

Canonical native source remains:

`LANG01G_SOURCE_GIT_BLOB=03b03cff32eee5c35e220cd562b1081b615ca36b`

`LANG01G_SOURCE_SHA256=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`

Final R3 entry runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R3.sh`

`LANG01G_R3_RUNNER_GIT_BLOB=6b51762246b348935d15816aa2a0c054e766432f`

`LANG01G_R3_RUNNER_SHA256=8d89cc504f36ce1190b7d364eac9cc76b0fe718824c54f484cf6b4da9561271c`

Observed R3 final summary:

`LANG01G_TOTAL_VM_INVOCATIONS=20`

`LANG01G_POST_VM_ALIGNMENT_PASS_COUNT=20`

`LANG01G_POST_VM_ALIGNMENT_FAIL_COUNT=0`

`LANG01G_VM_NONZERO_COUNT=0`

`LANG01G_STEP_LIMIT_HIT_COUNT=0`

`LANG01G_NEGATIVE_TEST=PASS`

`LANG01G_PERSISTENT_STATE_TEST=PASS`

`LANG01G_RESTART_REPLAY_TEST=PASS`

`LANG01G_ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE`

The R3 user-supplied final tail did not include its bytecode SHA256 line. Keep:

`LANG01G_R3_BYTECODE_SHA256=UNKNOWN_NOT_IN_SUPPLIED_R3_TAIL`

Do not infer it from the historical R2 failed run.

Historical R2 failure remains evidence: first locked compile passed, then CASE_001 failed `VM_RC=22` / `SIGMA host: string required`. Native locked-VM diagnostic localized the failure to `str_split` receiving the result of `read_text` on an absent fresh-state file. R3 only initialized that fixture as a zero-length state file; it did not change native lesson cognition, evidence scoring, antecedent selection, persistence policy, or the 20-case oracle set.

Keep claim limits:

`PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`

`COREFERENCE_RESOLUTION=NOT_PROVEN`

`PRONOUN_SEMANTICS=NOT_PROVEN`

`REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

No production binding is implied. The next language capability must be reselected dependency-first/capability-first; `LANG-02_NEGATION_AND_SCOPE_FOUNDATION` remains deferred, not rejected.

## Non-negotiable execution boundary

`SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`

`ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`

`HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`

`HOST_OR_BASH_COGNITION=FORBIDDEN`

`HOST_OR_BASH_LEARNING=FORBIDDEN`

`HOST_SEMANTIC_INTERPRETATION=NO`

`HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

All actual SIGMA learning, selection, scheduling decisions, curriculum decisions, revalidation decisions, lifecycle decisions, fairness decisions, truth decisions, knowledge generation, and cognitive computation must execute in native `.sigma` bytecode under the locked SIGMA VM.

Bash/host MUST NOT implement a missing native capability.

Bash/host may only be an external mechanical harness: invoke compiler/VM, exact byte/file transport, hashes, return codes, isolated fixture setup, fault injection, process supervision, and exact dispatch of an event/stage already chosen by native SIGMA. It may not choose or reinterpret the event.

`BASH_MAY_LAUNCH_SIGMA=YES`

`BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`

If host/Bash must calculate the answer for a gate to pass, the gate fails.

## Admission discipline

`DO_NOT_LOAD_RESULTS=YES`

`LOAD_CAPABILITIES=YES`

`RUNTIME_PROOF_REQUIRED=YES`

`FAILURE_IS_EVIDENCE=YES`

`WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

Compile/file/shell success alone is not a SIGMA capability proof.

## Locked runtime

`SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

`VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`

## Production

Keep production V2.4 running unchanged unless a real VM failure occurs.

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

## Claim limits

Unless separately admitted by locked-runtime proof, keep:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`

When any historical artifact conflicts with this file, a newer correction checkpoint, or the bootstrap directive, treat the historical artifact as provenance only and follow the stricter current rule.
