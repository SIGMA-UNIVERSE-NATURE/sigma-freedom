# V2.8R.1 REAL SURVEY -> CURRICULUM BRIDGE — LOCKED-RUNTIME PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Admission result

`V28R1_REAL_SURVEY_CURRICULUM_BRIDGE_PREFLIGHT=PASS`

Locked identities:

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- source SHA256: `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
- bytecode SHA256: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`

## Real-data evidence

Native code read the actual admitted V2.5B.2 survey state.

Observed:

- `SURVEY_LINE_TOTAL 57`
- `REAL_SURVEY_COMMITTED_DOC_COUNT 56`
- `DUPLICATE_SURVEY_DOC_COUNT 0`
- `IGNORED_SURVEY_RECORD_COUNT 0`
- `EMPTY_PROFILE_COUNT 0`
- `DISTINCT_NONEMPTY_ANCHOR_COUNT 31`

First fresh state run:

- `PERSISTED_DISPATCH_COUNT 0`
- `ELIGIBLE_UNDISPATCHED_COUNT 56`
- selected work: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
- selected exact-anchor support: `15`
- `DISPATCH_APPEND_RC 0`

Second fresh VM process reused committed dispatch state:

- `PERSISTED_DISPATCH_COUNT 1`
- `ELIGIBLE_UNDISPATCHED_COUNT 55`
- selected a different real document: `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`

Deterministic replay from empty isolated curriculum state reproduced the first selection and exact state/output hashes:

- state SHA256: `3225092993410c1b7ed77c5a668439e7d9fc78b0e572b394d0ece8a51417279e`
- selected-work SHA256: `aec665f2fe5e56d883007388ed467450745937aced3c85db3b3dbac1f5e46904`

Partial state test:

- uncommitted dispatch record was ignored;
- `IGNORED_STATE_RECORD_COUNT 1`;
- real first selection remained unchanged.

Bounded refusal tests:

- state split lines 67 -> `STATE_LIMIT_EXCEEDED 1`, `STATE_MUTATION_ALLOWED NO`;
- survey split lines 67 -> `SURVEY_LIMIT_EXCEEDED 1`, `STATE_MUTATION_ALLOWED NO`;
- both refusal cases returned VM rc 0 without mutating the selected-work sentinel.

Real survey source SHA before/after matched; `REAL_SURVEY_MUTATED=NO`.

## Admitted claim scope

- `REAL_SURVEY_56_DOCUMENT_INPUT=PASS`
- `NATIVE_REAL_SURVEY_STRUCTURAL_FRONTIER=PROVEN_IN_FROZEN_SNAPSHOT_SCOPE`
- `PERSISTENT_DISPATCH_STATE_INFLUENCES_LATER_FRESH_VM=PASS`
- `DETERMINISTIC_REAL_SURVEY_REPLAY=PASS`
- `PARTIAL_STATE_COMMIT_FILTER=PASS`
- `STEP_LIMIT_STATUS=BOUNDED`
- `HOST_WORK_PROFILE_GENERATION=NO`
- `HOST_CURRICULUM_PRIORITY=NO`
- `HOST_LESSON_SELECTION=NO`
- `HOST_LEARNING=NO`
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`

Still NOT proven:

- semantic importance;
- semantic understanding;
- bounded file I/O;
- atomic recovery from a kill during append.

## Next gate

`BUILD_SELECTED_WORK_TO_DEEP_RELEARN_SEGMENT_CURSOR_PREFLIGHT`

The next gate must consume a document selected by native curriculum output, resolve the actual frozen snapshot document without host semantic selection, and perform persistent bounded deep re-learning segment traversal with provenance.
