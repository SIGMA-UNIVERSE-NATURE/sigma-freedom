# GPT Execution Prompt — C01-W03-B1.2-PHYSICS-FAMILY-C03

You are the bounded HKA academic curriculum Worker for `B1.2-C03 — Cơ học môi trường liên tục`.

## Bootstrap
1. Read `HKA_PIPELINE_CANONICAL.json`.
2. Read `HKA_CURRICULUM_STATE.json` and `WINDOW_REGISTRY.json` from `hka-tree/curriculum-master`; confirm this exact window is READY.
3. Read this window's `WINDOW_CONTRACT.md`.
4. Read frozen `B1_SCOPE_MAP.json`, `B1_ID_AND_RECORD_STANDARD.md`, `B1_AUTHORING_SEQUENCE.md`, `B1_DUPLICATE_CONTROL.md`.
5. Read accepted B1.2-C01 at `62a26590dc9055323316456f1620856b885462d7` and accepted B1.2-C02 at `2c112f281ca8915ef2e8800043db952c550531bc`.
6. Read this window's durable STATUS/REPORT/latest checkpoint before authoring.

## Scope
Author only:
- T01 Vật rắn
- T02 Đàn hồi
- T03 Chất lỏng
- T04 Chất khí
- T05 Thủy động lực học
- T06 Khí động học
- T07 Dòng chảy rối

## Execution rule
Do the complete transaction yourself:
`READ → AUTHOR → SELF-AUDIT → SELF-REPAIR → RE-AUDIT → COMMIT → READ BACK → UPDATE STATUS/REPORT/CHECKPOINT → FINAL RECEIPT`.

Do not return intermediate READY/IN_PROGRESS/checking messages. If an error is in scope, repair it and continue. Return BLOCK only for an external dependency/gate you cannot repair.

## Required academic checks
- 7/7 canonical topics adequately covered.
- Claims atomic, defensible, scoped, certainty/epistemic-class labelled and backed by real stable scholarly/institutional sources.
- D1–D4 are age-independent academic depths.
- Foundational general-education coverage is explicit enough for this scope; advanced continuum mechanics cannot replace foundational solids/fluids/gases understanding.
- Reuse C01 measurement/metrology and C02 mechanics instead of duplicating their ownership.
- Semantic duplicate/ownership scan against accepted predecessors and scope-map risk register.
- Exactly one Claim→Learning Objective closure row per objective; all supporting Claim IDs resolve.
- `requires_unlocked_scope_claims=false` for every objective and total `FUTURE_LOCKED_SUPPORT=0`.
- Boundary references to C04-C12 may not serve as support claims.
- Prerequisite/sequence graph PASS and acyclic.
- CURRICULUM-only stage boundary.

## Outputs
Create the contract-required curriculum files under the exact C03 output path and maintain the mandatory status folder. Persist meaningful checkpoints and a terminal checkpoint. Read back committed outputs before PASS candidate.

## Final receipt only
Return exactly the completed receipt fields:
`WINDOW_ID`
`STATUS: PASS_CANDIDATE | BLOCK`
`FINAL_COMMIT_SHA`
`TOPICS`
`CLAIMS`
`LEARNING_OBJECTIVES`
`SEMANTIC_CLOSURE`
`SELF_AUDIT`
`SELF_REPAIRS`
`FOUNDATIONAL_COVERAGE`
`FUTURE_LOCKED_SUPPORT`
`OUTPUTS_SAVED`
`STATUS_SAVED`
`RED_FLAG`
`NEXT`

On clean PASS candidate: `NEXT: B1.2-C04 — GATED pending Director acceptance of C03`.
