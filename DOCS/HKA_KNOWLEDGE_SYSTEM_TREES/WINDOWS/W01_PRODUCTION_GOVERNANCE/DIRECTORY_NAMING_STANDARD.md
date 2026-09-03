---
title: "HKA — Directory, Identifier & Naming Standard"
version: "2.0"
status: "DIRECTOR-INTEGRATED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA DIRECTORY, IDENTIFIER & NAMING STANDARD

## 1. Repositories

```text
KNOWLEDGE / PROMPT CONTROL PLANE:
SIGMA-UNIVERSE-NATURE/sigma-freedom

OFFICIAL BRAND SOURCE:
linkcomltd-byte/sigma-universe-web
```

## 2. Git branches

```text
CANONICAL: hka-knowledge-system-trees
WINDOW: hka-tree/wXX-<tree-slug>
```

Window branch regex:

```regex
^hka-tree/w[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*$
```

## 3. Window directory

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/WXX_<UPPER_SNAKE_SLUG>/
```

Required academic/visual files include:

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
SELF_AUDIT.md
PROGRAM_TO_VISUAL_DIRECTOR_BRIEF.md
PRODUCTION_CORRECTION_REGISTER.md
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md
```

## 4. Canonical identifiers

```text
WINDOW ID: W02
TREE ID: HKA-TREE-<2_DIGIT_DOMAIN>-<SHORT_CODE>
NODE ID: HKA-WXX-<TREE_CODE>-<4_DIGIT_SEQUENCE>
RELATION ID: HKA-REL-WXX-<5_DIGIT_SEQUENCE>
VCU ID: HKA-VCU-WXX-<3_DIGIT_SEQUENCE>
ASSET ID: HKA-VIS-WXX-<4_DIGIT_SEQUENCE>
BATCH ID: HKA-WXX-BYY
RUN ID: HKA-WXX-BYY-RZZ
RELEASE ID: HKA-WXX-REL-<4_DIGIT_SEQUENCE>
```

Asset regex:

```regex
^HKA-VIS-W[0-9]{2}-[0-9]{4}$
```

Batch regex:

```regex
^HKA-W[0-9]{2}-B[0-9]{2}$
```

Run regex:

```regex
^HKA-W[0-9]{2}-B[0-9]{2}-R[0-9]{2}$
```

## 5. IMG Unit ID

IMG Unit là execution-window identity, không thay Batch ID hay Run ID.

```text
IMG-WXX-BYY-UZZ-RNN
```

Regex:

```regex
^IMG-W[0-9]{2}-B[0-9]{2}-U[0-9]{2}-R[0-9]{2}$
```

Ví dụ:

```text
BATCH: HKA-W02-B01
RUN: HKA-W02-B01-R01

IMG-W02-B01-U01-R01 → HKA-VIS-W02-0003, 0004
IMG-W02-B01-U02-R01 → HKA-VIS-W02-0005, 0006
IMG-W02-B01-U03-R01 → HKA-VIS-W02-0007, 0008
```

Một IMG Unit được authorize tối đa 2 Asset IDs. Unit ID không được tái sử dụng cho một assignment khác.

## 6. Image filenames

```text
<ASSET_ID>_CLEAN_MASTER.png
<ASSET_ID>_BRANDED_FINAL.png
```

Không thêm `latest`, `new`, `final-final`, producer name hoặc timestamp vào canonical filename.

## 7. Batch files

```text
BATCH_MANIFEST.json
BATCH_MANIFEST.sha256
BATCH_PROMPTS.md
PRODUCTION_STATUS.json
PRODUCTION_REPORT.md
SELF_QA_REPORT.json
INDEPENDENT_QA_REPORT.json
SHA256SUMS.txt
R2_UPLOAD_RECEIPT.json
RELEASE_INDEX.json
```

IMG unit-specific execution pack có thể lưu dưới:

```text
PRODUCTION/BATCHES/<BATCH_ID>/IMG_UNITS/<IMG_UNIT_ID>/IMG_EXECUTION_PACK.md
```

và correction receipts dưới cùng namespace nếu Window Contract cho phép.

## 8. Versioning

- document: `MAJOR.MINOR`;
- prompt record: increment khi semantic output requirement thay đổi;
- manifest: increment sau lock khi asset membership/metadata thay đổi;
- Run ID: tăng khi canonical batch run được tái sản xuất; không overwrite run cũ.

## 9. R2 canonical buckets

```text
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery
```

Director Layer không thêm bucket staging nếu chưa có canonical amendment.

## 10. R2 namespace

```text
v1/windows/<WINDOW_ID>-<tree-slug>/
  prompt-commit/<FULL_40_CHAR_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

Không dùng IMG Unit ID thay canonical Batch/Run namespace trong Vault.

## 11. SHA formatting

- Git SHA: 40 lowercase hex;
- SHA-256: 64 lowercase hex;
- machine-readable records không dùng SHA rút gọn.

## 12. Timestamps

Machine-readable timestamps dùng ISO 8601 UTC.

## 13. Forbidden ambiguous names

```text
latest
current
new
final-final
approved-new
image1.png
asset-final.png
batch-last
```

## 14. Validation

Mọi identifier/path phải validate trước `PROMPT_LOCKED`, `BATCH_READY`, `QA_APPROVED` hoặc `R2_VERIFIED`. IMG Unit assignment phải additionally validate `authorized_asset_count <= 2`.