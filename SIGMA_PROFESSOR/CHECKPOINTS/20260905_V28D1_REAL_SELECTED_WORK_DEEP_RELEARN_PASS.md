# V2.8D.1 REAL SELECTED WORK -> DEEP RE-LEARN — PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Locked runtime identities

- SIGMAC SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- V2.8R.1 bridge source SHA256: `8d4fee26c5d0768aaec99eaa960d0cd7f52251680d86391f3dd4c3de89d430e8`
- V2.8R.1 bridge bytecode SHA256: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
- V2.8D.1 source SHA256: `3da9195db5cf24fb3bc5094823ca13e52caa4335b6605c185e7921033079e8ce`
- V2.8D.1 bytecode SHA256 observed on device: `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`

## Real native curriculum selection

The exact admitted V2.8R.1 bridge was run against the real frozen V2.5B.2 56-document survey.

Observed:

- `VM_RC=0`
- `REAL_SURVEY_COMMITTED_DOC_COUNT 56`
- `HOST_WORK_PROFILE_GENERATION NO`
- `HOST_CURRICULUM_PRIORITY NO`
- `HOST_LESSON_SELECTION NO`
- `HOST_LEARNING NO`
- native selected work: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
- selected anchor support: `15`

The selected snapshot document SHA256 equals its content-addressed ID:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`.

## Native selected-work document resolution

V2.8D.1 consumed the native selected-work ID directly, combined it with the mechanical frozen snapshot-directory config, constructed the `.document` path natively, and exercised locked-VM `file_exists`.

Observed:

- `DOCUMENT_EXISTS 1`
- `FILE_EXISTS_LOCKED_VM_RUNTIME=PASS`
- `HOST_DOCUMENT_SELECTION=NO`

## Deep re-learn segment 0

Observed:

- `VM_RC=0`
- `LINE_TOTAL 10`
- `WORK_SWITCHED 1`
- `SEGMENT_INDEX 0`
- `SEGMENT_START_LINE 0`
- `SEGMENT_END_LINE 8`
- `TOKEN_COUNT 439`
- `RELATION_OCCURRENCES 431`
- `UNIQUE_RELATIONS 398`
- `BEST_LOCAL_RELATION in => the`
- `BEST_LOCAL_SUPPORT 6`
- `EVIDENCE_APPEND_RC 0`
- `EVIDENCE_READY 1`
- `CURSOR_APPEND_RC 0`

## Fresh VM segment 1

Observed:

- `VM_RC=0`
- `WORK_SWITCHED 0`
- `SEGMENT_INDEX 1`
- `SEGMENT_START_LINE 8`
- `SEGMENT_END_LINE 10`
- `TOKEN_COUNT 30`
- `RELATION_OCCURRENCES 28`
- `UNIQUE_RELATIONS 28`
- `BEST_LOCAL_RELATION As => disagreements`
- `BEST_LOCAL_SUPPORT 1`
- `EVIDENCE_APPEND_RC 0`
- `EVIDENCE_READY 1`
- `CURSOR_APPEND_RC 0`

## Fresh VM completion

Observed:

- `VM_RC=0`
- `DEEP_RELEARN_COMPLETE YES`
- `SEGMENT_INDEX 2`
- two committed deep-evidence records
- deep evidence SHA256: `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`

## Replay / negative / boundedness

Deterministic replay regenerated the exact same deep-evidence SHA256:
`9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a`.

Negative empty selection:

- `SELECTED_WORK_VALID 0`
- `STATE_MUTATION_ALLOWED NO`

Over-budget evidence state:

- `EVIDENCE_LINE_TOTAL 67`
- `EVIDENCE_LIMIT_EXCEEDED 1`
- `STATE_MUTATION_ALLOWED NO`

Immutability:

- `REAL_SURVEY_MUTATED=NO`
- `SELECTED_DOCUMENT_MUTATED=NO`
- `PRODUCTION_LEARNER_MEMORY_MUTATED=NO`

## Admission

`V28D1_SELECTED_WORK_TO_DEEP_RELEARN_PREFLIGHT=PASS`

Admitted within tested scope:

- `REAL_NATIVE_CURRICULUM_SELECTED_DOCUMENT=PASS`
- `NATIVE_SELECTED_WORK_DOCUMENT_RESOLUTION=PASS`
- `FILE_EXISTS_LOCKED_VM_RUNTIME=PASS`
- `NATIVE_REAL_SELECTED_WORK_SEGMENT_RELEARN=PROVEN_IN_SELECTED_DOCUMENT_SCOPE`
- `PERSISTED_CURSOR_INFLUENCES_LATER_FRESH_VM=PASS`
- `DETERMINISTIC_DEEP_EVIDENCE_REPLAY=PASS`
- `DEEP_EVIDENCE_PROVENANCE_PERSISTENCE=PASS`
- `NEGATIVE_EMPTY_SELECTION=PASS`
- `EVIDENCE_STATE_STEP_LIMIT_STATUS=BOUNDED`

Still not proven:

- `SEMANTIC_IMPORTANCE=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Next dependency

`BUILD_DEEP_RELEARN_COMPLETION_TO_REVALIDATION_PREFLIGHT`

Revalidation must be structural/evidence-based only. It must not relabel anchor recurrence as semantic truth or understanding.
