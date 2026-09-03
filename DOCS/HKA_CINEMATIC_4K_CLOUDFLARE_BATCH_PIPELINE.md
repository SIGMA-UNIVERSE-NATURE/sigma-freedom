---
title: "HKA CINEMATIC 4K — GitHub to Cloudflare R2 Batch Production Protocol"
project: "Human Knowledge Academic"
version: "1.0"
status: "MANDATORY"
language: "vi"
date: "2026-09-03"
---

# HKA CINEMATIC 4K — GITHUB → BATCH PRODUCTION → QA → CLOUDFLARE R2
## Quy trình chuẩn hóa sản xuất, kiểm định, lưu trữ và phát hành hình ảnh

Tài liệu này là hợp đồng vận hành bắt buộc cho toàn bộ HKA Knowledge System Trees. Nó chuẩn hóa luồng giao việc giữa cửa sổ viết prompt, cửa sổ sản xuất hình ảnh, cửa sổ kiểm định và kho Cloudflare.

Mục tiêu cuối cùng:

> **Sản xuất đúng nội dung giảng dạy, đúng số lượng, đúng nhận diện, đúng độ phân giải, truy vết được từng thay đổi và không đưa tài sản chưa đạt lên website.**

Tài liệu phải được đọc cùng:

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md
DOCS/HKA_CINEMATIC_4K_PRODUCTION_STANDARD.md
DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md
```

---

# I. QUYẾT ĐỊNH KIẾN TRÚC

## 1. GitHub là control plane

GitHub lưu và quản trị:

- kiến trúc tri thức;
- prompt;
- manifest;
- batch assignment;
- trạng thái sản xuất;
- báo cáo tự kiểm định;
- báo cáo kiểm định độc lập;
- checksum registry;
- release index;
- lịch sử phiên bản;
- commit SHA làm mốc bất biến.

GitHub **không phải kho chứa lâu dài cho ảnh 4K**. Không commit hàng loạt PNG 4K vào Git history.

## 2. Cloudflare R2 là binary asset plane

Cloudflare R2 lưu:

- CLEAN MASTER 4K;
- BRANDED FINAL 4K;
- Research Poster 4K;
- package ZIP;
- manifest đã khóa;
- checksum;
- QA report;
- upload receipt;
- release marker;
- provenance metadata.

## 3. Website là delivery plane

`sigmastudy.net` chỉ được đọc những release đã đạt trạng thái:

```text
R2_VERIFIED + RELEASED + WEB_APPROVED
```

Website không được đọc trực tiếp thư mục đang sản xuất, đang kiểm định, bị từ chối hoặc chưa có release marker.

## 4. Không dùng từ “branch” mơ hồ

Ba khái niệm phải tách biệt:

```text
GIT BRANCH
Nhánh làm việc trên GitHub.

KNOWLEDGE TREE BRANCH
Cành tri thức thuộc HKA World Tree.

R2 NAMESPACE
Tiền tố object key dùng để tách kho ảnh theo Window ID và Knowledge Tree.
```

Cloudflare R2 không có Git branch. Vì vậy, mỗi cành tri thức được tách bằng namespace bất biến chứa Window ID, tree slug, Git commit SHA, Batch ID và Run ID.

---

# II. CÁC NGUỒN BẤT BIẾN

## 1. Knowledge System source

```text
Repository: SIGMA-UNIVERSE-NATURE/sigma-freedom
Base branch: hka-knowledge-system-trees
Canonical tree: DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md
```

## 2. Official brand assets

```text
Repository: linkcomltd-byte/sigma-universe-web
Immutable commit: 2d3aa9d8418acccd39a3d263e917d4157e029e17
```

Characters:

```text
assets/characters/sigma.png
assets/characters/cricket.png
assets/characters/little-ant.png
assets/characters/professor-owl.png
```

Logo:

```text
assets/logo/sigma-logo-master.jpg
assets/logo/sigma-emblem-shell.jpg
```

Exact MOTTO:

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Không dùng branch mutable thay cho commit SHA trong sản xuất.

---

# III. HỆ ĐỊNH DANH

Mọi thành phần phải có mã duy nhất.

```text
WINDOW ID       W10
TREE ID         HKA-TREE-01-MATH
BATCH ID        HKA-W10-B00
RUN ID          HKA-W10-B00-R01
ASSET ID        HKA-VIS-W10-0001
RELEASE ID      HKA-W10-REL-0001
```

Quy tắc:

- Không tái sử dụng Asset ID cho ý tưởng khác.
- Không tái sử dụng Run ID cho lần sản xuất khác.
- Tái sản xuất một asset phải tăng Run ID hoặc Revision.
- Một release mới phải có Release ID mới.
- Không đổi nội dung dưới cùng một content SHA.

---

# IV. CHUỖI SHA BẮT BUỘC

Mỗi batch phải lưu đầy đủ:

```text
PROMPT_COMMIT_SHA
40 ký tự Git SHA của commit chứa prompt và manifest.

