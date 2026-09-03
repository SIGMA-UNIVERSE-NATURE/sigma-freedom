---
title: "HKA Production Correction Register Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE"
---

# PRODUCTION CORRECTION REGISTER

Chỉ ghi lỗi có khả năng lặp hoặc instruction cần truyền sang IMG Unit tiếp theo. Không dùng file này làm nhật ký hội thoại.

## CORRECTION: <WXX-CORR-NNN>

```text
WINDOW ID:
BATCH ID:
AFFECTED ASSET IDS:
DETECTED RUN:
ERROR CLASS:
SEVERITY:
STATUS: OPEN / APPLIED / CLOSED
```

### Evidence

```text
OBSERVED ERROR:
WHY IT VIOLATES PROMPT / STANDARD:
SOURCE / PASS-FAIL RULE:
```

### Director correction lock

Viết câu lệnh quan sát được:

```text
MUST:
MUST NOT:
RELOAD OFFICIAL REFERENCE:
COMPOSITION / SCALE / CONTENT CORRECTION:
```

Không viết “làm đẹp hơn”, “cẩn thận hơn” hoặc “giống bản đúng”.

### Scope

```text
APPLIES TO:
- THIS ASSET ONLY
- THIS BATCH
- THIS WINDOW
- GLOBAL HKA CANDIDATE
```

Global candidate không tự động thành canonical rule; Architect review required nếu thay standard.

### Closure

```text
CORRECTED RUN:
VERIFIED BY DIRECTOR:
SAME FAILURE REPEATED: YES/NO
ROOT CAUSE REVIEW REQUIRED: YES/NO
```