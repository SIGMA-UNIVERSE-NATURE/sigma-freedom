# SIGMA R21B FIX1 — Recovery Dispatch Repair + Active Integration PASS

Date: 2026-09-29
Source: user-supplied Termux runtime output and uploaded r21b_active_learning_integration_fix1.sh.

## Fault repair

Prior observed fault:
RESULT_R21_PACK_RECOVER_REFUSED_COMMAND

FIX1 root cause:
R21A command handlers were copied into the active Sigma source, but MAIN command dispatch entries for the R21 control-plane commands were missing.

FIX1 adds MAIN dispatch for:
- R21_PACK_STORE
- R21_PACK_RESTORE
- R21_PACK_RECOVER
- R21_PACK_STATUS

R21B_ACTIVE_STORE_PATCH=PASS
R21B_RECOVERY_DISPATCH_PATCH=PASS

## Deterministic build

R21B_COMPILE_DETERMINISTIC=PASS

ACTIVE_BYTECODE_SHA256=
672c15d6e2c7da9342f50938e5f38542f3307490550f80a8b9233b4f11ea0e69

## Recovery dispatch preflight

R21B_RECOVERY_DISPATCH_PREFLIGHT=PASS

The integration script verifies R21_PACK_RECOVER returns R21_RECOVER_READY before starting learning/crash injection.

## Active learning / crash / resume

REAL_SIGMA_COMMANDS=
R57_BEGIN_R57_STEP

ACTIVE_INTEGRATION_ROWS=12

CRASH_ACTIVE_DUPLICATE_APPEND_BYTES=0

R21B_SIMULATED_ACTIVE_PROCESS_CRASH=YES
R21B_ACTIVE_FIRST_PROCESS_INTERRUPTED=PASS

Crash recovery:
CRASH_AUTO_RECOVER=
RECOVER||COUNT||11||PACK_END||257753

CRASH_ACTIVE_FINAL_TACC=
59f4ace23e695f0b38ca26902569f041

CRASH_ACTIVE_STEPS=12

R21B_ACTIVE_AUTO_RESUME=PASS

## Uninterrupted reference

REFERENCE_ACTIVE_DUPLICATE_APPEND_BYTES=0

REFERENCE_ACTIVE_FINAL_TACC=
59f4ace23e695f0b38ca26902569f041

REFERENCE_ACTIVE_STEPS=12

## Determinism after recovery

R21B_ACTIVE_FINAL_TACC_DETERMINISTIC=PASS
R21B_ACTIVE_PACK_BYTE_IDENTICAL=PASS
R21B_ACTIVE_COMMIT_BYTE_IDENTICAL=PASS

## Independent verifier

R21B_INDEPENDENT_VERIFIER_PATCH=PASS

Independent verifier result:
VERIFY||RECORDS||25||PACK_BYTES||618375||COMMIT_BYTES||300||EXPECTED_FOUND||1||WHOLE_PACK_READ||NO

R21B_INDEPENDENT_VERIFIER=PASS

WHOLE_PACK_READ=NO

## Final active integration status

R21B_ACTIVE_LEARNING_INTEGRATION=PASS

FINAL_TACC=
59f4ace23e695f0b38ca26902569f041

HOT_STORE_FILES=4

ACTIVE_STATE_OBJECT_FILES=0
ACTIVE_PER_OBJECT_WRITE_RECEIPTS=0
ACTIVE_PRIVATE_SNAPSHOT_COUNT=1

NEW_INODES_PER_OBJECT=0
ACTIVE_DUPLICATE_APPEND_BYTES=0

AUTO_RESUME=PASS
RETEACH=NO

INDEPENDENT_NATIVE_VERIFIER=PASS

CANONICAL_MUTATION=NO
CURRENT_CANONICAL_RUNTIME_REPLACED=NO

NEXT=
R21C_SCALE_STRESS_AND_ADMISSION_CANDIDATE

## Hard-invariant closure for the observed fault

For the previously observed active-auto-resume failure:

FAULT_FIXED=YES
FAULT_CAUSE=MISSING_R21_MAIN_DISPATCH
RECOVERY_COMMAND_PREFLIGHT=PASS
AUTO_RESUME_AFTER_FIX=PASS
RETRAIN_FROM_ZERO=NO
UNATTENDED_DEAD_END=AVOIDED

The crash path resumes from the persisted controller checkpoint and produces the same final TACC, private.pack, and private.commit as the uninterrupted reference path.

## Interpretation boundary

This checkpoint closes the specific R21B recovery-dispatch fault and establishes prototype active-learning integration behavior over the supplied 12-row integration run.

It does not claim canonical runtime replacement or production admission:
CURRENT_CANONICAL_RUNTIME_REPLACED=NO
CANONICAL_MUTATION=NO

The next required stage remains scale/stress testing and admission-candidate evaluation.
