---
title: "HKA Academic Program Authoring Standard"
version: "1.1"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA ACADEMIC PROGRAM AUTHORING STANDARD

## 1. Objective

Tài liệu này định nghĩa cách W02–W64 biến một canonical Knowledge Tree branch thành một chương trình học thuật hoàn chỉnh trước khi tạo visual assets.

Chuẩn này phải đọc cùng `KNOWLEDGE_BRANCH_SCOPE_AND_VISUAL_BUDGET_STANDARD.md` để tránh cả under-development và over-development.

## 2. Required sequence

### Phase A — Scope lock

1. Đọc exact Window Contract.
2. Ghi Window ID, Tree ID, canonical branch path.
3. Liệt kê mandatory scope.
4. Liệt kê excluded scope và target owner.
5. Không đổi tên canonical level-1 branch nếu chưa được phép.

### Phase B — Academic inventory

Cho mỗi mandatory branch, lập inventory:

- central question;
- core concepts;
- definitions;
- structures/processes/mechanisms;
- methods and evidence;
- examples and counterexamples;
- applications;
- misconceptions;
- uncertainties;
- controversies;
- open questions;
- cross-tree dependencies.

Mỗi mandatory branch phải có Branch Coverage Record theo `KNOWLEDGE_BRANCH_SCOPE_AND_VISUAL_BUDGET_STANDARD.md`.

Không chuyển sang visual khi inventory còn vùng trắng không được giải trình.

### Phase C — Node decomposition

Một node tốt phải:

- có một primary knowledge function rõ;
- đủ nhỏ để có thể kiểm claim/source;
- đủ lớn để không biến catalog thành danh sách trivia;
- có prerequisites;
- có relationship với parent/sibling/cross-tree nodes;
- có D1–D4 progression;
- có source evidence;
- có visual implication hoặc `VISUAL NOT REQUIRED — reason`.

Authoring envelope và review triggers cho node được định nghĩa trong `KNOWLEDGE_BRANCH_SCOPE_AND_VISUAL_BUDGET_STANDARD.md`; chúng là trigger kiểm tra, không phải quota để kéo dài/rút ngắn giả tạo.

### Phase D — Learning progression

Mỗi core concept phải có progression:

```text
D1 — encounter / observe / recognize
D2 — construct / compare / explain
D3 — formalize / model / test
D4 — research / synthesize / critique / extend
```

D1–D4 không phải age bands. A1–A5 chỉ điều chỉnh expression.

### Phase E — Evidence and epistemic status

Mọi material claim phải được phân loại:

```text
SETTLED / HIGH CONSENSUS
CONTEXT-DEPENDENT
ACTIVE DEBATE
OPEN QUESTION
MODEL / APPROXIMATION
NORMATIVE / VALUE JUDGMENT
```

Không trình bày open question như settled fact.

### Phase F — Coverage and density audit

Window tự kiểm:

- 100% mandatory level-1 branches mapped;
- core methods represented;
- foundational + modern/emerging areas represented;
- no orphan prerequisites;
- no duplicate ownership;
- no unsupported high-risk claim;
- no D4 section consisting only of harder wording;
- Branch Coverage Record complete;
- Compression Test PASS;
- Expansion Test PASS;
- short-content review triggers resolved;
- long-content / flat fan-out review triggers resolved;
- no trivia fragmentation used to inflate node count.

### Phase G — Director review

Director có quyền:

- sửa trực tiếp naming/metadata/obvious omissions;
- yêu cầu bổ sung exact missing branch/source/node;
- yêu cầu merge/compress redundant material;
- yêu cầu split node khi nhiều primary knowledge functions bị trộn;
- dừng visual phase nếu chương trình chưa đủ hoặc đang phình lặp.

Chỉ sau `DIRECTOR ACADEMIC GATE: PASS` mới tạo visual package.

## 3. Required academic outputs

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
```

Window có thể bổ sung domain-specific files nhưng không thay thế bốn file trên.

## 4. Program completeness test

Một chương trình đạt khi một domain expert có thể:

1. biết phạm vi và boundaries;
2. lần từ branch → node → source;
3. biết prerequisite của một node;
4. biết điều gì chắc/chưa chắc;
5. biết progression D1–D4;
6. biết relation sang Window khác;
7. biết phần nào cần trực quan hóa;
8. không phải hỏi Window tác giả để hiểu cấu trúc.

Nếu cần hỏi lại vì file thiếu thông tin, program chưa done.

## 5. Program economy test

Program cũng chưa done nếu cùng một knowledge function bị lặp ở nhiều node/section mà không có progression hoặc ownership reason.

Mục tiêu:

```text
COMPLETE COVERAGE
+
MINIMUM REDUNDANCY
```

Độ dài không phải thành tích. Mỗi đoạn phải phục vụ một knowledge function, evidence function, progression function hoặc boundary function rõ ràng.