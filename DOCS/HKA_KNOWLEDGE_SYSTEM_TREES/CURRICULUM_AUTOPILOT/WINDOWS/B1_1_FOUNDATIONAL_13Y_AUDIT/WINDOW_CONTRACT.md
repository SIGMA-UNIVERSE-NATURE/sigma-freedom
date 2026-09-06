# WINDOW CONTRACT — B1.1 FOUNDATIONAL 13-YEAR COVERAGE AUDIT

Status: READY_CONTRACT  
Stage: `CURRICULUM`  
Audit target: `B1.1 — Toán học & Hệ hình thức`  
Execution branch: `hka-tree/b1-1-foundational-13y-audit`

## Purpose

Determine whether accepted B1.1 C01-C10 fully cover the foundational understandings accumulated across a learner's 13-year general-education journey, without allowing university/advanced content to substitute for missing foundational concepts.

## Inputs

- Canonical HKA World Tree at `fc799bf1104ab6352710e1801777a971b5179995`.
- Immutable B1 scope map at architecture commit `265bb584b5d7e36e11091289d58558408880118c` / blob `bedef47958a728e3f0d56d412f7bdea3ec465856`.
- Director-accepted B1.1 C01-C10.
- `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`.
- `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_AMENDMENT_1.md`.

## Hard rules

- D1-D4 remain age-independent academic depth; do not reinterpret them as grade bands.
- Foundational 13-year coverage is a separate axis.
- Advanced/university/research content cannot offset a missing foundational concept.
- Audit the full general-education progression, not only upper-secondary or university preparation.
- Use external curriculum mappings from multiple education systems across at least five continents; Vietnam cannot be the sole baseline.
- Do not copy external curricula mechanically; use them as coverage evidence against HKA's canonical knowledge ownership.
- Every identified gap must be assigned to the true existing owner C/topic when possible. Do not patch gaps into the currently active audit window or create semantic duplicates.
- Stable accepted IDs remain append-only. Any repair must use explicit Director amendment/overlay or owner-scope extension without silent renumbering.
- No B1.2 authoring and no post-CURRICULUM stage.

## Required audit dimensions

At minimum inspect whether B1.1 covers foundational progression for:

1. counting, place value, arithmetic operations, mental/written strategies;
2. fractions, decimals, percentages, ratios, rates, proportional reasoning;
3. estimation, magnitude, number sense and units where mathematical;
4. patterns, expressions, equations, inequalities and functional thinking;
5. coordinate representation, tables, graphs and multiple representations;
6. shape, spatial reasoning, transformations, measurement, perimeter/area/volume, angle and trigonometric foundations;
7. data collection/representation, descriptive statistics, probability, sampling and uncertainty foundations;
8. logic, reasoning, proof habits, counterexamples and mathematical communication;
9. discrete counting/combinatorial reasoning where part of general education;
10. modeling, numerical approximation and practical mathematical decision/problem-solving foundations;
11. prerequisite progression and conceptual transitions across the 13-year span;
12. common misconceptions or missing bridge concepts that advanced claims could otherwise conceal.

This list is minimum audit surface, not a new taxonomy and not permission to duplicate content.

## Output

Produce durable:

- `FOUNDATIONAL_13Y_COVERAGE_MATRIX.jsonl`
- `FOUNDATIONAL_GAPS.jsonl`
- `EXTERNAL_CURRICULUM_MAPPINGS.jsonl`
- `AUDIT_REPORT.md`
- checkpoint/status files.

Every gap record must include:

- gap_id
- foundational_learning_meaning
- evidence_from_external_curricula
- current_HKA_owner_scope
- current_HKA_supporting_claim_or_objective_ids if partial
- gap_type: MISSING | TOO_ADVANCED_WITHOUT_BRIDGE | SEQUENCING_GAP | REPRESENTATION_GAP | PRACTICE/UNDERSTANDING_GAP
- severity
- repair_owner_scope
- repair_action
- duplicate_risk

## PASS gate

`FOUNDATIONAL_GAP_COUNT = 0`

and

- at least five continents represented in benchmark evidence;
- full 13-year general-education progression represented;
- external mappings integrated;
- no unresolved owner ambiguity;
- no repair creates semantic duplicate meaning.

Only Director may declare this audit PASS and only then may B1.1 be marked complete or B1.2 be considered for opening.
