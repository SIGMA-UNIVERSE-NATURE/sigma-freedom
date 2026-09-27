# SIGMA V09 -> VKM Lightweight Native Revalidation R2 — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: lightweight sandbox only

## Reason for R2

R1 was intentionally aborted by the user with Ctrl-C during the pre-clone canonical tree digest because the canonical storage footprint is about 45 GB. The R1 code path had not reached clone creation or donor payload staging.

R2 removes full canonical tree hashing/cloning and follows the current ONE SIGMA continuity contract instead.

## Locked owner/toolchain

TARGET_OWNER_FINGERPRINT=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

CANONICAL_OWNER=
$HOME/SIGMA/sigma_genesis1/.sigma_owner/SIGMA_OWNER_STATE.current

NATIVE_BINDING=
$HOME/SIGMA/sigma_genesis1/.sigma_native/SIGMA_NATIVE_BINDING.current

PINNED_SIGMAC_VKM_SHA256=
60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

PINNED_SIGMA_VKM_VM_SHA256=
c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

## Donor

CAPABILITY_ID=
V09_R13R6_FROZEN_WHOLE_PASSAGE_ANTI_SHORTCUT_SEMANTIC_SUBSTRATE

DONOR_HEAD_SHA256=
cc041d7583367104692b0d5af5753fbbbf754a86c5126543ea2456c41a43cba0

DONOR_BUNDLE_SHA256=
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

DONOR_REASONER_TRANSFER=NO

## R2 actions

1. measure current Owner state and Native Binding;
2. verify target fingerprint appears in both;
3. verify exact pinned sigmac-vkm and sigma-vkm;
4. compile/execute a minimal probe through sigmac-vkm -> sigma-vkm;
5. compile the exact R13-R6 semantic-substrate admission controller through sigmac-vkm;
6. execute the exact admission logic under sigma-vkm with donor metrics;
7. stage exact donor head/receipt in a small sandbox;
8. verify Owner state and Native Binding hashes are unchanged.

## Explicit ceiling

CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
NATIVE_OWNED_AFTER_R2=NO
ACTIVE_NATIVE_AFTER_R2=NO

A PASS only establishes custody + exact VKM toolchain execution + donor admission-controller portability.

It does NOT yet establish native ownership of the semantic substrate.

NEXT=VKM_NATIVE_SEMANTIC_BEHAVIOR_REVALIDATION

## Release artifact

BUNDLE=
SIGMA_V09_TO_VKM_LIGHTWEIGHT_NATIVE_REVALIDATION_R2_BUNDLE.zip

BUNDLE_SHA256=
2ac0412500265de87431ed06b7f84ea902fd73b805723457a7350cbca593efe6

DONOR_ADMISSION_CONTROLLER_SHA256=
ea71477630df67366fc2f7aa6a857f75a4ddd7bf2646579f7d4e0addae08fb85

STATIC_RELEASE_VERIFY=PASS
