# VNM-08 FIX1 — Negative Support-Mismatch Fault Framing Failure

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: `FAIL_PRESERVED / VNM08_NOT_ADMITTED`

## Governance

```text
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN
FAIL_LOCAL_FIX_MINIMAL=YES
RERUN_FULL_REQUIRED_SUITE_AFTER_FIX=YES
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

## Active stage

```text
CAPABILITY_ID=VNM-08_HIERARCHICAL_SPAN_FORM_TO_PERSISTENT_WEIGHTING_INTEGRATION
INTEGRATION_ONLY_STAGE=YES
NEW_NATIVE_SOURCE_REQUIRED=NO
VNM08_FIX1_WRAPPER=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX1.sh
FIX1_WRAPPER_GIT_BLOB=9fdd179853a7f9eedefd934f143b0d958a9ff1fb
```

## Operator-supplied machine evidence

VNM-08 FIX1 passed the corrected VNM-07 dependency identity gate and progressed through the reused VNM-07 sub-suite and downstream positive/persistence path until the declared negative support-mismatch fixture.

The first failing VNM-04 invocation emitted:

```text
CASE=NEGATIVE_SUPPORT_MISMATCH
VM_RC=0
CANDIDATE_VALID=0
CANDIDATE_FORM_A=
CANDIDATE_FORM_B=
CANDIDATE_SUPPORT=0
RAW_OBSERVATION_LINE_COUNT=4
UNIQUE_OBSERVATION_COUNT=4
DUPLICATE_OBSERVATION_COUNT=0
OBSERVATION_ID_COLLISION_COUNT=0
INVALID_OBSERVATION_RECORD_COUNT=0
INPUT_BOUND_EXCEEDED=0
OBSERVATION_CAPACITY_EXCEEDED=0
ELIGIBLE_EVIDENCE_COUNT=0
SUPPORT_PAIR_COUNT=0
COMPETING_RAW_PAIR_COUNT=0
SUPPORT_MATCH=1
EVIDENCE_CAPACITY_EXCEEDED=0
OUTPUT_ALLOWED=0
BUNDLE_WRITE_READBACK_MATCH=0
OUTPUT_MUTATED=0
BRIDGE_STATUS=REFUSED_CANDIDATE_INVALID
HOST_CANDIDATE_SELECTION=NO
HOST_EVIDENCE_GENERATION=NO
HOST_WEIGHT_UPDATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

The predeclared oracle then reported:

```text
EXPECTED=SUPPORT_PAIR_COUNT 2
VNM_08_PREFLIGHT=FAIL
FAILURE_CASE=NEGATIVE_SUPPORT_MISMATCH
FAILURE=MISSING_EXPECTED_OUTPUT

MATERIALIZED_RUNNER_SHA256=ad85f4525b63ea24ce7802f29278caa6f1d0dbfb335178a7cac142a69f3f4a34
FULL_GATE_RC=60
```

## Exact harness defect

The canonical VNM-08 parent constructs a valid native VNM-02 candidate as:

```text
CANDIDATE||PAIR_CANDIDATE_INDUCED||FORM_A||<fa>||FORM_B||<fb>||SUPPORT||2
```

The positive VNM-04 path consumes that candidate successfully before the negative case.

The negative case intends to alter only the final support field `2 -> 3`, leaving the candidate protocol valid so native VNM-04 can recompute `SUPPORT_PAIR_COUNT=2`, compare it against candidate support `3`, and refuse with `REFUSED_CANDIDATE_SUPPORT_MISMATCH`.

However the runner currently performs the fault via an awk field-splitting/reconstruction expression. Runtime evidence proves the resulting candidate is not merely support-corrupted: native VNM-04 receives a protocol-invalid candidate (`CANDIDATE_VALID=0`, both form fields empty).

Therefore the negative fixture did not exercise the intended mismatch branch.

## Failure classification

```text
FAILURE_CLASS=B_RUNNER_HARNESS_DEFECT
DEFECT_SUBCLASS=NEGATIVE_FAULT_INJECTION_CORRUPTED_CANDIDATE_PROTOCOL_INSTEAD_OF_ONLY_FINAL_SUPPORT_FIELD
VNM04_NATIVE_SOURCE_DEFECT=NO_BY_FAILED_RUNTIME_EVIDENCE
VNM07_NATIVE_SOURCE_DEFECT=NO_EVIDENCE
VNM08_COGNITIVE_POLICY_DEFECT=NO
ORACLE_WEAKENING_ALLOWED=NO
EXPECTED_SUPPORT_PAIR_COUNT_2_REMAINS=YES
EXPECTED_SUPPORT_MATCH_0_REMAINS=YES
EXPECTED_BRIDGE_STATUS_REFUSED_CANDIDATE_SUPPORT_MISMATCH_REMAINS=YES
PRODUCTION_STATE_MUTATED=NO
ADMISSION=FAIL_NOT_ADMITTED
```

## Required repair

Repair only the mechanical negative fault injection:

1. preserve the exact native candidate bytes;
2. verify they end with exact scalar suffix `||SUPPORT||2`;
3. mechanically replace only that exact suffix with `||SUPPORT||3` using newline-free `printf`;
4. read back and equality-check the exact faulted bytes;
5. leave all native sources, case semantics, and expected VNM-04 outputs unchanged;
6. rerun the complete VNM-08 29-VM composed gate.

```text
NEXT_ACTION=RUN_VNM08_FIX2_FULL_29_VM_GATE_AFTER_RUNNER_ONLY_FAULT_INJECTION_REPAIR
```
