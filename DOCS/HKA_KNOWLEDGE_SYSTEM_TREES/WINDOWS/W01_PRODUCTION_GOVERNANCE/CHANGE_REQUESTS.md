---
title: "HKA W01 — Change Requests"
window_id: "W01"
version: "1.0"
status: "OPEN ITEMS RECORDED"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — CHANGE REQUESTS

W01 không tự sửa canonical files. Tài liệu này công khai các điểm có thể gây thực thi không nhất quán và đề xuất quyết định ở cấp kiến trúc.

---

## CHANGE REQUEST ID: HKA-CR-W01-001

```text
SOURCE FILE AND SECTION:
DOCS/HKA_CINEMATIC_4K_PRODUCTION_STANDARD.md
Section II — BRAND ASSET LOCK

CONFLICTING AUTHORITY:
DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md
Sections 1–6
```

### Problem

Production Standard mô tả một cây thư mục blueprint nội bộ:

```text
ASSETS/HKA_BRAND/CHARACTERS/...
ASSETS/HKA_BRAND/LOGO/...
```

Trong khi Brand Asset Lock đã xác minh nguồn bất biến thực tế ở repository khác:

```text
linkcomltd-byte/sigma-universe-web
commit 2d3aa9d8418acccd39a3d263e917d4157e029e17
assets/characters/*.png
assets/logo/*.jpg
```

Nếu cửa sổ hiểu blueprint là nguồn thật, đội sản xuất có thể chờ tệp không tồn tại hoặc tự tạo bản sao không được kiểm soát.

### Risk if unchanged

- Sai source-of-truth.
- Tái thiết kế nhân vật ngoài ý muốn.
- Dùng logo/character không đúng SHA.
- Không tái lập được package.
- P0 brand integrity failure.

### Proposed change

Thêm amendment hoặc sửa Production Standard để ghi rõ:

1. Cây `ASSETS/HKA_BRAND/` chỉ là **target packaging blueprint**, không phải nguồn master hiện hành.
2. Brand Asset Lock có quyền ưu tiên.
3. Mọi prompt phải dùng external repo + immutable commit + exact path.
4. Nếu sau này mirror asset vào HKA repository, mirror phải có checksum registry và quyết định canonical riêng; không thay ngầm external source.

### Impacted windows

```text
W01–W64
All Production Windows
All QA Windows
Release Uploader
```

### Backward compatibility

Tương thích nếu chỉ làm rõ. Không đổi Asset IDs hoặc visual manifests.

### Decision required

```text
APPROVE CLARIFICATION / REJECT / REQUEST REVISION
```

### Status

```text
OPEN — NONBLOCKING FOR W01 because Canonical Index gives Brand Asset Lock higher precedence.
```

---

## CHANGE REQUEST ID: HKA-CR-W01-002

```text
SOURCE FILE AND SECTION:
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_BATCH_PIPELINE.md
Sections IV, VII, XII and XIX

WINDOW CONTRACT:
W01 WINDOW_CONTRACT.md Section VII
```

### Problem

`BATCH_MANIFEST.json` bắt buộc chứa `prompt_commit_sha`, nhưng nếu prompt và manifest được tạo trong cùng một commit bằng Contents API hoặc workflow tuần tự, manifest không thể biết SHA của commit chứa chính nó trước khi commit tồn tại. Nếu manifest trỏ tới final manifest commit, xảy ra tự tham chiếu không thể giải quyết bằng cách hash thông thường.

### Risk if unchanged

- Placeholder SHA còn lại trong manifest.
- Cửa sổ tuyên bố một SHA không tồn tại.
- Batch không tái lập được.
- Các cửa sổ dùng chiến thuật khác nhau.
- P0 traceability failure.

### Proposed change

Chuẩn hóa hai commit có vai trò khác nhau:

```text
PROMPT_CONTENT_COMMIT_SHA
Commit chứa prompt source, visual strategy, production manifest CSV và batch prompt content; chưa chứa batch manifests đã khóa.

FINAL_MANIFEST_COMMIT_SHA
Commit sau, chứa BATCH_MANIFEST.json và sidecar hashes tham chiếu PROMPT_CONTENT_COMMIT_SHA.
```

`prompt_commit_sha` trong JSON Schema phải được hiểu là `PROMPT_CONTENT_COMMIT_SHA`, không phải commit chứa manifest.

Handoff phải ghi cả hai SHA. Không yêu cầu manifest tự trỏ `FINAL_MANIFEST_COMMIT_SHA`.

### Impacted windows

```text
W01–W64
Prompt Windows
Production Windows
QA Windows
Release Index
```

### Backward compatibility

Tương thích với schema hiện tại vì tên trường không đổi; cần tài liệu giải nghĩa chính thức. Các manifest cũ phải được kiểm tra xem SHA đang trỏ loại commit nào.

### Decision required

```text
APPROVE SEMANTIC DEFINITION / REQUEST SCHEMA V2
```

### Status

```text
OPEN — W01 applies the prescribed two-commit procedure as an explicit operational interpretation.
```

---

## CHANGE REQUEST ID: HKA-CR-W01-003

```text
SOURCE FILE:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-visual-batch-manifest.schema.json
```

### Problem

JSON Schema đặt `uniqueItems: true` cho mảng object `assets`, nhưng điều này chỉ ngăn hai object hoàn toàn giống nhau; nó không bảo đảm `asset_id` duy nhất khi hai object có cùng Asset ID nhưng khác trường khác.

### Risk if unchanged

- Một Asset ID có thể xuất hiện hai lần với prompt hash hoặc filename khác nhau mà schema vẫn pass.
- Asset count, output count và QA mapping có thể mâu thuẫn.
- P0/P1 integrity failure nếu không có validation bổ sung.

### Proposed change

Một trong hai lựa chọn:

1. Bổ sung validator ngoài JSON Schema kiểm uniqueness của `asset_id`, `clean_master_filename` và `branded_final_filename`; hoặc
2. Chuyển `assets` thành object map keyed by Asset ID trong schema v2.

Trong v1, mọi Window phải tự kiểm uniqueness và ghi kết quả trong Self Audit.

### Impacted windows

```text
All Prompt Windows and batch validators
```

### Backward compatibility

Validator ngoài schema hoàn toàn tương thích. Schema v2 cần migration.

### Decision required

```text
APPROVE EXTERNAL UNIQUENESS VALIDATOR / DESIGN SCHEMA V2
```

### Status

```text
OPEN — NONBLOCKING WITH MANDATORY SELF-AUDIT CHECK.
```

---

# Summary

```text
OPEN CHANGE REQUESTS: 3
BLOCKING W01 EXECUTION: 0
REQUIRES CANONICAL ARCHITECT DECISION: 3
CANONICAL FILES MODIFIED BY W01: 0
```
