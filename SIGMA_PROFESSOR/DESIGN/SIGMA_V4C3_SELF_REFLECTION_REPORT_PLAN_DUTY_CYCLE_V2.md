# SIGMA V4-C3 — NATIVE SELF-REFLECTION / REPORT / PLAN DUTY CYCLE V2

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Status

`DESIGN_READY=YES`

`IMPLEMENTATION_READY=NO`

`LOCKED_SIGMAC_COMPILE=NOT_RUN`

`LOCKED_VM_RUNTIME=NOT_RUN`

`ADMISSION=NOT_RUN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

This V2 refines the earlier V4-C3 duty-cycle design. The requested pause is not merely idle rest. It is a native self-reflection boundary in which SIGMA stops active learning, inspects its own committed machine evidence, commits a bounded report, chooses the next learning plan natively, exposes that plan for observation, pauses briefly, and then resumes automatically without human work selection.

## Canonical operating loop

First admission target:

`DISCOVER -> LEARN -> CONSOLIDATE -> REFLECT -> REPORT -> PLAN -> OBSERVE_PAUSE -> DISCOVER`

Default timing target after native clock admission:

- active learning interval: `3600` seconds;
- report/plan commit: immediately after native transition to reflection;
- observation pause after report commit: `180` seconds;
- after the native pause deadline: execute the already committed native plan and continue learning.

The process remains alive during `OBSERVE_PAUSE`.

`OBSERVE_PAUSE` means no learning, corpus-priority, revisit, or acquisition work is executed. It exists so the machine has a real reflection boundary and a human observer can read the exact committed report without participating in cognition.

## Native ownership invariant

The following decisions are native SIGMA decisions:

- when the active learning interval has ended;
- transition into `REFLECT`;
- which committed evidence belongs to the just-finished cycle;
- all self-assessment counters and percentages;
- which frontier is unresolved;
- which document/revisit/frontier/acquisition request should be next;
- the exact next native action;
- transition out of `OBSERVE_PAUSE` after the native deadline.

Host/Bash may only:

- launch the locked compiler/VM;
- mechanically dispatch an exact native action already emitted;
- transport an exact native line/query when the admitted protocol requires it;
- display exact report bytes;
- supervise process identity and machine logs.

`HOST_REFLECTION=NO`

`HOST_SELF_ASSESSMENT=NO`

`HOST_NEXT_WORK_SELECTION=NO`

`HOST_PERCENT_CALCULATION=NO`

`HOST_REPORT_SUMMARIZATION=NO`

`HOST_LEARNING=NO`

If host logic must compute a report field, understanding score, next-work choice, or phase transition for the gate to pass, the gate fails.

## REFLECT semantics

`REFLECT` is bounded evidence inspection, not a free-form language claim.

SIGMA must compare compact cycle-start and cycle-end state and inspect only bounded committed evidence needed for self-assessment. It must not obtain apparent reflection by rereading the entire corpus or deleting completion state.

Minimum evidence classes:

- documents touched during the cycle;
- per-document start/end line cursor where available;
- learner context/window provenance for committed evidence;
- profile commits;
- line/evidence commits;
- document completion events;
- hold/refusal events;
- unresolved structural frontiers;
- acquisition request history where applicable;
- exact native next-work evidence.

No fake relearning:

`DELETE_COMPLETE_TO_RELEARN=FORBIDDEN`

`RESET_CURSOR_TO_INCREASE_COUNTERS=FORBIDDEN`

`REREAD_IDENTICAL_BYTES_WITHOUT_NATIVE_REVISIT_REASON=FORBIDDEN`

## What SIGMA may report as "what I learned"

The machine must report evidence-grounded objects, for example:

- `CONSOLIDATED_SPAN` records;
- `SUPPORTED_RELATION` records;
- `PROFILE` records;
- `RESOLVED_FRONTIER` records;
- `OPEN_FRONTIER` records;
- `HOLD` / `REFUSAL` records;
- provenance IDs binding each reported item to the actual document/line/context/window evidence that produced it.

The machine must not convert a structural n-gram/span into an unsupported statement such as `I understand concept X`.

Until a separate semantic-understanding admission exists:

`SEMANTIC_UNDERSTANDING=NOT_PROVEN`

`SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`

`SEMANTIC_CURIOSITY=NOT_PROVEN`

## Percentage self-assessment

A numeric percentage is allowed only as an explicitly named machine-evidence proxy.

Canonical rule:

`UNDERSTANDING_PROXY_PERCENT != SEMANTIC_UNDERSTANDING_PERCENT`

The first V4-C3 reporter should expose multiple exact metrics rather than hide them behind one opaque number.

Required candidate fields:

- `CORPUS_DOCUMENT_COVERAGE_PERCENT`;
- `CYCLE_FRONTIER_RESOLUTION_PERCENT`;
- `CYCLE_HOLD_PERCENT`;
- `UNDERSTANDING_PROXY_PERCENT`.

A percentage may be emitted only when its denominator is machine-proven for the exact scope being reported. Otherwise the field must be:

`NOT_COMPUTABLE_FROM_CURRENT_MACHINE_EVIDENCE`

### Initial deterministic proxy policy

For an exact native corpus snapshot/pass where document counts are machine-proven:

`CORPUS_DOCUMENT_COVERAGE_PERCENT = 100 * COMPLETE_DOCUMENT_COUNT / DISCOVERED_DOCUMENT_COUNT`

For a cycle where frontier generation and resolution counts are both machine-proven:

`CYCLE_FRONTIER_RESOLUTION_PERCENT = 100 * RESOLVED_FRONTIER_COUNT / (RESOLVED_FRONTIER_COUNT + OPEN_FRONTIER_COUNT)`

For the same exact snapshot/pass:

`CYCLE_HOLD_PERCENT = 100 * HOLD_DOCUMENT_COUNT / DISCOVERED_DOCUMENT_COUNT`

The first admissible composite is deliberately conservative:

`UNDERSTANDING_PROXY_PERCENT = floor((CORPUS_DOCUMENT_COVERAGE_PERCENT + CYCLE_FRONTIER_RESOLUTION_PERCENT) / 2)`

but ONLY when both component denominators are machine-proven. Otherwise:

`UNDERSTANDING_PROXY_PERCENT=NOT_COMPUTABLE_FROM_CURRENT_MACHINE_EVIDENCE`

This proxy measures corpus coverage plus structural-frontier closure. It is not a semantic truth or human-equivalent understanding score.

## Native report schema

The first reporter must commit a bounded persistent machine report with at least:

```text
CYCLE_ID=<native-cycle-id>
PHASE=REPORT
LEARN_START_NATIVE_TIME=<native-time>
REFLECT_NATIVE_TIME=<native-time>
REPORT_COMMIT_NATIVE_TIME=<native-time>
PAUSE_TARGET_SECONDS=180

