---
title: "HKA W01 B00 — Production Handoff Authorization"
window_id: "W01"
batch_id: "HKA-W01-B00"
run_id: "HKA-W01-B00-R01"
version: "1.0"
status: "AUTHORIZED_TO_CLAIM"
language: "vi"
date: "2026-09-03"
---

# HKA-W01-B00-R01 — PRODUCTION HANDOFF AUTHORIZATION

## 1. Authorization decision

```text
AUTHORIZED ACTION:
One Image Production Window may claim and produce HKA-W01-B00-R01 only.

AUTHORIZED ASSET IDS:
HKA-VIS-W01-0001
HKA-VIS-W01-0002

AUTHORIZED IMAGE OUTPUTS:
2 CLEAN MASTER PNG
2 BRANDED FINAL PNG
TOTAL: 4 IMAGE FILES
```

This authorization does not cover B01, B02, R2 upload, merge or website deployment.

## 2. Immutable evidence

```text
REPOSITORY:
SIGMA-UNIVERSE-NATURE/sigma-freedom

EXECUTION BRANCH:
hka-tree/w01-production-governance

CANONICAL BASE COMMIT SHA:
b2c6b8dacfb425c5e6d260176ed879fb75da6dae

WINDOW CONTRACT COMMIT SHA:
7d1d77da5007029b2ef0f4af0736147d8646c1b5

PROMPT CONTENT COMMIT SHA:
04da1831a597f22c7eab5737b9b674e545b71622

FINAL MANIFEST COMMIT SHA:
7f8b57232a54e5a918fe72688337e47d52d4a47a

ARCHITECT ACCEPTANCE COMMIT SHA:
9de1016214b8bee9828de6c2ba05c739a473b068

BRAND REPOSITORY:
linkcomltd-byte/sigma-universe-web

BRAND ASSET COMMIT SHA:
2d3aa9d8418acccd39a3d263e917d4157e029e17
```

## 3. Batch source

```text
BATCH ID: HKA-W01-B00
RUN ID: HKA-W01-B00-R01
ASSET COUNT: 2

MANIFEST PATH:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/PRODUCTION/BATCHES/HKA-W01-B00/BATCH_MANIFEST.json

MANIFEST SHA-256:
d3756529d6fb5cf0239f3df53558dd1f6de365e41e64184ad9146c272314261e

BATCH PROMPTS PATH:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/PRODUCTION/BATCHES/HKA-W01-B00/BATCH_PROMPTS.md

CANONICAL PAYLOADS:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/PROMPT_HASH_PAYLOADS/HKA-VIS-W01-0001.json
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/PROMPT_HASH_PAYLOADS/HKA-VIS-W01-0002.json
```

Prompt hashes:

```text
HKA-VIS-W01-0001:
c5d839c819e5ed185a30033af26bdb5dd79d28c1db00269492ad7d6e9d5dbf38

HKA-VIS-W01-0002:
a922ea27d31b9f50803a0ebb48adf59b9fab8ee9449c81c59739d0efd7e89793
```

## 4. Official brand assets

```text
SIGMA:
assets/characters/sigma.png

CRICKET:
assets/characters/cricket.png

LITTLE ANT:
assets/characters/little-ant.png

PROFESSOR OWL:
assets/characters/professor-owl.png

LOGO MASTER:
assets/logo/sigma-logo-master.jpg

COMPACT EMBLEM:
assets/logo/sigma-emblem-shell.jpg

EXACT MOTTO:
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Asset 0001 must contain all four official Companion identities. Asset 0002 uses Sigma as the primary Companion.

## 5. Reference-asset availability gate

Before image generation, the Production Window must prove that its production system can pass the official character masters as actual visual references—not merely read their filenames or describe them from text.

If the production environment cannot load or condition on those image files, it must return:

```text
STATUS: ASSET_REFERENCE_BLOCKED
```

and must not approximate, redraw from memory or invent the characters.

Acceptable reference access includes an approved production system that can ingest the exact file bytes retrieved from the immutable brand commit. A text-only description is not sufficient for character-consistency approval.

## 6. Production rules

1. Read the exact manifest and prompt sources at the SHAs above.
2. Recompute B00 manifest SHA-256.
3. Recompute both canonical payload SHA-256 values.
4. Verify official brand file bytes are available as image references.
5. Do not edit or reinterpret prompt content.
6. Produce 0001 first and self-QA it before 0002.
7. Produce exactly one accepted CLEAN MASTER and one accepted BRANDED FINAL per Asset ID.
8. Alternative generations may exist in a temporary workspace but are not canonical outputs and must not enter the package.
9. Composite official Logo Sigma and exact MOTTO only after the clean scene passes visual and character checks.
10. Calculate SHA-256 for all four final files.
11. Create production report, self-QA report and package checksum.
12. Do not upload to Cloudflare R2.
13. Do not claim independent QA approval.

## 7. Required output filenames

```text
HKA-VIS-W01-0001_CLEAN_MASTER.png
HKA-VIS-W01-0001_BRANDED_FINAL.png
HKA-VIS-W01-0002_CLEAN_MASTER.png
HKA-VIS-W01-0002_BRANDED_FINAL.png
```

## 8. Output technical requirements

```text
RESOLUTION: 3840 × 2160
ASPECT RATIO: 16:9
MASTER FORMAT: PNG lossless
COLOR SPACE: sRGB unless the production pipeline records an approved Display-P3 workflow
MODEL-GENERATED TEXT: FORBIDDEN
MODEL-GENERATED LOGO: FORBIDDEN
```

## 9. Self-QA gates

Every asset must pass:

- Academic;
- Pedagogy;
- Visual;
- Character & Brand;
- Accessibility;
- Integrity.

Use:

```text
VISUAL_QA_CHECKLIST.md
QA_ACCEPTANCE_MATRIX.md
```

A self-QA PASS does not authorize R2 or website publication.

## 10. Production package required

The Image Production Window must return:

```text
4 image files
PRODUCTION_REPORT.md
SELF_QA_REPORT.json
SHA256SUMS.txt
HKA-W01-B00-R01_PRODUCTION.zip
Package SHA-256
PRODUCTION_STATUS.json update proposal
```

Do not commit the 4K images into Git history. Return them through an approved temporary file channel or production artifact store with a stable retrieval reference and package SHA-256.

## 11. Stop conditions

Return `PROMPT_BLOCKED` or `ASSET_REFERENCE_BLOCKED` if:

- any source SHA fails verification;
- manifest/payload hash differs;
- official visual reference files cannot be passed into the generation system;
- prompt and official character reference conflict;
- the generation tool cannot deliver 4K lossless masters;
- logo/MOTTO compositing cannot be controlled exactly;
- the environment attempts R2 upload or website deployment.

Do not lower quality or invent a workaround.

## 12. Authorized transition

```text
BATCH_READY
→ PRODUCTION_CLAIMED
```

The Production Window must first record a claim receipt before generating any image.

B01 and B02 remain:

```text
BATCH_READY — PRODUCTION NOT AUTHORIZED
```
