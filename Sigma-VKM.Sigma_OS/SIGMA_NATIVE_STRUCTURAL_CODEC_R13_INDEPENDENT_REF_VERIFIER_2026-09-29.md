# SIGMA Native Structural Codec R13 — Independent Reference Verifier

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_R13_INDEPENDENT_REF_VERIFIER.sigma

R13_VERIFIER_COMPILE_DETERMINISTIC=PASS

## Independent verifier — Run 1

GOOD_REF_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
BAD_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_OUTER_HASH_REJECT=PASS
BAD_REF_MAGIC_REJECT=PASS
REF_HASH_MISMATCH_REJECT=PASS
INVALID_REF_HEX_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS
MISSING_OBJECT_REJECT=PASS
CORRUPT_OBJECT_REJECT=PASS

R13_INDEPENDENT_REF_VERIFIER=PASS
R13_CASES=14_OF_14_PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Independent verifier — Run 2

GOOD_REF_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
BAD_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_OUTER_HASH_REJECT=PASS
BAD_REF_MAGIC_REJECT=PASS
REF_HASH_MISMATCH_REJECT=PASS
INVALID_REF_HEX_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS
MISSING_OBJECT_REJECT=PASS
CORRUPT_OBJECT_REJECT=PASS

R13_INDEPENDENT_REF_VERIFIER=PASS
R13_CASES=14_OF_14_PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Fresh-process reproducibility

R13_FRESH_PROCESS_REPRODUCIBILITY=PASS

## Interpretation boundary

This checkpoint records independent validation of the R13 durable-reference container/object relationship.

The supplied evidence establishes:
- good reference container accepted;
- malformed outer container fields rejected;
- malformed reference payload and invalid reference hex rejected;
- reference hash mismatch rejected;
- missing object rejected;
- corrupt referenced object rejected;
- both verifier runs produce identical output;
- verifier explicitly reports SELF_CERTIFIED=NO;
- no real-data deletion occurred.

This strengthens the prior R13 durable-reference encoder/dedup checkpoint, but does not by itself constitute a separate production-admission receipt.
