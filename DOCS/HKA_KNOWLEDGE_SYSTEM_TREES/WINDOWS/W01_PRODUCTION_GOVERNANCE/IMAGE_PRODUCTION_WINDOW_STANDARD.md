---
title: "HKA Image Production Window Standard"
version: "1.1"
status: "PROPOSED DESIGN — NOT ACTIVE CANONICAL; ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA IMAGE PRODUCTION WINDOW STANDARD

## 1. Activation boundary

The anti-drift IMG Unit design is accepted in principle but changes canonical Production Window semantics. Therefore:

```text
IMG UNIT DESIGN: PROPOSED
MAX 2 ASSETS PER IMG UNIT: PROPOSED
ACTIVE CANONICAL RULE UNTIL AMENDMENT APPROVAL:
ONE IMAGE PRODUCTION WINDOW OWNS ONE BATCH
```

Activation requires acceptance of `IMG_UNIT_CANONICAL_AMENDMENT_PROPOSAL.md` or a superseding canonical amendment.

The following anti-drift requirements may be adopted by a canonical batch Production Window immediately when compatible: exact immutable sources, official reference reload, no generated-image reference chaining, per-asset fresh-source cycle, no prompt editing, repeated-failure root-cause stop.

## 2. Proposed core rule

```text
CONTENT WINDOW DOES NOT GENERATE IMAGES.
IMG UNIT DOES NOT WRITE CURRICULUM.
IMG UNIT DOES NOT EDIT PROMPTS.
PROPOSED MAXIMUM AUTHORIZED ASSETS PER IMG UNIT: 2.
```

Batch remains the manifest/complete-snapshot/self-QA/Independent-QA/release unit. IMG Unit is only a proposed generation sub-unit.

## 3. Proposed naming

Canonical IDs remain:

```text
BATCH ID: HKA-W02-B01
RUN ID: HKA-W02-B01-R01
ASSET ID: HKA-VIS-W02-0003
```

Proposed execution-unit ID:

```text
IMG-W02-B01-U01-R01
IMG-W02-B01-U02-R01
IMG-W02-B01-U03-R01
```

Example only after amendment activation:

```text
U01 → 0003, 0004
U02 → 0005, 0006
U03 → 0007, 0008
```

Unit number never replaces Batch ID or Run ID.

## 4. Mandatory execution pack

The production executor receives exact values; it does not discover/select them.

```text
WINDOW ID
TREE ID
BATCH ID
RUN ID
IMG UNIT ID, IF AMENDMENT ACTIVE
AUTHORIZED ASSET IDS
ACADEMIC CONTENT COMMIT SHA
ACADEMIC TRUTH PACK REFERENCES
REPOSITORY
PROMPT CONTENT COMMIT SHA
FINAL MANIFEST COMMIT SHA
BATCH MANIFEST PATH
BATCH MANIFEST SHA-256
BATCH PROMPTS PATH
PROMPT HASH PAYLOAD PATHS
PROMPT SHA-256 PER ASSET
BRAND REPOSITORY
BRAND COMMIT SHA
EXACT CHARACTER MASTER PATHS
LOGO MASTER PATH
EXACT MOTTO
OUTPUT FILENAMES
OUTPUT SIZE
PASS / FAIL CRITERIA
DIRECTOR GLOBAL CORRECTION LOCKS
```

## 5. Reference gate

Every relevant asset must load exact official PNG bytes from:

```text
linkcomltd-byte/sigma-universe-web
2d3aa9d8418acccd39a3d263e917d4157e029e17
```

Generated output must never become the character reference for another asset.

If official visual reference cannot be loaded:

```text
STATUS: ASSET_REFERENCE_BLOCKED
```

## 6. Per-asset fresh-source cycle

Before every Asset ID:

1. reread exact prompt;
2. verify prompt SHA;
3. resolve Academic Truth Pack / claim-source locks;
4. reread mandatory/forbidden objects;
5. reread representation type and forbidden implications;
6. reload required official references;
7. reread PASS/FAIL;
8. generate CLEAN MASTER;
9. self-check;
10. only after pass, create BRANDED FINAL by controlled post-production;
11. hash files;
12. close asset and reset to immutable source.

