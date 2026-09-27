# SIGMA V09 -> VKM R5A Native Learning Interface Discovery — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE

Purpose:
read-only discovery of the exact current SIGMA_VKM native learning / curriculum / evaluator / candidate ABI after R4E fresh-unseen HOLD.

R4E preserved:
HOLD=FROZEN_DONOR_HEAD_FAILS_PRECOMMITTED_FRESH_UNSEEN_GATE
R4E_NATIVE_EXECUTION_PERFORMED=NO

R5A boundaries:
MODE=READ_ONLY_INTERFACE_DISCOVERY
CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO
TRAINING_ALLOWED=NO
SEMANTIC_EXECUTION_ALLOWED=NO

Bounded discovery only:
- VKM/SIGMA_AUTOLEARN_ADMIN maxdepth 3
- .sigma_ail/native_tools maxdepth 2
- VKM root maxdepth 1
- no recursive canonical backend scan

Target mechanisms:
06B2 / 06B3 / SEM68 / curriculum / train / evaluator / raw-byte ABI / head registry / head store / learning candidate / admission / Gen3.

Bundle:
SIGMA_V09_TO_VKM_R5A_NATIVE_LEARNING_INTERFACE_DISCOVERY_BUNDLE.zip

BUNDLE_SHA256=
d36aa676437021c43ceb519071d72043a260fdf6bc8702b9d65ea3a4e5b9854f

Release verification:
R5A_RELEASE_VERIFY=PASS

NEXT=RUN_R5A_AND_BIND_THE_NEXT_CANDIDATE_ONLY_TO_DISCOVERED_NATIVE_ABI