BRAND_ASSET_COMMIT_SHA
2d3aa9d8418acccd39a3d263e917d4157e029e17

MANIFEST_SHA256
SHA-256 của BATCH_MANIFEST.json canonicalized.

PROMPT_SHA256
SHA-256 riêng cho prompt của từng Asset ID.

CLEAN_MASTER_SHA256
SHA-256 của tệp CLEAN MASTER.

BRANDED_FINAL_SHA256
SHA-256 của tệp BRANDED FINAL.

BATCH_PACKAGE_SHA256
SHA-256 của gói ZIP bàn giao.

QA_REPORT_SHA256
SHA-256 của báo cáo QA đã duyệt.

RELEASE_INDEX_SHA256
SHA-256 của release index.
```

Không dùng ETag thay cho SHA-256 chuẩn của nội dung.

## Canonical hashing rule

- UTF-8;
- line ending LF;
- JSON key được sắp xếp ổn định;
- không có khoảng trắng thừa;
- `MANIFEST_SHA256` được lưu ở tệp sidecar `BATCH_MANIFEST.sha256`, không tự nhúng vào nội dung đang được hash.

---

# V. KIẾN TRÚC CLOUDFLARE R2

## 1. Ba bucket chuẩn

```text
hka-c4k-vault
Kho private canonical cho package đã QA APPROVED.

hka-c4k-audit
Kho private cho event log, upload receipt, verification result và audit trail.

hka-c4k-delivery
Kho phát hành website trong giai đoạn sau; hiện giữ private và chưa kết nối production.
```

Không tạo một bucket riêng cho từng cửa sổ. Tách cửa sổ bằng prefix giúp quản trị, kiểm toán và mở rộng dễ hơn.

## 2. Trạng thái bucket

### `hka-c4k-vault`

- Private.
- Không bật `r2.dev` public access.
- Chỉ nhận batch sau independent QA APPROVED.
- Release prefix được khóa chống overwrite/delete sau khi xác minh hoàn tất.
- Không phục vụ trực tiếp cho website.

### `hka-c4k-audit`

- Private.
- Chỉ ghi log, receipts và báo cáo sự kiện.
- Không chứa ảnh dùng cho website.

### `hka-c4k-delivery`

- Private trong giai đoạn hiện tại.
- Chỉ được mở trong giai đoạn triển khai website.
- Sau này dùng custom domain, đề xuất:

```text
media.sigmastudy.net
```

- Chỉ chứa derivative hoặc branded asset đã WEB_APPROVED.
- Không chứa CLEAN MASTER.

---

# VI. R2 NAMESPACE CHUẨN

## 1. Prefix cấp cửa sổ

```text
v1/windows/<WINDOW_ID>-<TREE_SLUG>/
```

Ví dụ:

```text
v1/windows/W10-mathematics-formal-systems/
```

## 2. Prefix cấp batch release

```text
v1/windows/<WINDOW_ID>-<TREE_SLUG>/
  prompt-commit/<FULL_40_CHAR_GIT_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

## 3. Cấu trúc package hoàn chỉnh

