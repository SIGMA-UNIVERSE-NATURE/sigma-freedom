---
title: "HKA W01 — Production Governance Standard"
window_id: "W01"
version: "1.0"
status: "REFERENCE IMPLEMENTATION"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — PRODUCTION GOVERNANCE STANDARD

## 1. Mục đích

Tài liệu này biến kiến trúc HKA CINEMATIC 4K thành một quy trình có thể thi hành, kiểm đếm, kiểm định và truy vết. Không tác nhân nào được tự suy đoán phần việc thuộc tác nhân khác.

```text
Canonical standards
→ Window Contract
→ Academic development
→ Visual strategy and locked count
→ Prompt records
→ Batch manifests
→ Production
→ Self-QA
→ Independent QA
→ R2 release
→ Website approval later
```

## 2. Thứ bậc hiệu lực

Khi có mâu thuẫn, áp dụng theo thứ tự:

1. Amendment có phiên bản cao hơn.
2. JSON Schema hiện hành cho hồ sơ tương ứng.
3. HKA CINEMATIC 4K Brand Asset Lock.
4. HKA Cloudflare Batch Pipeline.
5. HKA CINEMATIC 4K Production Standard.
6. Window Contract đã khóa.
7. Nội dung do cửa sổ tạo.

Không được giải quyết mâu thuẫn bằng sửa âm thầm. Mọi điểm cần đổi canonical phải vào `CHANGE_REQUESTS.md`.

## 3. Vai trò và decision rights

### 3.1. Canonical Architect

Được quyền:

- phát hành và khóa Window Contract;
- quyết định phạm vi, Tree ID, Window ID và tiêu chuẩn đầu ra;
- chấp nhận hoặc trả lại kết quả qua Architect Acceptance Gate;
- phê duyệt thay đổi canonical;
- cho phép merge, production, R2 release hoặc website integration bằng quyết định riêng.

Không thay QA độc lập bằng nhận xét cảm tính.

### 3.2. Prompt Window

Đầu vào:

- canonical index commit SHA;
- window contract commit SHA;
- brand asset commit SHA;
- phạm vi duy nhất.

Được quyền:

- phát triển nội dung học thuật trong phạm vi;
- tạo node/relation/source catalogs;
- thiết kế Visual Coverage Units;
- chọn hoặc nhận gói P12–P36;
- viết prompt, manifest và batch handoff.

Không được:

- sản xuất hình;
- sửa output hình;
- upload R2;
- thay canonical;
- chiếm nội dung cửa sổ khác;
- dùng từ `latest` thay cho SHA.

### 3.3. Image Production Window

Đầu vào bắt buộc:

- Prompt Commit SHA;
- Manifest SHA-256;
- Batch ID và Run ID;
- exact Asset IDs;
- brand repo + immutable commit + exact paths.

Được quyền tạo đúng CLEAN MASTER và BRANDED FINAL trong batch.

Không được sửa prompt. Nếu prompt mâu thuẫn, thiếu hoặc không thể thực hiện an toàn, trả `PROMPT_BLOCKED`.

### 3.4. Independent QA Window

Độc lập với Production Window. Kiểm 100% asset ở full resolution qua sáu gate:

- Academic;
- Pedagogy;
- Visual;
- Character & Brand;
- Accessibility;
- Integrity.

Chỉ trả `QA_APPROVED`, `QA_REJECTED` hoặc `QA_BLOCKED`. Không sửa hình và không viết lại prompt.

### 3.5. Release Uploader

Chỉ hoạt động sau `QA_APPROVED`. Xác minh SHA, upload R2 theo đúng thứ tự, ghi receipt, ghi `RELEASED.json` cuối cùng trong vault prefix, khóa prefix, ghi audit record và cập nhật release index.

### 3.6. Website Publisher

Chỉ hoạt động sau lệnh `WEB_APPROVED`. Không được xem `R2_VERIFIED` là quyền tự động deploy.

## 4. State machine duy nhất

