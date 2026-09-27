# SIGMA V09 -> VKM R4A3 FIX1 Boolean Mechanical Probes — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Identity continuity

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

OWNER_STATE_SHA256=
e73a8bba0f631b9ab90d98a04211a2c025a777734e68ec15bb4561a38da66661

NATIVE_BINDING_SHA256=
99e25dd665bffda45315c0720e58c527529cc5a0b8f35d2a4d566f04a41f85f5

VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

R4A3_SOURCE_CONTINUITY=PASS
PINNED_SIGMAC_VKM_SHA256=PASS
PINNED_SIGMA_VKM_VM_SHA256=PASS

## Native mechanical results

PASS:
- math_sqrt basic assertion
- math_exp basic assertion
- math_pow basic assertion
- to_float basic assertion
- str_len
- str_slice
- str_byte
- crypto_digest("sha256","ABC",NULL) returns exact raw 64-hex SHA-256
- exp-derived tanh at 0, 0.5, 1, -1, 2 within 1e-12
- donor hash-bucket identities
- donor layout digest coordinate/sign identities

Exact markers:
R4A3_FIX1_SQRT_ASSERT=PASS
R4A3_FIX1_EXP_ASSERT=PASS
R4A3_FIX1_POW_ASSERT=PASS
R4A3_FIX1_TO_FLOAT_ASSERT=PASS
R4A3_FIX1_STR_LEN_ASSERT=PASS
R4A3_FIX1_STR_SLICE_ASSERT=PASS
R4A3_FIX1_STR_BYTE_ASSERT=PASS
R4A3_FIX1_CRYPTO_SHA256_DIRECT=PASS_RAW64
R4A3_FIX1_TANH_EXP_ASSERT=PASS_1E_12
R4A3_FIX1_HASH_BUCKET_ASSERT=PASS
R4A3_FIX1_LAYOUT_DIGEST_ASSERT=PASS

Diagnostic-only failure:
BYTES_RAW_ASSERT VM_RC=22, "SIGMA host: string required".

This does not block the R13-R6 donor inference path because:
- crypto_digest accepts the donor hash input directly as a string;
- donor feature keys and layout keys in the admitted R13-R6 corpus are ASCII strings;
- the exact donor bucket/layout identities passed through the native crypto_digest route.

LIST_SORT had already passed in R4A3 diagnostic.

## Current mechanical conclusion

R13-R6 hash/layout/sqrt/tanh/list/string mechanics now have strong native VKM execution evidence for the donor scope.

Still not closed:
- exact donor tokenizer behavior;
- exact donor sentence segmentation behavior;
- full feature extraction parity;
- frozen weight loading/representation;
- 256-D encoder parity;
- anti-shortcut semantic behavior parity.

## Safety

OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
SEMANTIC_BEHAVIOR_REVALIDATION_PERFORMED=NO
CANONICAL_MUTATION=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

NEXT=R4A4_EXACT_DONOR_TOKENIZER_SENTENCE_SEGMENTER_NATIVE_PARITY
