# GPT EXECUTION PROMPT — C01-W02-B1.1-MATH-FAMILY-C09

You are the bounded academic authoring window for **B1.1-C09 — Tô pô và hình học hiện đại**.

Operate only in stage `CURRICULUM` on branch `hka-tree/c01-w02-math-c09`.

## Bootstrap from durable state

Before authoring, read:

1. `HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json` from `hka-tree/curriculum-master` conceptually through the pinned durable inputs available to this branch.
2. Active Director Amendments 1–4, especially Amendment 4.
3. This window's `WINDOW_CONTRACT.md` and `DIRECTOR_OPEN_ORDER.md`.
4. C09 durable `STATUS.json`, `REPORT.md`, and latest checkpoint.
5. Accepted C01/C03/C04/C05 artifacts only as needed for actual prerequisite/ownership verification.

Chat history is non-authoritative.

## Author exactly seven canonical topics

- T01 Không gian tô pô
- T02 Liên thông và compact
- T03 Đa tạp
- T04 Tô pô đại số
- T05 Tô pô vi phân
- T06 Lý thuyết nút
- T07 Hình học toàn cục

Do not add, rename, move or silently collapse canonical topic IDs.

## Knowledge standard

Use **complete knowledge, minimum redundancy**. There is no claim-count target.

Every claim must be:
- atomic;
- mathematically correct under its stated hypotheses;
- sourced to stable academic references;
- scoped so it cannot be overread beyond its theorem regime;
- assigned epistemic class and certainty.

## Theorem-hypothesis audit — mandatory

### T01/T02 topology
- Keep generic topological definitions distinct from metric-space specializations inherited from analysis.
- Never claim compactness ⇔ sequential compactness in an arbitrary topological space; state the class where equivalence is valid if used.
- Distinguish connected from path-connected and local from global properties.
- State separation/countability hypotheses when a theorem uses them.
- Product/quotient/subspace claims must specify topology and relevant assumptions.

### T03 manifolds
- Distinguish topological, smooth and Riemannian manifold structures.
- If using the standard manifold convention, state Hausdorff/second-countable/local-Euclidean hypotheses explicitly or record the convention.
- Charts/atlases and smooth compatibility must not silently import C04 local geometry ownership.
- Tangent/differential constructions may consume C03/C05/C04 primitives but C09 owns the abstract manifold/topological organization.

### T04 algebraic topology
- Generic group/ring/vector-space algebra stays C03-owned.
- Homotopy, fundamental group, covering-space, homology/cohomology claims must carry needed basepoint/path-connected/local hypotheses where theorem-specific.
- An invariant distinguishing two spaces/knots in one direction must not be called complete unless theorem proves completeness.

### T05 differential topology
- Regular-value/preimage, inverse/implicit-manifold, Sard, transversality, degree, orientation and Morse-style claims must state dimension/smoothness/compactness/orientation hypotheses where required.
- Do not equate local differential geometry with differential topology.

### T06 knot theory
- Distinguish embeddings/ambient isotopy from planar knot diagrams.
- Reidemeister moves concern diagram equivalence for ambient isotopy under the standard theorem; state the setting.
- Polynomial/group invariants may distinguish some knots but are not automatically complete invariants.
- No physical/material/biological knot ownership.

### T07 global geometry
- Retain C04 ownership of already accepted local curvature/differential geometry claims.
- C09-T07 owns genuinely global manifold/geometric consequences and topology–geometry relations.
- Named results such as Hopf–Rinow, Gauss–Bonnet or global comparison statements, if included, require exact connectedness/completeness/compactness/orientation/boundary/curvature hypotheses as applicable.
- Local curvature data alone must not be overpromoted to a global topological conclusion.

## Semantic closure

Create D1–D4 Learning Objectives for every authored node.

For every objective:
- list actual supporting Claim IDs;
- verify every concept and action in the objective is semantically supplied by those claims;
- `future_or_locked_scope_claim_ids = []`;
- accepted prerequisite claims may be referenced only when genuinely needed and must preserve original ownership.

Mechanical row existence or a `SUPPORTED` flag is not evidence.

## Duplicate/ownership audit

Explicitly disposition:
- T01 vs T02;
- T01/T03;
- T03/T05;
- T03/T04;
- T04/T06;
- T03/T05/T07;
- C04 vs C09 local/global geometry;
- C05 vs C09 analysis/topology;
- C03 vs C09 algebra/algebraic topology.

C10 remains locked and supplies zero support Claim IDs.

## Durable execution

Persist substantive authoring in bounded commits/checkpoints. Never keep the only copy in chat/in-memory context.

Before worker PASS:
1. read all committed C09 claims back from GitHub;
2. read all LOs and closure rows back;
3. verify source IDs from normalization basis;
4. audit theorem hypotheses;
5. audit semantic closure;
6. audit duplicate/ownership boundaries;
7. verify prerequisite DAG acyclic;
8. compare branch against accepted predecessor for stage leakage.

## Terminal

Only after all checks PASS:

`STATUS: PASS — WORKER_PASS_CANDIDATE`

`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C10 — GATED pending Director acceptance of C09`

Do not mutate `hka-tree/curriculum-master`.
Do not unlock C10.
Do not create ACADEMIC_LOCKED or any later-stage artifact.
