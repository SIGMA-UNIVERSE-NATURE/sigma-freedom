# Window Contract — C01-W01-B1-ARCHITECTURE

## Mission

Build the complete restartable execution architecture for canonical Branch 1 — `QUY LUẬT — Quy luật & Thực tại` — inside the `CURRICULUM` stage only.

This window does NOT create lesson-registry records, visual prompts, images, R2 artifacts, web derivatives or website updates.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
- Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
- Curriculum master branch: `hka-tree/curriculum-master`
- Canonical pipeline: `CURRICULUM_AUTOPILOT/HKA_PIPELINE_CANONICAL.json`
- Required controls:
  - `CURRICULUM_AUTOPILOT/MASTER_PLAN.md`
  - `CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json`
  - `CURRICULUM_AUTOPILOT/WINDOW_RECOVERY_PROTOCOL.md`
  - `CURRICULUM_AUTOPILOT/WINDOW_REGISTRY.json`

## Pipeline position

Required predecessor: `KNOWLEDGE=LOCKED_INPUT`.
Current stage: `CURRICULUM`.
This window cannot unlock `ACADEMIC_LOCKED`; that requires all six branches plus the global curriculum audit.

## Scope

Canonical Branch 1 contains exactly these five canonical subbranches:

- B1.1 Toán học & Hệ hình thức
- B1.2 Vật chất & Năng lượng
- B1.3 Chất & Biến đổi
- B1.4 Trái Đất & Vũ trụ
- B1.5 Thông tin & Tính toán

Map every canonical topic under those subbranches into a durable curriculum-authoring plan without deleting, silently collapsing or transferring away canonical coverage.

## Required outputs

Create under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/`

1. `B1_SCOPE_MAP.json`
   - Stable IDs for all canonical Branch 1 topic clusters.
   - Parent-child relationships.
   - Primary ownership.
   - Cross-tree links where evident.

2. `B1_COVERAGE_MATRIX.md`
   - Every canonical B1 topic mapped to one primary authoring unit.
   - No orphan topic.
   - Explicit semantic-overlap risks.

3. `B1_ID_AND_RECORD_STANDARD.md`
   - Stable ID rules for Node, Claim, Source, Learning Objective and future Lesson Slot references.
   - IDs survive crashes and replacement windows.

4. `B1_AUTHORING_SEQUENCE.md`
   - Prerequisite-aware authoring order.
   - Deterministic bounded child-window partition for B1.1-B1.5.
   - A child must be independently resumable; do not assign an entire large discipline to one long window.

5. `B1_DUPLICATE_CONTROL.md`
   - Semantic duplicate method.
   - Distinguish legitimate cross-domain reuse from repeated learning meaning.

6. `RESULT.json`
   - `window_id`
   - `stage` = `CURRICULUM`
   - `status`
   - `input_commit_sha`
   - output paths
   - counts
   - coverage result
   - duplicate-risk result
   - `next_action`

7. `HANDOFF.md`
   - Concise recovery note.
   - No essential information may exist only in HANDOFF or chat; it must be present in durable artifacts.

## PASS gate

PASS requires:

- every canonical B1 topic accounted for;
- exactly one primary authoring owner per canonical topic;
- deterministic bounded child partitions;
- no unauthorized work from later pipeline stages;
- `RESULT.json` committed with next_action pointing only to the first successor window.

No branch or global curriculum may be marked `ACADEMIC_LOCKED` by this architecture window.

## Failure/recovery

If canonical scope is genuinely ambiguous, record it and return `REVIEW_REQUIRED`; do not invent a silent canonical change.

If the window dies, a replacement reads GitHub state plus committed partial outputs and resumes unfinished scope according to `WINDOW_RECOVERY_PROTOCOL.md`.
