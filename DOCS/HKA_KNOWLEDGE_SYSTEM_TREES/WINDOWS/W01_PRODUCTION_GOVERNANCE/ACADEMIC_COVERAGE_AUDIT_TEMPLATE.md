---
title: "HKA Academic Coverage Audit Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# HKA ACADEMIC COVERAGE AUDIT

Durable artifact required for applicable content windows before Director Academic Gate.

## 1. Identity

```text
WINDOW ID:
WINDOW TYPE:
TREE ID:
WINDOW CONTRACT SHA:
ACADEMIC CONTENT COMMIT SHA:
TREE PATH:
NODE CATALOG PATH:
RELATION CATALOG PATH:
SOURCE REGISTER PATH:
```

## 2. Mandatory branch coverage

| Mandatory Branch | Required by Contract | Core Nodes | Methods/Evidence | Misconceptions | D1–D4 | Sources | Status |
|---|---|---:|---|---|---|---|---|

```text
MANDATORY BRANCH COVERAGE: <percent>
REQUIRED PASS: 100%
```

## 3. External curriculum / classification mapping

Khi Window Contract yêu cầu mapping:

| External Framework | Required Area/Code | HKA Node IDs | Mapping Type | Gap |
|---|---|---|---|---|

```text
UNRESOLVED REQUIRED EXTERNAL-MAPPING GAPS: 0
```

Nếu không áp dụng, ghi `NOT APPLICABLE — reason`.

## 4. Semantic duplicate-node audit

| Node A | Node B | Overlap | Decision: DISTINCT / MERGE / CROSS-LINK | Rationale |
|---|---|---|---|---|

```text
UNRESOLVED SEMANTIC DUPLICATE NODES: 0
```

## 5. Graph integrity

```text
TOTAL NODES:
ORPHAN NODES:
MISSING PREREQUISITE TARGETS:
PREREQUISITE CYCLES:
DOCUMENTED CO-REQUISITE EXCEPTIONS:
ENTRY POINT NODES:
UNREACHABLE REQUIRED NODES:
```

Required pass:

```text
ORPHAN NODES = 0 unless explicitly justified
MISSING PREREQUISITE TARGETS = 0
PREREQUISITE CYCLES = 0 except documented co-requisite semantics
UNREACHABLE REQUIRED NODES = 0
```

## 6. Claim/source coverage

```text
MATERIAL CLAIM IDS:
CLAIMS WITH FIT SOURCE MAP:
CLAIM-TO-SOURCE COVERAGE:
HIGH-RISK CLAIMS:
HIGH-RISK CLAIMS CROSS-CHECKED:
UNSUPPORTED HIGH-RISK CLAIMS:
UNRESOLVED RETRACTION/SUPERSESSION DEPENDENCIES:
```

Required pass:

```text
UNSUPPORTED HIGH-RISK CLAIMS = 0
```

## 7. Epistemic integrity

```text
CLAIMS WITH CERTAINTY CLASSIFICATION:
CLAIMS WITH CONTENT CLASS:
DEBATED/OPEN ITEMS PRESENTED AS SETTLED: 0
MODEL STATUS CONFLATED WITH CERTAINTY: 0
NORMATIVE STATUS CONFLATED WITH CERTAINTY: 0
```

## 8. D1–D4 progression

| Core Node/Concept | D1 | D2 | D3 | D4 | Substantive progression? |
|---|---|---|---|---|---|

```text
D1-D4 PLACEHOLDER-ONLY RECORDS: 0
```

## 9. Misconception coverage

```text
HIGH-RISK MISCONCEPTIONS IDENTIFIED:
HIGH-RISK MISCONCEPTIONS WITH COUNTERMEASURE:
UNRESOLVED HIGH-RISK MISCONCEPTIONS:
```

## 10. Ownership and cross-window conflicts

| Node/Relation | Claimed Owner | Other Window | Conflict | Resolution |
|---|---|---|---|---|

```text
UNRESOLVED CROSS-WINDOW OWNERSHIP CONFLICTS: 0
```

## 11. Expert-review items

| Item ID | Domain | Reason | Reviewer Needed | Status |
|---|---|---|---|---|

Unresolved expert-review items that affect material claims must block academic lock unless Window Contract explicitly permits a later gate.

## 12. Density/economy audit

```text
COMPRESSION TEST: PASS/FAIL
EXPANSION TEST: PASS/FAIL
SHORT-CONTENT REVIEW TRIGGERS RESOLVED: YES/NO
LONG-CONTENT / FLAT-FANOUT TRIGGERS RESOLVED: YES/NO
TRIVIA FRAGMENTATION: 0 / <count>
```

## 13. Result

```text
MANDATORY COVERAGE: PASS/FAIL
GRAPH INTEGRITY: PASS/FAIL
CLAIM/SOURCE COVERAGE: PASS/FAIL
EPISTEMIC INTEGRITY: PASS/FAIL
D1-D4 PROGRESSION: PASS/FAIL
MISCONCEPTION COVERAGE: PASS/FAIL
OWNERSHIP: PASS/FAIL
EXPERT-REVIEW BLOCKERS: 0 / <count>
ACADEMIC COVERAGE AUDIT: PASS / RETURN / BLOCKED
```