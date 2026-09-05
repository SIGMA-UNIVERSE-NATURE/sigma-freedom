# B1.1 Mathematics Execution Dependency Amendment 2

STATUS: ACTIVE
STAGE: CURRICULUM
SCOPE: B1.1 execution dependency only
CANONICAL TREE: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`
FROZEN B1 SCOPE MAP: `B1_SCOPE_MAP` blob `bedef47958a728e3f0d56d412f7bdea3ec465856` anchored by accepted architecture commit `265bb584b5d7e36e11091289d58558408880118c`

## Director finding

The frozen scope map registers both `B1.1-C07 — Xác suất, thống kê và suy luận` and `B1.1-C08 — Toán rời rạc và tổ hợp`, but the old authoring order would execute C07 before C08.

That order creates avoidable academic duplication risk:

1. `B1.1-C07-T10 — Suy luận nhân quả` at formal/research depth needs causal graph/DAG structure. If C07 is authored before C08, it would either duplicate generic graph foundations or under-author causal inference.
2. `B1.1-C07` formal probability/statistics should reuse already accepted C05 measure/Lebesgue foundations rather than recreate sigma-algebra/measure theory.
3. `B1.1-C08-T07 — Mã sửa lỗi` should reuse already accepted C03 field/linear-algebra primitives while retaining mathematical combinatorial/coding ownership distinct from B1.5 information-channel ownership.

## Corrected execution order

After Director-accepted C06:

`C06 → C08 → C07 → C09 → C10`

This amendment changes execution dependency only. Stable scope IDs, topic IDs, topic names and primary owners are unchanged.

## C08 prerequisite hardening

C08 may reuse:

- accepted C01 logic/proof/set foundations;
- accepted C02 arithmetic/number foundations;
- accepted C03 algebra, finite-field and linear-algebra primitives where required by algebraic/combinatorial coding.

C08 owns discrete/combinatorial mathematical structures, proof-oriented properties and combinatorial optimization formulations. Algorithmic operations/complexity remain B1.5-C03 boundaries; information-channel coding remains B1.5-C01 boundary.

Mandatory risk controls from frozen architecture:

- `R05` — mathematics vs algorithms: OVERLAP_REVIEW;
- `R02` — error-correcting-code overlap: CROSS_LINK_NOT_DUPLICATE.

## C07 prerequisite hardening after C08 acceptance

C07 must reuse:

- accepted C05 measure/Lebesgue foundations for probability-space and random-variable formalization;
- accepted C08 graph/discrete foundations for causal DAG representations where required;
- accepted C01/C02/C03 foundations as already registered.

C07 owns probability/statistical/causal inference meanings. It must not re-author generic measure theory from C05 or generic graph theory from C08.

Mandatory risk controls from frozen architecture:

- `R06` — mathematics/statistics vs data/AI: OVERLAP_REVIEW;
- `R13` — AI mandatory cross-domain node: SECONDARY_CROSS_LINK; B1.5-C10 remains primary for AI computation.

## Gates

- C06 must receive `DIRECTOR_ACCEPTED_PASS` before C08 becomes READY.
- C08 must receive `DIRECTOR_ACCEPTED_PASS` before C07 becomes READY.
- C07/C09/C10 remain locked while C08 is active.
- Worker PASS never unlocks a successor.
- No `ACADEMIC_LOCKED`, Lesson Registry, prompts, images, R2, delivery or website artifact is authorized by this amendment.
