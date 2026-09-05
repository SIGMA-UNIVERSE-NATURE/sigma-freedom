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

## CURRENT LANGUAGE-LANE IDENTITY CORRECTION — LANG-01G R2

Before any LANG-01G compile or VM run, read:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_CANONICAL_IDENTITY_METADATA_CORRECTION_R2.md`

The earlier LANG-01G R1 SHA256 metadata was incorrect even though the canonical Git blobs were unchanged. Until the living language checkpoint and shared handoff are reconciled after locked-runtime evidence, the correction checkpoint supersedes their old LANG-01G hash values.

Canonical native source remains unchanged:

`LANG01G_SOURCE_GIT_BLOB=03b03cff32eee5c35e220cd562b1081b615ca36b`

`LANG01G_SOURCE_SHA256=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`

Canonical historical R1 base runner:

`LANG01G_R1_RUNNER_GIT_BLOB=7a2a19ce9f7d36351f0f9b07ac14a900a82ffa63`

`LANG01G_R1_RUNNER_SHA256=d5f7ae2561a3f1955a9375f5eb855a133c9a9e5c7dd176064b01b7eff12035e2`

Active R2 entry runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R2.sh`

`LANG01G_R2_RUNNER_SHA256=2795bb7ae04d3d1c230ae0c609f6e33408569b33d11ac654ae8b588beda7a338`

This correction is metadata/harness-only. It does not change native lesson cognition, evidence scoring, antecedent selection, persistence policy, or the 20-case oracle set.

Keep until real locked-runtime proof:

`LANG01G_LOCKED_SIGMAC_COMPILE=NOT_RUN`

`LANG01G_TOTAL_VM_INVOCATIONS=0`

`LANG01G_ADMISSION=NOT_RUN`

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
