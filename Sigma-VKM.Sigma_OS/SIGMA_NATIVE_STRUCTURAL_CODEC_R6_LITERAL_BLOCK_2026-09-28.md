# SIGMA Native Structural Codec R6 — Literal Block

Date: 2026-09-28
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_STRUCTURAL_CODEC_R6_LITERAL_BLOCK.sigma

Two independent bytecode outputs were compiled:

codec_r6_literal_a.sigmab
codec_r6_literal_b.sigmab

DETERMINISTIC_COMPILE_R6=PASS

## Native VM training/roundtrip cases

### UNSEEN_MIXED

RAW_BYTES=15
PACKED_BYTES=14
PACK_UNPACK_ROUNDTRIP=PASS
STORAGE_CHOICE=STRUCTURED

### UNSEEN_RAW_BETTER

RAW_BYTES=3
PACKED_BYTES=8
PACK_UNPACK_ROUNDTRIP=PASS
STORAGE_CHOICE=RAW

### UNSEEN_DICT_REUSE

RAW_BYTES=16
PACKED_BYTES=13
PACK_UNPACK_ROUNDTRIP=PASS
STORAGE_CHOICE=STRUCTURED

### UNSEEN_DESCENDING_RANGE

RAW_BYTES=6
PACKED_BYTES=6
PACK_UNPACK_ROUNDTRIP=PASS
STORAGE_CHOICE=RAW

### UNSEEN_LITERAL_BLOCK

RAW_BYTES=27
PACKED_BYTES=16
PACK_UNPACK_ROUNDTRIP=PASS
STORAGE_CHOICE=STRUCTURED

## Final runtime status

TRAINING_ROUNDTRIP=PASS

REAL_DATA_DELETE=NO
CANONICAL_MUTATION=NO

STORAGE_SELF_MAINTENANCE=TRAINING

COST_MODEL=
ACTUAL_PACKED_BYTES_R5

PACK_FORMAT=
SG_U8_R_L_LB_REP_DICT_R6

MEMORY_WRITE=FALSE

## Interpretation boundary

This checkpoint records:
- deterministic compilation of the R6 literal-block structural codec;
- successful pack/unpack roundtrip on multiple unseen structural cases;
- storage selection between RAW and STRUCTURED according to actual packed byte cost;
- no real-data deletion;
- no canonical mutation;
- no memory write during this training/proof run.

This evidence establishes codec behavior for the supplied test cases only; it does not by itself prove production admission or persistent deployment.
