# SIGMA V09 -> VKM R4A3 Native Mechanical Microprobes — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: ISOLATED_NATIVE_MECHANICAL_PROBES

## Purpose

R4A2 showed that current SIGMA_VKM source does not expose exact source-level evidence for all donor R13-R6 mechanics.

Important exact findings:
- api_artifact_sha256_digest is fixture-only and must not be used as donor h64;
- api_index_tokenize is not donor-tokenizer equivalent;
- pinned sigma-vkm binary contains candidate mechanical primitive names:
  bytes_raw_utf8, crypto_digest, hex_encode, math_sqrt, math_exp, math_pow, list_sort, to_float.

R4A3 probes those primitive names through real:
sigmac-vkm -> sigmab -> sigma-vkm

Each uncertain signature is isolated in its own process.

## Locked identity

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

## Probe families

- math_sqrt
- math_exp
- math_pow
- to_float
- bytes_raw_utf8 + hex_encode
- five crypto_digest calling variants
- list_sort return-vs-mutate semantics
- str_len / string_length / value_len candidates
- exp-derived tanh compared mechanically to reference math.tanh values

Python in this package is evaluator-only; it does not provide semantic feature extraction or donor inference.

## Boundaries

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO
SEMANTIC_BEHAVIOR_CLAIM_ALLOWED=NO

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4A3_NATIVE_MECHANICAL_MICROPROBES_BUNDLE.zip

BUNDLE_SHA256=
70f965e2b9b8f6cacd08fb73126da724af6fcbb1112b7fdae71e92e9edd35ad3

R4A3_RELEASE_VERIFY=PASS

Runtime:
NOT_YET_RUN

NEXT=RUN_R4A3_NATIVE_MECHANICAL_MICROPROBES
