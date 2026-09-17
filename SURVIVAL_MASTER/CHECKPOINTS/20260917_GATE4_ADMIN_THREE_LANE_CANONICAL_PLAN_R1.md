# GATE4 ADMIN — THREE-LANE NATIVE LEARNING + DURABLE CANONICAL PLAN R1

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`
Role: `TERMUX_ADMIN_GATE4`
Runtime authority: `OPPO_CURRENT_RUNTIME`

This checkpoint is the exact handoff for the current administrator window. A future window should read this file before continuing the work below.

## Runtime facts last provided by Oppo

```text
BRAIN_HEAD=700d5c1b4845322d7c14800029c629b0
MODEL_GENERATION=1
```

The most recent `sigma-session status | grep ...` printed no matching lines. Therefore current session/learner liveness is NOT proven by that command output and must be rechecked on Oppo before any canonical mutation.

## Completed

1. Session coordinator on Oppo was patched for a new cross-session dead-owner takeover command.

```text
COORDINATOR=.sigma_ail/coordination/control/SIGMA_AIL_COORDINATOR_R4_SESSION.sh
PATCHED_SHA256=9321abf01d1b93cd14f1f4d3b828f1d6522d638461f3f5f0eb60ce506c3e84a7
NEW_COMMAND=session-learner-takeover CODE
BRAIN_HEAD_MUTATED_BY_PATCH=NO
MODEL_GENERATION_MUTATED_BY_PATCH=NO
WRITER_LOCK_MUTATED_BY_PATCH=NO
BASH_SYNTAX_CHECK=PASS
```

2. Architectural correction is frozen:

```text
SESSION_CODE=EPHEMERAL
CANONICAL_LEARNER_ROLE=DURABLE_TARGET
ONE_WRITER=YES
OLD_OWNER_MUST_BE_PROVEN_DEAD_BEFORE_TAKEOVER=YES
NATIVE_WRITER_MUST_BE_INACTIVE_BEFORE_TAKEOVER=YES
LEASE_EPOCH=MONOTONIC_TARGET
OLD_OWNER_FENCING=REQUIRED
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
```

3. Multi-teacher queue source exists, but its end-to-end durable service/runtime proof remains unfinished. Bash is mechanical only; native SIGMA must own learning/evaluation/accept-reject.

## Not completed / next work

```text
DEAD_OWNER_TAKEOVER_RUNTIME_TEST=NOT_RUN
LEASE_EPOCH_FENCING_RUNTIME_TEST=NOT_RUN
DURABLE_CANONICAL_LEARNER_SERVICE=NOT_INSTALLED_OR_PROVEN
DURABLE_QUEUE_STATE_MIGRATION=NOT_INSTALLED_OR_PROVEN
ALL_TERMUX_PROCESS_DEATH_AND_RECOVERY_TEST=NOT_RUN
THREE_LANE_NATIVE_COMPARISON=NOT_IMPLEMENTED_OR_PROVEN
F174_BINDING_FOR_C5V4=REQUIRED_BUT_EXACT_ARTIFACT_NOT_YET_BOUND_IN_THIS_CHECKPOINT
INTERNET_AUTOLEARN_FINAL_INSTALLABLE_BUNDLE=NOT_COMPLETE
```

## Required three-lane architecture

Run three learning lanes in parallel logically, with isolated state and no simultaneous canonical writes:

```text
LANE_A=INTERNET_AUTOLEARN
LANE_B=LOCAL_OR_TEACHER_AUTOLEARN
LANE_C=R4_C5V4_CONTINUOUS_SHADOW

