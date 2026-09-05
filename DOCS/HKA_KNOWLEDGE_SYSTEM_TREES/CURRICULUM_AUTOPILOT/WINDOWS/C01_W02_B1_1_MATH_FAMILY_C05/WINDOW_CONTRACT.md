# Window Contract — C01-W02-B1.1-MATH-FAMILY-C05

## Mission

Author the complete HKA `CURRICULUM` record set for stable scope `B1.1-C05 — Giải tích và biến đổi liên tục` only.

This window executes before C04 under `B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md` because differential geometry in C04 requires accepted calculus primitives. Stable IDs and ownership are unchanged.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Execution branch: `hka-tree/c01-w02-math-c05`
- Director-accepted predecessor C03: `7546ad74fb0e71ad2120c7091947993690bef82d`
- Director-accepted C02: `cfd9746e2296280705e2e2e67b2c5980d440f02d`
- Director-accepted C01: `5659288da80a239e2ded408da87348670c1410c2`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`
- Active dependency amendment: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/DIRECTOR_AMENDMENTS/B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md`

Do not substitute floating branch heads for accepted academic inputs.

## Assigned canonical scope

Stable scope: `B1.1-C05`
Canonical cluster: `Giải tích và biến đổi liên tục`

Immutable canonical topic IDs:

1. `B1.1-C05-T01` — Dãy và giới hạn
2. `B1.1-C05-T02` — Tính liên tục
3. `B1.1-C05-T03` — Đạo hàm
4. `B1.1-C05-T04` — Tích phân
5. `B1.1-C05-T05` — Chuỗi
6. `B1.1-C05-T06` — Giải tích nhiều biến
7. `B1.1-C05-T07` — Giải tích thực
8. `B1.1-C05-T08` — Giải tích phức
9. `B1.1-C05-T09` — Giải tích hàm
10. `B1.1-C05-T10` — Giải tích điều hòa

No topic may be omitted, transferred, renamed, or silently collapsed.

## Required outputs

Create only under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C05/`

Required:

1. `NODES.jsonl`
2. `CLAIMS.jsonl`
3. `SOURCES.jsonl`
4. `LEARNING_OBJECTIVES.jsonl`
5. `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
6. `CROSS_LINKS.jsonl`
7. `CURRICULUM_SEQUENCE_INTENT.jsonl`
8. `RESULT.json`
9. `HANDOFF.md`

Maintain mandatory durable status folder under `CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C05/`.

## Academic closure

- Complete knowledge, minimum redundancy; never target a claim count.
- Claims must be atomic, sourced, scoped, epistemically classified, certainty-labelled, and academically defensible.
- D1–D4 are epistemic depth and independent of age.
- Every Learning Objective must map to explicit supporting Claim IDs.
- No Learning Objective may require an academic claim from a locked/unopened scope.
- If closure exposes a missing proposition, add the minimum sourced claim rather than weakening the objective merely to pass.
- Prefer primary/scholarly/institutional/version-stable sources; pin online lock-critical identities where practicable.

## Mandatory ownership boundaries

### Accepted C02/C03

Reuse rather than duplicate:

- number systems, scalar arithmetic/order, estimation primitives — C02;
- equations/functions/algebraic structure, vector spaces/matrices — C03.

### C04 geometry — currently LOCKED

C05 must not take primary ownership of Euclidean/analytic/projective/differential/algebraic geometry.

Geometric interpretations of derivative/integral may appear only as examples or boundary links and may not supply support claims.

### C06 differential equations — LOCKED

C05 owns calculus/analysis primitives; C06 owns ODE/PDE/dynamical-system curriculum. Differential equations may appear only as applications/boundaries.

### C07 probability/statistics — LOCKED

If real analysis introduces measure/integration foundations, C07 later owns probability-measure specialization, stochastic meaning, statistics and inference. Do not author probability curriculum here.

### C09 topology — LOCKED

C05 may use analysis-specific metric/open/compact concepts when required for analysis, but generic topology/manifold/topological invariants remain C09 ownership. Record typed boundary links.

### C10 applied/computational math — LOCKED

Numerical methods, optimization algorithms and simulation are future ownership; do not substitute them for exact analysis.

## High-risk internal boundaries

Explicitly disposition at least:

- T01 limits vs T02 continuity;
- T03 derivative vs T06 multivariable derivative;
- T04 elementary/Riemann integration vs T07 real-analysis/Lebesgue-style foundations where included;
- T05 sequences/series vs T10 Fourier-series/harmonic meaning;
- T07 real analysis vs T09 functional analysis;
- T08 complex analysis vs T10 harmonic analysis.

## PASS gate

Candidate PASS requires:

- all 10 canonical topics covered;
- stable IDs unique;
- node fields complete;
- claims source-resolved and epistemically scoped;
- exactly one D1–D4 objective per node unless the accepted standard explicitly permits more;
- 100% Claim→Learning-Objective closure;
- zero future/locked-scope support Claim IDs;
- source identity/version audit PASS;
- semantic duplicate/ownership audit PASS against accepted C01–C03 and current C05;
- prerequisite/sequence graph acyclic and academically valid;
- C04 remains untouched/locked;
- no Lesson Registry, prompts, images, R2, delivery, website, or `ACADEMIC_LOCKED` artifacts;
- committed academic-closure and pre-PASS checkpoints;
- `RESULT.json.status=PASS` and `STATUS.json.status=PASS` agree.

Worker PASS is candidate only. It must not mutate control-plane or unlock C04.

On PASS:
`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C04 — GATED pending Director acceptance of C05`
