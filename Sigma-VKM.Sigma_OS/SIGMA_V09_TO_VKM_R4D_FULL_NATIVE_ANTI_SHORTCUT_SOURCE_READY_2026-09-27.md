# SIGMA V09 -> VKM R4D Full Native Anti-Shortcut Behavior Revalidation — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: SIGMA_NATIVE_BLIND_PRODUCER_INDEPENDENT_VERIFIER

## Preconditions established

R4B_NATIVE_FEATURE_EXTRACTION_PARITY=PASS
R4C_FIX1_FROZEN_HEAD_256D_ENCODER_PARITY=PASS

Current target Owner:
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

Pinned toolchain:
SIGMAC_VKM_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

Donor head:
cc041d7583367104692b0d5af5753fbbbf754a86c5126543ea2456c41a43cba0

## Blind runtime design

DOCUMENT_COUNT=384
ANTI_SHORTCUT_RELATION_COUNT=96
STATE_DIMENSION=256
STATE_COMPONENT_COUNT=98304

Runtime receives:
- 384 opaque text filenames only;
- exact frozen head state serialization;
- native Sigma controller.

Runtime does NOT receive:
- world IDs;
- fold IDs;
- renderer names;
- BASE / ALTERED / ALIAS labels;
- positive / negative / anchor roles;
- expected states;
- expected relation outcomes;
- independent reference.

After Sigma process exit:
- actual output is SHA-256 sealed;
- only then independent verifier reads hidden mapping/reference;
- verifier checks all 98,304 Q1E9 state components;
- verifier computes cross-view and alias-vs-altered relation behavior from actual native states.

Retention floor is not weakened:
CROSS_VIEW_CORRECT>=95/96
ALIAS_INVARIANCE=96/96
MIN_FOLD_CORRECT>=23/24

## Frozen mapping roots

SOURCE_MAP_SHA256=
9bb94b1f2e14eaf1ae75c782058d17e25d3e406e02bc6a41d329e274427e54c1

RELATIONS_SHA256=
63e36fb145ad8d19eb77c26ce491169d47d36bfaf68ff452b07fb00cdf830829

OPAQUE_INPUT_MANIFEST_SHA256=
116513c475f8ad8717b79bac1041c7cdbd76fe0c0c079e95ce5324e42060e315

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4D_FULL_NATIVE_ANTI_SHORTCUT_BEHAVIOR_REVALIDATION_BUNDLE.zip

BUNDLE_SHA256=
facc15cb4c99918347cb33ab03091b90851db5f6065ae6ef24de4d4c8ed2bb6e

R4D_RELEASE_VERIFY=PASS

## Boundaries

SIGMA_SELF_CERTIFICATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO

Runtime status:
NOT_YET_RUN

NEXT=RUN_R4D_FULL_NATIVE_ANTI_SHORTCUT_BEHAVIOR_REVALIDATION
