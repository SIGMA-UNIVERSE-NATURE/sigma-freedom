# HKA Curriculum Autopilot — Master Plan

Status: ACTIVE
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
Governance base: `b2c6b8dacfb425c5e6d260176ed879fb75da6dae`
Canonical pipeline: `CURRICULUM_AUTOPILOT/HKA_PIPELINE_CANONICAL.json`
Brand asset lock: `DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md`
BIS reference adoption lock: `CURRICULUM_AUTOPILOT/HKA_BIS_REFERENCE_ADOPTION_LOCK.md`

## Canonical production order — no stage skipping

```text
KNOWLEDGE
↓
CURRICULUM
↓
ACADEMIC_LOCKED
↓
LESSON_REGISTRY
↓
LESSON_REGISTRY_LOCKED
↓
PROMPTS
↓
PROMPT_LOCKED
↓
IMAGE_PRODUCTION
↓
R2 STAGING
↓
INDEPENDENT QA
↓
VAULT
↓
WEB OPTIMIZE
↓
DELIVERY
↓
WEBSITE UPDATE
```

This order is mandatory. A later stage MUST NOT start until the previous stage's exit gate is durably recorded as PASS/LOCKED.

## Stage responsibilities

### KNOWLEDGE
The HKA World Tree is the canonical knowledge architecture. It is read from the exact canonical commit and is not reconstructed from chat memory.

### CURRICULUM
Complete all six canonical HKA branches before global academic lock. Produce stable nodes/claims/sources, prerequisites, D1-D4 paths, age/presentation paths, learning objectives, lesson sequencing intent, cross-links, misconceptions/limits, certainty labels and semantic duplicate controls.

Branch-level locks are allowed as internal checkpoints, but they do NOT unlock Lesson Registry. Only the global `ACADEMIC_LOCKED` gate does.

### ACADEMIC_LOCKED
Requires all six branches complete plus global cross-tree coverage, prerequisite and semantic duplicate audits PASS. This creates the immutable academic input for lesson authoring.

### LESSON_REGISTRY
Author complete lesson records from the academic lock. Each lesson must have stable IDs and exact mapping intent, including program/path/age presentation metadata and website target metadata. No visual prompt authoring yet.

### LESSON_REGISTRY_LOCKED
Requires global lesson coverage, prerequisite, sequencing, age/path and duplicate audits PASS. Only this lock enables visual prompt authoring.

### PROMPTS
Author visual descriptions and exact prompts only from locked lesson records. Every visual job must have a distinct learning purpose and be checked against the full corpus for semantic and visual duplication.

Every production-bound visual record must also carry the exact locked character references when required, exact brand commit, brand-safe placement, and the policies:

`LOGO = DETERMINISTIC_POST_ONLY`

`MOTTO = DETERMINISTIC_POST_ONLY`

### PROMPT_LOCKED
Requires prompt integrity, global visual duplicate audit and mandatory brand-field audit PASS. Only this lock enables image production.

### IMAGE_PRODUCTION
`HKA_AUTOPILOT` invokes Generation AI from locked prompts and official references. Chat windows are not on the production critical path.

Generation AI creates the educational `CLEAN_MASTER`. It must not draw the official Sigma logo or generate the official motto text. A deterministic compositor creates `BRANDED_FINAL` using the locked logo source and exact canonical motto.

A generated CLEAN_MASTER alone is not production complete.

### R2 STAGING
Both CLEAN_MASTER and BRANDED_FINAL plus separate hashes and provenance are written create-only to Cloudflare R2 staging and read-back/checksum verified.

### INDEPENDENT QA
Independent QA AI reads exact staging binaries. It checks academic, visual, technical and brand integrity. A missing/malformed official logo or motto is `BRAND_GATE_FAILED`; such an asset cannot receive `QA_APPROVED`.

### VAULT
Only approved exact binaries are promoted to canonical R2 vault with release verification and immutable provenance.

### WEB OPTIMIZE
Create web derivatives only from verified vault masters. Optimization must preserve required visual quality and official branding and must never overwrite the canonical master or reconstruct branding generatively.

### DELIVERY
Store approved website-ready derivatives plus release metadata in R2 delivery. Website must not read staging or vault directly.

### WEBSITE UPDATE
Publish by locked mapping only:

`ASSET_ID -> LESSON_ID -> PROGRAM/PATH -> AGE/PRESENTATION -> WEBSITE_SLOT`

No placement by guesswork.

## Brand identity inheritance

The earlier BIS Sigma standards are retained as historical/reference evidence only. HKA does not inherit BIS episode structure, fixed 7-scene design, fixed 9:16 ratio or BIS curriculum taxonomy.

Useful identity principles are retained under the current HKA Brand Asset Lock: official Sigma characters, official logo, official motto and anti-repetition discipline.

Exact current HKA motto:

`PEACEFUL MIND-KINDLY HEART-KEEP GROWING.`

The image model is never trusted to remember this text or recreate the logo. Missing branding is a deterministic post-production defect and must be repaired without wasting a new full image render when the CLEAN_MASTER itself is valid.

## Canonical branches

1. B1 — QUY LUẬT — Quy luật & Thực tại
2. B2 — SỰ SỐNG — Sự sống, Sức khỏe & Tâm trí
3. B3 — KẾT NỐI — Hệ thống, Thiết kế & Kết nối
4. B4 — THỜI GIAN — Thời gian, Nơi chốn & Tương lai
5. B5 — BIỂU ĐẠT — Ngôn ngữ, Biểu đạt & Ý nghĩa
6. B6 — CÙNG TỒN TẠI — Cùng tồn tại, Lựa chọn & Công lý

## Academic traceability

Each knowledge unit must remain traceable as:

`NODE_ID -> CLAIM_ID -> SOURCE_ID -> PREREQUISITES -> DEPTH(D1-D4) -> LEARNING_OBJECTIVE -> LESSON_SLOT`

Age is a presentation/pathway attribute, not a replacement for D1-D4 depth.

## Duplicate control

Duplicate detection is semantic, not lexical. The minimum identity comparison is:

`NODE + CLAIM + LEARNING_OBJECTIVE + CONTEXT + VISUAL_JOB`

During Knowledge/Curriculum and Lesson Registry, `VISUAL_JOB` may be null. During Prompts it becomes mandatory for any image-bearing lesson.

Older BIS rules such as `No Repeated Scene`, `No Repeated Camera` and `No Repeated Environment` are treated as duplicate-risk signals, not universal bans. Intentional continuity is permitted only when the visual/learning job is genuinely different.

## Window independence and recovery

No ChatGPT window is authoritative project memory. Every window bootstraps from GitHub state, exact accepted commits and predecessor artifacts. Every completed unit writes `RESULT.json`, checkpoint data and `next_action`.

If a window dies, its replacement resumes from the last accepted checkpoint. It MUST NOT infer completion from chat history and MUST NOT renumber accepted IDs.

Large scopes must be partitioned into bounded child windows before detailed authoring. Each child has an independent PASS checkpoint so a dead long window cannot erase completed work.

## Current execution

Current canonical stage: `CURRICULUM`
Current branch: `B1`
Current window: `C01-W01-B1-ARCHITECTURE`

`KNOWLEDGE` input exists at the canonical tree commit above.
`ACADEMIC_LOCKED`: NOT YET.
`LESSON_REGISTRY`: GATED.
`PROMPTS`: GATED.
`IMAGE_PRODUCTION`: GATED.
`WEBSITE_UPDATE`: GATED.
