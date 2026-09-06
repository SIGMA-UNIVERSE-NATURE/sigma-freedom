# Cloudflare R2 / OPPO handoff checkpoint

STATUS=ACTIVE
DATE=2026-09-06
RCLONE_REMOTE=sigmar2:
R2_BUCKET=sigma-oppo-vault
R2_PREFIX=raw-ingest/SIGMA-OPPO-RAW-20260906-001/batches/
DELETE_OPPO=NO
DELETE_R2=NO
RCLONE_SYNC=NO
UPLOAD_MODE=BATCH_TAR_COPYTO
S3_NO_CHECK_BUCKET=REQUIRED

Completed groups observed in the transfer session:
- DNA batch
- shell-script batch: 740 files
- state-file batch
- sigma source batches: 89568 files total
- sigmab batches: 89178 files total
- run-file batch: 166 files
- one C5 V3 evidence TAR; evidence only, not authoritative live-database backup

Cloudflare credentials are intentionally not stored here. Continue using the already-authorized local OPPO rclone remote `sigmar2:`. Do not delete source or remote data during continuation. Do not tar/copy live SQLite databases as authoritative backups.
