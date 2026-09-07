# VNM-04 CASE_001 — Byte Audit Localizes Failure to VNM-01 Runtime Equality Path

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: FAILURE LOCALIZED FURTHER / VNM-04 ADMISSION STILL FAIL

## Governance

This checkpoint is governed by the global native teaching/admission standard, current handoff, VNM course directive, VNM-04 source-ready checkpoint, and the preserved CASE_001 failure checkpoint.

Failure remains evidence. No PASS gate has been changed.

## Operator-supplied exact byte-audit evidence

VNM-04 native candidate/counts:

```text
CANDIDATE_FORM_A=điện-252519012895220536
CANDIDATE_FORM_B=dien-252519012895220536
ELIGIBLE_EVIDENCE_COUNT=2
SUPPORT_PAIR_COUNT=2
COMPETING_RAW_PAIR_COUNT=0
```

VNM-04 native bundle:

```text
HYPOTHESIS||VNM04:điện-252519012895220536:dien-252519012895220536||FORM_A||điện-252519012895220536||FORM_B||dien-252519012895220536
EVIDENCE||VNM04:S11:1:S12:1||điện-252519012895220536||dien-252519012895220536||SOURCE||SRC-252519012895220536-1&SRC-252519012895220536-2
EVIDENCE||VNM04:S13:1:S14:1||điện-252519012895220536||dien-252519012895220536||SOURCE||SRC-252519012895220536-3&SRC-252519012895220536-4
```

Mechanically routed VNM-01 inputs contain exactly those records.

```text
BUNDLE_LINE1_EQUALS_HYPOTHESIS=YES
BUNDLE_LINES2N_EQUALS_EVIDENCE=YES
```

Therefore:

```text
VNM04_NATIVE_OUTPUT_CONTAINS_EXPECTED_CANDIDATE_PAIR=YES
VNM04_SUPPORT_PAIR_COUNT_AGREES_WITH_BUNDLE=YES
RUNNER_ROUTING_BYTE_EQUALITY=PASS
HOST_ROUTING_TRANSFORMED_SEMANTIC_CONTENT=NO
```

## Downstream native contradiction

On these exact routed bytes, admitted VNM-01 runtime emitted:

```text
VM_RC=0
HYPOTHESIS_VALID=1
FORM_A=điện-252519012895220536
FORM_B=dien-252519012895220536
NEW_EVIDENCE_LINE_COUNT=2
NEW_SUPPORT_COUNT=0
NEW_COMPETING_COUNT=2
WEIGHT_BEFORE=0
PROPOSED_WEIGHT=-2
WEIGHT_AFTER=-2
```

Canonical VNM-01 source defines exact pair in either direction as `SUPPORT` before candidate-member competing checks.

The byte audit therefore excludes the previously open VNM-04 output and shell routing explanations.

## Updated failure localization

```text
VNM04_NATIVE_OUTPUT_DEFECT=EXCLUDED_BY_CASE001_FAILED_BYTES
RUNNER_ROUTING_DEFECT=EXCLUDED_BY_BYTE_EQUALITY
VNM01_INPUT_PARSE_ACCEPTED=YES
VNM01_PERSISTENCE_PATH_WORKED=YES
VNM01_RUNTIME_PAIR_CLASSIFICATION_CONTRADICTS_EXPECTED_EXACT_PAIR_PATH=YES
FAILURE_CLASS=DOWNSTREAM_VNM01_RUNTIME_EQUALITY_OR_FUNCTION_CALL_PATH_UNRESOLVED
```

Do not yet claim compiler or VM defect. Remaining possibilities include:

- runtime string/value equality behavior on the exact parsed fields;
- compiler lowering / function argument binding on this path;
- a VNM-01 source-level runtime logic interaction not exposed by static reading.

## Required diagnostic before repair

Do not modify admitted VNM-01 or VNM-04 source yet.

Run a separate read-only native diagnostic under the locked compiler/VM on exact copies of the failed CASE_001 hypothesis/evidence bytes. It must print:

```text
INLINE_OBS_A_EQ_FORM_A
INLINE_OBS_B_EQ_FORM_B
INLINE_OBS_A_EQ_FORM_B
INLINE_OBS_B_EQ_FORM_A
INLINE_PAIR_CONCAT_EQ
CANDIDATE_MEMBER_OBS_A
CANDIDATE_MEMBER_OBS_B
RELATION_CLASS_FUNCTION
```

Interpretation only after machine evidence:

```text
inline exact equality PASS + relation_class COMPETING
-> function-call/compiler-lowering path suspected

inline exact equality FAIL on byte-identical source fields
-> runtime parsed string/value equality path suspected

inline equality + relation_class both SUPPORT
-> discrepancy is specific to full VNM-01 execution context and requires further localization
```

Diagnostic source/runner are separate artifacts and must not mutate failed case or production state.

```text
VNM04_ADMISSION=FAIL
FULL_73_INVOCATION_ADMISSION=NOT_COMPLETED
FAIL_LOCAL_FIX_MINIMAL=YES
RERUN_FULL_REQUIRED_SUITE_AFTER_FIX=YES
WEAKEN_GATE_TO_FORCE_PASS=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```
