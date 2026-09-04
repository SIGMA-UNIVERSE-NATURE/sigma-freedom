---
title: "HKA W02 B00 — Production Handoff Authorization"
window_id: "W02"
batch_id: "HKA-W02-B00"
run_id: "HKA-W02-B00-R01"
version: "1.0"
status: "AUTHORIZED_TO_CLAIM"
language: "vi"
date: "2026-09-04"
---

# HKA-W02-B00-R01 — PRODUCTION HANDOFF AUTHORIZATION

## 1. Director narrow re-review decision

```text
ACADEMIC PROGRAM: PASS — unchanged from Director Review 01
VISUAL / PROMPT CONTENT: PASS — unchanged from Director Review 01
PROMPT HASH TRACE: PASS — 18/18 cross-file propagation
BATCH MANIFEST SCHEMA: PASS — 4/4
CANONICAL MANIFEST SHA-256 SIDECARS: PASS — 4/4 after Director correction
B00 PRODUCTION HANDOFF: PASS
DIRECTOR ACCEPTED FOR B00 IMAGE PRODUCTION: YES
```

Only B00 is opened. B01–B03 remain closed.

## 2. Authorized action

```text
One Image Production Window may claim and produce:
HKA-W02-B00-R01

AUTHORIZED ASSET IDS:
HKA-VIS-W02-0001
HKA-VIS-W02-0002

AUTHORIZED OUTPUTS:
2 CLEAN MASTER PNG
2 BRANDED FINAL PNG
TOTAL CANONICAL IMAGE FILES: 4
```

No other Asset ID or batch is authorized.

## 3. Immutable evidence

```text
REPOSITORY:
SIGMA-UNIVERSE-NATURE/sigma-freedom

EXECUTION BRANCH:
hka-tree/w02-human-roots

WINDOW CONTRACT COMMIT SHA:
a8d8a2a6a23bface2f2116e6f2337201be806ad2

W02 EXECUTION PROMPT COMMIT SHA:
690873b30784233b44e19a8d37b1ae1c52741e87

ACADEMIC CONTENT COMMIT SHA:
e900d3b623c27f6d4a0fe2750fa499295788776e

PROMPT CONTENT COMMIT SHA:
295f73a8e833b5a0ffb9642078514e7e3924700a

W02 FINAL HANDOFF COMMIT SHA:
f176b9fcf4692bf9a5ec5478fd19ee2091bbc84d

DIRECTOR MANIFEST-HASH CORRECTION / EFFECTIVE FINAL INTEGRITY COMMIT SHA:
7028f0c008bca4e8dcaea2bd878ef9210113e223

BRAND REPOSITORY:
linkcomltd-byte/sigma-universe-web

BRAND ASSET COMMIT SHA:
2d3aa9d8418acccd39a3d263e917d4157e029e17
```

## 4. Exact B00 sources

```text
BATCH ID: HKA-W02-B00
RUN ID: HKA-W02-B00-R01
ASSET COUNT: 2

PROMPT REGISTRY PATH:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/VISUAL_PROMPTS_CINEMATIC_4K.md
READ AT PROMPT CONTENT COMMIT:
295f73a8e833b5a0ffb9642078514e7e3924700a

BATCH PROMPTS PATH:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_PROMPTS.md
READ AT PROMPT CONTENT COMMIT:
295f73a8e833b5a0ffb9642078514e7e3924700a

BATCH MANIFEST PATH:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_MANIFEST.json
READ AT EFFECTIVE FINAL INTEGRITY COMMIT:
7028f0c008bca4e8dcaea2bd878ef9210113e223

BATCH MANIFEST SHA-256:
b30f15d36d97f1b04b1dacb00072d4da2be2a59d0a9407472f1d00dc2635d60b

PROMPT SHA-256:
HKA-VIS-W02-0001 = ed03f468a3a59a3e460036e377cfb6407a0f767191883f49ea806ac476f6580c
HKA-VIS-W02-0002 = ca9297d02eb179523de398727733c59982fe57c168861b18106c8944e88e9195
```

