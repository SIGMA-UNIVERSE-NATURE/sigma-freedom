# SIGMA R21I — Real Reboot Test Prepared

Date: 2026-09-29
Source: user-supplied Termux runtime output and uploaded r21i_prepare_real_reboot_test.sh.

## Reference run

R21I_REFERENCE_RUN=PASS

REFERENCE_FINAL_TACC=
59f4ace23e695f0b38ca26902569f041

## Pre-reboot persisted resume pointer

R21I_PRE_REBOOT_RESUME_POINTER=PASS

SESSION_ID=
R21I_REAL_REBOOT_20260929T172514

PRE_REBOOT_BOOT_ID=
d4785274-ba7f-4340-ad20-d9df0da85eed

PRE_REBOOT_CONTROLLER_STATE=
RUNNING

PRE_REBOOT_LAST_GOOD_STEP=2

PRE_REBOOT_NEXT_STEP=3

## Boot hook

BOOT_HOOK_SHA256=
be319f5b84e0aa18c3d51f6f5f360930d7de12914d882136e433a4cf052af92c

The prepared boot hook records the current boot ID into a persistent marker and launches the admitted watchdog launcher via nohup.

## Production hot store before reboot

PRODUCTION_PACK_BYTES=154719

PRODUCTION_COMMIT_BYTES=84

## Final preparation status

R21I_REAL_REBOOT_TEST_PREPARED=PASS

READY_FOR_REAL_DEVICE_REBOOT=YES

AFTER_REBOOT_DO_NOT_MANUALLY_LAUNCH_WATCHDOG=YES

## Pending receipt contract

The preparation script writes a pending receipt carrying:
- session ID;
- workset and workset hash;
- production workdir;
- canonical head/model/runtime hash;
- pre-reboot boot ID;
- boot marker/log paths;
- boot hook path and SHA256;
- uninterrupted reference TACC;
- reference pack/commit hashes and sizes;
- pre-reboot controller state RUNNING;
- last good step 2;
- next step 3;
- REAL_REBOOT_REQUIRED=YES;
- MANUAL_LAUNCH_AFTER_REBOOT=FORBIDDEN_UNTIL_VERIFY.

## Interpretation boundary

This checkpoint proves preparation only.

The supplied evidence establishes:
- an uninterrupted reference result exists;
- the production controller was intentionally interrupted after native step 3 but before controller checkpoint;
- the persisted controller state is RUNNING with LAST_GOOD_STEP=2 and NEXT_STEP=3;
- a real reboot boot hook is installed and sealed by SHA256;
- persistent evidence files for boot dispatch/logging are prepared;
- the production pack/commit contain the pre-reboot partial session state;
- the system is ready for an actual device reboot.

It does NOT yet prove:
BOOT_TRIGGER_VERIFIED=PASS
REAL_REBOOT_AUTOSTART=PASS
POST_REBOOT_AUTO_RESUME=PASS

Those claims require evidence from a new Android/Linux boot ID after an actual device reboot, with no manual watchdog launch before verification.

NEXT=
PHYSICALLY_REBOOT_DEVICE_THEN_VERIFY_R21I_PENDING_RECEIPT_AND_BOOT_DISPATCH
