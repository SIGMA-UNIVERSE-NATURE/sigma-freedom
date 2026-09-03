---
title: "HKA — Directory, Identifier & Naming Standard"
version: "1.0"
status: "REFERENCE STANDARD"
language: "vi"
date: "2026-09-03"
---

# HKA DIRECTORY, IDENTIFIER & NAMING STANDARD

## 1. Mục tiêu

Mọi đường dẫn, mã và filename phải có thể được phân tích bằng máy, đọc được bởi con người và không phụ thuộc vào từ `latest`. Một mã đã phát hành không được tái sử dụng cho nội dung khác.

## 2. Git repositories

```text
KNOWLEDGE / PROMPT CONTROL PLANE:
SIGMA-UNIVERSE-NATURE/sigma-freedom

OFFICIAL BRAND ASSET SOURCE:
linkcomltd-byte/sigma-universe-web
```

## 3. Git branches

### Canonical base

```text
hka-knowledge-system-trees
```

### Window execution

```text
hka-tree/wXX-<tree-slug>
```

Regex:

```regex
^hka-tree/w[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*$
```

Không dùng khoảng trắng, chữ hoa, dấu tiếng Việt hoặc `/latest` trong slug.

### Production, QA và release

Production Window và QA Window không bắt buộc có branch riêng nếu chỉ trả package binary qua kênh tạm thời; mọi metadata chính thức vẫn phải được commit vào execution branch hoặc một branch audit được contract chỉ định. Không tự phát minh branch nếu contract không cho phép.

## 4. Git directory cấp cửa sổ

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/WXX_<UPPER_SNAKE_SLUG>/
```

Ví dụ:

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W10_MATHEMATICS_FORMAL_SYSTEMS/
```

Regex segment:

```regex
^W[0-9]{2}_[A-Z0-9]+(?:_[A-Z0-9]+)*$
```

## 5. Mã định danh

### 5.1. Window ID

```text
W01 ... W99
```

Regex:

```regex
^W[0-9]{2}$
```

### 5.2. Tree ID

```text
HKA-TREE-<2_DIGIT_DOMAIN>-<SHORT_CODE>
```

Ví dụ:

```text
HKA-TREE-01-MATH
HKA-TREE-02-CELL
```

Tree ID do Canonical Architect cấp; cửa sổ không tự đổi.

### 5.3. Node ID

```text
HKA-WXX-<TREE_CODE>-<4_DIGIT_SEQUENCE>
```

Ví dụ:

```text
HKA-W10-MATH-0001
```

Node ID không mang nghĩa phiên bản. Sửa nội dung node tăng node version, không đổi ID trừ khi đó là node khác.

### 5.4. Relation ID

```text
HKA-REL-WXX-<5_DIGIT_SEQUENCE>
```

Ví dụ:

```text
HKA-REL-W10-00001
```

### 5.5. Visual Coverage Unit ID

```text
HKA-VCU-WXX-<3_DIGIT_SEQUENCE>
```

### 5.6. Asset ID

```text
HKA-VIS-WXX-<4_DIGIT_SEQUENCE>
```

Regex:

```regex
^HKA-VIS-W[0-9]{2}-[0-9]{4}$
```

Không tái sử dụng Asset ID cho ý tưởng hình ảnh khác.

### 5.7. Batch ID

```text
HKA-WXX-B00 ... HKA-WXX-B99
```

`B00` luôn là calibration batch của cửa sổ.

Regex:

```regex
^HKA-W[0-9]{2}-B[0-9]{2}$
```

### 5.8. Run ID

```text
HKA-WXX-BYY-RZZ
```

Ví dụ:

```text
HKA-W10-B01-R01
```

Tái sản xuất output trong cùng batch tăng `RZZ`. Không ghi đè run cũ.

### 5.9. Release ID

```text
HKA-WXX-REL-<4_DIGIT_SEQUENCE>
```

Mỗi release bất biến có Release ID mới.

## 6. Phiên bản

### Tài liệu

```text
MAJOR.MINOR
```

- MAJOR: thay đổi không tương thích hoặc thay mục tiêu/phạm vi.
- MINOR: bổ sung tương thích, làm rõ, sửa lỗi không phá vỡ.