```text
v1/windows/W10-mathematics-formal-systems/
└── prompt-commit/<FULL_GIT_SHA>/
    └── batches/HKA-W10-B01/
        └── runs/HKA-W10-B01-R01/
            ├── assets/
            │   ├── HKA-VIS-W10-0001/
            │   │   ├── clean/<CLEAN_SHA256>/HKA-VIS-W10-0001_CLEAN_MASTER.png
            │   │   ├── branded/<BRANDED_SHA256>/HKA-VIS-W10-0001_BRANDED_FINAL.png
            │   │   └── metadata/HKA-VIS-W10-0001_ASSET.json
            │   └── ...
            ├── manifests/
            │   ├── BATCH_MANIFEST.json
            │   ├── BATCH_MANIFEST.sha256
            │   └── VISUAL_PRODUCTION_MANIFEST.csv
            ├── prompts/
            │   └── BATCH_PROMPTS.md
            ├── reports/
            │   ├── PRODUCTION_REPORT.md
            │   ├── SELF_QA_REPORT.json
            │   ├── INDEPENDENT_QA_REPORT.json
            │   └── QA_REPORT.sha256
            ├── checksums/
            │   └── SHA256SUMS.txt
            ├── packages/
            │   └── <BATCH_PACKAGE_SHA256>/HKA-W10-B01-R01_RELEASE.zip
            ├── receipts/
            │   └── R2_UPLOAD_RECEIPT.json
            └── RELEASED.json
```

`RELEASED.json` phải được ghi cuối cùng. Không có `RELEASED.json` nghĩa là batch chưa được công nhận là hoàn chỉnh.

---

# VII. GITHUB DIRECTORY CHO MỖI CỬA SỔ

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/WXX_<SLUG>/
├── TREE.md
├── NODE_CATALOG.md
├── RELATION_CATALOG.md
├── SOURCE_REGISTER.md
├── SELF_AUDIT.md
├── VISUAL_STRATEGY_AND_COUNT.md
├── VISUAL_COVERAGE_MATRIX.csv
├── VISUAL_PRODUCTION_MANIFEST.csv
├── VISUAL_PROMPTS_CINEMATIC_4K.md
├── VISUAL_QA_CHECKLIST.md
└── PRODUCTION/
    └── BATCHES/
        ├── HKA-WXX-B00/
        │   ├── BATCH_MANIFEST.json
        │   ├── BATCH_MANIFEST.sha256
        │   ├── BATCH_PROMPTS.md
        │   ├── PRODUCTION_STATUS.json
        │   ├── PRODUCTION_REPORT.md
        │   ├── SELF_QA_REPORT.json
        │   ├── INDEPENDENT_QA_REPORT.json
        │   ├── SHA256SUMS.txt
        │   ├── R2_UPLOAD_RECEIPT.json
        │   └── RELEASE_INDEX.json
        └── ...
