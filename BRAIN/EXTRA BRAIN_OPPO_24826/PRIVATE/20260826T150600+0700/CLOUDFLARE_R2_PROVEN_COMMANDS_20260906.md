# Proven Cloudflare R2 transfer commands

These commands were used successfully in the OPPO transfer session. No credentials are stored here.

## Remote / inventory

```bash
rclone listremotes
```

Expected remote: `sigmar2:`

```bash
rclone size sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/
```

```bash
du -sb ~/SIGMA/sigma_genesis1
```

## Small/medium file-class TAR

```bash
cd ~/SIGMA/sigma_genesis1 && find . -type f -name '*.EXT' -print0 | tar --null -T - -cf ~/SIGMA/SIGMA_BATCH_EXT_20260906.tar
```

Verify count:

```bash
tar -tf ~/SIGMA/SIGMA_BATCH_EXT_20260906.tar | wc -l
```

Upload one object:

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_EXT_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_EXT_20260906.tar --s3-no-check-bucket --progress
```

## Large file-class batching

```bash
find ~/SIGMA/sigma_genesis1 -type f -name '*.EXT' | sort > ~/SIGMA/ext_files.list
```

```bash
split -l 10000 -d -a 2 ~/SIGMA/ext_files.list ~/SIGMA/ext_batch_
```

```bash
tar -cf ~/SIGMA/SIGMA_BATCH_EXT_00_20260906.tar -T ~/SIGMA/ext_batch_00
```

```bash
tar -tf ~/SIGMA/SIGMA_BATCH_EXT_00_20260906.tar | wc -l
```

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_EXT_00_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_EXT_00_20260906.tar --s3-no-check-bucket --progress
```

`tar: Removing leading '/' from member names` and the matching hard-link-target warning were observed and are informational, not failures, when absolute paths are supplied via `-T`.

## Proven shell-script batch

```bash
cd ~/SIGMA/sigma_genesis1 && find . -type f -name '*.sh' -print0 | tar --null -T - -cf ~/SIGMA/SIGMA_BATCH_SH_20260906.tar
```

```bash
printf 'SOURCE='; find ~/SIGMA/sigma_genesis1 -type f -name '*.sh' | wc -l; printf 'TAR='; tar -tf ~/SIGMA/SIGMA_BATCH_SH_20260906.tar | wc -l
```

Observed: `SOURCE=740`, `TAR=740`.

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_SH_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_SH_20260906.tar --s3-no-check-bucket --progress
```

## Proven state-file batch

```bash
cd ~/SIGMA/sigma_genesis1 && find . -type f -name '*.state' -print0 | tar --null -T - -cf ~/SIGMA/SIGMA_BATCH_STATE_FILES_20260906.tar
```

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_STATE_FILES_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_STATE_FILES_20260906.tar --s3-no-check-bucket --progress
```

## Proven run-file batch

```bash
find ~/SIGMA/sigma_genesis1 -type f -name '*.run' | wc -l
```

Observed: `166`.

```bash
cd ~/SIGMA/sigma_genesis1 && find . -type f -name '*.run' -print0 | tar --null -T - -cf ~/SIGMA/SIGMA_BATCH_RUN_20260906.tar
```

```bash
tar -tf ~/SIGMA/SIGMA_BATCH_RUN_20260906.tar | wc -l
```

Observed: `166`.

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_RUN_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_RUN_20260906.tar --s3-no-check-bucket --progress
```