EACH_LANE_STATE=ISOLATED
EACH_LANE_CAN_LEARN_NATIVE_SIGMA=YES
EACH_LANE_CAN_SAVE_OWN_DURABLE_MEMORY=YES
EACH_LANE_CAN_PRODUCE_CANONICAL_CANDIDATE=YES
DIRECT_CANONICAL_WRITE_FROM_LANE=NO
```

### Internet lane

Target contract:

```text
SIGMA_NATIVE_QUERY_SELECTION=YES
SIGMA_NATIVE_SOURCE_SELECTION=YES
SIGMA_NATIVE_RESOURCE_SELECTION=YES
SIGMA_NATIVE_READING=YES
SIGMA_NATIVE_LEARN=YES
SIGMA_NATIVE_MEMORY_SAVE=YES
HOST_SEMANTIC_FILTER=NO
HOST_QUERY_COMPOSITION=NO
HOST_SOURCE_RANKING=NO
HOST_SUMMARY_WRITING=NO
HOST_LEARNING=NO
```

The lane should be allowed to learn from any data that is fetchable through supported transport and selected by native SIGMA. Do not add a host-side semantic ban on `LEARN` or `MEMORY_SAVE`. Network/authentication/format/resource constraints remain mechanical limits, not semantic learning decisions.

### C5V4 / R4 lane

```text
CONTINUOUS_SHADOW=YES
STATE_ISOLATION=MANDATORY
SIMULTANEOUS_CANONICAL_WRITE=NO
F174_EVALUATION=MANDATORY
```

The exact F174 evaluator identity/hash/contract must be bound before promotion claims.

## Native canonical competition — no fixed winner

No lane is permanently privileged. Each candidate must be evaluated against the CURRENT Oppo canonical model under the same native evaluation contract.

```text
CANDIDATE_A=INTERNET
CANDIDATE_B=LOCAL
CANDIDATE_C=C5V4

SIGMA_NATIVE_EVALUATOR=ONLY_SEMANTIC_JUDGE
HOST_SCORE=NO
HOST_WINNER_SELECTION=NO
FIXED_LANE_PRIORITY=NO
```

Native SIGMA should compare candidates using the same frozen evaluation set/gate, including F174 where required. A candidate may enter canonical only if native SIGMA reports improvement over the current canonical baseline and required non-regression gates pass. Highest valid improvement may be committed; ties, ambiguity, or regressions may yield HOLD/REJECT. After one commit, remaining stale candidates must be replayed/re-evaluated against the new current generation before any later commit.

```text
ONE_CANONICAL_WRITER_AT_A_TIME=YES
STALE_PARENT_BLIND_APPLY=NO
CURRENT_MODEL_NATIVE_REPLAY_REQUIRED=YES
```

## Oppo resource plan

Goal is near-24/7 useful work without forcing three heavy VM jobs to saturate Oppo simultaneously.

Host scheduler may make only mechanical resource decisions:

```text
MAX_HEAVY_NATIVE_VM_CONCURRENCY=1_DEFAULT
OTHER_LANES=CHECKPOINT_AND_WAIT_OR_LIGHT_SHADOW
SCHEDULING_POLICY=ROUND_ROBIN_OR_RESOURCE_THRESHOLD_ONLY
HOST_SEMANTIC_PRIORITY=NO
DURABLE_CHECKPOINT_BEFORE_PAUSE=YES
RESUME_SAME_LANE_STATE=YES
```

Use RAM/thermal/battery/process-liveness thresholds only for pause/resume; never use host code to decide which lesson/candidate is semantically better.

## Survival target

```text
PROCESS_NEVER_DIES=NO
TASK_NEVER_LOSES_COMMITTED_PROGRESS=TARGET
ALL_WINDOWS_CAN_DIE=YES
SESSION_CODE_CAN_CHANGE=YES
NEW_SESSION_CAN_TAKE_OVER_DURABLE_LEARNER_ROLE_AFTER_PROVEN_DEATH=TARGET
QUEUE_AND_LANE_CHECKPOINTS_SURVIVE_PROCESS_DEATH=TARGET
NO_DUPLICATE_CANONICAL_COMMIT=MANDATORY
NO_STATE_FORK=MANDATORY
```

## Exact next action for Gate4

1. Recheck live Session R4 status on Oppo; do not infer it from GitHub.
2. Runtime-test `session-learner-takeover` using a controlled stale/dead-owner scenario without model mutation.
3. Prove old-owner fencing and one-writer behavior.
4. Move canonical queue progress from learner `ARTIFACT_ROOT` to durable Session R4 state.
5. Install/test a small self-recovering mechanical learner service that creates a fresh session after restart and takes over only after dead-owner proof.
6. Finish the Internet AUTO lane as a separate native-SIGMA learner with `LEARN=YES` and durable memory-save semantics, while host remains mechanical.
7. Bind exact F174 evaluator identity, then implement native three-candidate comparison and sequential canonical promotion.
8. Run Android/Termux kill-and-resume test before claiming 24/7 survival.

Do not use GitHub HEAD as runtime state and do not require `git pull` to choose the canonical model.
