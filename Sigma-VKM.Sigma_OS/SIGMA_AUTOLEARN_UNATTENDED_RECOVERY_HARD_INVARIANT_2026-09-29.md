# SIGMA AutoLearn — Unattended Recovery Hard Invariant

Date: 2026-09-29
Authority: user-specified governing principle for future AutoLearn controller behavior.

## Hard invariants

UNATTENDED_DEAD_END=FORBIDDEN
AUTO_RESUME_REQUIRED=YES
FAULT_EXIT_WITHOUT_RESUME_POINTER=FORBIDDEN
RETRAIN_FROM_ZERO_AFTER_RECOVERABLE_FAULT=FORBIDDEN

These are hard controller invariants, not advisory notes.

## Required controller behavior

The AutoLearn controller must always provide the following behavior.

### 1. Checkpoint before every mutating step

Persist at minimum:

PRIVATE_HEAD
ACCUMULATOR_OR_PROPOSAL_HASH
COMMAND
INPUT_HASH
STEP_INDEX

A mutating step must not begin without a recoverable checkpoint boundary.

### 2. Faults must not terminate learning with an unrecoverable exit

A raw `exit 1` must not represent the terminal learning state.

On RC/fault, the controller must:

1. capture the fault;
2. write a fault receipt;
3. transition to RECOVERING;
4. attempt bounded, idempotent recovery from the last validated checkpoint;
5. if recovery is unsafe or impossible, transition to BLOCKED_SAFE with a valid resume pointer.

### 3. Generation counters are distinct

The controller must distinguish:

STATE_GENERATION
INTERNAL_MODEL_GENERATION
G3_SEMANTIC_GENERATION

Invariant:

GENERATION_COUNTER_EQUIVALENCE_HARDCODED=FORBIDDEN

The controller must never assume these counters are equal or interchangeable.

### 4. Resume from the last good checkpoint

Recoverable faults must resume from the last validated committed checkpoint, not retrain from zero.

Example:

If step 73/160 faults, recovery resumes from checkpoint 72/160 and continues with step 73.

RETRAIN_FROM_ZERO_AFTER_RECOVERABLE_FAULT=FORBIDDEN

### 5. Fail closed without becoming a dead end

If a semantic or integrity fault cannot be safely auto-recovered, the controller must enter:

STATE=BLOCKED_SAFE
CANONICAL_MUTATION=NO
REAL_DATA_DELETE=NO
RESUME_POINTER=<required>
FAULT_RECEIPT=<required>

BLOCKED_SAFE is a recoverable/safe halted state with explicit continuation metadata, not an abandoned execution path.

### 6. Recovery must be idempotent

Repeated controller invocation must:

- identify completed PASS steps;
- identify the last validated checkpoint;
- avoid replaying already committed mutating steps;
- avoid creating unbounded duplicate experiments or state copies;
- continue from the authorized resume point.

IDEMPOTENT_RECOVERY_REQUIRED=YES

## Required state machine

Normal path:

READY
→ RUNNING
→ CHECKPOINTED
→ RUNNING
→ CHECKPOINTED
→ ...

Fault path:

RUNNING
→ FAULT_CAPTURED
→ RECOVERING
→ CHECKPOINT_VALIDATED
→ RUNNING

Unrecoverable-safe path:

FAULT_CAPTURED
→ RECOVERING
→ BLOCKED_SAFE

No path may terminate without either:
- a completed terminal artifact/receipt for the intended operation, or
- an explicit BLOCKED_SAFE state carrying a valid recovery pointer.

## Minimum fault receipt schema

Every captured fault must record at minimum:

FAULT_COMMAND
FAULT_RC
FAULT_REASON
LAST_GOOD_PRIVATE_HEAD
LAST_GOOD_STEP
MODEL
STATE_GENERATION
INTERNAL_MODEL_GENERATION
G3_SEMANTIC_GENERATION
INPUT_SHA256
CANONICAL_HEAD
CANONICAL_MUTATION=NO
RESUME_COMMAND

Recommended additional fields:

FAULT_TIMESTAMP
FAULT_PHASE
CHECKPOINT_SHA256
ACCUMULATOR_OR_PROPOSAL_HASH
PRIVATE_STATE_PATH
EXPECTED_NEXT_STEP
RECOVERY_ATTEMPT_COUNT
RECOVERY_STATUS

## Human-independence invariant

Sigma AutoLearn must not depend on a human operator being present to push execution back into the learning loop after a recoverable fault.

The controller must know:

- current phase;
- current step;
- what has committed;
- what has not committed;
- last valid private head;
- last valid proposal/accumulator state;
- authorized continuation point;
- safe recovery action.

HUMAN_REQUIRED_FOR_RECOVERABLE_RESUME=NO

## Canonical safety invariant

During fault capture and recovery:

CANONICAL_MUTATION=NO

unless and until a separately authorized canonical admission/commit step has passed its own gate.

REAL_DATA_DELETE=NO

unless a separately authorized destructive-storage/GC contract explicitly permits it.

## Planned R21 packed-learning-store integration

After R20 consolidation, future R21 packed learning storage should integrate the recovery contract with the storage layer.

Required sequence:

CHECKPOINT_COMMIT
→ FSYNC
→ CRASH_OR_FAULT
→ TRUNCATE_UNCOMMITTED_TAIL
→ RESTORE_LAST_COMMITTED_LEARNING_STATE
→ VALIDATE_CHECKPOINT
→ RESUME

Goals:

- avoid unbounded inode growth;
- preserve learning continuity across crashes;
- recover from the last committed learning state;
- prevent retraining from zero after recoverable failure;
- prevent the system from losing its place in the learning loop.

R21_IMPLEMENTED=NO
R21_STATUS=FUTURE_CONTRACT

## Interpretation boundary

This document defines mandatory future AutoLearn controller invariants.

It does not claim that the full unattended recovery controller or R21 packed-learning-store integration is already implemented.

Existing evidence such as R15 crash-tail recovery, R18 storage sidecar/idempotence, R19 recovery rehearsal, and R20 codec ownership may provide supporting primitives, but this contract requires the controller-level state machine and fault/resume semantics above to be explicitly implemented and verified before claiming:

AUTO_RESUME_REQUIRED=SATISFIED
UNATTENDED_RECOVERY=PASS
