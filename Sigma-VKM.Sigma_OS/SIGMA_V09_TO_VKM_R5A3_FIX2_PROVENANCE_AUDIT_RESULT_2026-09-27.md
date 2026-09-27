# SIGMA V09 -> VKM R5A3 FIX2 Targeted Trainer/Curriculum Provenance Audit — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Safety and continuity

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

R4E_HOLD_PRESERVED=YES

## Target resolution

R5A3_FIX2_TARGETING=PASS

Candidate dir:
.../SIGMA_AUTOLEARN_ADMIN/SEM68_NATIVE_HEADS_20260927T003949_29415

Curriculum dir:
.../SIGMA_AUTOLEARN_ADMIN/06B3_NONFROZEN_CURRICULUM_20260927T002056_23723

Data-vs-mechanism dir:
.../SIGMA_AUTOLEARN_ADMIN/SEM68_DATA_VS_MECHANISM_R2_20260927T013614_9791

Candidate source SHA256:
008d62f8120a112b0f4cfa27676e5d6f80f5b686c5aa76a080c568f04d0bee6b

Targeted file count:
271

## Native candidate function identities

AL68_train
lines 3076-3127
body SHA256=0af3f11c3c9a93cdc331dcf50e7d0ee08217f342ff873257eec04887db5e4297
direct GOLD field refs=NONE

AL68_eval_saved_dev
lines 3128-3146
body SHA256=f079ea760d764d19663ca986c0a88f2d549fc11320f9428b58780c958d21903a
direct GOLD field refs=NONE

AL_native_eval
lines 2165-2231
body SHA256=5712c40b5595e35d3ce29ada14cb7e13c1269d336ac740e653e76200e8414b42
direct GOLD field refs=NONE

N_train
lines 1226-1361
body SHA256=14bb6bfb1a5174c17d7dd9855f8391b662862c2ce32b517808a1aa7872fd4734
direct GOLD field refs=NONE
host primitives observed: math_sqrt,to_int

G3_train
lines 2115-2127
body SHA256=194271f38015291329e02e073b27f0b79774e805f3ecfc9fec05f0552a2747de
direct GOLD field refs=NONE

N_model
lines 866-868
body SHA256=8ba69f92765bb17184409e75c9ca7677e4ff5ae6151e6630d3568a36c04ac6e4

G3_model_generation
lines 2072-2077
body SHA256=d4a4602e47f3719657c9d352bed11531d4eaca4cfb5e950d32c39ca4ac1d3fdf

N_features
lines 824-854
body SHA256=78c4e5e4442863654e8239b9abe0fb487b88c5a019b1b43ce1e4ea44d1f73034
host primitive observed: math_sqrt

AL68S_train_batch=NOT_FOUND in this candidate source
AL68S_eval_batch=NOT_FOUND in this candidate source
AL68_RAW_FEATURES=NOT_FOUND in this candidate source
AL68_RAW_ENCODE=NOT_FOUND in this candidate source
AL68_RAW_PAIR=NOT_FOUND in this candidate source
AL68_RAW_G3_SCORE=NOT_FOUND in this candidate source

## GOLD-field provenance classification

R5A3_GOLD_REFERENCE_NATIVE_SIGMA_FILE_COUNT=4
R5A3_GOLD_REFERENCE_HOST_CODE_FILE_COUNT=0
R5A3_GOLD_REFERENCE_DATA_JSONL_FILE_COUNT=7
R5A3_GOLD_REFERENCE_TEXT_METADATA_FILE_COUNT=3

Native Sigma sources found writing all relevant training fields:
- CURRICULUM_BUILDER.sigma
  SHA256=b3e3bbc1790d3de497803748973ec44a073b9334e50042c8e2824bbcce05b3f1
- CURRICULUM_BUILDER_FIX1.sigma
  SHA256=f84a16217a5d6e3c52e175e7b0aa121f7b54b5556c6febe26dd30c77bd26687f
- CURRICULUM_BUILDER_FIX2_DIAGNOSTIC.sigma
  SHA256=8ddf359b20344d04f153734496c049a740976eda618df020c3a249917264116e
- CURRICULUM_BUILDER_FIX2_SAFE_DIAGNOSTIC.sigma
  SHA256=df783ffa4040b6c123de7b6a6d52549943d05b4627354af90511dca23e644efd

Observed native map writes include:
PROBE_ID
PROBE_TYPE
ORIGINAL_TEXT
MUTATED_TEXT
GOLD_INVARIANT_MASK
GOLD_CHANGE_MASK
GOLD_SOURCE_SPAN
MUTATION_OPERATOR
PROBE_ID_MATERIAL

Observed source comment:
Host SHA256 is mechanical only: it hashes exact PROBE_ID_MATERIAL emitted by Sigma.

## Current evidence ceiling

Positive evidence:
- GOLD field writers were found in native .sigma sources.
- No host-code GOLD-field references were found in the targeted current directories.
- Candidate's major train/eval functions do not directly reference GOLD_* fields.

Still unresolved:
- which exact builder version produced the current 192-record TRAIN_CURRICULUM_NATIVE_R2.jsonl;
- exact native functions that compute change_mask, invariant_mask, gold_source_span, mutation_operator and dimension before map_set;
- whether semantic targets flow indirectly through helper functions/record decoding into AL68_train/N_train/G3_train;
- exact model/head store mutation path;
- exact native gain/admission decision path.

Therefore:
NATIVE_SEMANTIC_SUPERVISION_PROVEN=NOT_YET
HOST_SEMANTIC_SUBSTITUTION_ABSENT=NOT_YET_FULLY_PROVEN
SAFE_TO_USE_FOR_R5B_TRAINING=NOT_YET

## Safety

R5A3_TRAINING_PERFORMED=NO
R5A3_SEMANTIC_EXECUTION_PERFORMED=NO
OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
CANONICAL_MUTATION=NO
GIA_ADMISSION_PERFORMED=NO
DNA15_ALLOWED=NO

NEXT=ASK_SEM68_FOR_EXACT_BUILDER_TARGET_AND_TARGET_FUNCTION_BODIES
