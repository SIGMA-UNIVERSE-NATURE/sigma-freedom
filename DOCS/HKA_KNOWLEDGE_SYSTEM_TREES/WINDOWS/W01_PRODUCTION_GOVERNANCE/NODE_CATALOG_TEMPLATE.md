---
title: "HKA NODE_CATALOG.md Template"
version: "1.2"
status: "ARCHITECT FINALIZED REFERENCE"
---

# HKA NODE CATALOG

Mỗi node dùng đúng một record. Template này là minimum anatomy; Window có thể bổ sung field chuyên ngành nhưng không được bỏ các field material bên dưới.

---

## NODE: <NODE ID>

```text
NODE ID:
WINDOW ID:
WINDOW TYPE:
TREE ID:
PARENT NODE / BRANCH:
NODE VERSION:
STATUS: DRAFT / REVIEWED / LOCKED
TITLE:
NODE TYPE:
CONCEPT / PROCESS / MECHANISM / METHOD / EVIDENCE / CASE / DEBATE / OPEN_QUESTION / APPLICATION /
PHENOMENON / QUANTITY / LAW_PRINCIPLE / MODEL_THEORY / TOOL_PRACTICE / WORK / EVENT / PERSON / INSTITUTION / <DOMAIN_EXTENSION>
```

Node type taxonomy là extensible; extension phải có định nghĩa và không được đổi nghĩa type đã có.

### 1. Origin and knowledge contract

```text
ORIGINATING PHENOMENON / PROBLEM:
CENTRAL QUESTION:
CANONICAL DEFINITION:
CORE CLAIM / KNOWLEDGE FUNCTION:
WHY THIS NODE EXISTS:
BOUNDARY — INCLUDED:
BOUNDARY — EXCLUDED:
```

### 2. Representations

```text
REPRESENTATIONS:
- verbal / narrative:
- symbolic / mathematical, if applicable:
- diagrammatic / spatial, if applicable:
- data / documentary, if applicable:
- model / reconstruction / metaphor, if applicable:
REPRESENTATION LIMITS:
```

### 3. Prerequisites

```text
REQUIRED PREREQUISITE NODE IDS:
CO-REQUISITE NODE IDS, IF ANY:
HELPFUL PRIOR NODES:
ENTRY-POINT JUSTIFICATION:
WHAT MAY BE INTRODUCED HERE WITHOUT PRIOR FORMALISM:
```

### 4. Method of knowledge formation and evidence

```text
METHOD OF KNOWLEDGE FORMATION:
EVIDENCE TYPE:
CLAIM IDS:
SOURCE IDS:
```

Mỗi material claim phải dùng hai trục độc lập:

```text
CERTAINTY: ESTABLISHED / DEVELOPING / DEBATED / HYPOTHETICAL / UNKNOWN
CONTENT CLASS: ESTABLISHED_KNOWLEDGE / DEVELOPING_RESEARCH / ACADEMIC_DEBATE / PHILOSOPHICAL_DEBATE / HUMANISTIC_METAPHOR
```

Optional independent fields khi áp dụng:

```text
CONTEXT DEPENDENCE:
NORMATIVE STATUS:
MODEL STATUS / APPROXIMATION:
```

Model status không phải certainty level; một model có thể là ESTABLISHED.

### 5. Content

```text
KEY COMPONENTS:
PROCESS / MECHANISM:
CAUSE–EFFECT LIMITS:
EXAMPLES:
COUNTEREXAMPLES / BOUNDARY CASES:
APPLICATIONS:
```

### 6. Error, bias and limits

```text
ERROR SOURCES:
BIAS RISKS:
KNOWN LIMITATIONS:
UNCERTAINTY:
ACTIVE DEBATE:
OPEN QUESTIONS:
```

### 7. Misconceptions

| Misconception | Why wrong/incomplete | Correct model | Counterexample/evidence | Claim/Source IDs |
|---|---|---|---|---|

### 8. D1–D4 progression

```text
D1 — learner can:
D2 — learner can:
D3 — learner can:
D4 — learner can:
```

Mỗi dòng phải mô tả năng lực quan sát được; D4 không được chỉ là D3 viết khó hơn.

### 9. HKA Compass — canonical seven dimensions

La bàn HKA là một trục phản tư độc lập với bằng chứng học thuật. Không dùng La bàn để thay thế truth/evidence checks.

```text
SỰ THẬT / TRUTH:
SỰ SỐNG / LIFE:
TÍNH LIÊN KẾT / INTERCONNECTION:
PHẨM GIÁ / DIGNITY:
CÔNG BẰNG / JUSTICE:
HÒA BÌNH / PEACE:
TRÁCH NHIỆM / RESPONSIBILITY:
```

Không bắt buộc mọi node phải có tác động material ở cả bảy chiều. Với chiều không áp dụng, ghi `NOT APPLICABLE — reason`; không tự tạo liên hệ đạo đức để lấp trường.

### 10. Relations

```text
PARENT:
CHILDREN:
PREREQUISITE RELATION IDS:
OTHER IN-TREE RELATION IDS:
CROSS-TREE RELATION IDS:
```

### 11. Evidence of understanding / assessment

```text
EVIDENCE OF UNDERSTANDING:
ASSESSMENT / DEMONSTRATION TASKS:
COMMON FALSE-POSITIVE UNDERSTANDING:
TRANSFER TASK, IF APPLICABLE:
```

### 12. External curriculum / classification mappings

```text
EXTERNAL CURRICULUM MAPPINGS:
STANDARD / FRAMEWORK:
CODE / LEVEL / SECTION:
MAPPING TYPE: DIRECT / PARTIAL / CONTEXT_ONLY
NOTES:
```

Không bắt buộc mọi node phải có external mapping; khi Window Contract yêu cầu mapping, field này phải được điền có nguồn.

### 13. Visual implication

```text
VISUAL NEED: REQUIRED / USEFUL / NOT_REQUIRED
WHY:
WHAT MUST BE SEEN:
WHAT MUST NOT BE IMPLIED:
CANDIDATE REPRESENTATION TYPE:
MISCONCEPTION RISK:
CLAIM IDS THAT ANY VISUAL MUST PRESERVE:
```

### 14. Sources

```text
PRIMARY SOURCE IDS:
CROSS-CHECK SOURCE IDS:
HIGH-RISK CLAIMS FULLY MAPPED: YES/NO/NOT_APPLICABLE
```

### 15. Version history

| Version | Commit SHA | Date | Change | Affected Claim/Relation IDs | Supersedes |
|---|---|---|---|---|---|

`NODE VERSION` không thay thế version history.

### 16. Acceptance

```text
SOURCE COMPLETE: YES/NO
CLAIM-TO-SOURCE MAPPING COMPLETE: YES/NO
PREREQUISITE COMPLETE: YES/NO
PREREQUISITE CYCLE CHECK: PASS/EXEMPT_WITH_REASON/FAIL
D1-D4 COMPLETE: YES/NO
HKA COMPASS REVIEWED: YES/NO
OWNERSHIP CLEAR: YES/NO
ASSESSMENT EVIDENCE PRESENT: YES/NO
VERSION HISTORY PRESENT: YES/NO
DIRECTOR REVIEW: PASS / RETURN
```