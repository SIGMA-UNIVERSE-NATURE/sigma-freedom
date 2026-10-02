# SIGMA Gate A — New Coder Source Handoff

Date: 2026-10-02
Type: coordination / source handoff

## Coder report accepted

The repo archive contains historical/current checkpoint evidence but does not by itself contain all active Oppo runtime source required to implement Gate A production weight materialization.

The coder must NOT fall back to historical C5 materializers marked PRODUCTION_BINDING=NO.

The coder must NOT restart from zero.

## Active Oppo source root

Use the existing Oppo workspace:

CORE="$HOME/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1"

Active RealBrain module directory:

"$CORE/src/modules"

## Mandatory source set to inspect

1. Production seed executor currently installed:

"$CORE/src/modules/96_rb_production_seed_executor.sigma"

2. Module96 V2 resumable candidate already prepared:

"$HOME/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/MODULE96_RESUMABLE_V2_R1/96_rb_production_seed_executor_RESUMABLE_V2_CANDIDATE_FIX1.sigma"

3. Module96 V2 link plan:

"$HOME/SIGMA_R7_NEXT_R1/VKM/SIGMA_AUTOLEARN_ADMIN/MODULE96_RESUMABLE_V2_R1/module96_v2_candidate_link_precheck/MODULE96_V2_LINK_PLAN.env"

4. Model layout source:

"$CORE/src/modules/54_rb_model_layout.sigma"

Required known functions:
- RB_layout_tensor_count
- RB_layout_vocab
- RB_layout_d_model
- RB_layout_layers
- RB_layout_q_width
- RB_layout_kv_width
- RB_layout_d_ff

5. R21 tensor CAS source:

Locate the active module containing:
- RBT_nbytes
- RBT_chunk_bytes
- RBT_leaf_fanout
- RBT_max_leaves

The previously inspected active source was module 63.

Do not substitute historical C5 storage code.

6. Tokenizer production binding source:

Use the active module containing:
- RBTOK_restore
- RBTOK_piece
- RBTOK_state

The previously inspected active source was:

"$CORE/src/modules/73_rb_tokenizer_binding.sigma"

Current measured tokenizer checkpoint supplied:

TOKENIZER_EPOCH=83
TOKENIZER32=445ba2b30e6d68a108d964a47c2bfcff
TOKENIZER70=0480b3b124889b4b0ccf33621ba5f6fc

7. Optimizer layout/state

Locate the active module(s) providing current RealBrain optimizer descriptor/state and AdamW persistence.

Required contract already proven:
- ADAMW_M=F32
- ADAMW_V=F32
- ADAMW_ARITHMETIC=F32
- ADAMW_GRAD_HANDOFF=F32
- optimizer step persistence
- model/optimizer fresh restore
- exact replay append=0

Do not invent a new optimizer format.

## GitHub evidence to read before editing

- Sigma-VKM.Sigma_OS/SIGMA_PART5_REALBRAIN_MODEL_LAYOUT_HOLD_FIX_PASS_2026-09-30.md
- Sigma-VKM.Sigma_OS/SIGMA_C2_2_R21_TENSOR_CAS_PASS_2026-10-01.md
- Sigma-VKM.Sigma_OS/SIGMA_C2_3_MODEL_OPTIMIZER_R21_CAS_PASS_2026-10-01.md
- Sigma-VKM.Sigma_OS/SIGMA_C2_6C2C4A_TOKENIZER_BINDING_PASS_2026-10-01.md
- Sigma-VKM.Sigma_OS/SIGMA_REALBRAIN_OPTIMIZER_STATE_V1_PASS_2026-10-01.md
- Sigma-VKM.Sigma_OS/SIGMA_RB_PRODUCTION_SEED_PLAN_PASS_2026-10-02.md
- Sigma-VKM.Sigma_OS/SIGMA_RB_PRODUCTION_SEED_EXECUTOR_INSTALL_PASS_2026-10-02.md
- Sigma-VKM.Sigma_OS/SIGMA_PRODUCTION_SERVER_BUNDLE_V2_PASS_2026-10-02.md
- Sigma-VKM.Sigma_OS/SIGMA_FINAL_CUTOVER_FINGERPRINT_MATRIX_2026-10-02.md

GitHub is continuity/archive only; Oppo source/runtime remains the active implementation basis.

## Immediate Gate A task

Do not create receipts or labels first.

Read the active sources above and identify the exact existing APIs necessary to materialize one production tensor payload through R21 CAS under the current Model V3/optimizer/tokenizer contracts.

First deliverable should be a SOURCE/API MAP, not a new architecture.

Required output:

GATE_A_SOURCE_MAP=PASS

MODULE96_ACTIVE=<path/hash>
MODULE96_V2_CANDIDATE=<path/hash>
MODEL_LAYOUT_MODULE=<path/hash>
R21_TENSOR_CAS_MODULE=<path/hash>
TOKENIZER_BINDING_MODULE=<path/hash>
OPTIMIZER_MODULES=<paths/hashes>

EXISTING_API_FOR_TENSOR_CREATE=<symbol>
EXISTING_API_FOR_R21_CAS_WRITE=<symbol>
EXISTING_API_FOR_MODEL_ENVELOPE=<symbol>
EXISTING_API_FOR_OPTIMIZER_ENVELOPE=<symbol>
EXISTING_API_FOR_TOKENIZER_BIND=<symbol>

C5_HISTORICAL_MATERIALIZER_REUSED=NO
NEW_STORAGE_SILO=NO
NEW_MODEL_LAYOUT=NO
NEW_OPTIMIZER_FORMAT=NO

LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO

Only after this source/API map is verified should the coder patch or implement the smallest missing Gate A materialization path.

## Hard stop conditions

BLOCKED_SAFE if:
- active Oppo source files are actually missing;
- current Module96 V2 candidate cannot be located;
- R21 CAS API cannot represent required payload;
- tokenizer binding cannot be tied to current state;
- optimizer/model envelope contract is ambiguous.

Do not compensate by rebuilding from C5 or inventing new infrastructure.

ONE_SIGMA=YES
