# SIGMA V2.6 BOUNDED SEGMENT CURSOR + RESTART PREFLIGHT — PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Result

V2.6 preflight passed on the locked compiler + VM.

Locked identities:

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- Source SHA256: `9cac5d9ddb10295b3ebf1f4300412e1b6dc3adceaf5f1de70eb83d0508f3b970`
- Bytecode SHA256: `e850848a9b0fc8905ae50ddf609e28235a1c431fe045011bd88d9fc0c39e33b2`

Fixture:

`ccfdecb4cd296cd18d5d44c53be4638b027b212a2c6df2372abd350e2782efac.document`

Observed line count: 63.

Segment policy:

- fixed 8-line windows;
- segment index is derived natively from persisted cursor text;
- host does not choose the segment;
- empty-token relations remain filtered natively.

## Phase 1 — segment 0 + committed cursor

Observed:

- `VM_RC=0`
- `SEGMENT_INDEX 0`
- `SEGMENT_START_LINE 0`
- `SEGMENT_END_LINE 8`
- `SEGMENT_LINE_BUDGET 8`
- `TOKEN_COUNT 462`
- `RELATION_OCCURRENCES 451`
- `SKIPPED_EMPTY_RELATIONS 3`
- `UNIQUE_RELATIONS 419`
- `BEST_LOCAL_RELATION study => of`
- `BEST_LOCAL_SUPPORT 4`
- `CURSOR_APPEND_RC 0`
- `CURSOR_BYTES_AFTER=1`
- `V26_PHASE1_COMMIT=PASS`

After the successful VM commit, the runner deliberately terminated its own process with TERM.

## Phase 2 — restart + native resume

On a fresh invocation of the same runner:

- `V26_INITIALIZATION=REUSE_PERSISTED_CURSOR`
- `CURSOR_BYTES_BEFORE=1`
- `RECOVERY_DETECTED=YES`
- `PERSISTED_CURSOR_BEFORE_RESTART=1`
- `VM_RC=0`
- `SEGMENT_INDEX 1`
- `SEGMENT_START_LINE 8`
- `SEGMENT_END_LINE 16`
- `CURSOR_APPEND_RC 0`
- `CURSOR_BYTES_AFTER=2`

Final admission output:

- `V26_BOUNDED_SEGMENT_CURSOR_PREFLIGHT=PASS`
- `PERSISTED_CURSOR_RESUME_AFTER_PROCESS_TERMINATION=PASS`
- `HOST_SEGMENT_SELECTION=NO`
- `SIGMA_SEGMENT_SELECTION=PERSISTED_CURSOR_NEXT_FIXED_WINDOW`
- `SEGMENT_COMPUTATION_BOUNDED=YES`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_COMMIT_CRASH_ATOMICITY=NOT_PROVEN`
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Claim scope

Proven in tested scope:

- SIGMA-native derivation of fixed-window segment index from persistent cursor;
- persistent cursor advancement after a successful segment computation;
- process termination between committed cycles does not lose the cursor;
- fresh runner invocation resumes the next segment without host segment selection;
- segment computation itself is bounded to 8 lines.

Not proven:

- bounded file I/O (`read_text` still loads the whole file);
- atomic recovery from a kill during `append_text` itself;
- semantic understanding;
- semantic curiosity;
- general autonomous reasoning.

## Important observation

Segment 1 produced:

- `TOKEN_COUNT 58`
- `RELATION_OCCURRENCES 0`
- `SKIPPED_EMPTY_RELATIONS 50`
- `UNIQUE_RELATIONS 0`

This does not invalidate the cursor/restart proof. It does show that some fixed windows may contain mostly blank/spacing structure, so later structural grouping/curriculum stages must tolerate empty-evidence segments rather than treating every segment as informative.

## Next action

Build a V2.6 full-document segment-cursor runner using a fresh derived namespace and small batches. Prove complete traversal of the 63-line fixture to native `DOCUMENT_SEGMENTS_COMPLETE YES` before promoting segment traversal to broader corpus use.
