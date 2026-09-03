---
title: "HKA Academic Program Authoring Standard"
version: "1.3"
status: "ARCHITECT FINALIZED REFERENCE"
language: "vi"
date: "2026-09-03"
---

# HKA ACADEMIC PROGRAM AUTHORING STANDARD

## 1. Objective and applicability

Tài liệu này định nghĩa cách các **content-authoring Window Types** biến canonical Knowledge Tree scope thành chương trình học thuật hoàn chỉnh trước visual authoring.

Không mặc định áp dụng một semantics cho W02–W64. Applicability theo `WINDOW_TYPE_APPLICABILITY_STANDARD.md`. Full academic-authoring workflow áp dụng chủ yếu cho các Window có content scope; W61–W64 không bị ép vào curriculum-authoring semantics nếu contract là SYSTEM QA / INTEGRATION.

`KNOWLEDGE_BRANCH_SCOPE_AND_VISUAL_BUDGET_STANDARD.md` là **guidance chống thiếu/thừa**, không tạo thêm một lớp hồ sơ bắt buộc nếu TREE/NODE/QA đã chứa đủ bằng chứng tương đương.

## 2. Critical authoring sequence

### Phase A — Scope lock

1. Đọc exact Window Contract.
2. Ghi Window ID, Window Type, Tree ID và canonical branch path.
3. Liệt kê mandatory scope.
4. Liệt kê excluded scope và target owner.
5. Không đổi tên canonical level-1 branch nếu chưa được phép.

### Phase B — Academic inventory and TREE

Cho mỗi mandatory branch, xác định:

- central question;
- core concepts;
- definitions;
- structures/processes/mechanisms;
- methods and evidence;
- examples and counterexamples;
- applications;
- misconceptions;
- uncertainties;
- controversies/open questions;
- cross-tree dependencies.

Branch coverage record **được nhúng trong `TREE.md` hoặc Academic QA**, không bắt buộc file riêng.

### Phase C — Node / relation / source construction

Mỗi node tuân `NODE_CATALOG_TEMPLATE.md` và phải có prerequisites, typed relations, D1–D4, claim/source evidence, epistemic classification và visual implication hoặc `VISUAL NOT REQUIRED — reason`.

Mỗi relation tuân `RELATION_CATALOG_TEMPLATE.md`. Mỗi material claim phải có stable Claim ID và source mapping phù hợp claim type.

### Phase D — Learning progression

```text
D1 — encounter / observe / recognize
D2 — construct / compare / explain
D3 — formalize / model / test
D4 — research / synthesize / critique / extend
```

D1–D4 là competency depth, không phải age bands.

### Phase E — Epistemic classification

Mọi material claim/node giữ hai trục độc lập:

```text
CERTAINTY:
ESTABLISHED / DEVELOPING / DEBATED / HYPOTHETICAL / UNKNOWN

CONTENT CLASS:
ESTABLISHED_KNOWLEDGE
DEVELOPING_RESEARCH
ACADEMIC_DEBATE
PHILOSOPHICAL_DEBATE
HUMANISTIC_METAPHOR
```

Optional independent fields:

```text
CONTEXT DEPENDENCE
NORMATIVE STATUS
MODEL STATUS / APPROXIMATION
```

### Phase F — Academic QA

Mặc định tạo **một durable artifact duy nhất**:

```text
ACADEMIC_QA_REPORT.md
```

Report phải chứa hoặc liên kết một coverage matrix đủ để kiểm:

- 100% mandatory branch coverage;
- external curriculum/classification mapping khi contract yêu cầu;
- semantic duplicate nodes;
- orphan/unreachable nodes;
- prerequisite existence/cycle/reachability;
- claim-to-source coverage;
- high-risk cross-checks;
- D1–D4 substantive progression;
- misconception coverage;
- certainty/content-class separation;
- expert-review blockers;
- cross-window ownership conflicts;
- program economy.

Với chương trình lớn, có thể tách `ACADEMIC_COVERAGE_AUDIT.md` hoặc `ACADEMIC_COVERAGE_MATRIX.csv`; đó là **supporting artifact**, không phải một vòng review riêng.

Director có thể direct-fix lỗi nhỏ khách quan theo provenance rule. Material claim, prerequisite, source, learning objective hoặc scope defect phải trả đúng phần về owner Window và tạo academic content commit mới.

Chỉ sau:

```text
ACADEMIC QA REPORT: PASS
DIRECTOR ACADEMIC GATE: PASS
```

mới được tạo Program-to-Visual brief.

## 3. Minimum required academic outputs

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
ACADEMIC_QA_REPORT.md
SELF_AUDIT.md
```

Optional/supporting when justified:

```text
ACADEMIC_COVERAGE_AUDIT.md
ACADEMIC_COVERAGE_MATRIX.csv
DOMAIN-SPECIFIC APPENDICES
```

## 4. Program completeness test

Một chương trình đạt khi reviewer/domain expert có thể:

1. biết phạm vi và boundaries;
2. lần branch → node → claim → source;
3. biết prerequisite graph và entry points;
4. biết certainty riêng với content class/model/normative status;
5. biết progression D1–D4;
6. biết relation và owner sang Window khác;
7. biết phần nào cần trực quan hóa;
8. không phải hỏi tác giả để hiểu cấu trúc;
9. tái lập được Academic QA result từ các artifact đã khóa.

## 5. Program economy

```text
COMPLETE COVERAGE + MINIMUM REDUNDANCY
```

Không tạo node, file hay review step chỉ để lấp mẫu. Mỗi artifact phải phục vụ trực tiếp cho authoring, truth traceability, QA hoặc production handoff.