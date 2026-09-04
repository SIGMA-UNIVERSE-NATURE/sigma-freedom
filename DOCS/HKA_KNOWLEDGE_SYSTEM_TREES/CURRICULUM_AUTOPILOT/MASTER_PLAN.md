# HKA Curriculum Autopilot — Master Plan

Status: ACTIVE
Canonical tree: `DOCS/HKA_KNOWLEDGE_SYSTEM_TREES.md`
Canonical tree commit: `fc799bf1104ab6352710e1801777a971b5179995`
Governance base: `b2c6b8dacfb425c5e6d260176ed879fb75da6dae`

## Non-negotiable production order

HKA is built in four locked phases. Later phases MUST NOT start early.

1. `PHASE_A_CURRICULUM`
   - Complete the academic/curriculum architecture for all six canonical HKA branches.
   - Produce nodes, claims, sources, prerequisites, D1-D4 depth paths, age/presentation paths, learning objectives, lesson sequencing, cross-links, misconception/limit records, certainty labels, and duplicate controls.
   - No image prompts. No image generation.

2. `PHASE_B_LESSON_SPEC`
   - Starts only after every canonical branch is `ACADEMIC_LOCKED` and the global cross-tree audit passes.
   - Produce complete lesson records and website mapping.
   - No image generation.

3. `PHASE_C_VISUAL_PROMPTS`
   - Starts only after the global lesson registry is `LESSON_LOCKED`.
   - Produce visual descriptions and exact image prompts, with duplicate prevention against the complete lesson corpus.
   - No image generation.

4. `PHASE_D_IMAGE_PRODUCTION`
   - Starts only after all required visual prompts are `PROMPT_LOCKED`.
   - HKA_AUTOPILOT generates images, writes R2 staging, invokes Independent QA, promotes approved masters to vault, optimizes delivery derivatives, and updates website mappings.

## Canonical branches

1. B1 — QUY LUẬT — Quy luật & Thực tại
2. B2 — SỰ SỐNG — Sự sống, Sức khỏe & Tâm trí
3. B3 — KẾT NỐI — Hệ thống, Thiết kế & Kết nối
4. B4 — THỜI GIAN — Thời gian, Nơi chốn & Tương lai
5. B5 — BIỂU ĐẠT — Ngôn ngữ, Biểu đạt & Ý nghĩa
6. B6 — CÙNG TỒN TẠI — Cùng tồn tại, Lựa chọn & Công lý

## Branch completion rule

A branch may be marked `ACADEMIC_LOCKED` only when all of its canonical subbranches have completed authoring and a branch integration audit has passed.

Each knowledge unit must be traceable as:

`NODE_ID -> CLAIM_ID -> SOURCE_ID -> PREREQUISITES -> DEPTH(D1-D4) -> LEARNING_OBJECTIVE -> LESSON_SLOT`

Age is a presentation/pathway attribute, not a replacement for D1-D4 depth.

## Duplicate rule

Duplicate detection is semantic, not lexical. Repeated words across the World Tree are allowed only when their epistemic role is different.

The minimum duplicate key is:

`NODE + CLAIM + LEARNING_OBJECTIVE + CONTEXT + VISUAL_JOB`

During Phases A and B, `VISUAL_JOB` may remain null. During Phase C it becomes mandatory for visual assets.

## Window independence rule

No ChatGPT window is authoritative memory.

Every window MUST bootstrap from GitHub state, exact accepted commits, and predecessor artifacts. Every completed window MUST write a machine-readable result and handoff. A new window MUST be able to continue with zero access to prior chat history.

## Failure rule

If a window dies before an accepted completion commit, the replacement window resumes from the last accepted checkpoint. It MUST NOT infer completion from chat text.

## Current execution

Current phase: `PHASE_A_CURRICULUM`
Current branch: `B1`
Current window: `C01-W01-B1-ARCHITECTURE`

Image prompt authoring: DISABLED
Image production: DISABLED
Website publication: DISABLED