Do not use “same as previous image” as specification.

## 7. Hard pre-next-asset check

All must be YES:

```text
ASSET ID CORRECT
ACADEMIC TRUTH PACK RESOLVED
PROMPT SHA VERIFIED
OFFICIAL REFERENCES USED
MANDATORY OBJECTS COMPLETE
FORBIDDEN OBJECTS ABSENT
WHAT MUST NOT BE IMPLIED ABSENT
ACADEMIC RELATION CORRECT
SCALE / PROCESS CORRECT
REPRESENTATION TYPE CLEAR
CHARACTER IDENTITY CORRECT
CHARACTER ROLE CORRECT
NO RANDOM TEXT
CLEAN MASTER PASS
BRANDED FINAL PASS
FILENAMES CORRECT
```

A `NO` blocks moving to the next asset.

## 8. Proposed IMG Unit close

If the canonical IMG Unit amendment is active, after 1–2 assets:

```text
STATUS: PRODUCTION_UNIT_COMPLETE
```

No further assets may be added to that Unit.

## 9. Batch Production Orchestrator — proposed amendment semantics

Multiple IMG Units may contribute only if the amendment is active. A designated Batch Production Orchestrator/Director must assemble one complete Batch Run snapshot and own complete batch self-QA.

```text
NO PARTIAL IMG UNIT PACKAGE MAY ENTER INDEPENDENT QA.
```

Required complete-snapshot checks:

```text
ALL MANIFEST ASSET IDS PRESENT
N CLEAN + N BRANDED
NO UNDECLARED FILES
ALL FILE SHA-256 VALUES PRESENT
BATCH_ASSET_PROVENANCE COMPLETE
PRODUCTION REPORT COMPLETE
BATCH SELF-QA COMPLETE
PACKAGE SHA-256 COMPLETE
```

## 10. Rework and Run ID

When a complete Batch Run needs output rework:

- never overwrite the old run;
- next complete snapshot uses a new Batch Run ID;
- regenerate only affected assets when academically/prompt-compatible;
- accepted prior bytes may be carried forward only under `BATCH_ASSET_PROVENANCE_TEMPLATE.md`;
- every final asset records `ORIGIN_RUN_ID`, `ORIGIN_IMG_UNIT_ID`, origin SHA values, `CARRIED_FORWARD`, and `REVALIDATED_IN_FINAL_BATCH`;
- Independent QA reviews the entire new complete batch snapshot.

Repeated identical failure twice triggers root-cause review before another generation attempt.

## 11. Error classes

```text
OUTPUT_ERROR
PROMPT_ERROR
REFERENCE_ERROR
MODEL_CAPABILITY_ERROR
SYSTEMIC_ERROR
```

Production reports evidence; Director determines nontrivial correction path.

## 12. B00 — canonical mass-production gate

B00 remains calibration batch of exactly two assets.

Before any B01+ mass production may open, both conditions are mandatory:

```text
B00 DIRECTOR CONSISTENCY REVIEW = PASS
AND
B00 INDEPENDENT IMAGE QA = QA_APPROVED
```

If B00 is `QA_REJECTED` or `QA_BLOCKED`, all B01+ production remains closed.

Director review alone never opens bulk production.

If IMG Unit amendment becomes active, B00 is one IMG Unit of exactly two assets by default.

## 13. Parallel production

Parallel B01+ production is allowed only after the B00 gate above and must still obey canonical parallelism limits.

Parallel IMG Units inside a batch are **not active** unless the IMG Unit canonical amendment is accepted.

## 14. Production handback

Canonical batch Production Window returns the existing batch package required by canonical pipeline. If IMG Unit amendment is active, each Unit additionally returns:

```text
IMG UNIT ID
BATCH ID
TARGET RUN ID
AUTHORIZED / PRODUCED ASSET IDS
ACADEMIC TRUTH PACK REFERENCES
OFFICIAL REFERENCES VERIFIED
UNIT SELF-QA
OUTPUT FILE REFERENCES
SHA-256 PER FILE
KNOWN LIMITATIONS
STATUS
```

Neither IMG Unit nor Director may claim `QA_APPROVED`.