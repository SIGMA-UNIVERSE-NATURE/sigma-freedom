# SIGMA V09 -> VKM R4E Fresh Unseen Blind Anti-Shortcut Generalization — HOLD

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Identity/toolchain continuity

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

## Freshness / anti-shortcut pre-audit

R4E_FRESH_EXACT_DONOR_TEXT_OVERLAP=0
R4E_FRESH_MIN_NOVEL_TOKEN_COUNT_PER_WORLD=21
R4E_FRESH_RAW_FEATURE_LEXICAL_TRAP=32_OF_32
R4E_FRESH_TOKEN_JACCARD_TRAP=32_OF_32

## Frozen-head fresh reference

R4E_REFERENCE_CROSS_CORRECT=17_OF_32
R4E_REFERENCE_ALIAS_CORRECT=32_OF_32

R4E_REFERENCE_MIN_FAMILY_CROSS=0_OF_4
R4E_REFERENCE_MIN_FAMILY_ALIAS=4_OF_4

Family cross/alias:
F1=4/4,4/4
F2=4/4,4/4
F3=4/4,4/4
F4=4/4,4/4
F5=0/4,4/4
F6=0/4,4/4
F7=0/4,4/4
F8=1/4,4/4

R4E_Q1E9_RELATION_ORDER_EQUIVALENT=PASS
R4E_REFERENCE_FRESH_GENERALIZATION_FLOOR=FAIL

R4E_REFERENCE_SHA256=
25ef73457c3d0f9e656a47f51a4f89e68f6cba1f54f95cd0b5f1621a63f7dbdc

R4E_REFERENCE_CREATED_BEFORE_SIGMA_RUNTIME=YES
R4E_REFERENCE_VISIBLE_TO_SIGMA_RUNTIME=NO
R4E_EXPECTED_LABELS_VISIBLE_TO_SIGMA_RUNTIME=NO

R4E_PRE_RUNTIME_REFERENCE_RC=40

## Correct classification

HOLD=FROZEN_DONOR_HEAD_FAILS_PRECOMMITTED_FRESH_UNSEEN_GATE
R4E_NATIVE_EXECUTION_PERFORMED=NO

This is a falsification of strong fresh-unseen generalization for the frozen V09 R13-R6 head.

It is NOT evidence that SIGMA_VKM native execution failed, because the native run was intentionally blocked before execution.

R4D remains valid evidence that SIGMA_VKM reproduces the donor capability in the original declared R13-R6 scope:
- 384 native documents;
- 98,304 state components;
- zero mismatches;
- cross-view 96/96;
- alias 96/96;
- minimum fold 24/24.

Therefore:
V09_R13R6_DECLARED_SCOPE_NATIVE_REPRODUCTION=PASS
V09_R13R6_FRESH_UNSEEN_GENERALIZATION=HOLD

## Promotion boundary

NATIVE_OWNED=NO
GIA_ADMISSION_PERFORMED=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

Do not:
- lower the R4E gate;
- relabel the R4E set as PASS;
- train on R4E and later call the same set unseen;
- promote the frozen donor head as a general semantic capability.

## Correct next direction

Use R4E only as preserved falsification evidence.

Discover and use the current SIGMA_VKM-native learning/curriculum mechanisms (06B3 / SEM68 / current Gen3 sandbox learning path) to build a new non-canonical candidate from disjoint training evidence with:
- native Sigma supervision;
- no host semantic supervision;
- no R4E expected-label exposure during training;
- R4D regression preservation;
- a new post-freeze unseen blind evaluator after candidate freeze.

NEXT=R5A_DISCOVER_CURRENT_NATIVE_LEARNING_CURRICULUM_AND_TRAINING_ABI
