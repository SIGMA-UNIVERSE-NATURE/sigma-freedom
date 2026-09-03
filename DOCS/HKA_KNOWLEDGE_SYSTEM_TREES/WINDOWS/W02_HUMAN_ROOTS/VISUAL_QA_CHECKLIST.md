---
title: "HKA W02 — Visual QA Checklist"
version: "2.0"
status: "PROMPT_LOCK_PASS / PRE-PRODUCTION_REFERENCE"
date: "2026-09-04"
---

# VISUAL QA CHECKLIST

## 1. Prompt-lock QA completed in W02

```text
ACADEMIC CONTENT COMMIT: e900d3b623c27f6d4a0fe2750fa499295788776e
PROMPT CONTENT AUTHORING COMMIT: 65c852bfd12adc94745c65a5c8e900c40ef501c5
SELECTED PACKAGE: P18
ASSET RECORDS: 18/18
NORMALIZED A–J RESOLUTION: PASS — each asset-specific A–J block resolves with G-W02-PROMPT-2.0; no required template field is semantically omitted
SHA-256 CANONICALIZATION: PASS — 18/18 recomputed after omitting the hash line itself
ASSET → VCU → NODE → CLAIM → SOURCE TRACE: PASS — 18/18
CANONICAL ROOT CONCEPT COVERAGE: PASS — 21/21
UNSUPPORTED HIGH-RISK VISUAL CLAIMS: 0
DUPLICATE VISUAL JOBS: 0
DECORATIVE-ONLY ASSETS: 0
MODEL/REALITY/RECONSTRUCTION DISCLOSURE: PASS — 18/18
MODEL-GENERATED LOGO/MOTTO/CRITICAL TEXT REQUESTS: 0
IMAGE RUNS EXECUTED BY W02: 0
```

The prompt hashes in `VISUAL_PRODUCTION_MANIFEST.csv` were recomputed from the exact asset-specific A–J block stored in the required batch `BATCH_PROMPTS.md`, UTF-8/LF, trailing whitespace removed, no BOM, with the `PROMPT SHA-256:` line omitted. Each block resolves inherited static fields through `G-W02-PROMPT-2.0` in `VISUAL_PROMPTS_CINEMATIC_4K.md`. Hash and trace checks passed before final lock.

## 2. Required pre-run check for every future asset

### Academic
- [ ] Asset ID, VCU, Node IDs, Claim IDs, Source IDs and prompt hash match the locked manifest.
- [ ] Output shows no stronger conclusion than the mapped claims.
- [ ] Certainty, claim type and model/reconstruction boundary remain honest.
- [ ] No universal-body, universal-face, fixed-identity, cultural-stereotype, free-will-proof, memory-camera, fairness=equal, conflict=violence, responsibility-collapse or scenario=prediction error.

### Pedagogy
- [ ] Exactly one primary learning objective is visually recoverable.
- [ ] The image is necessary for the declared learning job.
- [ ] Audience expression changes presentation, not academic truth.
- [ ] A recurrent concept has a real D/epistemic delta rather than an age/style-only variation.

### Human representation
- [ ] Diversity without tokenism or a single default body/family/community/worldview.
- [ ] Disability, ageing, care, conflict and identity are shown with dignity.
- [ ] No demographic trait is used as a cue for guilt, merit, need, culture or emotional state.

### Epistemic representation
- [ ] Documentary reality contains only directly observable elements.
- [ ] Conceptual/scientific models have visible boundaries.
- [ ] Historical reconstruction contains no unverified period-specific detail.
- [ ] Scientific visualization uses scale cues and no unsupported causal arrows.
- [ ] Research posters contain no model-generated factual text/data/citations.

### Character & brand
- [ ] Exact official PNG master used from brand commit `2d3aa9d8418acccd39a3d263e917d4157e029e17`.
- [ ] HERO contains all four official characters.
- [ ] Companion role serves the declared academic function and never substitutes for evidence.
- [ ] Logo/MOTTO are not model-generated.
- [ ] Official logo is composited only from `assets/logo/sigma-logo-master.jpg`.
- [ ] Exact post-production motto is `PEACEFUL MIND-KINDLY HEART-KEEP GROWING.`

### Technical
- [ ] 0001–0016: 3840×2160, 16:9; 0017–0018: 2160×3840, 9:16.
- [ ] sRGB, lossless PNG.
- [ ] Clean master contains no branding/readable generated text.
- [ ] Filenames match manifest exactly.
- [ ] Color is not the only semantic channel.
- [ ] Safe areas do not cover evidence/method/source regions.

## 3. B00 production gate

In any later image-production Window:

1. Run only B00 assets 0001 and 0002 first.
2. Director reviews the actual outputs.
3. Independent image QA must mark B00 `QA_APPROVED`.
4. Only then may B01–B03 image generation begin.
5. Any prompt-semantic change invalidates the old hash and requires a new prompt-record version/hash.

W02 has prepared B00–B03 prompt/manifests but has **not** executed these production steps.

## 4. Final W02 visual-authoring decision

```text
DIRECTOR VISUAL GATE: PASS — prompt/manifest authoring scope
READY FOR FUTURE B00 PILOT: YES — handoff only
IMAGE PRODUCTION AUTHORIZED BY W02: NO
INDEPENDENT IMAGE-OUTPUT QA EXECUTED: NO — no output exists by instruction
R2 UPLOAD: NO
MERGE: NO
WEBSITE DEPLOY: NO
```
