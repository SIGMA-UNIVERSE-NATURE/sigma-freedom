---
title: "HKA Window Type Applicability Standard"
version: "1.0"
status: "PROPOSED REFERENCE — ARCHITECT REVIEW REQUIRED"
---

# HKA WINDOW TYPE APPLICABILITY STANDARD

Director Layer không áp dụng một Content Window semantics duy nhất cho W02–W64. Mỗi Window Contract phải khai báo một `WINDOW TYPE`.

## 1. Window Types

```text
FOUNDATION / ROOT / METHOD WINDOW
DOMAIN / DISCIPLINE CONTENT WINDOW
CROSS-DOMAIN HUB WINDOW
SYSTEM QA / INTEGRATION WINDOW
```

Architect có thể định nghĩa subtype, nhưng phải map về một profile trên hoặc phát hành contract riêng.

## 2. FOUNDATION / ROOT / METHOD WINDOW

Primary jobs:

- foundational ontology/methods;
- cross-program entry points;
- root concepts and evidence practices;
- definitions used by multiple downstream windows.

Default artifacts when applicable:

```text
TREE.md
NODE_CATALOG.md
RELATION_CATALOG.md
SOURCE_REGISTER.md
ACADEMIC_COVERAGE_AUDIT.md
ACADEMIC_QA_REPORT.md
```

Visual authoring only if Window Contract requires it.

## 3. DOMAIN / DISCIPLINE CONTENT WINDOW

Primary jobs:

- develop full assigned Knowledge Tree/branch program;
- source and graph integrity;
- D1–D4 progression;
- Program-to-Visual authoring when visual production is in scope.

Default full academic workflow applies.

Expected initial applicability: content windows in W02–W60 unless an exact contract says otherwise.

## 4. CROSS-DOMAIN HUB WINDOW

Primary jobs:

- relation-heavy integration across owner windows;
- shared methods/interfaces;
- cross-domain learning arcs;
- avoid duplicating owner-window nodes.

Required emphasis:

```text
RELATION_CATALOG
OWNERSHIP AUDIT
CROSS-WINDOW CLAIM/SOURCE TRACE
DUPLICATE-NODE / DUPLICATE-VISUAL CHECK
```

May use TREE/NODE artifacts for hub-owned content but must not copy detailed content from target owner windows.

## 5. SYSTEM QA / INTEGRATION WINDOW

Primary jobs may include:

- system-wide coverage/consistency audit;
- integration checks;
- release-candidate validation;
- cross-window graph/identifier validation;
- final system QA.

These windows are **not** forced to create `TREE.md + prompt package` unless their own Window Contract explicitly assigns content-authoring scope.

W61–W64 are expected to use system QA/integration semantics under the established architecture unless their future exact contracts state otherwise.

## 6. Applicability matrix

| Requirement | Foundation/Method | Domain Content | Cross-Domain Hub | System QA/Integration |
|---|---|---|---|---|
| Exact Window Contract | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| TREE/NODE authoring | AS CONTRACTED | REQUIRED | HUB-OWNED ONLY | NOT DEFAULT |
| Relation Catalog | REQUIRED/AS NEEDED | REQUIRED | REQUIRED/PRIMARY | AUDIT/INTEGRATION |
| Source Register | REQUIRED | REQUIRED | REQUIRED | AUDIT SOURCES AS NEEDED |
| Academic Coverage Audit | REQUIRED IF CONTENT | REQUIRED | REQUIRED FOR HUB SCOPE | SYSTEM-SPECIFIC AUDIT |
| Academic QA Report | REQUIRED IF CONTENT | REQUIRED | REQUIRED | SYSTEM QA REPORT |
| Program-to-Visual Brief | IF VISUALS IN SCOPE | REQUIRED IF VISUALS IN SCOPE | IF VISUALS IN SCOPE | NOT DEFAULT |
| Prompt/Manifest authoring | IF CONTRACTED | IF VISUALS IN SCOPE | IF CONTRACTED | NOT DEFAULT |
| Image generation | FORBIDDEN IN CONTENT WINDOW | FORBIDDEN | FORBIDDEN | FORBIDDEN UNLESS SEPARATE PRODUCTION ROLE |

## 7. Contract rule

Every future Window Contract must state:

```text
WINDOW TYPE:
PRIMARY FUNCTION:
ACADEMIC AUTHORING PROFILE:
VISUAL AUTHORING IN SCOPE: YES/NO
SYSTEM QA / INTEGRATION DUTIES:
REQUIRED OUTPUT PROFILE:
```

A Window may not inherit requirements merely because its numeric ID falls in a broad range.