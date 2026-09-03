---
title: "HKA — QA Acceptance Matrix"
version: "1.0"
status: "REFERENCE STANDARD"
language: "vi"
date: "2026-09-03"
---

# HKA QA ACCEPTANCE MATRIX

QA kiểm 100% Asset IDs ở full resolution. `PASS` chỉ được cấp khi có bằng chứng quan sát được. `BLOCKED` dùng khi thiếu nguồn hoặc hồ sơ khiến không thể kết luận. QA không sửa output và không viết lại prompt.

## 1. Kết quả và severity

```text
PASS     Đạt tiêu chí.
FAIL     Có bằng chứng không đạt; cần sửa output hoặc prompt.
BLOCKED  Không đủ dữ kiện/quyền/hồ sơ để kết luận an toàn.
```

```text
P0 CRITICAL  Sai nguồn/SHA/batch, brand giả, vi phạm an toàn, deploy trái phép.
P1 MAJOR     Sai kiến thức, cơ chế, tỷ lệ, lịch sử, giải phẫu, thông điệp giảng dạy.
P2 MODERATE  Bố cục, ánh sáng, độ rõ, character pose hoặc brand placement chưa đạt.
P3 MINOR     Metadata, caption, alt text, filename hoặc report.
```

Release yêu cầu mọi lỗi unresolved bằng 0.

---

# GATE A — ACADEMIC

| ID | Kiểm tra | Bằng chứng | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|---|
| A01 | Hiện tượng đúng | Prompt truth locks + source + ảnh | Các thành phần và quan hệ khớp nguồn | Hiện tượng sai hoặc bịa — P1 | Xác định prompt hay output; prompt sai → commit mới, output sai → run mới |
| A02 | Cơ chế đúng | Process/mechanism specification | Trình tự và quan hệ nhân quả đúng | Đảo trình tự, nhân quả giả — P1 | Tái sản xuất hoặc sửa prompt |
| A03 | Tỷ lệ đúng | Scale locks + visual cues | Tỷ lệ thật hoặc mô hình được disclosure | Scale gây hiểu sai — P1 | Run mới; prompt mới nếu thiếu lock |
| A04 | Phân loại biểu diễn | Representation type + caption | Reality/model/reconstruction/metaphor phân biệt rõ | Mô hình được trình bày như ảnh thật — P1 | Sửa prompt/caption và tái QA |
| A05 | Bối cảnh lịch sử/văn hóa | Sources + reconstruction locks | Không anachronism/stereotype | Sai thời kỳ, vật thể, trang phục — P1 | Prompt/output review |
| A06 | Mức chắc chắn | Certainty field + caption | Không nâng giả thuyết thành sự thật | Phóng đại độ chắc chắn — P1 | Prompt commit mới nếu claim sai |
| A07 | Nguồn kiểm chứng | Source register | Nguồn đủ thẩm quyền và đúng claim | Thiếu nguồn cho claim trọng yếu — BLOCKED/P1 | Trả Prompt Window |
| A08 | Không pseudoscience | Image + prompt | Không có cấu trúc/khẳng định giả khoa học | Pseudoscience — P0/P1 | Dừng batch khi có tính hệ thống |

Gate A FAIL nếu bất kỳ A01–A08 fail.

---

# GATE B — PEDAGOGY

