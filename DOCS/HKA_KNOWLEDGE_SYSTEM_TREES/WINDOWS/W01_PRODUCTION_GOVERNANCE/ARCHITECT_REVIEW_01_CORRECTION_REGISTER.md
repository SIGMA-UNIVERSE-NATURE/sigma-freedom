---
title: "HKA W01 Director — Architect Review 01 Correction Register"
version: "1.0"
status: "TARGETED CORRECTION PASS COMPLETE — PENDING ARCHITECT REVIEW 02"
review_source_commit: "f06943624024d492cc0f344e38bc4022d6c2b587"
---

# ARCHITECT REVIEW 01 — CORRECTION REGISTER

This register maps Issue #18 findings to targeted Director corrections. It does not declare Architect acceptance.

| Finding | Severity | Correction | Primary files | Director status |
|---|---|---|---|---|
| HKA-ADR-W01-001 | P0 | B00 bulk gate requires Director consistency PASS **and** Independent Image QA `QA_APPROVED`; reject/block keeps B01+ closed | `IMAGE_PRODUCTION_WINDOW_STANDARD.md`, `DIRECTOR_OPERATING_STANDARD.md`, `DIRECTOR_REVIEW_GATE.md`, `WINDOW_CONTRACT_DIRECTOR_ADDENDUM.md` | ADDRESSED |
| HKA-ADR-W01-002 | P1 | Expanded node anatomy: phenomenon/problem, canonical definition, representations, knowledge formation, errors/limits, HKA Compass, assessment, version history, external mappings; extensible node types | `NODE_CATALOG_TEMPLATE.md` | ADDRESSED |
| HKA-ADR-W01-003 | P1 | Replaced one-axis epistemic list with independent `CERTAINTY` + `CONTENT CLASS`; context/normative/model status separate | `ACADEMIC_PROGRAM_AUTHORING_STANDARD.md`, `NODE_CATALOG_TEMPLATE.md`, `ACADEMIC_TRUTH_PACK_TEMPLATE.md` | ADDRESSED |
| HKA-ADR-W01-004 | P1 | Canonical relation superset restored; direction/inverse/node-type/evidence/duplicate-equivalence semantics explicit | `RELATION_CATALOG_TEMPLATE.md` | ADDRESSED |
| HKA-ADR-W01-005 | P1 | Universal source hierarchy replaced by claim-type source-fitness matrix; stable Claim IDs and claim-to-source records | `SOURCE_REGISTER_TEMPLATE.md` | ADDRESSED |
| HKA-ADR-W01-006 | P1 | Durable Academic Coverage Audit + Academic QA Report required; graph/coverage/claim/source/expert/ownership checks explicit | `ACADEMIC_PROGRAM_AUTHORING_STANDARD.md`, `ACADEMIC_COVERAGE_AUDIT_TEMPLATE.md`, `ACADEMIC_QA_REPORT_TEMPLATE.md`, `DIRECTOR_REVIEW_GATE.md`, `WINDOW_CONTRACT_DIRECTOR_ADDENDUM.md` | ADDRESSED |
| HKA-ADR-W01-007 | P1 | Program→Visual carries claim/source/certainty/content-class/misconception/seen/not-implied/disclosure/truth-lock/expert metadata | `PROGRAM_TO_VISUAL_DIRECTOR_BRIEF_TEMPLATE.md`, `ACADEMIC_TRUTH_PACK_TEMPLATE.md`, `IMG_EXECUTION_PACK_TEMPLATE.md` | ADDRESSED |
| HKA-ADR-W01-008 | P1 | Window Types defined; full content workflow no longer assumed for W02–W64; W61–W64 system QA/integration default preserved | `WINDOW_TYPE_APPLICABILITY_STANDARD.md`, `DIRECTOR_OPERATING_STANDARD.md`, `ACADEMIC_PROGRAM_AUTHORING_STANDARD.md`, `WINDOW_CONTRACT_DIRECTOR_ADDENDUM.md` | ADDRESSED |
| HKA-ADR-W01-009 | P1 | IMG Unit model explicitly deactivated pending canonical amendment; formal amendment proposal defines batch/orchestrator/unit/run/QA semantics | `IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md`, `IMAGE_PRODUCTION_WINDOW_STANDARD.md`, `IMG_EXECUTION_PACK_TEMPLATE.md`, `DIRECTOR_CHANGE_REQUESTS.md` | ADDRESSED — CANONICAL DECISION OPEN |
| HKA-ADR-W01-010 | P2 | Direct-fix provenance + downstream invalidation defined; material changes return to owner Window | `DIRECTOR_FIX_PROVENANCE_TEMPLATE.md`, `DIRECTOR_OPERATING_STANDARD.md`, `DIRECTOR_REVIEW_GATE.md`, `WINDOW_CONTRACT_DIRECTOR_ADDENDUM.md` | ADDRESSED |
| HKA-ADR-W01-011 | P2 | Per-asset origin run/unit/hashes/carry-forward/revalidation required for later complete batch snapshot | `BATCH_ASSET_PROVENANCE_TEMPLATE.md`, `IMAGE_PRODUCTION_WINDOW_STANDARD.md`, `IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md`, `DIRECTOR_REVIEW_GATE.md` | ADDRESSED |

## Open architecture decisions after correction

```text
1. ARCHITECT REVIEW ROUND 2 / DIRECTOR LAYER ACCEPTANCE
2. HKA-CR-W01-DIR-002 — IMG UNIT CANONICAL AMENDMENT: OPEN / NOT ACTIVE
3. HKA-CR-W01-DIR-001 — R2 STAGING AMENDMENT: OPEN / NOT ACTIVE
4. CONCRETE FULL-RESOLUTION IMAGE HANDOFF PATH BEFORE AUTOMATED PRODUCTION: OPEN
```

## Prohibitions maintained

```text
W02 OPENED: NO
IMAGE PRODUCTION: NO
R2 UPLOAD: NO
MERGE: NO
WEBSITE DEPLOY: NO
SELF-DECLARED ACCEPTED: NO
```