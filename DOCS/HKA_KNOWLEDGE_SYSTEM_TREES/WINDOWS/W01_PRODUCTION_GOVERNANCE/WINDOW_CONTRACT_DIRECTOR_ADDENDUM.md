---
title: "HKA Window Contract — Director Addendum"
version: "1.1"
status: "PROPOSED REFERENCE ADDENDUM — ARCHITECT REVIEW REQUIRED"
---

# HKA WINDOW CONTRACT — DIRECTOR ADDENDUM

Use with the accepted `WINDOW_CONTRACT_TEMPLATE.md` only after Architect accepts this Director Layer.

## A. Window Type — mandatory

Every future contract must state:

```text
WINDOW TYPE:
FOUNDATION / ROOT / METHOD WINDOW
DOMAIN / DISCIPLINE CONTENT WINDOW
CROSS-DOMAIN HUB WINDOW
SYSTEM QA / INTEGRATION WINDOW

PRIMARY FUNCTION:
ACADEMIC AUTHORING PROFILE:
VISUAL AUTHORING IN SCOPE: YES/NO
SYSTEM QA / INTEGRATION DUTIES:
REQUIRED OUTPUT PROFILE:
```

Use `WINDOW_TYPE_APPLICABILITY_STANDARD.md`. Do not force W61–W64 into ordinary curriculum/prompt semantics unless their exact contracts explicitly do so.

## B. Required academic outputs by applicable content profile

For content-authoring windows, contract must require as applicable:

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
ACADEMIC_COVERAGE_AUDIT.md or ACADEMIC_COVERAGE_MATRIX.csv
ACADEMIC_QA_REPORT.md
SELF_AUDIT.md
```

Window does not stop at outline. Mandatory scope becomes a complete, auditable program.

## C. Director Academic Gate

Contract must lock:

```text
MANDATORY BRANCH COVERAGE = 100%
SEMANTIC DUPLICATE NODES UNRESOLVED = 0
ORPHAN / UNREACHABLE REQUIRED NODES = 0 OR JUSTIFIED
MISSING PREREQUISITE TARGETS = 0
PREREQUISITE CYCLE CHECK = PASS / EXEMPT_WITH_REASON
CLAIM-TO-SOURCE COVERAGE = PASS
UNSUPPORTED HIGH-RISK CLAIMS = 0
HIGH-RISK CROSS-CHECKS = COMPLETE
CERTAINTY / CONTENT CLASS = SEPARATE
D1-D4 = SUBSTANTIVE
UNRESOLVED MATERIAL EXPERT-REVIEW ITEMS = 0 OR CONTRACTED DEFERMENT
UNRESOLVED OWNERSHIP CONFLICTS = 0
ACADEMIC COVERAGE AUDIT = PASS
ACADEMIC QA REPORT = PASS
DIRECTOR ACADEMIC GATE = PASS BEFORE PROGRAM-TO-VISUAL
```

## D. Program-to-Visual bridge

When visual authoring is in scope, require:

```text
PROGRAM_TO_VISUAL_DIRECTOR_BRIEF.md
ACADEMIC_TRUTH_PACK per VCU/Asset or equivalent embedded records
```

The handoff must preserve:

```text
ACADEMIC CONTENT COMMIT SHA
NODE IDS
CLAIM IDS
SOURCE IDS + exact locations/versions
CERTAINTY
CONTENT CLASS
MISCONCEPTION TO PREVENT
WHAT MUST BE SEEN
WHAT MUST NOT BE IMPLIED
REPRESENTATION DISCLOSURE
ACADEMIC TRUTH LOCKS
REQUIRED EXPERT REVIEW STATUS
```

## E. Director Visual Gate

```text
ALL VCUS TRACE NODE→CLAIM→SOURCE
ACADEMIC TRUTH PACKS COMPLETE
DECORATIVE-ONLY ASSETS = 0
FINAL DUPLICATE VISUAL JOB COUNT = 0
PROMPT RECORDS COMPLETE
PROMPT HASHES REPRODUCIBLE
BATCH MAP VALID
PACKAGE = SMALLEST SUFFICIENT CANONICAL PACKAGE
DIRECTOR VISUAL GATE = PASS
```

## F. Production model boundary

Current active canonical production semantics remain the accepted canonical pipeline.

The anti-drift model:

```text
IMG UNIT ID = IMG-WXX-BYY-UZZ-RNN
PROPOSED MAX ASSETS PER IMG UNIT = 2
```

is **not active** until a canonical amendment is approved. See `IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md`.

A Window Contract must not activate multiple IMG Units merely by referencing Director Layer.

## G. B00 production gate

Before any B01+ mass production may open:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps later production closed.

## H. Director correction authority and provenance

Director direct-fix is allowed only for bounded nonmaterial defects and must use `DIRECTOR_FIX_PROVENANCE_TEMPLATE.md`.

Required fields include:

```text
DIRECTOR FIX COMMIT SHA
SUPERSEDES ACADEMIC CONTENT COMMIT SHA
AFFECTED NODE/CLAIM/RELATION IDS
SOURCE IMPACT
DOWNSTREAM PROMPT INVALIDATION
```

Material claim/prerequisite/source/learning-objective/scope change returns to owner Window and invalidates downstream locks as appropriate.

## I. Partial rework provenance

If bytes from an older run carry into a later complete batch snapshot, require per-asset `BATCH_ASSET_PROVENANCE` with:

```text
ORIGIN_RUN_ID
ORIGIN_IMG_UNIT_ID
ORIGIN_CLEAN_SHA256
ORIGIN_BRANDED_SHA256
CARRIED_FORWARD
REVALIDATED_IN_FINAL_BATCH
```

Independent QA reviews the complete final snapshot.

## J. Required completion receipt additions

For applicable content windows:

```text
WINDOW TYPE
ACADEMIC CONTENT COMMIT SHA
ACADEMIC COVERAGE AUDIT PATH / RESULT
ACADEMIC QA REPORT PATH / RESULT
DIRECTOR ACADEMIC GATE
PROGRAM-TO-VISUAL BRIEF PATH, IF APPLICABLE
ACADEMIC TRUTH PACK STATUS, IF APPLICABLE
DIRECTOR VISUAL GATE, IF APPLICABLE
DIRECTOR FIX RECORDS
OPEN EXPERT-REVIEW ITEMS
OPEN CANONICAL CHANGE REQUESTS
```

## K. Release boundary

Director Layer does not replace Independent Image QA, canonical R2 buckets or Amendment 1.1 release order. `hka-c4k-staging` remains non-active pending separate amendment.