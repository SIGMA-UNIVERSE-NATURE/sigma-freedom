# HKA Worker Execution Prompt — B1.4 C01-C03

Repo: `SIGMA-UNIVERSE-NATURE/sigma-freedom`  
Branch: `hka-tree/c01-w05-earth-universe-c01-c03`  
Window: `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03`  
Owner: `W45`  
Stage: `CURRICULUM` only  
Family controller: `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY`  
Family branch: `hka-tree/c01-w05-earth-universe-family`  
Control-plane opening SHA: `72c00cdd57aaacc0e8483939b4c5cf01004ed3c9`  
Director open-order commit: `6c2cd116c32d7278dd3e44d20719eb6534a8ca56`  
Director opening checkpoint: `565640d4e7a02838d690769662f0005a1ca36940`

## Canonical child contract

This bounded child owns exactly three stable scopes/topics and must execute them in canonical order:

1. `B1.4-C01 — Khoáng vật, đá và địa hóa` / topic `B1.4-C01-T01`
2. `B1.4-C02 — Cấu trúc bên trong Trái Đất` / topic `B1.4-C02-T01`
3. `B1.4-C03 — Địa vật lý` / topic `B1.4-C03-T01`

Do not merge, split, rename or renumber these scopes/topics. Primary ownership remains with this W45 child.

### Exact prerequisite chain

External accepted prerequisite for `B1.4-C01`:

- `B1.3-C01@d3d5eb000b927f69732554c9dd58b4c087d7ca7d`

Internal child prerequisites:

- `B1.4-C02` depends on the newly authored and internally validated `B1.4-C01`.
- `B1.4-C03` depends on the newly authored and internally validated `B1.4-C02`.

No additional canonical prerequisite scopes may be invented.

Read before authoring:
- current `HKA_CURRICULUM_STATE.json`
- current `WINDOW_REGISTRY.json`
- current `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json`
- current `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`
- immutable `B1_SCOPE_MAP.json@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_AUTHORING_SEQUENCE.md@265bb584b5d7e36e11091289d58558408880118c`
- immutable `B1_DUPLICATE_CONTROL.md@265bb584b5d7e36e11091289d58558408880118c`
- immutable B1 ID/record standard
- accepted `B1.3-C01` artifacts at the exact accepted SHA
- prior accepted B1 artifacts needed for semantic duplicate/ownership checks

## Transaction

`READ STATE → AUTHOR C01 → SELF-AUDIT/REPAIR C01 → AUTHOR C02 → SELF-AUDIT/REPAIR C02 → AUTHOR C03 → SELF-AUDIT/REPAIR C03 → FULL-CHILD RE-AUDIT → COMMIT → READ BACK → UPDATE RESULT/HANDOFF/STATUS/REPORT/CHECKPOINT → FINAL RECEIPT`

Repair all in-scope defects before returning. Return `BLOCK` only for a genuine outside dependency/gate.

## Required output root

Write only under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.4/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03/`

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

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03/`

Create/maintain `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/*.json`.

## Mandatory academic gates

- 3/3 canonical scopes/topics complete in frozen order.
- Stable scope/topic IDs preserved.
- Atomic sourced claims with deterministic source resolution.
- Explicit D1-D4 learning objectives; depth is academic depth, not age band.
- Exactly one semantically complete closure row per learning objective.
- Foundational/general-education geology/geophysics spine must be complete before advanced specialization dominates.
- Prerequisite graph must be acyclic with no dangling IDs.
- Support must resolve only to local/accepted prerequisites; `requires_unlocked_scope_claims=false`.
- Run semantic duplicate control against all prior accepted B1 claims/objectives.

### R11 — chemistry vs Earth-system

Applies to `B1.4-C01`.

- B1.3 retains primary ownership of chemical composition, chemical reactions, pollutant/process chemistry and chemistry-facing material claims.
- B1.4-C01 owns mineral/rock/geochemical occurrence and classification in Earth context, geological reservoirs/process histories and Earth-system geochemical interpretation.
- Reuse accepted chemistry as prerequisite/reference where meaning is identical; do not silently duplicate chemistry objectives.

### R10 — physics vs Earth/space

Applies to `B1.4-C03`.

- B1.2 retains transferable physical laws, measurement methods and generic physical theory.
- B1.4-C03 owns geophysical observation/inference about Earth structure and processes: Earth-specific fields, seismic/geophysical evidence, inverse interpretation and system history/context.
- Reuse physics foundations rather than reteaching unchanged physical-law objectives.

### Cross-domain boundary

No mandatory architecture X-node is registered for B1.4-C01/C02/C03. Do not fabricate X01-X08 links merely for template completeness.

## Lock controls

- `FUTURE_LOCKED_SUPPORT=0`.
- `CROSS_SCOPE_ACADEMIC_MUTATION=0`.
- Do not mutate accepted B1.1, B1.2 or B1.3 academic artifacts.
- `C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C04-C06` remains locked.
- All later B1.4 children remain locked.
- B1.5 remains locked.
- CURRICULUM only: no Lesson Registry, prompt-production, image, R2, QA, delivery, vault or website artifacts.

## Terminal gate

Return `PASS_CANDIDATE` only if all pass:
- scopes/topics complete
- claim integrity
- source resolution
- D1-D4 objective completeness
- semantic closure
- foundational coverage
- stable IDs
- exact prerequisite chain
- prerequisite graph
- R11 disposition
- R10 disposition
- duplicate/ownership scan
- support resolution
- future locked support = 0
- cross-scope academic mutation = 0
- stage boundary = `PASS_CURRICULUM_ONLY`
- durable read-back = PASS
- red flag = NONE

## Final receipt only

Return:
- `WINDOW_ID: C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C01-C03`
- `STATUS: PASS_CANDIDATE` or genuine `BLOCK`
- `FINAL_COMMIT_SHA`
- scopes/topics
- claims
- learning objectives
- semantic closure
- worker self-repairs
- foundational coverage
- stable IDs
- prerequisite alignment and graph
- R11 / R10 ownership dispositions
- source resolution
- support resolution
- future locked support
- cross-scope academic mutation
- stage boundary
- durable read-back
- red flag
- `NEXT: C04-C06 remains gated pending Director acceptance of C01-C03; B1.5 remains locked.`

Do not self-accept. Do not unlock C04-C06. Do not unlock B1.5. Do not report intermediate progress.
