# SURVIVAL MASTER CHECKPOINT — MULTI-TEACHER CANONICAL QUEUE R1 SOURCE READY

Date: 2026-09-17 (Asia/Ho_Chi_Minh)
Branch: `AIL_SIGMA`

## User requirement

Multiple teaching windows must be able to contribute learning to SIGMA's canonical weights without allowing simultaneous canonical writers to race or overwrite one another.

## Architecture frozen

```text
MULTI_TEACHER_WINDOWS=YES
MULTI_CANDIDATE_LEARNING=YES
CANONICAL_WEIGHT_UPGRADE=YES
ONE_CANONICAL_WRITER_AT_A_TIME=YES
TWO_CANONICAL_WRITERS=NO
NO_STATE_FORK=MANDATORY
```

Teacher windows remain artifact-only and seal content-addressed candidate packets in their own workspaces. One canonical learner session drains candidates sequentially. Each candidate must provide an exact lane-specific replay entrypoint that re-runs/re-evaluates native SIGMA learning against the CURRENT canonical head/model generation before any commit.

The host queue never merges weight deltas, never accepts/rejects learning semantically, and never edits canonical head/model generation/writer locks directly.

## Source tree

```text
SURVIVAL_MASTER/CANDIDATES/MULTI_TEACHER_CANONICAL_QUEUE_R1/
  CONTRACT.md
  PACKET_FORMAT.md
  README_RUN.md
  teacher/seal_candidate.sh
  canonical/drain_once.sh
  canonical/daemon.sh
  samples/CANDIDATE_DESCRIPTOR.template
```

## Critical behavior

```text
TEACHER_SESSION_MODE=STANDARD
TEACHER_CANONICAL_MUTATION=NO
TEACHER_CAN_PRODUCE_NATIVE_WEIGHT_CANDIDATE=YES
CANONICAL_DRAINER_SESSION_MODE=CANONICAL_LEARNER
CANONICAL_DRAINER_ONE_WRITER=YES
STALE_PARENT_BLIND_APPLY=NO
CURRENT_MODEL_NATIVE_REPLAY_REQUIRED=YES
HOST_WEIGHT_MERGE=NO
HOST_ACCEPT_REJECT=NO
SIGMA_NATIVE_LEARNING_OWNER=YES
```

## Replay result contract

```text
QUEUE_RESULT=ACCEPTED|REJECTED|HOLD
```

`ACCEPTED` requires a model-generation advance and exact native commit receipt. `REJECTED` requires no canonical mutation. `HOLD` remains pending and stops the daemon instead of host-side skipping/re-ranking.

## Current runtime state relevant to deployment

The latest human-provided machine evidence established one valid canonical learner session:

```text
SESSION_CODE=SBE0DAD2082DF
SESSION_MODE=CANONICAL_LEARNER
ONE_WRITER=YES
BRAIN_WRITE=ALLOW
BRAIN_WRITE_OWNER=SIGMA_NATIVE_VM_ONLY
BRAIN_WRITE_NATIVE_RECEIPT_REQUIRED=YES
STATE_WRITE=ALLOW
MODEL_WRITE=ALLOW
LEARN=ALLOW
COMMIT=ALLOW
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=ALLOW
AUTHORIZED_HEAD=700d5c1b4845322d7c14800029c629b0
AUTHORIZED_MODEL_GENERATION=1
```

The previous learner `SCA7A3C3A6323` was explicitly finished with:

```text
SESSION_FINISH=PASS
CANONICAL_MODEL_MUTATION_OBSERVED=NO
```

Runtime state must be rechecked before deployment; GitHub does not prove present liveness.

## Claim ceiling

```text
QUEUE_MECHANICS_SOURCE_READY=YES
OPPO_PREFLIGHT=NOT_RUN
OPPO_INSTALL=NOT_RUN
CONTINUOUS_DAEMON=NOT_RUN
MULTI_TEACHER_END_TO_END_WEIGHT_ACCUMULATION=NOT_PROVEN_UNTIL_DEVICE_TEST
GENERAL_WEIGHT_DELTA_MERGE=NOT_IMPLEMENTED
MULTI_WRITER_CANONICAL_COMMIT=FORBIDDEN
```

## Next action

Stage the exact source tree on Oppo, run shell syntax/static checks, verify current canonical learner status, then test with one synthetic/no-mutation `REJECTED` packet before testing one real native learning packet. Do not enable a long-running daemon until that preflight passes.
