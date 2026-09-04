---
title: "HKA W02 B00 — Production Handoff Authorization"
window_id: "W02"
batch_id: "HKA-W02-B00"
run_id: "HKA-W02-B00-R01"
version: "1.1"
status: "AUTHORIZED_TO_CLAIM — AUTO_REFERENCE_RUNTIME"
language: "vi"
date: "2026-09-04"
---

# HKA-W02-B00-R01 — PRODUCTION HANDOFF AUTHORIZATION

## 1. Authorization decision

```text
ACADEMIC PROGRAM: PASS
VISUAL / PROMPT CONTENT: PASS
B00 PRODUCTION HANDOFF: PASS
DIRECTOR ACCEPTED FOR B00 IMAGE PRODUCTION: YES
```

Authorized only:

```text
HKA-VIS-W02-0001
HKA-VIS-W02-0002
```

Outputs:

```text
2 CLEAN MASTER PNG
2 BRANDED FINAL PNG
TOTAL: 4 canonical image files
```

B01–B03 remain closed.

## 2. Immutable evidence

```text
REPOSITORY: SIGMA-UNIVERSE-NATURE/sigma-freedom
EXECUTION BRANCH: hka-tree/w02-human-roots
WINDOW CONTRACT COMMIT: a8d8a2a6a23bface2f2116e6f2337201be806ad2
W02 EXECUTION PROMPT COMMIT: 690873b30784233b44e19a8d37b1ae1c52741e87
ACADEMIC CONTENT COMMIT: e900d3b623c27f6d4a0fe2750fa499295788776e
PROMPT CONTENT COMMIT: 295f73a8e833b5a0ffb9642078514e7e3924700a
EFFECTIVE FINAL MANIFEST / INTEGRITY COMMIT: 7028f0c008bca4e8dcaea2bd878ef9210113e223
SHARED IMAGE PRODUCTION RUNTIME STANDARD COMMIT: 07dbb95d7631976caad1c8217546eb2d660dda7e
BRAND ASSET COMMIT: 2d3aa9d8418acccd39a3d263e917d4157e029e17
```

## 3. B00 source lock

```text
BATCH MANIFEST:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_MANIFEST.json

MANIFEST SHA-256:
b30f15d36d97f1b04b1dacb00072d4da2be2a59d0a9407472f1d00dc2635d60b

BATCH PROMPTS:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_PROMPTS.md

PROMPT SHA-256:
HKA-VIS-W02-0001 = ed03f468a3a59a3e460036e377cfb6407a0f767191883f49ea806ac476f6580c
HKA-VIS-W02-0002 = ca9297d02eb179523de398727733c59982fe57c168861b18106c8944e88e9195
```

## 4. Runtime binding — no manual user upload

Production must obey:

```text
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/SHARED_IMAGE_PRODUCTION_RUNTIME_STANDARD.md
@ 07dbb95d7631976caad1c8217546eb2d660dda7e
```

The Production Window must automatically fetch actual official brand bytes from immutable GitHub source and verify Git blob SHA/size before generation.

Manual user upload of Sigma/Cricket/Little Ant/Professor Owl/logo is **not required and must not be requested as the normal path**.

Locked brand blobs:

```text
Sigma           72e29ad1ba8e71a25f7fc7d4da656a6196fdf6db  1094258
Cricket         87e30fe00beb0a122fefde8126c54d98ae7c0e08  1535430
Little Ant      a931ae833d184ecb48f1b20bc90a8cbeee181d8c  1224688
Professor Owl   b5c58c5502ee39aff941769fa143f071384c3472  1843472
Sigma logo      1f19dcbb970ef414fe3a58d406d1b4b55360853e   225466
```

Previous `ASSET_REFERENCE_BLOCKED` returns caused only by missing chat attachments are superseded. No generation occurred, so Run ID remains `HKA-W02-B00-R01`.

A future `ASSET_REFERENCE_BLOCKED` is valid only with diagnostics:

```text
REFERENCE_FETCH: PASS/FAIL
BLOB_VERIFY: PASS/FAIL
GENERATION_ENGINE_REFERENCE_INGEST: PASS/FAIL
BLOCKING_CAPABILITY: <exact capability>
```

Text descriptions or model memory may never replace official binary references.

## 5. Production / QA / R2 separation

Production Window:
- generates exactly B00;
- creates self-QA + checksums + package;
- does not claim Independent QA;
- does not upload canonical package to R2.

Independent QA Window:
- reviews actual full-resolution B00 outputs;
- returns `QA_APPROVED`, `QA_REJECTED`, or `QA_BLOCKED`;
- does not modify images;
- does not upload R2.

Cloudflare Release Uploader:
- may run only after `QA_APPROVED`;
- then uploads and verifies the approved release automatically under canonical R2 pipeline Amendment 1.1.

This sequencing satisfies the requirement that finished approved images are stored in Cloudflare without manual user transfer while preserving the Independent QA gate.

## 6. Locked downstream

```text
HKA-W02-B01: CLOSED
HKA-W02-B02: CLOSED
HKA-W02-B03: CLOSED
R2 BEFORE QA_APPROVED: FORBIDDEN
R2 AFTER QA_APPROVED: RELEASE UPLOADER ELIGIBLE
MERGE: NOT AUTHORIZED
WEBSITE DEPLOY: NOT AUTHORIZED
```

B01–B03 may open only after B00 Director consistency PASS and Independent Image QA = `QA_APPROVED`.
