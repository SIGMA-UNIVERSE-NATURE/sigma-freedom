# V2.15R.1 EVENT-DRIVEN REAL NEXT-WORK TRANSITION — PASS

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Admission

`V215R1_EVENT_DRIVEN_REAL_NEXT_WORK_TRANSITION_PREFLIGHT=PASS`

Runner SHA256:
`3b54dc2fce2d408c9ffb9f4cedead91a2b82f69ec8a1688d6518837e9e02e687`

Locked runtime gate in runner:

- sigmac SHA256 `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- VM v09 candidate SHA256 `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

Note: this V2.15 transcript did not print the two runtime hashes even though the runner equality-gated them before execution. All future admission runners must print `SIGMAC_SHA256` and `VM_SHA256` explicitly at the start of the transcript.

Observed recompiled bytecodes:

- V2.8R.1 selector: `0244d7a6ea0888c95f7db97ee2df0e7f50bfcb7bae2a00fd9b48e2aa0dec1eb5`
- V2.8D.1 deep learner: `e23fd92ed4a554195505cc490d5114531320e32ffbb481a421ded36e9c94e2ff`
- V2.13: `ef3ea3e54a9d9d4c1858c877fc9046f9a66227fb150bd5a3c0d9847246ce609d`
- V2.14C1 controller: `9d7b120c7f51939c6679d55629d46816f041679164ff5c4afa8feb5af278d4f5`

## Real first -> second work transition

First native selected work:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

First selector state SHA256:
`3225092993410c1b7ed77c5a668439e7d9fc78b0e572b394d0ece8a51417279e`

Native V2.13 test-evidence branch produced:
`REOBSERVED -> ARCHIVE_FOR_NOW`.

Native V2.14C1 then produced exact event:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b::|::SELECT_NEXT_WORK`

Mechanical dispatcher routed that exact stage to the already-admitted V2.8R.1 selector.

Second native selected work:
`26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`

Second selector state SHA256:
`16134eff08cd5fe385897f2ec689febab4e719f224470d296ebccc3ad118037d`

The second work differs from the first and resolved to a real frozen snapshot document whose SHA256 equals its content-addressed ID:
`26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`.

## Second real work native learning

Second document line total: 8.

Segment 0:

- VM_RC=0
- DOCUMENT_EXISTS=1
- WORK_SWITCHED=1
- SEGMENT_INDEX=0
- [0,8)
- TOKEN_COUNT=180
- RELATION_OCCURRENCES=169
- SKIPPED_EMPTY_RELATIONS=3
- UNIQUE_RELATIONS=154
- BEST_LOCAL_RELATION=`of => the`
- BEST_LOCAL_SUPPORT=3
- EVIDENCE_READY=1
- CURSOR_APPEND_RC=0

Second-work evidence SHA256 after segment 0:
`8cbd66050013d4061086f2d774b60a632fe98e3263427592f8806fa25c56d2b5`

Second-work cursor SHA256 after segment 0:
`cbe5cfdf7c2118a9c3d78ef1d684f3afa089201352886449a06a6511cfef74a7`

Fresh VM continuation:

- VM_RC=0
- DEEP_RELEARN_COMPLETE=YES
- WORK_SWITCHED=0
- LINE_TOTAL=8
- SEGMENT_INDEX=1
- SEGMENT_START_LINE=8

Thus persisted second-work state influenced a later fresh VM invocation.

## Negative / replay / immutability

Native non-selection event:
`...::||::EXECUTE_REVISIT`

The selector was not invoked and selector state remained unchanged.

Deterministic selector replay reproduced first -> second selection and exact second selector-state hash.

Real survey SHA256 after:
`de682a2d5a27e1985d2529106c5410f7e824dafbf5e7cb541485687166295d08`

Second selected document SHA256 after:
`26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`

## Claims admitted

- `NATIVE_ARCHIVE_TO_SELECT_NEXT_WORK_EVENT=PASS`
- `REAL_NATIVE_FIRST_TO_SECOND_WORK_TRANSITION=PROVEN_IN_FROZEN_56_DOCUMENT_SURVEY_SCOPE`
- `SECOND_REAL_WORK_DIFFERS_FROM_FIRST=PASS`
- `SECOND_REAL_WORK_NATIVE_DOCUMENT_RESOLUTION=PASS`
- `SECOND_REAL_WORK_NATIVE_LEARNING_STARTED=PASS`
- `SECOND_REAL_WORK_PERSISTED_CURSOR_INFLUENCES_FRESH_VM=PASS`
- `NON_SELECTION_EVENT_DOES_NOT_TRIGGER_SELECTOR=PASS`
- `DETERMINISTIC_REAL_SELECTOR_REPLAY=PASS`
- `REAL_SURVEY_MUTATED=NO`
- `SECOND_SELECTED_DOCUMENT_MUTATED=NO`

Host boundary remained:

- `HOST_WORK_SELECTION=NO`
- `HOST_STAGE_DECISION=NO`
- `HOST_ARCHIVE_DECISION=NO`
- `HOST_DOCUMENT_SELECTION=NO`
- `HOST_LEARNING=NO`
- `MECHANICAL_HOST_EVENT_DISPATCH=YES`

## Claim limits

The archive-producing evidence for the first work in V2.15 was a structural test fixture. Therefore:

- `MULTI_DOCUMENT_AUTONOMOUS_CYCLE=NOT_PROVEN`
- `SECOND_WORK_COMPLETE_CYCLE=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

## Next

Build a real complete lifecycle on the second selected document using its real deep evidence. Do not hardcode whether real revalidation yields REOBSERVED or NOT_REOBSERVED; let native evidence decide and route the resulting native lifecycle mechanically.
