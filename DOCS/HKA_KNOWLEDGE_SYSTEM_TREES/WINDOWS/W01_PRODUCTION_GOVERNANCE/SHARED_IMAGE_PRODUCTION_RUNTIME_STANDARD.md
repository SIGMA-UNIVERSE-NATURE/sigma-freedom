---
title: "HKA — Shared Image Production Runtime Standard"
version: "1.1"
status: "DIRECTOR OPERATIONAL STANDARD — ADDITIVE"
language: "vi"
date: "2026-09-04"
---

# HKA SHARED IMAGE PRODUCTION RUNTIME STANDARD

## 1. Mục tiêu

Chuẩn này loại bỏ hoàn toàn yêu cầu người dùng phải upload lại character/logo assets hoặc production outputs bằng tay giữa các HKA Windows.

Mọi Production Window phải:

1. tự lấy **actual official brand binary bytes** từ immutable brand source;
2. verify đúng bytes;
3. truyền bytes vào image-generation engine làm visual references;
4. sau khi output tự-QA đạt, tự persist exact output qua Production Bridge vào Cloudflare staging;
5. bàn giao exact staging binaries cho Independent QA;
6. sau `QA_APPROVED`, Release Bridge canonize exact approved binaries vào Vault theo Cloudflare Amendment 1.1/1.2.

Chuẩn này không thay đổi academic content, prompt semantics, batch manifest schema hay Independent QA authority.

## 2. Immutable brand source

```text
REPOSITORY: linkcomltd-byte/sigma-universe-web
COMMIT: 2d3aa9d8418acccd39a3d263e917d4157e029e17
```

Locked files:

| Asset | Path | Git blob SHA-1 | Size bytes |
|---|---|---:|---:|
| Sigma | `assets/characters/sigma.png` | `72e29ad1ba8e71a25f7fc7d4da656a6196fdf6db` | 1094258 |
| Cricket | `assets/characters/cricket.png` | `87e30fe00beb0a122fefde8126c54d98ae7c0e08` | 1535430 |
| Little Ant | `assets/characters/little-ant.png` | `a931ae833d184ecb48f1b20bc90a8cbeee181d8c` | 1224688 |
| Professor Owl | `assets/characters/professor-owl.png` | `b5c58c5502ee39aff941769fa143f071384c3472` | 1843472 |
| Sigma logo master | `assets/logo/sigma-logo-master.jpg` | `1f19dcbb970ef414fe3a58d406d1b4b55360853e` | 225466 |
| Sigma emblem shell | `assets/logo/sigma-emblem-shell.jpg` | `91ae7ea19a3e43d0aac13ad0fa42aa4b7a37eb7e` | 355227 |

Exact motto:

```text
PEACEFUL MIND-KINDLY HEART-KEEP GROWING.
```

## 3. Mandatory auto-fetch bootstrap

Before any generation call, Production Window must execute this sequence:

1. Verify the immutable brand commit exists.
2. Query GitHub contents metadata at that exact commit for every required reference file.
3. Verify path, Git blob SHA-1 and byte size against the locked table.
4. Download binary with a binary-capable mechanism using immutable commit addressing.
5. Recompute Git blob identity:

```text
SHA1("blob " + decimal_byte_length + "\0" + file_bytes)
```

6. Verify equality to the locked Git blob SHA-1.
7. Store verified references only in run workspace/cache.
8. Pass local binary bytes/files directly into image-reference/image-conditioning inputs.
9. Generated output must never become the reference source for another asset. Reload/reuse verified official source bytes.

Mutable branch names are never acceptable brand sources.

## 4. No manual user upload dependency

Normal production must never require the user to re-upload official character/logo files.

`ASSET_REFERENCE_BLOCKED` is valid only when binary retrieval/verification genuinely fails or the generation engine cannot accept verified reference bytes.

Blocked return must include:

```text
REFERENCE_FETCH: PASS/FAIL
BLOB_VERIFY: PASS/FAIL
LOCAL_MATERIALIZATION: PASS/FAIL
GENERATION_ENGINE_REFERENCE_INGEST: PASS/FAIL
BLOCKING_CAPABILITY: <exact capability>
```

