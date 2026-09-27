# SIGMA V09 -> VKM R4A Native Donor Inference Portability Audit — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Preflight

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

DONOR_HEAD_SHA256=
cc041d7583367104692b0d5af5753fbbbf754a86c5126543ea2456c41a43cba0

DONOR_BUNDLE_SHA256=
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

PINNED_SIGMAC_VKM_SHA256=PASS
PINNED_SIGMA_VKM_VM_SHA256=PASS
DONOR_HEAD_IDENTITY=PASS
DONOR_BUNDLE_IDENTITY=PASS
DONOR_INFERENCE_FUNCTION_IDENTITY=PASS

## Donor inference identity

DONOR_HASH_BUCKETS=4096
DONOR_STATE_DIMENSION=256
DONOR_FANOUT=8
DONOR_TOKEN_RE=[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?

DONOR_HEAD_SCHEMA=PASS
DONOR_HEAD_WEIGHT_ROWS=4096
DONOR_HEAD_WEIGHT_WIDTH=8
DONOR_HEAD_STATE_DIMENSION=256
DONOR_HEAD_QUESTION_LABELS_USED_TO_TRAIN_ENCODER=NO

DONOR_SUBSTRATE_ADMISSION=PASS
DONOR_REASONER_EXCLUDED=PASS

## Primitive audit

Strong/exact current VKM evidence:
- UTF8 text read: H(read_text)
- sparse map mechanics: H(map_new/map_get/map_set)
- modulo: source operator %
- vector/list mechanics: H(list_new/list_get/list_set) plus loop syntax

Candidate-only, not exact equivalence evidence:
- SHA256 string path
- regex/tokenization
- sentence split
- substring
- sort/dedupe
- pair-combinations
- integer/hex conversion
- frozen-state loading

No source-name evidence:
- SQRT
- TANH

Therefore current evidence is insufficient to implement and claim an exact native R13-R6 frozen encoder without a further primitive closure audit.

## Boundary

API410_AS_R13R6_DONOR_EXECUTOR=NO
R4A_PORTABILITY_GAP_AUDIT=COMPLETE
CANONICAL_MUTATION=NO
OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

## Decision

Do not implement R4B by:
- Python semantic substitution;
- host-side feature extraction;
- approximate tanh/sqrt without equivalence testing;
- guessed hash/tokenization semantics.

NEXT=R4A2_EXACT_NATIVE_PRIMITIVE_CLOSURE_AUDIT
