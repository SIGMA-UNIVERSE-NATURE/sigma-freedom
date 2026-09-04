# Window Contract — C01-W01-B1-ARCHITECTURE

## Mission

Build the complete execution architecture for canonical Branch 1 — `QUY LUẬT — Quy luật & Thực tại` — before any detailed lesson authoring begins.

This window does NOT generate images, visual prompts, lesson artwork descriptions, or website production assets.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
- Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
- Curriculum master branch: `hka-tree/curriculum-master`
- Required control files:
  - `CURRICULUM_AUTOPILOT/MASTER_PLAN.md`
  - `CURRICULUM_AUTOPILOT/HKA_CURRICULUM_STATE.json`
  - `CURRICULUM_AUTOPILOT/WINDOW_RECOVERY_PROTOCOL.md`
  - `CURRICULUM_AUTOPILOT/WINDOW_REGISTRY.json`

## Scope

Canonical Branch 1 contains exactly these five canonical subbranches:

- B1.1 Toán học & Hệ hình thức
- B1.2 Vật chất & Năng lượng
- B1.3 Chất & Biến đổi
- B1.4 Trái Đất & Vũ trụ
- B1.5 Thông tin & Tính toán

The window must map every canonical topic present under those subbranches into a durable curriculum-authoring plan without deleting, renaming away, or silently collapsing canonical coverage.

## Required outputs

Create under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/`

1. `B1_SCOPE_MAP.json`
   - Stable IDs for all canonical Branch 1 topic clusters.
   - Parent-child relationships.
   - Cross-links to other HKA branches where already evident.

2. `B1_COVERAGE_MATRIX.md`
   - Every canonical Branch 1 topic mapped to an authoring unit.
   - No orphan canonical topic.
   - Explicit overlap risks.

3. `B1_ID_AND_RECORD_STANDARD.md`
   - Stable ID rules for Node, Claim, Source, Learning Objective, Lesson Slot.
   - IDs must remain stable across window crashes/restarts.

4. `B1_AUTHORING_SEQUENCE.md`
   - Prerequisite-aware authoring order.
   - Deterministic child-window partition plan for B1.1-B1.5.
   - Child scopes must be small enough that a dead/long window can be replaced without losing the whole subbranch.

5. `B1_DUPLICATE_CONTROL.md`
   - Semantic duplicate method.
   - Distinguish legitimate cross-domain reuse from repeated lesson meaning.

6. `RESULT.json`
   - `window_id`
   - `status`
   - `input_commit_sha`
   - output paths
   - counts
   - coverage result
   - duplicate-risk result
   - `next_action`

7. `HANDOFF.md`
   - Concise recovery note for the next window.
   - Must contain no information that is absent from committed artifacts.

## Completion gate

PASS requires all canonical B1 topics accounted for and a deterministic, restartable authoring partition for B1.1-B1.5.

No detailed lesson prompt authoring is allowed in this window.

No branch may be marked `ACADEMIC_LOCKED` by this window.

## Failure behavior

If canonical scope is ambiguous, record the ambiguity and use `REVIEW_REQUIRED`; do not invent a silent canonical change.

If the window dies, replacement resumes from committed outputs according to `WINDOW_RECOVERY_PROTOCOL.md`.
