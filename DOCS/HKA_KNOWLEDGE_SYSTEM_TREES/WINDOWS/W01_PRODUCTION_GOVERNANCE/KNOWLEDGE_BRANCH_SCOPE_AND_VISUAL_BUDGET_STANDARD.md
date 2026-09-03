---
title: "HKA Knowledge Branch Scope & Visual Budget Standard"
version: "1.0"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA KNOWLEDGE BRANCH SCOPE & VISUAL BUDGET STANDARD

## 1. Mục tiêu

Chuẩn này ngăn hai lỗi hệ thống khi W02–W64 phát triển Knowledge System Trees:

1. **UNDER-DEVELOPMENT** — viết quá ngắn, bỏ mất knowledge functions, prerequisite, evidence, misconception hoặc D1–D4.
2. **OVER-DEVELOPMENT** — viết quá dài, lặp claim/node, tách trivia thành quá nhiều node và kéo theo visual assets trùng nhau.

Không dùng số từ đơn thuần để định nghĩa chất lượng. Số từ chỉ là tín hiệu review; đơn vị thật là **knowledge function** và **visual learning job**.

---

## 2. Branch Coverage Record — bắt buộc cho mỗi mandatory branch

Mỗi cành bắt buộc phải chứng minh đủ các thành phần sau trước khi được đánh `BRANCH_COMPLETE`:

```text
BRANCH ID / PATH
CENTRAL QUESTION
WHY IT BELONGS IN THIS TREE
CORE KNOWLEDGE FUNCTIONS
CORE NODES
PREREQUISITE ENTRY POINTS
DOMAIN METHODS / EVIDENCE
FOUNDATIONAL EXAMPLES
COUNTEREXAMPLES OR BOUNDARY CASES
HIGH-RISK MISCONCEPTIONS
UNCERTAINTY / LIMITS
CONTROVERSIES / OPEN QUESTIONS WHEN APPLICABLE
MODERN / EMERGING EXTENSIONS WHEN APPLICABLE
CROSS-TREE RELATIONS
D1 → D4 PROGRESSION
SOURCE COVERAGE
VISUAL IMPLICATIONS
```

Thiếu một mục material phải ghi `NOT APPLICABLE — reason`; không được bỏ trống.

---

## 3. Content envelope cho một core node

Một core node phải có **một primary knowledge function**. Node không phải chương sách và cũng không phải trivia card.

Recommended authoring envelope, không tính bảng nguồn/prompt/metadata:

```text
250–1200 prose words per core node: NORMAL
<200 words: DIRECTOR SHORT-CONTENT REVIEW TRIGGER
>1500 words: DIRECTOR SPLIT/COMPRESSION REVIEW TRIGGER
```

Đây không phải hard word-count law. Director có thể chấp nhận ngoại lệ nếu cấu trúc ngành yêu cầu, nhưng phải ghi lý do.

### Node quá ngắn khi

- chỉ có định nghĩa mà thiếu cơ chế/quan hệ hoặc evidence cần thiết;
- không có prerequisite;
- không có example/boundary case khi cần;
- D1–D4 chỉ là tiêu đề;
- không đủ thông tin để xác định claim nào cần source;
- người đọc phải hỏi tác giả để hiểu node nằm ở đâu trong progression.

### Node quá dài khi

- có hơn một primary knowledge function độc lập;
- chứa nhiều câu hỏi trung tâm không phụ thuộc nhau;
- có thể tách thành hai node mà không làm mất meaning;
- lặp cùng claim/evidence ở nhiều section;
- phần giải thích dài không tạo thêm prerequisite, mechanism, evidence, boundary, uncertainty hoặc application mới.

Action:

```text
TOO SHORT → EXPAND MISSING KNOWLEDGE FUNCTION
TOO LONG → COMPRESS OR SPLIT BY KNOWLEDGE FUNCTION
```

Không tách node chỉ để đạt số lượng.

---

## 4. Branch fan-out control

Một mandatory level-1 branch phải đủ sâu để trở thành chương trình thật, nhưng không được biến thành flat list.

Director review trigger:

```text
<3 substantive core nodes under a broad mandatory branch
→ possible UNDER-DEVELOPMENT

>12 direct core nodes without sub-grouping
→ possible FLAT OVER-DEVELOPMENT
```

Nếu >12 direct core nodes, Window phải kiểm tra khả năng nhóm thành coherent sub-branches trước khi tiếp tục. Ngoại lệ được phép cho taxonomy tự nhiên của ngành nhưng phải giải trình.

Không dùng fan-out trigger như quota. Mục tiêu là hierarchy có nghĩa.

---

## 5. Compression test và Expansion test

### Compression test

Với mỗi section/node, hỏi:

> Nếu xóa đoạn này, chương trình có mất một claim, mechanism, prerequisite, evidence, boundary, misconception, uncertainty, method hoặc application duy nhất không?

