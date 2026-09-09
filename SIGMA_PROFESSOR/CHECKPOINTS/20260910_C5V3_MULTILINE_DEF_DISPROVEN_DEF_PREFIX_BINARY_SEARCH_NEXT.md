# C5V3 — multiline DEF hypothesis disproven / DEF-prefix binary search next

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## Locked identities

```text
R3_FIX1_SOURCE_SHA256=152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8
R3_FIX1_DEF_COUNT=176
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
```

## Multiline DEF signature test

Exact R3 contains one multiline DEF signature at DEF `p0_receipt_envelope_shape_valid`.

Machine controls proved:

```text
MINIMAL_ONE_LINE_DEF_COMPILE_RC=0
MINIMAL_ONE_LINE_DEF_BYTECODE_BYTES=124
MINIMAL_MULTILINE_DEF_COMPILE_RC=0
MINIMAL_MULTILINE_DEF_BYTECODE_BYTES=124
MINIMAL_ONE_LINE_AND_MULTILINE_BYTECODE_SHA256_IDENTICAL=YES
MULTILINE_DEF_SIGNATURE_PARSER_QUIRK=NO_OBSERVED
```

Exact single-delta folding of that R3 signature did not alter the zero-code artifact:

```text
R3_FOLDED_SIGNATURE_COMPILE_RC=0
R3_FOLDED_SIGNATURE_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
R3_FOLDED_SIGNATURE_BYTECODE_BYTES=29
R3_ZERO_CODE_ROOT_CAUSE_SINGLE_MULTILINE_DEF_SIGNATURE=NOT_PROVEN
```

Entry visibility remained absent after the fold:

```text
R3_FOLDED_COUNTERFACTUAL_BYTECODE_CHANGED=NO
R3_FOLDED_UNBALANCED_COMPILE_RC=0
FOLDED_R3_MAIN_LITERAL_SENSITIVITY=FAIL_OR_NOT_REACHED
```

Therefore the multiline DEF hypothesis is closed.

## Current inference

R0 and Gate-A fresh compile reproduce their historical nontrivial bytecodes with the same locked sigmac. Header/version profile is already disproven. The remaining root-cause zone is R3 source composition / entry visibility.

R3 deterministic composition order is:

```text
DEF 1..17   = P0 trust/state
DEF 18..94  = 77 pure Gate-A cognition DEFs
DEF 95..176 = 82 T1/T2/T3 tool DEFs
then single P0 main entry
```

## Exact next machine gate

```text
C5_M5/RUN_C5V3_R3_DEF_PREFIX_ENTRY_VISIBILITY_BINARY_SEARCH_R1.sh
SCRIPT_COMMIT=3f491eef577f54a1aa360426e10dc16cdb66d0a7
```

The gate constructs fresh source variants from exact R3 DEF bodies and a minimal executable sentinel entry:

```text
prefix 0 DEF
prefix 17 DEF
prefix 94 DEF
prefix 176 DEF
cognition-only 77 DEF
tools-only 82 DEF
P0 17 DEF + exact P0 main
```

If all 176 DEFs plus a minimal sentinel entry emit nontrivial bytecode, the root cause moves into the P0 main body.

If all 176 DEFs plus sentinel emit the 29-byte header-only artifact, the gate performs a monotonic prefix binary search and reports the first suspect DEF index/name where entry visibility disappears.

## Admission boundary

```text
R3_FIX1_RUNTIME_ADMISSION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
CLAIM_LEQ_EVIDENCE=MANDATORY
```