Manifest SHA-256 is computed from canonical JSON serialization: UTF-8, sorted keys, compact separators, no extraneous whitespace.

## 5. Official brand/reference lock

```text
SIGMA: assets/characters/sigma.png
CRICKET: assets/characters/cricket.png
LITTLE ANT: assets/characters/little-ant.png
PROFESSOR OWL: assets/characters/professor-owl.png
LOGO MASTER: assets/logo/sigma-logo-master.jpg
COMPACT EMBLEM: assets/logo/sigma-emblem-shell.jpg
EXACT MOTTO: PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

Asset 0001 requires all four official Companion identities.
Asset 0002 requires Professor Owl as primary Companion.

The production system must load the actual official character image bytes from the immutable brand commit as visual references. Filenames or text descriptions alone are insufficient.

If exact reference bytes cannot be passed to the image-generation system:

```text
STATUS: ASSET_REFERENCE_BLOCKED
```

Do not approximate or redraw from memory.

## 6. Production rules

1. Verify all immutable SHAs before generation.
2. Recompute B00 canonical manifest SHA-256 and both prompt SHA-256 values.
3. Load exact official visual references for every relevant asset.
4. Do not edit, paraphrase or reinterpret the locked prompts.
5. Produce asset 0001 first; complete self-check before starting 0002.
6. Produce CLEAN MASTER first.
7. Only after CLEAN MASTER passes, composite official logo + exact motto in controlled post-production to create BRANDED FINAL.
8. Do not let the image model generate logo, motto, captions, labels or factual text.
9. Preserve exact Asset IDs and filenames.
10. Hash all final files and create production evidence package.
11. Do not upload R2.
12. Do not claim Independent QA approval.

## 7. Required filenames

```text
HKA-VIS-W02-0001_CLEAN_MASTER.png
HKA-VIS-W02-0001_BRANDED_FINAL.png
HKA-VIS-W02-0002_CLEAN_MASTER.png
HKA-VIS-W02-0002_BRANDED_FINAL.png
```

## 8. Technical lock

```text
RESOLUTION: 3840 × 2160
ASPECT RATIO: 16:9
COLOR SPACE: sRGB
MASTER FORMAT: PNG lossless
MODEL-GENERATED READABLE TEXT: FORBIDDEN
MODEL-GENERATED LOGO: FORBIDDEN
MODEL-GENERATED MOTTO: FORBIDDEN
```

## 9. Required production return

```text
STATUS:
BATCH ID:
RUN ID:
PRODUCED ASSET IDS:
OFFICIAL REFERENCE BYTES VERIFIED: YES/NO
CLEAN MASTER FILE REFERENCES:
BRANDED FINAL FILE REFERENCES:
SHA-256 PER FILE:
SELF-QA PER ASSET:
PRODUCTION REPORT REFERENCE:
SELF-QA REPORT REFERENCE:
SHA256SUMS REFERENCE:
PACKAGE REFERENCE:
PACKAGE SHA-256:
KNOWN LIMITATIONS:
```

The production return must not claim `QA_APPROVED`.

## 10. Stop conditions

Stop with `PROMPT_BLOCKED`, `ASSET_REFERENCE_BLOCKED` or `OUTPUT_FAILED` when applicable if any immutable SHA/hash fails, official reference bytes cannot be used, prompt execution would violate its truth locks, exact branding cannot be controlled, or 4K lossless output cannot be delivered.

## 11. Locked downstream state

```text
HKA-W02-B01: CLOSED
HKA-W02-B02: CLOSED
HKA-W02-B03: CLOSED
R2 UPLOAD: NOT AUTHORIZED
MERGE: NOT AUTHORIZED
WEBSITE DEPLOY: NOT AUTHORIZED
```

B01–B03 may open only after B00 actual outputs pass Director consistency review and Independent Image QA returns `QA_APPROVED`.
