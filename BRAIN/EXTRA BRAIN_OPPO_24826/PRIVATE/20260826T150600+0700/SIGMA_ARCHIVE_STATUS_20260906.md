# SIGMA archive status — 2026-09-06

Purpose: handoff for future ChatGPT windows/operators. This file records what has already been archived, where it was archived, and the proven command pattern. Do not repeat completed batches.

## Safety rules

- Source OPPO root: `~/SIGMA/sigma_genesis1`
- Never use `rclone sync`.
- Never delete OPPO source during this archive phase.
- Do not touch live SQLite under `.sigma_c5_real_shadow_v2` as an authoritative backup.
- Cloudflare credentials/secrets must never be committed to GitHub.
- Use `--s3-no-check-bucket` for uploads to the existing R2 bucket.

## R2 locations

### Raw ingest / data for later classification

`sigmar2:sigma-oppo-vault/raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/`

### SIGMA-generated archive / restore-only storage

`sigmar2:sigma-oppo-vault/sigma-archive/SIGMA-OPPO-20260906/`

The `sigma-archive` branch is for SIGMA-generated/internal artifacts that should be preserved for restore. Do not classify, deduplicate, rewrite, or delete these automatically.

## Completed raw-ingest groups

Completed before/within this session:

- DNA batch — DONE
- `*.sh` — DONE
- `*.state` — DONE
- `*.sigma` — 89,568 / 89,568 — DONE
- `*.sigmab` — 89,178 / 89,178 — DONE
- `*.run` — DONE
- `*.json` — 1,185,040 / 1,185,040 archived as JSON batches `00..23` — DONE
  - batches `00..22`: 50,000 files each
  - batch `23`: 35,040 files
- selected important `.txt` group matching dictionary/learned_words/corpus/user_material/vocab/lexicon/memory — 467 files — DONE

Note: a later live recount showed 1,185,045 JSON files, meaning SIGMA likely created 5 additional JSON files after the completed 1,185,040-file archive snapshot. Do not rerun all prior JSON batches. Future archive work should capture only new files since the saved cutoff.

## Completed SIGMA restore-only archive groups

Under `sigma-archive/SIGMA-OPPO-20260906/`:

- `SIGMA_ARCHIVE_BLOB_20260906.tar` — DONE — uploaded 234.629 MiB
  - source: `.sigma_native/knowledge_v2/objects/*.blob`
- `SIGMA_ARCHIVE_DONE_20260906.tar` — DONE — uploaded 3.789 MiB
  - source: `.sigma_native/processed/*.done`
- `SIGMA_ARCHIVE_TSV_20260906.tar` — DONE — uploaded 180 KiB
  - source: `.sigma_research/integration/rankings/*.tsv`

Do not recreate or re-upload these same dated batches.

## Groups identified as SIGMA-generated / KEEP LOCAL unless explicitly archived later

These were inspected by sample path and identified as SIGMA runtime/internal/generated artifacts:

- `*.log`
- `*.stdout`
- `*.stderr`
- `*.entry`
- `*.env`
- `*.seq`
- `*.raw`
- `*.url`
- `*.request`
- `*.query`
- `*.writeout`
- `*.input`
- `*.next_epoch`
- `*.ordinal`
- `*.readback`
- `*.sha256`
- `*.error`
- `*.urls`
- `*.ledger`
- `*.out`
- `.py` tools/source outside `.sigma_exec` are KEEP LOCAL unless a later explicit archive decision is made.

Important: KEEP LOCAL does not mean delete. It means preserve on OPPO and do not send to raw-ingest for classification. If later backing these up, send them to the dated `sigma-archive/` restore-only prefix, not `raw-ingest/`.

## Proven archive command pattern

For a known SIGMA-generated group that should be preserved as restore-only archive:

```bash
cd ~/SIGMA/sigma_genesis1
find <SOURCE_PATH> -type f -name '<PATTERN>' -print0 | tar --null -T - -cf ~/SIGMA/<BATCH_NAME>.tar
rclone copyto ~/SIGMA/<BATCH_NAME>.tar sigmar2:sigma-oppo-vault/sigma-archive/SIGMA-OPPO-20260906/<BATCH_NAME>.tar --s3-no-check-bucket --progress
```

Example already proven for `.blob`:

```bash
cd ~/SIGMA/sigma_genesis1
find .sigma_native/knowledge_v2/objects -type f -name '*.blob' -print0 | tar --null -T - -cf ~/SIGMA/SIGMA_ARCHIVE_BLOB_20260906.tar
rclone copyto ~/SIGMA/SIGMA_ARCHIVE_BLOB_20260906.tar sigmar2:sigma-oppo-vault/sigma-archive/SIGMA-OPPO-20260906/SIGMA_ARCHIVE_BLOB_20260906.tar --s3-no-check-bucket --progress
```

## Continuation rule for a future date

1. Read this file first.
2. Do not repeat any batch marked DONE.
3. Use a new dated prefix for a new archive session, for example `sigma-archive/SIGMA-OPPO-YYYYMMDD/`.
4. Archive only data created/changed after the previous saved cutoff whenever practical.
5. Prefer TAR batches over recursive per-file R2 copy for large classes.
6. Keep SIGMA-generated restore-only material separate from raw-ingest material that needs later classification.
7. Never delete local SIGMA data merely because an upload succeeded.
