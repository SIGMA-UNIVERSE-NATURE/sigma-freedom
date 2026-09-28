# SIGMA VKM R15 — Durable Packfile + Crash-Tail Recovery

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Durable writer result

FILE_RAW_BYTES=12000
WINDOW_LIMIT=240
WINDOWS=50
STRUCTURED_WINDOWS=50
RAW_WINDOWS=0

PACKFILE_BYTES=9564
COMMIT_LOG_BYTES=612
COMMITTED_OFFSET=9564

WHOLE_FILE_READ=NO
PACKFILE_COUNT=1
COMMIT_LOG_COUNT=1
SOURCE_DELETE=NO
REAL_DATA_DELETE=NO

TOTAL_DURABLE_BYTES=10176

ACTUAL_DURABLE_STORAGE_SMALLER=PASS

## Crash-tail injection

PACK_BEFORE=9564
INJECT_RC=0
PACK_AFTER=9571
COMMIT_LOG_UNCHANGED=612

Injected bytes extended the packfile tail without advancing the commit log.

## Recovery

PACK_SIZE_BEFORE=9571
COMMITTED_OFFSET=9564
COMMITTED_RECORDS=50

TAIL_TRUNCATE_RC=0
PACK_SIZE_AFTER=9564

CRASH_TAIL_RECOVERY=PASS

WHOLE_PACK_READ=NO
REAL_DATA_DELETE=NO

## Interpretation boundary

This checkpoint records durable packfile storage and recovery behavior for the R15 runtime.

The supplied evidence establishes:
- 12,000 raw bytes are represented by 9,564 packfile bytes plus 612 commit-log bytes;
- total durable storage is 10,176 bytes, smaller than the 12,000-byte raw input;
- all 50 windows were stored structurally;
- the writer does not perform a whole-file read;
- one packfile and one commit log are present;
- source data is not deleted;
- a simulated uncommitted tail grows the packfile from 9,564 to 9,571 bytes while the commit log remains unchanged;
- recovery reads the last commit record, identifies committed offset 9,564 and 50 committed records, truncates only the uncommitted tail, and restores packfile size to exactly 9,564 bytes;
- recovery reports CRASH_TAIL_RECOVERY=PASS;
- no whole-pack read and no real-data deletion are reported.

This is crash-tail recovery evidence for the R15 durable packfile path. It does not by itself establish broader crash consistency for failure modes not covered by this injected-tail test.
