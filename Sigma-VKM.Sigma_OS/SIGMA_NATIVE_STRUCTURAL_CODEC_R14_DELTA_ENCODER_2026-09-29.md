# SIGMA Native Structural Codec R14 — Delta Encoder

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_R14_DELTA_ENCODER.sigma

R14_ENCODER_DETERMINISTIC=PASS

## First write

BASE_CREATED=YES
WRITE_RC=0

BASE_SHA256=
abf4bafcddb38bbf3855e47b5e61b75dedbcf42aa44ffd4bb85d0b08d97e2682

TARGET_SHA256=
219aa0cbebf914f45ab38734bee28e9dbc18da27b5f686597c6a4a7868be2905

BASE_BYTES=240
TARGET_BYTES=240
DELTA_PAYLOAD_BYTES=99
DELTA_CONTAINER_BYTES=177
INCREMENTAL_SAVING_BYTES=63

REAL_DATA_DELETE=NO

## Second write

BASE_CREATED=NO
WRITE_RC=0

BASE_SHA256=
abf4bafcddb38bbf3855e47b5e61b75dedbcf42aa44ffd4bb85d0b08d97e2682

TARGET_SHA256=
219aa0cbebf914f45ab38734bee28e9dbc18da27b5f686597c6a4a7868be2905

BASE_BYTES=240
TARGET_BYTES=240
DELTA_PAYLOAD_BYTES=99
DELTA_CONTAINER_BYTES=177
INCREMENTAL_SAVING_BYTES=63

REAL_DATA_DELETE=NO

## Stability and dedup

DELTA_CONTAINER_STABLE=PASS

BASE_CONTENT_DEDUP=PASS

GOOD14_SHA256=
d559f72f02d6e743e440f960c9e9b76384dd1cd4df3f2f91f9589f33c9d30183

BASE_OBJECT_COUNT=1

## Interpretation boundary

This checkpoint records deterministic R14 delta encoding with a durable base-object reference and stable repeated output.

The supplied evidence establishes:
- deterministic encoder compilation;
- the first write creates the base object;
- the second identical write reuses the same base object;
- base object count remains exactly one;
- the delta container is stable across repeated writes;
- a 240-byte target is represented by a 177-byte delta container, reported as 63 bytes of incremental saving;
- no real-data deletion occurred.

This is R14 encoder/delta/dedup evidence only and is not, by itself, an independent production-admission receipt.