| ID | Kiểm tra | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|
| B01 | Một mục tiêu chính | Người xem biết phải chú ý điều gì | Nhiều mục tiêu cạnh tranh — P2/P1 | Giảm tải hoặc tách asset |
| B02 | Phù hợp audience | Ngôn ngữ hình ảnh và độ dày phù hợp | Quá tải hoặc quá đơn giản gây sai — P2 | Run/prompt revision |
| B03 | D1–D4 đúng năng lực | Nhiệm vụ phản ánh depth, không tuổi | Depth bị dùng như cấp tuổi — P2 | Sửa metadata/prompt |
| B04 | Nhìn thấy quan hệ | Bố cục làm rõ process/comparison/link | Quan hệ chỉ tồn tại trong caption — P2 | Tái bố cục |
| B05 | Chống ngộ nhận | Hình không củng cố misconception | Hình tạo/duy trì hiểu sai — P1 | Fail asset |
| B06 | Không chỉ trang trí | Mỗi yếu tố chính phục vụ mục tiêu | Cinematic spectacle lấn át kiến thức — P2 | Tái sản xuất |
| B07 | Câu hỏi mở không áp đặt | Ethical/philosophical scene cho nhiều dữ kiện | Hình định sẵn “đáp án đạo đức” — P1/P2 | Prompt revision |
| B08 | Chuyển giao học tập | Có cue để giải thích hoặc quan sát lại | Chỉ tạo cảm xúc, không tạo hiểu biết — P2 | Prompt/output revision |

---

# GATE C — VISUAL

| ID | Kiểm tra | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|
| C01 | Độ phân giải | 3840×2160 hoặc poster 2160×3840 đúng contract | Sai kích thước — P2 | Re-export/run |
| C02 | Focal hierarchy | Focal point và reading order rõ | Mắt không biết nhìn đâu — P2 | Tái bố cục |
| C03 | Camera/lens logic | Góc nhìn không bóp méo nội dung | Lens gây scale/shape sai — P1/P2 | Run mới |
| C04 | Lighting logic | Ánh sáng làm rõ cấu trúc | Che chi tiết hoặc tạo vật lý sai — P1/P2 | Run mới |
| C05 | Không artifact | Tay/mắt/vật thể/cạnh không méo | Artifact đáng kể — P2; sai anatomy — P1 | Run mới |
| C06 | Vùng brand | Safe area đủ, không che nội dung | Không thể ghép brand an toàn — P2 | Tái crop/run |
| C07 | Không text rác | Không chữ/công thức/logo tự sinh | Chữ ngẫu nhiên — P2; brand giả — P0 | Từ chối |
| C08 | Màu có chức năng | Nghĩa không phụ thuộc chỉ vào màu | Người mù màu mất thông tin — P2 | Bổ sung shape/pattern |
| C09 | Mức chi tiết | Đủ để dạy, không clutter | Clutter/chi tiết giả — P2/P1 | Run mới |

---

# GATE D — CHARACTER & BRAND

| ID | Kiểm tra | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|
| D01 | Repo và commit | Khớp immutable source lock | Sai source/commit — P0 | Dừng batch |
| D02 | Nhân vật khớp master | Hình dạng, màu, tỷ lệ cốt lõi đúng | Tái thiết kế/trộn nhân vật — P0/P1 | Run mới; điều tra pipeline |
| D03 | Vai học thuật đúng | Hành vi phù hợp Sigma/Cricket/Ant/Owl | Chỉ trang trí hoặc sai chức năng — P2 | Tái bố cục/prompt |
| D04 | Placement mode đúng | Nhân vật không bị hiểu là phần thật của vi mô/lịch sử | Mascot nằm trong cơ quan/nguyên tử như thực — P1 | Run/prompt revision |
| D05 | HERO ensemble | HERO có đủ bốn | Thiếu nhân vật — P1 | Run mới |
| D06 | Logo chính thức | Ghép hậu kỳ từ master, không méo/crop | Logo model-generated/sai — P0 | Từ chối branded final |
| D07 | MOTTO chính xác | `PEACEFUL MIND-KINDLY HEART-KEEP GROWING.` | Sai một ký tự — P0 | Từ chối branded final |
| D08 | Clean vs branded | Clean không brand; branded có đúng brand | Thiếu một variant — P1 integrity | Hoàn thiện package |

---

# GATE E — ACCESSIBILITY & RESPONSIBLE REPRESENTATION

