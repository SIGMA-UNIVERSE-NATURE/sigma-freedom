# WINDOW CONTRACT — C01-W02-B1.1-MATH-FAMILY-C04

## Identity

- Window: `C01-W02-B1.1-MATH-FAMILY-C04`
- Stage: `CURRICULUM`
- Scope: `B1.1-C04 — Hình học và đo lường`
- Execution branch: `hka-tree/c01-w02-math-c04`
- Director-accepted predecessor: `9c743ab4d5b5ad2ed18000af6a3b80bdace81e16`
- Accepted C03 academic predecessor: `7546ad74fb0e71ad2120c7091947993690bef82d`
- Accepted C02: `cfd9746e2296280705e2e2e67b2c5980d440f02d`
- Accepted C01: `5659288da80a239e2ded408da87348670c1410c2`
- Canonical tree: `fc799bf1104ab6352710e1801777a971b5179995`
- Active dependency amendment: `B1_1_MATH_EXECUTION_DEPENDENCY_AMENDMENT_1.md`

## Canonical topics — exact and frozen

1. `B1.1-C04-T01` — Hình dạng và kích thước
2. `B1.1-C04-T02` — Độ dài, diện tích và thể tích
3. `B1.1-C04-T03` — Góc và lượng giác
4. `B1.1-C04-T04` — Hình học Euclid
5. `B1.1-C04-T05` — Hình học giải tích
6. `B1.1-C04-T06` — Phép biến hình và đối xứng
7. `B1.1-C04-T07` — Hình học xạ ảnh
8. `B1.1-C04-T08` — Hình học vi phân
9. `B1.1-C04-T09` — Hình học đại số

Do not renumber, rename, split, merge or transfer primary ownership of these canonical topic IDs.

## Required academic outputs

Create under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C04/`

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

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C04/`

with `STATUS.json`, `REPORT.md`, and substantive checkpoints.

## Academic record rules

- Complete knowledge, minimum redundancy. Do not target a claim/node count.
- Preserve all accepted C01/C02/C03/C05 IDs and learning meanings; reference them instead of duplicating them.
- Claims must be atomic, sourced, scoped, epistemically classified and certainty-labelled.
- Lock-critical sources must use immutable or explicit version/edition identities where practicable.
- D1–D4 are epistemic depths independent of age.
- Exactly one D1, D2, D3 and D4 Learning Objective per node unless a later Director amendment explicitly changes this contract.
- Every Learning Objective must have exactly one closure row with explicit supporting Claim IDs.
- Candidate PASS requires `100%` Claim → Learning Objective closure.
- No support Claim ID may come from a locked/future scope.
- Future scope references are boundary/cross-link metadata only.
- Sequence/prerequisite graph must be acyclic and may depend only on accepted predecessors or earlier nodes in this C04 scope.
- Worker PASS is candidate only. It does not mutate control-plane or unlock any successor.

## Mandatory ownership / duplicate-control boundaries

### T01 ↔ T04 — shape/size vs Euclidean geometry
T01 owns primitive geometric shape, congruence/similarity-scale intuition and size descriptors at the bounded geometry-entry level. T04 owns axiomatic Euclidean incidence/parallelism/congruence theorems and proof structure. Do not duplicate the same proposition/objective under both topics.

### T02 ↔ C02 / B1.2 physical measurement
T02 owns geometric length/area/volume and geometric measurement formulas/structure. C02 retains arithmetic approximation/error primitives. B1.2-C01 retains physical metrology, instruments, uncertainty and standards. Geometric measure must not become physical-measurement curriculum.

### T03 ↔ C03 functions / C05 analysis
T03 owns angle, radian measure, trigonometric ratios/identities and geometric trigonometry. C03 owns generic algebraic function behavior; C05 owns analytic limit/derivative/integral properties. Do not re-author generic function or calculus foundations as trigonometry.

### T05 ↔ C03 algebra/functions / C05 calculus
T05 owns coordinate/analytic geometry: coordinate representations of lines, conics, distances, loci and algebra-geometry translation. C03 owns algebraic equation/function primitives; C05 owns differential/integral analysis. Use them as accepted prerequisites only.

### T06 ↔ C03 group theory
T06 owns geometric transformations, isometries/similarities/affine transformations and symmetry as geometric actions. C03-T06 retains abstract group axioms, homomorphisms, quotients and actions. Geometric symmetry examples must not duplicate abstract-group learning objectives.

### T07 ↔ T05/T06
T07 owns projective incidence, homogeneous coordinates, projective transformations, points at infinity and projective invariants. Coordinate algebra and generic transformation machinery remain prerequisites/interfaces, not duplicate ownership.

### T08 — Differential geometry dependency lock
T08 may use accepted C05 derivative/multivariable-calculus primitives and accepted C03 linear algebra. It may own calculus-based local differential geometry of curves/surfaces, tangent objects, curvature, parametrization and metric/shape quantities within the bounded C04 scope.

`B1.1-C09` remains LOCKED. Generic topological spaces, manifold foundations, differential topology and global topology must NOT be used as support claims. If manifold/topological language is mentioned, it is boundary-only unless the needed fact is fully established inside C04 without importing locked C09 claims.

### T09 — Algebraic geometry dependency lock
T09 may use accepted C03 ring/field/commutative-algebra claims, including polynomial rings, ideals and Spec/Zariski primitives already accepted there, plus C04 projective-geometry primitives. It owns geometric interpretation of algebraic sets/varieties and bounded algebraic-geometry structure.

Do not import locked C09 generic topology as support. Do not duplicate C03 commutative-algebra definitions as new primary claims when a cross-link/reference suffices.

## Stage boundary

During this window, do NOT create or modify:

- B1.1-C06/C07/C08/C09/C10 academic records
- any B1.2+ academic family
- `ACADEMIC_LOCKED`
- Lesson Registry
- prompts
- images
- R2 staging/vault/delivery
- website artifacts
- curriculum control-plane state/registry

## PASS gate

Candidate `PASS` is allowed only after committed GitHub read-back verifies:

1. exact 9/9 topic coverage;
2. stable/unique/referentially valid IDs;
3. academically correct and sufficiently scoped claims;
4. source provenance/version identity and deterministic source IDs;
5. D1–D4 coverage;
6. 100% Claim → Learning Objective closure;
7. all mandatory ownership boundaries dispositioned;
8. acyclic prerequisites/sequence with zero locked-scope prerequisites/support claims;
9. stage-boundary diff clean;
10. substantive pre-PASS checkpoint exists before terminal candidate PASS.

If any uncertainty remains, use `REVIEW_REQUIRED`; never force PASS.
