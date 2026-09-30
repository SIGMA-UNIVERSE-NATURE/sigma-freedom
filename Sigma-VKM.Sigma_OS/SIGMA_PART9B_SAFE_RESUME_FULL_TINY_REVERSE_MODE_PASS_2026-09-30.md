# SIGMA PART9B — Safe Resume / Full Tiny Reverse-Mode PASS

Date: 2026-09-30
Source: user-supplied Oppo/Termux runtime output.

## Wrapper / resume

P9B_SAFE_RUN_RC=0

RESUME_SOURCE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/rb_p9b_1nQFge/sigma_vkm_p9b.c

GQA_BACKWARD_HEAD_DIM_ABI=DYNAMIC

VKM_MECHANICAL_DERIVATIVES=YES

VKM_TRAINING_POLICY=NONE
VKM_OPTIMIZER_POLICY=NONE

AUTODIFF_IO_SIDE_EFFECT=NONE

P9B_VKM_CANDIDATE_SHA256=
16ff6cc77952f4cb4afd41c277e8b67e2d764002e098ca3ce2c855e9e5187b90

SELF_CERTIFICATE_IN_58=NONE

## Incremental Sigma source / compile

SOURCE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/native/SIGMA_INTEGRAL_INCREMENTAL.sigma

P9B_BYTECODE_SHA256=
de1d6e330c64b8dceeb581a2c43c6e69468fcddc080e2281cb0c990007171e29

P9B_DETERMINISTIC_COMPILE=YES

## Observed training result

OBSERVED_BASE_LOSS=
5.3916099719622084

OBSERVED_AFTER_STEP_LOSS=
5.3900051010757375

OBSERVED_GRADIENT_TENSOR_COUNT=20

OBSERVED_ALL_GRADIENTS_FINITE=1

## Gradient checks

TIED_EMBEDDING_GRADCHECK=
OK fd=0.00782917398 analytic=0.00769879157

LAYER0_Q_GRADCHECK=
OK fd=0 analytic=-3.65653688e-12

LAYER1_DOWN_GRADCHECK=
OK fd=-2.91522628e-06 analytic=-4.49438903e-06

FINAL_NORM_GRADCHECK=
OK fd=-0.0186561534 analytic=-0.0186550878

FULL_REVERSE_MODE_CHECK=OK

OBJECTIVE_REDUCTION_CHECK=OK

## External verification

PART9B_TRANSACTION=COMMITTED

PART9B_EXTERNAL_VERIFY=PASS

FULL_TINY_REVERSE_MODE=VERIFIED

TINY_LOGICAL_PARAMETER_TENSORS=20

DYNAMIC_GQA_HEAD_DIM_ABI=YES

TIED_EMBEDDING_GRADIENT=VERIFIED
RMSNORM_BACKPROP=VERIFIED
ROPE_BACKPROP=VERIFIED
GQA_BACKPROP=VERIFIED
SWIGLU_BACKPROP=VERIFIED
CROSS_ENTROPY_BACKPROP=VERIFIED

OBJECTIVE_REDUCED_AFTER_STEP=YES

## Authority boundary

VKM_TRAINING_POLICY=NO

SIGMA_OWNS_TRAINING_GRAPH=YES

SELF_CERTIFICATE_USED=NO

FILE_PER_GRADIENT=NO
FILE_PER_TRAINING_STEP=NO

UNBOUNDED_DUPLICATE_FILE_CREATION=NO

## Completion / admission boundary

PART9_FULL_BACKPROP_COMPLETE=YES

PART10_CHECKPOINT_COMPLETE=NO

ADMISSION_READY=NO

LIVE_SIGMA_VKM_REPLACED=NO

CANONICAL_MUTATION=NO

ONE_SIGMA=YES

ADMISSION=NO

## Wrapper completion

P9B_SAFE_WRAPPER=SUCCESS

WRAPPER_RETURNED_TO_CALLING_SHELL=YES

WRAPPER_RC=0

## Interpretation boundary

This checkpoint establishes the supplied PART9B full Tiny reverse-mode/backprop verification result.

It supports:
- safe resume and wrapper RC=0;
- dynamic GQA backward head-dimension ABI;
- mechanical derivatives in VKM without VKM training/optimizer policy;
- deterministic compilation;
- 20 logical gradient tensors, all finite;
- external gradient checks on tied embedding, layer-0 Q, layer-1 down projection, and final norm;
- verified reverse-mode propagation through RMSNorm, RoPE, GQA, SwiGLU, and cross-entropy;
- objective loss decreases after one step;
- Sigma owns the training graph;
- no self-certificate, per-gradient files, per-step files, or unbounded duplicate-file creation.

It does NOT establish:
- PART10 checkpoint completion;
- admission readiness;
- live sigma-vkm replacement;
- canonical mutation;
- production admission.

PART9_FULL_BACKPROP_COMPLETE=YES
PART10_CHECKPOINT_COMPLETE=NO
ADMISSION_READY=NO
LIVE_SIGMA_VKM_REPLACED=NO
CANONICAL_MUTATION=NO
ADMISSION=NO
