# SIGMA V4-C3 R4 — OPERATIONAL REFLECTION + PLAN CONTROLLER WITHOUT FORCED SEMANTIC UTTERANCE V1

Date: 2026-09-05 Asia/Ho_Chi_Minh
Branch: `SIGMA_LIFE`

## Purpose

Replace blocked-for-future-integration C3R1 with a native controller that preserves the admitted operational reflection mechanics while removing teacher-authored semantic-understanding and understanding-percentage conclusions from SIGMA output and persisted report state.

Governing correction:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4C3R1_BLOCKED_FOR_FUTURE_INTEGRATION_BY_FORCED_SEMANTIC_UTTERANCE.md`

Governing lock:

`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md`

## Native responsibilities

C3R4 may natively:

- observe exact C2R2/B4R2 operational state;
- track a persisted progress budget from native learner context/cursor changes;
- decide when the operational reflection boundary is reached;
- count current raw/profile/complete/hold/evidence files using mechanical ABI primitives;
- choose an operational next plan from current native execution state;
- commit an exact operational report and exact native plan;
- use native `time_now` / `time_sleep` for the observe pause;
- clear only its own progress counter after a successful native pause;
- resume the learning loop after the pause.

C3R4 must not:

- emit `UNDERSTOOD`, `NOT_UNDERSTOOD`, `NOT_PROVEN`, or equivalent teacher-selected semantic verdicts;
- emit a teacher-selected understanding percentage or understanding-proxy conclusion;
- decide semantic truth from structural recurrence;
- choose a document, line, token window, source, research goal, or learning content on behalf of C2R2/B4R2;
- learn corpus content itself;
- allow host/Bash/GPT to choose the plan or reflection result.

## Compatibility

To preserve persistent shadow continuity without host migration of cognitive state, C3R4 intentionally reuses the existing C3R1 state file names:

```text
SIGMA_V4C3R1_INITIALIZED.memory
SIGMA_V4C3R1_LAST_SEEN_PROGRESS_KEY.memory
SIGMA_V4C3R1_PROGRESS.memory
SIGMA_V4C3R1_CYCLE.memory
SIGMA_V4C3R1_PROGRESS_BUDGET.memory
SIGMA_V4C3R1_PAUSE_SECONDS.memory
SIGMA_V4C3R1_LAST_REPORT.memory
SIGMA_V4C3R1_PLAN.memory
SIGMA_V4C3R1_STATUS.memory
```

This is a state-schema compatibility choice, not a claim that the R1 source remains current.

No host translation or semantic migration is required.

## Operational plan algorithm

The plan is selected by native SIGMA from current machine state, not injected as the per-case answer.

Precedence:

1. any current `.hold` -> `PLAN_NATIVE_HOLD_RECOVERY_REQUIRED`;
2. otherwise C2 phase PROFILE -> `PLAN_CONTINUE_NATIVE_PROFILE`;
3. otherwise C2 phase PRIORITY -> `PLAN_CONTINUE_NATIVE_GLOBAL_PRIORITY`;
4. otherwise C2 phase LEARN with no active doc -> `PLAN_REEVALUATE_CORPUS`;
5. otherwise C2 phase LEARN with active doc -> `PLAN_RESUME_ACTIVE_DOCUMENT`;
6. otherwise -> `PLAN_CONTINUE_NATIVE_CORPUS_EVALUATION`.

These are operational action codes. Admission must show output changes under materially different runtime state.

## Operational report

Persisted report fields are limited to machine-observable operational evidence:

```text
CYCLE_U
PROGRESS_U
DISCOVERED_DOCUMENTS_U
PROFILE_DOCUMENTS_U
COMPLETE_DOCUMENTS_U
HOLD_DOCUMENTS_U
EVIDENCE_DOCUMENTS_U
C2_PHASE
ACTIVE_DOCUMENT
C2_STATUS
B4_STATUS
BEST_WIDTH_U
BEST_SUPPORT_U
NEXT_PLAN
COMMIT=YES
```

Forbidden report fields include any teacher-authored semantic-understanding verdict or understanding percentage/proxy conclusion.

## Native pause

The pause remains native:

```text
PAUSE_SECONDS=str_len(PAUSE_U)
START_TIME=time_now()
TARGET_TIME=START_TIME+PAUSE_SECONDS
time_sleep(PAUSE_SECONDS)
END_TIME=time_now()
```

If `TARGET_TIME <= END_TIME`, native SIGMA clears only its C3 progress state and emits operational resume status.

If the clock progress condition is not satisfied, the operational refusal status is:

`REFUSE_OBSERVE_PAUSE_PROGRESS_INSUFFICIENT`

The replacement avoids the `NOT_PROVEN` token entirely.

## Admission requirements

The locked-runtime preflight must prove, in exact fixture scope:

```text
LOCKED_SIGMAC_EXECUTION=PASS
LOCKED_VM_EXECUTION=PASS
FORCED_SEMANTIC_VERDICT_LITERAL_IN_SOURCE=NO
FORCED_SEMANTIC_VERDICT_IN_VM_OUTPUT=NO
NATIVE_PROGRESS_BUDGET_DECISION=PASS
NATIVE_OPERATIONAL_PLAN_CHANGES_WITH_RUNTIME_STATE=PASS
NATIVE_OPERATIONAL_REPORT_COMMIT=PASS
NATIVE_OBSERVE_PAUSE_RESUME=PASS
NEGATIVE_INVALID_STATE_REFUSAL=PASS
HOST_REFLECTION=NO
HOST_SELF_ASSESSMENT=NO
HOST_NEXT_WORK_SELECTION=NO
HOST_LEARNING=NO
BASH_LEARNING=NO
GPT_AS_SIGMA_COGNITION=NO
```

At minimum, exercise materially different plan states without changing source/bytecode:

- active LEARN document -> `PLAN_RESUME_ACTIVE_DOCUMENT`;
- PRIORITY state -> `PLAN_CONTINUE_NATIVE_GLOBAL_PRIORITY`;
- HOLD state -> `PLAN_NATIVE_HOLD_RECOVERY_REQUIRED`;
- malformed unary state -> native refusal.

The fixture may establish mechanical state conditions. It must not prewrite `SIGMA_V4C3R1_PLAN.memory` with the expected answer before the controller runs.

## Integration after admission

Only after C3R4 passes should the real continuous shadow be updated to:

```text
C2R2 / A3 / B4R2
-> C3R4 operational reflection boundary
-> C3R4 native report+plan commit
-> C3R4 native 180-second pause
   -> during pause, R3 evidence-first reporter runs read-only on the same native state
-> C3R4 native resume
-> next C2R2 turn
```

The host may mechanically observe that the C3 report changed and launch the already-admitted R3 reporter. It may not summarize, translate, classify, or choose the report meaning.

## Claim boundary

C3R4 is an operational reflection controller, not a semantic-understanding capability and not yet the DNA15/DNA25 self-adaptation controller.

Repository-only claims remain external bookkeeping and are not injected as SIGMA speech.

```text
V4C3R4_DESIGN_READY=YES
V4C3R4_SOURCE_READY=NO
V4C3R4_RUNTIME_ADMISSION=NOT_RUN
REAL_C2R2_CONTINUOUS_R3_REPORT_INTEGRATION=NOT_PROVEN
AUTONOMOUS_SELF_LEARNING_ADAPTATION=NOT_PROVEN
V4_PRODUCTION_PROMOTION_ALLOWED=NO
PRODUCTION_V2_4_KEEP_RUNNING=YES
```