“User did not upload attachments” is not a valid blocker.

## 5. Cloudflare staging transport is active

Authority:

```text
DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_2.md
```

Production output transport bucket:

```text
hka-c4k-staging
```

Staging is temporary/non-canonical. Production must never treat it as a release or website origin.

Staging prefix:

```text
tmp/v1/windows/<WINDOW_ID>-<TREE_SLUG>/
  prompt-commit/<PROMPT_COMMIT_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

Writes are create-only/no-overwrite.

## 6. Production Bridge

Logical connected service:

```text
HKA_PRODUCTION_UPLOAD_BRIDGE
```

Expected callable actions:

```text
production_begin_run(...)
production_upload_asset(...)
production_upload_record(...)
production_complete_run(...)
```

After CLEAN MASTER and BRANDED FINAL pass Production self-QA, upload exact binaries immediately to staging with their SHA-256 and metadata. At run completion persist the production evidence package/records required by the batch contract and mark the run complete through the bridge.

The Production Window receives no raw Cloudflare credential.

If the bridge action itself is unavailable, report:

```text
STATUS: PRODUCTION_BRIDGE_BLOCKED
GENERATION: COMPLETE/NOT_STARTED/PARTIAL
LOCAL_OUTPUT_HASHES: <if any>
BRIDGE_ACTION_AVAILABLE: NO
```

Do not ask the user to move files manually.

## 7. Production and QA separation

Flow:

```text
BATCH_READY
→ PRODUCTION_CLAIMED
→ PRODUCING
→ SELF_QA
→ STAGING_PERSISTED
→ QA_PENDING
→ QA_REVIEW
```

Only Independent QA may return:

```text
QA_APPROVED
QA_REJECTED
QA_BLOCKED
```

QA reads the exact staging binaries through `HKA_QA_BRIDGE`, not user-reuploaded copies.

Required QA actions:

```text
qa_get_run(...)
qa_list_run_assets(...)
qa_get_asset(...)
qa_get_manifest(...)
qa_submit_verdict(...)
```

## 8. QA-approved release

After `QA_APPROVED`, orchestration hands the same approved run to:

```text
HKA_RELEASE_BRIDGE
```

Release Bridge reads staging + audit, copies exact approved bytes to `hka-c4k-vault`, and follows Amendment 1.1 release order exactly:

```text
1. CLEAN MASTER
2. BRANDED FINAL
3. asset metadata
4. prompts/manifests
5. production + independent QA reports
6. SHA256SUMS.txt
7. release ZIP
8. verify objects + SHA-256
9. R2_UPLOAD_RECEIPT.json
10. verify receipt
11. RELEASED.json LAST in vault prefix
12. verify marker
13. lock prefix
14. audit record to hka-c4k-audit
15. update GitHub RELEASE_INDEX.json
```

Vault prefix:

```text
v1/windows/<WINDOW_ID>-<TREE_SLUG>/
  prompt-commit/<PROMPT_COMMIT_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

No regeneration or mutation of QA-approved binaries is allowed during release.

## 9. Delivery remains WEB_APPROVED-only

`hka-c4k-delivery` is not automatically populated merely because QA passes or Vault reaches `R2_VERIFIED`.

Website delivery requires:

```text
R2_VERIFIED + RELEASED + WEB_APPROVED
```

Only website-consumable branded assets/metadata may then move to delivery. CLEAN MASTER never moves to delivery.

## 10. Rejected runs

For `QA_REJECTED`:

- preserve staging run under its immutable Run ID according to staging retention policy;
- preserve QA audit report;
- no Vault write;
- no Delivery write;
- no release marker;
- next attempt uses a new Run ID.

## 11. Default inheritance

All future HKA Image Production Windows inherit this runtime standard by immutable commit reference. Window-specific prompts add only IDs, SHAs, asset list, companion requirements and output locks. They must not reintroduce manual brand upload or manual production-file transfer.
