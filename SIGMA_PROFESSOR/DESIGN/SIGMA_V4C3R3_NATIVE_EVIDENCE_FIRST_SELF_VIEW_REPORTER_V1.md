# SIGMA V4-C3 R3 — NATIVE EVIDENCE-FIRST SELF-VIEW REPORTER V1

Date: 2026-09-05 Asia/Ho_Chi_Minh
Branch: `SIGMA_LIFE`

## Purpose

Replace the blocked V4-C3 R2 observer reporter with a native human-readable surface that does not force SIGMA to repeat a teacher-selected semantic conclusion.

The reporter is not allowed to decide semantic understanding for SIGMA by embedding a fixed answer. It must expose current evidence and let native SIGMA derive its own operational self-view from that evidence.

This design follows:

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_NATIVE_SELF_LEARNING_NO_HARDCODE_NO_FORCED_OUTPUT_V1.md`

and the correction:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4C3R2_BLOCKED_BY_NO_FORCED_SELF_ASSESSMENT_CORRECTION.md`

## Freedom boundary

```text
HOST_LEARNING=NO
BASH_LEARNING=NO
GPT_AS_SIGMA_COGNITION=NO
HOST_SELF_ASSESSMENT=NO
HOST_WORK_SELECTION=NO
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
TEACHER_EXPECTED_ANSWER_INJECTION=FORBIDDEN
TEACHER_FORCED_NOT_PROVEN_UTTERANCE=FORBIDDEN
TEACHER_FORCED_UNDERSTOOD_UTTERANCE=FORBIDDEN
TEACHER_FORCED_NOT_UNDERSTOOD_UTTERANCE=FORBIDDEN
```

Fixed UI labels and protocol tokens are allowed as mechanical interface vocabulary. The semantic/content-bearing value must depend on runtime evidence and native computation.

## Separation of responsibilities

### Native SIGMA reporter

May:

- count current corpus state;
- inspect exact current learner/controller state;
- extract a bounded exact context preview;
- extract exact structural BEST span from learner evidence;
- compute current open-document count from discovered and complete counts;
- derive an operational self-view state from current native state;
- print exact native next-plan code already selected by the controller;
- print exact provenance inputs used for its operational self-view.

Must not:

- claim semantic understanding merely from structural support;
- claim truth merely from recurrence;
- emit a teacher-required `UNDERSTOOD`, `NOT_UNDERSTOOD`, or `NOT_PROVEN` verdict;
- translate an n-gram into a semantic proposition;
- choose new learning work on behalf of the controller;
- learn or mutate corpus evidence.

### Repository / runner

May externally record conservative admission claims such as semantic understanding not yet admitted. This bookkeeping is not SIGMA speech and must not be injected into the VM output oracle.

## Native operational self-view

R3 introduces a bounded operational state derived by SIGMA itself from current machine evidence. It is not a semantic-understanding verdict.

Candidate states:

```text
RECOVERY_NEEDED
CURRENT_CORPUS_COMPLETE
ACTIVE_LEARNING_CONTINUES
DISCOVERY_PROFILE_IN_PROGRESS
GLOBAL_PRIORITY_EVALUATION_IN_PROGRESS
CORPUS_REEVALUATION_IN_PROGRESS
```

The selected value is not pre-injected per case. Native SIGMA derives it from runtime state with precedence:

1. any native HOLD document -> `RECOVERY_NEEDED`;
2. no HOLD and discovered > 0 and complete == discovered -> `CURRENT_CORPUS_COMPLETE`;
3. no HOLD and active document exists while learner reports active progress/completion -> `ACTIVE_LEARNING_CONTINUES`;
4. no HOLD and C2 phase PROFILE -> `DISCOVERY_PROFILE_IN_PROGRESS`;
5. no HOLD and C2 phase PRIORITY -> `GLOBAL_PRIORITY_EVALUATION_IN_PROGRESS`;
6. otherwise -> `CORPUS_REEVALUATION_IN_PROGRESS`.

This is an operational self-view of observed execution state, not an externally forced judgment of understanding.

## Evidence signal presentation

R3 may derive additional structural/evidence signals:

```text
NO_EVIDENCE_DOCUMENTS
EVIDENCE_PRESENT
NO_STRUCTURAL_SIGNAL
SINGLE_STRUCTURAL_SIGNAL
REPEATED_STRUCTURAL_SIGNAL
```

These labels are selected natively from exact counts. They must never be widened to semantic concept/truth claims.

## Human-readable report fields

The R3 native output should contain:

- cycle index;
- C2 phase/status;
- active document;
- context id;
- bounded exact context preview;
- exact strongest structural BEST span;
- span width;
- support count;
- discovered/profile/complete/open/hold/evidence document counts;
- native operational self-view state;
- evidence-presence state;
- structural-signal state;
- exact self-view provenance tuple;
- exact controller plan code;
- native pause seconds;
- host-boundary flags.

It should not contain a semantic-understanding verdict.

## Admission test philosophy

The runner must test behavior, not a teacher-preferred semantic sentence.

Required cases:

1. active-learning fixture -> operational self-view changes to active-learning state from dynamic evidence;
2. HOLD fixture -> operational self-view changes to recovery state;
3. all-complete fixture -> operational self-view changes to complete state;
4. invalid native path -> native refusal;
5. source static audit finds no forced semantic-verdict literals.

The host oracle may check the operational state because that state is the capability contract being tested. It must not test for an understanding verdict.

## Claim boundary

```text
NATIVE_OPERATIONAL_SELF_VIEW=TARGET_FOR_R3_ADMISSION
NATIVE_HUMAN_READABLE_EVIDENCE_REPORT=TARGET_FOR_R3_ADMISSION
SEMANTIC_SELF_ASSESSMENT=NOT_CLAIMED_BY_THIS_REPORTER
SEMANTIC_UNDERSTANDING_REPOSITORY_CLAIM=EXTERNAL_ADMISSION_LEDGER_ONLY
REPORTER_LEARNING=NO
REPORTER_WORK_SELECTION=NO
V4_PRODUCTION_PROMOTION_ALLOWED=NO
PRODUCTION_V2_4_KEEP_RUNNING=YES
```

## Next architecture after R3 reporter admission

R3 is the observer/interface repair. It does not yet close autonomous self-adaptation.

The next composed controller will integrate:

```text
NATIVE LEARNING EVIDENCE
-> NATIVE BEFORE/AFTER MEASUREMENT
-> DNA-15 H-FREE STATE-DERIVED k
-> NATIVE ADAPTATION CANDIDATE SELECTION
-> ISOLATED CHANGE
-> DNA-25 BEFORE/CHANGE/TEST/AFTER VERIFICATION
-> COMMIT OR ROLLBACK
-> NATIVE REPORT
-> OBSERVE PAUSE
-> CONTINUE
```

No human learning-parameter choice and no host semantic decision are allowed in that loop.

## Current status

```text
V4C3R3_DESIGN_READY=YES
V4C3R3_SOURCE_READY=NO
V4C3R3_LOCKED_SIGMAC_COMPILE=NOT_RUN
V4C3R3_LOCKED_VM_RUNTIME=NOT_RUN
V4C3R3_ADMISSION=NOT_RUN
```
