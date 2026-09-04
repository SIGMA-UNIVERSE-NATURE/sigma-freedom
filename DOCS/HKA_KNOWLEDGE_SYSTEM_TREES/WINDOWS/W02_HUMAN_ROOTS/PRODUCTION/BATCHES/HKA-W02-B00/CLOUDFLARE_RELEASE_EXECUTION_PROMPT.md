---
title: "HKA W02 B00 — Cloudflare R2 Release Execution Prompt"
version: "1.0"
status: "WAITING_FOR_QA_APPROVED"
window_id: "W02"
batch_id: "HKA-W02-B00"
run_id: "HKA-W02-B00-R01"
release_id: "HKA-W02-REL-0001"
date: "2026-09-04"
---

# HKA W02 B00 — CLOUDFLARE R2 RELEASE UPLOADER

```text
BẠN LÀ RELEASE UPLOADER CHO HKA W02 — B00.

KHÔNG ĐƯỢC CHẠY nếu chưa có Independent QA status = QA_APPROVED.

BATCH / RUN / RELEASE:
HKA-W02-B00
HKA-W02-B00-R01
HKA-W02-REL-0001

IMMUTABLE LOCKS:
PROMPT CONTENT COMMIT: 295f73a8e833b5a0ffb9642078514e7e3924700a
EFFECTIVE MANIFEST / INTEGRITY COMMIT: 7028f0c008bca4e8dcaea2bd878ef9210113e223
B00 MANIFEST SHA-256: b30f15d36d97f1b04b1dacb00072d4da2be2a59d0a9407472f1d00dc2635d60b

CANONICAL AUTHORITY:
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_BATCH_PIPELINE.md
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_1.md

MANDATORY SCHEMAS:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-upload-receipt.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-release-record.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-release-index.schema.json

CANONICAL BUCKETS:
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery

DO NOT USE:
hka-c4k-staging

VAULT PREFIX:
v1/windows/W02-human-roots/prompt-commit/295f73a8e833b5a0ffb9642078514e7e3924700a/batches/HKA-W02-B00/runs/HKA-W02-B00-R01/

PRECONDITIONS — ALL REQUIRED:
1. Independent QA report exists and is schema-valid.
2. QA status = QA_APPROVED.
3. QA_REPORT_SHA256 is verified.
4. Production package SHA-256 is verified.
5. CLEAN MASTER / BRANDED FINAL checksums match SHA256SUMS.txt.
6. BATCH_MANIFEST SHA-256 matches locked value.
7. Target vault prefix does not contain a prior locked release.
8. Release ID HKA-W02-REL-0001 is unused.

IF ANY PRECONDITION FAILS:
STATUS: R2_RELEASE_BLOCKED
STOP.

MANDATORY RELEASE ORDER — DO NOT REORDER:
1. Upload CLEAN MASTER objects.
2. Upload BRANDED FINAL objects.
3. Upload asset metadata sidecars.
4. Upload prompts and manifests.
5. Upload production and independent QA reports.
6. Upload SHA256SUMS.txt.
7. Upload batch package ZIP.
8. Verify object count, metadata and SHA-256.
9. Generate and upload schema-valid R2_UPLOAD_RECEIPT.json.
10. Verify R2_UPLOAD_RECEIPT.json; status must be R2_OBJECTS_VERIFIED.
11. Generate and upload RELEASED.json as the FINAL object in the vault release prefix.
12. Verify RELEASED.json and its SHA-256.
13. Apply lock to the complete vault release prefix.
14. Write schema-valid R2_RELEASE_AUDIT_RECORD.json to hka-c4k-audit; status must be R2_VERIFIED.
15. Update GitHub RELEASE_INDEX.json with audit record object key + SHA-256 and status R2_VERIFIED.

R2 object layout must follow canonical pipeline, including:
assets/<ASSET_ID>/clean/<CLEAN_SHA256>/<ASSET_ID>_CLEAN_MASTER.png
assets/<ASSET_ID>/branded/<BRANDED_SHA256>/<ASSET_ID>_BRANDED_FINAL.png
assets/<ASSET_ID>/metadata/<ASSET_ID>_ASSET.json
manifests/
prompts/
reports/
checksums/
packages/
receipts/
RELEASED.json

IMPORTANT:
- RELEASED.json must be the final object written inside the vault release prefix.
- After prefix lock, write no more objects into that vault prefix.
- Audit confirmation goes to hka-c4k-audit, not the locked vault prefix.
- Do not use ETag as a substitute for SHA-256.
- Do not deploy website.
- Do not move CLEAN MASTER into hka-c4k-delivery.
- hka-c4k-delivery remains a later WEB_APPROVED step.

FINAL RETURN:
STATUS:
RELEASE ID:
BATCH ID:
RUN ID:
QA STATUS VERIFIED:
QA_REPORT_SHA256:
BATCH PACKAGE SHA-256:
VAULT BUCKET:
VAULT PREFIX:
OBJECT COUNT EXPECTED/VERIFIED:
R2_UPLOAD_RECEIPT KEY:
R2_UPLOAD_RECEIPT SHA-256:
RELEASED.json KEY:
RELEASED.json SHA-256:
RELEASE MARKER VERIFIED:
PREFIX LOCK APPLIED:
R2_RELEASE_AUDIT_RECORD KEY:
R2_RELEASE_AUDIT_RECORD SHA-256:
GITHUB RELEASE_INDEX STATUS:
R2 VERIFIED: YES/NO
KNOWN LIMITATIONS:

Then STOP. Website publication requires separate WEB_APPROVED instruction.
```
