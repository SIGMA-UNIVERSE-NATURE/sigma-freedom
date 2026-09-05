# V4-PK4 Native Admission V1 — D16 Capacity Fixture Schema Failure

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Status

V4PK4_ADMISSION=FAIL_AT_D16_HARNESS_FIXTURE
V4PK4_NATIVE_SOURCE_RUNTIME_FAILURE=NO
V4PK4_NATIVE_SOURCE_CHANGE_REQUIRED=NO
RUNNER_FIX_REQUIRED=YES
PRODUCTION_BINDING=NO

## Observed machine evidence

The user-provided Termux transcript reached directed case `D16_CAPACITY` with:

- `VM_RC=0`
- `INPUT_VALID=1`
- `GRAPH_VALID=1`
- `EVIDENCE_VALID=1`
- `PREMISE_PAIR_COUNT=1`
- native relation/bridge/premise discovery correct for the target case
- `STATE_VALID=0`
- `INVALID_STATE_RECORD_COUNT=64`
- `V4PK4_STATUS=REFUSE_INVALID_INFERENCE_STORE`
- `POST_VM_ALIGNMENT=FAIL`

## Root cause

The Bash harness capacity fixture wrote each synthetic inference record using the old 13-field shape:

`INFERENCE||...||premise_edge_2||1||1||COMMIT||YES`

The current native V4-PK4 inference schema validates the 12-field shape:

`INFERENCE||id||rule||relation||start||bridge||target||premise_edge_1||premise_edge_2||threshold||COMMIT||YES`

Therefore all 64 synthetic capacity records were correctly rejected by native SIGMA as malformed.

## Interpretation

This failure is evidence of a harness/schema mismatch, not a reason to weaken native validation.

SIGMA_BEHAVIOR_ON_MALFORMED_CAPACITY_FIXTURE=CORRECT_FAIL_CLOSED
NATIVE_INFERENCE_STORE_VALIDATION=OBSERVED_WORKING
HOST_SEMANTIC_SUBSTITUTION=NO

## Required correction

- change only the D16 mechanical capacity fixture to the 12-field current schema;
- keep native `.sigma` source unchanged;
- regenerate runner SHA and bundle SHA;
- rerun the full admission suite from a clean directory;
- V4-PK4 remains NOT ADMITTED until the corrected full suite passes.

CLAIM_SCOPE=HARNESS_FIXTURE_FAILURE_RECORDED_ONLY
