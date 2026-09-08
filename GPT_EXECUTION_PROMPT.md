# HKA Worker Execution Prompt — B1.3-C08

Repo: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `hka-tree/c01-w04-chemistry-c08`
Window: `C01-W04-B1.3-CHEMISTRY-FAMILY-C08`
Scope: `B1.3-C08 — Hóa sinh và sinh học hóa học`
Stage: `CURRICULUM` only
Control-plane baseline: `b90f3e8eea3c6fadd501a6ae3ac53c51df4e9a3c`

## Canonical scope
Frozen topic order:
1. Amino acid và protein
2. Carbohydrate
3. Lipid
4. Acid nucleic
5. Enzyme
6. Chuyển hóa
7. Thiết kế phân tử sinh học

Canonical prerequisites exactly:
- `B1.3-C06@f5802d4d9d7f3a4a200e532301c2b6ee2dcb55ba`
- `B1.3-C07@4da2338f420d12b958b0af71edda922816ff69cb`

Read before authoring:
- current `HKA_CURRICULUM_STATE.json`
- current `WINDOW_REGISTRY.json`
- current `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json`
- current `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`
- immutable `B1_SCOPE_MAP.json@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_AUTHORING_SEQUENCE.md@265bb584b5d7e36e11091289d58558408880118c`
- prior accepted C06/C07 artifacts needed for prerequisite/boundary checking.

## Transaction
`READ STATE → AUTHOR C08 ONLY → SELF-AUDIT → SELF-REPAIR → RE-AUDIT → COMMIT → READ BACK → UPDATE RESULT/HANDOFF/STATUS/REPORT/CHECKPOINT → FINAL RECEIPT`

Repair all in-scope defects before returning. Return `BLOCK` only for a genuine outside dependency/gate.

## Required academic outputs
Write only under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C08/`

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
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W04-B1.3-CHEMISTRY-FAMILY-C08/`

Maintain current `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/*.json`.

## Mandatory gates
- 7/7 canonical topics.
- Atomic sourced claims; deterministic source resolution.
- Explicit D1-D4 learning objectives; D1-D4 are academic depth, not age bands.
- Exactly one semantically complete closure row per learning objective.
- Full foundational/general-education biomolecule, enzyme and metabolism spine before advanced molecular-design dominance.
- Exact prerequisite ownership: C06 + C07 only.
- Preserve C06 organic-chemistry ownership and C07 physical/theoretical-chemistry ownership.
- Cross-links `X03`/`X04` are secondary/boundary only; they supply no ownership transfer or supporting Claim IDs.
- Architecture overlap risk `R14` explicitly dispositioned; no duplicate takeover of global-health/food or later-domain ownership.
- Prerequisite graph acyclic; no dangling IDs.
- Duplicate/ownership PASS.
- `requires_unlocked_scope_claims=false`.
- `FUTURE_LOCKED_SUPPORT=0`; C09-C10 are boundary-only and supply zero supporting Claim IDs.
- `CROSS_SCOPE_ACADEMIC_MUTATION=0`.
- Stable IDs preserved after repair.
- CURRICULUM only; no Lesson Registry/prompt-production/image/R2/delivery/web artifacts.
- Durable read-back PASS after terminal commit.

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
- `NEXT: B1.3-C09 gated pending Director acceptance of C08`

Do not unlock C09. Do not make Director acceptance decisions. Do not report intermediate progress.
