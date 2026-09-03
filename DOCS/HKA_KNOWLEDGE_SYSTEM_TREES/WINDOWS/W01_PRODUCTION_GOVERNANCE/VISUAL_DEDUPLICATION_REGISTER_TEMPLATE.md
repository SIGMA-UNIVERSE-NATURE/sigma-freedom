---
title: "HKA Visual Deduplication Register Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE"
---

# HKA VISUAL DEDUPLICATION REGISTER

Mục tiêu: ngăn nhiều Asset IDs dạy cùng một knowledge claim bằng cùng một visual mechanism.

Mỗi candidate asset phải được ghi vào registry này trước khi cấp Asset ID cuối cùng.

## 1. Record

```text
CANDIDATE ID:
WINDOW ID:
VCU ID:
PRIMARY NODE ID:
SECONDARY NODE IDS:
PRIMARY LEARNING OBJECTIVE:
UNIQUE VISUAL JOB:
REPRESENTATION TYPE:
PRIMARY PHENOMENON / STRUCTURE / PROCESS:
MANDATORY SCENE ELEMENTS:
AUDIENCE:
DEPTH:
SPIRAL PREDECESSOR ASSET, IF ANY:
DELTA FROM PREDECESSOR:
NEAREST EXISTING ASSET ID:
OVERLAP DESCRIPTION:
REUSE EXISTING ASSET POSSIBLE: YES / NO
POST-PRODUCTION DERIVATIVE SUFFICIENT: YES / NO
NEW ASSET JUSTIFIED: YES / NO
DIRECTOR DECISION: ADMIT / MERGE / REUSE / REJECT
RATIONALE:
```

## 2. Duplicate test

Candidate mặc định bị coi là `DUPLICATE` khi một asset hiện hữu đã có cả ba yếu tố:

```text
same or materially equivalent learning objective
+
same visual job
+
same phenomenon/mechanism/relationship being shown
```

Không đủ để biện minh asset mới bằng:

- audience khác;
- Companion khác;
- góc camera khác;
- màu khác;
- style khác;
- caption khác;
- crop khác.

## 3. Spiral exception

Một spiral asset mới được admit khi nó làm người học thực hiện một cognitive/epistemic job mới.

Ví dụ:

```text
Asset A: observe what changes
Asset B: compare variables and infer relation
Asset C: formalize/test mechanism
Asset D: critique model limits using evidence
```

Nếu chỉ là cùng nội dung viết lại cho tuổi lớn hơn:

```text
DECISION: REUSE / DERIVATIVE / REJECT
```

## 4. Scene-overlap test

Director phải so candidate với asset gần nhất theo:

```text
OBJECTS
SPATIAL RELATIONS
PROCESS ORDER
SCALE
REPRESENTATION TYPE
LEARNING OBJECTIVE
```

Nếu scene overlap cao nhưng learning objective thật sự khác, Director phải chỉ rõ `DELTA` mà người học có thể quan sát được trong output.

Nếu không chỉ được delta:

```text
NEW ASSET JUSTIFIED: NO
```

## 5. Reuse hierarchy

Ưu tiên theo thứ tự:

```text
1. REUSE exact approved asset
2. REUSE approved CLEAN MASTER with controlled post-production overlay/crop when pedagogically valid
3. CREATE derivative for delivery layer when only format changes
4. CREATE new canonical Asset ID only for a new visual learning job
```

Không dùng derivative để thay đổi academic meaning của master.

## 6. Cross-window duplicate check

Trước khi khóa package, Director kiểm cả:

```text
WITHIN WINDOW DUPLICATES
CROSS-WINDOW KNOWN DUPLICATES
```

Nếu một visual job đã thuộc owner Window khác, Window hiện tại tạo cross-link thay vì sản xuất lại, trừ khi context mới đòi hỏi một distinct visual job có giải trình.

## 7. Metrics

Window báo:

```text
CANDIDATE VISUAL JOBS:
ADMITTED ASSETS:
MERGED CANDIDATES:
REUSED EXISTING ASSETS:
DERIVATIVE-ONLY CASES:
REJECTED DUPLICATES:
FINAL DUPLICATE COUNT: 0
```

`FINAL DUPLICATE COUNT` phải bằng 0 trước `DIRECTOR VISUAL GATE: PASS`.