```text
DRAFT
→ ACADEMIC_REVIEWED
→ PROMPT_LOCKED
→ BATCH_READY
→ PRODUCTION_CLAIMED
→ PRODUCING
→ SELF_QA
→ QA_REVIEW
```

Từ `QA_REVIEW`:

```text
QA_REJECTED
→ REWORK_REQUIRED
→ NEW RUN ID
→ QA_REVIEW
```

hoặc:

```text
QA_BLOCKED
→ PROMPT_REVISION_REQUIRED
→ NEW PROMPT COMMIT SHA
→ BATCH_READY
```

hoặc:

```text
QA_APPROVED
→ R2_UPLOAD_AUTHORIZED
→ UPLOADING
→ R2_VERIFYING
→ R2_OBJECTS_VERIFIED
→ RELEASED
→ R2_VERIFIED
→ WEB_APPROVED later
→ PUBLISHED later
```

Không nhảy trạng thái. Mỗi chuyển trạng thái phải có bằng chứng và hồ sơ hợp schema.

## 5. Definition of Ready

### 5.1. Prompt Window Ready

- Có Window ID, Tree ID và phạm vi duy nhất.
- Đọc được toàn bộ nguồn bắt buộc tại SHA đã khóa.
- Có execution branch.
- Có allowed write prefix.
- Brand references tồn tại.
- Không có blocker P0.

### 5.2. Batch Ready for Production

- Prompt records hoàn chỉnh.
- `BATCH_MANIFEST.json` hợp schema.
- Asset count khớp manifest.
- Prompt SHA-256 tồn tại cho từng asset.
- Prompt Commit SHA là 40 ký tự và tồn tại.
- Một batch chỉ dùng một Prompt Commit SHA.
- Không còn placeholder.
- Status là `BATCH_READY`.

### 5.3. Ready for Independent QA

- Đủ CLEAN MASTER và BRANDED FINAL.
- Package SHA-256 tồn tại.
- `PRODUCTION_REPORT.md` và `SELF_QA_REPORT.json` hoàn chỉnh.
- Filename, count và checksums khớp manifest.

### 5.4. Ready for R2 Upload

- Independent QA status là `QA_APPROVED`.
- P0=P1=P2=P3 unresolved=0.
- QA report SHA-256 hợp lệ.
- Release ID được cấp.
- R2 prefix chưa tồn tại hoặc chưa khóa.

## 6. Definition of Done

### 6.1. Prompt Window Done

- Toàn bộ file bắt buộc tồn tại.
- 100% cành cấp 1 được ánh xạ.
- Gói hình có một con số khóa cứng.
- Prompt ↔ manifest là quan hệ 1:1.
- Batch mapping chính xác.
- Brand references và MOTTO chính xác.
- Self-audit trung thực.
- Không sửa ngoài prefix.
- Báo Content Commit SHA và Final Manifest Commit SHA.

### 6.2. Production Batch Done

- 100% Asset IDs được tạo.
- N CLEAN MASTER và N BRANDED FINAL.
- Self-QA pass.
- Package và checksums hoàn chỉnh.
- Chưa đồng nghĩa QA approved.

### 6.3. R2 Release Done

- Upload receipt được xác minh.
- `RELEASED.json` là object cuối trong vault prefix.
- Release marker checksum đúng.
- Prefix lock đã áp dụng.
- Audit record tồn tại trong audit bucket.
- GitHub release index được cập nhật.

## 7. SHA chain

Mỗi Asset ID phải truy ngược được qua:

```text
CANONICAL_INDEX_COMMIT_SHA
WINDOW_CONTRACT_COMMIT_SHA
PROMPT_CONTENT_COMMIT_SHA
FINAL_MANIFEST_COMMIT_SHA
BRAND_ASSET_COMMIT_SHA
PROMPT_SHA256
MANIFEST_SHA256
CLEAN_MASTER_SHA256
BRANDED_FINAL_SHA256
BATCH_PACKAGE_SHA256
QA_REPORT_SHA256
R2_UPLOAD_RECEIPT_SHA256
R2_RELEASE_AUDIT_RECORD_SHA256
RELEASE_INDEX_SHA256
```

