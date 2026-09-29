# SIGMA R21G — Autonomous Controller Admission PASS

Date: 2026-09-29
Source: user-supplied Termux runtime output and uploaded r21g_autonomous_controller_admission_fix1.sh.

## Controller build / source checks

R21G_CONTROLLER_PY_COMPILE=PASS
R21G_STATE_API_KEYWORD_COLLISION_FIX=PASS
R21G_CONTROLLER_SOURCE_READY=PASS

AUTOCONTROLLER_SHA256=
b13dfc12e80f6525c2cdb44415b05c20fa792183158b9abbbff116021a5ff4e5

SUPERVISOR_SHA256=
1b6912a34fbf16b4f41e26c427e31827a1550f861017b830edffd41b16c6c358

## Rehearsal / recovery behavior

R21_SUPERVISOR_AUTO_RELAUNCH=1

R21_PRE_RUN_RECOVERY_SELF_TEST=PASS
R21_AUTOCONTROLLER_AUTO_RESUME=PASS
R21_AUTOCONTROLLER_COMPLETE=PASS

FINAL_TACC=
4bcabec075e8a3bb1ef522b07acb0386

TOTAL_STEPS=32

R21_SUPERVISOR_COMPLETE=PASS
R21_SUPERVISOR_RELAUNCHES=1

Reference run:
R21_PRE_RUN_RECOVERY_SELF_TEST=PASS
R21_AUTOCONTROLLER_COMPLETE=PASS
FINAL_TACC=4bcabec075e8a3bb1ef522b07acb0386
TOTAL_STEPS=32
R21_SUPERVISOR_COMPLETE=PASS
R21_SUPERVISOR_RELAUNCHES=0

## Exactly-once / inode / verifier

R21G_MIDSTEP_CRASH_REPLAY=PASS
R21G_EXACTLY_ONCE_EFFECT=PASS
R21G_HOT_STORE_INODES_STABLE=PASS

Independent verifier:
VERIFY||RECORDS||65||PACK_BYTES||1648735||COMMIT_BYTES||780||EXPECTED_FOUND||1||WHOLE_PACK_READ||NO

R21G_INDEPENDENT_NATIVE_VERIFIER=PASS

R21_PRE_RUN_RECOVERY_SELF_TEST=PASS
R21_AUTOCONTROLLER_SELF_TEST=PASS

## Final admission status

R21G_AUTONOMOUS_CONTROLLER_ADMISSION=PASS

HEAD=
142a5fcc295a02610e7134312acfee63

MODEL=
4a9f5ef84131c4162633fed959d4fb4d

ACTIVE_RUNTIME_SHA256=
672c15d6e2c7da9342f50938e5f38542f3307490550f80a8b9233b4f11ea0e69

AUTOCONTROLLER_SHA256=
b13dfc12e80f6525c2cdb44415b05c20fa792183158b9abbbff116021a5ff4e5

SUPERVISOR_SHA256=
1b6912a34fbf16b4f41e26c427e31827a1550f861017b830edffd41b16c6c358

CONTROLLER_STATE_FORMAT=
DUAL_SLOT_SHA256_V1

CONTROLLER_STATE_BYTES=8192

CONTROLLER_STATE_INODE_REPLACEMENT_PER_CHECKPOINT=NO

HOT_STORE_INODE_STABILITY=PASS

REHEARSAL_ROWS=32
MIDSTEP_CRASH_AFTER_NATIVE_STEP=11

SUPERVISOR_AUTO_RELAUNCH=PASS
MIDSTEP_CRASH_REPLAY=PASS
FINAL_TACC_DETERMINISTIC=PASS

PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS
COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS

EXACTLY_ONCE_EFFECT=PASS
INDEPENDENT_NATIVE_VERIFIER=PASS

PRE_RUN_RECOVERY_SELF_TEST=PASS

FAULT_EXIT_WITHOUT_RESUME_POINTER=FORBIDDEN
UNATTENDED_DEAD_END=FORBIDDEN
BLOCKED_SAFE_RETAINS_RESUME_POINTER=YES

HOT_STORE_FILES=4
PRODUCTION_PACK_BYTES=0
PRODUCTION_COMMIT_BYTES=0

NEW_INODES_PER_OBJECT=0
NEW_INODES_PER_BATCH=0
NEW_INODES_PER_CHECKPOINT=0

HOST_LEARNING=NO
HOST_SCORING=NO
SIGMA_LEARNS=YES

CANONICAL_MUTATION=NO
MODEL_MUTATION=NO
HEAD_MUTATION=NO
RUNTIME_SELECTOR_MUTATION=NO

REAL_DATA_DELETE=NO

AUTONOMOUS_CONTROLLER_ADMISSION=PASS

NEXT=
R21H_BOOT_PERSISTENCE_AND_PROCESS_WATCHDOG

## Controller contract observations from uploaded implementation

The admitted controller uses:
- a fixed-size 8192-byte dual-slot SHA256 state file;
- atomic in-place slot updates with fsync;
- READY/RUNNING/CHECKPOINTED/RECOVERING/FAULT_CAPTURED/BLOCKED_SAFE/COMPLETE semantics;
- recovery self-test before every invocation;
- persisted resume pointer before mutating native commands;
- bounded retry count with BLOCKED_SAFE after retry exhaustion;
- supervisor auto-relaunch only on RC 75;
- fail-closed supervisor behavior for unexpected child RCs;
- no controller-state inode replacement per checkpoint.

The rehearsal injects a process exit after a native step has completed but before the controller checkpoint is written. On relaunch, the persisted RUNNING state causes replay of that exact step; content-addressed packed storage preserves exactly-once effect.

## Interpretation boundary

This checkpoint records admission of the autonomous controller/supervisor into the already-admitted R21 runtime authority.

It establishes:
- autonomous recovery controller admission;
- pre-run recovery self-test;
- mid-step crash replay;
- exactly-once effect for the tested rehearsal;
- deterministic final TACC versus uninterrupted reference;
- byte-identical pack/commit versus reference;
- independent native verification;
- fixed hot-store inode contract;
- BLOCKED_SAFE retains resume pointer;
- no host learning or scoring;
- no canonical head/model mutation;
- no runtime selector mutation in this R21G step;
- no real-data deletion.

This step does not claim boot/watchdog persistence yet.

NEXT is R21H_BOOT_PERSISTENCE_AND_PROCESS_WATCHDOG.
