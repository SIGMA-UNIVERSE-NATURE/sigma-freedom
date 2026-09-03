---
title: "HKA Program-to-Visual Director Brief Template"
version: "1.2"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# PROGRAM-TO-VISUAL DIRECTOR BRIEF

Tài liệu này nối curriculum đã qua Academic QA với visual package. Nó không thay prompt record.

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
ACADEMIC COVERAGE AUDIT PATH:
ACADEMIC QA REPORT PATH:
ACADEMIC QA RESULT: PASS
DIRECTOR ACADEMIC GATE: PASS
BRANCH SCOPE / VISUAL BUDGET STANDARD VERIFIED: YES/NO
```

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

Mỗi VCU/Asset candidate phải có một completed `ACADEMIC_TRUTH_PACK` hoặc equivalent embedded record chứa:

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

## 7. Visual candidate deduplication

Hoàn thành `VISUAL_DEDUPLICATION_REGISTER.md` và kiểm Global Visual Asset Ledger nếu được triển khai.

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

Không chọn package lớn rồi tạo hình để lấp capacity. Nếu nhu cầu unique visual jobs vượt P36, dừng và đưa Director/Architect scope decision.

## 9. Asset sequence and truth lock

| Asset ID | VCU | Audience | Depth | Companion | Claim IDs | Truth Pack Ref | Unique visual job | Prior visual | Next visual |
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
- Academic Truth Pack path/reference;
- claim/source identifiers and exact locations;
- certainty/content class;
- truth locks and forbidden implications;
- character identity;
- recurring environment/object continuity;
- representation conventions;
- camera/scale conventions when necessary;
- Director global correction locks.

## 11. Director approval

```text
PROGRAM COVERAGE VERIFIED: YES/NO
ACADEMIC QA PASS: YES/NO
COMPRESSION TEST: PASS/FAIL
EXPANSION TEST: PASS/FAIL
VISUALS TRACE NODE→CLAIM→SOURCE: YES/NO
ACADEMIC TRUTH PACK COMPLETE PER ASSET: YES/NO
UNIQUE VISUAL JOB PER ASSET: YES/NO
FINAL DUPLICATE COUNT: 0 / <count>
NO DECORATIVE-ONLY ASSET: YES/NO
SPIRAL/CONTINUITY REVIEWED: YES/NO
PACKAGE IS SMALLEST SUFFICIENT: YES/NO
READY FOR PROMPT LOCK: YES/NO
DIRECTOR SIGN-OFF:
```