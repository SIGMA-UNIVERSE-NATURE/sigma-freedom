---
title: "HKA Window Contract — Director Addendum"
version: "1.3"
status: "ARCHITECT FINALIZED REFERENCE"
---

# HKA WINDOW CONTRACT — DIRECTOR ADDENDUM

Use with the accepted `WINDOW_CONTRACT_TEMPLATE.md` after Architect acceptance of Director Layer.

## A. Window Type — mandatory

Every future contract states:

```text
WINDOW TYPE:
FOUNDATION / ROOT / METHOD WINDOW
DOMAIN / DISCIPLINE CONTENT WINDOW
CROSS-DOMAIN HUB WINDOW
SYSTEM QA / INTEGRATION WINDOW

PRIMARY FUNCTION:
ACADEMIC AUTHORING PROFILE:
VISUAL AUTHORING IN SCOPE: YES/NO
REQUIRED OUTPUT PROFILE:
```

Use `WINDOW_TYPE_APPLICABILITY_STANDARD.md`. Do not force W61–W64 into ordinary curriculum/prompt semantics unless their exact contracts explicitly do so.

## B. Minimum academic outputs for applicable content windows

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
ACADEMIC_QA_REPORT.md
SELF_AUDIT.md
```

Coverage audit/matrix may be embedded in `ACADEMIC_QA_REPORT.md`. Create a separate `ACADEMIC_COVERAGE_AUDIT.md` or `.csv` only when program size or contract makes a separate artifact useful.

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
ACADEMIC QA REPORT = PASS
DIRECTOR ACADEMIC GATE = PASS BEFORE PROGRAM-TO-VISUAL
```

## D. Program-to-Visual bridge

When visual authoring is in scope, require:

```text
PROGRAM_TO_VISUAL_DIRECTOR_BRIEF.md
```

Academic Truth metadata and visual deduplication are embedded in this brief by default. Separate Truth Pack, dedup registry or global ledger records are created only when complexity/cross-window reuse requires them.

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
TRUTH METADATA COMPLETE
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

is not active until a canonical amendment is approved. W02 authoring does not wait for that amendment; only image-production activation does.

## G. B00 production gate

Before any B01+ mass production may open:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps later production closed.

## H. Director correction authority and provenance

Director direct-fix is allowed only for bounded nonmaterial defects and must create traceable provenance. Material claim/prerequisite/source/learning-objective/scope change returns to owner Window and invalidates downstream locks as appropriate.

## I. Partial rework provenance

If bytes from an older run carry into a later complete batch snapshot, record per-asset origin run/hash and `REVALIDATED_IN_FINAL_BATCH`. Independent QA reviews the complete final snapshot.

## J. Required completion receipt additions

For applicable content windows:

```text
WINDOW TYPE
ACADEMIC CONTENT COMMIT SHA
ACADEMIC QA REPORT PATH / RESULT
DIRECTOR ACADEMIC GATE
PROGRAM-TO-VISUAL BRIEF PATH, IF APPLICABLE
DIRECTOR VISUAL GATE, IF APPLICABLE
OPEN EXPERT-REVIEW ITEMS
OPEN CANONICAL CHANGE REQUESTS
```

Do not add receipt fields that duplicate information already present in an immutable artifact unless needed for handoff.

## K. Release boundary

Director Layer does not replace Independent Image QA, canonical R2 buckets or Amendment 1.1 release order. `hka-c4k-staging` remains non-active pending separate amendment.

## L. Default GitHub write authority — automatic for every Window

Every Window opened by Architect receives GitHub write authority by default for its own assigned execution branch and allowed write prefix. No separate user approval is required for routine Window-owned GitHub writes.

The Window may, without asking the user for each action:

```text
CREATE FILES
UPDATE FILES
DELETE ITS OWN DRAFT FILES
CREATE DIRECTORIES
COMMIT
VERSION
CREATE MANIFESTS / CHECKSUMS / QA REPORTS / SELF-AUDITS / CHANGE REQUESTS
UPDATE ITS OWN ISSUE / DRAFT PR REVIEW SURFACES WHEN CONTRACTED
```

At completion, the Window must commit all required durable outputs to GitHub before returning its Completion Receipt. Local-only completion is not accepted when GitHub write capability is available.

This automatic authority is bounded by the exact Window Contract:

```text
WRITE ONLY TO ASSIGNED BRANCH / PREFIX
DO NOT EDIT CANONICAL FILES OUTSIDE AUTHORIZED SCOPE
DO NOT WRITE INTO ANOTHER WINDOW'S PREFIX OR BRANCH
DO NOT MERGE UNLESS SEPARATELY AUTHORIZED
DO NOT TREAT GITHUB WRITE AUTHORITY AS R2 / WEBSITE / PRODUCTION AUTHORITY
```

Architect issues these write boundaries when opening the Window and does not ask the user again for per-file or per-commit permission inside the assigned scope.