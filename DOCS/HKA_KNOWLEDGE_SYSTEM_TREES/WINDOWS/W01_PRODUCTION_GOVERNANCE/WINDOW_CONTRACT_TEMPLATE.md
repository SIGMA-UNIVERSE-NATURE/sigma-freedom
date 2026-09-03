---
title: "HKA — Window Contract Template"
version: "1.0"
status: "REFERENCE TEMPLATE"
language: "vi"
date: "2026-09-03"
---

# HKA WINDOW CONTRACT TEMPLATE

> Sao chép template này thành `WINDOW_CONTRACT.md` của từng cửa sổ. Mọi placeholder phải được thay bằng giá trị cụ thể trước khi phát hành. Không cho phép `TBD`, `latest`, hoặc khoảng số lượng trong bản `CONTRACT_LOCKED`.

---

## 01. WINDOW IDENTITY

```text
WINDOW ID:
WINDOW NAME:
TREE ID:
TREE SLUG:
HKA DOMAIN:
CONTRACT VERSION:
CONTRACT STATUS: DRAFT / CONTRACT_LOCKED
ISSUED DATE:
```

## 02. SOURCE LOCK

```text
CANONICAL REPOSITORY:
CANONICAL BASE BRANCH:
CANONICAL BASE COMMIT SHA:
CANONICAL INDEX PATH:
CANONICAL INDEX COMMIT SHA:
WINDOW CONTRACT PATH:
WINDOW CONTRACT COMMIT SHA:
EXECUTION BRANCH:
ALLOWED WRITE PREFIX:
BRAND REPOSITORY:
BRAND ASSET COMMIT SHA:
```

## 03. POSITION IN HKA

Nêu rõ cửa sổ nằm ở đâu trong HKA World Tree:

```text
ROOT / DOMAIN / TREE / BRANCH PATH:
PARENT TREE:
SIBLING WINDOWS:
CANONICAL OWNER OF OVERLAPPING NODES:
```

## 04. CENTRAL QUESTION

```text
CÂU HỎI TRUNG TÂM:
WHY THIS QUESTION MATTERS:
```

## 05. SINGLE OBJECTIVE

Viết một mục tiêu duy nhất, đo được ở cấp gói đầu ra. Không dùng khẩu hiệu thay mục tiêu.

## 06. MANDATORY SCOPE

Liệt kê chính xác các cành, nhánh, phương pháp, ứng dụng và vấn đề phải phát triển.

```text
MANDATORY BRANCHES:
MANDATORY METHODS:
MANDATORY APPLICATIONS:
MANDATORY CONTROVERSIES / OPEN QUESTIONS:
```

## 07. EXCLUDED SCOPE

Liệt kê những phần cửa sổ không được chiếm. Với mỗi phần, chỉ rõ `TARGET WINDOW` và loại liên kết được phép tạo.

## 08. CANONICAL BRANCH STRUCTURE

Dán cây canonical được phép phát triển. Không tự đổi tên cấp 1 nếu chưa có change request được phê duyệt.

## 09. ACADEMIC COVERAGE BASELINE

Xác định các vùng học thuật, chuẩn năng lực, giáo trình hoặc classification scheme dùng để kiểm toán độ phủ. Chúng là nguồn đối chiếu, không phải cấu trúc tối cao.

```text
COVERAGE SOURCES:
MINIMUM CORE AREAS:
EXPLICITLY REQUIRED MODERN / EMERGING AREAS:
```

## 10. DOMAIN-SPECIFIC METHODS

Liệt kê các phương pháp hình thành tri thức đặc thù của lĩnh vực và tiêu chuẩn bằng chứng tương ứng.

## 11. NON-NEGOTIABLE CORE NODES

Bảng bắt buộc:

| Core Node | Node Type | Why Non-Negotiable | Minimum D1–D4 Reach |
|---|---|---|---|

## 12. OPEN QUESTIONS

Mỗi câu hỏi mở phải ghi:

```text
QUESTION:
CURRENT STATUS:
WHY OPEN:
EVIDENCE NEEDED:
MISREPRESENTATION TO AVOID:
```

## 13. ACADEMIC CONTROVERSIES

Phân biệt:

- tranh luận về dữ liệu;
- tranh luận về phương pháp;
- tranh luận về diễn giải;
- tranh luận triết học;
- khác biệt chuẩn tắc.

Không được biến khác biệt học thuật thành “hai bên đều đúng” nếu bằng chứng không cân bằng.

## 14. REQUIRED CROSS-TREE LINKS

| Source Node/Branch | Target Window | Target Node/Branch | Relation Type | Reason | Ownership Rule |
|---|---|---|---|---|---|

## 15. HIGH-RISK MISCONCEPTIONS

Bảng:

| Misconception | Why Harmful | Correct Model | Visual Risk | Required Countermeasure |
|---|---|---|---|---|

## 16. D1–D4 REQUIREMENTS

```text
D1 — GẶP GỠ:
Observable capability indicators:

D2 — KIẾN TẠO:
Observable capability indicators:

D3 — HÌNH THỨC HÓA:
Observable capability indicators:

D4 — NGHIÊN CỨU & TỔNG HỢP:
Observable capability indicators:
```

Không gắn D1–D4 với tuổi.

## 17. A1–A5 EXPRESSION REQUIREMENTS

| Mode | Default Ages | Language | Visual Density | Interaction | Safety/Sensitivity |
|---|---:|---|---|---|---|
| A1 | 5–8 | | | | |
| A2 | 9–12 | | | | |
| A3 | 13–15 | | | | |
| A4 | 16–18 | | | | |
| A5 | 19–24 | | | | |
| R | Research | | | | |

