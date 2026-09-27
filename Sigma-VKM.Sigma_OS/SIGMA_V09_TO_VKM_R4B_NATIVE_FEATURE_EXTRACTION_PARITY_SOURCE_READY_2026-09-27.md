# SIGMA V09 -> VKM R4B Native Feature Extraction Parity — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Purpose

Port the exact donor R13-R6 feat() computation into native SIGMA_VKM and verify it with a blind independent verifier.

## Locked identities

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

PINNED_SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

PINNED_SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

DONOR_BUNDLE_SHA256=
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

DONOR_FEAT_FUNCTION_SHA256=
99e93d0f12b109f96092716e5a0252d4a3eddf13576a5b3ac143a5d8b23ee9c2

## Honesty boundary

SIGMA native runtime receives only:
- R4B native feature controller;
- 10 blind text fixtures.

Frozen expected feature vectors are stored separately and are not copied into Sigma runtime.

REFERENCE_FEATURES_SHA256=
4a3fa2e07d2d4e3802bf3f480b3f423b3680cced28a6bcd2a2ff696fdf162d77

FIXTURE_MANIFEST_ROOT_SHA256=
044e0f0a2a794bcaf3bcc1d81a6f0b99a41f07f6d135348849db0d077bcee33b

Reference is generated before SIGMA runtime from the frozen donor feat() implementation.

Runtime sequence:
SIGMA_VKM native feat execution
-> native output complete
-> actual output SHA-256 seal
-> chmod read-only
-> only then independent verifier reads reference
-> compare all 10 x 4096 quantized components

SIGMA_SELF_CERTIFICATE=NO
HOST_SEMANTIC_SUBSTITUTION=NO
REFERENCE_VISIBLE_TO_SIGMA_RUNTIME=NO

## Pass gate

CASE_COUNT=10
FEATURE_DIMENSION=4096
QUANTIZATION_SCALE=1000000000
TOTAL_COMPONENT_COMPARISONS=40960

PASS requires every quantized feature component and support count to match the frozen reference.

## Claim ceiling

R4B PASS would prove native donor feature-extraction parity for the frozen test scope.

It would NOT yet prove:
- frozen 4096x8 head parity;
- 256-D encoder parity;
- anti-shortcut semantic behavior;
- native ownership;
- GIA admission;
- DNA15 eligibility.

CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO

BUNDLE=
SIGMA_V09_TO_VKM_R4B_NATIVE_FEATURE_EXTRACTION_PARITY_BUNDLE.zip

BUNDLE_SHA256=
94e9ecbc59be4b7fcbfd073ade3c5e35bbd5ccd8635f4ef0a3a189364dbba412

RELEASE_VERIFY=PASS

NEXT=RUN_R4B_NATIVE_FEATURE_EXTRACTION_PARITY
