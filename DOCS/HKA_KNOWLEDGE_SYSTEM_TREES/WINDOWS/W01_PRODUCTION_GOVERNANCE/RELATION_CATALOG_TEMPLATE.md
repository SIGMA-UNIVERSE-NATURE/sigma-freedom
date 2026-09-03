---
title: "HKA RELATION_CATALOG.md Template"
version: "1.1"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# HKA RELATION CATALOG

Mỗi relation là một assertion có owner, direction semantics và evidence. Không dùng generic `TWO_WAY` để che quan hệ vốn có hướng.

## RELATION: <RELATION ID>

```text
RELATION ID:
SOURCE WINDOW:
SOURCE NODE:
TARGET WINDOW:
TARGET NODE / BRANCH:
RELATION TYPE:
OWNER WINDOW:
STATUS: PROPOSED / VERIFIED / LOCKED
DIRECTION SEMANTICS:
INVERSE RELATION, IF APPLICABLE:
ALLOWED SOURCE NODE TYPES:
ALLOWED TARGET NODE TYPES:
EVIDENCE REQUIREMENT:
DUPLICATE-EQUIVALENCE KEY:
```

## 1. Canonical core relation types — mandatory superset

```text
PREREQUISITE
PART_OF
CAUSES
AFFECTS
MEASURED_BY
STRUCTURAL_ANALOGY
USED_IN
EVIDENCE_FOR
EVIDENCE_AGAINST
HISTORICAL_DEVELOPMENT
DEBATES_WITH
ETHICAL_SOCIAL_CONSEQUENCE
```

Director/Window extensions may remain, including:

```text
CONSTRAINS
MODELS
COMPARES_WITH
APPLIES_TO
HISTORICALLY_PRECEDES
CROSS_TREE_CONTEXT
CONTRASTS_WITH
```

Không được đổi nghĩa canonical core type.

## 2. Core direction semantics

| Relation | Direction semantics | Inverse / symmetric rule | Minimum evidence rule |
|---|---|---|---|
| PREREQUISITE | source is required before target | `REQUIRED_BY` if inverse record is needed | curriculum/knowledge dependency must be explicit |
| PART_OF | source is a component/subset of target | `HAS_PART` | structural/taxonomic evidence |
| CAUSES | source causally contributes to target | `CAUSED_BY` | causal evidence; correlation alone insufficient |
| AFFECTS | source materially changes/influences target without full causal exclusivity | `AFFECTED_BY` | evidence of effect/influence |
| MEASURED_BY | source phenomenon/quantity is measured by target method/tool | `MEASURES` | method/measurement validity |
| STRUCTURAL_ANALOGY | source and target share mapped structure | symmetric/self | explicit mapped similarities + limits |
| USED_IN | source tool/concept/practice is used in target | `USES` | documented use/application |
| EVIDENCE_FOR | source evidence supports target claim/model | `SUPPORTED_BY` | source/claim mapping |
| EVIDENCE_AGAINST | source evidence challenges target claim/model | `CHALLENGED_BY` | source/claim mapping |
| HISTORICAL_DEVELOPMENT | source contributes to later development target | `DEVELOPED_FROM` | historical evidence and chronology |
| DEBATES_WITH | source position debates target position | symmetric/self | positions and sources represented fairly |
| ETHICAL_SOCIAL_CONSEQUENCE | source action/system/idea has target consequence | `CONSEQUENCE_OF` | evidence or clearly marked normative analysis |

Inverse labels above are semantic aids; they do not create a second relation record unless the implementation requires one.

## 3. Extension definition requirement

Mỗi extension relation type phải có một definition record:

```text
EXTENSION RELATION TYPE:
DEFINITION:
DIRECTION SEMANTICS:
INVERSE RELATION, IF APPLICABLE:
ALLOWED SOURCE NODE TYPES:
ALLOWED TARGET NODE TYPES:
EVIDENCE REQUIREMENT:
DUPLICATE-EQUIVALENCE RULE:
WHY CORE TYPES ARE INSUFFICIENT:
```

## 4. Rationale and evidence

```text
WHY THIS RELATION EXISTS:
CLAIM IDS:
EVIDENCE / SOURCE IDS:
LIMITS:
MISINTERPRETATION TO AVOID:
```

Không dùng `CAUSES` nếu evidence chỉ cho association/correlation. Không dùng `STRUCTURAL_ANALOGY` để ngụ ý causal hoặc historical relation.

## 5. Ownership rule

Cross-tree relation không chuyển quyền sở hữu node. Source Window chỉ mô tả đủ để tạo relation; nội dung chi tiết thuộc owner Window của target.

## 6. Duplicate-equivalence

Hai records được coi là semantic duplicate khi source/target pair và relation meaning tương đương sau khi chuẩn hóa direction/inverse. Ví dụ `A PREREQUISITE B` và một record khác diễn đạt `B REQUIRED_BY A` không được tính thành hai knowledge relations độc lập.

## 7. Validation

```text
SOURCE NODE EXISTS: YES/NO
TARGET NODE/OWNER EXISTS: YES/NO
RELATION TYPE CORE OR DEFINED EXTENSION: YES/NO
DIRECTION SEMANTICS VALID: YES/NO
INVERSE SEMANTICS VALID: YES/NO/NOT_APPLICABLE
NODE-TYPE PAIR ALLOWED: YES/NO
EVIDENCE SUFFICIENT: YES/NO
DUPLICATE-EQUIVALENCE CHECK: PASS/FAIL
DIRECTOR REVIEW: PASS/RETURN
```