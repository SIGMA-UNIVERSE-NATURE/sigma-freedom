# C5V3 — R0/Gate-A compiler oracle: VERSION/profile root cause disproven

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO
VM execution in this oracle: NO

## Locked identities

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
R0_SOURCE_SHA256=81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a
R0_FROZEN_BYTECODE_SHA256=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300
GATEA_SOURCE_SHA256=bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1
GATEA_HISTORICAL_BYTECODE_SHA256=569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2
R3_FIX1_SOURCE_SHA256=152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8
HEADER_ONLY_29B_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

## Fresh compiler oracle

```text
R0_ORIGINAL_COMPILE_RC=0
R0_ORIGINAL_BYTECODE_SHA256=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300
R0_ORIGINAL_BYTECODE_BYTES=2180
R0_FRESH_MATCHES_FROZEN=YES

GATEA_ORIGINAL_COMPILE_RC=0
GATEA_ORIGINAL_BYTECODE_SHA256=569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2
GATEA_ORIGINAL_BYTECODE_BYTES=73265
GATEA_FRESH_MATCHES_HISTORICAL=YES

R3_ORIGINAL_COMPILE_RC=0
R3_ORIGINAL_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
R3_ORIGINAL_BYTECODE_BYTES=29
R3_ORIGINAL_BYTECODE_CLASS=HEADER_ONLY_29B
```

This proves the current locked sigmac can still reproduce both historical nontrivial executable artifacts exactly.

## Header/version counterfactual

R0 original header:

```text
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.PROPOSITION.SPAN.CANDIDATE][VERSION=1.0]
```

Gate-A original header:

```text
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5M5SCOPEDPROVISIONALEPISTEMICTRUTH1]
```

R3 historical identity header:

```text
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]
```

Counterfactual results:

```text
R0_FORCED_C5FULLR1_COMPILE_RC=0
R0_FORCED_C5FULLR1_SHA=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300

GATEA_FORCED_C5FULLR1_COMPILE_RC=0
GATEA_FORCED_C5FULLR1_SHA=569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2

R3_FORCED_GATEA_VERSION_COMPILE_RC=0
R3_FORCED_GATEA_VERSION_SHA=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a

R0_VERSION_PROFILE_EFFECT=NO_OBSERVED
GATEA_VERSION_PROFILE_EFFECT=NO_OBSERVED
R3_GATEA_VERSION_RESTORES_NONTRIVIAL_EMISSION=NO
```

## Conclusion

```text
R3_ZERO_CODE_ROOT_CAUSE_IS_HEADER_VERSION_PROFILE=NO
R3_HISTORICAL_C5FULLR1_IDENTITY_MAY_BE_PRESERVED=YES
SIGMAC_CURRENT_LINEAGE_CAN_EMIT_NONTRIVIAL_FULL_SIGMA=PROVEN_BY_R0_AND_GATEA
R3_ZERO_CODE_ROOT_CAUSE=SOURCE_OR_COMPOSITION_GRAMMAR_BOUNDARY
R3_FIX1_RUNTIME_ADMISSION=NO
```

Do not mutate the historical C5 identity to work around the zero-code artifact.

## Static next hypothesis

R3 FIX1 P0 contains a multiline DEF signature before the entry block:

```text
DEF p0_receipt_envelope_shape_valid(
    invocation_id,
    event_type,
    expected_phase,
    parent_state_sha,
    action_id,
    receipt_kind
) {
```

Exact Gate-A and exact R6 have one-line DEF signatures. Prior R3 evidence also showed that deleting the final entry brace did not cause a compile rejection, while a minimal unbalanced entry is rejected. This makes top-level parser/entry visibility a high-priority hypothesis.

## Exact next machine test

```text
C5_M5/RUN_C5V3_R3_MULTILINE_DEF_SIGNATURE_EMISSION_PROBE_R1.sh
SCRIPT_COMMIT=3893dc39eca7b0e03d32e60fe08b3fc3be708c44
```

The probe performs:

```text
minimal one-line DEF vs multiline DEF grammar controls
exact R3 single-delta fold of p0_receipt_envelope_shape_valid signature
fresh compile of folded R3
folded-R3 observable print-literal counterfactual
folded-R3 final-brace negative control
live core/runner non-mutation recheck
```

If folding that one signature restores nontrivial emission and main sensitivity, root cause is proven by exact single delta. Otherwise proceed to DEF-composition-vs-main binary search.

`CLAIM <= EVIDENCE`
