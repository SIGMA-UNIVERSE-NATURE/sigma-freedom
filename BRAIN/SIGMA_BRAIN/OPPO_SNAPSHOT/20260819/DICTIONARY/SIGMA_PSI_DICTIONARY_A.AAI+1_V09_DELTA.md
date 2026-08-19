# SIGMA-Ψ DICTIONARY — A.AAI+1 V0.9 VERIFIED DELTA

BASE_DICTIONARY = SIGMA_PSI_DICTIONARY_A.AAI.md
BASE_HISTORY = PRESERVED
SOURCE_OVERWRITE = FALSE
UPGRADE_MODE = VERIFIED_SEMANTIC_DELTA

## 1. OPERATING LEARNING RULE

SIGMA development loop:

INPUT_REAL
-> SIGMA_OUTPUT_REAL
-> INSPECT_SEMANTICS
-> IF_WRONG_OR_INCOMPLETE:
       REPAIR_SIGMA
       TEACH_SIGMA
       RETEST
-> IF_MACHINE_EVIDENCE_PASS:
       LOCK_PASS
       UPDATE_SIGMA_PSI_DICTIONARY
-> NEXT_UNPROVEN_BEHAVIOR

Implementation must not advance while the SIGMA-Ψ dictionary/spec remains stale.

Goal:

C_SUBSTRATE_SEMANTICS
-> PROGRESSIVELY_TRANSFER_TO_SIGMA
-> SIGMA_DEFINES_MORE_OF_SIGMA
-> C_BECOMES_MINIMAL_GENERIC_SUBSTRATE

## 2. `//` — VERIFIED FLOORDIV + COMMENT DISAMBIGUATION

Previous A.AAI status:
`//` FLOORDIV = P
`//` comment = D

V0.9 verified lexical rule:

IF characters before `//` on the current line are only whitespace:
    `//` = LINE_COMMENT
ELSE:
    `//` = B_FLOORDIV

Therefore `//` is no longer globally ambiguous in the tested compiler path.

Examples:

// this is a comment

x = 7 // 2;

## 3. VERIFIED FLOORDIV SEMANTICS

Canonical current semantics:

INT // INT
-> V_INT

FLOAT // INT
-> V_FLOAT

INT // FLOAT
-> V_FLOAT

FLOAT // FLOAT
-> V_FLOAT

Floor is mathematical floor, including negative values.

Verified examples:

7 // 2
-> value 3
-> type V_INT = 2

-7 // 2
-> value -4
-> type V_INT = 2

7.5 // 2
-> value 3
-> type V_FLOAT = 3

7 // 2.5
-> value 2
-> type V_FLOAT = 3

## 4. VERIFIED RUNTIME TYPE CODES IN TESTED SCOPE

V_NULL  = 0
V_BOOL  = 1
V_INT   = 2
V_FLOAT = 3
V_STR   = 4

These are runtime ValueType identities.
They are NOT SIGMA lexer keywords merely because the runtime uses them.

## 5. GENERIC SUBSTRATE PRIMITIVES USED BY V0.9

value_type(a)
-> returns runtime type identity as V_INT

numeric_to_int(a)
-> canonical numeric conversion through substrate h_int behavior

math_floor(a)
-> floor operation returning V_FLOAT

host(...)
-> generic builtin/substrate dispatch boundary

These names belong to runtime/substrate ABI vocabulary.
They are NOT automatically SIGMA reserved keywords.

## 6. VM CALL FRONTIER LEARNED

SIGMA-written VM now includes generic builtin `host` dispatch in the
tested VM_CALL path.

This was learned from actual bytecode symbol evidence:

symbol 5 = host

Previous observed failure:

SIGMA_VM_ERROR UNDEFINED_FUNCTION_SYMBOL 5

After repair, host dispatch is generic and is not FLOORDIV-test hardcoding.

## 7. V0.9 MACHINE-EVIDENCE STATUS

V09_FLOORDIV_EXACT_PARITY             = PASS
V09_FLOAT_REGRESSION_PARITY           = PASS
V09_FUNCTION_LOCAL_REGRESSION_PARITY  = PASS
V09_BINARY_ARITH_REGRESSION_PARITY    = PASS
V09_UNARY_REGRESSION_PARITY           = PASS
V09_IF_WHILE_REGRESSION_PARITY        = PASS

V09_OVERALL = PASS_WITH_TESTED_SCOPE

FULL_VM_PARITY = NOT_CLAIMED

## 8. LOCKED V0.9 ARTIFACT IDENTITIES

sigmac.c
SHA256=e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452

sigma_vm.c
SHA256=8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2

native/sigmac.floordiv_candidate
SHA256=f7b9d6334f0d6cf231a220896c1bb0ef2761b6d7e1d9cd5e25f832988ee43d86

native/sigma-vm.v09_candidate
SHA256=320a084011fd7d5e9e743eccc59d5590ad1e5cf5e911c0c7ca1ea4a9b7e5904f

sigma_vm_core_v0_9_floordiv_exact.sigma
SHA256=61ebd4bf7889f24f59f48173b6ec163030539d68e8383e807f1eac1dce7c9ed2

sigma_vm_core_v0_9_floordiv_exact.host_candidate.sigmab
SHA256=7724cb684244b0300e699c65dafe9f35c52a32d2a95f184c585b4321e8329fe0

parity_floordiv_exact.sigma
SHA256=1d02eff3964abde2e88b78589a1e9c195deb21d70161602054a386331636bfdd

parity_floordiv_exact.candidate.sigmab
SHA256=bfd33a9d73fa18c547c3fea8f6c93e2450bc3fd1b3336052fec57a20aad208d4

parity_binary_ops.sigmab
SHA256=cd4547b97fb8c9cadfdcad63f697089d03ce67ade11e0d242f8515c395d078fb

parity_unary.sigmab
SHA256=d6f55a28201bea7cf50da1915df18c5c8a9a344e430b1e04c9fcd5283a0e4053

parity_if_while.sigmab
SHA256=12192e04c6fb49db43ccb8685e4d8348f96d0d39f7e1581ae62c74c76377b9ba

## 9. LANGUAGE-EVOLUTION RULE

A SIGMA-Ψ feature may be promoted only within the scope actually proven.

DO_NOT_INFER_PASS
DO_NOT_HARDCODE_TEST_OUTPUT
DO_NOT_HIDE_FAILURE
DO_NOT_REPLACE_SIGMA_SEMANTICS_WITH_NEW_C_SPECIAL_CASES

Preferred direction:

LOCATE
-> INSPECT
-> INPUT
-> SIGMA_OUTPUT
-> FIND_MISMATCH
-> REPAIR_OR_TEACH_IN_SIGMA
-> RETEST
-> MACHINE_EVIDENCE
-> UPDATE_DICTIONARY
-> CONTINUE

# END A.AAI+1 V0.9 VERIFIED DELTA
