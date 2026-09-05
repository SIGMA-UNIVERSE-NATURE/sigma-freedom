# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C08

STATUS: READY_AFTER_DIRECTOR_C06_ACCEPTANCE
STAGE: CURRICULUM
SCOPE: B1.1-C08 — Toán rời rạc và tổ hợp
EXECUTION_BRANCH: `hka-tree/c01-w02-math-c08`
INPUT_COMMIT_SHA: `e0d6f667d38e937c7c6040b51fb14e34f0bb6345`

## Canonical anchors

- HKA World Tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`
- Accepted B1 architecture: `265bb584b5d7e36e11091289d58558408880118c`
- Frozen `B1_SCOPE_MAP` blob: `bedef47958a728e3f0d56d412f7bdea3ec465856`
- Active dependency amendment: `B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_2.md`

## Canonical topics — exact stable order

1. `B1.1-C08-T01` — Kỹ thuật đếm
2. `B1.1-C08-T02` — Hoán vị và tổ hợp
3. `B1.1-C08-T03` — Quan hệ truy hồi
4. `B1.1-C08-T04` — Lý thuyết đồ thị
5. `B1.1-C08-T05` — Cây và mạng
6. `B1.1-C08-T06` — Tối ưu tổ hợp
7. `B1.1-C08-T07` — Mã sửa lỗi
8. `B1.1-C08-T08` — Cấu trúc rời rạc

Stable topic IDs and primary ownership are frozen. Do not renumber or silently rename.

## Accepted foundations

Reuse accepted foundations by reference rather than re-authoring:

- C01 logic, set, relation and proof foundations.
- C02 arithmetic, integer and number-system foundations.
- C03 algebra, finite-field, vector-space and linear-algebra primitives where required, especially for algebraic coding structures.
- C04/C05/C06 may be secondary context only where genuinely relevant; they are not generic prerequisites for this scope.

## Required academic outputs

Under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C08/`

- `NODES.jsonl`
- `CLAIMS.jsonl`
- `SOURCES.jsonl`
- `LEARNING_OBJECTIVES.jsonl`
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
- `CROSS_LINKS.jsonl`
- `CURRICULUM_SEQUENCE_INTENT.jsonl`
- `RESULT.json`
- `HANDOFF.md`

Mandatory durable status folder:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C08/`

## Academic gates

1. Complete knowledge, minimum redundancy; never target a claim count.
2. Every claim is atomic, sourced, scope-limited, epistemically classified and certainty-labelled.
3. D1–D4 remain epistemic depths independent of age.
4. Every Learning Objective has exactly one effective closure row and direct semantic support from listed Claim IDs.
5. A closure row or `SUPPORTED` flag is not evidence by itself; compare objective semantics against actual claim propositions.
6. Future/locked-scope support Claim IDs must be zero.
7. Source IDs follow deterministic SHA-256 normalization and stable DOI/ISBN/version identities where practicable.
8. Prerequisite/sequence graph must be acyclic and academically necessary.
9. Worker PASS is candidate only; only Director acceptance unlocks another scope.

## Mandatory ownership and duplicate controls

### R05 — Mathematics vs algorithms — `OVERLAP_REVIEW`

- C08 owns graph/combinatorial structures, recurrence structure, mathematical counting, proof-oriented properties and combinatorial optimization formulations.
- Future `B1.5-C03` owns algorithmic operations, data structures, running-time/complexity analysis and algorithm engineering.
- Do not make a second objective merely by wrapping the same graph/combinatorial theorem in algorithmic language.

### R02 — Error-correcting codes — `CROSS_LINK_NOT_DUPLICATE`

- C08-T07 owns algebraic/combinatorial code structures, distance, bounds and proof-oriented mathematical properties.
- Future `B1.5-C01-T05` owns coding for information transmission/channel reliability and information-system objectives.
- Reuse accepted C03 finite-field/linear-algebra primitives where required; do not re-author field/vector-space foundations.

### T06 — Tối ưu tổ hợp boundary

- C08 owns discrete feasible structures, combinatorial objective formulations and mathematical optimality/proof properties.
- Future C10 owns broader applied optimization/numerical procedures; future B1.5-C03 owns algorithmic complexity/implementation.
- No locked-scope claim may support a C08 objective.

## Locked boundaries

- `B1.1-C07` probability/statistics/inference: LOCKED until Director-accepted C08 PASS under Amendment 2.
- `B1.1-C09`: LOCKED.
- `B1.1-C10`: LOCKED.
- B1.2+ and B1.5 computational/application scopes: boundary references only unless already Director-accepted.
- No `ACADEMIC_LOCKED`, Lesson Registry, prompts, images, R2, delivery or website artifact.

## Terminal rule

If committed read-back and all gates PASS:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: B1.1-C07 — GATED pending Director acceptance of C08`

If uncertainty remains, return `REVIEW_REQUIRED` rather than forcing PASS.
