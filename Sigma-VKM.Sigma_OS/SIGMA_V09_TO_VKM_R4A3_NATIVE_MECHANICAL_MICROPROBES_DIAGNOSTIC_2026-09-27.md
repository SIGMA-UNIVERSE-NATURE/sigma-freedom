# SIGMA V09 -> VKM R4A3 Native Mechanical Microprobes — Diagnostic Result

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

## VM primitive strings observed

Positive binary strings include:
bytes_concat
bytes_f64
bytes_find_byte
bytes_get
bytes_get_f64
bytes_i64
bytes_len
bytes_new
bytes_raw_utf8
bytes_slice
bytes_slice_string
bytes_u16
bytes_u32
bytes_u8
bytes_write
crypto_digest
hex_encode
list_sort
math_abs
math_ceil
math_cos
math_exp
math_floor
math_log
math_pow
math_round
math_sin
math_sqrt
math_tan
numeric_to_int
str_byte
str_len
str_slice
str_split
to_float
to_int

Binary-string presence remains discovery evidence, not callable-behavior proof.

## Probe interpretation

### Proven in this run

LIST_SORT_RETURN:
VM_RC=0
output=a|b|c
PASS

LIST_SORT_MUTATE:
VM_RC=0
original list observed as a|b|c after list_sort
PASS

Therefore current list_sort both returned a sorted list and left the tested original list sorted in this case.

### Harness-invalid numeric verdicts

The following controllers used string + numeric concatenation to print their result:
- SQRT
- EXP
- POW
- TO_FLOAT
- STR_LEN
- TANH_EXP

All returned:
VM_RC=6
SIGMA C VM: incompatible binary operands

This does NOT prove the mechanical primitive call failed. The numeric host call is evaluated before the string concatenation in the controller expression, so the observed failure is compatible with successful primitive execution followed by an invalid string+numeric operation.

Classify:
R4A3_NUMERIC_PROBES=HOLD_HARNESS_OUTPUT_TYPE_MISMATCH

Do not classify sqrt/exp/pow/to_float/str_len/tanh as absent from this run.

### Bytes / crypto signature diagnostics

BYTES_HEX:
VM_RC=22
SIGMA host: string required

CRYPTO_A/B/C/E:
VM_RC=22
SIGMA host: string required

CRYPTO_D:
crypto_digest("sha256","ABC",NULL) progressed farther and then the controller reported an error at the hex_encode stage:
VM_RC=26
SIGMA host: unknown operation hex_encode

This is evidence that CRYPTO_D is the highest-priority candidate signature for direct digest-result testing. Do not infer its return type yet.

## Safety

OWNER_STATE_MUTATION=NO
NATIVE_BINDING_MUTATION=NO
CANONICAL_MUTATION=NO
SEMANTIC_BEHAVIOR_REVALIDATION_PERFORMED=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

## Corrective action

R4A3 FIX1 must:
- avoid all string+numeric output concatenation;
- evaluate numeric assertions inside Sigma and print only literal PASS/FAIL strings;
- test bytes_raw_utf8 through bytes_len/bytes_get;
- test str_len/str_byte directly;
- test crypto_digest candidate signatures by direct equality against expected SHA-256 text, without hex_encode;
- test exp-derived tanh by in-Sigma tolerance assertions.

NEXT=R4A3_FIX1_BOOLEAN_ASSERTION_MICROPROBES
