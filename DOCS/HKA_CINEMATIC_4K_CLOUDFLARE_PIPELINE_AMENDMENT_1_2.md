---
title: "HKA CINEMATIC 4K Cloudflare Pipeline — Amendment 1.2"
project: "Human Knowledge Academic"
version: "1.2"
status: "MANDATORY / ACTIVATES STAGING TRANSPORT AND AUTOMATED BRIDGES"
language: "vi"
date: "2026-09-04"
---

# HKA CLOUDFLARE PIPELINE — AMENDMENT 1.2

This amendment activates the temporary transport layer and machine-to-machine bridge architecture supplied by the HKA Cloudflare project window. It is additive to Amendment 1.1 and does not change the 1.1 immutable vault release order.

If this amendment conflicts with older text that says `hka-c4k-staging` is inactive, this amendment overrides that older text for production transport only.

## 1. Four storage planes

```text
hka-c4k-staging   TEMPORARY production/QA transport; non-canonical
hka-c4k-vault     canonical immutable release after QA_APPROVED
hka-c4k-audit     QA/release audit records
hka-c4k-delivery  website delivery plane; gated by WEB_APPROVED
```

`hka-c4k-staging` is now ACTIVE as a temporary transport bucket. Staging objects are never canonical releases and must never be treated as website origin.

## 2. Zero-manual-transfer architecture

```text
IMAGE PRODUCTION WINDOW
  -> HKA_PRODUCTION_UPLOAD_BRIDGE
  -> hka-c4k-staging
  -> HKA_QA_BRIDGE / Independent QA
  -> QA_APPROVED
  -> HKA_RELEASE_BRIDGE
  -> hka-c4k-vault
  -> RELEASED.json + lock
  -> hka-c4k-audit
  -> GitHub RELEASE_INDEX
  -> [WEB_APPROVED only] hka-c4k-delivery
```

There must be no normal-path `user download -> user upload` step.

## 3. Staging namespace

Production writes only under:

```text
tmp/v1/windows/<WINDOW_ID>-<TREE_SLUG>/
prompt-commit/<PROMPT_COMMIT_SHA>/
batches/<BATCH_ID>/
runs/<RUN_ID>/
```

Required behavior:

- create-only / no overwrite;
- same Run ID is never reused for a distinct production attempt;
- staging stores exact generated binaries plus production metadata needed by QA;
- staging is readable by Production and QA principals according to least privilege;
- staging is not a release marker plane and has no `RELEASED.json` semantics.

## 4. Production principal and bridge

Logical service name:

```text
HKA_PRODUCTION_UPLOAD_BRIDGE
```

Production principal permissions:

```text
READ  hka-c4k-staging
WRITE hka-c4k-staging
NO ACCESS hka-c4k-vault
NO ACCESS hka-c4k-audit
NO ACCESS hka-c4k-delivery
```

Required callable interface:

```text
production_begin_run(window_id, tree_slug, prompt_commit_sha, batch_id, run_id)
production_upload_asset(run_id, asset_id, variant, file, sha256, metadata)
production_upload_record(run_id, record_type, file, sha256)
production_complete_run(run_id, manifest_sha256, package_sha256)
```

The Production Window never receives raw Cloudflare credentials. The bridge runs in a trusted automation environment with server-side secrets.

## 5. Production completion and event pipeline

After each CLEAN MASTER, BRANDED FINAL and asset metadata file is accepted by Production self-QA, the Production Bridge uploads it to staging immediately.

At run completion Production also persists the locked manifest/sidecar, prompt reference, production report, self-QA report, checksum registry and package as required by the run contract.

The Cloudflare operational pipeline supplied by the project window is:

```text
hka-c4k-staging
  -> R2 object-create
  -> hka-c4k-upload-events
  -> hka-c4k-upload-event-consumer
  -> QA_PENDING
```

Dead-letter queue:

```text
hka-c4k-upload-events-dlq
```

The exact completion trigger must be a machine-verifiable run-complete event or completion record. `BATCH_MANIFEST.sha256` remains a checksum sidecar and must not be semantically overloaded in a way that changes its canonical hashing role.

