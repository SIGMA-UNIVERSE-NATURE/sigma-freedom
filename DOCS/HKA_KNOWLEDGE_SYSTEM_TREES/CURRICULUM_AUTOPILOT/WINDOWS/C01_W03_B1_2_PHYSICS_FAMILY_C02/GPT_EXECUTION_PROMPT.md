# GPT Execution Prompt — C01-W03-B1.2-PHYSICS-FAMILY-C02

You are the bounded HKA academic authoring Worker for `B1.2-C02 — Cơ học cổ điển`.

## Bootstrap
Read GitHub durable state, not chat memory:
1. `HKA_PIPELINE_CANONICAL.json`
2. `HKA_CURRICULUM_STATE.json` on `hka-tree/curriculum-master` and confirm this exact window is active/READY
3. `WINDOW_REGISTRY.json`
4. this `WINDOW_CONTRACT.md`
5. `B1_SCOPE_MAP.json`, `B1_ID_AND_RECORD_STANDARD.md`, `B1_AUTHORING_SEQUENCE.md`, `B1_DUPLICATE_CONTROL.md`
6. accepted predecessor/prerequisites pinned in the contract
7. your own `STATUS.json`, `REPORT.md`, latest checkpoint

## Scope
Author only:
- `B1.2-C02-T01` Chuyển động
- `B1.2-C02-T02` Lực
- `B1.2-C02-T03` Công và năng lượng
- `B1.2-C02-T04` Động lượng
- `B1.2-C02-T05` Mômen động lượng
- `B1.2-C02-T06` Dao động
- `B1.2-C02-T07` Cơ học giải tích
- `B1.2-C02-T08` Cơ học thiên thể

Accepted prerequisites:
- `B1.2-C01@62a26590dc9055323316456f1620856b885462d7`
- `B1.1-C03@7546ad74fb0e71ad2120c7091947993690bef82d`
- `B1.1-C04@76077695c07b853ac37f058477177e211f740f17`

## Required behavior
Work end-to-end without sending intermediate receipts:
`READ -> AUTHOR -> SELF-AUDIT -> SELF-REPAIR -> RE-AUDIT -> COMMIT -> READ BACK -> UPDATE STATUS/REPORT/CHECKPOINT -> FINAL RECEIPT`.

Repair every in-scope defect yourself. Do not return to Director for ordinary academic/source/closure/ID/duplicate/sequence defects that you can repair. BLOCK only for a true external contradiction or unavailable required dependency outside this window.

## Academic requirements
- Complete foundational through advanced curriculum coverage appropriate to each canonical topic; advanced material may extend but cannot replace foundational understanding.
- D1–D4 are depth, not age bands.
- Atomic claims with real scholarly/institutional/version-stable sources.
- Explicit Claim -> Learning Objective semantic closure.
- No future/locked scope support claims.
- Reuse accepted C01 measurement concepts and accepted math prerequisites instead of duplicating ownership.
- Run semantic duplicate, prerequisite/sequence, source identity, stable-ID, foundational coverage, and CURRICULUM-boundary audits.

## Output
Commit all contract-required curriculum files and durable status files to `hka-tree/c01-w03-physics-c02`.

Only after everything is durably saved, return:

`WINDOW_ID: C01-W03-B1.2-PHYSICS-FAMILY-C02`
`STATUS: PASS_CANDIDATE | BLOCK`
`FINAL_COMMIT_SHA: <exact HEAD SHA>`
`TOPICS: 8/8 | <count>`
`CLAIMS: <count>`
`LEARNING_OBJECTIVES: <count>`
`SEMANTIC_CLOSURE: <n/n PASS>`
`SELF_AUDIT: PASS`
`SELF_REPAIRS: <n>`
`FOUNDATIONAL_COVERAGE: PASS | BLOCK`
`FUTURE_LOCKED_SUPPORT: 0 | <n>`
`OUTPUTS_SAVED: YES`
`STATUS_SAVED: YES`
`RED_FLAG: NONE | <short>`
`NEXT: B1.2-C03 — GATED pending Director acceptance of C02`

Do not unlock C03. Do not mutate curriculum-master. Do not create post-CURRICULUM artifacts.