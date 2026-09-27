# SIGMA V09 -> VKM R4A3 FIX1 Boolean Mechanical Probes — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: ISOLATED_NATIVE_MECHANICAL_PROBES

## Repair

R4A3 numeric probes were invalidated by an output-harness type error:
string + numeric concatenation caused:
SIGMA C VM: incompatible binary operands

FIX1 removes numeric output concatenation entirely.

All numeric/mechanical assertions are evaluated inside Sigma.
Only literal PASS/FAIL strings are printed.

## Exact continuity locks

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

PINNED_SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

PINNED_SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

## Probes

- sqrt
- exp
- pow
- to_float
- str_len
- str_slice
- str_byte
- bytes_raw_utf8 + bytes_len/get
- direct crypto_digest("sha256","ABC",NULL)
- exp-derived tanh against frozen numeric references
- donor SHA-256 bucket equivalence
- donor layout digest coordinate/sign equivalence

The donor hash equivalence avoids full unsigned-64 parsing:
- bucket mod 4096 is recovered from the last 3 hex digits of the first 8 digest bytes;
- layout coordinate mod 256 is the fourth digest byte;
- sign parity is derived from the fifth digest byte.

This preserves the exact donor result required by R13-R6 for these uses.

## Safety

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO
SEMANTIC_BEHAVIOR_CLAIM_ALLOWED=NO

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4A3_FIX1_BOOLEAN_MECHANICAL_PROBES_BUNDLE.zip

BUNDLE_SHA256=
1fe42fa337776a1edb7014ee7707da097e1e32af42bd88df6cb0b85cfd248f09

R4A3_FIX1_RELEASE_VERIFY=PASS
SELFTEST=PASS

Runtime status:
NOT_YET_RUN

NEXT=RUN_R4A3_FIX1
