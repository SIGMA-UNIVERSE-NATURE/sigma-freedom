# SIGMA R21B — Active Auto-Resume Fault

Date: 2026-09-29
Source: user-supplied Termux runtime output and uploaded r21b_active_learning_integration.sh.

## Pre-fault progress

R21B_ACTIVE_STORE_PATCH=PASS

R21B_COMPILE_DETERMINISTIC=PASS

ACTIVE_BYTECODE_SHA256=
60a71b4f4f748ce4ed8e8a644a85515305ae82448cec3a33cb451e9f1ea8725a

CRASH_ACTIVE_DUPLICATE_APPEND_BYTES=0

R21B_SIMULATED_ACTIVE_PROCESS_CRASH=YES

R21B_ACTIVE_FIRST_PROCESS_INTERRUPTED=PASS

## Fault

R21B_CONTROLLER_FAIL=
RESULT_R21_PACK_RECOVER_REFUSED_COMMAND

R21B_FAIL=
ACTIVE_AUTO_RESUME

## Fault location in controller contract

The uploaded integration controller enters recovery when controller state is RUNNING, FAULT_CAPTURED, or RECOVERING.

It transitions to RECOVERING and invokes:

R21_PACK_RECOVER

with expected result:

R21_RECOVER_READY

The observed runtime instead caused:

RESULT_R21_PACK_RECOVER_REFUSED_COMMAND

Therefore the recovery command was not accepted by the active integrated Sigma command dispatch in this run.

## Hard-invariant interpretation

This is a recoverable integration fault, not a learning-result rejection.

The following must remain true:

UNATTENDED_DEAD_END=FORBIDDEN
AUTO_RESUME_REQUIRED=YES
FAULT_EXIT_WITHOUT_RESUME_POINTER=FORBIDDEN
RETRAIN_FROM_ZERO_AFTER_RECOVERABLE_FAULT=FORBIDDEN

The failed R21B run must not be restarted from zero as a substitute for fixing the recovery command integration.

Required safe state:

STATE=BLOCKED_SAFE
CANONICAL_MUTATION=NO
REAL_DATA_DELETE=NO

LAST_GOOD_STATE=
the checkpoint committed immediately before the simulated crash

FAULT_COMMAND=
R21_PACK_RECOVER

FAULT_REASON=
RESULT_R21_PACK_RECOVER_REFUSED_COMMAND

RESUME_TARGET=
repair/verify active command dispatch for R21_PACK_RECOVER, then resume from the last committed R21B learning checkpoint rather than restarting the learning sequence.

## Canonical safety boundary

CANONICAL_MUTATION=NO
REAL_DATA_DELETE=NO

No R21B admission or active runtime replacement occurred.

R21B_ACTIVE_LEARNING_INTEGRATION=NOT_PASS

R21B_ACTIVE_AUTO_RESUME=FAULT

CURRENT_CANONICAL_RUNTIME_REPLACED=NO

## Next

NEXT=
R21B_FIX_RECOVER_COMMAND_DISPATCH_AND_RESUME_FROM_LAST_GOOD_CHECKPOINT

The subsequent repair must demonstrate:
- R21_PACK_RECOVER is accepted by the integrated active command dispatcher;
- uncommitted pack/commit tail is recovered fail-closed;
- controller resumes from LAST_GOOD_STEP;
- no reteach/retrain-from-zero;
- interrupted and uninterrupted final TACC are identical;
- pack and commit are byte-identical to the uninterrupted reference;
- independent verifier passes;
- canonical state remains unchanged during prototype integration.
