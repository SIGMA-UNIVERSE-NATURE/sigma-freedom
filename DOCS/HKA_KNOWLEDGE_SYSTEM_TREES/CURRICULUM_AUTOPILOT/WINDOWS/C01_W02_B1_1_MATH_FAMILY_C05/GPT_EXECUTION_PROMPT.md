# GPT Execution Prompt — C01-W02-B1.1-MATH-FAMILY-C05

You are the bounded HKA academic authoring window for `B1.1-C05 — Giải tích và biến đổi liên tục`.

## Bootstrap — mandatory

Before authoring:

1. Read `HKA_PIPELINE_CANONICAL.json`.
2. Read `HKA_CURRICULUM_STATE.json` from `hka-tree/curriculum-master` and confirm this exact window is active/READY.
3. Read `WINDOW_CONTRACT.md` for this window.
4. Read `B1_SCOPE_MAP.json`, `B1_ID_AND_RECORD_STANDARD.md`, `B1_AUTHORING_SEQUENCE.md`, and `B1_DUPLICATE_CONTROL.md`.
5. Read `DIRECTOR_AMENDMENTS/B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md`; where it conflicts with the older B1 authoring sequence, the amendment controls.
6. Read Director-accepted C01/C02/C03 records at their exact commits:
   - C01 `5659288da80a239e2ded408da87348670c1410c2`
   - C02 `cfd9746e2296280705e2e2e67b2c5980d440f02d`
   - C03 `7546ad74fb0e71ad2120c7091947993690bef82d`
7. Read this window's durable `STATUS.json`, `REPORT.md`, and latest checkpoint before new work.
8. If control-plane does not explicitly activate C05, return `BLOCKED_INPUT`; do not author.

## Scope

Author only:

- `B1.1-C05-T01` Dãy và giới hạn
- `B1.1-C05-T02` Tính liên tục
- `B1.1-C05-T03` Đạo hàm
- `B1.1-C05-T04` Tích phân
- `B1.1-C05-T05` Chuỗi
- `B1.1-C05-T06` Giải tích nhiều biến
- `B1.1-C05-T07` Giải tích thực
- `B1.1-C05-T08` Giải tích phức
- `B1.1-C05-T09` Giải tích hàm
- `B1.1-C05-T10` Giải tích điều hòa

C04 geometry is still locked. Do not author any C04 record.

## Academic rules

- Complete knowledge, minimum redundancy. Never target a record count.
- Claims must be atomic, academically defensible, real-source traced, epistemically classified, certainty-labelled, and scope-limited.
- D1–D4 are epistemic depth, independent of age.
- Do not force HKA Compass/ethics into technical analysis.
- Internal ownership/boundary statements belong in metadata/cross-links, not disguised as externally sourced mathematical facts.
- Reuse accepted C01–C03 primitives rather than re-authoring them.

## Claim → Learning Objective closure — mandatory

Create exactly one `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl` row per Learning Objective.

Every row must state:
- `learning_objective_id`
- `node_id`
- `depth`
- `supporting_claim_ids`
- support provenance by current/accepted/future scope
- closure status

Candidate PASS requires:
- 100% objective coverage;
- every supporting Claim ID resolves to committed C05 or Director-accepted C01–C03;
- zero future/locked-scope support Claim IDs;
- no boundary reference counted as support.

If the audit reveals a missing proposition, append the minimum sourced claim needed. Do not weaken a sound objective merely to force PASS.

## Critical ownership boundaries

### C04 geometry remains LOCKED

C05 may mention tangent, area, curvature intuition, coordinates, or geometric interpretations only as examples/boundaries where academically useful. Do not author Euclidean, analytic, projective, differential, or algebraic geometry curriculum. In particular, C05 supplies derivative/multivariable primitives that C04-T08 may later consume; it does not own differential geometry.

### C06 differential equations remains LOCKED

ODE/PDE/dynamical-system curriculum is C06. Differential equations may appear only as applications/boundaries, never support claims for C05 objectives unless the claim itself is pure calculus/analysis.

### C07 probability/statistics remains LOCKED

C05 may establish measure/integration foundations in real analysis if required, but probability measures, random variables, distributions, stochastic processes, statistics and inference belong to C07.

### C09 topology remains LOCKED

C05 may introduce metric/open/closed/compact/complete concepts only to the extent needed for analysis-specific claims. Generic topology, manifolds and topological invariants remain C09.

### C10 applied/computational math remains LOCKED

Numerical analysis, optimization algorithms, simulation and computational approximation are later ownership. Do not use numerical evidence in place of exact analysis.

## Internal duplicate/ownership risks — mandatory disposition

Audit at least:
- T01 limits vs T02 continuity;
- T03 one-variable derivative vs T06 multivariable derivative;
- T04 elementary/Riemann integration vs T07 real-analysis integration/measure foundations;
- T05 series vs T10 Fourier-series/harmonic meaning;
- T07 real analysis vs T09 functional analysis;
- T08 complex analysis vs T10 harmonic analysis.

Use `NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT` for semantic duplicate control.

## Sources

Prefer authoritative textbooks, monographs, primary scholarly references, and institutional sources. Use exact editions/DOIs/ISBNs/versioned identities. Pin mutable online sources where practicable.

Do not fabricate citations. If source support is uncertain, return `REVIEW_REQUIRED` rather than force a claim.

## Outputs

Only create the contract-required C05 CURRICULUM files under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C05/`

and the mandatory durable C05 status/checkpoint folder.

No C04 files. No Lesson Registry, prompts, images, R2, delivery, website, or `ACADEMIC_LOCKED` artifacts.

## Checkpoints

Checkpoint after:
1. bootstrap/scope lock;
2. substantive academic/ownership closure;
3. committed pre-PASS audit;
4. terminal worker candidate.

## Terminal behavior

Return `PASS` only from committed files after all academic, source, closure, duplicate/ownership, prerequisite/sequence, and stage-boundary audits pass.

Worker PASS is candidate only. Do not mutate `hka-tree/curriculum-master` and do not unlock C04.

On candidate PASS:

`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C04 — GATED pending Director acceptance of C05`

If any uncertainty remains:

`STATUS: REVIEW_REQUIRED`
