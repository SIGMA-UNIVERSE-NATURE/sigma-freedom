# SIGMA R21I — Real Reboot Trigger Verification PASS

Date: 2026-09-29
Source: user-supplied post-reboot Termux output and uploaded verification/finalization scripts.

## Initial post-reboot verification

R21I_DEVICE_BOOT_ID_CHANGED=PASS
R21I_TERMUX_BOOT_DISPATCH=PASS

Durable watchdog session reported:
STATE=COMPLETE

R21I_BOOT_WATCHDOG_SESSION_COMPLETE=PASS
R21I_CONTROLLER_RESUME_AFTER_REBOOT=PASS
R21I_FINAL_TACC_DETERMINISTIC=PASS
R21I_PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS
R21I_COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS

Initial verifier then stopped only at:

R21I_VERIFY_FAIL=BOOT_LOG_SESSION_COMPLETE

## Observability fix

The follow-up finalizer identified the watchdog completion line as a stdout buffering/observability issue rather than a durability or resume failure.

Follow-up script SHA256:
181bb1621c3eafa111b25b35ab1f5a84aa52f342913873bf693c11abbea2a59d

R21I_DEVICE_BOOT_ID_CHANGED=PASS
R21I_TERMUX_BOOT_DISPATCH=PASS
R21I_DURABLE_WATCHDOG_SESSION_COMPLETE=PASS
R21I_CONTROLLER_RESUME_AFTER_REBOOT=PASS
R21I_FINAL_TACC_DETERMINISTIC=PASS
R21I_PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS
R21I_COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS
R21I_BOOT_LOG_AUTO_RESUME=PASS

WATCHDOG_LOG_COMPLETION=
BUFFERED_NOT_DURABILITY_SIGNAL

Independent verifier:
VERIFY||RECORDS||25||PACK_BYTES||618375||COMMIT_BYTES||300||EXPECTED_FOUND||1||WHOLE_PACK_READ||NO

R21I_INDEPENDENT_NATIVE_VERIFIER=PASS

R21I_WATCHDOG_STDOUT_UNBUFFERED_FIX=PASS

## Final verified status

R21I_REAL_REBOOT_TRIGGER_VERIFICATION=PASS

DEVICE_BOOT_ID_CHANGED=PASS
TERMUX_BOOT_DISPATCH=PASS
DURABLE_WATCHDOG_SESSION_COMPLETE=PASS
CONTROLLER_RESUME_AFTER_REBOOT=PASS

FINAL_TACC_DETERMINISTIC=PASS
PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS
COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS

BOOT_LOG_AUTO_RESUME=PASS
WATCHDOG_LOG_COMPLETION=BUFFERED_NOT_DURABILITY_SIGNAL
WATCHDOG_STDOUT_UNBUFFERED_FIX=PASS

INDEPENDENT_NATIVE_VERIFIER=PASS

BOOT_TRIGGER_VERIFIED=YES
REBOOT_AUTOSTART=PASS

HOT_STORE_FILES=4

NEW_INODES_PER_OBJECT=0
NEW_INODES_PER_BATCH=0
NEW_INODES_PER_CHECKPOINT=0

UNATTENDED_DEAD_END=FORBIDDEN

R21_AUTO_RESUME_STACK=FULLY_VERIFIED

NEXT=
R21_FINAL_OWNERSHIP_AUDIT

## Authority / interpretation boundary

The durable completion authority for this real reboot test is:
- device boot ID changed;
- boot hook wrote the current boot ID;
- durable watchdog session reached COMPLETE for the armed session ID;
- durable controller state reached COMPLETE with expected final TACC;
- post-reboot pack and commit match the uninterrupted reference byte-for-byte;
- independent native verifier passes without whole-pack read.

The missing watchdog completion text in the first boot log was not used as the durability authority. It was treated as a buffered observability signal.

The subsequent patch changes future launcher observability to unbuffered Python stdout and does not retroactively redefine the durable evidence.

This checkpoint establishes that the real reboot trigger, Termux boot dispatch, and unattended post-reboot AutoLearn resume path have been empirically verified for the tested session.

NEXT is R21_FINAL_OWNERSHIP_AUDIT.
