# SIGMA I5A Fix1 — D03 stale request-event fixture contamination

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: HARNESS_FAILURE / NATIVE_D03_BEHAVIOR_CORRECT / RUNNER_ONLY_REPAIR_REQUIRED

## User machine evidence

```text
C02_CANONICAL_VERIFY VM_RC=0
CANDIDATE_SET_VALID=1
CANDIDATE_COUNT=10
I5A_STATUS DISCOVERY_RESULT_READY
POST_VM_ALIGNMENT=PASS

D03_WRONG_FAMILY VM_RC=0
SOURCE_FAMILY_ID 20
SOURCE_FAMILY ARXIV
I5A_STATUS HOLD_NOT_WIKIPEDIA
REQUEST_EVENT_EMITTED 0
POST_VM_ALIGNMENT=PASS
HOLD=WRONG_FAMILY_REQUEST_EVENT_EMITTED
```

## Root cause

The native D03 wrong-family behavior was correct:

```text
I5A_STATUS=HOLD_NOT_WIKIPEDIA
REQUEST_EVENT_EMITTED=0
```

The runner then inspected the persistent file:

`state/i5a_request_event.txt`

without clearing the canonical C01 request event first. The file was therefore non-empty because of prior-case residue, not because D03 emitted an event.

Exact runner inspection confirms:

```text
D03 has no pre-case reset of i5a_request_event.txt/request.query.txt
D04/D05/D06 already reset those mechanical output files before each independent PREPARE fixture
```

Classification:

```text
FAILURE_CLASS=MECHANICAL_HARNESS_FIXTURE_CONTAMINATION
NATIVE_I5A_COGNITIVE_FAILURE=NO_EVIDENCE
D03_NATIVE_BEHAVIOR=CORRECT_IN_OBSERVED_SCOPE
NATIVE_I5A_SOURCE_REPAIR_REQUIRED=NO
RUNNER_ONLY_REPAIR_REQUIRED=YES
ORACLE_WEAKENING_ALLOWED=NO
```

## Required repair

Fix2 must preserve all native sources, query/candidate protocols, expected statuses, anti-hardcode gates and host-cognition boundaries.

Before the independent dynamic PREPARE suite, mechanically truncate prior I5A output artifacts so each fixture starts from a clean output state.

```text
HOST_QUERY_GENERATION=NO
HOST_RESULT_RANKING=NO
HOST_CANDIDATE_SELECTION=NO
HOST_RESOURCE_SELECTION=NO
NATIVE_RESOURCE_SELECTION=NOT_PROVEN
I5A_RUNTIME_ADMISSION=NOT_PROVEN_PENDING_FULL_GATE
```
