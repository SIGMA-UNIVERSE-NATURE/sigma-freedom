# VNM-01 FIX1 — REPLAY INPUT FINGERPRINT HARNESS FAILURE

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: FAILURE EVIDENCE / RUNNER-HARNESS DEFECT / NATIVE SOURCE NOT IMPLICATED BY THIS FAILURE

## Governing rules

`FAILURE_IS_EVIDENCE=YES`

`FAIL_LOCAL_FIX_MINIMAL=YES`

`RERUN_FULL_REQUIRED_SUITE_AFTER_FIX=YES`

`WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

## Supplied machine evidence boundary

The operator supplied the final CASE_018 native output and terminal gate failure from the full VNM-01 FIX1 rerun.

Observed CASE_018 boundary:

```text
CASE=CASE_018_REPLAY_B
VM_RC=0
HYPOTHESIS_VALID=1
PREVIOUS_STATE_VALID=1
PREVIOUS_STATE_INVALID=0
PRIOR_EVIDENCE_COUNT=1
PRIOR_SUPPORT_COUNT=1
PRIOR_COMPETING_COUNT=0
NEW_EVIDENCE_LINE_COUNT=1
NEW_QUALIFIED_EVIDENCE_COUNT=1
NEW_SUPPORT_COUNT=0
NEW_COMPETING_COUNT=1
EVIDENCE_ID_COLLISION_COUNT=0
INVALID_EVIDENCE_RECORD_COUNT=0
INPUT_BOUND_EXCEEDED=0
EVIDENCE_CAPACITY_EXCEEDED=0
WEIGHT_BEFORE=1
PROPOSED_WEIGHT=0
WEIGHT_AFTER=0
NATIVE_UPDATE_REASON=EVIDENCE_SHIFTED_WEIGHT_DOWN
LEARNING_STATUS=QUALIFIED_UPDATE_PERSISTED
STATE_COMMIT_ALLOWED=1
WRITE_READBACK_MATCH=1
STATE_MUTATED=1
HOST_LEARNING=NO
HOST_WEIGHT_UPDATE=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

Terminal gate failure:

```text
VNM_01_PREFLIGHT=FAIL
FAILURE=REPLAY_INPUT_MISMATCH
```

Fields not present in the supplied excerpt remain unknown:

```text
RUNNER_RC=UNKNOWN_NOT_SUPPLIED
BYTECODE_SHA256=UNKNOWN_NOT_SUPPLIED_IN_THIS_EXCERPT
TOTAL_VM_INVOCATIONS=UNKNOWN_NOT_SUPPLIED_IN_THIS_EXCERPT
POST_VM_ALIGNMENT_PASS_COUNT=UNKNOWN_NOT_SUPPLIED_IN_THIS_EXCERPT
POST_VM_ALIGNMENT_FAIL_COUNT=UNKNOWN_NOT_SUPPLIED_IN_THIS_EXCERPT
STEP_LIMIT_HIT_COUNT=UNKNOWN_NOT_SUPPLIED_IN_THIS_EXCERPT
```

## Failure classification

`FAILURE_CLASS=B_RUNNER_HARNESS_DEFECT`

The VNM-01 FIX1 runner computed replay input fingerprints as:

```bash
sha256sum "$IN/hypothesis.memory" "$IN/evidence.memory" | sha256sum
```

GNU/Termux `sha256sum` output contains both each content hash and the file pathname. CASE_017 and CASE_018 live under different sandbox paths, so identical input bytes can produce different aggregate fingerprints solely because the pathname bytes differ.

Therefore the observed `REPLAY_INPUT_MISMATCH` does not, by itself, demonstrate unequal runtime input bytes or a native SIGMA replay defect.

The replay equality gate remains required. The repair must make the fingerprint path-independent while still covering both ordered input files exactly.

## Repair constraint

Allowed repair:

```text
hash hypothesis content
hash evidence content
retain only the two content hashes in declared order
hash that ordered pair
```

Forbidden repair:

```text
remove replay test
ignore mismatch
compare only expected semantic output
change native source to satisfy harness
weaken PASS definition
```

## Native source status

```text
NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma
SOURCE_SHA256=cd399793ebde7e5dfa4a10cf263bb97fd45d1379ce8dac02520d5277cf2ca788
NATIVE_SOURCE_CHANGE_REQUIRED_BY_THIS_FAILURE=NO
```

## Admission status

```text
VNM_01_FIX1_ADMISSION=FAIL
FAILURE_LAYER=RUNNER_HARNESS
PRODUCTION_STATE_MUTATED=NO
SEMANTIC_EQUIVALENCE=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

## Next action

```text
MINIMAL_RUNNER_FIX=PATH_INDEPENDENT_ORDERED_INPUT_CONTENT_FINGERPRINT
RERUN_SCOPE=FULL_18_VM_INVOCATION_VNM01_GATE
NEXT_CAPABILITY=DO_NOT_OPEN_VNM02_UNTIL_VNM01_FULL_PASS
```
