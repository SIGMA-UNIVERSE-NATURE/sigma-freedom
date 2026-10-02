# SIGMA Production Layout / CAS / Tokenizer Epoch 83 Checkpoint

Date: 2026-10-02
Source: user-supplied Oppo/Termux runtime output.

## RealBrain layout

RB_layout_tensor_count(profile) = 2 + 9 * RB_layout_layers(profile)

SIGMA_RB_TINY:
- vocab = 256
- d_model = 8
- layers = 2
- d_ff = 16

SIGMA_RB_32B:
- vocab = 131072
- d_model = 7168
- layers = 60
- d_ff = 18944
- tensor_count = 542

SIGMA_RB_70B:
- vocab = 131072
- d_model = 8192
- layers = 80
- d_ff = 28672
- tensor_count = 722

q_width = heads * head_dim
kv_width = kv_heads * head_dim

## R21 tensor CAS byte semantics

RBT_nbytes(t) =
RB_tensor_numel(t) * RBT_dtype_size(RB_tensor_dtype(t))

RBT_chunk_bytes = 61440
RBT_leaf_fanout = 1024
RBT_max_leaves = 1024

## Expected production parameter footprint

PROFILE=SIGMA_RB_32B
PARAMETERS=32429128704
TENSOR_COUNT=542
BF16_PARAMETER_BYTES=64858257408
BF16_PARAMETER_GIB=60.404

PROFILE=SIGMA_RB_70B
PARAMETERS=69526102016
TENSOR_COUNT=722
BF16_PARAMETER_BYTES=139052204032
BF16_PARAMETER_GIB=129.502

## Current tokenizer state supplied

TOKENIZER32=
445ba2b30e6d68a108d964a47c2bfcff

TOKENIZER70=
0480b3b124889b4b0ccf33621ba5f6fc

TOKENIZER_EPOCH=83

READY_FOR_6_AUTOLEARN_CORPORA=NO

CALLING_SHELL_STILL_ALIVE=YES

## Boundary

This checkpoint establishes the current source-reported production layout formulas, expected BF16 parameter footprint, R21 tensor-CAS byte semantics, and tokenizer states at epoch 83.

It does NOT establish:
- production 32B/70B weight payload materialization;
- Model V3 production binding;
- readiness for six AutoLearn corpora;
- admission;
- cutover.

The tokenizer epoch/state values are supplied runtime evidence and should be treated as current only to the extent they were measured directly on Oppo in this output.
