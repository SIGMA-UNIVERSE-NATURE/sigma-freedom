---
title: "HKA CINEMATIC 4K Cloudflare Pipeline — Amendment 1.1"
project: "Human Knowledge Academic"
version: "1.1"
status: "MANDATORY / OVERRIDES CONFLICTING 1.0 RELEASE-ORDER TEXT"
language: "vi"
date: "2026-09-03"
---

# HKA CLOUDFLARE PIPELINE — AMENDMENT 1.1

Tài liệu này sửa và làm rõ thứ tự release trong:

```text
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_BATCH_PIPELINE.md
```

Nếu có mâu thuẫn về `R2_UPLOAD_RECEIPT.json`, `RELEASED.json` hoặc prefix lock, **Amendment 1.1 có hiệu lực cao hơn**.

## 1. Nguyên tắc

`RELEASED.json` phải là object cuối cùng được ghi vào **release prefix trong `hka-c4k-vault`**. Sau khi marker được xác minh, prefix được khóa. Báo cáo xác nhận marker và lock được ghi sang **`hka-c4k-audit`**, không ghi thêm object vào release prefix đã khóa.

## 2. Thứ tự chuẩn không được thay đổi

```text
1. Upload CLEAN MASTER objects
2. Upload BRANDED FINAL objects
3. Upload asset metadata sidecars
4. Upload prompts and manifests
5. Upload production and independent QA reports
6. Upload SHA256SUMS.txt
7. Upload batch package ZIP
8. Verify object count, metadata and SHA-256
9. Generate and upload R2_UPLOAD_RECEIPT.json
10. Verify R2_UPLOAD_RECEIPT.json
11. Generate and upload RELEASED.json as the final vault-prefix object
12. Verify RELEASED.json
13. Apply bucket lock to the complete release prefix
14. Write R2_RELEASE_AUDIT_RECORD.json to hka-c4k-audit
15. Update GitHub RELEASE_INDEX.json with the audit-record key and SHA-256
```

## 3. Trạng thái

`R2_UPLOAD_RECEIPT.json` chỉ được mang trạng thái:

```text
R2_OBJECTS_VERIFIED
```

Nó chứng minh tất cả release objects trước marker đã được upload và xác minh, đồng thời cho phép ghi release marker.

`R2_RELEASE_AUDIT_RECORD.json` mang trạng thái:

```text
R2_VERIFIED
```

Nó chứng minh:

- `RELEASED.json` tồn tại và checksum đúng;
- prefix lock đã được áp dụng;
- release đã trở thành bất biến theo chính sách khóa;
- GitHub có thể ghi nhận release hoàn tất.

## 4. Schema bắt buộc

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-upload-receipt.schema.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-r2-release-record.schema.json
```

## 5. Điều kiện đọc của website

Trong giai đoạn website sau này, một batch chỉ được xem là hợp lệ nếu đồng thời có:

```text
RELEASED.json in hka-c4k-vault
+
R2_RELEASE_AUDIT_RECORD.json in hka-c4k-audit
+
matching SHA-256 values
+
GitHub RELEASE_INDEX status = R2_VERIFIED or WEB_APPROVED
```

Chỉ thấy `RELEASED.json` mà không có audit record không đủ để xuất bản.

---

> **Marker đóng gói release. Audit record chứng minh marker đã được khóa. Không ghi thêm vào release prefix sau khi khóa.**
