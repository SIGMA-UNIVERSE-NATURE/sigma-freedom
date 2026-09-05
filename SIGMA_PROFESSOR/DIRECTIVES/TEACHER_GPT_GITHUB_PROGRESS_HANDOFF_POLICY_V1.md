# TEACHER_GPT GITHUB PROGRESS + HANDOFF UPDATE POLICY V1

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Status: ACTIVE / LANE COORDINATION POLICY

## Purpose

This directive exists so a later ChatGPT window/session can continue SIGMA work without requiring the user to restate the project history.

This policy does not change SIGMA cognition, admission gates, or the native-only execution standard. It is a coordination/provenance rule for repository state.

## Mandatory update cadence

For the Teacher-GPT SIGMA development lane:

```text
GITHUB_PROGRESS_UPDATE_REQUIRED=YES
UPDATE_AFTER_EACH_MEANINGFUL_COMPLETION=PREFERRED
MAX_COMPLETIONS_WITHOUT_GITHUB_STATUS_UPDATE=2
UPDATE_AFTER_ANY_MEANINGFUL_FAILURE=YES
UPDATE_BEFORE_CONTEXT_WINDOW_HANDOFF=YES
```

A "completion" means an admission PASS, a completed repair+rerun, a dependency-stage completion, or a source-ready handoff that materially changes the frontier.

A meaningful failure must also be recorded when it changes the diagnosis, candidate source/runner, or next action.

## Required contents of each living progress update

Every update must contain, when applicable:

```text
CURRENT_LEVEL=
CURRENT_STAGE=
CURRENT_CAPABILITY=
ADMISSION_STATUS=
LATEST_MACHINE_EVIDENCE=
LOCKED_SIGMAC_SHA256=
LOCKED_VM_SHA256=
NATIVE_SOURCE_SHA256=
BYTECODE_SHA256=KNOWN_OR_UNKNOWN
RUNNER_SHA256=KNOWN_OR_UNKNOWN
HOST_COGNITION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_BINDING=YES/NO
KNOWN_FAILURES_AND_REPAIRS=
RESULTS_OBTAINED=
CLAIM_BOUNDARIES=
NEXT_ACTION=
NEXT_DEPENDENCY_OR_CAPABILITY=
SAMPLE_MACHINE_EXECUTED_ARTIFACT=
```

Unknown fields must remain `UNKNOWN` / `NOT_PROVEN`; never infer missing bytecode, runner, ledger, or production identities.

## Living handoff file

For the current V4 -> V5 journey, maintain:

`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_V4_V5_JOURNEY_CURRENT.md`

This is a living coordination checkpoint. It should be updated after each meaningful milestone when practical, and never later than two completed milestones.

Immutable admission/failure checkpoints should still be created separately when appropriate. The living handoff is not a replacement for immutable evidence checkpoints.

## Machine-executed sample requirement

Maintain at least one repository sample that shows a capability that SIGMA actually executed under the locked VM in an admitted scope.

The sample must state whether it is:

- exact captured machine bytes; or
- a deterministic case definition from the admitted runner whose pass is established by the final machine summary.

Do not label reconstructed or illustrative data as exact machine output.

Current sample pointer:

`SIGMA_PROFESSOR/artifacts/SAMPLES/V4PK6_VERIFIED_EVOLUTION_MACHINE_PASS_SAMPLE_V1.txt`

## New-window continuation rule

A new Teacher-GPT window working on the V4/V5 journey should read, after the repository bootstrap/global directives/current handoff:

1. `SIGMA_PROFESSOR/DIRECTIVES/TEACHER_GPT_GITHUB_PROGRESS_HANDOFF_POLICY_V1.md`
2. `SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_V4_V5_JOURNEY_CURRENT.md`
3. the latest immutable checkpoint named by the living handoff
4. the current source/runner identities named by the living handoff

Then continue from `NEXT_ACTION` without asking the user to repeat prior milestones unless machine evidence required for the next gate is genuinely missing.

## Non-negotiable boundaries preserved

```text
ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO
CLAIM_SCOPE_MUST_MATCH_PROOF=YES
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN
PRODUCTION_V2_4_KEEP_RUNNING=YES
UPGRADE_V2_4_IN_PLACE=NO
```

This progress policy is documentation/coordination only. It must never be used as evidence that SIGMA possesses a cognitive capability.