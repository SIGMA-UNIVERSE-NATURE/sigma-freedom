# HKA Foundational 13-Year Coverage Amendment 2 — Fine-Grained Foundational Objective Layer

Status: `ACTIVE`

Stage: `CURRICULUM`

Authority: higher-version continuation of `HKA_FOUNDATIONAL_13_YEAR_COVERAGE_AMENDMENT_1.md`.

## 1. Purpose

The accepted C scopes use one canonical D1, D2, D3 and D4 Learning Objective per canonical node as academic-depth anchors. The 13-year audit shows that forcing every missing school-level meaning into those four anchor objectives would make them too broad and would recreate the curriculum-overload problem this gate is intended to prevent.

Therefore HKA adds a separate, append-only `FOUNDATIONAL_OBJECTIVE` layer.

## 2. D1-D4 remain unchanged in meaning

- D1-D4 remain academic-depth labels and are age-independent.
- Existing accepted canonical D1-D4 Learning Objective IDs are not renumbered or silently rewritten.
- A foundational objective declares its own `academic_depth` but is not a new universal school grade.
- General-education progression is tracked by a separate `foundation_band` and per-system external mappings.

## 3. Foundational objective identity

Stable ID pattern:

`HKA-F13-<scope>-<node>-FLO-<nnn>`

Example:

`HKA-F13-B1-1-C02-N001-FLO-001`

Required fields:

- `foundational_objective_id`
- `owner_scope_id`
- `owner_node_id`
- `canonical_topic_ids`
- `academic_depth` (`D1`–`D4`)
- `foundation_band`
- `objective`
- `supporting_claim_ids`
- `prerequisite_foundational_objective_ids`
- `external_curriculum_mappings`
- `common_spine_required`
- `misconceptions_or_representation_notes`
- `record_version`

Foundation bands are descriptive progression bands, not universal ages:

- `EARLY_FOUNDATION`
- `DEVELOPING_FOUNDATION`
- `CONSOLIDATING_FOUNDATION`
- `UPPER_SECONDARY_FOUNDATION`

A jurisdiction-specific mapping may map a foundational objective to a grade/year/phase without claiming that mapping is universal.

## 4. Foundational claim repair

A confirmed gap may add new atomic claims to the effective owner node through a Director foundational overlay.

Rules:

- use new append-only Claim IDs under the existing owner node;
- never reuse or renumber an accepted Claim ID;
- source and scope-limit every added claim;
- mark the overlay as `FOUNDATIONAL_13_YEAR_REPAIR`;
- do not duplicate an accepted claim merely to use simpler wording;
- if an accepted claim already supports the foundational objective, reference it directly.

Effective academic content for a repaired scope is:

`accepted_scope_head + active Director academic amendments + active foundational repair overlays`.

## 5. Lesson Registry consequence

This amendment does not open Lesson Registry now.

When Lesson Registry eventually opens after global `ACADEMIC_LOCKED`:

- every `common_spine_required=true` foundational objective must map to at least one effective lesson or an explicitly justified shared lesson;
- advanced canonical D3/D4 or specialist objectives may become extension/deeper pathways and are not automatically mandatory for the common general-education spine;
- lesson count follows learning need, not theorem count;
- no grade is forced merely from academic depth.

## 6. Repair location

Foundational repair overlays live under:

`CURRICULUM_AUTOPILOT/FOUNDATIONAL_AUDITS/<audit>/REPAIRS/<scope>/`

Each repaired scope must have:

- `CLAIMS_FOUNDATIONAL_AMENDMENT_<n>.jsonl` when new claims are required;
- `FOUNDATIONAL_OBJECTIVES_<n>.jsonl`;
- `EXTERNAL_CURRICULUM_MAPPINGS_<n>.jsonl` or equivalent mapping inside objective records;
- `REPAIR_AUDIT_<n>.json`.

## 7. Exit gate

A gap closes only when:

- every required meaning has direct accepted/effective Claim support;
- every foundational objective is fine-grained enough for later lesson derivation;
- external mappings demonstrate the general-education need;
- no false ownership transfer or semantic duplicate is introduced;
- Director audit passes.

B1.2 remains locked until all B1.1 foundational gaps close and `FOUNDATIONAL_GAP_COUNT=0`.
