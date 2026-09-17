# CORRECTION — EPHEMERAL SESSION / DURABLE CANONICAL LEARNER ROLE R1

Date: 2026-09-17
Status: REQUIRED DESIGN CORRECTION; OPPO COORDINATOR PATCH NOT YET INSTALLED

## Machine evidence

The live Oppo Session R4 coordinator shows:

- `session_learner_acquire` rejects whenever `SESSION_LEARNER_LEASE` already exists.
- `session_learner_recover` requires the lease owner `SESSION_CODE` to equal the requesting code.
- `session_finish` removes the learner lease only on a clean finish by the current owner.
- session identity is created randomly by `session_new_code` and is therefore ephemeral.
- `native_writer_available` uses an OS `flock` probe and is suitable as one required mechanical guard before stale-owner takeover.

Therefore a whole-Termux/Android kill can leave a durable learner lease owned by a session code that can never exist again. The current same-code `session-learner-recover` is insufficient for whole-process-group resurrection.

## Correct architecture

```text
SESSION_CODE=EPHEMERAL
CANONICAL_LEARNER_ROLE=DURABLE
CURRENT_OWNER_SESSION=REPLACEABLE
ONE_WRITER=YES
LEASE_EPOCH=MONOTONIC
OLD_OWNER_WRITE_AFTER_TAKEOVER=REJECT
```

A chat/teacher window is not manually selected as the permanent writer. A dedicated canonical queue service obtains the role. If it dies, a later fresh service session may take over only after the old owner is mechanically proven dead and the current Oppo canonical state is reconciled.

## Safe takeover gates

A new session may take over a stale learner lease only when all are true:

```text
REQUESTER_SESSION_STATE=GRANTED
REQUESTER_SESSION_MODE=STANDARD
REQUESTER_OPEN_HEAD=CURRENT_OPPO_HEAD
REQUESTER_OPEN_MODEL_GENERATION=CURRENT_OPPO_MODEL_GENERATION
PREVIOUS_OWNER_LIVENESS=PROVEN_DEAD
NATIVE_WRITER_LOCK=AVAILABLE
CURRENT_OPPO_HEAD=LEASE_AUTHORIZED_HEAD
CURRENT_OPPO_MODEL_GENERATION=LEASE_EXPECTED_MODEL_GENERATION
TAKEOVER_SERIALIZATION_LOCK=HELD
```

If owner liveness is unknown, takeover must fail closed.

If model generation or head differs from the lease expectation, takeover must not guess. This may indicate a commit completed before the old process died but the learner lease was not advanced. Exact native receipt reconciliation is required before resuming.

## Fencing

Every durable learner lease must carry a monotonic `LEASE_EPOCH`. On takeover:

```text
NEW_EPOCH=OLD_EPOCH+1
PREVIOUS_SESSION_CODE=<old owner>
SESSION_CODE=<new owner>
```

The previous session record is marked fenced/revoked. Existing coordinator ownership checks by `SESSION_CODE` already provide an additional fence because a former owner no longer passes `session_learner_owned_by` after lease transfer. A writer-active check remains mandatory before takeover.

## Queue durability correction

Canonical queue progress must not be stored under the current learner session's `ARTIFACT_ROOT`, because that makes processed/attempt state depend on an ephemeral learner session.

Required durable mechanical queue state:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/DURABLE/MULTI_TEACHER_CANONICAL_QUEUE_R2/
  attempts/
  processed/
  rejected/
  drain.lock
```

Teacher candidate packets may remain in their persistent Session R4 workspaces only while workspace retention is guaranteed until terminal processing. They must be content-addressed and self-contained.

## Whole-Termux resurrection

```text
all windows/processes killed
-> model/head/queue/receipts remain on Oppo storage
-> no computation occurs while Termux is dead
-> next Termux bootstrap starts canonical queue service
-> service opens a NEW ephemeral session code
-> acquire if no learner lease exists
-> otherwise stale-owner takeover if all gates pass
-> resume durable queue from processed receipts/checkpoints
```

No recovery procedure depends on remembering the old session code.

## Authority

```text
RUNTIME_AUTHORITY=OPPO_CURRENT_RUNTIME
GITHUB_HEAD_IS_RUNTIME_AUTHORITY=NO
GIT_PULL_REQUIRED_FOR_RUNTIME=NO
HOST_COGNITION=NO
HOST_LEARNING=NO
SIGMA_NATIVE_VM_IS_LEARNING_ENGINE=YES
```
