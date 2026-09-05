# B1.1 Foundational 13-Year Coverage Audit Protocol

Status: `ACTIVE`

Stage: `CURRICULUM`

Scope: accepted `B1.1-C01` through `B1.1-C10`.

This audit implements `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_AMENDMENT_1.md` and `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json`.

## Purpose

Verify that B1.1 preserves the full foundational mathematical understanding developed across a learner's general-education journey, rather than allowing university/research-level material to displace elementary or secondary foundations.

`D1-D4` remain academic-depth labels and are not school-grade labels.

## Benchmark rule

Use full general-education progressions, not university syllabi, from multiple systems across at least five continents. Current benchmark set:

- Europe: England national curriculum mathematics, Years 1-11 / Key Stages 1-4.
- North America: US Common Core Mathematics, Kindergarten-Grade 8 plus high-school domains.
- Oceania: Australian Curriculum Mathematics F-10 plus senior-secondary pathway distinction.
- Asia: Singapore Primary 1-6 and Secondary Mathematics syllabuses.
- South America: Brazil BNCC Mathematics across Ensino Fundamental and Ensino Médio.
- Africa: South Africa CAPS Mathematics across Foundation, Intermediate, Senior and FET phases.

No single national curriculum is treated as the universal truth. A foundational requirement is high-confidence when it recurs across several systems or is necessary to make later accepted HKA meaning learnable.

## Audit dimensions

1. number sense, counting, cardinality and place value;
2. arithmetic meanings, fluency, mental/written strategies and reasonableness;
3. fractions, decimals, ratios and percentages from concrete meaning to formal structure;
4. pattern, equality, unknowns, early algebra and function/graph progression;
5. everyday measurement and units, including time, money, mass/capacity and scale/conversion;
6. elementary 2-D/3-D shape, spatial relations, position/direction, transformations and coordinates;
7. data collection, classification, tables, charts/graphs, scales and descriptive interpretation;
8. elementary chance/probability from experiment and relative frequency to formal probability;
9. mathematical problem solving, estimation, modelling and checking reasonableness;
10. upper-secondary consolidation and optional/advanced pathways without making advanced content the common baseline.

## Coverage statuses

- `FULL`: accepted HKA claims/objectives already cover the foundational meaning.
- `PARTIAL`: related content exists but an essential foundational learning meaning is absent.
- `GAP`: the required foundational meaning is not represented in the effective accepted curriculum.
- `NOT_OWNER`: meaning belongs elsewhere in the HKA tree and must not be patched into B1.1.

## Repair rule

A concrete gap reopens only its true owner scope through an explicit append-only Director foundational amendment. Existing accepted IDs are never renumbered or silently rewritten.

Repairs must use a separate foundational coverage axis and must not overload the existing four D1-D4 anchor objectives into giant school-grade objectives.

A repair may add:

- atomic foundational claims under the existing owner node;
- fine-grained `FOUNDATIONAL_OBJECTIVE` records mapped to those claims;
- external curriculum mappings by system/year or phase;
- prerequisite links and misconceptions/representation notes needed for later Lesson Registry.

The existing canonical topic/node remains the owner. No extra C scope is created merely to patch school-level coverage.

## Exit gate

B1.1 is complete only when:

- every high-confidence foundational item is `FULL` after repairs;
- `FOUNDATIONAL_GAP_COUNT = 0`;
- all repairs resolve to true owners without semantic duplication;
- the accepted C01-C10 chain plus Director overlays remains academically consistent;
- Backup Sentinel returns `TREE_ALIGNMENT_PASS`.

Until then B1.2 remains locked.
