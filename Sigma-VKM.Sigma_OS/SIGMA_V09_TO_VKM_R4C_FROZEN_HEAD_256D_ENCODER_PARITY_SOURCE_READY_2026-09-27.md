# SIGMA V09 -> VKM R4C Frozen Head 256-D Encoder Parity — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: SIGMA_NATIVE_PRODUCER_INDEPENDENT_VERIFIER

## Purpose

R4B proved native donor feat() parity.

R4C isolates the accepted frozen R13-R6 semantic head:
- exact donor bundle;
- exact frozen head SHA256;
- exact donor layout() and encode() function identities;
- native-readable frozen head serialization;
- native 4096x8 -> 256-D accumulation;
- native tanh;
- independent post-run state verification.

## Safety / honesty

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO
SEMANTIC_BEHAVIOR_CLAIM_ALLOWED=NO

REFERENCE_VISIBLE_TO_SIGMA_RUNTIME=NO
SIGMA_SELF_CERTIFICATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO

Host/Python is used only before runtime to:
- verify frozen donor source/function hashes;
- verify donor head hash/admission receipt;
- mechanically serialize frozen head coordinates/weights;
- generate isolated encoder input feature fixtures;
- freeze expected encoder outputs.

The Sigma runtime receives only:
- frozen native head state;
- encoder feature inputs;
- native Sigma controller.

Expected 256-D states are not copied into runtime.

## Fixed identities

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

EXPECTED_VKM_SOURCE_SHA256=
af918fe8794791d70dcf6fb1b62e1b2fdd075f4ec237a7f3b72b9054e39876c7

SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

DONOR_HEAD_SHA256=
cc041d7583367104692b0d5af5753fbbbf754a86c5126543ea2456c41a43cba0

DONOR_LAYOUT_FUNCTION_SHA256=
7f0580b7f3b9bdbc3e5f398932146aca0f695aec057afc31ef7c70194c5b89ef

DONOR_ENCODE_FUNCTION_SHA256=
a092905e0088fc30c1132a2797c5ec6ba25b875733db70a506364a72c123d074

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4C_FROZEN_HEAD_256D_ENCODER_PARITY_BUNDLE.zip

BUNDLE_SHA256=
7344aae44f73676f87df0961be76c6a72ef38106f29831264811dbc54e53abe4

R4C_RELEASE_VERIFY=PASS

Runtime status:
NOT_YET_RUN

NEXT=RUN_R4C
