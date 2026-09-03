---
title: "HKA W01 Director Layer — Architect Independent Review 01"
reviewer: "Canonical Architect / President Layer"
review_version: "1.0"
status: "RETURN_FOR_TARGETED_CORRECTIONS"
language: "vi"
date: "2026-09-03"
base_reference_commit: "5ed62129b8eae603d9d9917ca57a46a03361c909"
director_commit_reviewed: "7f127678153cdbed81a1d78f3b376e33f537054b"
---

# HKA W01 DIRECTOR LAYER — ARCHITECT INDEPENDENT REVIEW 01

## 1. Review decision

```text
DIRECTOR COMMIT REVIEWED:
7f127678153cdbed81a1d78f3b376e33f537054b

DIFF AGAINST ARCHITECT-ACCEPTED REFERENCE:
16 files added
0 accepted files modified
23 commits ahead

FINAL DECISION:
RETURN_FOR_TARGETED_CORRECTIONS

W02 AUTHORIZATION:
NOT YET

IMAGE PRODUCTION:
NOT AUTHORIZED

R2:
NOT AUTHORIZED

MERGE:
NOT AUTHORIZED
```

Director Layer is structurally strong and should be preserved. The review does **not** request a rewrite. It requests targeted corrections before this layer becomes the operating standard inherited by W02 and later content windows.

---

# 2. Items accepted without correction

The following design decisions are accepted in principle:

1. Director Layer is additive and preserves the Architect-Accepted reference byte-for-byte.
2. Academic program must exist before visual authoring.
3. Required core program artifacts are `TREE.md`, `NODE_CATALOG.md`, `RELATION_CATALOG.md`, `SOURCE_REGISTER.md`.
4. D1–D4 are competency depth, not age bands.
5. Program-to-Visual Director Brief is the correct bridge between curriculum and VCU/prompt production.
6. Content Window must not generate images.
7. IMG generation must use exact immutable prompt/manifest/brand references.
8. Official character master must be reloaded for every relevant asset.
9. Generated image must never replace the official character master for the next asset.
10. Maximum two Asset IDs per IMG Unit is accepted as an anti-drift execution concept, subject to the canonical-amendment requirement below.
11. Same repeated generation failure twice triggers root-cause review instead of infinite regeneration.
12. Production Correction Register is useful and correctly scoped.
13. R2 staging was correctly kept as a change request instead of silently changing canonical architecture.
14. Independent Image QA remains separate from Director review.

---

# 3. BLOCKING FINDINGS

## HKA-ADR-W01-001 — P0 — B00 gate conflicts with canonical production gate

### Evidence

Canonical Cloudflare Batch Pipeline states:

```text
Không mở sản xuất hàng loạt trước khi B00 đạt independent QA.
```

Director `IMAGE_PRODUCTION_WINDOW_STANDARD.md` states only:

```text
B00 Director review phải PASS trước khi mở production hàng loạt của Window.
```

Director review is explicitly not Independent QA. Therefore the current text can be read as authorizing B01+ production before B00 Independent QA approval.

### Required correction

