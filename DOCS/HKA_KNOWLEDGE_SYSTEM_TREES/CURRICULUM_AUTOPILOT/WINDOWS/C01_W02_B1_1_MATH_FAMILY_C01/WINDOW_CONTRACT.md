# Window Contract — C01-W02-B1.1-MATH-FAMILY-C01

## Mission

Author the complete HKA `CURRICULUM` record set for stable scope `B1.1-C01 — Logic, tập hợp và chứng minh` only.

This is the first bounded child of `C01-W02-B1.1-MATH-FAMILY`. It is not a whole-mathematics window and it must not expand into another stable scope.

## Immutable inputs

- Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
- Execution branch: `hka-tree/c01-w02-math-c01`
- Accepted predecessor commit: `265bb584b5d7e36e11091289d58558408880118c`
- Canonical HKA tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
- Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
- Current control plane: branch `hka-tree/curriculum-master`
- Required predecessor standards at the accepted predecessor commit:
  - `CURRICULUM/B1_RULES_REALITY/B1_SCOPE_MAP.json`
  - `CURRICULUM/B1_RULES_REALITY/B1_ID_AND_RECORD_STANDARD.md`
  - `CURRICULUM/B1_RULES_REALITY/B1_AUTHORING_SEQUENCE.md`
  - `CURRICULUM/B1_RULES_REALITY/B1_DUPLICATE_CONTROL.md`
  - `CURRICULUM/B1_RULES_REALITY/RESULT.json`
  - `CURRICULUM/B1_RULES_REALITY/HANDOFF.md`

The accepted predecessor SHA is pinned. Do not substitute a floating branch head.

## Assigned canonical scope

Stable scope: `B1.1-C01`
Canonical cluster: `Logic, tập hợp và chứng minh`
Primary owner window: `C01-W02-B1.1-MATH-FAMILY-C01`

The eight assigned canonical topic IDs are immutable:

1. `B1.1-C01-T01` — Logic mệnh đề
2. `B1.1-C01-T02` — Logic vị từ
3. `B1.1-C01-T03` — Lý thuyết tập hợp
4. `B1.1-C01-T04` — Quan hệ và ánh xạ
5. `B1.1-C01-T05` — Tiên đề và hệ hình thức
6. `B1.1-C01-T06` — Chứng minh và phản ví dụ
7. `B1.1-C01-T07` — Lý thuyết mô hình
8. `B1.1-C01-T08` — Những giới hạn của hệ hình thức

No assigned topic may be omitted, transferred, renamed into another scope, or silently collapsed.

## Required academic outputs

Create only under:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM/B1_RULES_REALITY/AUTHORING/B1.1/C01-W02-B1.1-MATH-FAMILY-C01/`

Required files:

1. `NODES.jsonl`
2. `CLAIMS.jsonl`
3. `SOURCES.jsonl`
4. `LEARNING_OBJECTIVES.jsonl`
5. `CROSS_LINKS.jsonl`
6. `CURRICULUM_SEQUENCE_INTENT.jsonl`
7. `RESULT.json`
8. `HANDOFF.md`

Every record must obey `B1_ID_AND_RECORD_STANDARD.md` exactly.

## Academic completeness

The goal is complete foundational coverage with minimum redundancy, not a target number of records.

For this scope:

- Every assigned canonical topic ID must be represented by academically adequate node/claim coverage.
- Every node must satisfy the minimum HKA node record fields defined by the accepted standard.
- Claims must be atomic enough for epistemic class, certainty, scope limits, and source traceability.
- Every claim must cite one or more real source IDs unless it is explicitly a non-factual humanistic/metaphorical record permitted by the standard; do not fabricate sources.
- Source records must contain verifiable bibliographic metadata and stable/persistent locators where available.
- D1–D4 must all be explicit. Depth is independent of age.
- Learning objectives must describe observable understanding, not an activity wrapper or future image scene.
- `presentation_pathways` may express age-appropriate presentation, but age must not redefine epistemic depth.
- Misconceptions, counterexamples, limitations, and open/debated questions must be represented where academically meaningful.

## Boundary and duplicate control

Mandatory risk disposition: `R04` from `B1_DUPLICATE_CONTROL.md`.

`B1.1-C01` owns mathematical logic, set/foundational, axiomatic, proof, and model-theoretic claims.

It must NOT take primary ownership of:

- computability as a computing-theory curriculum domain;
- formal-language/automata curriculum owned by B1.5;
- program verification/software-engineering curriculum owned by B1.5.

Where those are natural consequences or applications, use typed prerequisites/cross-links and record `OVERLAP_REVIEW` / `CROSS_LINK_NOT_DUPLICATE` dispositions instead of reteaching another scope unchanged.

Within this child, perform semantic duplicate detection using:

`NODE MEANING + CLAIM SET + LEARNING OBJECTIVE + CONTEXT`

Changing wording, examples, age pathway, notation, or future presentation does not create a new learning meaning.

## Curriculum boundary

This window may create future `LSREF-*` sequencing references only as non-registry placeholders.

Forbidden:

- `LESSON_ID` records;
- Lesson Registry authoring;
- visual descriptions or image prompts;
- image generation;
- R2 actions;
- web-optimization/delivery outputs;
- website routes or publication changes;
- setting B1 or global `ACADEMIC_LOCKED`.

## Durable status folder — mandatory

Maintain:

`DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT/STATUS_REPORTS/C01-W02-B1.1-MATH-FAMILY-C01/`

Required:

- `STATUS.json`
- `REPORT.md`
- `CHECKPOINTS/`

At minimum create/update checkpoints after meaningful academic work and a final pre-PASS audit checkpoint.

`NO STATUS FOLDER = NO ACCEPTED COMPLETION`.

A replacement window must be able to resume solely from GitHub state, this folder, and committed outputs. Chat history is not project state.

## PASS gate

PASS requires all of the following:

- all 8 canonical topic IDs accounted for;
- stable IDs valid and non-colliding;
- node minimum fields complete;
- claims have epistemic class, certainty, scope limits, and real source traceability;
- D1–D4 learning objectives complete and not age-coded;
- R04 explicitly dispositioned in `CROSS_LINKS.jsonl`;
- semantic duplicate scan PASS;
- prerequisite/sequence references valid;
- no later-stage artifacts authored;
- pre-PASS checkpoint exists;
- `RESULT.json.status=PASS` and `STATUS.json.status=PASS` agree;
- `REPORT.md` accurately states finished/remaining work.

On PASS, `next_action` must be exactly:
`C01-W02-B1.1-MATH-FAMILY-C02`.

Allowed non-PASS outcomes are `BLOCKED_INPUT`, `BLOCKED_CONTRADICTION`, or `REVIEW_REQUIRED`. Do not hide uncertainty to force PASS.
