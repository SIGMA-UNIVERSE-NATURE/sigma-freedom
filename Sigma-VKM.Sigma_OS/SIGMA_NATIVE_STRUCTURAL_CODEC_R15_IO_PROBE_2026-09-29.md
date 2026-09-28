# SIGMA Native Structural Codec R15 — IO Probe

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Compile

Source:
SIGMA_VKM_R15_IO_PROBE.sigma

Compiled bytecode:
r15_io_probe.sigmab

## Run 1

INITIAL_WRITE_RC=0
SIZE_3=3

APPEND_RC=0
SIZE_7=7

FULL_SHA=
25df57c207ca3857d776903400f316fbc951227fbe429c97ba86925e8f57a54b

TRUNCATE_RC=0
SIZE_5=5

TRUNCATED_SHA=
36bc5cd4af3917246fa191d0633a587f1bdc9ec17f1df5e9e2cc87dfaf13d6dd

EXTEND_REJECT_RC=7
SIZE_STILL_5=5

REAL_DATA_DELETE=NO

## Run 2

INITIAL_WRITE_RC=0
SIZE_3=3

APPEND_RC=0
SIZE_7=7

FULL_SHA=
25df57c207ca3857d776903400f316fbc951227fbe429c97ba86925e8f57a54b

TRUNCATE_RC=0
SIZE_5=5

TRUNCATED_SHA=
36bc5cd4af3917246fa191d0633a587f1bdc9ec17f1df5e9e2cc87dfaf13d6dd

EXTEND_REJECT_RC=7
SIZE_STILL_5=5

REAL_DATA_DELETE=NO

## Fresh-process reproducibility

R15_IO_FRESH_PROCESS_REPRODUCIBILITY=PASS

## Host-side confirmation

Expected final bytes:
01 02 03 04 00

Host SHA256:
36bc5cd4af3917246fa191d0633a587f1bdc9ec17f1df5e9e2cc87dfaf13d6dd

FINAL_SIZE=5

## Interpretation boundary

This checkpoint records R15 IO behavior:
- initial write succeeds;
- append succeeds and grows the file from 3 to 7 bytes;
- truncate succeeds and reduces the file to 5 bytes;
- attempted extension is rejected with RC 7 and size remains 5 bytes;
- VM-produced truncated SHA matches an independent host hash of the expected 5-byte sequence;
- two fresh runs produce identical output;
- no real-data deletion is reported.

This is IO primitive/probe evidence only and is not, by itself, an admission receipt.
