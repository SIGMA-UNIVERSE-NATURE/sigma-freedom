# SIGMA R18B — Cost-Aware Store + Duplicate Idempotence

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Too-expensive path

R18B_TOO_EXPENSIVE=PASS

## Net-beneficial store path

SOURCE_BYTES=1024
FRAME_BYTES=147
PROJECTED_APPEND_BYTES=303

DECISION=STORE

BUNDLE_SHA256=
300bc2d5cf9981b47b9542e459926c216daea95657ea0d6f2540108d889f1be8

APPENDED_BYTES=303
RECORD_COUNT=2
PACK_BYTES=1640
COMMIT_BYTES=36

NEW_INODES_PER_ARTIFACT=0

MODEL_MUTATION=NO
GENERATION_MUTATION=NO
CANONICAL_HEAD_MUTATION=NO
CANDIDATE_ADMISSION=NO
REAL_DATA_DELETE=NO

R18B_NET_BENEFICIAL_STORE=PASS

STORE_SOURCE_BYTES=1024
STORE_APPEND_COST=303

The measured append cost is strictly smaller than the source bytes for this case.

## Duplicate path

Repeated storage attempt on the same bundle returned:

DECISION=SKIP_DUPLICATE

BUNDLE_SHA256=
300bc2d5cf9981b47b9542e459926c216daea95657ea0d6f2540108d889f1be8

SOURCE_BYTES=1024
APPENDED_BYTES=0
NEW_INODES_PER_ARTIFACT=0
REAL_DATA_DELETE=NO

Pack and commit hashes/sizes remained unchanged during the duplicate attempt.

R18B_DUPLICATE_IDEMPOTENT=PASS

## Production isolation

PRODUCTION_PACK_UNCHANGED=PASS
PRODUCTION_COMMIT_UNCHANGED=PASS

R18B_TEST_COMPLETE

## Interpretation boundary

This checkpoint records cost-aware sidecar storage behavior for the supplied R18B tests:

- a too-expensive case is rejected/skipped;
- a net-beneficial case with 1,024 source bytes and 303 projected append bytes is stored;
- the same bundle is subsequently recognized as a duplicate and appends zero bytes;
- duplicate handling leaves pack and commit content/size unchanged;
- no new inode is created per artifact in the tested path;
- no model, generation, or canonical-head mutation occurs;
- no candidate admission and no real-data deletion occur;
- production pack and commit artifacts remain unchanged by this test.

This evidence applies to the tested R18B decision/idempotence paths and does not by itself authorize deleting source or unique-state artifacts.