Tuổi chỉ điều chỉnh cách biểu đạt, không khóa tri thức.

## 18. VISUAL COVERAGE UNIT RULES

Xác định:

- cách nhóm nút thành VCU;
- tối đa 2 cành cấp 1/VCU;
- tối đa 6 node IDs/asset;
- một learning objective chính;
- tiêu chí chấm Centrality 0–3, Visualization Need 0–3, Misconception Risk 0–2, Cross-link Value 0–2;
- điều kiện cần ảnh và điều kiện nên dùng phương tiện khác.

## 19. LOCKED PACKAGE

```text
SELECTED PACKAGE: P12 / P18 / P24 / P30 / P36
LOCKED ASSET COUNT:
CALIBRATION BATCH COUNT: 2 assets
PRODUCTION BATCH MAP:
EXPECTED CLEAN MASTER COUNT:
EXPECTED BRANDED FINAL COUNT:
EXPECTED TOTAL IMAGE FILES:
RATIONALE:
```

Không dùng khoảng số lượng.

## 20. REQUIRED ASSET TYPES

Chỉ rõ số lượng chính xác theo loại:

```text
HERO:
ANCHOR/OVERVIEW:
CONCEPT/PROCESS/MECHANISM/RECONSTRUCTION:
COMPARISON/SCALE/MISCONCEPTION:
CROSS-LINK:
HUMAN IMPACT/ETHICAL SCENARIO:
RESEARCH POSTER:
TOTAL:
```

## 21. CHARACTER DISTRIBUTION

```text
SIGMA PRIMARY COUNT:
CRICKET PRIMARY COUNT:
LITTLE ANT PRIMARY COUNT:
PROFESSOR OWL PRIMARY COUNT:
ENSEMBLE FOUR COUNT:
ALLOWED JUSTIFICATION FOR IMBALANCE:
```

Mỗi asset phải có ít nhất một companion; HERO phải đủ bốn.

## 22. LOGO & MOTTO LOCK

```text
LOGO MASTER PATH:
COMPACT EMBLEM PATH:
EXACT MOTTO: PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
POST-PRODUCTION COMPOSITING REQUIRED: YES
MODEL-GENERATED LOGO/TEXT ALLOWED: NO
```

## 23. BRAND ASSET SOURCE

Ghi repo + full 40-char commit SHA + exact character paths. Không dùng link branch mutable làm nguồn sản xuất.

## 24. PROMPT RECORD SCHEMA

Tham chiếu `PROMPT_ASSET_RECORD_TEMPLATE.md` và bổ sung các trường chuyên ngành bắt buộc.

## 25. NEGATIVE PROMPTS

Tách ba lớp:

```text
GLOBAL HKA NEGATIVE PROMPT:
DOMAIN-SPECIFIC NEGATIVE PROMPT:
ASSET-SPECIFIC NEGATIVE PROMPT:
```

## 26. SELF-AUDIT REQUIREMENTS

Tối thiểu kiểm:

- độ phủ cành cấp 1;
- node trùng/sai owner;
- liên kết mơ hồ;
- nguồn yếu;
- tranh luận bị trình bày như sự thật;
- prompt ↔ manifest;
- batch count;
- character distribution;
- brand lock;
- placeholder SHA;
- file ngoài prefix.

## 27. ACCEPTANCE GATES

Chỉ rõ bằng chứng và PASS/FAIL/BLOCKED cho:

```text
Academic
Pedagogy
Visual
Character & Brand
Accessibility
Integrity
```

## 28. GIT PATHS & VERSION CONTROL

```text
REPOSITORY:
EXECUTION BRANCH:
ALLOWED WRITE PREFIX:
FORBIDDEN PATHS:
COMMIT CONVENTION:
CONTENT COMMIT RULE:
FINAL MANIFEST COMMIT RULE:
MERGE AUTHORIZATION: NO
```

## 29. HANDOFF RECEIPT

Yêu cầu cửa sổ trả đầy đủ:

```text
STATUS
CONTENT COMMIT SHA
FINAL MANIFEST COMMIT SHA
FILES CREATED
OUT-OF-SCOPE CHANGES
NODE/RELATION/SOURCE COUNTS
ASSET/PROMPT/BATCH COUNTS
SCHEMA VALIDATION
BRAND VERIFICATION
OPEN RISKS
EXPERT REVIEW REQUIRED
```

## 30. BLOCKED CONDITIONS

Cửa sổ phải dừng nếu:

- không đọc được source lock;
- không có quyền ghi khi commit là đầu ra bắt buộc;
- schema không thể biểu diễn output;
- prompt mâu thuẫn học thuật;
- brand asset thiếu/sai;
- manifest chưa khóa được số lượng;
- còn placeholder SHA;
- bị yêu cầu merge, R2 upload hoặc deploy trái quyền.

Mỗi blocker phải có:

```text
BLOCKER ID:
SOURCE:
AFFECTED OUTPUTS:
WHY EXECUTION CANNOT CONTINUE SAFELY:
REQUIRED DECISION:
```

---

# FINAL CONTRACT CHECK

Trước khi chuyển `CONTRACT_LOCKED`, người phát hành phải xác nhận:

```text
[ ] 30 phần đã điền đầy đủ
[ ] Không còn placeholder/TBD
[ ] Một phạm vi duy nhất
[ ] Gói và số lượng chính xác
[ ] Batch map chính xác
[ ] Brand repo/commit/path chính xác
[ ] MOTTO chính xác
[ ] Git prefix và quyền hạn rõ
[ ] Acceptance criteria có thể quan sát
[ ] Stop conditions rõ
[ ] Contract commit SHA được ghi vào execution prompt
```