DISCOVERED_DOCUMENT_COUNT=<native-count-or-not-computable>
DOCUMENTS_TOUCHED_THIS_CYCLE=<native-bounded-records>
PROFILE_COMMIT_COUNT=<native-count>
LINE_COMMIT_COUNT=<native-count>
EVIDENCE_COMMIT_COUNT=<native-count>
DOCUMENT_COMPLETE_COUNT=<native-count>
DOCUMENT_HOLD_COUNT=<native-count>
REFUSAL_COUNT=<native-count>

CONSOLIDATED_SPANS=<bounded-native-records-with-provenance>
RESOLVED_FRONTIERS=<bounded-native-records-with-provenance>
OPEN_FRONTIERS=<bounded-native-records-with-provenance>

CORPUS_DOCUMENT_COVERAGE_PERCENT=<percent-or-not-computable>
CYCLE_FRONTIER_RESOLUTION_PERCENT=<percent-or-not-computable>
CYCLE_HOLD_PERCENT=<percent-or-not-computable>
UNDERSTANDING_PROXY_PERCENT=<percent-or-not-computable>

NEXT_NATIVE_ACTION=<exact-native-action>
NEXT_DOCUMENT=<native-selected-doc-or-none>
NEXT_FRONTIER=<native-selected-frontier-or-none>
NEXT_ACQUISITION_QUERY=<native-query-or-none>
PLAN_PROVENANCE=<exact-evidence-id-or-record>

SEMANTIC_UNDERSTANDING=NOT_PROVEN
SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
COMMIT=YES
```

The bounded record count for representative spans/frontiers must be fixed by source and admission-tested. The reporter must not dump unbounded corpus state.

## PLAN semantics

After `REPORT` is committed, native SIGMA chooses one next plan from machine evidence.

First admissible priority order:

1. resume an incomplete active line/token continuation;
2. profile a newly discovered unprofiled document;
3. continue an incomplete profiled document selected by native corpus priority;
4. revisit only when an admitted native revisit reason with provenance exists;
5. resolve a native open structural frontier;
6. emit a native exact acquisition request when the frontier requires outside evidence and acquisition is admitted;
7. wait when no admissible work exists.

The plan must be committed before `OBSERVE_PAUSE` begins.

Humans may inspect it but may not edit it to make the next cycle pass.

`HUMAN_OBSERVER_ONLY=YES`

`HUMAN_WORK_SELECTION=NO`

## "Increase capability" claim boundary

In this design, `increase capability` means increasing the persisted learned/evidence state through further admitted learning, consolidation, frontier resolution, and acquisition.

It does NOT yet mean autonomous rewriting of SIGMA source code, compiler code, VM code, admission policy, or locked identities.

`AUTONOMOUS_SELF_SOURCE_MODIFICATION=NOT_PROVEN`

A future self-modification lane would require a separate design and admission boundary.

## Native clock prerequisite

The source-ready clock gate remains prerequisite:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_CLOCK_PERSISTENCE_PROBE_V4C3T1.sigma`

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C3T1_NATIVE_CLOCK_PERSISTENCE_PREFLIGHT.sh`

Until that locked runtime gate passes:

`NATIVE_WALL_CLOCK_DUTY_CYCLE=NOT_PROVEN`

`ONE_HOUR_LEARNING_INTERVAL=NOT_PROVEN`

`THREE_MINUTE_OBSERVE_PAUSE=NOT_PROVEN`

Do not implement a Bash-owned 3600/180 stage timer as a substitute.

## Required implementation sequence

1. run/admit V4-C3 T1 native clock persistence;
2. add compact native cycle-start/cycle-end accounting to the V4 learning controller without destroying existing R2 evidence;
3. implement native self-reflection reporter with bounded evidence records and machine-only percentage calculations;
4. implement native PLAN commit;
5. implement native 3600-second learning deadline and 180-second observation-pause deadline;
6. preflight on isolated shadow state with shortened clock fixtures only for state-machine proof, while native SIGMA still owns all comparisons/transitions;
7. run a real-duration 3600/180 observed gate before claiming the actual duty cycle;
8. only after report/plan/resume PASS, integrate native frontier acquisition;
9. retire V2.4 only after a separate successor cutover/rollback gate proves V4 no longer depends on it.

## Current claim

`V4C3_SELF_REFLECTION_ARCHITECTURE=DESIGN_READY_ONLY`

`SOURCE_READY=NO`

`RUNTIME_PROOF=NO`

`NEXT_ACTION=RUN_NATIVE_CLOCK_GATE_THEN_BUILD_COMPACT_CYCLE_ACCOUNTING_AND_NATIVE_REFLECTION_REPORTER`
