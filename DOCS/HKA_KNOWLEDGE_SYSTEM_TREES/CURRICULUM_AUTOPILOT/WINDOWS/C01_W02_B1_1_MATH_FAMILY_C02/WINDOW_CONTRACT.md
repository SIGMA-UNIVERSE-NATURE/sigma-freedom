# Window Contract — C01-W02-B1.1-MATH-FAMILY-C02

## Mission

Author the complete HKA `CURRICULUM` record set for stable scope `B1.1-C02 — Số học và lý thuyết số` only.

This is the second bounded child of `C01-W02-B1.1-MATH-FAMILY`. It must not expand into another stable scope or any later pipeline stage.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Execution branch: `hka-tree/c01-w02-math-c02`
- Director-accepted predecessor candidate to be recorded by control-plane acceptance: `5659288da80a239e2ded408da87348670c1410c2`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md@fc799bf1104ab6352710e1801777a971b5179995`
- Required predecessor standards:
  - `CURRICULUM/B1_RULES_REALITY/B1_SCOPE_MAP.json`
  - `CURRICULUM/B1_RULES_REALITY/B1_ID_AND_RECORD_STANDARD.md`
  - `CURRICULUM/B1_RULES_REALITY/B1_AUTHORING_SEQUENCE.md`
  - `CURRICULUM/B1_RULES_REALITY/B1_DUPLICATE_CONTROL.md`
- Prior accepted detailed child records: all accepted `B1.1-C01` outputs at commit `5659288da80a239e2ded408da87348670c1410c2`.

Do not substitute floating branch heads for pinned academic inputs.

## Assigned canonical scope

Stable scope: `B1.1-C02`
Canonical cluster: `Số học và lý thuyết số`
Primary owner window: `C01-W02-B1.1-MATH-FAMILY-C02`

Immutable canonical topics:

1. `B1.1-C02-T01` — Số tự nhiên, số nguyên và phân số
2. `B1.1-C02-T02` — Số hữu tỉ, vô tỉ, thực và phức
3. `B1.1-C02-T03` — Phép toán và thứ tự
4. `B1.1-C02-T04` — Ước lượng và độ lớn
5. `B1.1-C02-T05` — Tỉ lệ, phần trăm và tỉ suất
6. `B1.1-C02-T06` — Chia hết và số nguyên tố
7. `B1.1-C02-T07` — Đồng dư
8. `B1.1-C02-T08` — Lý thuyết số hiện đại

No assigned topic may be omitted, transferred, silently collapsed, or used to author another scope.

## Required outputs

Create only under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C02/`

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

## Academic completeness

The objective is complete foundational coverage with minimum redundancy; there is no target record count.

- Every canonical topic must receive academically adequate node/claim coverage.
- Claims must be atomic, sourced, scoped, epistemically classified and certainty-labelled.
- Internal HKA ownership/governance statements belong in boundary metadata/cross-links, not inside an externally sourced academic proposition unless the proposition itself is academic.
- D1–D4 are epistemic depths independent of age.
- Every learning objective must describe observable understanding.
- Every learning objective must have an explicit closure row listing the committed `supporting_claim_ids` that actually establish the knowledge needed by that objective.
- `SUPPORTED_BY_CLAIMS=true` is permitted only when every listed support claim resolves and the objective requires no academic proposition from an unlocked scope.
- Misconceptions, counterexamples, errors/limits and open questions must be represented where academically meaningful.

## Source discipline

Use real scholarly/institutional sources. Prefer DOI/ISBN/standard/repository commit/archive/versioned institutional locators. For lock-critical web or open-text sources, pin an immutable/versioned identity where practicable. Moving landing pages alone are not sufficient when an exact archival/version identity is available.

Deterministic `SOURCE_ID` rules in `B1_ID_AND_RECORD_STANDARD.md` remain mandatory.

## Duplicate and predecessor control

Run semantic duplicate comparison against:

1. all records authored in C02;
2. accepted C01 records at `5659288da80a239e2ded408da87348670c1410c2`;
3. architecture duplicate/risk register.

Identity test:

`NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`

A different age, example, notation, language or activity wrapper does not create new learning meaning.

C02 may use logic/set/proof foundations from C01 as prerequisites or links; it must not re-author C01 learning objectives under arithmetic scenery.

## Curriculum boundary

Allowed future `LSREF-*` values are sequencing placeholders only.

Forbidden: Lesson Registry, `LESSON_ID`, visual descriptions/prompts, images, R2, delivery, website changes, or any academic/global lock.

## Durable status

Maintain:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C02/`

with `STATUS.json`, `REPORT.md`, and append-only `CHECKPOINTS/`.

A replacement window must recover solely from GitHub state, pinned commits, status/checkpoints, outputs and this contract.

## PASS gate

PASS requires:

- 8/8 canonical topics accounted for;
- stable IDs valid and non-colliding;
- node minimum fields complete;
- all claims correctly sourced/classified/scoped;
- D1–D4 complete and age-independent;
- `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl` has exactly one row per learning objective, no missing support Claim IDs and no unlocked-scope academic dependency;
- immutable/versioned source audit PASS where practicable;
- semantic duplicate scan against accepted C01 and C02 PASS;
- prerequisite graph/sequence valid;
- no later-stage artifacts;
- pre-PASS checkpoint exists;
- `RESULT.json.status=PASS`, `STATUS.json.status=PASS`, and `REPORT.md` agree.

A child PASS remains a candidate until independent Director acceptance.

On candidate PASS, `next_action` must be `C01-W02-B1.1-MATH-FAMILY-C03 — GATED pending Director acceptance of C02`.

Allowed non-PASS outcomes: `BLOCKED_INPUT`, `BLOCKED_CONTRADICTION`, `REVIEW_REQUIRED`.