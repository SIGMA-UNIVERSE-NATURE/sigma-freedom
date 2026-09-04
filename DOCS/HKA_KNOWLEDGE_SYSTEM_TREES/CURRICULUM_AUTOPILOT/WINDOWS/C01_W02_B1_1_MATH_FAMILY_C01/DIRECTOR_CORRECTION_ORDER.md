# DIRECTOR CORRECTION ORDER — C01-W02-B1.1-MATH-FAMILY-C01

Director decision: `REVIEW_REQUIRED`
Candidate terminal commit reviewed: `359359ae5663f5a62383c1774c2ff359ccb092a7`
Successor `C01-W02-B1.1-MATH-FAMILY-C02`: `LOCKED`

This order reopens only the academic closure gaps in C01. Do not re-author the scope or renumber existing IDs.

## Required repair set

1. `HKA-B1-1-C01-N001` — append sourced atomic claim(s) that explicitly close propositional syntax/well-formed-formula formation and distinguish syntax from valuation/truth semantics. Preserve existing claim IDs.

2. `HKA-B1-1-C01-N003` — append the minimum sourced atomic claim(s) needed to support the existing D3 objective on axiomatic set existence, especially restricted separation/set-existence principles versus unrestricted comprehension. Do not broaden into a full axiomatic-set-theory course.

3. `HKA-B1-1-C01-N008` — append sourced atomic claim(s) defining the decidability distinction required by D2 while preserving R04: detailed computability/automata/Church-Turing/complexity remains `B1.5-C02`.

4. Replace moving Open Logic Project landing/build references as lock-critical source identities with immutable source locators where practicable (exact `OpenLogicProject/OpenLogic` commit/tag or another versioned/archived scholarly locator). If normalized source identity changes, mint a new deterministic `SOURCE_ID` and update claim references; never keep a deterministic ID that no longer matches its normalization basis.

5. Add/produce a claim-to-learning-objective closure audit for all 32 objectives. Each objective must list supporting claim IDs and resolve `SUPPORTED_BY_CLAIMS=true`. Lesson Registry must not need to invent new academic propositions after `ACADEMIC_LOCKED`.

## Re-audit gates

All prior gates must remain PASS, plus:
- `claim_to_learning_objective_closure = PASS`
- `immutable_source_pin = PASS`
- `director_identified_gaps = 0`
- `R04 = PASS`
- `semantic_duplicate_scan = PASS`
- `prerequisite_and_sequence = PASS`
- `stage_boundary = PASS`

Do not return PASS unless committed files satisfy every gate.

Allowed terminal outcomes: `PASS`, `REVIEW_REQUIRED`, `BLOCKED_INPUT`, `BLOCKED_CONTRADICTION`.

On repaired PASS, `next_action` must remain exactly `C01-W02-B1.1-MATH-FAMILY-C02`, but C02 is not unlocked until independent Director acceptance.
