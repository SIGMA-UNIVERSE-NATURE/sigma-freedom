---
title: "HKA Program-to-Visual Director Brief Template"
version: "1.3"
status: "ARCHITECT FINALIZED REFERENCE"
---

# PROGRAM-TO-VISUAL DIRECTOR BRIEF

Tài liệu này nối curriculum đã qua Academic QA với visual package. Mục tiêu là **một brief đủ để khóa visual direction mà không tạo thêm registry thủ công không cần thiết**.

## 1. Program lock

```text
WINDOW ID:
WINDOW TYPE:
TREE ID:
ACADEMIC CONTENT COMMIT SHA:
TREE PATH:
NODE CATALOG PATH:
RELATION CATALOG PATH:
SOURCE REGISTER PATH:
ACADEMIC QA REPORT PATH:
ACADEMIC QA RESULT: PASS
DIRECTOR ACADEMIC GATE: PASS
```

Coverage audit có thể nằm trong `ACADEMIC_QA_REPORT.md` hoặc được liên kết tới một matrix/audit riêng khi chương trình lớn.

## 2. Visual thesis

Viết 1–3 đoạn: chương trình này cần được “nhìn” như thế nào để người học hiểu cấu trúc tri thức, không phải chỉ để đẹp.

## 3. Visual learning arc

| Sequence | Node/Concept | Claim IDs | Learner state before | Visual job | Learner state after |
|---|---|---|---|---|---|

## 4. Spiral visuals

Mỗi spiral successor phải có `LEARNING / EPISTEMIC DELTA` quan sát được. Nếu chỉ đổi tuổi, Companion, camera hoặc style mà không đổi cognitive/epistemic job, ưu tiên reuse/derivative thay vì Asset ID mới.

## 5. Continuity locks

```text
RECURRING ENVIRONMENTS:
RECURRING OBJECT MOTIFS:
SCALE CONVENTIONS:
MODEL/REALITY DISCLOSURE CONVENTIONS:
CHARACTER ROLE CONTINUITY:
COLOR / SHAPE LOGIC:
```

## 6. VCU map with academic truth metadata

| VCU ID | Node IDs | Claim IDs | Source IDs | Certainty / Content Class | One learning objective | Unique visual job | Misconception to prevent | Score /10 |
|---|---|---|---|---|---|---|---|---:|

Mỗi VCU/Asset candidate phải mang đủ truth metadata sau. **Mặc định nhúng trực tiếp trong brief này; chỉ tạo file `ACADEMIC_TRUTH_PACK` riêng khi asset phức tạp hoặc nhiều reviewer cần dùng độc lập.**

```text
CLAIM IDS
SOURCE IDS + exact locations/versions
CERTAINTY
CONTENT CLASS
CONTEXT DEPENDENCE, if relevant
NORMATIVE STATUS, if relevant
MODEL STATUS / APPROXIMATION, if relevant
MISCONCEPTION TO PREVENT
WHAT MUST BE SEEN
WHAT MUST NOT BE IMPLIED
REPRESENTATION DISCLOSURE
ACADEMIC TRUTH LOCKS
REQUIRED EXPERT REVIEW + STATUS
ACADEMIC CONTENT COMMIT SHA
```

Một VCU không được dùng để che lỗ hổng curriculum.

## 7. Deduplication — embedded by default

Không bắt buộc tạo một `VISUAL_DEDUPLICATION_REGISTER.md` riêng cho mọi Window. Dùng bảng dưới đây ngay trong brief; file riêng chỉ cần cho chương trình rất lớn hoặc cross-window duplicate review phức tạp.

| Candidate | Nearest existing asset/job | Overlap | Learning delta | Decision: ADMIT / REUSE / MERGE / REJECT |
|---|---|---|---|---|

```text
CANDIDATE VISUAL JOBS:
MERGED / REUSED / REJECTED:
ADMITTED NEW ASSETS:
FINAL DUPLICATE COUNT: 0
```

`GLOBAL_VISUAL_ASSET_LEDGER` là công cụ Director cấp hệ thống khi được triển khai, không phải bước viết bắt buộc của từng Window.

## 8. Package decision

```text
SELECTED PACKAGE:
LOCKED ASSET COUNT:
UNUSED PACKAGE CAPACITY:
RATIONALE:
WHY THIS IS THE SMALLEST SUFFICIENT PACKAGE:
WHAT IS NOT VISUALIZED AND WHY:
```

Không chọn package lớn rồi tạo hình để lấp capacity. Nếu nhu cầu unique visual jobs vượt P36, dừng và đưa Director/Architect scope decision.

## 9. Asset sequence and truth lock

| Asset ID | VCU | Audience | Depth | Companion | Claim IDs | Truth metadata ref | Unique visual job | Prior visual | Next visual |
|---|---|---|---|---|---|---|---|---|---|

For each asset:

```text
WHAT MUST BE SEEN:
WHAT MUST NOT BE IMPLIED:
REPRESENTATION DISCLOSURE:
ACADEMIC TRUTH LOCKS:
REQUIRED EXPERT REVIEW STATUS:
```

## 10. Production consistency

Transfer to the production handoff/execution pack:

- Academic Content Commit SHA;
- embedded or linked Academic Truth metadata;
- claim/source identifiers and exact locations;
- certainty/content class;
- truth locks and forbidden implications;
- character identity;
- recurring environment/object continuity;
- representation conventions;
- camera/scale conventions when necessary;
- Director correction locks when applicable.

## 11. Director approval

```text
PROGRAM COVERAGE VERIFIED: YES/NO
ACADEMIC QA PASS: YES/NO
VISUALS TRACE NODE→CLAIM→SOURCE: YES/NO
TRUTH METADATA COMPLETE PER ASSET: YES/NO
UNIQUE VISUAL JOB PER ASSET: YES/NO
FINAL DUPLICATE COUNT: 0 / <count>
NO DECORATIVE-ONLY ASSET: YES/NO
SPIRAL/CONTINUITY REVIEWED: YES/NO
PACKAGE IS SMALLEST SUFFICIENT: YES/NO
READY FOR PROMPT LOCK: YES/NO
DIRECTOR SIGN-OFF:
```