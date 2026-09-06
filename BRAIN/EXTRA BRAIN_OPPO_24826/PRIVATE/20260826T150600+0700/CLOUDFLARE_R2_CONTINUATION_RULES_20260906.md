# Cloudflare R2 continuation rules — 2026-09-06

## Do not repeat these approaches

1. Do not use recursive whole-tree `rclone copy` for routine continuation. It caused long metadata scans and small-file transfers.
2. Do not use `rclone sync`; deletion semantics are outside the transfer contract.
3. Do not build one whole-tree TAR/ZIP while SIGMA is active. An interrupted whole-tree TAR produced `Unexpected EOF in archive`.
4. Do not TAR all `.sigma_*` areas blindly while active runtime processes exist.
5. Do not copy/TAR live SQLite databases and call that an authoritative backup. A proper consistent database backup mechanism is required.
6. Do not use R2 multipart ETag as a substitute for full-object SHA256 during final validation.
7. Do not store Cloudflare credentials in GitHub.

## Known upload fix

A direct upload initially failed with S3 `CreateBucket` / `403 AccessDenied`. The proven fix for this already-existing bucket is:

```bash
--s3-no-check-bucket
```

Therefore the standard upload form is:

```bash
rclone copyto LOCAL_TAR sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/REMOTE_TAR --s3-no-check-bucket --progress
```

## Next-window operating procedure

1. Read the three Cloudflare R2 handoff files in this directory.
2. Confirm the local OPPO remote:

```bash
rclone listremotes
```

Expected: `sigmar2:`.

3. Ask which file class/group should be archived next.
4. Count first:

```bash
find ~/SIGMA/sigma_genesis1 -type f -name '*.EXT' | wc -l
```

5. If the class is small/medium, create one TAR with null-safe paths, verify count, upload one object.
6. If the class has tens of thousands of files, create a sorted list, split at 10,000 lines, TAR each list, verify each count, and upload each TAR separately.
7. Never delete OPPO or R2 data during this continuation phase.
8. Keep RAW ingest intact until cloud-side inventory, exact-hash deduplication, classification, read-back verification, and isolated restore validation are complete.
9. Exact duplicate decisions must be content-based, not filename-only.
10. At handoff time `*.json` had been proposed as a possible next class but had not yet been counted or archived.

## Historical baseline only

Before later batches were uploaded, remote inventory was observed as:

```text
249644 objects
2634255901 bytes
2.453 GiB
```

This is not the current remote total.
