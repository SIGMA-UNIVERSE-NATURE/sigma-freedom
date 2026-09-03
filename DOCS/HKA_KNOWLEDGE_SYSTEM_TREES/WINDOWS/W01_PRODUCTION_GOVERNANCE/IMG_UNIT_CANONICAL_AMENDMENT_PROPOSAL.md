---
title: "HKA IMG Unit Canonical Amendment Proposal"
version: "0.1"
status: "PROPOSED — NOT ACTIVE CANONICAL"
architect_review_required: true
---

# HKA IMG UNIT CANONICAL AMENDMENT PROPOSAL

This proposal addresses Architect finding `HKA-ADR-W01-009`. It does **not** activate IMG Units. Until a canonical amendment is accepted, the existing canonical rule remains: one Image Production Window owns one batch.

## 1. Proposed semantics

```text
BATCH
= manifest + complete production snapshot + batch self-QA + Independent QA + release unit

IMG UNIT
= generation sub-unit inside one Batch Run; maximum 2 authorized Asset IDs

BATCH PRODUCTION ORCHESTRATOR
= Director or designated production orchestrator that assembles IMG Unit returns into one complete Batch Run snapshot
```

## 2. Proposed Unit ID grammar

```text
IMG-WXX-BYY-UZZ-RNN
```

Where:

```text
WXX = Window ID
BYY = Batch number matching Batch ID HKA-WXX-BYY
UZZ = unit sequence inside the target Batch Run
RNN = target complete Batch Run number, matching HKA-WXX-BYY-RNN
```

Example:

```text
Batch Run: HKA-W02-B01-R01
IMG-W02-B01-U01-R01 → assets 0003,0004
IMG-W02-B01-U02-R01 → assets 0005,0006
IMG-W02-B01-U03-R01 → assets 0007,0008
```

## 3. Initial production

All IMG Units contributing to one initial complete snapshot share the same Batch Run ID.

Each IMG Unit returns:

```text
IMG UNIT ID
TARGET BATCH RUN ID
AUTHORIZED ASSET IDS
OUTPUT FILE REFERENCES
PER-FILE SHA-256
UNIT SELF-QA RESULT
ACADEMIC TRUTH PACK REFERENCES
OFFICIAL REFERENCE METHOD
```

No Unit may add an undeclared Asset ID.

## 4. Batch assembly

Batch Production Orchestrator must assemble all required Asset IDs into exactly one complete snapshot and verify:

```text
ASSET COUNT = MANIFEST COUNT
CLEAN MASTER COUNT = MANIFEST COUNT
BRANDED FINAL COUNT = MANIFEST COUNT
UNDECLARED FILE COUNT = 0
PER-FILE SHA-256 COMPLETE
UNIT PROVENANCE COMPLETE
ACADEMIC/PROMPT/MANIFEST SHAS MATCH
```

The orchestrator then produces batch-level:

```text
PRODUCTION_REPORT.md
SELF_QA_REPORT.json
SHA256SUMS.txt
BATCH_ASSET_PROVENANCE record
BATCH_PACKAGE_SHA-256
```

## 5. Batch self-QA responsibility

IMG Unit self-QA is local only. The Batch Production Orchestrator owns complete batch self-QA before Independent QA.

A partial set of Unit outputs must never be labeled `SELF_QA_COMPLETE` for the batch.

## 6. Independent QA boundary

```text
NO PARTIAL BATCH MAY ENTER INDEPENDENT QA.
```

Independent QA reviews one complete final Batch Run snapshot containing every manifest Asset ID, regardless of how many IMG Units produced its bytes.

## 7. B00 rule

Default:

```text
B00 = 2 assets = exactly 1 IMG Unit
```

No B01+ mass production may open until both:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

`QA_REJECTED` or `QA_BLOCKED` keeps all B01+ production closed.

## 8. Rework and Batch Run ID

When a complete Batch Run has been reviewed and one or more outputs require regeneration:

```text
NEXT COMPLETE SNAPSHOT = NEW BATCH RUN ID
```

Example:

```text
R01 reviewed; asset 0004 fails output QA
→ target next complete snapshot HKA-W02-B01-R02
→ a new R02 IMG Unit regenerates 0004
→ accepted R01 bytes may be carried forward for other Asset IDs only with per-asset provenance
→ R02 complete snapshot contains every manifest Asset ID
→ Independent QA reviews the complete R02 snapshot
```

Accepted bytes are never overwritten and do not become new bytes merely because they are included in R02.

## 9. Carry-forward provenance

Every final asset in the target snapshot must record:

```text
ORIGIN_RUN_ID
ORIGIN_IMG_UNIT_ID
ORIGIN_CLEAN_SHA256
ORIGIN_BRANDED_SHA256
CARRIED_FORWARD: YES/NO
REVALIDATED_IN_FINAL_BATCH: YES/NO
```

Use `BATCH_ASSET_PROVENANCE_TEMPLATE.md`.

## 10. Activation requirements

IMG Unit semantics become active only after:

1. canonical Architect approves amendment;
2. canonical pipeline language is amended;
3. production-status / handoff schemas are confirmed compatible or versioned;
4. Window Contracts explicitly opt into the approved model;
5. any staging/full-resolution handoff path required for automation is separately approved.

Until then:

```text
IMG UNIT DESIGN = PROPOSED
ACTIVE CANONICAL PRODUCTION MODEL = EXISTING ONE-PRODUCTION-WINDOW-PER-BATCH RULE
```