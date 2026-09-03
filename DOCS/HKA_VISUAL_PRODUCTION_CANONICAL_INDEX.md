---
title: "HKA Visual Production — Canonical Document Index"
project: "Human Knowledge Academic"
version: "1.0"
status: "MANDATORY ENTRY POINT"
language: "vi"
date: "2026-09-03"
---

# HKA VISUAL PRODUCTION — CANONICAL DOCUMENT INDEX

Mọi Prompt Window, Image Production Window, Independent QA Window, Release Uploader và Website Publisher phải bắt đầu từ tài liệu này.

Không được chỉ đọc một tệp riêng lẻ rồi tự suy đoán phần còn lại.

## I. Thứ tự đọc bắt buộc

### 1. Kiến trúc tri thức

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md
```

Xác định cây, cành, nội dung học thuật và quan hệ trong HKA.

### 2. Chuẩn sản xuất CINEMATIC 4K

```text
DOCS/HKA_CINEMATIC_4K_PRODUCTION_STANDARD.md
```

Xác định gói P12–P36, Visual Coverage Unit, loại hình, phân bổ người học, nhân vật, Logo Sigma, MOTTO và hồ sơ prompt.

### 3. Khóa tài sản thương hiệu

```text
DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md
```

Xác định repo, commit SHA và exact path của bốn nhân vật cùng Logo Sigma.

### 4. Pipeline GitHub → Batch Production → QA → Cloudflare R2

```text
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_BATCH_PIPELINE.md
```

Xác định vai trò cửa sổ, batch, state machine, SHA chain, R2 namespace, QA, upload và release.

### 5. Amendment bắt buộc về thứ tự release

```text
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_1.md
```

Tệp này có quyền ưu tiên cao hơn mọi đoạn mâu thuẫn trong Pipeline 1.0 liên quan tới upload receipt, `RELEASED.json`, audit record và prefix lock.

### 6. JSON Schemas

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-visual-batch-manifest.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-production-status.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-independent-qa-report.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-upload-receipt.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-release-record.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-release-index.schema.json
```

Các file JSON không hợp schema tương ứng phải bị từ chối trước khi sản xuất hoặc release.

## II. Thứ bậc hiệu lực

Khi có mâu thuẫn:

```text
1. Amendment có số phiên bản cao hơn
2. JSON Schema hiện hành cho loại hồ sơ tương ứng
3. Brand Asset Lock
4. Cloudflare Batch Pipeline
5. CINEMATIC 4K Production Standard
6. Window-specific contract
7. Nội dung tự do do cửa sổ tạo
```

Window-specific contract không được phép hạ thấp hoặc làm trái chuẩn canonical.

## III. Source-of-truth rule

Một tác vụ chỉ hợp lệ khi ghi rõ:

```text
CANONICAL INDEX COMMIT SHA
WINDOW CONTRACT COMMIT SHA
PROMPT COMMIT SHA
BRAND ASSET COMMIT SHA
MANIFEST SHA-256
BATCH ID
RUN ID
```

Không chấp nhận các từ:

```text
latest
current
newest
bản mới nhất
file ở trên
branch đang chạy
```

nếu không đi kèm commit SHA hoặc checksum cụ thể.

## IV. Điều kiện bắt đầu theo vai trò

### Prompt Window

Chỉ bắt đầu sau khi có Window ID, Tree ID, canonical branch và phạm vi duy nhất.

### Production Window

Chỉ bắt đầu sau khi có `BATCH_READY`, Prompt Commit SHA và manifest hash hợp lệ.

### QA Window

Chỉ bắt đầu sau khi có package SHA-256 và Production Report hoàn chỉnh.

### Release Uploader

Chỉ bắt đầu sau khi Independent QA Report có trạng thái `QA_APPROVED`.

### Website Publisher

Chỉ bắt đầu sau khi release có `R2_VERIFIED` và lệnh `WEB_APPROVED` riêng.

## V. Lệnh dừng bắt buộc

Bất kỳ cửa sổ nào cũng phải dừng và trả `BLOCKED` nếu:

- thiếu commit SHA;
- manifest không hợp schema;
- checksum không khớp;
- Asset ID ngoài manifest;
- thiếu tài sản brand chính thức;
- prompt mâu thuẫn với nguồn học thuật;
- batch trộn nhiều Prompt Commit SHA;
- QA chưa APPROVED;
- production đang HOLD nhưng có yêu cầu deploy;
- có thao tác ghi đè release đã khóa.

---

> **Một entry point. Một thứ bậc hiệu lực. Một chuỗi truy vết. Không tự suy đoán.**
