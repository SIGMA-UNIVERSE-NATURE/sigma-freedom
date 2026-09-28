# SIGMA R19 — GC Rehearsal + Durable Recovery

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Fresh-process restore

Restore run 1:
RESTORED_FILES=1
R19_RESTORE=PASS
BYTE_EXACT_DURABLE_RECOVERY=PASS
SOURCE_READ=NO
RETEACH=NO
WHOLE_PACK_READ=NO
REAL_DATA_DELETE=NO

Restore run 2:
RESTORED_FILES=1
R19_RESTORE=PASS
BYTE_EXACT_DURABLE_RECOVERY=PASS
SOURCE_READ=NO
RETEACH=NO
WHOLE_PACK_READ=NO
REAL_DATA_DELETE=NO

RESTART1=BYTE_EXACT_PASS
RESTART2=BYTE_EXACT_PASS

R19_FRESH_PROCESS_OUTPUT_DETERMINISTIC=PASS
R19_RESTORED_BYTES_DETERMINISTIC=PASS

## Canonical continuity

HEAD=
507aae721fbd50ec13b8bfd653caf3e9

## R19 receipt

SCHEMA=
SIGMA_AUTOLEARN_STORAGE_R19_GC_REHEARSAL_R1

STATUS=PASS
LINEAGE=ONE_SIGMA

HEAD=
507aae721fbd50ec13b8bfd653caf3e9

SIGMA_VKM_SHA256=
0ad6424ccb84bfe2f44240bff8d1cf531a2fb0be88c61491ee113ba740269755

R19_MISSING_ACK_FAIL_CLOSED=PASS
R19_CORRUPT_LEDGER_FAIL_CLOSED=PASS
R19_CORRUPT_PACK_FAIL_CLOSED=PASS
R19_CORRUPT_COMMIT_FAIL_CLOSED=PASS

R19_SYNTHETIC_STORAGE_ACK=PASS
R19_STORAGE_DURABILITY_GATE=PASS
R19_SYNTHETIC_DELETE_REHEARSAL=PASS

R19_FRESH_PROCESS_RESTORE_1=PASS
R19_FRESH_PROCESS_RESTORE_2=PASS
R19_BYTE_EXACT_DURABLE_RECOVERY=PASS
R19_FRESH_PROCESS_DETERMINISM=PASS

R19_RETEACH=NO
R19_SOURCE_READ_AFTER_DELETE=NO

FULL_STATE_COPY=NO
REAL_GC_ENABLED=NO
REAL_DATA_DELETE=NO

R19_GC_REHEARSAL=PASS

R20_FULL_CODEC_OWNERSHIP=PENDING

## Ownership state append

R19_GC_REHEARSAL=PASS
R19_CORRUPTION_FAIL_CLOSED=PASS
R19_SYNTHETIC_DELETE_REHEARSAL=PASS
R19_FRESH_PROCESS_BYTE_EXACT_RECOVERY=PASS
R19_NO_RETEACH_RECOVERY=PASS

R20_FULL_CODEC_OWNERSHIP=PENDING
REAL_GC_ENABLED=NO
REAL_DATA_DELETE=NO

## Interpretation boundary

This checkpoint records a rehearsal only.

The supplied evidence establishes:
- missing acknowledgement and corrupt ledger/pack/commit paths fail closed;
- synthetic storage acknowledgement and durability gate pass;
- synthetic delete rehearsal passes;
- two fresh-process restores recover one file byte-exactly;
- restore output and restored bytes are deterministic across the two fresh runs;
- recovery uses neither source reread nor reteaching;
- no whole-pack read is reported;
- canonical head remains unchanged;
- no full-state copy is reported;
- real GC remains disabled;
- no real data deletion occurs.

R20_FULL_CODEC_OWNERSHIP remains PENDING. This R19 receipt must not be interpreted as authorization for real destructive GC.
