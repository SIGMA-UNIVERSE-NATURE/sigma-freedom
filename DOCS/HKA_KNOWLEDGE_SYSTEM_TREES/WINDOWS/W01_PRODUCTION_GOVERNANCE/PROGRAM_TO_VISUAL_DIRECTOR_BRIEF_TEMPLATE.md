---
title: "HKA Program-to-Visual Director Brief Template"
version: "1.1"
status: "PROPOSED REFERENCE TEMPLATE"
---

# PROGRAM-TO-VISUAL DIRECTOR BRIEF

Tài liệu này nối toàn bộ curriculum với visual package. Nó không thay prompt record.

## 1. Program lock

```text
WINDOW ID:
TREE ID:
ACADEMIC CONTENT COMMIT SHA:
TREE PATH:
NODE CATALOG PATH:
RELATION CATALOG PATH:
SOURCE REGISTER PATH:
DIRECTOR ACADEMIC REVIEW STATUS:
BRANCH SCOPE / VISUAL BUDGET STANDARD VERIFIED: YES/NO
```

## 2. Visual thesis

Viết 1–3 đoạn: chương trình này cần được “nhìn” như thế nào để người học hiểu cấu trúc tri thức, không phải chỉ để đẹp.

## 3. Visual learning arc

| Sequence | Node/Concept | Learner state before | Visual job | Learner state after |
|---|---|---|---|---|

## 4. Spiral visuals

Xác định concept nào quay lại ở A1–A5/D1–D4 với độ sâu tăng dần. Không lặp cùng một ảnh chỉ đổi độ tuổi.

Mỗi spiral successor phải ghi một `LEARNING / EPISTEMIC DELTA` quan sát được. Nếu không có delta, ưu tiên reuse/derivative thay vì Asset ID mới.

## 5. Continuity locks

```text
RECURRING ENVIRONMENTS:
RECURRING OBJECT MOTIFS:
SCALE CONVENTIONS:
MODEL/REALITY DISCLOSURE CONVENTIONS:
CHARACTER ROLE CONTINUITY:
COLOR / SHAPE LOGIC:
```

## 6. VCU map

| VCU ID | Node IDs | One learning objective | Unique visual job | Why image | Score /10 | Candidate asset type |
|---|---|---|---|---|---:|---|

Một VCU không được dùng để che lỗ hổng curriculum.

Default:

```text
8–10 = strong visual candidate
6–7  = Director judgment
0–5  = default no new canonical asset
```

Score không tự động cấp Asset ID. Deduplication gate vẫn bắt buộc.

## 7. Visual candidate deduplication

Trước khi cấp Asset ID, hoàn thành:

```text
VISUAL_DEDUPLICATION_REGISTER.md
```

Tóm tắt:

```text
CANDIDATE VISUAL JOBS:
MERGED CANDIDATES:
REUSED EXISTING ASSETS:
DERIVATIVE-ONLY CASES:
REJECTED DUPLICATES:
ADMITTED NEW ASSETS:
FINAL DUPLICATE COUNT: 0
```

## 8. Package decision

```text
SELECTED PACKAGE:
LOCKED ASSET COUNT:
UNUSED PACKAGE CAPACITY:
RATIONALE:
WHY THIS IS THE SMALLEST SUFFICIENT PACKAGE:
WHAT IS NOT VISUALIZED AND WHY:
```

Không chọn package lớn rồi tạo hình để lấp capacity.

Nếu nhu cầu visual thực sự vượt P36, dừng và đưa Director/Architect scope decision; không tự vượt package và không nhồi nhiều learning objectives vào một ảnh.

## 9. Asset sequence

| Asset ID | VCU | Audience | Depth | Companion | Unique visual job | Role in whole program | Prior visual | Next visual |
|---|---|---|---|---|---|---|---|---|

## 10. Production consistency

Ghi các khóa phải được chuyển cho mọi IMG Unit:

- character identity;
- recurring environment/object continuity;
- representation conventions;
- camera/scale conventions khi cần;
- global forbidden patterns;
- Director global correction locks.

## 11. Director approval

```text
PROGRAM COVERAGE VERIFIED: YES/NO
COMPRESSION TEST: PASS/FAIL
EXPANSION TEST: PASS/FAIL
VISUALS TRACE TO NODES: YES/NO
UNIQUE VISUAL JOB PER ASSET: YES/NO
FINAL DUPLICATE COUNT: 0 / <count>
NO DECORATIVE-ONLY ASSET: YES/NO
SPIRAL/CONTINUITY REVIEWED: YES/NO
PACKAGE IS SMALLEST SUFFICIENT: YES/NO
READY FOR PROMPT LOCK: YES/NO
DIRECTOR SIGN-OFF:
```