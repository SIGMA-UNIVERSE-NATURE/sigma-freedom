# SIGMA VM — EXPERIMENT HANDOFF (COMPACT)

**Date:** 2026-08-18  
**Device:** OPPO / Termux / aarch64  
**Main tree:** `~/SIGMA/sigma_genesis1`  
**Status:** `PASS_WITH_DEFINED_SCOPE`  
**Current frontier:** `SIGMA VM v0.6 — GENERAL FUNCTION CALL / FRAME / RETURN`

---

## 1. Goal

Use **SIGMA itself** to progressively implement the SIGMA runtime/VM.

```text
NO FAKE PASS
NO INVENTED OPCODES
NO HARDCODED EXPECTED OUTPUT
NO TEST-SPECIFIC EXECUTION PATH
FAILURE = EVIDENCE
PASS ONLY AFTER REAL EXECUTION + PARITY
```

---

## 2. Actual ABI verified from `sigma_vm.c`

```text
0x01 PUSH_CONST
0x02 POP
0x10 LOAD
0x11 STORE
0x20 UNARY
0x21 BINARY
0x30 CALL
0x31 RETURN
0x40 JUMP
0x41 JUMP_IF_FALSE
0xFF HALT

U_NOT=0x01
U_NEG=0x02
U_POS=0x03

B_ADD=0x01
B_SUB=0x02
B_MUL=0x03
B_DIV=0x04
B_FLOORDIV=0x05
B_MOD=0x06
B_POW=0x07
B_EQ=0x10
B_NE=0x11
B_LT=0x12
B_GT=0x13
B_LE=0x14
B_GE=0x15
B_AND=0x20
B_OR=0x21
```

Important correction:

```text
OLD/WRONG: IADD = 0x10
ACTUAL:    OP_BINARY = 0x21, B_ADD = 0x01
```

LOAD/STORE:

```text
LOAD  = locals -> globals
STORE = globals in main; locals inside functions
```

---

## 3. Verified milestones

### v0.2 — Sigma-written VM, actual ABI

` sigma_vm_core_v0_2_actual_abi.sigma `

```text
C VM:     rc=0, stdout=30, stderr=empty
SIGMA VM: rc=0, stdout=30, stderr=empty
OUTPUT_PARITY=PASS
```

stdout SHA-256 both:

`f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c`

### Binary-read capability

Generic host primitives added:

```text
read_bytes(path)
bytes_get(bytes,index)
```

Verified:

```text
READ_BYTES_CAPABILITY=PASS
BYTES_GET_CAPABILITY=PASS
RAW_BYTE_PARITY=PASS
```

First 8 bytes read by SIGMA:

```text
83 73 71 77 66 67 48 49 = SIGMBC01
```

### v0.3 — External `.sigmab`

SIGMA performs:

```text
read_bytes
-> R8/R16/R32/RI64
-> verify SIGMBC01
-> decode constants/symbols/functions/main
-> execute
```

External input:

`vm_actual_abi_compare.sigmab`

SHA-256:

`efcd04d2d31731f75faf5703e17d52a496bbdff5059e9108d71c86b4bdb804b9`

```text
C VM:     rc=0, stdout=30, stderr=empty
SIGMA VM: rc=0, stdout=30, stderr=empty
EXTERNAL_BYTECODE_OUTPUT_PARITY=PASS
```

### v0.4 — Runtime-selected input

Input comes from:

```text
getenv("SIGMA_VM_INPUT")
```

VM binary SHA-256:

`9d943aa3aeb2616587ce776ff03dd7b8a4c028919668a9293e1b14f096c35ad1`

Same VM binary:

```text
Input A: 10+20 -> 30 => parity PASS
Input B: 7+8   -> 15 => parity PASS
all rc=0
all stderr=empty
```

### v0.5 — Arithmetic / unary / control flow

VM binary SHA-256:

`a41aed0465ae388613c7342f8de89a9e062a540e1ce5ac1a8e9f13e7d949ae85`

Evidence gate:

```text
parity_binary_ops  PARITY=PASS STDERR=PASS
parity_unary       PARITY=PASS STDERR=PASS
parity_if_while    PARITY=PASS STDERR=PASS
```

Verified within tested scope:

```text
UNARY: NOT / NEG / POS
BINARY: ADD / SUB / MUL / DIV / MOD / POW
        EQ / NE / LT / GT / LE / GE / AND / OR
CONTROL: JUMP / JUMP_IF_FALSE
```

`B_FLOORDIV` is not yet claimed as full parity.

---

## 4. Current failure frontier

v0.5 function test:

```text
SIGMA_VM_ERROR UNSUPPORTED_FUNCTION_SYMBOL 0
SIGMA_VM_EXTERNAL_RUN_FAIL 8
```

Not yet verified:

```text
GENERAL USER CALL
PARAMETER BINDING
FUNCTION LOCAL ENV
FUNCTION FRAME
OP_RETURN
RETURN VALUE TO CALLER
```

---

## 5. v0.6 audit and rebuild

A file named `sigma_vm_core_v0_6_function_frames.sigma` was initially identical to v0.5:

```text
V05_V06_SOURCE_IDENTICAL=YES
```

So previous v0.6 function claims were not accepted.

Pre-patch source SHA-256:

`c3190dcb104354c6ae3506a910f96b609e4d54d955af5329805317a428602c51`

Rebuild now proceeds step-by-step.

Already added to source:

```text
VM_NEW:
  + code
  + return_value

VM_NEW_CHILD(parent, code, locals):
  shared program/abi/globals
  private locals/stack/code/ip/return_value
  is_main=FALSE

VM_FIND_FUNCTION(program, sym):
  generic name_sym lookup
```

Current status:

```text
GENERAL_CALL_EXECUTION = NOT_YET_VERIFIED
OP_RETURN              = NOT_YET_VERIFIED
V06_OVERALL            = HOLD
```

---

## 6. Current verified state

```text
SIGMA executable language subset        = VERIFIED
Self-host compiler foundation           = VERIFIED
Actual ABI mapping                      = VERIFIED
VM written in SIGMA                     = VERIFIED
Raw binary read from SIGMA              = PASS
SIGMBC01 parsing by SIGMA               = PASS
External bytecode loading               = PASS
External bytecode execution             = PASS
Runtime-selected input                  = PASS
Same-VM multiple-program parity         = PASS
Arithmetic/unary/control parity         = PASS_WITH_TESTED_SCOPE

User-function CALL/frame/RETURN          = NOT_YET_VERIFIED
Full SIGMA VM                            = NOT_YET
SIGMA Brain                              = NOT_YET
```

---

## 7. Architecture reached

```text
SIGMA source
    ↓
SIGMA compiler
    ↓
SIGMA bytecode
    ↓
VM ENGINE WRITTEN IN SIGMA
    ↓
SIGMA reads external SIGMBC01
    ↓
SIGMA decodes actual bytecode
    ↓
SIGMA executes actual ABI
    ↓
parity against C VM
```

C remains substrate + generic host primitives while more runtime logic moves into SIGMA.

---

## 8. Next exact frontier

```text
SIGMA VM v0.6

OP_CALL
-> generic function lookup
-> argument order
-> parameter binding
-> child/local frame
-> execute function code
-> OP_RETURN
-> return value to caller
-> parity against C VM
```

**Do not call FULL VM PASS yet.**

---

**END — COMPACT EXPERIMENT HANDOFF**
