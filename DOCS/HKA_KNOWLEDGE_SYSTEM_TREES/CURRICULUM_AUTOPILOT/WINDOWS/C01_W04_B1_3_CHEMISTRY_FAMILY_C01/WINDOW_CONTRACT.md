# WINDOW CONTRACT — C01-W04-B1.3-CHEMISTRY-FAMILY-C01

Stage: `CURRICULUM`
Scope: `B1.3-C01 — Cấu trúc vật chất`
Execution branch: `hka-tree/c01-w04-chemistry-c01`

## Canonical topics
1. Nguyên tử
2. Phân tử
3. Ion
4. Đồng vị
5. Trạng thái vật chất
6. Cấu trúc điện tử

Canonical prerequisites:
- `B1.2-C07@7d710491de2d4bb5e550a2b9b208739934a9f650`
- `B1.2-C08@65ea8a21141e114dbff1c9e9a3e63b5a49571ad8`

Immutable anchors:
- canonical tree `fc799bf1104ab6352710e1801777a971b5179995`
- B1 architecture `265bb584b5d7e36e11091289d58558408880118c`
- scope-map blob `bedef47958a728e3f0d56d412f7bdea3ec465856`
- B1.2 exit Sentinel `5b0ff94151386fab2ebeffe434e9fa8ac06ec4ac`

## Ownership
C01 owns chemistry-level structure-of-matter foundations for its six canonical topics. Reuse B1.2-C07 quantum foundations and B1.2-C08 atomic/molecular/optical physics without duplicating their ownership. Do not pre-author B1.3-C02 periodic/inorganic chemistry or B1.3-C03 bonding/molecular-structure specialization; later B1.3 children are boundary-only and supply no support Claim IDs.

## Required academic outputs
Under `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.3/C01-W04-B1.3-CHEMISTRY-FAMILY-C01/`:
- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

## Mandatory gates
- 6/6 canonical topics.
- Atomic sourced claims with stable IDs.
- Age-independent D1-D4 objectives.
- Exactly one semantically valid closure row per learning objective.
- Full foundational/general-education progression before advanced dominance.
- Canonical prerequisite alignment PASS.
- Ownership/semantic-duplicate PASS.
- Prerequisite graph acyclic, zero dangling IDs.
- `requires_unlocked_scope_claims=false`.
- `FUTURE_LOCKED_SUPPORT=0`.
- Stage boundary `CURRICULUM` only.
- Durable GitHub read-back PASS.

Worker must self-audit, repair every in-scope defect, re-audit, commit, read back, update own status/report/checkpoint, and return only a final PASS candidate or true external BLOCK. Stable accepted IDs from prior scopes must not be changed.