Every Director document that controls production sequencing must state:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
BEFORE ANY B01+ MASS PRODUCTION MAY OPEN.
```

`QA_REJECTED` or `QA_BLOCKED` keeps all later production closed.

---

## HKA-ADR-W01-002 — P1 — NODE_CATALOG template is below canonical minimum node anatomy

Canonical HKA node anatomy requires, among other fields:

- originating phenomenon;
- representations;
- method of knowledge formation;
- evidence;
- error and limits;
- HKA Compass;
- evidence/demonstration of understanding;
- sources;
- version history;
- mapping to external curricula.

Current `NODE_CATALOG_TEMPLATE.md` has useful content but omits or collapses several of these fields.

### Required correction

Add explicit fields at minimum:

```text
ORIGINATING PHENOMENON / PROBLEM
CANONICAL DEFINITION
REPRESENTATIONS
METHOD OF KNOWLEDGE FORMATION
ERROR / BIAS / LIMITS
HKA COMPASS LINKS
EVIDENCE OF UNDERSTANDING / ASSESSMENT TASKS
VERSION HISTORY
EXTERNAL CURRICULUM MAPPINGS
```

Do not rely on `NODE VERSION` alone as version history.

Node-type taxonomy must also be extensible. The current list is too narrow for history, humanities, law, arts and institutional knowledge. Add canonical or extensible types such as:

```text
PHENOMENON
QUANTITY
LAW / PRINCIPLE
MODEL / THEORY
TOOL / PRACTICE
WORK
EVENT
PERSON
INSTITUTION
```

without removing current types.

---

## HKA-ADR-W01-003 — P1 — Epistemic status taxonomy must preserve canonical two-axis distinction

Current Academic Program Authoring Standard uses:

```text
SETTLED / HIGH CONSENSUS
CONTEXT-DEPENDENT
ACTIVE DEBATE
OPEN QUESTION
MODEL / APPROXIMATION
NORMATIVE / VALUE JUDGMENT
```

This mixes certainty, representational status and normative status into one list. HKA canonical architecture requires certainty and content classification to remain distinguishable.

### Required correction

Every material claim/node must support at least two independent axes:

```text
CERTAINTY:
ESTABLISHED / DEVELOPING / DEBATED / HYPOTHETICAL / UNKNOWN

