# DNA-15 V2 FIX1 H-FREE STATE-DERIVED-K — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Prior evidence

V2 runtime failed and remains historical evidence:

```text
SOURCE_SHA256=94f4684115d03116bff19348ce840457f5c066d2399c7f83dd3f5b9ecfd24f26
BYTECODE_SHA256=c44a85358c4ab0fd7ca5fd71f328575859bf16b7dfdffca516f15620eeb26f76
TOTAL_VM_INVOCATIONS=50
POST_VM_ALIGNMENT_PASS_COUNT=45
POST_VM_ALIGNMENT_FAIL_COUNT=5
POST_VM_NUMERIC_ALIGNMENT_PASS_COUNT=48
POST_VM_NUMERIC_ALIGNMENT_FAIL_COUNT=2
VM_NONZERO_COUNT=0
ADMISSION=FAIL
```

Failure checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260905_DNA15_V2_FAIL_45_OF_50_AND_FIX_SCOPE.md`

## FIX1 exact repair

Native source delta from V2 is exactly one semantic emission line:

```text
MEASUREMENT_COMPLETE:
- INPUT_BINDING_VALID
+ REQUIRED_FIELDS_PRESENT
```

This keeps measurement-field completeness distinct from dependency validity.

Runner numeric-oracle repair:
- for `domain=0` with `input_valid=1`, expected `TIME_OFFSET` is now the parsed `t-t0`;
- all k/log/exp/reconstruction outputs remain zero/blocked when the positive-A derivation domain is invalid.

No active-design rollback:
- H remains unread by native source;
- caller-k remains unread by native source;
- k formula remains `ln(A_t/A0)/(t-t0)^2`;
- F174 reconstruction remains `A0*exp(k*(t-t0)^2)`.

## Artifact

SOURCE_PATH=DNA15_F174_HFREE_STATE_DERIVED_K_NATIVE_V2.sigma
SOURCE_SHA256=e0ac36559b85a189152709238e176a99e48f325f3f1308aba8b360a768e74d8f
RUNNER_PATH=run_DNA15_NATIVE_ADMISSION_V2_FIX1.sh
RUNNER_SHA256=560d93d0d4b3c921f3874218104d85c329bfae7d8e8004d047a0374e0ffb17dc
MANIFEST_SHA256=1d475b2111a654404c3300cbf0ed3fa0bcae79107063bcb3adf54a20eba42de9
BUNDLE_SHA256=c668eecbf7e0e9b17106bba8caabe4881b765de862263b2895221a8379298071
CANON_REFERENCE_BLOB_SHA1=50ec4940f554d594c385a96ef986fc88dca7f53c

## Static audit

```text
MIDFILE_HASH_COMMENT_COUNT=0
RUNNER_PYTHON_COMMAND_COUNT=0
H_INPUT_PATH_READ_COUNT=0
CALLER_K_INPUT_PATH_READ_COUNT=0
MEASUREMENT_COMPLETE_EMISSION=REQUIRED_FIELDS_PRESENT
BASH_SYNTAX=PASS
MANIFEST=PASS
ZIP_INTEGRITY=PASS
```

## Admission state

```text
DNA15_V2_FIX1_SOURCE=SOURCE_ONLY
DNA15_V2_FIX1_COMPILE=NOT_RUN
DNA15_V2_FIX1_VM=NOT_RUN
DNA15_V2_FIX1_ADMISSION=NOT_RUN
STATE_DERIVED_K=NOT_ADMITTED
MATH_LOG_ABI=NOT_ADMITTED
K_TEMPORAL_CONSTANCY=NOT_PROVEN
```

Full 50-case rerun is required. Static repair is not runtime capability evidence.
