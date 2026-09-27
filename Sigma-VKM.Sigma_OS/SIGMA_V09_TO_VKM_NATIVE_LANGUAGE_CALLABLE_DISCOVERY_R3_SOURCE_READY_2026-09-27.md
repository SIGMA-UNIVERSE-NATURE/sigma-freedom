# SIGMA V09 -> VKM Native Language Callable Discovery R3 Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: READ_ONLY_DISCOVERY

Purpose:
determine the exact current SIGMA_VKM native language/semantic callable contract before running V09 R13-R6 semantic behavior revalidation.

This stage intentionally performs no semantic execution and no ownership promotion.

Locked state:
TARGET_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
EXPECTED_R2_VKM_SOURCE_SHA256=af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7
PINNED_SIGMAC_VKM_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
PINNED_SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

R2 checkpoint:
SIGMA_V09_TO_VKM_LIGHTWEIGHT_NATIVE_REVALIDATION_R2=PASS
R2 checkpoint commit=f141ddb6c8863fb195b47f461daf927e1dfd3e95

Release bundle:
SIGMA_V09_TO_VKM_NATIVE_LANGUAGE_CALLABLE_DISCOVERY_R3_BUNDLE.zip
ZIP_SHA256=9de8a5dc44d1efbc1f4f2bd1b9ebbc55853aae628c6adcf8af5f6e2361602d34

Safety:
CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
NO_FULL_CANONICAL_SCAN_OR_CLONE=YES
SEMANTIC_EXECUTION_PERFORMED=NO

R3 will inspect only:
- SIGMA_VKM.sigma
- canonical Owner state
- Native Binding
- bounded relevant provenance filenames

Output:
- DISCOVERY_MATCHES.tsv
- DEF_CANDIDATES.json
- R3_DISCOVERY_RECEIPT.json

NEXT:
use the exact discovered callable contract to build R4 VKM-native semantic behavior revalidation for the accepted R13-R6 anti-shortcut semantic substrate.
