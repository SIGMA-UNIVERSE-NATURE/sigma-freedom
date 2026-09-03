---
title: "HKA Image Production Window Standard"
version: "1.0"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA IMAGE PRODUCTION WINDOW STANDARD

## 1. Core rule

```text
CONTENT WINDOW DOES NOT GENERATE IMAGES.
IMG UNIT DOES NOT WRITE CURRICULUM.
IMG UNIT DOES NOT EDIT PROMPTS.
MAXIMUM AUTHORIZED ASSETS PER IMG UNIT: 2.
```

Batch remains the canonical manifest/QA/release unit. IMG Unit is only the generation-execution unit.

## 2. Naming

Canonical IDs remain:

```text
BATCH ID: HKA-W02-B01
RUN ID: HKA-W02-B01-R01
ASSET ID: HKA-VIS-W02-0003
```

Execution-window display ID:

```text
IMG-W02-B01-U01-R01
IMG-W02-B01-U02-R01
IMG-W02-B01-U03-R01
```

Example assignment:

```text
U01 → 0003, 0004
U02 → 0005, 0006
U03 → 0007, 0008
```

Unit number is not a replacement for Batch ID or Run ID.

## 3. Mandatory execution pack

IMG Unit receives exact values; it does not discover or select them.

```text
WINDOW ID
TREE ID
BATCH ID
RUN ID
IMG UNIT ID
AUTHORIZED ASSET IDS (1 or 2)

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

## 4. Reference gate

Mọi asset có Companion phải load exact official PNG bytes từ:

```text
linkcomltd-byte/sigma-universe-web
2d3aa9d8418acccd39a3d263e917d4157e029e17
```

Không được dùng generated output trước làm character reference cho output sau.

Nếu tool không thể nạp official visual reference:

```text
STATUS: ASSET_REFERENCE_BLOCKED
```

## 5. Per-asset fresh-source cycle

Trước mỗi Asset ID:

1. reread exact prompt;
2. verify prompt SHA;
3. reread mandatory/forbidden objects;
4. reread representation type;
5. reload required official references;
6. reread PASS/FAIL;
7. generate CLEAN MASTER;
8. self-check;
9. only after pass, create BRANDED FINAL by controlled post-production;
10. lock file hashes;
11. reset context to source before next asset.

Không dùng “same as previous image” làm specification.

## 6. Hard pre-next-asset check

Tất cả phải YES:

```text
ASSET ID CORRECT
PROMPT SHA VERIFIED
OFFICIAL REFERENCES USED
MANDATORY OBJECTS COMPLETE
FORBIDDEN OBJECTS ABSENT
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

Một `NO` = không chuyển sang asset kế.

## 7. Unit close

Sau 1–2 assets:

```text
STATUS: PRODUCTION_UNIT_COMPLETE
```

Không giao thêm asset vào cùng cửa sổ.

## 8. Rework and Run ID

Nếu output error:

- không overwrite R01;
- Director ghi correction;
- canonical Batch Run tăng theo existing rework rule;
- chỉ failed assets cần regenerate;
- accepted bytes từ run trước chỉ được carry forward vào snapshot mới khi provenance và SHA được ghi rõ;
- Independent QA kiểm final complete batch snapshot.

Nếu cùng failure lặp hai lần, không tự động mở run thứ ba. Director phải xử lý root cause.

## 9. Error classes

```text
OUTPUT_ERROR
PROMPT_ERROR
REFERENCE_ERROR
MODEL_CAPABILITY_ERROR
SYSTEMIC_ERROR
```

IMG Unit chỉ mô tả evidence; Director quyết định correction path khi lỗi không phải output đơn giản.

## 10. B00

B00 = 2 assets = one IMG Unit by default.

B00 Director review phải PASS trước khi mở production hàng loạt của Window.

## 11. Parallel production

Sau B00 PASS, tối đa số batch song song vẫn tuân canonical pipeline. Bên trong một batch, các IMG Units có thể chạy song song nếu dùng cùng immutable prompt/manifest locks và không chia sẻ mutable generated reference.

## 12. Production handback

Mỗi IMG Unit trả:

```text
IMG UNIT ID:
BATCH ID:
RUN ID:
AUTHORIZED ASSET IDS:
PRODUCED ASSET IDS:
OFFICIAL REFERENCES VERIFIED:
SELF-QA:
OUTPUT FILE REFERENCES:
SHA-256 PER FILE:
KNOWN LIMITATIONS:
STATUS:
```

IMG Unit không được claim `QA_APPROVED`.