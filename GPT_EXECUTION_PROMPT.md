# HKA Worker Execution Prompt — B1.3-C10

Repo: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `hka-tree/c01-w04-chemistry-c10`
Window: `C01-W04-B1.3-CHEMISTRY-FAMILY-C10`
Scope: `B1.3-C10 — Hóa học môi trường, công nghiệp và bền vững`
Owner: `W32`
Stage: `CURRICULUM` only
Control-plane baseline: `61cfc23ebd235750936cad3c84f167687458570b`
Director open-order commit: `0f5d4a686940a47dbd4db914fbb1ee6493c812da`
Director opening checkpoint: `73d60ae7684865fc997ba0c80290b3ece80a4659`

## Canonical scope

Frozen topic order:
1. Hóa học khí quyển
2. Hóa học nước và đất
3. Ô nhiễm và độc chất
4. Quy trình công nghiệp
5. Xúc tác
6. Hóa học xanh
7. Kinh tế nguyên tử
8. Vòng đời vật liệu

Canonical prerequisites exactly:
- `B1.3-C04@caa12019682e1a9274fe75b8ab20435c3bfb4d2e`
- `B1.3-C05@d19b011f00ac5f24d7a212c957cac3bb5046f06e`
- `B1.3-C09@921226d0e83409d80f26eac1247d5f1e06269601`

C09 is both the sequential-governance predecessor and an exact canonical academic prerequisite for C10.

Read before authoring:
- current `HKA_CURRICULUM_STATE.json`
- current `WINDOW_REGISTRY.json`
- current `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json`
- current `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`
- immutable `B1_SCOPE_MAP.json@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_AUTHORING_SEQUENCE.md@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_DUPLICATE_CONTROL.md@265bb584b5d7e36e11091289d58558408880118c`
- prior accepted C04/C05/C09 artifacts needed for prerequisite/boundary checking
- prior accepted B1 artifacts needed for semantic duplicate scanning

## Transaction

`READ STATE → AUTHOR C10 ONLY → SELF-AUDIT → SELF-REPAIR → RE-AUDIT → COMMIT → READ BACK → UPDATE RESULT/HANDOFF/STATUS/REPORT/CHECKPOINT → FINAL RECEIPT`

Repair all in-scope defects before returning. Return `BLOCK` only for a genuine outside dependency/gate.

## Required academic outputs

Write only under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C10/`

Required:
- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

Status path:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W04-B1.3-CHEMISTRY-FAMILY-C10/`

Create/maintain `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/*.json`.

## Mandatory gates

- 8/8 canonical topics in frozen order with stable IDs preserved.
- Atomic sourced claims with deterministic source resolution.
- Explicit D1-D4 learning objectives; D1-D4 are academic depth, not age bands.
- Exactly one semantically complete closure row per learning objective.
- Complete foundational/general-education environmental, industrial and sustainability chemistry spine before advanced specialization dominates.
- Exact canonical prerequisite ownership: C04 + C05 + C09 only.
- Architecture risk `R11` must be explicitly dispositioned: C10 owns chemical composition, reactions, pollutants and chemical/industrial processes; B1.4 owns coupled Earth-system reservoirs, flows, hazards and environmental geology.
- Architecture risk `R12` must be explicitly dispositioned: C10 contributes disciplinary chemistry to climate links; `X01` is secondary cross-domain aggregation and transfers no primary ownership.
- Architecture risk `R14` must be explicitly dispositioned: chemical claims stay in C10; `X03` global health and `X04` food are secondary cross-domain boundaries, with health/biology/policy/culture/food-system synthesis outside C10 ownership.
- Mandatory cross-domain links: `X01`, `X03`, `X04`; secondary/boundary only, no ownership transfer, no future-scope supporting Claim IDs.
- Run semantic duplicate control against prior accepted B1 claims/objectives; same meaning must be referenced/extended rather than silently duplicated.
- Prerequisite graph acyclic; no dangling IDs.
- Duplicate/ownership PASS.
- `requires_unlocked_scope_claims=false`.
- `FUTURE_LOCKED_SUPPORT=0`; B1.4/B1.5 and all later scopes are boundary-only and supply zero supporting Claim IDs.
- `CROSS_SCOPE_ACADEMIC_MUTATION=0`; do not mutate accepted C01-C09 academic artifacts.
- Stable IDs preserved after any repair.
- CURRICULUM only; no Lesson Registry/prompt-production/image/R2/delivery/web artifacts.
- Durable read-back PASS after terminal commit.
- B1.4 remains locked. C10 worker has no authority to open B1.3 family-exit/integration or B1.4.

## Final receipt only

Return:
- `WINDOW_ID`
- `STATUS: PASS_CANDIDATE` or genuine `BLOCK`
- `FINAL_COMMIT_SHA` exact terminal branch HEAD
- topics / claims / learning objectives / semantic closure
- worker self-repairs
- foundational coverage
- stable IDs
- canonical prerequisite alignment
- prerequisite graph
- ownership / R11 / R12 / R14 dispositions
- X01 / X03 / X04 boundary control
- source resolution
- support resolution
- future locked support
- cross-scope academic mutation
- stage boundary
- durable read-back
- red flag
- `NEXT: B1.3 family integration/exit gated pending Director acceptance of C10; B1.4 remains locked.`

Do not self-accept C10. Do not unlock B1.4. Do not author post-CURRICULUM artifacts. Do not report intermediate progress.