Nếu `NO`, đoạn đó là ứng viên merge/compress.

### Expansion test

Với mỗi mandatory branch, hỏi:

> Một learner hoặc reviewer có thể lần từ central question đến core concepts, mechanism/evidence, misconceptions, D1–D4 và sources mà không phải hỏi thêm tác giả không?

Nếu `NO`, branch còn thiếu.

Branch chỉ PASS khi qua cả hai test.

---

## 6. Visual budget không tỷ lệ với số chữ

Quy tắc cứng:

```text
MORE TEXT ≠ MORE IMAGES
MORE NODES ≠ MORE IMAGES
ONE NODE ≠ AUTOMATIC IMAGE
```

Một image asset chỉ tồn tại nếu có **unique visual learning job**.

Unique visual learning job là một việc mà hình phải giúp người học nhìn/so sánh/theo dõi/định vị mà asset đã có chưa làm được.

Ví dụ hợp lệ:

- spatial structure;
- process/mechanism order;
- scale relationship;
- evidence versus inference;
- before/after comparison;
- system feedback;
- reconstruction with uncertainty;
- cross-link that requires simultaneous visual relation;
- misconception that is best corrected visually.

Không hợp lệ:

- cùng scene đổi tuổi;
- cùng mechanism đổi góc camera;
- cùng claim đổi Companion;
- cùng nội dung chỉ thay màu/phong cách;
- tạo ảnh vì mỗi node “nên có một ảnh”.

---

## 7. VCU admission thresholds

Giữ scoring hiện hành:

```text
Centrality            0–3
Visualization Need    0–3
Misconception Risk    0–2
Cross-link Value      0–2
TOTAL                 0–10
```

Director default decision:

```text
8–10 → STRONG VISUAL CANDIDATE
6–7  → DIRECTOR JUDGMENT; must prove image adds learning value
0–5  → DEFAULT NO NEW ASSET; use text/table/diagram/post-production layer unless exceptional
```

Score không tự động tạo asset. Deduplication gate vẫn bắt buộc.

---

## 8. VCU → Asset control

```text
DEFAULT: 1 primary asset per VCU
SECOND ASSET: allowed only with a distinct learning objective + distinct visual job
MAXIMUM: 2 level-1 branches per VCU
MAXIMUM: 6 node IDs per asset
ONE primary learning objective per asset
```

Một VCU có thể không tạo asset nếu một asset khác đã phục vụ đúng visual job.

Nếu cùng concept quay lại ở A1–A5/D1–D4, asset mới chỉ được phép khi **epistemic/learning delta** thực sự tăng, ví dụ:

```text
D1 observe → D2 compare/explain → D3 model/test → D4 critique/synthesize
```

Không tạo asset mới chỉ vì đổi age label.

---

## 9. Package cap là budget, không phải mục tiêu phải lấp đầy

Các package canonical:

```text
P12 / P18 / P24 / P30 / P36
```

Window chọn **package nhỏ nhất đủ bao phủ các unique visual jobs đã PASS**.

Không được chọn P36 rồi tìm cách tạo đủ 36 ảnh.

Nếu unique visual jobs vượt khả năng P36 mà không thể merge an toàn:

```text
STOP VISUAL LOCK
→ Director scope review
→ Architect decides scope split / future window / non-image medium
```

Không nhồi nhiều learning objectives vào một asset và cũng không tự vượt P36.

---

## 10. Canonical image-count containment

Với W02–W64, mỗi Window bị chặn bởi package tối đa P36. Do đó canonical Asset IDs không được tăng vô hạn theo độ dài curriculum.

Reruns, rejected candidates và web derivatives là các đối tượng khác; chúng không được tính như canonical learning Asset IDs mới.

Director phải theo dõi riêng:

```text
CANONICAL ASSET COUNT
PRODUCTION RUN COUNT
REJECTED RUN COUNT
WEB DERIVATIVE COUNT
```

Không dùng production attempts để phóng đại curriculum asset count.

---

## 11. Director stop conditions

Director trả `RETURN` trước prompt lock nếu:

- mandatory branch bị under-developed;
- node catalog chứa trivia fragmentation;
- cùng claim xuất hiện như nhiều node không cần thiết;
- VCU tồn tại chỉ để lấp package;
- asset candidate trùng visual job;
- spiral asset không có learning delta;
- package lớn hơn nhu cầu thực;
- content length đang che giấu thiếu structure hoặc redundancy.

---

## 12. Final principle

```text
COMPLETE KNOWLEDGE, MINIMUM REDUNDANCY.
ENOUGH VISUALS TO TEACH, NO VISUALS TO FILL SPACE.
```

Mục tiêu là chương trình đủ sâu để đúng học thuật nhưng visual package đủ gọn để production giữ chất lượng và toàn HKA có thể mở rộng mà không sinh hàng nghìn ảnh trùng nhau.