| ID | Kiểm tra | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|
| E01 | Alt text | Mô tả mục tiêu và quan hệ, không chỉ màu sắc | Thiếu/sai — P3/P1 | Sửa metadata |
| E02 | Contrast | Thành phần chính phân biệt được | Contrast thấp — P2 | Hậu kỳ/tái xuất |
| E03 | Color independence | Có shape, position, pattern hoặc label hậu kỳ | Chỉ dùng đỏ/xanh — P2 | Sửa visual |
| E04 | Inclusive representation | Không stereotype, tokenism hoặc kỳ thị | Stereotype — P1/P0 | Prompt/output revision |
| E05 | Age sensitivity | Không gây sốc không cần thiết | Gore/sensationalism — P1/P0 | Từ chối |
| E06 | Cultural specificity | Chi tiết cụ thể có nguồn hoặc được trung tính hóa | “Phổ quát” giả nhưng thiên lệch — P1/P2 | Sửa prompt |
| E07 | Poster legibility | Có hierarchy/vùng chữ đủ | Panel quá nhỏ, không thể đọc — P2 | Tái bố cục |

---

# GATE F — INTEGRITY & TRACEABILITY

| ID | Kiểm tra | PASS | FAIL / Severity | Hành động |
|---|---|---|---|---|
| F01 | Asset ID | Khớp manifest và filename | Nhầm ID — P0 | Dừng batch |
| F02 | Count | N clean + N branded, không dư | Thiếu/dư file — P1 | Sửa package |
| F03 | Filename | Regex và ID đúng | Sai tên — P3/P1 | Rename + rehash |
| F04 | SHA-256 | Mọi hash khớp byte | Không khớp — P0 | Dừng, điều tra |
| F05 | Prompt commit | Full SHA tồn tại và đúng | Trỏ sai commit — P0 | Dừng batch |
| F06 | Manifest | Schema valid và hash đúng | Invalid/tampered — P0 | Trả Prompt Window |
| F07 | Batch isolation | Một batch, một prompt commit | Trộn commit/window — P0 | Dừng |
| F08 | Package | ZIP hash, file list và reports đúng | Package không tái lập — P0/P1 | Đóng gói lại |
| F09 | No undeclared assets | Không file ngoài manifest | Dư file không khai báo — P1 | Loại và rehash |
| F10 | State | Chuyển trạng thái có bằng chứng | Nhảy state — P0 | Hủy authorization |

---

# 2. Quyết định output lỗi hay prompt lỗi

QA phải phân loại:

```text
OUTPUT_ERROR
Prompt đủ và đúng; hình không tuân thủ.
→ Giữ Prompt Commit SHA.
→ Tăng Run ID.

PROMPT_ERROR
Prompt thiếu/sai/mâu thuẫn khiến output đúng theo prompt vẫn sai.
→ QA_BLOCKED hoặc QA_REJECTED.
→ Prompt Window sửa.
→ Prompt Commit SHA mới.

METADATA_ERROR
Hình đạt, metadata không đạt.
→ Sửa metadata, tính hash mới nếu package byte thay đổi.

SYSTEMIC_ERROR
Lỗi có thể ảnh hưởng nhiều asset/batch.
→ P0/P1; pause các batch liên quan.
```

## 3. QA report tối thiểu mỗi asset

```text
ASSET ID:
CLEAN SHA-256:
BRANDED SHA-256:
GATE A:
GATE B:
GATE C:
GATE D:
GATE E:
GATE F:
ISSUES:
SEVERITY:
ERROR CLASS:
REQUIRED ACTION:
STATUS: PASS / FAIL / BLOCKED
```

## 4. Overall approval

```text
QA_APPROVED chỉ khi:
- 100% assets reviewed
- all asset statuses PASS
- all gates PASS
- P0=P1=P2=P3 unresolved=0
- counts and SHA verified
```

Không dùng điểm trung bình để bù một lỗi nghiêm trọng.