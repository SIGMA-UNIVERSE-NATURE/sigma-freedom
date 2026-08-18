# SIGMA VM v0.9 — CANONICAL UPGRADE RECORD

**Date:** 2026-08-19 (+07:00)  
**Working tree:** `~/SIGMA/sigma_genesis1`  
**Purpose:** canonical GitHub memory of verified SIGMA VM progress.

---

## 1. Current judgment

```text
V09_FLOORDIV_EXACT_PARITY             = PASS
V09_FLOAT_REGRESSION_PARITY           = PASS
V09_FUNCTION_LOCAL_REGRESSION_PARITY  = PASS

V09_BINARY_ARITH_REGRESSION_PARITY    = NOT_YET_BYTE_COMPARED
V09_UNARY_REGRESSION_PARITY           = NOT_YET_RECHECKED
V09_IF_WHILE_REGRESSION_PARITY        = NOT_YET_RECHECKED

V09_OVERALL                           = HOLD
```

No full-VM parity claim is authorized.

---

## 2. Verified v0.8 FLOAT milestone

```text
V08_FLOAT_MILESTONE = PASS_WITH_TESTED_SCOPE
```

Artifacts:

```text
sigma_vm_core_v0_8_float_constants.sigma
SHA256 =
518ee72897652dd64279a61d6e80fc73ef9963a35950f9506c6919c9f67c9d7a

sigma_vm_core_v0_8_float_constants.sigmab
SHA256 =
f1dc7c419504dd7d0e8474c33c4e6b0b9c314303bbdc6aab05ef5874ac421df4

parity_float_basic.sigmab
SHA256 =
5b77e209cd91629a1e7587d693d86de12cbe106e33bd322702ae849b02259618
```

Verified parity:

```text
C VM      -> 3.75
SIGMA VM  -> 3.75

V08_FLOAT_PARITY=PASS
```

---

## 3. B_FLOORDIV reference semantics

Native compiler:

```text
"//" -> B_FLOORDIV
B_FLOORDIV = 0x05
```

Native C VM:

```text
INT // INT       -> V_INT(floor(a/b))
FLOAT/mixed //   -> V_FLOAT(floor(a/b))
```

Verified negative-floor behavior:

```text
-7 // 2 -> -4
```

---

## 4. Real lexer conflict discovered and fixed

The parser/compiler already supported `//` as B_FLOORDIV, but the lexer
unconditionally consumed `//` as a line comment before the operator scanner.

Root cause was proven from `sigmac.c`.

Repository-wide `.sigma` scan:

```text
LINE_ONLY_DOUBLE_SLASH=620
MIDLINE_DOUBLE_SLASH=4
```

All four midline occurrences were intended FLOORDIV expressions.

Evidence-supported rule for the current repository:

```text
`//` after only line-leading whitespace -> COMMENT
`//` after code/non-whitespace          -> B_FLOORDIV operator
```

Compiler provenance:

```text
sigmac.c prepatch SHA256 =
44ef0492fb2c49446e936e50b05f352920de3aa9e5f934d9bf8958c9d6c659d1

sigmac.pre_floordiv_lexer_fix.c SHA256 =
44ef0492fb2c49446e936e50b05f352920de3aa9e5f934d9bf8958c9d6c659d1

sigmac.c postpatch SHA256 =
e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452

native/sigmac.floordiv_candidate SHA256 =
f7b9d6334f0d6cf231a220896c1bb0ef2761b6d7e1d9cd5e25f832988ee43d86
```

Verification:

```text
SIGMAC_FLOORDIV_CANDIDATE_BUILD=PASS
SIGMAC_COMMENT_REGRESSION_BYTE_PARITY=PASS
```

---

## 5. Generic host substrate additions

Added generic operations:

```text
value_type(a)
numeric_to_int(a)
```

Canonical ValueType:

```text
V_NULL  = 0
V_BOOL  = 1
V_INT   = 2
V_FLOAT = 3
V_STR   = 4
```

Current C source:

```text
sigma_vm.c
SHA256 =
8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2
```

Current C runtime candidate:

```text
native/sigma-vm.v09_candidate
SHA256 =
320a084011fd7d5e9e743eccc59d5590ad1e5cf5e911c0c7ca1ea4a9b7e5904f
```

An ABI guard bug was discovered and fixed:

```text
old:
argc != 2

