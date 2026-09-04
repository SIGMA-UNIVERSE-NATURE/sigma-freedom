# V2.5B.2 RESUME BATCH — 10 COMMITTED

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Context

V2.5B.2 filtered + batched full-corpus structural survey is running against the frozen 56-document snapshot.

This checkpoint records the second successful 5-document batch and, importantly, demonstrates persistent resume across separate runner invocations.

## Start state

COMMITTED_AT_START=5
BATCH_LIMIT=5
SNAPSHOT_DOCUMENT_COUNT=56

## Runtime evidence

All five VM cycles completed with VM_RC=0.

Cycle outputs included native structural survey fields:

- document identity/file;
- line count / survey-line limit;
- token and relation counts;
- SKIPPED_EMPTY_RELATIONS;
- unique and recurring relation counts;
- native-selected BEST_LOCAL_RELATION and support;
- HOST_LEARNING=NO;
- HOST_DOCUMENT_SELECTION=NO;
- SEMANTIC_UNDERSTANDING=NOT_PROVEN.

Observed BEST_LOCAL_RELATION values in this batch included:

- `Phi => Sigma`
- `more => than`
- `of => the`
- `is => the`
- `Sigma => Alpha`

No empty-token best relation was observed.

The empty-token filter activated when needed, e.g. SKIPPED_EMPTY_RELATIONS values included 1, 2 and 3 in earlier/adjacent clean batches, proving the native gate is not merely dormant.

## End state

COMMITTED_SURVEY_COUNT=10
SURVEY_COMPLETE_SENTINEL=0
PRODUCTION_RAW_MUTATED=NO
PRODUCTION_LEARNER_MEMORY_MUTATED=NO
HOST_LEARNING=NO
HOST_DOCUMENT_SELECTION=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
V25B_2_FULL_CORPUS_SURVEY=BATCH_COMPLETE
NEXT_ACTION=RERUN_SAME_RUNNER_TO_RESUME_NEXT_BATCH

## Admission interpretation

NATIVE_SURVEY_RESUME_ACROSS_RUNNER_INVOCATIONS=PROVEN_IN_CURRENT_SCOPE

This is not yet the V2.6 deliberate kill/restart/resume proof. It only proves that the V2.5B.2 canonical survey state persists across normal runner termination and the next runner invocation resumes from the next unsurveyed document.

FULL_CORPUS_SURVEY_PASS=NOT_YET
SEMANTIC_UNDERSTANDING=NOT_PROVEN

Do not promote V2.5B.2 to full-corpus PASS until committed count reaches 56 and native SURVEY_COMPLETE=YES is observed.
