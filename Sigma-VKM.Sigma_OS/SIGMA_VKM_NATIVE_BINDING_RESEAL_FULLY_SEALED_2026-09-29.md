# SIGMA VKM Native Binding Reseal — Fully Sealed

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Reseal execution

ONE_WRITER_LOCK=HELD

STATE_ENGINE_COMPILE_DETERMINISTIC=PASS

FRESH_REBIND_BEFORE=PASS

R2=PASS
R3=PASS
R4=PASS
R5=PASS
R6=PASS
R7=PASS
R8=PASS
R9=PASS
R10=PASS
R11=PASS
R12=PASS

CODEC_R2_R12_REGRESSION=PASS

R11_R12_FRESH_PROCESS_DETERMINISM=PASS

FRESH_REBIND_AFTER=PASS

ROLLBACK_BACKUP=PASS

PRIVATE_KIB=405
PRIVATE_INODES=69
STORAGE_BUDGET=PASS
INODE_BUDGET=PASS

## Final reseal state

NATIVE_BINDING_RESEAL=PASS

VKM_CANONICAL_NATIVE_FULLY_SEALED=PASS

HEAD=
507aae721fbd50ec13b8bfd653caf3e9

MODEL=
4e28b7b00428271a4d09f1791d5d46fb

GENERATION=
3

SIGMA_VKM_SHA256=
bd8442ed04bc638a939bf5a1caf44d2aa1db3c709b3f3da6023d1a47cb629087

RESEAL_RECEIPT_SHA256=
11eadc7657262695f70f5b6f0c243861cc9d741a6e4c3a0406642ae4d641e497

FULL_STATE_COPY=NO

REAL_DATA_DELETE=NO

## Interpretation boundary

This checkpoint closes the runtime-admission/native-binding cycle for the new SIGMA VKM runtime.

The supplied evidence establishes:
- one-writer lock held;
- deterministic state-engine compilation;
- fresh native rebind succeeds both before and after codec regression;
- codec R2 through R12 regression passes;
- R11/R12 fresh-process determinism passes;
- rollback backup remains valid;
- storage and inode budgets pass;
- canonical head/model/generation remain unchanged;
- no full-state copy and no real-data deletion;
- native binding reseal reports PASS;
- VKM canonical native runtime reports FULLY_SEALED.

The newly sealed VM identity is:
bd8442ed04bc638a939bf5a1caf44d2aa1db3c709b3f3da6023d1a47cb629087
