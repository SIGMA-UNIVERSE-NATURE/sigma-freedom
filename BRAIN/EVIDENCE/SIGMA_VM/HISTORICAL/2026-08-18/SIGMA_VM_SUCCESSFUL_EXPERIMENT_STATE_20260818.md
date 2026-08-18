# SIGMA VM — SUCCESSFUL EXPERIMENT STATE

**Recorded:** 2026-08-18  
**Environment represented by source evidence:** OPPO / Android / Termux / aarch64  
**Historical working tree:** `~/SIGMA/sigma_genesis1`  
**Classification:** `EVIDENCE_BACKED_SUCCESS_LEDGER_WITH_OPEN_HOLDS_PRESERVED`

## Source provenance

This state record is derived only from the following uploaded evidence:

1. `SIGMA_VM_CURRENT_STATE_2026-08-18_v2.md`
   - SHA-256: `4b4101ac53039c28e897ace135aeac8f3dec7cd798e58ae3a1d5cf1be0dc457c`
2. `SIGMA_VM_V09_FLOORDIV_UPGRADE_HANDOFF_2026-08-18_2140_VN.md`
   - SHA-256: `5cdaf2e5191d9d09431df910420b62c762de5a55c6063f97df6c252f6d046fa2`

This document records successful experimental milestones. It does not erase failures, enlarge tested scope, or replace the current experiment-map frontier.

---

## 1. v0.2 — actual ABI basic parity

Verified result:

```text
C VM:     RC=0, STDOUT=30, STDERR=EMPTY
SIGMA VM: RC=0, STDOUT=30, STDERR=EMPTY
OUTPUT_PARITY=PASS
```

Shared stdout SHA-256:

`f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c`

Status:

`V02_ACTUAL_ABI_BASIC_PARITY = PASS`

---

## 2. v0.3 — external SIGMBC01 load/decode/execute

Verified external input SHA-256:

`efcd04d2d31731f75faf5703e17d52a496bbdff5059e9108d71c86b4bdb804b9`

Verified result:

```text
C VM:     RC=0, STDOUT=30, STDERR=EMPTY
SIGMA VM: RC=0, STDOUT=30, STDERR=EMPTY
EXTERNAL_BYTECODE_OUTPUT_PARITY=PASS
```

Status:

`V03_EXTERNAL_SIGMBC01_LOAD_DECODE_EXECUTE = PASS`

---

## 3. v0.4 — runtime-selected multi-input parity

Locked VM bytecode SHA-256:

`9d943aa3aeb2616587ce776ff03dd7b8a4c028919668a9293e1b14f096c35ad1`

The same VM artifact executed multiple external inputs without recompilation:

```text
10 + 20 -> 30  = PARITY PASS
7 + 8   -> 15  = PARITY PASS
```

Status:

`V04_RUNTIME_SELECTED_MULTI_INPUT_PARITY = PASS`

---

## 4. v0.5 — arithmetic, unary and control-flow parity

Locked VM bytecode SHA-256:

`a41aed0465ae388613c7342f8de89a9e062a540e1ce5ac1a8e9f13e7d949ae85`

Verified gates:

```text
parity_binary_ops = PASS
parity_unary      = PASS
parity_if_while   = PASS
```

Status:

`V05_ARITHMETIC_UNARY_CONTROL_PARITY = PASS_WITH_TESTED_SCOPE`

---

## 5. v0.6 — generic function frame milestone

Locked VM bytecode SHA-256:

`4939c08e0f11c5eb087a68b93d3a2e93db4767d4d920479a98bbcb7606a853b8`

Two independent function programs passed against the C VM using the same VM artifact:

```text
ADD_TWO(40,2) -> 42
CALC(6,7,1), with local temp/result -> 43
```

Verified behavior within tested scope:

```text
VM_FIND_FUNCTION
GENERAL_USER_CALL
ARGUMENT_ORDER
PARAMETER_BINDING
FUNCTION_LOCAL_ENV
CHILD_FUNCTION_FRAME
OP_RETURN
RETURN_VALUE_TO_CALLER
```

Regression over the existing v0.5 test set:

```text
parity_binary_ops = PASS
parity_unary      = PASS
parity_if_while   = PASS
```

Status:

`V06_OVERALL = PASS_WITH_TESTED_SCOPE`

---

## 6. v0.7 — string constant materialization and parity

Locked artifacts:

```text
V07 source SHA-256:
7546aae17392254e14d98e52b93c0a1f86a7203ff49c804c898586a0f82e757d

V07 bytecode SHA-256:
e17478f9bc7d3a19935eb2b0f61472b7511bcca99cdaa19451b0997e839d34aa

String-capability runtime SHA-256:
35fa66823c456d6c346c882cdb0875d68e0e1afc7c0df2f576b82ea7569045df
```

