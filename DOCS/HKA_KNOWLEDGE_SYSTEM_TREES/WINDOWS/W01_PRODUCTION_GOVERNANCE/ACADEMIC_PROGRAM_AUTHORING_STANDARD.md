---
title: "HKA Academic Program Authoring Standard"
version: "1.2"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
language: "vi"
date: "2026-09-03"
---

# HKA ACADEMIC PROGRAM AUTHORING STANDARD

## 1. Objective and applicability

Tài liệu này định nghĩa cách các **content-authoring Window Types** biến canonical Knowledge Tree scope thành chương trình học thuật hoàn chỉnh trước visual authoring.

Không mặc định áp dụng một semantics cho W02–W64. Applicability phải theo `WINDOW_TYPE_APPLICABILITY_STANDARD.md`. Full academic-authoring workflow dự kiến áp dụng chủ yếu cho W02–W60 khi Window Contract phân loại chúng là FOUNDATION / ROOT / METHOD, DOMAIN / DISCIPLINE CONTENT hoặc CROSS-DOMAIN HUB. W61–W64 không bị ép vào curriculum-authoring semantics nếu contract của chúng là SYSTEM QA / INTEGRATION.

Chuẩn này phải đọc cùng `KNOWLEDGE_BRANCH_SCOPE_AND_VISUAL_BUDGET_STANDARD.md`.

## 2. Required sequence

### Phase A — Scope lock

1. Đọc exact Window Contract.
2. Ghi Window ID, Window Type, Tree ID và canonical branch path.
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

Mỗi mandatory branch phải có Branch Coverage Record. Không chuyển visual khi inventory còn vùng trắng không được giải trình.

### Phase C — Node decomposition

Mỗi node phải tuân `NODE_CATALOG_TEMPLATE.md`, có một primary knowledge function, prerequisites, relations, D1–D4, claim/source evidence, epistemic classification và visual implication hoặc `VISUAL NOT REQUIRED — reason`.

### Phase D — Learning progression

```text
D1 — encounter / observe / recognize
D2 — construct / compare / explain
D3 — formalize / model / test
D4 — research / synthesize / critique / extend
```

D1–D4 là competency depth, không phải age bands.

### Phase E — Epistemic classification: canonical two-axis rule

Mọi material claim/node phải giữ **hai trục độc lập**:

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

Optional independent fields khi phù hợp:

```text
CONTEXT DEPENDENCE:
NORMATIVE STATUS:
MODEL STATUS / APPROXIMATION:
```

Không dùng `MODEL / APPROXIMATION` như certainty level. Một scientific model có thể là ESTABLISHED. Không dùng `NORMATIVE / VALUE JUDGMENT` để thay content class hoặc certainty.

### Phase F — Durable coverage audit

Window phải tạo:

```text
ACADEMIC_COVERAGE_AUDIT.md
hoặc
ACADEMIC_COVERAGE_MATRIX.csv
```

Audit phải kiểm tối thiểu:

- 100% mandatory branch coverage;
- external curriculum / classification mapping khi contract yêu cầu;
- semantic duplicate-node detection;
- orphan-node detection;
- prerequisite existence;
- prerequisite-cycle detection hoặc documented co-requisite exception;
- entry-point reachability;
- claim-to-source coverage;
- high-risk claim cross-checks;
- D1–D4 substantive progression;
- misconception coverage;
- certainty/content-class separation;
- unresolved expert-review items;
- cross-window ownership conflict = 0 before lock;
- Compression Test PASS;
- Expansion Test PASS;
- density/fan-out triggers resolved.

Một Window không được ghi `COMPLETE` chỉ vì mọi heading có text.

### Phase G — Academic QA report and Director gate

Trước visual authoring phải tạo:

```text
ACADEMIC_QA_REPORT.md
```

Report có thể do Director và/hoặc designated domain expert hoàn thiện theo Window Contract; không bắt buộc tạo thêm một Window chỉ để review nếu review có thể thực hiện chuẩn xác trong cùng operating flow.

Director có quyền sửa lỗi nhỏ khách quan chỉ theo `DIRECTOR_FIX_PROVENANCE_TEMPLATE.md`. Material claim, prerequisite, source, learning objective hoặc scope defect phải trả đúng phần về owner Window và tạo academic content commit mới.

Chỉ sau:

```text
ACADEMIC COVERAGE AUDIT: PASS
ACADEMIC QA REPORT: PASS
DIRECTOR ACADEMIC GATE: PASS
```

mới được tạo Program-to-Visual package.

## 3. Required academic outputs for applicable content windows

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
ACADEMIC_COVERAGE_AUDIT.md or ACADEMIC_COVERAGE_MATRIX.csv
ACADEMIC_QA_REPORT.md
SELF_AUDIT.md
```

Window Types khác dùng profile trong `WINDOW_TYPE_APPLICABILITY_STANDARD.md`.

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
9. tái lập được coverage/QA result từ durable artifacts.

## 5. Program economy

```text
COMPLETE COVERAGE
+
MINIMUM REDUNDANCY
```

Độ dài không phải thành tích. Mỗi đoạn phải phục vụ một knowledge/evidence/progression/boundary function. Semantic duplicate node hoặc redundant claim phải merge, cross-link hoặc giải trình.