# SIGMA VKM R17 — Storage Planner

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

R17_COMPILE_DETERMINISTIC=PASS

## Run 1

### CASE_RAW

RAW_FRAME_BYTES=110
STRUCT_FRAME_BYTES=115
SELECTED_MODE=RAW
SELECTED_FRAME_BYTES=110
NEW_INODES=0
NEVER_EXPANDS=PASS
EXPECTED_SELECTION=PASS

### CASE_STRUCTURED

RAW_FRAME_BYTES=318
STRUCT_FRAME_BYTES=87
SELECTED_MODE=STRUCTURED
SELECTED_FRAME_BYTES=87
NEW_INODES=0
NEVER_EXPANDS=PASS
EXPECTED_SELECTION=PASS

### CASE_REF

RAW_FRAME_BYTES=318
STRUCT_FRAME_BYTES=323
SELECTED_MODE=REF
SELECTED_FRAME_BYTES=146
NEW_INODES=0
NEVER_EXPANDS=PASS
EXPECTED_SELECTION=PASS

### CASE_DELTA

DELTA_FRAME_BYTES=177
RAW_FRAME_BYTES=318
STRUCT_FRAME_BYTES=323
SELECTED_MODE=DELTA
SELECTED_FRAME_BYTES=177
NEW_INODES=0
NEVER_EXPANDS=PASS
EXPECTED_SELECTION=PASS

R17_STORAGE_PLANNER=PASS
ACTUAL_SERIALIZED_COST_DECISION=PASS
BYTE_BUDGET_ENFORCED=PASS
INODE_BUDGET_ENFORCED=PASS
NEW_INODES_PER_ARTIFACT=0
REAL_DATA_DELETE=NO

## Run 2

The same case results were reproduced exactly.

R17_STORAGE_PLANNER=PASS
ACTUAL_SERIALIZED_COST_DECISION=PASS
BYTE_BUDGET_ENFORCED=PASS
INODE_BUDGET_ENFORCED=PASS
NEW_INODES_PER_ARTIFACT=0
REAL_DATA_DELETE=NO

## Fresh-process reproducibility

R17_FRESH_PROCESS_REPRODUCIBILITY=PASS

## Interpretation boundary

This checkpoint records R17 storage-planner behavior for the supplied RAW, STRUCTURED, REF, and DELTA cases.

The supplied evidence establishes:
- planner selection is based on actual serialized frame cost;
- RAW is selected when structured form is larger;
- STRUCTURED is selected when it is materially smaller;
- REF and DELTA are selected when their serialized representations are the expected lower-cost choice;
- selected forms do not exceed the compared alternatives in these test cases;
- byte and inode budgets are enforced;
- no new inode is created per tested artifact;
- no real-data deletion occurred;
- two fresh runs produce identical output.

This is storage-planner evidence for the tested cases and does not, by itself, establish behavior for untested planner states or a separate runtime admission.