Verified same-input output:

```text
C VM:       Xin chào SIGMA-Ψ!
SIGMA v0.7: Xin chào SIGMA-Ψ!
RC=0, STDERR=EMPTY, byte-for-byte parity=PASS
```

Status:

```text
TAG_STR_RUNTIME_MATERIALIZATION = PASS
HELLO_STRING_EXECUTION          = PASS
HELLO_STRING_PARITY             = PASS
V07_STRING_MILESTONE            = PASS_WITH_TESTED_SCOPE
```

---

## 7. v0.8 — exact FLOAT constant materialization and basic arithmetic parity

Locked artifacts:

```text
V08 source SHA-256:
518ee72897652dd64279a61d6e80fc73ef9963a35950f9506c6919c9f67c9d7a

V08 bytecode SHA-256:
f1dc7c419504dd7d0e8474c33c4e6b0b9c314303bbdc6aab05ef5874ac421df4

FLOAT runtime candidate SHA-256:
bef48163b4009a43758e63a70c8d683c46136d990f0f68995c19ffe41ccd20bc

FLOAT guest bytecode SHA-256:
5b77e209cd91629a1e7587d693d86de12cbe106e33bd322702ae849b02259618
```

Verified result:

```text
C reference: RC=0, STDOUT=3.75, STDERR=EMPTY
SIGMA v0.8:  RC=0, STDOUT=3.75, STDERR=EMPTY
BYTE-FOR-BYTE PARITY=PASS
```

Status:

```text
TAG_FLOAT_RUNTIME_MATERIALIZATION = PASS
FLOAT_BINARY_ADD_EXECUTION        = PASS
FLOAT_OUTPUT_PARITY               = PASS
V08_FLOAT_MILESTONE               = PASS_WITH_TESTED_SCOPE
```

---

## 8. v0.9 — successful sub-gates, overall HOLD preserved

The following v0.9 sub-gates succeeded:

```text
V09_C_GENERIC_PRIMITIVES        = SOURCE_VERIFIED
V09_C_STRICT_BUILD              = PASS
V09_C_REGRESSION_OVER_V08_FLOAT = PASS
V09_SIGMA_FLOORDIV_SOURCE       = SOURCE_VERIFIED
V09_SIGMA_COMPILE               = PASS
V09_SIGMA_BYTECODE_HASH         = LOCKED
```

Locked artifacts:

```text
Post-patch C source SHA-256:
df60a8258a6816476f625fe758b47cc7c5e0ad8188a373f00f169077542962d1

C runtime candidate SHA-256:
f764f1b34e8b46df21a95bc2ceb9dcc0eef3f53a265ea868b77784a5d707cac6

SIGMA v0.9 source SHA-256:
6259201f845821ce8dbb7c59912ee14505dc2e67134864a13f261fd0ed6d7d15

SIGMA v0.9 bytecode SHA-256:
e4f003abb2e1524038891531b6bc65d17ed2f036c49fd467aabbc5296fd874a6
```

The following did not pass at that checkpoint:

```text
FLOORDIV_EXACT_GUEST_COMPILE       = FAIL
FLOORDIV_EXACT_GUEST_COMPILE_CAUSE = NOT_YET_DIAGNOSED
FLOORDIV_C_REFERENCE               = NOT_YET
FLOORDIV_SIGMA_V09_EXECUTION       = NOT_YET
FLOORDIV_VALUE_PARITY              = NOT_YET
FLOORDIV_TYPE_PARITY               = NOT_YET
V09_OVERALL                        = HOLD
```

Observed compiler failure:

```text
sigmac: line 9 col 5: expected ';' (token=⚡)
```

No cause is inferred from the location alone.

---

## 9. Current experiment-map relationship

This historical successful-state ledger does not replace the later v12c/v13a evidence or the current dependency map.

```text
E04_BOUNDARY_BASELINE_005      = HOLD_MISSING_READABLE_CURRENT_ARTIFACTS
E04P_ARTIFACT_PROVISIONING_001 = REQUIRED
E06_FLOAT64_CANDIDATE          = BLOCKED
CURRENT_FRONTIER               = SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001
NO_STATE_DOWNGRADE             = TRUE
NO_CAPABILITY_PROMOTION        = TRUE
```

---

## 10. Mutation boundary

```text
SIGMA_LIFE_DIRECT_MUTATION = FALSE
CANONICAL_MERGE            = NONE
FOUNDATION_MERGE           = NONE
PHASE2_REOPEN              = NONE
512_PROMOTION              = NONE
```

End of evidence-backed successful experiment state.