```

Ảnh 4K không nằm trong Git repo. GitHub chỉ lưu metadata, status, checksums, reports và R2 object keys.

---

# VIII. PHÂN VAI CÁC CỬA SỔ

## 1. Prompt Window

Một Prompt Window phụ trách đúng một Knowledge Tree.

Trách nhiệm:

- phát triển nội dung học thuật;
- kiểm toán độ phủ;
- chọn đúng gói P12/P18/P24/P30/P36;
- chia asset thành batch;
- viết prompt đầy đủ;
- khóa manifest;
- commit toàn bộ tài liệu;
- cung cấp Prompt Commit SHA;
- không sản xuất ảnh;
- không tự sửa output của Image Production Window;
- không upload lên R2.

## 2. Image Production Batch Window

Một Image Production Window phụ trách đúng một batch, không phụ trách cả cây.

Tên cửa sổ:

```text
IMG-<WINDOW_ID>-<BATCH_ID>-<RUN_ID>
```

Trách nhiệm:

- checkout hoặc đọc đúng Prompt Commit SHA;
- xác minh `BATCH_MANIFEST.sha256`;
- chỉ sản xuất Asset ID trong batch;
- không tự sửa prompt;
- tạo CLEAN MASTER và BRANDED FINAL;
- tính SHA-256;
- tự QA;
- tạo production report;
- giao gói batch để kiểm định;
- không upload canonical package lên R2 trước independent QA APPROVED.

Nếu prompt có lỗi, Production Window phải trả trạng thái:

```text
PROMPT_BLOCKED
```

và chỉ rõ Asset ID, lỗi, bằng chứng, đề xuất sửa. Không được âm thầm diễn giải lại prompt.

## 3. Independent QA Window

Một QA Window phụ trách đúng một batch và độc lập với Production Window.

Tên:

```text
QA-<WINDOW_ID>-<BATCH_ID>-<RUN_ID>
```

Trách nhiệm:

- xác minh Prompt Commit SHA;
- xác minh manifest hash;
- kiểm tra từng asset ở full resolution;
- kiểm tra học thuật, sư phạm, hình ảnh, nhân vật, thương hiệu, khả năng tiếp cận và file integrity;
- phát hành PASS, FAIL hoặc BLOCKED cho từng Asset ID;
- không sửa hình;
- không viết lại prompt;
- không upload R2;
- ký `INDEPENDENT_QA_REPORT.json` bằng SHA-256.

## 4. Release Uploader

Release Uploader chỉ chạy sau QA APPROVED.

Trách nhiệm:

- xác minh toàn bộ hash;
- tải đúng package lên `hka-c4k-vault`;
- ghi metadata;
- kiểm tra lại object count và checksum;
- ghi upload receipt;
- ghi `RELEASED.json` cuối cùng;
- kích hoạt bucket lock trên release prefix;
- không deploy website.

## 5. Website Publisher — giai đoạn sau

Chỉ hoạt động khi có lệnh riêng.

Trách nhiệm:

- đọc release đã WEB_APPROVED;
- tạo derivative;
- đưa sang `hka-c4k-delivery`;
- cập nhật website preview;
- không thay đổi master;
- không đụng production nếu vẫn HOLD.

---

# IX. CHIA BATCH CHUẨN

## 1. Calibration batch bắt buộc

Mỗi cửa sổ bắt đầu bằng:

```text
B00 — CALIBRATION BATCH — 2 ASSETS
```

B00 gồm:

1. HERO có đủ bốn nhân vật.
2. Một asset có nguy cơ sai học thuật hoặc sai cơ chế cao nhất trong cây.

Không mở sản xuất hàng loạt trước khi B00 đạt independent QA.

## 2. Production batch

Sau B00:

- tối đa 6 Asset IDs mỗi batch;
- không trộn Asset ID của hai Prompt Windows;
- không trộn hai Prompt Commit SHA trong cùng một batch;
- một batch phải có mục tiêu và phạm vi rõ;
- batch cuối được phép có ít hơn 6 asset.

## 3. Số batch chuẩn theo gói

| Gói | Phân bổ batch | Tổng batch |
|---|---|---:|
| P12 | 2 + 6 + 4 | 3 |
| P18 | 2 + 6 + 6 + 4 | 4 |
| P24 | 2 + 6 + 6 + 6 + 4 | 5 |
| P30 | 2 + 6 + 6 + 6 + 6 + 4 | 6 |
| P36 | 2 + 6 + 6 + 6 + 6 + 6 + 4 | 7 |

Prompt Window phải ghi chính xác Asset ID thuộc batch nào trước khi khóa manifest.

## 4. Parallelism

Sau khi B00 PASS:

- tối đa 3 Production Batches chạy song song cho cùng một Knowledge Tree;
- mỗi batch có Production Window riêng;
- không dùng một chat window sản xuất nhiều batch song song;
- QA chạy độc lập theo batch;
- nếu một batch có lỗi hệ thống, các batch chưa hoàn thành của cùng cây phải PAUSE để đánh giá ảnh hưởng.

---

# X. STATE MACHINE BẮT BUỘC

```text
DRAFT
↓
ACADEMIC_REVIEWED
↓
PROMPT_LOCKED
↓
BATCH_READY
↓
PRODUCTION_CLAIMED
↓
PRODUCING
↓
SELF_QA
↓
QA_REVIEW
├── QA_REJECTED → REWORK_REQUIRED → NEW RUN ID → QA_REVIEW
├── QA_BLOCKED  → PROMPT_REVISION_REQUIRED → NEW PROMPT COMMIT SHA
└── QA_APPROVED
      ↓
R2_UPLOAD_AUTHORIZED
      ↓
