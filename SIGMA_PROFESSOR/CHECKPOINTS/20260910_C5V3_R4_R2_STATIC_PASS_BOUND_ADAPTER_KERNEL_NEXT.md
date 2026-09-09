# C5V3 — R4 R2 static PASS / bound adapter+kernel next

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## R4 R2 machine static result

Operator output established:

```text
STATE_SHA256=83a43ed6e778775c4b0ea823fa1ab4179adfccbf8a0478c2a7e4a9f8cfd5af33
STATE_IDENTITY=PASS
TRANSITIONS_SHA256=3273a9d6e09728882244e5428cac994d505f58b1e54b69c2fb009a6a714bb3e9
TRANSITIONS_IDENTITY=PASS
ADAPTER_SHA256=43e22c9b9140dfb0b1882d34d85ffd1e460854f20bd61420f93098052cd0aa89
ADAPTER_IDENTITY=PASS
R4_R2_COMBINED_SHA256=84d064435fdba01ccd6c700f5efd266b39e297f51fedc7cfddbf9c05489fe209
STATE_DEF_COUNT=28
TRANSITIONS_DEF_COUNT=12
ADAPTER_DEF_COUNT=12
R4_R2_COMBINED_DEF_COUNT=52
MAX_DEF_ARITY=6
MULTILINE_DEF_SIGNATURE_COUNT=0
EXACT_SCHEMA_FIELD_PARSE=PASS
SAFE_ATOM_EQUALS_REJECTION=PASS
NATIVE_SUPPLIED_CAPABILITY_ID_REQUIRED=PASS
R4_R2_STATIC_GOVERNANCE=PASS
R4_R2_SOURCE_AUDIT=PASS
RUNTIME_ADMISSION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

The 52-DEF R2 base is therefore a valid static source substrate in exactly this tested scope.

## Pre-runtime semantic-binding review

Before composition/runtime admission, two additional defects were found in the R2 adapter/kernel path:

1. adapter R2 mapped opposite-side source evidence to `NEUTRAL` rather than `CONTRARY`;
2. kernel R1 did not bind `evidence.SUBJECT_ID` to `claim.SUBJECT_ID` and accepted an unbound raw source-stance argument.

These are source architecture defects found before runtime. They do not invalidate the R2 static PASS, but they prevent R2 adapter/kernel from becoming the runtime target.

## Corrected bound-learning target

### Gate-A adapter R3

```text
PATH=C5_M5/R4_NATIVE_LEARNING/C5_GATEA_R4_LEARNING_ADAPTER_R3.sigma.inc
COMMIT=02bb0c6d60f2568583211b16baa8fbbd3de0e77f
DEF_COUNT=16
```

Corrections:

```text
A evidence vs B claim -> CONTRARY
B evidence vs A claim -> CONTRARY
INCONSISTENT/NONE -> NEUTRAL
source stance is materialized as a source-ID-bound native record
truth posture is materialized from Gate-A ledgers inside native SIGMA
```

### One-cycle kernel R2

```text
PATH=C5_M5/R4_NATIVE_LEARNING/C5_R4_ONE_CYCLE_LEARNING_KERNEL_R2.sigma.inc
COMMIT=b3fc9cfa25a4cd09bca98e4f5718d76c637f1259
DEF_COUNT=10
```

Corrections:

```text
claim subject == evidence subject required
stance record source ID == evidence source ID required
claim revision consumes a Gate-A truth-posture record
conflict-gap opening consumes the same native truth-posture record
```

## New composition shape

```text
28 State R2
12 Transitions R2
16 Adapter R3
10 Kernel R2
= 66 DEF bound-learning source surface
```

No runtime-learning PASS is claimed yet.

## Exact next machine gate

```text
C5_M5/RUN_C5V3_R4_NATIVE_LEARNING_BOUND_ADAPTER_KERNEL_SOURCE_AUDIT_R1.sh
SCRIPT_COMMIT=cc1dc106d169a698c9f413dca38332422b7ba97b
```

The gate checks exact R2 base identities and commit-binds adapter R3/kernel R2, then statically verifies:

```text
CONTRARY evidence mapping
claim/evidence subject binding
stance/evidence source binding
internal Gate-A truth posture
no direct I/O
no LEFT/RIGHT or legacy learner
no automatic capability selection
max arity <= 6
no multiline DEF signature
```

After PASS, write the transaction-aware R4 cycle main under P0 trust semantics, then compose with exact Gate-A pure donor and exact admitted T1/T2/T3.

## Claim boundary

```text
R4_R2_STATIC_SOURCE_AUDIT=PASS
R4_BOUND_ADAPTER_KERNEL_SOURCE=WRITTEN
R4_BOUND_ADAPTER_KERNEL_STATIC_AUDIT=PENDING
R4_RUNTIME_LEARNING=NOT_ADMITTED
GENERAL_SEMANTIC_LEARNING=NOT_PROVEN
WHOLE_WORK_UNDERSTANDING=FAIL
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
