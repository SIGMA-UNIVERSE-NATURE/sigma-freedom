# Window Contract — C01-W02-B1.1-MATH-FAMILY-C03

## Mission

Author the complete HKA `CURRICULUM` record set for stable scope `B1.1-C03 — Đại số và cấu trúc` only.

This is the third bounded child of `C01-W02-B1.1-MATH-FAMILY`. It must not expand into C04 or any later stable scope.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Execution branch: `hka-tree/c01-w02-math-c03`
- Director-accepted predecessor commit: `cfd9746e2296280705e2e2e67b2c5980d440f02d`
- Accepted C01 commit: `5659288da80a239e2ded408da87348670c1410c2`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
- Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
- Control plane: `hka-tree/curriculum-master`

Read exact predecessor standards before authoring:

- `CURRICULUM/B1_RULES_REALITY/B1_SCOPE_MAP.json`
- `CURRICULUM/B1_RULES_REALITY/B1_ID_AND_RECORD_STANDARD.md`
- `CURRICULUM/B1_RULES_REALITY/B1_AUTHORING_SEQUENCE.md`
- `CURRICULUM/B1_RULES_REALITY/B1_DUPLICATE_CONTROL.md`

## Assigned canonical topics

1. `B1.1-C03-T01` — Biểu thức và phương trình
2. `B1.1-C03-T02` — Bất phương trình
3. `B1.1-C03-T03` — Hàm và quan hệ
4. `B1.1-C03-T04` — Đại số tuyến tính
5. `B1.1-C03-T05` — Ma trận và không gian vectơ
6. `B1.1-C03-T06` — Nhóm
7. `B1.1-C03-T07` — Vành và trường
8. `B1.1-C03-T08` — Đại số giao hoán
9. `B1.1-C03-T09` — Lý thuyết biểu diễn

No assigned topic may be omitted, transferred, silently collapsed, or replaced by a later-scope topic.

## Required outputs

Create only under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C03/`

Required files:

1. `NODES.jsonl`
2. `CLAIMS.jsonl`
3. `SOURCES.jsonl`
4. `LEARNING_OBJECTIVES.jsonl`
5. `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl`
6. `CROSS_LINKS.jsonl`
7. `CURRICULUM_SEQUENCE_INTENT.jsonl`
8. `RESULT.json`
9. `HANDOFF.md`

## Academic completeness

Complete knowledge, minimum redundancy. Do not target a record count.

Every claim must be atomic enough to carry:

- `epistemic_class`
- `certainty`
- `source_ids`
- `scope_limits`

Every node must meet the canonical HKA minimum record standard. D1–D4 are epistemic depth and are independent of age.

## Mandatory inherited-foundation boundaries

Do not duplicate accepted C01/C02 learning meaning.

- C01 owns generic relation/function foundations, proof logic, set foundations and formal-system foundations.
- C02 owns number systems, arithmetic laws/order, ratio/percent/rate, elementary numerical approximation, divisibility/primes, congruence and the bounded modern-number-theory map.
- C03 may consume those records as prerequisites/cross-links but may not re-author them under algebra scenery.

### High-risk internal overlap — must be explicitly dispositioned

C03 has adjacent topics with natural semantic overlap. PASS requires typed ownership boundaries in `CROSS_LINKS.jsonl` and no duplicate learning objectives.

1. `T03 Hàm và quan hệ` vs accepted C01 `Quan hệ và ánh xạ`: C01 retains generic definitions; C03 owns algebraic/function behavior needed for equations, transformations and algebraic structures.
2. `T04 Đại số tuyến tính` vs `T05 Ma trận và không gian vectơ`: author distinct epistemic jobs. Do not duplicate matrix/vector-space definitions, linear-system procedures, transformations, basis/dimension/eigen concepts under two topic IDs. Record which topic owns each claim/objective and cross-link the other.
3. `T06 Nhóm`, `T07 Vành và trường`, `T08 Đại số giao hoán`, `T09 Lý thuyết biểu diễn`: reuse shared algebraic-structure foundations rather than restating definitions/theorems. Representation theory must consume group/ring and linear-algebra foundations rather than duplicate them.
4. `T01 Biểu thức và phương trình` / `T02 Bất phương trình` must not re-author C02 arithmetic/order rules; they own algebraic manipulation, solution sets and equation/inequality reasoning.

## Claim → Learning Objective closure — mandatory

Create exactly one closure row per Learning Objective. Candidate PASS requires:

- 100% objectives represented exactly once;
- all `supporting_claim_ids` resolve to committed C03 claims or Director-accepted prerequisite claims;
- `requires_unlocked_scope_claims=false` for every row;
- future scopes may appear only in `boundary_references_not_support_claims`;
- if an objective needs a proposition not yet locked as a claim, append the minimum necessary sourced claim before PASS.

## Source discipline

Prefer scholarly textbooks, primary papers, standards, institutional references and persistent DOI/ISBN/version identities. Pin exact online versions/commits/archives for lock-critical web material where practicable.

Do not treat a moving landing page alone as immutable provenance when a stable edition/DOI/commit exists.

## Stage boundary

Forbidden:

- B1.1-C04 or later curriculum authoring;
- Lesson Registry;
- visual descriptions/prompts;
- image production;
- R2;
- delivery/website work;
- `ACADEMIC_LOCKED`.

## Durable status

Maintain:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C03/`

Required: `STATUS.json`, `REPORT.md`, append-only `CHECKPOINTS/`.

Checkpoint after bootstrap/scope lock, after substantial academic closure, and before candidate PASS.

## PASS gate

PASS requires all nine topics covered, stable IDs, academically defensible sourced claims, D1–D4 coverage, 100% Claim→Objective closure, duplicate/ownership boundaries PASS, prerequisite graph valid/acyclic, source identity audit PASS, clean stage boundary and durable status/checkpoints.

Worker PASS is only a candidate. It must not unlock C04 or mutate control-plane.

On candidate PASS:

`NEXT_ACTION: C01-W02-B1.1-MATH-FAMILY-C04 — GATED pending Director acceptance of C03`

Use `REVIEW_REQUIRED` rather than hiding uncertainty.