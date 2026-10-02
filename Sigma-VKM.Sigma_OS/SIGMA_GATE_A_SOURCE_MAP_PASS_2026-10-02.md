# SIGMA Gate A — Source Map PASS

Date: 2026-10-02
Source: user-supplied Oppo/Termux source inspection.

GATE_A_SOURCE_MAP=PASS
LIVE_MUTATION=NO
C5_HISTORICAL_MATERIALIZER_REUSED=NO
NEW_STORAGE_SILO=NO
ADMISSION=NO
CUTOVER=NO

## Exact source map

MODULE96_ACTIVE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/src/modules/96_rb_production_seed_executor.sigma

MODULE96_ACTIVE_SHA256=
269c542eeb6ec757dda7396d4afae85990f1b1729783c9df2e3a7a3e37041779

MODULE96_V2_CANDIDATE=
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/MODULE96_RESUMABLE_V2_R1/96_rb_production_seed_executor_RESUMABLE_V2_CANDIDATE_FIX1.sigma

MODULE96_V2_CANDIDATE_SHA256=
4dbfebfe20c7c0fa763db449c5ecc1fd74f42a462c8ddcf5af28055a0f79df56

MODEL_LAYOUT_MODULE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/src/modules/54_rb_model_layout.sigma

MODEL_LAYOUT_MODULE_SHA256=
ae27822512320f6535a893c80f851bdcfcedec1d9b5f64e4056e160d02b3c096

R21_TENSOR_CAS_MODULE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/src/modules/63_rb_r21_tensor_cas.sigma

R21_TENSOR_CAS_MODULE_SHA256=
7760da964efb780ae4d02275641591c1c88a60689199d163850222dc1743a80c

TOKENIZER_BINDING_MODULE=
/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/src/modules/73_rb_tokenizer_binding.sigma

TOKENIZER_BINDING_MODULE_SHA256=
78dc9490209be0a5e712be8a22351c1b1ce3db66b02a8d7fa6ff677ffdc1806c

## Existing APIs

EXISTING_API_FOR_TENSOR_CREATE=
RB_graph_model_new(profile)

EXISTING_API_FOR_TENSOR_INIT=
RB_init_tensor(...)

EXISTING_API_FOR_R21_CAS_WRITE=
RBT_store_tensor(base,t)

EXISTING_API_FOR_R21_CAS_RESTORE=
RBT_restore_into(base,t,ref)

EXISTING_API_FOR_MODEL_ENVELOPE=
RBX_checkpoint_generic(base,model,"0")

EXISTING_API_FOR_MODEL_RESTORE=
RBX_restore_generic(base,model,model_ref)

EXISTING_API_FOR_OPTIMIZER_ENVELOPE=
RBOPT_checkpoint(base,model,states)

EXISTING_API_FOR_OPTIMIZER_RESTORE=
RBOPT_restore(base,model,opt_ref)

EXISTING_API_FOR_OPTIMIZER_STEP_ZERO_SOURCE=
RBOPT_state_list_new(model)

EXISTING_API_FOR_TOKENIZER_BIND=
RBTOK_restore(base,state_ref)

EXISTING_API_FOR_TOKENIZER_STATE=
RBTOK_state(h)

EXISTING_API_FOR_TOKENIZER_PIECE=
RBTOK_piece(h)

## Optimizer modules

58_rb_training.sigma
SHA256=
58a482efb827db436b46ebcfa02a24aba02dfff7f42719f8de3ee694d96040a1

Key APIs:
- RB_adamw_state_new
- RB_adamw_step
- RB_graph_model_new
- RB_graph_param_list

61_rb_optimizer_state.sigma
SHA256=
f8e34ff05394dedaad56fe01c2329c4daee7b36955b1ad0d3c0c14c6efee7a7b

Key APIs:
- RBOPT_state_list_new
- RBOPT_step_all
- RBOPT_checkpoint
- RBOPT_restore
- RBOPT_fingerprint

## Current Gate A boundary

Gate A materialization is NOT yet PASS.

Source/API discovery is complete.

Do not scan/rebuild from historical C5.

Next implementation target:
patch candidate-only Module96 V2 using existing APIs:

RB_graph_model_new
RBOPT_state_list_new
RBX_checkpoint_generic
RBOPT_checkpoint
RBX_restore_generic
RBOPT_restore
RB_layout_tensor_count
RBTOK_restore

Target outputs:

PRODUCTION_WEIGHT_PAYLOAD_MATERIALIZED=YES
MODEL_V3_PRODUCTION_BINDING=PASS
GENERATION=0
OPTIMIZER_STEP=0

LIVE_MUTATION=NO
SERVER_SEED=NO
ADMISSION=NO
CUTOVER=NO

## Implementation constraints

- candidate-only path;
- no new model layout;
- no new optimizer format;
- no second storage silo;
- no historical C5 materializer;
- exact tokenizer epoch/state binding;
- R21 content-addressed persistence;
- fresh-process restore;
- exact replay append=0;
- fail closed on any binding or fingerprint mismatch.
