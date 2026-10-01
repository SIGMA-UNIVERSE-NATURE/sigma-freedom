# SIGMA B8 — PREPARE V2 Double-Traversal Diagnosis + Accelerator Plan

Date: 2026-10-01
Type: master diagnosis / coordination contract
Source: user-supplied current analysis and recovery pointer.

## Root cause diagnosis

Current PREPARE traverses the tokenizer piece-chain twice:

1. RBTOK_restore(base,t32)
2. A second full traversal of s32.head to rebuild known/ids, restoring and SHA-verifying each piece again.

At epoch 11 there are 11,264 custom pieces, so this duplicates O(vocab) work.

Current diagnosis:
- stats persistence is not the primary bottleneck;
- duplicated tokenizer piece-chain traversal is the primary PREPARE cost.

## Constraint

Do NOT solve by permanently raising production step ceiling.

Production target remains:

SIGMA_MAX_STEPS=10000000

ONE_SIGMA=YES

## PREPARE V2 target

RBTOK_restore
-> one authoritative validation pass
-> native tokenizer_has_bytes()
-> candidate loop over selected 1024 pieces
-> no second full piece-chain scan

Historical B7 module 87 must not be mutated for this repair.
Use a new module/path for PREPARE V2.

## Immediate verification before patch

Before modifying PREPARE, inspect the exact implementations of:
- RBTOK_restore
- RBTOK_piece
- RBTOK_state
- tokenizer host structures
- tok_add_piece / tok_add_bytes
- tokenizer_add_bytes
- tokenizer_token_bytes

Purpose:
preserve every validation currently performed by RBTOK_restore and remove only the redundant second traversal.

## Recovery authority

Recovery pointer must remain unchanged:

EXPECTED_MODE=STATE

EXPECTED_REF=
4bb9e0900bfdbcaf47fee49960618a76

Do not advance or replace this state pointer until the PREPARE V2 repair is proven.

## Long-term tokenizer accelerator

Authoritative design:

authoritative R21 piece chain
-> single derived packed tokenizer snapshot
-> native bulk restore
-> PREPARE cost approximately selected/stats work

Goal:
restore cost must not grow linearly with 11k -> 50k -> 100k pieces during ordinary production PREPARE.

The accelerator is derived/rebuildable.
The authoritative R21 piece chain remains source of truth.

## Bootstrap exception

A one-time bootstrap operation may use a higher temporary step budget if strictly required to construct the derived accelerator.

That exception must NOT redefine production runtime limits.

Production returns to:

SIGMA_MAX_STEPS=10000000

## Learning-efficiency principle

MEASURE ONCE
PERSIST ONCE
VERIFY FRESH ONCE

Avoid:

MEASURE
-> redundant same-process verification
-> repeated profile-32B verification
-> repeated profile-70B traversal
-> another fresh verification of already-authoritative knowledge

Guiding principle:

INCREASING KNOWLEDGE, NOT INCREASING WASTE FOR LEARNING.

## Non-negotiable invariants

ONE_SIGMA=YES

32B_UNCHANGED=YES
70B_UNCHANGED=YES
VOCAB_CAPACITY=131072

SIGMA_MAX_STEPS=10000000

HOST_SELECTION=NO
HOST_STOP_POLICY=NO

LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO

## Boundary

This document records the diagnosis and repair plan only.

It does NOT establish:
- PREPARE V2 PASS;
- tokenizer accelerator PASS;
- growth-to-stop completion;
- production tokenizer qualification;
- admission;
- cutover.
