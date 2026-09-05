# V2.15R.1 EVENT-DRIVEN REAL NEXT-WORK TRANSITION — SOURCE READY

Date: 2026-09-05

## Purpose

Composition/admission step only. No new cognitive native source is introduced.

Target chain:

1. exact admitted V2.8R.1 selector chooses first real work and persists dispatch state;
2. admitted V2.13 receives a structural matching test fixture and natively decides `REOBSERVED -> ARCHIVE_FOR_NOW`;
3. admitted V2.14C1 emits exact `SELECT_NEXT_WORK` event;
4. host mechanically routes that event to V2.8R.1;
5. V2.8R.1 selects the second real work from the same frozen 56-document survey;
6. admitted V2.8D.1 resolves and starts bounded learning on that second real snapshot document;
7. a fresh VM invocation must reuse work/cursor state.

Expected deterministic selector sequence from already-admitted V2.8R.1 runtime evidence:

- first: `0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`
- second: `26d19552540508d564f76543e43858724c6e479d0544b50f23bf47b276c9d0f6`

## Runner

`RUN_SIGMA_V215R1_EVENT_DRIVEN_REAL_NEXT_WORK_TRANSITION_PREFLIGHT.sh`

SHA256:
`3b54dc2fce2d408c9ffb9f4cedead91a2b82f69ec8a1688d6518837e9e02e687`

`bash -n` RC = 0.

README:
`SIGMA_V215R1_EVENT_DRIVEN_REAL_NEXT_WORK_TRANSITION_PREFLIGHT_README.txt`

## Admission gates

- first real work native selection;
- native archive lifecycle branch from structural test evidence;
- native `SELECT_NEXT_WORK` event;
- second real work native selection;
- second work differs from first;
- second real snapshot document resolves;
- second work segment 0 native learning begins;
- fresh VM uses persisted work/cursor state;
- non-selection event does not invoke selector;
- deterministic first->second selector replay;
- real survey and second document remain immutable.

## Host boundary

- `HOST_WORK_SELECTION=NO`
- `HOST_STAGE_DECISION=NO`
- `HOST_ARCHIVE_DECISION=NO`
- `HOST_DOCUMENT_SELECTION=NO`
- `HOST_LEARNING=NO`
- mechanical event routing only.

## Claim limits

The archive-producing evidence is a test fixture. Therefore even after PASS:

- `MULTI_DOCUMENT_AUTONOMOUS_CYCLE=NOT_PROVEN`
- `SECOND_WORK_COMPLETE_CYCLE=NOT_PROVEN`
- `GENERAL_AUTONOMOUS_CYCLE_EXECUTION=NOT_PROVEN`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

A PASS may establish only a real event-driven first->second work transition plus learning start on the second real work.
