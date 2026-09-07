# HKA Worker Execution Prompt — B1.3-C07

Repo: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `hka-tree/c01-w04-chemistry-c07`
Window: `C01-W04-B1.3-CHEMISTRY-FAMILY-C07`
Scope: `B1.3-C07 — Hóa lý và hóa học lý thuyết`
Stage: `CURRICULUM` only
Control-plane baseline: `509f042d747cf063aa07b96a43cce508e605b988`

## Canonical scope
Frozen topic order:
1. Nhiệt động hóa học
2. Động học hóa học
3. Hóa lượng tử
4. Hóa học bề mặt
5. Hóa keo
6. Hóa học tính toán

Canonical prerequisites:
- `B1.3-C03@3ce2ef9679d821386bef92895a37ca379016fdf0`
- `B1.3-C04@caa12019682e1a9274fe75b8ab20435c3bfb4d2e`
- `B1.2-C07@7d710491de2d4bb5e550a2b9b208739934a9f650`

Read before authoring:
- current `HKA_CURRICULUM_STATE.json`
- current `WINDOW_REGISTRY.json`
- current `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json`
- current `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`
- immutable `B1_SCOPE_MAP.json@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_AUTHORING_SEQUENCE.md@265bb584b5d7e36e11091289d58558408880118c`
- prior accepted C03/C04 and B1.2-C07 artifacts needed for prerequisite/boundary checking.

## Transaction
`READ STATE → AUTHOR C07 ONLY → SELF-AUDIT → SELF-REPAIR → RE-AUDIT → COMMIT → READ BACK → UPDATE RESULT/HANDOFF/STATUS/REPORT/CHECKPOINT → FINAL RECEIPT`

Worker repairs all in-scope defects itself before returning. Return `BLOCK` only for a genuine outside dependency/gate.

## Required academic outputs
Write only under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C07/`

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
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W04-B1.3-CHEMISTRY-FAMILY-C07/`

Maintain current `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/*.json`.

## Mandatory gates
- 6/6 canonical topics.
- Atomic sourced claims; deterministic source resolution.
- Explicit D1-D4 learning objectives; D1-D4 are academic depth, not age bands.
- Exactly-one semantic closure row per learning objective, semantically complete.
- Full foundational/general-education physical-chemistry spine before advanced theory/computation dominance.
- Exact prerequisite ownership: C03 + C04 + B1.2-C07 only.
- Prerequisite graph acyclic; no dangling IDs.
- Duplicate/ownership PASS.
- Architecture overlap risks `R07`/`R08` explicitly dispositioned: C07 owns chemistry-facing physical/theoretical chemistry; C03 retains bonding/structure, C04 retains reaction/equilibrium, B1.2-C07 retains quantum-physics foundations.
- `requires_unlocked_scope_claims=false`.
- `FUTURE_LOCKED_SUPPORT=0`; C08-C10 are boundary-only and supply zero supporting Claim IDs.
- `CROSS_SCOPE_ACADEMIC_MUTATION=0`.
- Stable IDs preserved after repair.
- CURRICULUM only; no Lesson Registry/prompt-production/image/R2/delivery/web artifacts.
- Durable read-back PASS after final commit.

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
- ownership
- source resolution
- support resolution
- future locked support
- cross-scope academic mutation
- stage boundary
- red flag
- `NEXT: B1.3-C08 gated pending Director acceptance of C07 and C08 prerequisites`

Do not unlock C08. Do not make Director acceptance decisions. Do not report intermediate progress.
