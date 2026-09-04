# DIRECTOR-W01 — Status Report

## Current stage

`CURRICULUM`

No later pipeline stage is unlocked.

## Director-accepted academic scopes

### B1.1-C01 — Logic, tập hợp và chứng minh

Accepted commit:
`5659288da80a239e2ded408da87348670c1410c2`

C01 was repaired before acceptance and remains the canonical prerequisite for generic logic, set, relation/function and proof foundations.

### B1.1-C02 — Số học và lý thuyết số

Director-accepted commit:
`cfd9746e2296280705e2e2e67b2c5980d440f02d`

Independent Director audit confirmed:

- 8/8 canonical topics, 8 nodes;
- 64/64 claims reviewed;
- 7/7 persistent/versioned sources reviewed and deterministic IDs verified;
- 32/32 Learning Objectives have explicit supporting Claim IDs;
- zero future/unlocked support claims;
- 15 cross-links with no primary ownership transfer;
- prerequisite/sequence graph PASS;
- stage boundary PASS;
- NIST SP 811 round-to-even claim verified;
- the `a!=0` divisibility definition was rechecked and treated as an explicitly declared convention difference, not a blocker.

C02 is `DIRECTOR_ACCEPTED_PASS` and must not be re-authored casually.

## Active work

Only active child:
`C01-W02-B1.1-MATH-FAMILY-C03`

Scope:
`B1.1-C03 — Đại số và cấu trúc`

Execution branch:
`hka-tree/c01-w02-math-c03`

Pinned predecessor:
`cfd9746e2296280705e2e2e67b2c5980d440f02d`

Canonical topics:

1. Biểu thức và phương trình
2. Bất phương trình
3. Hàm và quan hệ
4. Đại số tuyến tính
5. Ma trận và không gian vectơ
6. Nhóm
7. Vành và trường
8. Đại số giao hoán
9. Lý thuyết biểu diễn

## Mandatory C03 risk controls

- C03 T03 must not duplicate C01 generic relation/function foundations.
- C03 T01/T02 must not duplicate C02 arithmetic/order foundations.
- T04/T05 must establish one primary owner per linear-algebra/matrix/vector-space proposition and objective, especially systems, vector spaces, span/independence, basis/dimension, matrices, linear maps, rank/nullity, determinants and eigen concepts.
- T06/T07/T08/T09 must form a prerequisite/specialization hierarchy rather than repeat shared algebraic-structure content.
- 100% Claim → Learning Objective closure remains mandatory.
- Future locked scopes may be boundary references only, never support claims.

## Durable activation

- Control-plane state activation: `54e9f7867e44dbcbef4744dfc6a8246f38566048`
- Window registry activation: `09d379c8747bce087dbbe0944bb7c096b220b39a`
- C03 contract: `2aee98b0bf17eb23fa0af5969d816c6408c03d5e`
- C03 execution prompt: `0037ccf9f1c0ad8ea9de5a53570962214cd92b83`
- C03 Director open order: `55034606c0c182a3082b082b7018836ca5efc029`
- C03 bootstrap checkpoint: `a5ac5945ccdc4db8ee2647a15399d1fbfb734877`
- Director checkpoint: `12b33ee81fb84e1c7bca7cc48c0ae4c189cc349a`

## Locked rules

- `NO STATUS FOLDER = NO ACCEPTED COMPLETION`.
- Chat memory is not project state.
- Worker PASS is only a candidate until independent Director acceptance.
- C04 and later scopes remain locked until C03 is accepted.
- No Lesson Registry, prompts, images, R2, delivery, website or `ACADEMIC_LOCKED` artifacts during CURRICULUM.

## Next action

Run only `C01-W02-B1.1-MATH-FAMILY-C03` from `DIRECTOR_OPEN_ORDER.md` and `GPT_EXECUTION_PROMPT.md` on `hka-tree/c01-w02-math-c03`.
