# SIGMA Native Structural Codec R12 — Independent Verifier

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Compile

Source:
SIGMA_VKM_R12_INDEPENDENT_VERIFIER.sigma

Compiled bytecode:
r12_independent_verifier.sigmab

## Independent verifier — Run 1

GOOD_STRUCTURED_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
UNKNOWN_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_HASH_REJECT=PASS
BAD_INNER_MAGIC_REJECT=PASS
UNKNOWN_TAG_REJECT=PASS
EXTERNAL_DICT_TAG_REJECT=PASS
BAD_SEGMENT_COUNT_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS

R12_INDEPENDENT_STRUCTURED_VERIFIER=PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Independent verifier — Run 2

GOOD_STRUCTURED_VALID=PASS
BAD_MAGIC_REJECT=PASS
BAD_VERSION_REJECT=PASS
UNKNOWN_MODE_REJECT=PASS
BAD_ORIGINAL_LENGTH_REJECT=PASS
BAD_PAYLOAD_LENGTH_REJECT=PASS
BAD_HASH_REJECT=PASS
BAD_INNER_MAGIC_REJECT=PASS
UNKNOWN_TAG_REJECT=PASS
EXTERNAL_DICT_TAG_REJECT=PASS
BAD_SEGMENT_COUNT_REJECT=PASS
TRUNCATED_REJECT=PASS
TRAILING_REJECT=PASS

R12_INDEPENDENT_STRUCTURED_VERIFIER=PASS
SELF_CERTIFIED=NO
REAL_DATA_DELETE=NO

## Fresh-process reproducibility

R12_FRESH_PROCESS_REPRODUCIBILITY=PASS

## Interpretation boundary

This checkpoint records independent verification of the R12 structured container format:
- valid structured container accepted;
- malformed magic/version/mode/length/hash rejected;
- malformed inner format/tag/segment count rejected;
- truncated and trailing data rejected;
- external-dictionary tag rejected;
- two fresh verifier runs produced identical output;
- verifier explicitly reports SELF_CERTIFIED=NO;
- no real data deletion occurred.

This evidence strengthens the prior R12 encoder/roundtrip checkpoint, but does not by itself constitute production admission.
