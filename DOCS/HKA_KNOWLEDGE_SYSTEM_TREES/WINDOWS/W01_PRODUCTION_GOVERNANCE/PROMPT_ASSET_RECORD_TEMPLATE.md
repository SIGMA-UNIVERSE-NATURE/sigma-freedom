---
title: "HKA — Prompt Asset Record Template"
version: "1.0"
status: "REFERENCE TEMPLATE"
language: "vi"
date: "2026-09-03"
---

# HKA PROMPT ASSET RECORD TEMPLATE

Mỗi Asset ID phải có đúng một hồ sơ hoàn chỉnh theo cấu trúc dưới đây. Không được xóa trường; trường không áp dụng phải ghi `NOT APPLICABLE — <reason>`.

```text
────────────────────────────────────────────────────────────────────
A. IDENTITY & TRACEABILITY
────────────────────────────────────────────────────────────────────

ASSET ID:
WINDOW ID:
TREE ID:
TREE / BRANCH / NODE IDS:
VISUAL COVERAGE UNIT ID:
BATCH ID:
RUN ID PLANNED:
PROMPT RECORD VERSION:
PROMPT SHA-256:
PROMPT CONTENT COMMIT SHA:
BRAND ASSET COMMIT SHA:

────────────────────────────────────────────────────────────────────
B. PEDAGOGICAL CONTRACT
────────────────────────────────────────────────────────────────────

TITLE:
SINGLE LEARNING OBJECTIVE:
WHY AN IMAGE IS NECESSARY:
PRIMARY AUDIENCE: UNIVERSAL / A1_5_8 / A2_9_12 / A3_13_15 / A4_16_18 / A5_19_24 / RESEARCH
ACADEMIC DEPTH: D1 / D2 / D3 / D4 / MULTI_DEPTH
PRIOR KNOWLEDGE ASSUMED:
WHAT THE LEARNER MUST NOTICE:
WHAT THE LEARNER SHOULD BE ABLE TO EXPLAIN AFTER VIEWING:
HIGH-RISK MISCONCEPTION ADDRESSED:
COGNITIVE LOAD LIMIT:
SENSITIVITY / SAFETY NOTES:

────────────────────────────────────────────────────────────────────
C. EPISTEMIC & ACADEMIC TRUTH LOCK
────────────────────────────────────────────────────────────────────

ASSET TYPE:
REPRESENTATION TYPE:
- DOCUMENTARY_REALITY
- SCIENTIFIC_RECONSTRUCTION
- HISTORICAL_RECONSTRUCTION
- SCIENTIFIC_VISUALIZATION
- CONCEPTUAL_MODEL
- HUMANISTIC_METAPHOR
- DATA_RESEARCH_POSTER

WHAT IS DIRECTLY OBSERVABLE REALITY:
WHAT IS INFERRED:
WHAT IS A MODEL:
WHAT IS A RECONSTRUCTION:
WHAT IS A METAPHOR:
ACADEMIC CLAIMS SHOWN:
ACADEMIC CLAIMS NOT SHOWN:
LEVEL OF CERTAINTY:
KNOWN LIMITATIONS:
SOURCE CHECKS:
SOURCE ACCESS DATE:
EXPERT REVIEW DOMAIN:

────────────────────────────────────────────────────────────────────
D. CHARACTER CONTRACT
────────────────────────────────────────────────────────────────────

PRIMARY COMPANION:
PRIMARY COMPANION ACADEMIC FUNCTION:
SECONDARY COMPANIONS:
SECONDARY COMPANION FUNCTIONS:
CHARACTER PLACEMENT MODE: IN_SCENE_PARTICIPANT / OBSERVER_FRAME / GUIDE_LAYER

BRAND ASSET SOURCE REPOSITORY:
linkcomltd-byte/sigma-universe-web

BRAND ASSET SOURCE COMMIT:
2d3aa9d8418acccd39a3d263e917d4157e029e17

PRIMARY COMPANION MASTER PATH:
SECONDARY COMPANION MASTER PATHS:
CHARACTER CONSISTENCY LOCKS:
CHARACTER ACTION:
CHARACTER GAZE / ATTENTION TARGET:
CHARACTER MUST NOT DO:

────────────────────────────────────────────────────────────────────
E. SCENE SPECIFICATION
────────────────────────────────────────────────────────────────────

SCENE TITLE:
LOCATION / ENVIRONMENT:
TIME / ERA / SEASON:
WEATHER / ATMOSPHERE:
PRIMARY PHENOMENON:
MANDATORY OBJECTS:
FORBIDDEN OBJECTS:
SPATIAL RELATIONS:
SIZE AND SCALE RELATIONS:
SCALE CUES:
PROCESS ORDER / TEMPORAL SEQUENCE:
CAUSE–EFFECT RELATIONS:
MATERIALS AND SURFACES:
HUMAN REPRESENTATION REQUIREMENTS:
CULTURAL / HISTORICAL ACCURACY LOCKS:
SCIENTIFIC / TECHNICAL ACCURACY LOCKS:

────────────────────────────────────────────────────────────────────
F. CINEMATIC COMPOSITION
────────────────────────────────────────────────────────────────────

CANVAS:
ASPECT RATIO:
SHOT TYPE:
CAMERA HEIGHT:
CAMERA ANGLE:
LENS / FOCAL LENGTH LOGIC:
FOREGROUND:
MIDGROUND:
BACKGROUND:
FOCAL POINT:
VISUAL READING ORDER:
DEPTH OF FIELD:
MOTION TREATMENT:
LIGHT SOURCE:
LIGHT DIRECTION:
LIGHT QUALITY:
EXPOSURE PRIORITY:
FUNCTIONAL COLOR LOGIC:
CONTRAST / ACCESSIBILITY:
EMPTY SPACE FOR WEB OVERLAY:

────────────────────────────────────────────────────────────────────
G. BRAND COMPOSITING CONTRACT
────────────────────────────────────────────────────────────────────

SIGMA LOGO MASTER PATH:
assets/logo/sigma-logo-master.jpg

COMPACT EMBLEM PATH, IF AUTHORIZED:
assets/logo/sigma-emblem-shell.jpg

EXACT MOTTO:
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.

MODEL-GENERATED LOGO ALLOWED: NO
MODEL-GENERATED MOTTO/TEXT ALLOWED: NO
LOGO PLACEMENT:
LOGO SAFE AREA:
MOTTO PLACEMENT:
MOTTO SAFE AREA:
BRAND CONTRAST REQUIREMENTS:
POST-PRODUCTION COMPOSITING NOTES:

────────────────────────────────────────────────────────────────────
H. GENERATION PROMPTS
────────────────────────────────────────────────────────────────────

PROMPT VI:
<Complete Vietnamese production prompt. It must restate all critical visual and accuracy locks without relying on the field labels above.>

PROMPT EN:
<Complete English production prompt optimized for the image-production system. It must be semantically equivalent to PROMPT VI.>

GLOBAL NEGATIVE PROMPT:
no pseudoscience, no false anatomy, no impossible physics, no incorrect molecular structure, no inaccurate historical clothing, no anachronistic objects, no misleading scale, no meaningless equations, no random letters, no generated logo, no generated motto text, no embedded captions, no watermark, no unauthorized brand mark, no copyrighted third-party character, no sensationalism, no cultural stereotype, no unnecessary gore, no cluttered composition, no distortion of the four official HKA characters

DOMAIN-SPECIFIC NEGATIVE PROMPT:

ASSET-SPECIFIC NEGATIVE PROMPT:

────────────────────────────────────────────────────────────────────
I. OUTPUT CONTRACT
────────────────────────────────────────────────────────────────────

OUTPUT SIZE:
COLOR SPACE:
MASTER FORMAT:
CLEAN MASTER FILENAME:
BRANDED FINAL FILENAME:
CLEAN MASTER REQUIREMENTS:
BRANDED FINAL REQUIREMENTS:
DERIVATIVES NOT INCLUDED:
ALT TEXT:
CAPTION:
REPRESENTATION DISCLOSURE:

────────────────────────────────────────────────────────────────────
J. OBSERVABLE ACCEPTANCE CRITERIA
────────────────────────────────────────────────────────────────────

PASS — ACADEMIC:
PASS — PEDAGOGY:
PASS — VISUAL:
PASS — CHARACTER & BRAND:
PASS — ACCESSIBILITY:
PASS — INTEGRITY:

FAIL — P0 CONDITIONS:
FAIL — P1 CONDITIONS:
FAIL — P2 CONDITIONS:
FAIL — P3 CONDITIONS:

REWORK RULE IF OUTPUT ERROR:
BLOCK RULE IF PROMPT ERROR:
```

## Quy tắc chuẩn hóa hash

`PROMPT_SHA256` phải được tính trên một canonical prompt record không chứa chính trường `PROMPT_SHA-256`. Cách chuẩn:

1. Xuất các trường A–J thành UTF-8.
2. Dùng line ending LF.
3. Xóa trailing whitespace mỗi dòng.
4. Bỏ dòng `PROMPT SHA-256:` khỏi input hash.
5. Không thêm byte-order mark.
6. Tính SHA-256 và ghi chữ thường 64 ký tự hex vào registry/manifest.

Nếu prompt thay đổi dù chỉ một ký tự có ý nghĩa, phải tính hash mới và tăng record version.

## Điều kiện từ chối hồ sơ prompt

Hồ sơ bị từ chối trước production khi:

- thiếu Asset ID hoặc dùng trùng ID;
- thiếu một learning objective chính;
- không phân biệt reality/model/reconstruction/metaphor;
- nguồn không đủ để khóa nội dung có nguy cơ cao;
- yêu cầu model tự tạo logo hoặc chữ;
- không có exact character master path;
- không quy định output filenames;
- pass/fail chỉ dùng từ cảm tính;
- prompt VI và EN mâu thuẫn;
- chứa placeholder trong bản `PROMPT_LOCKED`.
