---
title: "HKA CINEMATIC 4K — Official Brand Asset Lock"
project: "Human Knowledge Academic"
version: "1.0"
status: "MANDATORY / IMMUTABLE REFERENCE"
language: "vi"
date: "2026-09-03"
---

# HKA CINEMATIC 4K — OFFICIAL BRAND ASSET LOCK 1.0

Tài liệu này khóa nguồn tham chiếu chính thức cho bốn nhân vật HKA, Logo Sigma và MOTTO. Nó phải được đọc cùng:

```text
DOCS/HKA_CINEMATIC_4K_PRODUCTION_STANDARD.md
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md
```

## 1. Nguồn tài sản bất biến

```text
Repository: linkcomltd-byte/sigma-universe-web
Visibility: private
Candidate branch: sigmastudy/academic-mainline-20260901-v0-1
Immutable commit: 2d3aa9d8418acccd39a3d263e917d4157e029e17
Production status: HOLD — không được tác động production từ quy trình HKA Knowledge Trees
```

Mọi cửa sổ và đội sản xuất phải khóa tài sản theo **commit SHA**, không theo branch mutable. Tên branch chỉ dùng để truy vết preview.

## 2. Master nhân vật chính thức

| Nhân vật | Master path | Git blob SHA | Vai trò học thuật |
|---|---|---|---|
| Sigma | `assets/characters/sigma.png` | `72e29ad1ba8e71a25f7fc7d4da656a6196fdf6db` | Định hướng bằng câu hỏi |
| Cricket | `assets/characters/cricket.png` | `87e30fe00beb0a122fefde8126c54d98ae7c0e08` | Phát hiện và mở rộng kết nối |
| Little Ant | `assets/characters/little-ant.png` | `a931ae833d184ecb48f1b20bc90a8cbeee181d8c` | Chia nhỏ nhiệm vụ, luyện tập và kiên trì |
| Professor Owl | `assets/characters/professor-owl.png` | `b5c58c5502ee39aff941769fa143f071384c3472` | Kiểm tra nguồn, bằng chứng, giới hạn và điều chưa biết |

Các tệp PNG trên là tài sản tham chiếu master cho nhận diện nhân vật. Không được tự phát minh, tái thiết kế hoặc thay thế bằng nhân vật gần giống.

## 3. Derivative chính thức tối ưu cho website

| Nhân vật | Website derivative path | Git blob SHA |
|---|---|---|
| Sigma | `assets/characters/official/sigma.webp` | `e653c331bd0083b86ae0bd5ee391f6717ad26dec` |
| Cricket | `assets/characters/official/cricket.webp` | `bfdea9c01959fcaf854c274b38b1e987f1427b33` |
| Little Ant | `assets/characters/official/little-ant.webp` | `d89f2d728e05ea30d254853541a4c7f045ba8e04` |
| Professor Owl | `assets/characters/official/professor-owl.webp` | `c92f28fb3371e2113ca011a3d3e543353548fd66` |

Các tệp WebP chỉ là derivative phục vụ website. Chúng không thay thế PNG master trong quy trình character-reference và kiểm định nhất quán.

## 4. Logo Sigma chính thức

### Master artwork

```text
Path: assets/logo/sigma-logo-master.jpg
Git blob SHA: 1f19dcbb970ef414fe3a58d406d1b4b55360853e
Native dimensions: 1304 × 1536
SHA-256: f97d39065255bfcc09c46b23616e95165f250dbc13e860a5b80445dbd8dc8c2c
```

Quy tắc bắt buộc:

- Giữ nguyên tỷ lệ gốc.
- Dùng `object-fit: contain` khi triển khai trên website.
- Không crop, kéo giãn, đổi màu, giản lược, vẽ lại hoặc thay thế.
- Không đặt dòng chữ logo trùng lặp ngay cạnh master lockup.

### Compact navigation emblem

```text
Path: assets/logo/sigma-emblem-shell.jpg
Git blob SHA: 91ae7ea19a3e43d0aac13ad0fa42aa4b7a37eb7e
```

Chỉ dùng khi master portrait lockup không thể đọc rõ, ví dụ favicon, navigation hoặc compact lesson control.

## 5. MOTTO khóa chính xác

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Không được:

- đổi `KINDLY HEART` thành một biến thể khác;
- đổi dấu gạch nối;
- bỏ dấu chấm cuối;
- tự dịch trong branded final;
- yêu cầu mô hình tạo ảnh tự sinh MOTTO.

MOTTO phải được ghép bằng typography hậu kỳ đã phê duyệt.

## 6. Quy tắc tham chiếu trong mọi visual prompt

Mỗi Asset ID phải có khối sau:

```text
BRAND ASSET SOURCE REPOSITORY:
linkcomltd-byte/sigma-universe-web

BRAND ASSET SOURCE COMMIT:
2d3aa9d8418acccd39a3d263e917d4157e029e17

PRIMARY COMPANION MASTER PATH:
<one exact PNG master path>

SECONDARY COMPANION MASTER PATHS:
<zero or more exact PNG master paths>

SIGMA LOGO MASTER PATH:
assets/logo/sigma-logo-master.jpg

COMPACT EMBLEM PATH, IF AUTHORIZED:
assets/logo/sigma-emblem-shell.jpg

EXACT MOTTO:
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

## 7. Quy tắc bàn giao cho đội sản xuất

Gói sản xuất phải chứa:

1. Manifest đã khóa với từng Asset ID.
2. Prompt tiếng Việt và tiếng Anh.
3. Danh sách chính xác các master path theo commit.
4. Chỉ dẫn character-placement.
5. Brand-safe area cho Logo và MOTTO.
6. CLEAN MASTER không logo/motto.
7. BRANDED FINAL có logo/motto chính thức.
8. Checklist character consistency và brand integrity.

Đội sản xuất không được nhận một link branch chung rồi tự chọn tài sản. Họ phải nhận **repo + commit + exact path** cho từng nhân vật và logo.

## 8. Điều kiện nghiệm thu

Một hình không đạt nếu:

- nhân vật không khớp tài sản tham chiếu;
- thay đổi hình dáng, màu, trang phục hoặc tỷ lệ cốt lõi mà không có phê duyệt;
- dùng derivative WebP làm căn cứ để tái thiết kế nhân vật;
- logo bị crop, kéo méo, đổi màu hoặc tự vẽ lại;
- MOTTO sai dù chỉ một ký tự;
- thiếu CLEAN MASTER hoặc BRANDED FINAL;
- tài sản được lấy từ commit khác mà manifest không ghi nhận;
- việc sản xuất làm thay đổi hoặc triển khai lên production trong khi production đang HOLD.

## 9. Trạng thái xác minh

```text
REPOSITORY ACCESS: VERIFIED
COMMIT: VERIFIED
CANDIDATE BRANCH HEAD: VERIFIED
FOUR PNG CHARACTER MASTERS: VERIFIED
FOUR OFFICIAL WEBP DERIVATIVES: VERIFIED
SIGMA LOGO MASTER: VERIFIED
SIGMA COMPACT EMBLEM: VERIFIED
PRODUCTION: UNTOUCHED / HOLD PRESERVED
```

---

> **Một nguồn bất biến. Một nhận diện nhất quán. Một gói sản xuất có thể kiểm đếm và kiểm định.**

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```
