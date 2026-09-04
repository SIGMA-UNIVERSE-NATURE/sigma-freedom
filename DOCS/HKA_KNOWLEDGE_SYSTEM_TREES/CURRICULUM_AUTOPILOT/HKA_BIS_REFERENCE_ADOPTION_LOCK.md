# HKA BIS Reference Adoption Lock

Status: `REFERENCE_ADOPTED_WITH_OVERRIDES`

Purpose: preserve useful identity/quality lessons from the earlier BIS Sigma production package without importing obsolete BIS curriculum or production structure into HKA.

## 1. Reference package examined

User-supplied archive: `bộ sigma tieu chuan.zip`

Archive SHA-256:
`ab0921b50daaf169f9362716aa7174b1c462366cb905910d11de602d874149fb`

The package contains ten BIS V2.0 PDFs: Foundation, Runtime, Master Production Standard, Product Standard, Lesson Standard, Episode Standard, Poster Standard, Cinematic Standard, Quality Standard and Living Manifest.

This archive is **reference evidence only**. It is not a canonical HKA curriculum source and does not override any current HKA canonical document.

## 2. Authority and override rule

For HKA, current canonical authority remains:

1. HKA World Tree and current higher-version amendments.
2. `DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md`.
3. Current HKA production/pipeline standards and schemas.
4. This BIS reference adoption document.
5. BIS V2.0 reference PDFs.

If a BIS rule conflicts with current HKA, **HKA wins**.

## 3. What HKA inherits from BIS

HKA preserves the following identity principles:

- Sigma identity must remain recognizable and consistent.
- Official characters must come from an immutable Character/Brand source, never from model invention.
- Official motto is a locked brand element.
- Production should actively prevent meaningless repetition.
- Publication quality must include truth, completeness, understandability, beauty, consistency and no accidental repetition.

The old BIS anti-repetition statements (`No Repeated Scene`, `No Repeated Camera`, `No Repeated Environment`) are retained as **duplicate-risk signals**, not literal universal bans. HKA may intentionally reuse an environment or camera relationship where pedagogically necessary; what is forbidden is repeated learning meaning or visually redundant production without a distinct learning job.

## 4. What HKA does NOT inherit from BIS

The following BIS-specific structure is not canonical for HKA:

- fixed `1 Episode = 7 scenes`;
- fixed BIS episode/lesson hierarchy;
- fixed `9:16` production ratio;
- BIS-specific restrictions on which episode positions may show characters;
- any BIS curriculum taxonomy that conflicts with HKA World Tree;
- any rule that forces image production before HKA curriculum/lesson/prompt locks.

HKA follows `HKA_PIPELINE_CANONICAL.json` instead.

## 5. Current HKA official brand lock

Canonical source:
`DOCS/HKA_CINEMATIC_4K_BRAND_ASSET_LOCK.md`

Brand repository:
`linkcomltd-byte/sigma-universe-web`

Immutable brand commit:
`2d3aa9d8418acccd39a3d263e917d4157e029e17`

Official character masters:

- Sigma: `assets/characters/sigma.png`
- Cricket: `assets/characters/cricket.png`
- Little Ant: `assets/characters/little-ant.png`
- Professor Owl: `assets/characters/professor-owl.png`

Official logo master:
`assets/logo/sigma-logo-master.jpg`

Official compact emblem, only where specifically authorized:
`assets/logo/sigma-emblem-shell.jpg`

Exact HKA motto:

`PEACEFUL MIND-KINDLY HEART-KEEP GROWING.`

The BIS wording is historical reference. The exact HKA motto above is authoritative for all current HKA branded finals.

## 6. Mandatory BRAND GATE

GPT/image models are **never responsible for remembering, spelling or drawing the official logo or motto**.

Branding is deterministic post-production.

Every visual asset that reaches production must have two distinct outputs:

1. `CLEAN_MASTER` - generated/edited educational image without model-generated official logo or motto.
2. `BRANDED_FINAL` - deterministic composition of the approved CLEAN_MASTER with the official logo master and exact official motto.

A model may not be asked to recreate the logo or render the motto text.

### Hard failure conditions

An asset must enter `BRAND_GATE_FAILED` and cannot advance if any of the following is true:

- BRANDED_FINAL is absent;
- official logo is absent from BRANDED_FINAL;
- official motto is absent from BRANDED_FINAL;
- motto differs by any character, hyphen or terminal period;
- logo source is not the locked logo asset;
- logo is redrawn, distorted, recolored or cropped outside an authorized deterministic layout;
- provenance does not record the brand repository commit and exact asset path;
- CLEAN_MASTER is missing;
- CLEAN_MASTER and BRANDED_FINAL hashes are not recorded separately.

## 7. Required stage enforcement

### PROMPTS

Each asset record must declare:

- exact character master path(s), when characters are required;
- exact brand commit;
- logo policy: `DETERMINISTIC_POST_ONLY`;
- motto policy: `DETERMINISTIC_POST_ONLY`;
- brand-safe placement zone;
- clean-master requirement;
- branded-final requirement.

### PROMPT_LOCKED

Prompt lock cannot pass if any production-bound asset lacks the brand fields above.

### IMAGE_PRODUCTION

Generation AI creates only the CLEAN_MASTER educational scene. A deterministic brand compositor then creates BRANDED_FINAL from the locked logo and motto.

A successful image generation by itself is **not** `PRODUCTION_COMPLETE`.

### R2_STAGING

Staging completion requires both CLEAN_MASTER and BRANDED_FINAL plus separate SHA-256 values and brand provenance.

### INDEPENDENT_QA

Independent QA must explicitly verify brand integrity in addition to academic/visual quality. `QA_APPROVED` is impossible while `BRAND_GATE_FAILED` is true.

QA must not trust model-generated text as evidence of the official motto. Brand provenance and deterministic compositor output are authoritative.

### VAULT / WEB_OPTIMIZE / DELIVERY

Vault receives only QA-approved branded finals and their clean masters/provenance as required by the current release standard. Web optimization derives website assets only from verified vault masters. Website never reconstructs the official logo or motto using generative AI.

## 8. Character-reference gate

Where an HKA lesson specifies a companion character, Generation AI must receive the exact locked PNG reference(s) and the manifest must record the corresponding locked Git blob identity.

A missing required character reference is `REFERENCE_GATE_FAILED`, not permission to improvise a similar character.

Character use is pedagogical, not decorative. No lesson is forced to include a character unless its locked lesson/visual specification requires one.

## 9. Director rule

Brand omissions are deterministic production defects, not creative-review questions.

If logo/motto are missing or malformed, the system fixes deterministic branding and re-verifies. It does **not** waste a full GPT regeneration.

This lock exists specifically to ensure that model forgetfulness cannot remove Sigma identity from publication-ready HKA assets.
