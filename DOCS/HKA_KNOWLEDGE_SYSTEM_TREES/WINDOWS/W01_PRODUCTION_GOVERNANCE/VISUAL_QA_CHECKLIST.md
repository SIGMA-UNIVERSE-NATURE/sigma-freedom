---
title: "HKA W01 — Visual QA Checklist"
window_id: "W01"
version: "1.0"
status: "REFERENCE CHECKLIST"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — VISUAL QA CHECKLIST

Dùng checklist này cho từng Asset ID ở độ phân giải đầy đủ. Mọi mục phải là `PASS`, `FAIL` hoặc `BLOCKED`; không dùng “gần đạt”. QA độc lập không sửa hình.

## A. Identity & package

```text
[ ] Asset ID khớp manifest
[ ] Batch ID và Run ID khớp
[ ] CLEAN MASTER filename đúng
[ ] BRANDED FINAL filename đúng
[ ] Có đúng 2 file hình cho Asset ID
[ ] Không có file ngoài manifest
[ ] PNG mở được, không hỏng
[ ] Kích thước pixel đúng
[ ] SHA-256 khớp registry
```

## B. Academic truth

```text
[ ] Hiện tượng/cấu trúc/quá trình đúng prompt
[ ] Vật thể bắt buộc đều có
[ ] Vật thể bị cấm đều không có
[ ] Quan hệ không gian đúng
[ ] Trình tự quá trình đúng
[ ] Tỷ lệ thật hoặc có disclosure mô hình
[ ] Reality/model/reconstruction/metaphor được phân biệt
[ ] Không biến giả thuyết thành sự thật
[ ] Không có chi tiết giả khoa học hoặc anachronism
```

## C. Pedagogy

```text
[ ] Một learning objective chính đọc được từ hình
[ ] Phù hợp audience A1–A5/Research
[ ] Không đồng nhất tuổi với độ sâu
[ ] Focal point là nội dung học tập
[ ] Cognitive load trong giới hạn
[ ] Hình hỗ trợ quan sát/so sánh/cơ chế/liên kết
[ ] Không củng cố misconception
[ ] Không áp đặt đáp án đạo đức nếu asset là tình huống suy xét
```

## D. CINEMATIC 4K

```text
[ ] Bố cục có reading order rõ
[ ] Camera/lens không làm sai tỷ lệ
[ ] Ánh sáng làm rõ nội dung
[ ] Vật liệu và bóng đổ hợp lý
[ ] Không có lỗi tay, mắt, chân, cạnh hoặc vật thể
[ ] Depth of field không xóa chi tiết cần học
[ ] Không clutter hoặc hiệu ứng điện ảnh vô nghĩa
[ ] Có vùng trống đúng cho web/brand
```

## E. Companion consistency

```text
[ ] Dùng đúng PNG master theo immutable commit
[ ] Màu, hình dáng, tỷ lệ và đặc điểm cốt lõi đúng
[ ] Không trộn hoặc nhân đôi nhân vật
[ ] Primary Companion đúng manifest
[ ] Secondary Companion đúng manifest
[ ] Hành động đúng chức năng học thuật
[ ] Gaze hướng đúng đối tượng
[ ] Placement mode đúng
[ ] Nhân vật không che hiện tượng
[ ] Nhân vật không bị trình bày như phần thật của vi mô/lịch sử
```

## F. Logo & MOTTO

CLEAN MASTER:

```text
[ ] Không có Logo Sigma
[ ] Không có MOTTO
[ ] Không có text/logo model-generated
[ ] Có brand-safe area
```

BRANDED FINAL:

```text
[ ] Logo lấy từ assets/logo/sigma-logo-master.jpg hoặc compact emblem khi được phép
[ ] Logo giữ đúng tỷ lệ, không crop/kéo méo/đổi màu
[ ] MOTTO chính xác từng ký tự:
    PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
[ ] Logo và MOTTO không che nội dung
[ ] Tương phản đủ
[ ] Không có logo/MOTTO thứ hai do model sinh
```

Sai source logo hoặc sai một ký tự MOTTO là P0.

