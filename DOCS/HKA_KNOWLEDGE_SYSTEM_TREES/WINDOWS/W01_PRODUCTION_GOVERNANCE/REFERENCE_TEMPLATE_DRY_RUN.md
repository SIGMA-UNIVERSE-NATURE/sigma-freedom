---
title: "HKA W01 — Reference Template Dry Run"
window_id: "W01"
test_target: "W10 Mathematics & Formal Systems"
version: "1.0"
status: "PASS"
language: "vi"
date: "2026-09-03"
---

# HKA W01 — REFERENCE TEMPLATE DRY RUN

## 1. Mục đích

Kiểm tra `WINDOW_CONTRACT_TEMPLATE.md` bằng một instantiation giả lập cho:

```text
WINDOW: W10
TREE: Toán học & Hệ hình thức
TREE ID: HKA-TREE-01-MATH
SLUG: mathematics-formal-systems
```

Đây không phải W10 contract, không tạo W10 branch, không phát triển nội dung W10 và không cấp production authorization.

## 2. Dry-run mapping

| Template section | Example W10 input | Kết quả |
|---|---|---|
| 01 Identity | W10 / HKA-TREE-01-MATH | PASS |
| 02 Source lock | Canonical SHA, W10 contract SHA, brand SHA | PASS |
| 03 HKA position | Quy luật & Thực tại → Toán học & Hệ hình thức | PASS |
| 04 Central question | Các cấu trúc và quan hệ hình thức biểu diễn quy luật thế nào? | PASS |
| 05 Objective | Phát triển ontology toán từ D1 đến D4 và gói visual khóa | PASS |
| 06 Mandatory scope | Logic, số, đại số, hình học, giải tích, xác suất, rời rạc, tô pô, ứng dụng | PASS |
| 07 Excluded scope | Vật lý chủ sở hữu W11; computation chủ sở hữu W14 | PASS |
| 08 Canonical branches | 10 cành cấp 1 từ HKA World Tree | PASS |
| 09 Coverage baseline | School core, undergraduate core, research taxonomy | PASS |
| 10 Methods | Definition, proof, counterexample, computation, modeling | PASS |
| 11 Core nodes | Number, function, proof, space, change, randomness | PASS |
| 12 Open questions | Phân loại riêng; không cần biết đáp án trước | PASS |
| 13 Controversies | Foundations, interpretation, method disputes | PASS |
| 14 Cross-links | W11 physics, W14 computing, W47 economics | PASS |
| 15 Misconceptions | Equality vs approximation; correlation vs causation | PASS |
| 16 D1–D4 | Observable competencies independent of age | PASS |
| 17 A1–A5 | Expression modes without knowledge lock | PASS |
| 18 VCU | Max two branches and six nodes per asset | PASS |
| 19 Package | Decision table supports P12–P36 or scope split | PASS |
| 20 Asset types | Hero, mechanism, scale, misconception, cross-link, poster | PASS |
| 21 Characters | Balanced role-based distribution | PASS |
| 22 Logo/MOTTO | Exact immutable lock | PASS |
| 23 Brand source | Repo + full commit + exact paths | PASS |
| 24 Prompt schema | Academic + visual + output + QA fields | PASS |
| 25 Negative prompts | Global + math-specific + asset-specific | PASS |
| 26 Self-audit | Coverage, ownership, source and manifest checks | PASS |
| 27 Acceptance gates | Six gates apply without modification | PASS |
| 28 Git | Branch, path, two-commit procedure | PASS |
| 29 Handoff | Counts, SHAs, risks and validation | PASS |
| 30 Blocked conditions | Missing sources/write access/schema/brand | PASS |

## 3. Questions the template resolves without clarification

```text
Where may W10 write?
What must W10 cover?
What belongs to another owner?
How are D1–D4 separated from A1–A5?
How is image count selected and locked?
What does every prompt contain?
Which character and logo files are authoritative?
How are Prompt Content Commit and Final Manifest Commit separated?
What makes an output PASS, FAIL or BLOCKED?
What must W10 return for review?
```

## 4. Scope-size test

The template prevents a large tree from silently exceeding P36:

1. W10 inventories branches and visual-demand nodes.
2. W10 forms VCUs.
3. If more than 19 VCUs can be represented within P36 without overload, use P36.
4. If P36 would force an asset above two branches/six nodes/one learning objective, W10 must propose a scope split before production.

Thus the package cap does not encourage visual overcrowding.

## 5. Domain-specific extension test

The generic prompt template leaves explicit fields for mathematics-specific controls, including:

- proof versus illustration;
- exact versus approximate equality;
- coordinate and orientation conventions;
- graph axes and scale;
- symbolic content added in controlled post-production;
- counterexamples;
- domain restrictions;
- stochastic versus deterministic models.

No generic field needs to be deleted. W10 can add stricter locks without weakening the standard.

## 6. Dry-run result

```text
G01 NO FIELD INVENTION REQUIRED: PASS
G02 QUANTITY DECISION CLEAR: PASS
G03 BRAND SOURCE CLEAR: PASS
G04 GIT/HANDOFF CLEAR: PASS
G05 QA EVIDENCE CLEAR: PASS
G06 VOCABULARY CONSISTENT: PASS
G07 CREATIVE FREEDOM PRESERVED INSIDE TRUTH LOCKS: PASS

OVERALL: PASS
```

## 7. Limitation

This dry run proves template executability at contract-design level. It does not prove the future W10 academic content is complete or correct; that requires the dedicated W10 Window and expert review.