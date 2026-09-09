# C5V3 R4 bound-learning audit — harness multiplicity FIX1

Date: 2026-09-10
Branch: `SIGMA_LIFE`

## Classification

The first bound-learning source audit stopped with:

```text
KERNEL_REQUIRED_d86e035aa126_COUNT=2
HOLD=KERNEL_REQUIRED_SURFACE:IF (c5a3_truth_posture_valid(posture_record) == 0) { RETURN ""; }
```

This is an **audit-harness expectation defect**, not evidence that Adapter R3 or Kernel R2 failed.

Exact Kernel R2 contains the truth-posture guard in two independent and required transitions:

```text
c5c3_revise_claim_from_posture(...)
c5c3_open_conflict_gap(...)
```

Each transition must independently reject an invalid Gate-A truth-posture record before using it. Therefore total guard multiplicity `2` is correct.

## Source identities observed by the operator

```text
STATE_SHA256=83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33
TRANSITIONS_SHA256=3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9
ADAPTER_R3_SHA256=223aeb84c4d4fcc8e1cbdbf62943a38382efa8250de72eb4df4ba3df79e5b02b
KERNEL_R2_SHA256=91d660902bc400ec967904d21aab3be876006777926dee55f7b8b2ec4f01e2f6
STATE_DEF_COUNT=28
TRANSITIONS_DEF_COUNT=12
ADAPTER_R3_DEF_COUNT=16
KERNEL_R2_DEF_COUNT=10
R4_BOUND_COMBINED_DEF_COUNT=66
MAX_DEF_ARITY=6
MULTILINE_DEF_SIGNATURE_COUNT=0
DIRECT_WRITE_TEXT_COUNT=0
DIRECT_READ_TEXT_COUNT=0
R1_AUTO_CAPABILITY_SELECT_COUNT=0
```

The audit reached all preceding source/governance checks without a source-identity or forbidden-surface failure.

## FIX1

Updated gate:

```text
C5_M5/RUN_C5V3_R4_NATIVE_LEARNING_BOUND_ADAPTER_KERNEL_SOURCE_AUDIT_R1.sh
FIX1_COMMIT=1eb0c9a3df8142f1a3c252e0ff88eaf33d2750fa
```

FIX1 changes only the evaluator/harness:

```text
locks exact Adapter R3 SHA256
locks exact Kernel R2 SHA256
requires truth-posture guard total count = 2
requires exactly one guard inside c5c3_revise_claim_from_posture
requires exactly one guard inside c5c3_open_conflict_gap
```

Adapter R3 and Kernel R2 source bytes are unchanged.

## Claim boundary

```text
R4_R2_STATIC_SOURCE_AUDIT=PASS
R4_BOUND_ADAPTER_KERNEL_SOURCE_IDENTITY=OBSERVED_MATCHING_EXPECTED_OPERATOR_OUTPUT
R4_BOUND_ADAPTER_KERNEL_STATIC_AUDIT=HOLD_HARNESS_EXPECTATION_DEFECT_PENDING_FIX1_RERUN
R4_BOUND_SOURCE_FAIL=NO_EVIDENCE
R4_RUNTIME_LEARNING=NOT_ADMITTED
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
