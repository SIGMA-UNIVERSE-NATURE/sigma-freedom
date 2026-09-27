# SIGMA V09 -> VKM R4A2 Exact Native Primitive Closure Audit — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Identity continuity

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

R4A_SOURCE_CONTINUITY=PASS
PINNED_SIGMAC_VKM_SHA256=PASS
PINNED_SIGMA_VKM_VM_SHA256=PASS

## Source inventory

DEF_TOTAL=1103
GLOBAL_H_PRIMITIVE_COUNT=32
RELEVANT_H_PRIMITIVE_COUNT=9
PERCENT_OPERATOR_COUNT=1
WHILE_COUNT=79
FOR_COUNT=0
NUMERIC_DECIMAL_LITERAL_COUNT=21

## Exact/current evidence

Exact H evidence:
- read_text
- list_slice
- str_slice
- str_split
- str_lower
- numeric_to_int
- map/list primitives from R4A

Current wrappers found:
- api_artifact_sha256_digest(artifact), but no direct H hash primitive in its body
- artifact_hash(experiment,artifact)
- api_index_tokenize(text)
- api_text_slice(x,start,end)
- api_num_mod(a,b)
- api_num_to_int(x)
- vkm_state_parse(text)
- vkm_state_read(path)
- api_split_digest(split)
- api_split_provenance(dataset,train_ratio,seed,digest)
- api_list_slice
- api_map_items/keys/values

No H primitive-name evidence in current SIGMA_VKM.sigma for:
- sha/hash/digest
- regex
- sqrt
- tanh
- exp
- pow
- log
- float
- hex
- parse
- UTF

Positive-only binary-string counts:
SIGMAC_RELEVANT_BINARY_STRING_COUNT=25
SIGMAC_SQRT_STRING_COUNT=0
SIGMAC_TANH_STRING_COUNT=0
SIGMAC_SHA_STRING_COUNT=1
SIGMAC_REGEX_STRING_COUNT=0

VM_RELEVANT_BINARY_STRING_COUNT=23
VM_SQRT_STRING_COUNT=1
VM_TANH_STRING_COUNT=0
VM_SHA_STRING_COUNT=6
VM_REGEX_STRING_COUNT=0

Binary string presence is not treated as callable primitive proof.

## Interpretation

The exact donor R13-R6 encoder still cannot be claimed portable from current evidence.

Strong current mechanics:
- UTF-8-ish text file read path
- split/slice/lower string mechanics
- maps/lists
- integer conversion
- modulo operator
- loops

Unclosed donor-critical mechanics:
1. exact donor h64 = SHA-256(UTF-8) first 8 bytes big-endian;
2. exact donor tokenizer/sentence segmentation equivalence;
3. sqrt;
4. tanh;
5. deterministic sorted-unique/top-18 behavior;
6. exact frozen-head loading/constant embedding strategy.

Do not fill these gaps with host semantic substitution or unverified approximations.

## Safety

SEMANTIC_BEHAVIOR_EXECUTION_PERFORMED=NO
CANONICAL_MUTATION=NO
OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

R4A2_PRIMITIVE_CLOSURE_AUDIT=COMPLETE

NEXT=EXTRACT_EXACT_HASH_TOKENIZER_NUMERIC_HELPER_BODIES_AND_BINARY_STRINGS_THEN_BUILD_R4A3_MECHANICAL_MICROPROBES