## 6. QA principal and bridge

Logical service name:

```text
HKA_QA_BRIDGE
```

QA principal permissions:

```text
READ  hka-c4k-staging
WRITE hka-c4k-audit only for QA report/audit records
NO WRITE hka-c4k-staging
NO ACCESS hka-c4k-vault write
NO ACCESS hka-c4k-delivery write
```

Required callable interface:

```text
qa_get_run(run_id)
qa_list_run_assets(run_id)
qa_get_asset(run_id, asset_id, variant)
qa_get_manifest(run_id)
qa_submit_verdict(run_id, verdict, report, report_sha256)
```

Independent QA must inspect the exact immutable staging binaries produced by the run, not user-reuploaded copies.

Valid verdicts remain:

```text
QA_APPROVED
QA_REJECTED
QA_BLOCKED
```

## 7. Release principal and bridge

Logical service name:

```text
HKA_RELEASE_BRIDGE
```

Release principal permissions:

```text
READ  hka-c4k-staging
READ/WRITE hka-c4k-audit
READ/WRITE hka-c4k-vault
NO hka-c4k-delivery publication before WEB_APPROVED
```

Release begins only when the Independent QA verdict is `QA_APPROVED` and all required package/checksum/report preconditions verify.

The Release Bridge must copy exact approved binaries; it must not regenerate, recompress or mutate them.

## 8. Vault release order remains Amendment 1.1

The following order is unchanged and mandatory:

```text
1. Upload CLEAN MASTER objects
2. Upload BRANDED FINAL objects
3. Upload asset metadata sidecars
4. Upload prompts and manifests
5. Upload production and independent QA reports
6. Upload SHA256SUMS.txt
7. Upload batch package ZIP
8. Verify object count, metadata and SHA-256
9. Generate and upload R2_UPLOAD_RECEIPT.json
10. Verify R2_UPLOAD_RECEIPT.json
11. Generate and upload RELEASED.json as the final vault-prefix object
12. Verify RELEASED.json
13. Apply lock to the complete vault release prefix
14. Write R2_RELEASE_AUDIT_RECORD.json to hka-c4k-audit
15. Update GitHub RELEASE_INDEX.json with audit key + SHA-256
```

Vault canonical prefix remains:

```text
v1/windows/<WINDOW_ID>-<TREE_SLUG>/
prompt-commit/<PROMPT_COMMIT_SHA>/
batches/<BATCH_ID>/
runs/<RUN_ID>/
```

## 9. Delivery gate

`hka-c4k-delivery` remains a separate delivery plane. This amendment does NOT authorize automatic website publication merely because QA is approved or a vault release is R2_VERIFIED.

Delivery write/publish requires the existing website gate:

```text
R2_VERIFIED + RELEASED + WEB_APPROVED
```

After WEB_APPROVED, a delivery bridge/publisher may copy website-consumable branded artifacts and metadata to the delivery namespace. CLEAN MASTER must never be placed in delivery.

## 10. QA rejected runs

For `QA_REJECTED`:

```text
staging binaries: retained under immutable rejected Run ID according to staging retention policy
audit report: retained
vault write: NONE
delivery write: NONE
RELEASED.json: NONE
GitHub RELEASE_INDEX release entry: NONE
```

A new production attempt must use a new Run ID. No overwrite of the rejected run is allowed.

## 11. Secret handling

Production, QA and Release are distinct principals. Credentials live only in trusted automation secrets/bindings. Secrets must never be written into GitHub source, prompts, manifests, reports, release markers or chat conversations.

## 12. Implementation requirement

For zero-manual-transfer to be real, the runtime hosting HKA Windows must expose connected callable actions for the bridge interfaces above. Bucket names alone or raw access keys are insufficient.

Until those actions are connected, windows may author/validate the contract but must not pretend that an R2 upload occurred.

---

> Staging transports exact production binaries to QA. Vault canonizes only QA-approved binaries. Delivery remains WEB_APPROVED-only.