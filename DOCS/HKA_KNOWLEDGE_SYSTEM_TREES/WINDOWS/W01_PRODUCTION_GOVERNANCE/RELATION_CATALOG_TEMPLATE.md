---
title: "HKA RELATION_CATALOG.md Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE"
---

# HKA RELATION CATALOG

Mỗi relation là một assertion có owner, direction và evidence.

## RELATION: <RELATION ID>

```text
RELATION ID:
SOURCE WINDOW:
SOURCE NODE:
TARGET WINDOW:
TARGET NODE / BRANCH:
RELATION TYPE:
DIRECTION: ONE_WAY / TWO_WAY
OWNER WINDOW:
STATUS: PROPOSED / VERIFIED / LOCKED
```

### Relation types

```text
PREREQUISITE
PART_OF
CAUSES
CONSTRAINS
EVIDENCE_FOR
MODELS
MEASURES
COMPARES_WITH
APPLIES_TO
HISTORICALLY_PRECEDES
CROSS_TREE_CONTEXT
CONTRASTS_WITH
```

Không dùng `CAUSES` nếu evidence chỉ cho correlation/association.

### Rationale

```text
WHY THIS RELATION EXISTS:
EVIDENCE / SOURCE IDS:
LIMITS:
MISINTERPRETATION TO AVOID:
```

### Ownership rule

Cross-tree relation không chuyển quyền sở hữu node. Source Window chỉ được mô tả đủ để tạo liên kết; nội dung chi tiết thuộc Target Window.

### Validation

```text
SOURCE NODE EXISTS: YES/NO
TARGET OWNER IDENTIFIED: YES/NO
EVIDENCE SUFFICIENT: YES/NO
NO DUPLICATE RELATION: YES/NO
DIRECTOR REVIEW: PASS/RETURN
```