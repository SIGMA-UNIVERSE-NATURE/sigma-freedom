---
title: "HKA Batch Asset Provenance Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# HKA BATCH ASSET PROVENANCE

Required when a complete Batch Run snapshot contains bytes produced in different origin runs/IMG Units, including carry-forward after partial rework.

## 1. Batch identity

```text
WINDOW ID:
BATCH ID:
FINAL SNAPSHOT RUN ID:
PROMPT CONTENT COMMIT SHA:
FINAL MANIFEST COMMIT SHA:
MANIFEST SHA-256:
```

## 2. Per-asset provenance record

For every Asset ID in the final complete batch snapshot:

```text
ASSET ID:
ORIGIN RUN ID:
ORIGIN IMG UNIT ID:
ORIGIN CLEAN SHA256:
ORIGIN BRANDED SHA256:
CARRIED FORWARD: YES/NO
CARRY-FORWARD SOURCE SNAPSHOT RUN ID:
REVALIDATED IN FINAL BATCH: YES/NO
FINAL SNAPSHOT CLEAN SHA256:
FINAL SNAPSHOT BRANDED SHA256:
ACADEMIC TRUTH PACK REF:
PROMPT SHA-256:
```

If `CARRIED FORWARD = YES`, final snapshot hashes must equal the recorded origin hashes byte-for-byte.

## 3. Carry-forward eligibility

Carry-forward is allowed only when:

- original bytes were accepted at the relevant production/Director stage and are not the subject of the rework;
- prompt/truth locks for that Asset ID have not changed;
- brand source requirements have not changed;
- the bytes remain checksum-identical;
- the final Batch Run explicitly records their origin;
- they are revalidated as part of the complete final batch snapshot.

If prompt, academic truth lock or brand requirement changes for an Asset ID, prior bytes cannot be carried forward without a new compatibility decision and normally require regeneration.

## 4. Complete-snapshot rule

```text
ASSET PROVENANCE RECORD COUNT = MANIFEST ASSET COUNT
MISSING PROVENANCE RECORDS = 0
```

No partial set enters Independent QA.

## 5. Independent QA rule

Independent QA reviews the complete final snapshot, including carried-forward bytes. A prior PASS does not exempt an asset from presence/integrity/consistency checks in the final Batch Run.

## 6. Summary

```text
TOTAL ASSETS:
NEWLY GENERATED IN FINAL RUN:
CARRIED FORWARD:
PROVENANCE RECORDS COMPLETE: YES/NO
CARRY-FORWARD HASH MATCH: PASS/FAIL
FINAL COMPLETE SNAPSHOT READY FOR INDEPENDENT QA: YES/NO
```