CONTENT CLASS:
ESTABLISHED_KNOWLEDGE
DEVELOPING_RESEARCH
ACADEMIC_DEBATE
PHILOSOPHICAL_DEBATE
HUMANISTIC_METAPHOR
```

Add optional independent fields where relevant:

```text
CONTEXT_DEPENDENCE
NORMATIVE_STATUS
MODEL_STATUS / APPROXIMATION
```

A scientific model can be well established; therefore `MODEL / APPROXIMATION` must not be treated as a certainty level.

---

## HKA-ADR-W01-004 — P1 — Relation taxonomy is not a canonical superset

Current relation list includes useful types but omits several relation types required by the HKA architecture and changes naming/direction semantics.

### Required correction

The Relation Catalog must include the canonical core relation types as a mandatory superset:

```text
PREREQUISITE
PART_OF
CAUSES
AFFECTS
MEASURED_BY
STRUCTURAL_ANALOGY
USED_IN
EVIDENCE_FOR
EVIDENCE_AGAINST
HISTORICAL_DEVELOPMENT
DEBATES_WITH
ETHICAL_SOCIAL_CONSEQUENCE
```

Existing extensions may remain, for example:

```text
CONSTRAINS
MODELS
COMPARES_WITH
APPLIES_TO
HISTORICALLY_PRECEDES
CROSS_TREE_CONTEXT
CONTRASTS_WITH
```

but each extension must define:

- direction semantics;
- allowed source/target node types;
- inverse relation if applicable;
- evidence requirement;
- duplicate-equivalence rule.

Do not use a generic `TWO_WAY` flag for relations whose semantics are inherently directional such as `PREREQUISITE` and `CAUSES`.

---

## HKA-ADR-W01-005 — P1 — Source-quality protocol needs claim-type evidence rules, not a single linear hierarchy

Current Source Register starts with a numbered hierarchy that places primary research in level 1 and systematic reviews/consensus reports in level 2. This can mis-rank evidence depending on the claim.

Examples:

- state-of-evidence scientific or medical claim may require systematic review/meta-analysis/consensus above any single study;
- historical primary sources are primary evidence but not automatically the strongest interpretation;
- law requires current authoritative legal text for what the law is;
- statistics should prefer the responsible official dataset for the reported measure;
- philosophy/humanities often require primary text plus scholarly interpretation.

### Required correction

Replace the universal numbered hierarchy with a **source-fitness matrix by claim type**.

Add stable claim-to-source mapping fields:

```text
CLAIM ID
CLAIM TEXT / SCOPE
SOURCE ID
SOURCE LOCATION / SECTION / TABLE / DATASET VERSION
SUPPORT TYPE: SUPPORTS / QUALIFIES / CONTRADICTS / CONTEXT
EVIDENCE ROLE
SOURCE FITNESS FOR THIS CLAIM
CROSS-CHECK STATUS
RETRACTION / SUPERSESSION STATUS
```

High-risk claims must have explicit claim IDs and auditable source links; free-text `SUPPORTED CLAIMS` alone is insufficient at HKA scale.

---

## HKA-ADR-W01-006 — P1 — Academic QA artifacts and completeness checks are insufficiently explicit

`DIRECTOR_REVIEW_GATE.md` has a good checklist but Window Contract Addendum does not require durable academic QA artifacts beyond the core four files and self-audit.

### Required correction

Require, for each applicable content window:

```text
ACADEMIC_COVERAGE_AUDIT.md or ACADEMIC_COVERAGE_MATRIX.csv
ACADEMIC_QA_REPORT.md
```

Academic QA must explicitly check:

```text
100% mandatory branch coverage
external curriculum / classification mapping where applicable
semantic duplicate-node detection
orphan-node detection
prerequisite existence
prerequisite-cycle detection or documented co-requisite exception
entry-point reachability
claim-to-source coverage
high-risk claim cross-checks
D1-D4 substantive progression
misconception coverage
open/debated/settled separation
unresolved expert-review items
cross-window ownership conflict = 0 before lock
```

A Window may not use `COMPLETE` merely because every heading has text.

---

## HKA-ADR-W01-007 — P1 — Program-to-Visual bridge loses academic truth metadata

Current `PROGRAM_TO_VISUAL_DIRECTOR_BRIEF_TEMPLATE.md` maps VCU to Node IDs and learning objective, which is necessary but not sufficient. The production prompt can still lose the exact claims, source constraints and epistemic status that justified the image.

### Required correction

Extend the VCU/Asset handoff with:

```text
CLAIM IDS
SOURCE IDS
CERTAINTY / CONTENT CLASS
MISCONCEPTION TO PREVENT
WHAT MUST BE SEEN
WHAT MUST NOT BE IMPLIED
REPRESENTATION DISCLOSURE
ACADEMIC TRUTH LOCKS
REQUIRED EXPERT REVIEW, IF ANY
ACADEMIC CONTENT COMMIT SHA
```

The IMG Execution Pack should carry or reference this Academic Truth Pack so Independent Image QA can trace:

```text
IMAGE → ASSET ID → VCU → NODE → CLAIM → SOURCE
```

---

## HKA-ADR-W01-008 — P1 — Applicability range W02–W64 is structurally too broad

Director documents repeatedly apply one Content Window model to `W02–W64`.

Under the established HKA window architecture, later windows do not all perform the same function: W61–W64 are system-level validation/integration/release-candidate roles rather than ordinary curriculum-authoring windows. Early foundation windows and cross-domain hub windows also have different authoring profiles.

### Required correction

Define `WINDOW TYPE` and applicability profiles, at minimum:

```text
FOUNDATION / ROOT / METHOD WINDOW
DOMAIN / DISCIPLINE CONTENT WINDOW
CROSS-DOMAIN HUB WINDOW
SYSTEM QA / INTEGRATION WINDOW
```

The full Academic Authoring workflow should apply to the appropriate content windows, expected initially W02–W60 unless a later contract explicitly changes ownership.

W61–W64 require their own audit/integration contract rather than being forced into `TREE.md + prompt authoring` semantics.

---

## HKA-ADR-W01-009 — P1 — IMG Unit architecture changes canonical Production Window semantics and needs an explicit amendment

Canonical pipeline currently says one Image Production Window owns one batch. Director Layer introduces multiple IMG Units within one batch, each with at most two assets. The concept is accepted as useful, but it is a real execution-model change, not merely a stricter wording.

### Required correction

Do not activate IMG Units solely through a supplemental Director standard.

Create a canonical change request/amendment proposal that defines:

```text
BATCH = manifest / complete-snapshot / independent-QA / release unit
IMG UNIT = generation sub-unit, max 2 assets
BATCH PRODUCTION ORCHESTRATOR / DIRECTOR = assembles IMG Unit outputs into one complete batch snapshot
```

Specify:

- Unit ID grammar;
- how unit outputs are assembled;
- batch self-QA responsibility;
- when a Batch Run ID changes;
- how multiple unit outputs share one Batch Run;
- no partial batch is submitted to Independent QA;
- B00 remains one IMG Unit of exactly two assets by default.

Until that amendment is accepted, IMG Unit design remains `PROPOSED`, not active canonical production behavior.

---

# 4. NONBLOCKING BUT REQUIRED BEFORE FIRST REAL PRODUCTION

## HKA-ADR-W01-010 — P2 — Director direct-fix provenance

When Director directly fixes a small Window-generated file after an academic content lock, the system must not keep using the previous content SHA as if nothing changed.

Define:

```text
DIRECTOR FIX COMMIT SHA
SUPERSEDES ACADEMIC CONTENT COMMIT SHA
AFFECTED NODE/CLAIM IDS
SOURCE IMPACT: NONE / RECHECK REQUIRED
DOWNSTREAM PROMPT INVALIDATION: YES/NO
```

If the fix changes a material claim, prerequisite, source or learning objective, it must return to the owner Window and invalidate downstream visual locks.

---

## HKA-ADR-W01-011 — P2 — Partial rework carry-forward provenance

Director allows accepted bytes from an earlier run to be carried into a new complete batch snapshot. This is sound only if each final asset records provenance.

Add per-asset fields such as:

```text
ORIGIN_RUN_ID
ORIGIN_IMG_UNIT_ID
ORIGIN_CLEAN_SHA256
ORIGIN_BRANDED_SHA256
CARRIED_FORWARD: YES/NO
REVALIDATED_IN_FINAL_BATCH: YES/NO
```

Independent QA still reviews the complete final batch snapshot.

---

# 5. R2 STAGING DECISION

`HKA-CR-W01-DIR-001` is handled correctly: staging was not silently added to canonical infrastructure.

Architect direction:

```text
STAGING CONCEPT: APPROVED IN PRINCIPLE
CANONICAL STATUS: NOT YET ACTIVE
ACTION: separate Cloudflare/R2 amendment after account infrastructure is available
BLOCKS W02 ACADEMIC AUTHORING: NO
BLOCKS AUTOMATED IMAGE PRODUCTION PIPELINE: YES, until a concrete approved full-resolution handoff path exists
```

---

# 6. REQUIRED W01 CORRECTION PASS

W01 Director should perform one targeted correction pass only. Do not rewrite accepted parts.

Required result:

```text
NEW DIRECTOR COMMIT SHA
FILES CHANGED
FINDING IDs ADDRESSED
SELF-AUDIT RESULT
OPEN ITEMS
```

All P0/P1 findings above must be closed before Architect PASS.

After W01 submits the corrected commit, Architect will review only:

1. the correction diff from `7f127678...`;
2. all affected integrated documents;
3. cross-document consistency;
4. final applicability to W02.

---

# 7. CURRENT STATE

```text
W01 DIRECTOR LAYER:
STRONG / PRESERVED / RETURNED FOR TARGETED CORRECTIONS

ARCHITECT PASS:
NO

W02:
NOT OPEN

IMAGE PRODUCTION:
NOT OPEN

R2:
NOT OPEN

MERGE:
NOT AUTHORIZED

SIGMASTUDY.NET:
HOLD
```
