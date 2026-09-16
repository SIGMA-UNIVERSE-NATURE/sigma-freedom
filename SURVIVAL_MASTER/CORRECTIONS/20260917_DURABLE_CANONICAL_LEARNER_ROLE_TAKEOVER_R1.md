# CORRECTION — DURABLE CANONICAL LEARNER ROLE / DEAD-OWNER TAKEOVER R1

Date: 2026-09-17
Branch: `AIL_SIGMA`
Status: REQUIRED DESIGN CORRECTION / OPPO COORDINATOR PATCH NOT YET APPLIED

## Machine evidence that triggered this correction

Current Oppo coordinator `session_learner_recover()` requires:

```text
session env for requested SESSION_CODE must still exist
learner lease must still exist
session_learner_owner == requested SESSION_CODE
current HEAD == lease AUTHORIZED_HEAD
current MODEL_GENERATION == lease EXPECTED_MODEL_GENERATION
native writer must be inactive
```

Therefore the current command is a SAME-SESSION recovery primitive. It is not a dead-owner takeover primitive.

If all windows/processes die and a later shell receives a new SESSION_CODE, the new session cannot recover the old canonical learner lease because recovery rejects unless the lease owner equals the requested code.

## Required architecture

```text
SESSION_CODE=EPHEMERAL
CANONICAL_LEARNER_ROLE=DURABLE
CANONICAL_LEARNER_OWNER=REPLACEABLE
ONE_WRITER=YES
NO_STATE_FORK=MANDATORY
```

No human should need to choose permanently which chat/window owns canonical write authority. No canonical learner identity may depend on one window staying alive forever.

## Required takeover behavior

When a session requests canonical learner authority:

```text
1. validate live SIGMA compiler/VM identity
2. read durable learner lease and current Oppo HEAD/model generation
3. if no learner lease exists -> normal atomic acquire
4. if lease owner is live -> reject with CANONICAL_LEARNER_ALREADY_ACTIVE
5. if lease owner is dead -> continue takeover gate
6. require native writer inactive
7. reconcile lease expected generation with current runtime generation
8. if an in-flight commit is ambiguous -> HOLD for receipt/journal reconciliation; never guess
9. atomically transfer the durable learner role to the new SESSION_CODE
10. increment a durable LEASE_EPOCH/FENCE_TOKEN
11. mark the new session CANONICAL_LEARNER
12. future BRAIN_WRITE / MODEL_WRITE / LEARN / COMMIT authorization must require current owner + current epoch
```

The first valid claimant after confirmed stale-owner death may win the lease atomically. Concurrent claimants must observe exactly one winner.

## Fencing requirement

A session code alone is not a sufficient long-lived fence for takeover races. The durable lease should contain at minimum:

```text
OWNER_SESSION_CODE=<current owner>
OWNER_RUN_ID=<current owner run>
LEASE_EPOCH=<monotonic integer>
AUTHORIZED_HEAD=<current authorized head>
EXPECTED_MODEL_GENERATION=<current authorized generation>
```

Every weight-affecting native intent/commit receipt after this correction should bind the current `LEASE_EPOCH` (or equivalent opaque fencing token). Once takeover increments the epoch, any stale process holding an older epoch is rejected even if it later resumes.

## Liveness rule

Do not decide owner death from prose, GitHub, or an old SESSION record alone.

Owner liveness must be established from current Oppo process/pane identity using the coordinator's exact liveness primitives. PID alone is insufficient across Android/Termux restarts because PID reuse is possible; bind process identity strongly enough to distinguish a restarted process (for example process start identity / tmux pane identity / coordinator-recorded incarnation as supported by the current runtime).

## Queue durability correction

Canonical queue progress must not live only inside the current learner session's artifact root.

Required:

```text
CANDIDATE_PACKETS=durable in teacher artifact workspaces
CANONICAL_QUEUE_PROGRESS=durable coordinator-owned mechanical state
PROCESSED_RECEIPTS=durable across learner-session replacement
CURRENT_CANONICAL_OWNER=replaceable session
```

A new canonical learner must be able to continue the same pending queue after all old windows die without copying the old SESSION_CODE into the new shell.

## Recovery after all windows die

Target sequence:

```text
all windows / Termux worker processes die
-> durable HEAD/model generation/queue/receipts remain on Oppo storage
-> Termux/runtime returns
-> a new ordinary session is created with a NEW SESSION_CODE
-> coordinator detects stale/dead canonical owner
-> coordinator atomically takes over durable learner role with a NEW LEASE_EPOCH
-> new owner rereads CURRENT Oppo HEAD + MODEL_GENERATION
-> reconcile any incomplete native commit by exact receipt/journal evidence
-> resume first unprocessed candidate
-> native SIGMA continues learning/commit under ONE_WRITER
```

No old session code is required as user input.

## Non-goals / forbidden shortcuts

```text
COPY_OLD_SESSION_CODE_INTO_NEW_SHELL=NO
MANUAL_DELETE_LEARNER_LEASE=NO
MANUAL_DELETE_WRITER_LOCK=NO
MANUAL_EDIT_BRAIN_HEAD=NO
MANUAL_EDIT_MODEL_GENERATION=NO
GITHUB_HEAD_AS_RUNTIME_RECOVERY_SOURCE=NO
MULTIPLE_CANONICAL_WRITERS=NO
HOST_SEMANTIC_MERGE=NO
```

## Current implementation status

```text
CURRENT_session_learner_recover=SAME_SESSION_RECOVERY_ONLY
DEAD_OWNER_NEW_SESSION_TAKEOVER=NOT_IMPLEMENTED_BY_SHOWN_FUNCTION
LEASE_EPOCH_FENCING=NOT_PROVEN
DURABLE_QUEUE_PROGRESS_INDEPENDENT_OF_LEARNER_SESSION=REQUIRED_TO_VERIFY
OPPO_COORDINATOR_PATCH=NOT_YET_APPLIED
```

## Next implementation step

Before patching Oppo, inspect the exact coordinator implementations for:

```text
session_learner_acquire
session_finish
session liveness / pane liveness helpers
native_writer_available
session_learner_owner / session_learner_owned_by
lease creation/removal helpers
```

Then implement a fail-closed `session-learner-takeover` (or equivalent acquire-with-stale-owner-recovery) using those exact primitives rather than guessing process liveness.
