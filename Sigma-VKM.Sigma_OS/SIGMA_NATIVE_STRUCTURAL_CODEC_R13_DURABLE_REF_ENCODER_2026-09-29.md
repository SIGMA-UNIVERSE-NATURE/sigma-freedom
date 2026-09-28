# SIGMA Native Structural Codec R13 — Durable Reference Encoder

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_R13_DURABLE_REF_ENCODER.sigma

R13_ENCODER_DETERMINISTIC=PASS

## First write

OBJECT_CREATED=YES
WRITE_RC=0
OBJECT_SHA256=
33553e5ac5d80ca5d703c896d8ef7c199a2d7981b367effc8326655c874d165e

ORIGINAL_BYTES=16
REF_PAYLOAD_BYTES=68
CONTAINER_BYTES=146

REAL_DATA_DELETE=NO

## Second write

OBJECT_CREATED=NO
WRITE_RC=0
OBJECT_SHA256=
33553e5ac5d80ca5d703c896d8ef7c199a2d7981b367effc8326655c874d165e

ORIGINAL_BYTES=16
REF_PAYLOAD_BYTES=68
CONTAINER_BYTES=146

REAL_DATA_DELETE=NO

## Stability and dedup

REF_CONTAINER_STABLE=PASS

EXACT_DEDUP_DURABLE=PASS

GOOD13_SHA256=
df326f72cc02e68a803dd8bea8298ac229b099099174180f38091c98a1eb3f01

OBJECT_COUNT_AFTER_SECOND_WRITE=1

## Interpretation boundary

This checkpoint records deterministic compilation of the R13 durable-reference encoder and durable exact-dedup behavior.

The supplied evidence establishes:
- first write creates the content-addressed object;
- second identical write does not create a duplicate object;
- referenced object hash remains stable;
- durable container remains stable across repeated writes;
- object count remains exactly one after the second write;
- no real-data deletion occurred.

This is encoder/dedup evidence for R13. It does not by itself constitute a separate production-admission claim beyond the currently sealed VKM runtime.