UPLOADING
      ↓
R2_VERIFYING
      ├── R2_FAILED → UPLOAD_RETRY OR NEW RUN
      └── R2_VERIFIED
            ↓
RELEASED
            ↓
WEB_APPROVED — giai đoạn sau
            ↓
PUBLISHED — giai đoạn sau
```

Không nhảy trạng thái.

---

# XI. QUY TRÌNH ĐẦU CUỐI

## Phase 1 — Prompt Window

1. Đọc canonical architecture.
2. Phát triển Knowledge Tree.
3. Kiểm toán chương trình chính.
4. Chọn gói hình.
5. Tạo VCU.
6. Gán Asset ID.
7. Chia batch.
8. Viết prompt.
9. Tạo manifest.
10. Tính hash.
11. Commit.
12. Xuất Handoff Receipt.

## Phase 2 — Production Window

1. Nhận repo, branch, Prompt Commit SHA, Batch ID.
2. Xác minh commit và hash.
3. Xác minh brand asset commit.
4. Sản xuất đúng asset count.
5. Xuất hai file cho mỗi Asset ID.
6. Tính checksum.
7. Tự kiểm định.
8. Tạo package ZIP.
9. Tạo Production Report.
10. Giao full-resolution package cho QA bằng kênh tạm thời được phê duyệt; không commit ảnh vào Git.

## Phase 3 — Independent QA

1. Xác minh package SHA.
2. Kiểm từng file.
3. Kiểm từng Asset ID.
4. Ghi lỗi theo severity.
5. PASS/FAIL/BLOCKED.
6. Tạo QA report.
7. Tính QA report SHA.

## Phase 4 — Release Upload

1. Chỉ nhận package QA APPROVED.
2. Xác minh mọi hash.
3. Upload objects.
4. Upload sidecar metadata.
5. Upload reports và manifests.
6. Verify object count.
7. Verify checksum.
8. Ghi R2 upload receipt.
9. Ghi `RELEASED.json` cuối cùng.
10. Lock release prefix.
11. Cập nhật GitHub Release Index.

## Phase 5 — Website Integration

Thực hiện sau bằng protocol riêng. Không nằm trong pipeline hiện tại.

---

# XII. BATCH MANIFEST TỐI THIỂU

```json
{
  "schema_version": "1.0",
  "window_id": "W10",
  "tree_id": "HKA-TREE-01-MATH",
  "tree_slug": "mathematics-formal-systems",
  "prompt_repository": "SIGMA-UNIVERSE-NATURE/sigma-freedom",
  "prompt_branch": "hka-tree/w10-mathematics-formal-systems",
  "prompt_commit_sha": "FULL_40_CHAR_SHA",
  "brand_repository": "linkcomltd-byte/sigma-universe-web",
  "brand_asset_commit_sha": "2d3aa9d8418acccd39a3d263e917d4157e029e17",
  "batch_id": "HKA-W10-B00",
  "run_id": "HKA-W10-B00-R01",
  "asset_count": 2,
  "assets": [
    {
      "asset_id": "HKA-VIS-W10-0001",
      "prompt_sha256": "64_HEX",
      "clean_master_filename": "HKA-VIS-W10-0001_CLEAN_MASTER.png",
      "branded_final_filename": "HKA-VIS-W10-0001_BRANDED_FINAL.png"
    }
  ],
  "status": "BATCH_READY"
}
```

Manifest phải khớp JSON schema của dự án.

---

# XIII. PRODUCTION STATUS

Mỗi batch có `PRODUCTION_STATUS.json`:

```json
{
  "batch_id": "HKA-W10-B00",
  "run_id": "HKA-W10-B00-R01",
  "prompt_commit_sha": "FULL_40_CHAR_SHA",
  "manifest_sha256": "64_HEX",
  "status": "PRODUCING",
  "asset_total": 2,
  "asset_completed": 1,
  "asset_passed_self_qa": 1,
  "asset_failed_self_qa": 0,
  "blocked_asset_ids": [],
  "updated_at": "ISO-8601-UTC"
}
```

Không dùng mô tả trạng thái tự do thay cho state machine.

---

# XIV. CỔNG KIỂM ĐỊNH

## Gate A — Academic

Pass khi:

- đúng hiện tượng;
- đúng cơ chế;
- đúng tỷ lệ;
- đúng trình tự;
- đúng bối cảnh;
- không biến giả thuyết thành sự thật;
- không dùng ẩn dụ như mô tả khoa học;
- không bỏ nội dung cốt lõi đã được manifest yêu cầu.

## Gate B — Pedagogy

Pass khi:

- có một learning objective chính;
- phù hợp nhóm người học;
- không quá tải;
- giúp quan sát, so sánh, hiểu cơ chế hoặc kết nối;
- không chỉ đẹp;
- không tạo ngộ nhận mới.

## Gate C — Visual

Pass khi:

- 4K đúng kích thước;
- bố cục rõ;
- không có vật thể vô nghĩa;
- không méo hình;
- ánh sáng không che nội dung;
- tỷ lệ hình ảnh có cue rõ;
- vùng logo/motto không che nội dung.

## Gate D — Character & Brand

Pass khi:

- nhân vật đúng master reference;
- đúng chức năng học thuật;
- HERO có đủ bốn;
- logo là asset chính thức;
- MOTTO đúng tuyệt đối;
- không có logo hoặc text do model tự bịa.

## Gate E — Accessibility

Pass khi:

- alt text đủ;
- không truyền nghĩa chỉ bằng màu;
- tương phản hợp lý;
- không dùng stereotype;
- nội dung nhạy cảm được xử lý phù hợp.

## Gate F — Integrity

Pass khi:

- đúng Asset ID;
- đúng filename;
- đủ CLEAN MASTER và BRANDED FINAL;
- checksum khớp;
- số lượng khớp manifest;
- không có file dư không khai báo;
- package SHA khớp.

---

# XV. PHÂN LOẠI LỖI

```text
P0 — CRITICAL
Sai nguồn, sai brand asset, sai sự thật nghiêm trọng, vi phạm an toàn, nhầm batch, sai SHA hoặc upload nhầm release.
Hành động: dừng toàn bộ batch và đóng băng các batch liên quan.

