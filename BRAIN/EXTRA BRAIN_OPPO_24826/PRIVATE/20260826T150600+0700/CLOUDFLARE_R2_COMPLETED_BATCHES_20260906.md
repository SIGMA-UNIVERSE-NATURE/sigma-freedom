# Completed Cloudflare R2 batches — 2026-09-06

Observed complete uploads in this session:

```text
DNA batch                         COMPLETE
C5 V3 evidence TAR               COMPLETE; evidence only
SH batch                          COMPLETE; 740 files
STATE_FILES batch                 COMPLETE
SIGMA source batches              COMPLETE; 89568 files total
SIGMAB batches                    COMPLETE; 89178 files total
RUN batch                         COMPLETE; 166 files
```

## `*.sigma`

Source count observed: `89568`.

Commands used to prepare the lists:

```bash
find ~/SIGMA/sigma_genesis1 -type f -name '*.sigma' | sort > ~/SIGMA/sigma_files.list
```

```bash
split -l 10000 -d -a 2 ~/SIGMA/sigma_files.list ~/SIGMA/sigma_batch_
```

Each batch was created with the same proven form, changing `NN` from `00` through `08`:

```bash
tar -cf ~/SIGMA/SIGMA_BATCH_SIGMA_NN_20260906.tar -T ~/SIGMA/sigma_batch_NN
```

Each batch was checked before upload:

```bash
tar -tf ~/SIGMA/SIGMA_BATCH_SIGMA_NN_20260906.tar | wc -l
```

Verified counts:

```text
00=10000
01=10000
02=10000
03=10000
04=10000
05=10000
06=10000
07=10000
08=9568
TOTAL=89568
```

Upload form used for every batch:

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_SIGMA_NN_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_SIGMA_NN_20260906.tar --s3-no-check-bucket --progress
```

All nine were observed `Transferred: 1 / 1, 100%`.

## `*.sigmab`

Source count observed: `89178`.

```bash
find ~/SIGMA/sigma_genesis1 -type f -name '*.sigmab' | sort > ~/SIGMA/sigmab_files.list
```

```bash
split -l 10000 -d -a 2 ~/SIGMA/sigmab_files.list ~/SIGMA/sigmab_batch_
```

Batch create/check/upload forms:

```bash
tar -cf ~/SIGMA/SIGMA_BATCH_SIGMAB_NN_20260906.tar -T ~/SIGMA/sigmab_batch_NN
```

```bash
tar -tf ~/SIGMA/SIGMA_BATCH_SIGMAB_NN_20260906.tar | wc -l
```

```bash
rclone copyto ~/SIGMA/SIGMA_BATCH_SIGMAB_NN_20260906.tar sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/SIGMA_BATCH_SIGMAB_NN_20260906.tar --s3-no-check-bucket --progress
```

Verified counts:

```text
00=10000
01=10000
02=10000
03=10000
04=10000
05=10000
06=10000
07=10000
08=9178
TOTAL=89178
```

All nine were observed `Transferred: 1 / 1, 100%`.

## Other completed upload observations

```text
SIGMA_BATCH_SH_20260906.tar             6.895 MiB, 1/1, 100%
SIGMA_BATCH_STATE_FILES_20260906.tar    8.018 MiB, 1/1, 100%
SIGMA_BATCH_RUN_20260906.tar            320 KiB, 1/1, 100%
C5 V3 evidence TAR                      859.219 MiB, 1/1, 100%
```

Do not infer current full-bucket size from the earlier 2.453 GiB baseline; many batches were uploaded afterward.
