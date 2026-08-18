# SIGMA VM — CURRENT EXPERIMENT STATE

**Updated:** 2026-08-18
**Device:** OPPO / Termux / aarch64
**Main tree:** `~/SIGMA/sigma_genesis1`
**Mode:** ONE_EXPERIMENT_AT_A_TIME / EVIDENCE_ONLY

## Verified milestones

```text
v0.2 ACTUAL ABI BASIC PARITY             = PASS
v0.3 EXTERNAL SIGMBC01 LOAD/DECODE       = PASS
v0.4 RUNTIME-SELECTED MULTI-INPUT PARITY = PASS
v0.5 ARITHMETIC/UNARY/CONTROL PARITY     = PASS
```

v0.5 bytecode SHA-256:

```text
a41aed0465ae388613c7342f8de89a9e062a540e1ce5ac1a8e9f13e7d949ae85
```

v0.5 evidence gate:

```text
parity_binary_ops  PARITY=PASS STDERR=PASS
parity_unary       PARITY=PASS STDERR=PASS
parity_if_while    PARITY=PASS STDERR=PASS
```

## v0.6 audit

The initial file named `sigma_vm_core_v0_6_function_frames.sigma`
was proven identical to v0.5:

```text
V05_V06_SOURCE_IDENTICAL=YES
```

Therefore any earlier v0.6 function PASS claim is not accepted.

Pre-patch v0.6 source SHA-256:

```text
c3190dcb104354c6ae3506a910f96b609e4d54d955af5329805317a428602c51
```

Historical backup:

```text
sigma_vm_core_v0_6_function_frames.pre_patch.sigma
```

## v0.6 rebuild — source patches applied so far

```text
VM_NEW_PATCH          = APPLIED / SOURCE-VERIFIED
VM_NEW_CHILD_PATCH    = APPLIED / SOURCE-VERIFIED
VM_FIND_FUNCTION_PATCH= APPLIED / NOT_YET_SOURCE-INSPECTED
```

`VM_NEW` now includes:

```text
code
return_value
is_main=TRUE
```

`VM_NEW_CHILD(parent, code, locals)` now uses:

```text
shared:  program / abi / globals
private: locals / stack / code / ip / halted / return_value
is_main=FALSE
```

`VM_FIND_FUNCTION(program, sym)` was just inserted as a generic
`name_sym` lookup. Its actual source has not yet been inspected after patch.

## Current frontier

```text
GENERAL USER CALL      = NOT_YET_VERIFIED
ARGUMENT ORDER         = NOT_YET_VERIFIED
PARAMETER BINDING      = NOT_YET_VERIFIED
FUNCTION LOCAL FRAME   = NOT_YET_VERIFIED
OP_RETURN              = NOT_YET_VERIFIED
RETURN VALUE TO CALLER = NOT_YET_VERIFIED

V06_OVERALL = HOLD
```

## Discipline

```text
ONE OPPO STEP AT A TIME
NO FAKE PASS
NO TEST-SPECIFIC HARDCODE
NO CLAIM FROM FILE NAME
NO CLAIM FROM RC=0 ALONE
FAILURE IS EVIDENCE
UPDATE STATE AFTER EACH VERIFIED STEP
```

## Exact next step

Inspect the source of `VM_FIND_FUNCTION` only.
Do not patch VM_CALL or OP_RETURN yet.