### Prompt record

```text
1.0, 1.1, 2.0
```

Prompt thay đổi dẫn đến output khác phải tăng version và tính prompt SHA mới.

### Manifest

```text
MANIFEST VERSION: 1, 2, 3...
```

Sau `MANIFEST_LOCKED`, mọi thêm/bớt/thay Asset ID phải tăng version.

## 7. Tên file học thuật và sản xuất

### Cấp cửa sổ

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
SELF_AUDIT.md
VISUAL_STRATEGY_AND_COUNT.md
VISUAL_COVERAGE_MATRIX.csv
VISUAL_PRODUCTION_MANIFEST.csv
VISUAL_PROMPTS_CINEMATIC_4K.md
VISUAL_QA_CHECKLIST.md
```

### Cấp batch

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

### Image files

```text
<ASSET_ID>_CLEAN_MASTER.png
<ASSET_ID>_BRANDED_FINAL.png
```

Regex clean:

```regex
^HKA-VIS-W[0-9]{2}-[0-9]{4}_CLEAN_MASTER\.png$
```

Regex branded:

```regex
^HKA-VIS-W[0-9]{2}-[0-9]{4}_BRANDED_FINAL\.png$
```

Không thêm từ `final-final`, `new`, `latest`, tên người sản xuất hoặc timestamp vào filename canonical. Run/Release nằm trong path và metadata.

## 8. R2 buckets

```text
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery
```

- `vault`: canonical masters và approved release package.
- `audit`: receipts, release audit records và events.
- `delivery`: website derivatives sau WEB_APPROVED.

## 9. R2 namespace

```text
v1/windows/<WINDOW_ID>-<tree-slug>/
  prompt-commit/<FULL_40_CHAR_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

Ví dụ:

```text
v1/windows/W10-mathematics-formal-systems/
  prompt-commit/0123456789abcdef0123456789abcdef01234567/
  batches/HKA-W10-B01/
  runs/HKA-W10-B01-R01/
```

Full prefix regex:

```regex
^v1/windows/W[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*/prompt-commit/[a-f0-9]{40}/batches/HKA-W[0-9]{2}-B[0-9]{2}/runs/HKA-W[0-9]{2}-B[0-9]{2}-R[0-9]{2}/$
```

Window ID phải khớp ở mọi đoạn.

## 10. R2 asset paths

```text
assets/<ASSET_ID>/clean/<CLEAN_SHA256>/<ASSET_ID>_CLEAN_MASTER.png
assets/<ASSET_ID>/branded/<BRANDED_SHA256>/<ASSET_ID>_BRANDED_FINAL.png
assets/<ASSET_ID>/metadata/<ASSET_ID>_ASSET.json
```

Content SHA trong path làm cho object bất biến và tránh ghi đè.

## 11. Release marker và audit

Trong vault prefix:

```text
RELEASED.json
```

Đây là object cuối cùng được ghi trước khi khóa prefix.

Trong audit bucket:

```text
v1/releases/<RELEASE_ID>/R2_RELEASE_AUDIT_RECORD.json
```

Không ghi thêm vào vault prefix sau lock.

## 12. Trạng thái supersede và revoke

- `SUPERSEDED`: release vẫn tồn tại cho audit nhưng không còn là lựa chọn hiện hành.
- `REVOKED`: release bị cấm sử dụng do lỗi nghiêm trọng.
- Không xóa âm thầm.
- Release mới phải nêu `supersedes_release_id` khi áp dụng.

## 13. Timestamps

Dùng ISO 8601 UTC:

```text
2026-09-03T04:30:00Z
```

Không dùng múi giờ địa phương trong machine-readable records.

## 14. SHA formatting

- Git commit SHA: 40 ký tự hex thường.
- SHA-256: 64 ký tự hex thường.
- Không rút gọn trong manifest hoặc receipt.
- SHA rút gọn chỉ được dùng trong prose, không dùng làm khóa.

## 15. Cấm đặt tên mơ hồ

Không dùng:

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

## 16. Validation rule

Mọi identifier và path phải được kiểm bằng schema/regex trước khi `PROMPT_LOCKED`, `BATCH_READY`, `QA_APPROVED` hoặc `R2_VERIFIED`.