Git SHA chứng minh phiên bản repository. SHA-256 chứng minh nội dung byte. Không dùng ETag thay SHA-256.

## 8. Quy tắc hai commit cho prompt và manifest

Để tránh tự tham chiếu:

1. Hoàn thiện toàn bộ prompt source, strategy, coverage và batch prompt files.
2. Commit; SHA này là `PROMPT_CONTENT_COMMIT_SHA`.
3. Tạo/cập nhật manifests tham chiếu SHA đó.
4. Tính manifest SHA-256 và sidecar.
5. Commit; SHA cuối là `FINAL_MANIFEST_COMMIT_SHA`.

Manifest không được tự trỏ đến commit chứa chính lần cập nhật manifest đó. Handoff phải ghi cả hai SHA và giải thích vai trò.

## 9. Stop conditions

Bất kỳ tác nhân nào cũng phải trả `BLOCKED` khi:

- thiếu hoặc không xác minh được SHA bắt buộc;
- thiếu GitHub write capability cho nhiệm vụ bắt buộc phải commit;
- manifest không hợp schema;
- checksum không khớp;
- prompt sai hoặc mâu thuẫn nguồn;
- Asset ID ngoài manifest;
- batch trộn nhiều Prompt Commit SHA;
- brand asset không đúng commit/path;
- MOTTO sai ký tự;
- có yêu cầu ghi đè release;
- có yêu cầu upload trước QA;
- có yêu cầu deploy khi production HOLD.

Dừng an toàn không phải thất bại. Tuyên bố thành công khi thiếu bằng chứng là P0.

## 10. Phân loại lỗi và đường sửa

| Mức | Ví dụ | Hành động |
|---|---|---|
| P0 | Sai SHA, sai nguồn, nhầm batch, deploy trái phép, brand giả | Dừng batch và đóng băng phần liên quan |
| P1 | Sai cơ chế, giải phẫu, lịch sử, tỷ lệ hoặc nội dung giảng dạy | Fail asset; xem xét prompt hay output |
| P2 | Bố cục, ánh sáng, pose, độ rõ chưa đạt | Tái sản xuất asset bằng Run ID mới nếu output sai |
| P3 | Metadata, alt text, filename, report | Sửa metadata; tăng version khi cần |

Nếu prompt đúng nhưng output sai: giữ Prompt Commit SHA, tăng Run ID.

Nếu prompt sai: tạo Prompt Commit SHA mới; batch cũ không được tiếp tục.

## 11. Escalation path

```text
Execution uncertainty
→ BLOCKED report with evidence
→ Canonical Architect decision
→ Contract clarification or canonical change request
→ New immutable commit
→ Resume from authorized state
```

Không giải quyết bằng tin nhắn ngoài hồ sơ mà không đưa quyết định trở lại GitHub.

## 12. Nguyên tắc không tự suy đoán

Tác nhân phải dùng chính xác:

- repo;
- branch;
- commit SHA;
- path;
- schema version;
- Asset ID;
- Batch ID;
- Run ID;
- Release ID.

Nếu một dữ kiện bắt buộc không có, phải dừng. Không được lấy file cùng tên ở branch khác hoặc chọn asset “gần giống”.

## 13. Quy tắc số lượng

- Prompt Window khóa P12/P18/P24/P30/P36.
- Batch tối đa 6 asset.
- B00 luôn là calibration batch 2 asset.
- Không dùng khoảng số lượng.
- Không thêm asset ngoài manifest để “bù”.
- Một asset sửa vẫn giữ Asset ID, nhưng tăng Run ID/revision; ý tưởng mới phải có Asset ID mới.

## 14. Trách nhiệm cuối

Mục tiêu không phải tối đa hóa số file. Mục tiêu là để mỗi đầu ra có thể được giao nguyên vẹn, sản xuất đúng, từ chối đúng và truy vết đến tận nguồn quyết định.