## G. Accessibility & representation

```text
[ ] Nghĩa không phụ thuộc chỉ vào màu
[ ] Contrast đủ để nhận biết thành phần chính
[ ] Alt text khớp hình và mục tiêu
[ ] Không stereotype văn hóa/giới/khuyết tật
[ ] Nội dung nhạy cảm phù hợp audience
[ ] Không gore/sensationalism không cần thiết
[ ] Poster có vùng chữ đủ lớn và hierarchy rõ
```

## H. Asset-specific checks

### 0001

```text
[ ] Đủ bốn Companion
[ ] Sáu cành đồng cấp
[ ] Không có thang/hierarchy
[ ] Đọc rõ đây là conceptual model
```

### 0002

```text
[ ] Một giọt nước chính trên lá
[ ] Sigma nhìn đúng giọt
[ ] Không phân tử/lực/tia sáng giả
```

### 0003

```text
[ ] Đúng 12 vật: 4 lá + 4 đá + 4 quả hạt
[ ] Ba khay phân biệt bằng hình và màu
[ ] Không vật nhỏ nguy cơ nuốt
```

### 0004

```text
[ ] Hoa–ong–ánh sáng–đất/rễ đều rõ
[ ] Cutaway có border
[ ] Không tia năng lượng hoặc nhân quả một chiều giả
```

### 0005

```text
[ ] Có dấu chân, cỏ cong và lông rời
[ ] Không thấy/định danh con vật
[ ] Owl không che dấu
```

### 0006

```text
[ ] Ba panel tách biệt
[ ] Không ngụ ý cùng độ phóng đại
[ ] Có ba vùng scale bar trống
[ ] Vi khuẩn không có nhân/organelles giả
```

### 0007

```text
[ ] Evidence và reconstruction tách rõ
[ ] Phần không chắc được ghosted
[ ] Không gán culture/date không có nguồn
```

### 0008

```text
[ ] Ba con lắc cùng bob/góc/hệ đo
[ ] Chỉ chiều dài khác
[ ] Little Ant ngoài quỹ đạo
```

### 0009

```text
[ ] Trạng thái–sensor–controller–actuator–kết quả rõ
[ ] Có thể hậu kỳ vòng phản hồi
[ ] Không fake UI/arrows/text
```

### 0010

```text
[ ] Ba phương pháp thực địa riêng biệt
[ ] Một câu hỏi chung
[ ] Không ngụ ý phục hồi đã thành công
[ ] Phỏng vấn tôn trọng và có khoảng cách phù hợp
```

### 0011

```text
[ ] Năm panel
[ ] Sample identity nhất quán không chỉ bằng màu
[ ] Có ít nhất ba phép đo lặp
[ ] Panel dữ liệu/code trống
[ ] Owl không là con dấu chân lý
```

### 0012

```text
[ ] 2160×3840, 9:16
[ ] Sáu vùng poster rõ
[ ] Không chữ, data point, graph, equation hoặc citation giả
[ ] Có vùng uncertainty và source
```

## I. Severity decision

```text
P0: sai SHA/source/batch/brand; deploy trái phép; brand giả
P1: sai kiến thức/cơ chế/tỷ lệ/lịch sử/giải phẫu; thiếu thành phần bắt buộc
P2: bố cục/ánh sáng/pose/độ rõ/brand placement chưa đạt
P3: metadata/caption/alt text/filename/report
```

## J. Overall result

```text
ASSET ID:
GATE A — ACADEMIC:
GATE B — PEDAGOGY:
GATE C — VISUAL:
GATE D — CHARACTER & BRAND:
GATE E — ACCESSIBILITY:
GATE F — INTEGRITY:
P0:
P1:
P2:
P3:
ERROR CLASS: OUTPUT_ERROR / PROMPT_ERROR / METADATA_ERROR / SYSTEMIC_ERROR
STATUS: PASS / FAIL / BLOCKED
REQUIRED ACTION:
```

Batch chỉ `QA_APPROVED` khi 100% asset PASS và mọi lỗi unresolved bằng 0.