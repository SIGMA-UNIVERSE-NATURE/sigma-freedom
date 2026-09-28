# SIGMA VKM R15 IO — Pre-Admission

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## 1 MiB bound test

EXACT_LEN=1048576
BIG_LEN=1048577

EXACT_APPEND_RC=0
SIZE_AFTER_EXACT=1048576

BIG_APPEND_RC=3
SIZE_AFTER_BIG_REJECT=1048576

PACK_SHA=
30e14955ebf1352266dc2ff8067e68104607e750abb9d3b36582b8af909fcb58

Host-side SHA cross-check matched.

R15_IO_1MIB_BOUND=PASS

## R2-R14 regression on R15 candidate VM

R2=PASS
R3=PASS
R4=PASS
R5=PASS
R6=PASS
R7=PASS
R8=PASS
R9=PASS
R10=PASS
R11=PASS
R12=PASS
R13=PASS
R14=PASS

R15_CANDIDATE_CODEC_R2_R14_REGRESSION=PASS

## Pre-admission manifest

SCHEMA=SIGMA_VKM_R15_IO_PRE_ADMISSION_R1
STATUS=PASS

BYTES_APPEND=PASS
FILE_SIZE=PASS
FILE_TRUNCATE_SHRINK_ONLY=PASS
ONE_MIB_APPEND_BOUND=PASS
ADDITIVE_SOURCE_AUDIT=PASS
R2_R14_REGRESSION=PASS

FULL_STATE_COPY=NO
REAL_DATA_DELETE=NO
CANONICAL_MUTATION=NO
ADMISSION=PENDING

PRE_ADMISSION.env SHA256=
c9ecd2bc096b1f17285716498f0439771dd16cc8b3b41378842d17425e2f2448

## Candidate VM

CANDIDATE_VM_SHA256=
0ad6424ccb84bfe2f44240bff8d1cf531a2fb0be88c61491ee113ba740269755

## Final status

R15_IO_PRE_ADMISSION=PASS

## Interpretation boundary

This checkpoint establishes R15 IO pre-admission evidence only:
- exact 1 MiB append succeeds;
- append beyond the configured bound is rejected without growing the file;
- host hash confirms the exact-bound output;
- codec/verifier lineage R2 through R14 passes on the R15 candidate VM;
- additive source audit is reported PASS;
- no full-state copy, no real-data deletion, and no canonical mutation occurred.

ADMISSION remains PENDING. The candidate VM hash above must not be treated as canonical until a separate runtime admission/native binding reseal completes.
