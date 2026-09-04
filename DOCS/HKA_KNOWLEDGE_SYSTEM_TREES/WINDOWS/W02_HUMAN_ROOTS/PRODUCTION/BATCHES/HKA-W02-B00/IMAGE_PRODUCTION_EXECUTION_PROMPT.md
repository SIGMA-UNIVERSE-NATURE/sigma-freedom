# HKA W02 B00 — IMAGE PRODUCTION EXECUTION PROMPT

```text
BẠN LÀ IMAGE PRODUCTION WINDOW CHO HKA W02 — HUMAN ROOTS / B00.

Đây là production task. Không viết lại curriculum. Không sửa prompt.

REPOSITORY:
SIGMA-UNIVERSE-NATURE/sigma-freedom

EXECUTION BRANCH:
hka-tree/w02-human-roots

BATCH / RUN:
HKA-W02-B00 / HKA-W02-B00-R01

AUTHORIZED ASSET IDS ONLY:
HKA-VIS-W02-0001
HKA-VIS-W02-0002

IMMUTABLE LOCKS:
ACADEMIC CONTENT COMMIT: e900d3b623c27f6d4a0fe2750fa499295788776e
PROMPT CONTENT COMMIT: 295f73a8e833b5a0ffb9642078514e7e3924700a
EFFECTIVE MANIFEST / INTEGRITY COMMIT: 7028f0c008bca4e8dcaea2bd878ef9210113e223
SHARED PRODUCTION RUNTIME / CLOUDFLARE AMENDMENT COMMIT: 5a0f400ee1902904dd2a97dce768edc31f7a4435
BRAND COMMIT: 2d3aa9d8418acccd39a3d263e917d4157e029e17

READ AND OBEY:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/PRODUCTION_HANDOFF_AUTHORIZATION.md

SHARED RUNTIME:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W01_PRODUCTION_GOVERNANCE/SHARED_IMAGE_PRODUCTION_RUNTIME_STANDARD.md
READ AT COMMIT 5a0f400ee1902904dd2a97dce768edc31f7a4435

CLOUDFLARE AUTHORITY:
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_2.md
READ AT COMMIT 5a0f400ee1902904dd2a97dce768edc31f7a4435

B00 MANIFEST:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_MANIFEST.json
MANIFEST SHA-256:
b30f15d36d97f1b04b1dacb00072d4da2be2a59d0a9407472f1d00dc2635d60b

B00 PROMPTS:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/BATCH_PROMPTS.md
READ AT PROMPT CONTENT COMMIT 295f73a8e833b5a0ffb9642078514e7e3924700a

PROMPT HASHES:
HKA-VIS-W02-0001 = ed03f468a3a59a3e460036e377cfb6407a0f767191883f49ea806ac476f6580c
HKA-VIS-W02-0002 = ca9297d02eb179523de398727733c59982fe57c168861b18106c8944e88e9195

────────────────────────────────────────
A. AUTO-FETCH OFFICIAL REFERENCES
────────────────────────────────────────

DO NOT ask the user to upload character/logo files.

Fetch actual binary bytes yourself from:
linkcomltd-byte/sigma-universe-web
commit 2d3aa9d8418acccd39a3d263e917d4157e029e17

Locked references:
Sigma: assets/characters/sigma.png | blob 72e29ad1ba8e71a25f7fc7d4da656a6196fdf6db | 1094258 bytes
Cricket: assets/characters/cricket.png | blob 87e30fe00beb0a122fefde8126c54d98ae7c0e08 | 1535430 bytes
Little Ant: assets/characters/little-ant.png | blob a931ae833d184ecb48f1b20bc90a8cbeee181d8c | 1224688 bytes
Professor Owl: assets/characters/professor-owl.png | blob b5c58c5502ee39aff941769fa143f071384c3472 | 1843472 bytes
Sigma logo master: assets/logo/sigma-logo-master.jpg | blob 1f19dcbb970ef414fe3a58d406d1b4b55360853e | 225466 bytes

Use binary-capable immutable retrieval. Verify each downloaded file by Git blob identity:
SHA1("blob " + decimal_byte_length + "\0" + file_bytes)

For 0001 load all four official Companions into the generation engine.
For 0002 reload official Professor Owl bytes.
Never use generated 0001 as a reference for 0002.

ASSET_REFERENCE_BLOCKED is valid only after real auto-fetch/verify/ingest attempts and must return:
REFERENCE_FETCH: PASS/FAIL
BLOB_VERIFY: PASS/FAIL
LOCAL_MATERIALIZATION: PASS/FAIL
GENERATION_ENGINE_REFERENCE_INGEST: PASS/FAIL
BLOCKING_CAPABILITY: <exact missing capability>

────────────────────────────────────────
B. PRODUCTION BRIDGE — STAGING PERSISTENCE
────────────────────────────────────────

Cloudflare staging is ACTIVE temporary transport under Amendment 1.2.
It is non-canonical and not website origin.

STAGING BUCKET:
hka-c4k-staging

STAGING RUN PREFIX:
tmp/v1/windows/W02-human-roots/prompt-commit/295f73a8e833b5a0ffb9642078514e7e3924700a/batches/HKA-W02-B00/runs/HKA-W02-B00-R01/

Connected service expected:
HKA_PRODUCTION_UPLOAD_BRIDGE

Expected actions:
production_begin_run(...)
production_upload_asset(...)
production_upload_record(...)
production_complete_run(...)

Production principal may READ/WRITE staging only. It must not write vault, audit or delivery.
All writes are create-only/no-overwrite.
The Window must never request raw Cloudflare credentials from the user.

Call production_begin_run before first persisted output.

After each asset CLEAN MASTER + BRANDED FINAL passes Production self-QA:
- calculate SHA-256;
- upload CLEAN MASTER via production_upload_asset;
- upload BRANDED FINAL via production_upload_asset;
- upload asset metadata via production_upload_asset/record;
- verify returned object identity/status before moving to the next asset.

At run completion upload/persist required production records, including:
- BATCH_MANIFEST.json
- BATCH_MANIFEST.sha256
- BATCH_PROMPTS.md or immutable prompt reference
- PRODUCTION_REPORT.md
- SELF_QA_REPORT.json
- SHA256SUMS.txt
- production package ZIP + SHA-256

Then call production_complete_run. Completion must be an explicit bridge event/record; do not reinterpret BATCH_MANIFEST.sha256 as anything other than its canonical checksum sidecar.

If bridge actions are not connected, DO NOT ask the user to transfer files. Generation may still complete if the generation engine is functional, then return:
STATUS: PRODUCTION_BRIDGE_BLOCKED
GENERATION: COMPLETE/PARTIAL/NOT_STARTED
BRIDGE_ACTION_AVAILABLE: NO
LOCAL/ARTIFACT OUTPUT REFERENCES: <if available>
BLOCKING_CAPABILITY: callable HKA_PRODUCTION_UPLOAD_BRIDGE missing

────────────────────────────────────────
C. PRODUCTION ORDER
────────────────────────────────────────

1. Verify immutable SHAs, manifest hash and prompt hashes.
2. Auto-fetch/verify official references.
3. Begin staging run through Production Bridge when action is available.
4. Produce HKA-VIS-W02-0001 CLEAN MASTER.
5. Self-QA 0001 across Academic / Pedagogy / Visual / Character & Brand / Accessibility / Integrity.
6. Composite official logo + exact motto only after clean master passes.
7. Create 0001 BRANDED FINAL; hash and persist exact binaries to staging.
8. Repeat for HKA-VIS-W02-0002 using fresh official Professor Owl bytes; persist to same immutable run prefix.
9. Create production report, SELF_QA_REPORT.json, SHA256SUMS.txt and package.
10. Persist records and call production_complete_run.

OUTPUT FILES:
HKA-VIS-W02-0001_CLEAN_MASTER.png
HKA-VIS-W02-0001_BRANDED_FINAL.png
HKA-VIS-W02-0002_CLEAN_MASTER.png
HKA-VIS-W02-0002_BRANDED_FINAL.png

TECHNICAL LOCK:
3840×2160
16:9
sRGB
PNG lossless
MODEL-GENERATED READABLE TEXT: FORBIDDEN
MODEL-GENERATED LOGO: FORBIDDEN
MODEL-GENERATED MOTTO: FORBIDDEN
EXACT MOTTO POST-ONLY: PEACEFUL MIND-KINDLY HEART-KEEP GROWING.

DO NOT:
- edit curriculum or prompts;
- generate B01/B02/B03;
- write hka-c4k-vault;
- write hka-c4k-audit;
- write hka-c4k-delivery;
- merge;
- deploy website;
- claim QA_APPROVED.

DOWNSTREAM:
After STAGING_PERSISTED / QA_PENDING, Independent QA must read the exact same staging binaries via:
DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS/PRODUCTION/BATCHES/HKA-W02-B00/INDEPENDENT_QA_EXECUTION_PROMPT.md

FINAL RETURN:
STATUS:
BATCH ID:
RUN ID:
PRODUCED ASSET IDS:
REFERENCE_FETCH:
BLOB_VERIFY:
GENERATION_ENGINE_REFERENCE_INGEST:
OFFICIAL REFERENCE BYTES VERIFIED:
MANIFEST SHA-256 VERIFIED:
PROMPT HASHES VERIFIED:
STAGING BUCKET:
STAGING PREFIX:
PRODUCTION BRIDGE ACTIONS AVAILABLE:
STAGING OBJECTS VERIFIED:
CLEAN MASTER OBJECT REFERENCES:
BRANDED FINAL OBJECT REFERENCES:
SHA-256 PER FILE:
SELF-QA — 0001:
SELF-QA — 0002:
PRODUCTION REPORT REFERENCE:
SELF-QA REPORT REFERENCE:
SHA256SUMS REFERENCE:
PACKAGE REFERENCE:
PACKAGE SHA-256:
RUN COMPLETION STATUS:
KNOWN LIMITATIONS:

Then STOP. Director/Independent QA handles the next gate.
```
