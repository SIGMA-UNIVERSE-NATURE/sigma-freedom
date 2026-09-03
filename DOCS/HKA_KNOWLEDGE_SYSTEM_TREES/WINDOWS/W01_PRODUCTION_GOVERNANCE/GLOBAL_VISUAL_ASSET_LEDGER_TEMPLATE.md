---
title: "HKA Global Visual Asset Ledger Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE"
---

# HKA GLOBAL VISUAL ASSET LEDGER

Mục tiêu: Director có một registry duy nhất để ngăn cross-window visual duplication và biết asset nào có thể reuse/cross-link.

Ledger này là control-plane metadata; không chứa binary image.

## 1. Record per canonical Asset ID

```text
ASSET ID:
OWNER WINDOW:
OWNER TREE ID:
PRIMARY NODE ID:
SECONDARY NODE IDS:
PRIMARY LEARNING OBJECTIVE:
UNIQUE VISUAL JOB:
VISUAL JOB CODE:
PRIMARY PHENOMENON / STRUCTURE / PROCESS:
REPRESENTATION TYPE:
DEPTH:
AUDIENCE:
SEMANTIC TAGS:
APPROVED CLEAN MASTER STATUS:
APPROVED BRANDED FINAL STATUS:
REUSABLE ACROSS WINDOWS: YES / NO / CONDITIONAL
REUSE CONDITIONS:
SUPERSEDES ASSET ID:
SUPERSEDED BY ASSET ID:
SOURCE WINDOW PROMPT COMMIT SHA:
FINAL MANIFEST COMMIT SHA:
STATUS: CANDIDATE / LOCKED / PRODUCED / QA_APPROVED / RELEASED / SUPERSEDED / REVOKED
```

## 2. Visual job code

Mỗi asset được gắn một functional code để search nhanh, ví dụ:

```text
OBSERVE
COMPARE
CLASSIFY
PROCESS
MECHANISM
SCALE
EVIDENCE_INFERENCE
RECONSTRUCTION
SYSTEM_FEEDBACK
CROSS_LINK
MISCONCEPTION
HUMAN_IMPACT
ETHICAL_SCENARIO
RESEARCH_POSTER
```

Code không thay semantic review; nó chỉ thu hẹp candidate duplicates.

## 3. Pre-admission search

Trước khi Window cấp Asset ID mới, Director phải tìm ledger theo:

```text
semantic tags
visual job code
phenomenon / mechanism
representation type
related node ownership
```

Kết quả phải dẫn đến một trong:

```text
NO MATCH → continue local dedup review
REUSABLE MATCH → reuse/cross-link existing asset
DERIVATIVE SUFFICIENT → no new canonical Asset ID
CONTEXTUALLY DISTINCT → new asset allowed with explicit delta
DUPLICATE → reject candidate
```

## 4. Cross-window ownership rule

Nếu asset hiện hữu dạy đúng visual job thuộc owner Window khác, Window mới ưu tiên:

```text
CROSS-LINK TO OWNER
+
REUSE APPROVED ASSET WHEN PEDAGOGICALLY VALID
```

Không sản xuất lại chỉ để “có ảnh riêng của Window”.

Asset mới được phép khi context làm thay đổi materially:

- learning objective;
- phenomenon/mechanism;
- evidence relation;
- scale;
- representation boundary;
- cognitive job.

## 5. Ledger metrics

Director báo định kỳ:

```text
TOTAL CANONICAL ASSET IDS:
TOTAL RELEASED ASSETS:
TOTAL REUSABLE ASSETS:
CROSS-WINDOW REUSES:
DUPLICATE CANDIDATES REJECTED:
SUPERSEDED ASSETS:
REVOKED ASSETS:
```

Production attempts/runs không tạo entry canonical mới trừ khi Asset ID mới thực sự được cấp.

## 6. Scale rule

Ledger tồn tại để bảo đảm HKA có thể có hàng nghìn production files nhưng vẫn giữ số **canonical learning assets** ở mức cần thiết, có owner và không trùng chức năng.

Director không đánh giá thành công bằng số lượng Asset IDs. Thành công là coverage đầy đủ với redundancy thấp nhất có thể.