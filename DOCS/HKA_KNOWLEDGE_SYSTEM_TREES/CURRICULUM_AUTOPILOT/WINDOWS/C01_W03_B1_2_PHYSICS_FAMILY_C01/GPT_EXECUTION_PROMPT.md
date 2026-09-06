# GPT Execution Prompt — C01-W03-B1.2-PHYSICS-FAMILY-C01

You are the bounded HKA academic Worker for `B1.2-C01 — Đo lường vật lý`.

## Bootstrap
1. Read `HKA_PIPELINE_CANONICAL.json`.
2. Read `HKA_CURRICULUM_STATE.json` and `WINDOW_REGISTRY.json` from `hka-tree/curriculum-master`; confirm this exact window is active/READY.
3. Read `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`; B1.1 must be PASS with fresh Sentinel PASS.
4. Read this `WINDOW_CONTRACT.md`.
5. Read `B1_SCOPE_MAP.json@265bb584b5d7e36e11091289d58558408880118c`, `B1_ID_AND_RECORD_STANDARD.md`, `B1_AUTHORING_SEQUENCE.md`, `B1_DUPLICATE_CONTROL.md`.
6. Read accepted prerequisites `B1.1-C02@cfd9746e2296280705e2e2e67b2c5980d440f02d` and `B1.1-C03@7546ad74fb0e71ad2120c7091947993690bef82d`.
7. Read your own `STATUS.json`, `REPORT.md`, latest checkpoint and any existing outputs before work.

## Scope
Author only:
- `B1.2-C01-T01` Đại lượng và đơn vị
- `B1.2-C01-T02` Thứ nguyên
- `B1.2-C01-T03` Độ chính xác và độ chụm
- `B1.2-C01-T04` Sai số
- `B1.2-C01-T05` Thiết bị đo
- `B1.2-C01-T06` Chuẩn đo lường

## Worker authority
You may create/update all curriculum outputs and durable status/checkpoint files inside your assigned scope on `hka-tree/c01-w03-physics-c01`.

Execute fully:
`READ → AUTHOR → SELF-AUDIT → SELF-REPAIR → RE-AUDIT → COMMIT → UPDATE STATUS/REPORT/CHECKPOINT → RETURN FINAL`.

Do not stop to report ordinary fixable defects. Repair them yourself. Do not return ACTIVE/IN_PROGRESS to Director.

## Academic requirements
- Complete foundational-to-advanced coverage appropriate to this scope, without using advanced material to replace foundational measurement literacy.
- Atomic, defensible, sourced claims with epistemic class, certainty and scope limits.
- D1–D4 are academic depth, not age/grade.
- Prefer primary, standards, metrology institutes, scholarly and stable sources; pin versions where practicable.
- Reuse B1.1-C02/C03 mathematical prerequisites rather than duplicate them.
- No B1.2-C02..C12 Claim IDs may supply academic support.

## Closure
Create exactly one `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl` row per objective. Every support Claim ID must resolve to committed C01 or accepted prerequisite records. `requires_unlocked_scope_claims` must be false for PASS.

## Self-audit before final
Verify at minimum:
- 6/6 canonical topics covered;
- stable ID integrity;
- claim/source/objective schema validity;
- semantic claim→objective closure;
- semantic duplicate control;
- prerequisite graph/sequence valid;
- foundational measurement coverage adequate;
- FUTURE_LOCKED_SUPPORT = 0;
- CURRICULUM-only stage boundary;
- all required output/status files committed.

Repair anything inside scope and re-audit before final.

## Terminal output
Only after committed terminal state, return:

`WINDOW_ID: C01-W03-B1.2-PHYSICS-FAMILY-C01`
`STATUS: PASS_CANDIDATE | BLOCK`
`FINAL_COMMIT_SHA: <exact branch HEAD>`
`TOPICS: 6/6`
`CLAIMS: <n>`
`LEARNING_OBJECTIVES: <n>`
`SEMANTIC_CLOSURE: <n>/<n> PASS`
`SELF_AUDIT: PASS`
`SELF_REPAIRS: <n>`
`FOUNDATIONAL_COVERAGE: PASS`
`FUTURE_LOCKED_SUPPORT: 0`
`OUTPUTS_SAVED: YES`
`STATUS_SAVED: YES`
`RED_FLAG: NONE | <true external blocker>`
`NEXT: B1.2-C02 — GATED pending Director acceptance of C01`

Do not unlock C02 and do not mutate `hka-tree/curriculum-master`.