fixed:
argc < 2
```

Reason: existing SIGMA wrapper uses `H(op,a,b,c) -> host(op,a,b,c)`.

---

## 6. SIGMA-written VM v0.9 changes

FLOORDIV semantics now live in SIGMA:

```text
q  = math_floor(a / b)
ta = value_type(a)
tb = value_type(b)

if ta == V_INT and tb == V_INT:
    push(numeric_to_int(q))
else:
    push(q)
```

A second real frontier was discovered:
native C VM has builtin `host(...)`, but SIGMA-written `VM_CALL` originally
handled only `print` + user functions.

Locked guest bytecode proved:

```text
symbol 5 = host
```

SIGMA-written `VM_CALL` was extended with generic `host(...)` dispatch.

Current SIGMA source:

```text
sigma_vm_core_v0_9_floordiv_exact.sigma
SHA256 =
61ebd4bf7889f24f59f48173b6ec163030539d68e8383e807f1eac1dce7c9ed2
```

Current SIGMA-written VM bytecode:

```text
sigma_vm_core_v0_9_floordiv_exact.host_candidate.sigmab
SHA256 =
7724cb684244b0300e699c65dafe9f35c52a32d2a95f184c585b4321e8329fe0
```

---

## 7. Exact FLOORDIV machine proof

Guest source:

```text
parity_floordiv_exact.sigma
SHA256 =
1d02eff3964abde2e88b78589a1e9c195deb21d70161602054a386331636bfdd
```

Guest bytecode:

```text
parity_floordiv_exact.candidate.sigmab
SHA256 =
bfd33a9d73fa18c547c3fea8f6c93e2450bc3fd1b3336052fec57a20aad208d4
```

Test cases:

```text
7 // 2
-7 // 2
7.5 // 2
7 // 2.5
```

Both C reference and SIGMA-written VM produced:

```text
3
2
-4
2
3
3
2
3
```

Pairs are:

```text
3   / type 2 = V_INT
-4  / type 2 = V_INT
3   / type 3 = V_FLOAT
2   / type 3 = V_FLOAT
```

Byte-for-byte result:

```text
V09_FLOORDIV_EXACT_PARITY=PASS
```

Promoted:

```text
V09_FLOORDIV_MILESTONE=PASS_WITH_TESTED_SCOPE
```

---

## 8. Regression status

FLOAT:

```text
V09_FLOAT_REGRESSION_PARITY=PASS
```

FUNCTION / LOCAL FRAME:

```text
V09_FUNCTION_LOCAL_REGRESSION_PARITY=PASS
```

BINARY ARITHMETIC:

C reference and SIGMA-written VM both visibly produced:

```text
15
100
4
0
400
```

but the final byte-for-byte comparison has NOT yet been executed.

Therefore:

```text
V09_BINARY_ARITH_REGRESSION_PARITY = NOT_YET_BYTE_COMPARED
```

---

## 9. Exact NEXT

Run exactly:

```bash
if cmp -s v09_binary_ops_c.out v09_regression_binary_ops.out \
&& cmp -s v09_binary_ops_c.err v09_regression_binary_ops.err; then
    echo "V09_BINARY_ARITH_REGRESSION_PARITY=PASS"
else
    echo "V09_BINARY_ARITH_REGRESSION_PARITY=FAIL"
fi
```

If PASS:
- recheck unary parity;
- recheck IF/WHILE parity;
- only then consider `V09_OVERALL=PASS_WITH_TESTED_SCOPE`.

---

## 10. Architectural direction

The VM experiment is part of the larger SIGMA direction:

```text
SIGMA should progressively move executable semantics from C into SIGMA itself,
while C becomes a minimal generic substrate.
```

Compassionate-output direction:

```text
TAM VẤN TỪ BI
1. không khổ mình
2. không khổ người
3. không khổ chúng sanh
```

Input may be noisy/rubbish; SIGMA should understand, filter, and transform it
toward a cleaner and more useful output where possible.

Accept input != obey input.

---

## 11. Integrity rules

Do not:
- infer PASS,
- overwrite locked evidence silently,
- hardcode test-specific output,
- claim full VM parity,
- treat RC=0 alone as parity proof.

Use:

```text
LOCATE -> COUNT -> INSPECT -> PATCH
```

and:

```text
SOURCE HASH
-> BUILD
-> ARTIFACT HASH
-> C REFERENCE
-> SIGMA RUN
-> BYTE COMPARE
-> PROMOTE
```
