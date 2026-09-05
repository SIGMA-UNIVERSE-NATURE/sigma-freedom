# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C09

STATUS: READY_AFTER_DIRECTOR_C07_ACCEPTANCE
STAGE: CURRICULUM
SCOPE: B1.1-C09 — Tô pô và hình học hiện đại
EXECUTION_BRANCH: `hka-tree/c01-w02-math-c09`
INPUT_COMMIT_SHA: `be10c01bf8df64a723e135524b75ce644947dcbd`

## Canonical topics — exact stable order

1. `B1.1-C09-T01` — Không gian tô pô
2. `B1.1-C09-T02` — Liên thông và compact
3. `B1.1-C09-T03` — Đa tạp
4. `B1.1-C09-T04` — Tô pô đại số
5. `B1.1-C09-T05` — Tô pô vi phân
6. `B1.1-C09-T06` — Lý thuyết nút
7. `B1.1-C09-T07` — Hình học toàn cục

Stable IDs, names and primary ownership are fixed.

## Accepted prerequisites

Frozen architecture prerequisites:
- C01 — sets, relations, functions and proof foundations.
- C04 — accepted geometry foundations.

Dependency Amendment 4 supplemental accepted prerequisites:
- C03 — groups, linear algebra and algebraic structures.
- C05 — continuity, differentiability, multivariable and analysis primitives.

Accepted predecessor for durable branch continuity is C07 head `be10c01bf8df64a723e135524b75ce644947dcbd`.

## Required output artifacts

Under:
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C09/`

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
`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C09/`

## Academic gates

1. Complete knowledge, minimum redundancy; never target a claim count.
2. Every claim atomic, source-traceable, scope-limited, epistemically classified and certainty-labelled.
3. D1–D4 remain age-independent; exactly one objective per node per depth unless a justified canonical node split is required without changing topic IDs.
4. Every objective must be semantically supported by actual listed Claim IDs; mechanical closure-row presence is insufficient.
5. `future_or_locked_scope_claim_ids` must be empty for every closure row.
6. Stable SOURCE_ID normalization and edition/DOI/ISBN identity required.
7. Prerequisite graph must be acyclic and academically necessary.
8. Worker PASS is candidate only; successor unlock belongs to Director.

## Mandatory ownership boundaries

### C05 analysis versus C09 topology
- C05 retains analysis/calculus and analysis-specific metric/open/closed/compact/complete concepts already accepted.
- C09-T01/T02 own generic topological-space, continuity/homeomorphism, separation, connectedness and compactness meanings at topology level.
- Reuse accepted C05 primitives where useful; do not duplicate C05 learning objectives under topological wording.

### C04 geometry versus C09 manifolds/global geometry
- C04 retains accepted Euclidean, analytic, projective, local differential and algebraic geometry learning meanings.
- C09-T03 owns abstract topological/smooth manifold structure: charts, atlases, manifold maps and manifold-level organization.
- C09-T05 owns differential-topology meanings such as smooth-map regularity at manifold level, regular values/transversality and topology-changing/classification consequences where sourced.
- C09-T07 may own genuinely global manifold/geometric consequences and invariants.
- C09 must not re-author C04 local curvature/differential-geometry claims merely with manifold terminology.

### C03 algebra versus C09 algebraic topology
- C03 retains groups/rings/vector spaces/linear maps and algebraic foundations.
- C09-T04 owns topological invariants/constructions such as homotopy/fundamental-group/homology-type meanings, using C03 algebra by reference rather than re-teaching it.

### Knot theory
- C09-T06 owns mathematical knot/link equivalence and topological invariants.
- Do not drift into materials, biology, physical knot dynamics or computation/algorithm complexity.

### Locked C10
- C10 numerical/applied/computational mathematics remains locked and supplies zero support Claim IDs.
- Numerical topology/geometry algorithms, optimization or simulation are boundary-only.

## Internal overlap controls

Mandatory explicit dispositions:
- T01 generic topology vs T02 connectedness/compactness.
- T01/T03 topology vs manifold structure.
- T03 manifolds vs T05 differential topology.
- T03/T04 manifold spaces vs algebraic-topology invariants.
- T04 algebraic topology vs T06 knot invariants.
- T03/T05/T07 local smooth structure vs genuinely global geometry.

## Stage boundary

Forbidden:
- `ACADEMIC_LOCKED`
- Lesson Registry
- prompts
- images
- R2
- QA/Vault/Web Optimize/Delivery/Website Update

## Terminal rule

If committed read-back and all gates PASS:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C10 — GATED pending Director acceptance of C09`

If any theorem hypothesis, ownership, source or semantic-closure uncertainty remains:

`STATUS: REVIEW_REQUIRED`
