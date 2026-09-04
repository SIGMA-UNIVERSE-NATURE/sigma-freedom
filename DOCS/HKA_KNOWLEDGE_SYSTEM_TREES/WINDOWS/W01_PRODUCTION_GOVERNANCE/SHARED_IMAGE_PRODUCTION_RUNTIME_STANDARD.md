---
title: "HKA — Shared Image Production Runtime Standard"
version: "1.0"
status: "DIRECTOR OPERATIONAL STANDARD — ADDITIVE"
language: "vi"
date: "2026-09-04"
---

# HKA SHARED IMAGE PRODUCTION RUNTIME STANDARD

## 1. Mục tiêu

Chuẩn này loại bỏ hoàn toàn yêu cầu người dùng phải upload lại character/logo assets cho từng Image Production Window. Mọi Production Window phải tự lấy **actual binary bytes** từ immutable brand source, tự verify, rồi truyền chính bytes đó vào image-generation engine làm visual references.

Chuẩn này không thay đổi academic content, prompt semantics, batch manifest schema, Independent QA gate hay Cloudflare release order.

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
3. Verify returned path, Git blob SHA-1 and byte size against the locked table above.
4. Download the binary with a **binary-capable** mechanism, using one of these equivalent methods:
   - GitHub `download_url` returned by contents API at the immutable ref;
   - immutable `raw.githubusercontent.com/<repo>/<commit>/<path>` URL;
   - `git fetch/checkout` of the exact commit followed by local file read.
5. Verify the downloaded bytes by recomputing Git blob identity:

```text
SHA1("blob " + decimal_byte_length + "\0" + file_bytes)
```

The result must equal the locked Git blob SHA-1.
6. Store verified files only in ephemeral run workspace/cache.
7. Pass the local binary bytes/files directly into the image-generation engine's image-reference/image-conditioning inputs.
8. Generated output must never become the character reference for another asset. Reuse of the **verified official source bytes** within the same run is allowed.

A mutable branch (`main`, `master`, `latest`) is never an acceptable brand source.

## 4. No manual user upload dependency

Normal production must **never require the user to re-upload official character/logo files**.

Manual upload is not a production dependency and must not be included in window completion instructions.

`ASSET_REFERENCE_BLOCKED` is valid only when the Production Window has successfully obtained and verified the binary source, but its generation engine cannot accept local/reference image bytes, or when every binary-capable retrieval path available to that runtime fails.

A blocked return must identify exactly which capability is missing:

```text
REFERENCE_FETCH: PASS/FAIL
BLOB_VERIFY: PASS/FAIL
GENERATION_ENGINE_REFERENCE_INGEST: PASS/FAIL
BLOCKING_CAPABILITY: <exact capability>
```

Text descriptions, filenames and model memory are never substitutes for the official reference bytes.

## 5. Production and QA separation

Canonical flow remains:

```text
BATCH_READY
→ PRODUCTION_CLAIMED
→ PRODUCING
→ SELF_QA
→ QA_REVIEW
```

Production creates CLEAN MASTER + BRANDED FINAL + checksums/reports/package, but does not claim Independent QA approval.

Only an independent QA Window may return:

```text
QA_APPROVED
QA_REJECTED
QA_BLOCKED
```

## 6. Automatic Cloudflare handoff after QA_APPROVED

Once Independent QA returns `QA_APPROVED`, orchestration must immediately hand the approved package to Release Uploader. No user re-upload or manual asset transfer should be required.

Canonical buckets:

```text
hka-c4k-vault
hka-c4k-audit
hka-c4k-delivery
```

`hka-c4k-staging` is not active canonical and must not be used.

Release Uploader must follow `HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_1.md` exactly:

```text
1. Upload CLEAN MASTER objects
2. Upload BRANDED FINAL objects
3. Upload asset metadata sidecars
4. Upload prompts and manifests
5. Upload production and independent QA reports
6. Upload SHA256SUMS.txt
7. Upload batch package ZIP
8. Verify object count, metadata and SHA-256
9. Generate/upload R2_UPLOAD_RECEIPT.json
10. Verify R2_UPLOAD_RECEIPT.json
11. Upload RELEASED.json as final vault-prefix object
12. Verify RELEASED.json
13. Apply prefix lock
14. Write R2_RELEASE_AUDIT_RECORD.json to hka-c4k-audit
15. Update GitHub RELEASE_INDEX.json
```

No canonical R2 upload occurs before `QA_APPROVED`.

## 7. R2 namespace

For each approved run:

```text
v1/windows/<WINDOW_ID>-<TREE_SLUG>/
  prompt-commit/<PROMPT_COMMIT_SHA>/
  batches/<BATCH_ID>/
  runs/<RUN_ID>/
```

GitHub remains control plane. R2 remains binary asset plane. 4K masters are not committed to Git history.

## 8. Default inheritance for future production windows

All future HKA Image Production Windows should inherit this runtime standard by immutable commit reference. Window-specific execution prompts should only add:

- Window/Tree IDs;
- Batch/Run IDs;
- exact Asset IDs;
- prompt/manifest SHA locks;
- asset-specific required companions;
- output filenames and dimensions.

They must not reintroduce manual brand-asset upload steps.