P1 — MAJOR
Sai cơ chế, cấu trúc, tỷ lệ, lịch sử, giải phẫu, nội dung giảng dạy hoặc thiếu thành phần bắt buộc.
Hành động: asset fail; có thể yêu cầu tái sản xuất.

P2 — MODERATE
Bố cục, ánh sáng, chi tiết, character pose, logo placement hoặc độ rõ chưa đạt nhưng không làm sai kiến thức cốt lõi.
Hành động: sửa hoặc tái sản xuất asset.

P3 — MINOR
Metadata, caption, alt text, filename hoặc format report.
Hành động: sửa metadata nếu không thay đổi nội dung hình.
```

Release yêu cầu:

```text
P0 = 0
P1 = 0
P2 = 0 unresolved
P3 = 0 unresolved in release metadata
```

---

# XVI. UPLOAD PROTOCOL

## 1. Quyền truy cập

- Prompt Window: không có Cloudflare credential.
- Production Window: không có permanent R2 credential.
- QA Window: không có write credential.
- Release Uploader: Object Read & Write, giới hạn đúng bucket.
- Audit verifier: read vault + write audit.
- Website Publisher: read release + write delivery, chỉ ở giai đoạn sau.

Ưu tiên credential ngắn hạn hoặc presigned upload cho đúng batch/prefix.

## 2. Upload order

```text
1. CLEAN MASTER objects
2. BRANDED FINAL objects
3. Asset metadata sidecars
4. Prompt and manifests
5. Production and QA reports
6. SHA256SUMS.txt
7. Package ZIP
8. R2_UPLOAD_RECEIPT.json
9. RELEASED.json — ghi cuối cùng
```

## 3. Metadata tối thiểu trên mỗi object

```text
hka-window-id
hka-tree-id
hka-batch-id
hka-run-id
hka-asset-id
hka-prompt-commit-sha
hka-manifest-sha256
hka-content-sha256
hka-brand-commit-sha
hka-qa-status
hka-release-id
```

Metadata chi tiết nằm trong sidecar JSON; custom metadata chỉ giữ khóa truy vết thiết yếu.

## 4. Verification

Sau upload:

- HEAD từng object;
- kiểm Content-Length;
- kiểm Content-Type;
- kiểm metadata;
- kiểm SHA-256 theo manifest;
- kiểm object count;
- kiểm expected filenames;
- kiểm package SHA;
- chỉ sau đó ghi `RELEASED.json`.

## 5. Immutability

- Không overwrite object đã release.
- Nội dung sửa đổi phải có SHA mới và Run ID mới.
- Sau verify, lock release prefix chống overwrite/delete.
- Release cũ được đánh dấu `SUPERSEDED`, không xóa âm thầm.

---

# XVII. R2 EVENT AUDIT

R2 upload events phải được gửi tới queue kiểm toán.

Đề xuất:

```text
Queue: hka-c4k-upload-events
Dead-letter queue: hka-c4k-upload-events-dlq
Audit sink: hka-c4k-audit
```

Consumer kiểm tra:

- key có đúng namespace không;
- metadata bắt buộc có đủ không;
- Asset ID có trong manifest không;
- checksum có khớp không;
- release marker chỉ xuất hiện sau đủ object không;
- object bất thường được ghi cảnh báo.

Event log không thay thế upload receipt; cả hai đều bắt buộc.

---

# XVIII. GITHUB ACTIONS GATE

Khi tự động hóa, workflow upload phải dùng protected environment:

```text
Environment: hka-r2-release
```

Yêu cầu:

- manual approval;
- branch/ref restriction;
- secrets chỉ mở sau approval;
- workflow input bắt buộc gồm Window ID, Batch ID, Run ID, Prompt Commit SHA và Package SHA-256;
- không cho self-approval nếu cấu hình cho phép;
- concurrency key theo Batch ID để ngăn hai upload cùng batch chạy đồng thời.

Upload workflow chỉ chạy nếu `INDEPENDENT_QA_REPORT.json` có trạng thái `QA_APPROVED`.

---

# XIX. BATCH HANDOFF RECEIPT

Prompt Window phải giao:

```text
PROMPT WINDOW:
WINDOW ID:
TREE:
GIT BRANCH:
PROMPT COMMIT SHA:
MANIFEST SHA256:
BATCH ID:
ASSET COUNT:
ASSET IDS:
BRAND ASSET COMMIT SHA:
EXPECTED CLEAN MASTER COUNT:
EXPECTED BRANDED FINAL COUNT:
EXPECTED TOTAL IMAGE FILES:
PROMPT PATH:
MANIFEST PATH:
STATUS: BATCH_READY
```

Production Window phải giao:

```text
PRODUCTION WINDOW:
BATCH ID:
RUN ID:
PROMPT COMMIT SHA VERIFIED: YES/NO
MANIFEST SHA VERIFIED: YES/NO
ASSET COUNT PRODUCED:
CLEAN MASTER COUNT:
BRANDED FINAL COUNT:
PACKAGE SHA256:
SELF QA STATUS:
BLOCKED ASSETS:
PRODUCTION REPORT PATH:
STATUS: SELF_QA_COMPLETE
```

QA Window phải giao:

```text
QA WINDOW:
BATCH ID:
RUN ID:
PACKAGE SHA256 VERIFIED: YES/NO
ASSETS PASSED:
ASSETS FAILED:
P0 COUNT:
P1 COUNT:
P2 COUNT:
P3 COUNT:
QA REPORT SHA256:
STATUS: QA_APPROVED / QA_REJECTED / QA_BLOCKED
```

Release Uploader phải giao:

```text
RELEASE ID:
BATCH ID:
RUN ID:
R2 BUCKET:
R2 PREFIX:
OBJECT COUNT EXPECTED:
OBJECT COUNT VERIFIED:
CHECKSUMS VERIFIED: YES/NO
RELEASED MARKER WRITTEN: YES/NO
PREFIX LOCK APPLIED: YES/NO
UPLOAD RECEIPT SHA256:
STATUS: R2_VERIFIED / R2_FAILED
```

---

# XX. REWORK VÀ SỬA LỖI

## 1. Output lỗi, prompt đúng

- Giữ Prompt Commit SHA.
- Tạo Run ID mới.
- Chỉ tái sản xuất Asset ID lỗi.
- QA lại toàn bộ asset được sửa.
- Package release mới phải chứa bộ hoàn chỉnh của batch.

## 2. Prompt lỗi

- Production Window trả `PROMPT_BLOCKED`.
- Prompt Window sửa prompt và manifest.
- Commit mới.
- Tạo Prompt Commit SHA mới.
- Batch mới không được tham chiếu SHA cũ.

## 3. Brand asset thay đổi

- Tạo Brand Asset Commit SHA mới.
- Không thay ngầm trên release cũ.
- Tài sản cần cập nhật phải tạo release mới.

## 4. Asset đã release nhưng phát hiện sai

- Đánh dấu release `REVOKED` hoặc `SUPERSEDED` trong release registry.
- Không xóa ngay nếu cần audit.
- Ngăn website sử dụng.
- Tạo Run ID và Release ID mới.

---

# XXI. WEBSITE INTEGRATION — CHƯA THỰC HIỆN

Giai đoạn sau sẽ:

1. Chọn release `WEB_APPROVED`.
2. Tạo derivative WebP/AVIF.
3. Đưa sang `hka-c4k-delivery`.
4. Dùng URL content-addressed chứa SHA.
5. Kết nối custom domain `media.sigmastudy.net`.
6. Thiết lập cache immutable cho URL có SHA.
7. Tạo mapping từ HKA node/Asset ID sang delivery URL.
8. Tích hợp preview trước.
9. Chỉ chạm production sau lệnh phê duyệt riêng.

Production hiện giữ HOLD.

---

# XXII. NGUYÊN TẮC KHÔNG ĐƯỢC VI PHẠM

1. Không sản xuất từ branch “latest” mà thiếu commit SHA.
2. Không sửa prompt trong cửa sổ sản xuất.
3. Không trộn nhiều Prompt Commit SHA trong cùng batch.
4. Không upload canonical package trước QA APPROVED.
5. Không ghi đè asset đã release.
6. Không dùng ETag thay cho SHA-256 registry.
7. Không commit hàng loạt ảnh 4K vào Git.
8. Không dùng một chat window sản xuất nhiều batch song song.
9. Không để website đọc prefix chưa có `RELEASED.json`.
10. Không đưa CLEAN MASTER vào public delivery.
11. Không để mô hình tự vẽ lại Logo Sigma hoặc tự sinh MOTTO.
12. Không thay đổi production khi trạng thái vẫn HOLD.

---

# XXIII. DEFINITION OF DONE

Một batch chỉ hoàn thành khi đồng thời đạt:

```text
PROMPT COMMIT SHA VERIFIED
MANIFEST SHA256 VERIFIED
100% ASSET IDS PRODUCED
100% CLEAN MASTERS PRESENT
100% BRANDED FINALS PRESENT
100% SHA256 VERIFIED
SELF QA PASSED
INDEPENDENT QA APPROVED
R2 OBJECT COUNT VERIFIED
R2 OBJECT CHECKSUMS VERIFIED
UPLOAD RECEIPT WRITTEN
RELEASED.json WRITTEN LAST
RELEASE PREFIX LOCKED
GITHUB RELEASE INDEX UPDATED
```

Một Knowledge Tree chỉ hoàn thành về hình ảnh khi:

- toàn bộ batch đã RELEASED;
- tổng Asset ID khớp gói P12/P18/P24/P30/P36;
- 100% cành cấp 1 được bao phủ;
- không có batch đang BLOCKED hoặc REJECTED;
- window-level release index đã được kiểm định;
- chưa tự động đồng nghĩa với website PUBLISHED.

---

# XXIV. TUYÊN BỐ CHỐT

> **GitHub nói phải làm gì.**  
> **Batch xác định làm bao nhiêu.**  
> **Production tạo đúng từng Asset ID.**  
> **QA quyết định có đạt hay không.**  
> **Cloudflare R2 giữ bản đã được chứng minh.**  
> **Website chỉ xuất bản release đã được cho phép.**

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```
