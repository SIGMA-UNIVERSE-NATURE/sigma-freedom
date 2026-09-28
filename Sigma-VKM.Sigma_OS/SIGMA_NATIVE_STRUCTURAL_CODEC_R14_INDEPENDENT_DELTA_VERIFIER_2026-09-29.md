# SIGMA Native Structural Codec R14 — Independent Delta Verifier

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_R14_INDEPENDENT_DELTA_VERIFIER.sigma

R14_VERIFIER_COMPILE_DETERMINISTIC=PASS

## Independent verifier — Run 1

GOOD_DELTA_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
BAD_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_TARGET_HASH_REJECT=PASS
BAD_DELTA_MAGIC_REJECT=PASS
BAD_BASE_HASH_REJECT=PASS
INVALID_BASE_HEX_REJECT=PASS
UNKNOWN_OPCODE_REJECT=PASS
COPY_OOB_REJECT=PASS
INSERT_OOB_REJECT=PASS
BAD_OP_COUNT_REJECT=PASS
BAD_INSERT_DATA_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS
MISSING_BASE_REJECT=PASS
CORRUPT_BASE_REJECT=PASS

R14_INDEPENDENT_DELTA_VERIFIER=PASS
R14_CASES=19_OF_19_PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Independent verifier — Run 2

GOOD_DELTA_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
BAD_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_TARGET_HASH_REJECT=PASS
BAD_DELTA_MAGIC_REJECT=PASS
BAD_BASE_HASH_REJECT=PASS
INVALID_BASE_HEX_REJECT=PASS
UNKNOWN_OPCODE_REJECT=PASS
COPY_OOB_REJECT=PASS
INSERT_OOB_REJECT=PASS
BAD_OP_COUNT_REJECT=PASS
BAD_INSERT_DATA_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS
MISSING_BASE_REJECT=PASS
CORRUPT_BASE_REJECT=PASS

R14_INDEPENDENT_DELTA_VERIFIER=PASS
R14_CASES=19_OF_19_PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Fresh-process reproducibility

R14_FRESH_PROCESS_REPRODUCIBILITY=PASS

## Interpretation boundary

This checkpoint records independent validation of the R14 delta container/base-object relationship.

The supplied evidence establishes:
- good delta container accepted;
- malformed outer container fields rejected;
- target/base hash corruption rejected;
- invalid base hex rejected;
- unknown opcode rejected;
- copy/insert out-of-bounds rejected;
- invalid operation count and insert data rejected;
- truncated and trailing data rejected;
- missing base rejected;
- corrupt base rejected;
- both verifier runs produce identical output;
- verifier explicitly reports SELF_CERTIFIED=NO;
- no real-data deletion occurred.

This strengthens the prior R14 delta encoder/dedup checkpoint, but does not by itself constitute a separate production-admission receipt.
