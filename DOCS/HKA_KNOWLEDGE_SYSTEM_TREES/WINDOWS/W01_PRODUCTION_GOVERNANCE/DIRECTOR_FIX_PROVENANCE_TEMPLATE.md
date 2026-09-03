---
title: "HKA Director Fix Provenance Template"
version: "1.0"
status: "PROPOSED REFERENCE TEMPLATE — ARCHITECT REVIEW REQUIRED"
---

# HKA DIRECTOR FIX PROVENANCE

Use whenever Director directly edits a Window-generated file after an academic content lock.

## 1. Identity

```text
FIX ID:
WINDOW ID:
DIRECTOR FIX COMMIT SHA:
SUPERSEDES ACADEMIC CONTENT COMMIT SHA:
AFFECTED FILES:
AFFECTED NODE IDS:
AFFECTED CLAIM IDS:
AFFECTED RELATION IDS:
```

## 2. Fix classification

```text
FIX CLASS:
METADATA / TYPO / IDENTIFIER / FORMATTING / NONMATERIAL CLARIFICATION / MATERIAL ACADEMIC

SOURCE IMPACT: NONE / RECHECK REQUIRED
PREREQUISITE IMPACT: NONE / CHANGED
LEARNING OBJECTIVE IMPACT: NONE / CHANGED
SCOPE IMPACT: NONE / CHANGED
VISUAL JOB IMPACT: NONE / CHANGED
```

## 3. Downstream invalidation

```text
ACADEMIC COVERAGE AUDIT INVALIDATED: YES/NO
ACADEMIC QA REPORT INVALIDATED: YES/NO
PROGRAM-TO-VISUAL BRIEF INVALIDATED: YES/NO
ACADEMIC TRUTH PACK INVALIDATED: YES/NO
PROMPT HASHES INVALIDATED: YES/NO
PROMPT CONTENT COMMIT INVALIDATED: YES/NO
FINAL MANIFEST INVALIDATED: YES/NO
PRODUCTION AUTHORIZATION INVALIDATED: YES/NO
```

Every `NO` must be justified.

## 4. Direct-fix permission rule

Director may direct-fix only bounded, objectively verifiable defects that do not materially change academic meaning, prerequisite topology, source interpretation, learning objective or canonical scope.

If any of these changes materially:

```text
MATERIAL CLAIM
PREREQUISITE
SOURCE / SOURCE INTERPRETATION
LEARNING OBJECTIVE
SCOPE / OWNERSHIP
VISUAL LEARNING JOB
```

then:

```text
DIRECTOR MUST RETURN AFFECTED SECTION TO OWNER WINDOW
→ NEW ACADEMIC CONTENT COMMIT SHA
→ RERUN COVERAGE/ACADEMIC QA AS AFFECTED
→ INVALIDATE DOWNSTREAM VISUAL/PROMPT/MANIFEST LOCKS AS NECESSARY
```

## 5. Commit rule

Any byte change committed to Git has a new commit SHA. The old Academic Content Commit SHA must never continue to be presented as the commit containing the corrected bytes.

A nonmaterial fix may avoid prompt/manifest invalidation only when the changed field is outside their semantic/hash inputs and this is explicitly demonstrated.

## 6. Record

```text
FIX DESCRIPTION:
WHY DIRECT FIX IS ALLOWED:
BEFORE VALUE / LOCATION:
AFTER VALUE / LOCATION:
SOURCE RECHECK EVIDENCE:
DOWNSTREAM INVALIDATION RATIONALE:
OWNER WINDOW NOTIFIED / SECTION RETURNED:
STATUS: COMPLETE / RETURNED_TO_OWNER / BLOCKED
```