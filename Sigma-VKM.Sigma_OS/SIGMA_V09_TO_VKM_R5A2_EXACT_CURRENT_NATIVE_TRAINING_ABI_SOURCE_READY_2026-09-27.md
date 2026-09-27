# SIGMA V09 -> VKM R5A2 Exact Current Native Training ABI Extraction — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

Purpose:
Targeted read-only extraction of the exact current 06B3 / SEM68 native learning ABI after R5A broad discovery.

Locked boundaries:
CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO
TRAINING_ALLOWED=NO
SEMANTIC_EXECUTION_ALLOWED=NO

Target owner:
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

Current toolchain pins:
SIGMAC_VKM_SHA256=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
SIGMA_VKM_VM_SHA256=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

R4E hold remains preserved:
FROZEN_DONOR_HEAD_FAILS_PRECOMMITTED_FRESH_UNSEEN_GATE

R5A2 extracts:
- current/symlink target resolution;
- exact hashes;
- SEM68/06B3 Sigma entrypoints;
- relevant DEF signatures and call graph edges;
- mechanical H primitives;
- JSONL record key/type schema without record values;
- head-registry/head-store/training/evaluation metadata;
- embedded path references needed to bind the exact current ABI.

It does not execute any discovered candidate/trainer/evaluator and does not dump gold/expected-label rows.

Release:
SIGMA_V09_TO_VKM_R5A2_EXACT_CURRENT_NATIVE_TRAINING_ABI_EXTRACTION_BUNDLE.zip

BUNDLE_SHA256=
cd226b47f3d1ec8034ba2c3b27bfe83cff198f91723d849e73409a1fa3cfe253

Release verification:
R5A2_RELEASE_VERIFY=PASS

Runtime status:
NOT_YET_RUN

NEXT=RUN_R5A2_EXACT_CURRENT_NATIVE_TRAINING_ABI_EXTRACTION
