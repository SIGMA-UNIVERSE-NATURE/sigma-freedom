# C5V3 — V18 R0 exact artifact recovered / compiler oracle

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## Why this checkpoint exists

The historical V18 R0 attachment was no longer present on the current conversation file surface. Git history retained the exact immutable identities and canonical Oppo paths, allowing exact recovery without broad filesystem scanning.

## Historical identities recovered from canonical history

```text
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
V18_R0_ENGINE_SOURCE_SHA256=81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a
V18_R0_ENGINE_BYTECODE_SHA256=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300
V18_R0_VERIFIER_PY_SHA256=a6664245d02e92dc78f8c7c73b07a58aca27d3dfa989ec9dd675b61aa45f2104
V18_R0_RUNNER_SHA256=747e98334b12e4efff8c11d48cea70a03952c167563d27b27eaf18626c06cb5f
V18_R0_VERIFIER_SHA256=6c7e65cf12ec169186b71bb2260c67d88edb425613eab17905c60513e035a027
V18_R0_WRAPPER_SHA256=d1926a7496a3a77c60832d433f421892bac6882e28e8156dc0554ea894aa5fe3
```

Historical canonical run evidence includes:

```text
FORMATION_VM_RC=0
FORMATION_VERIFY_RC=0
DRIVER_RC=0
INDEPENDENT_VERIFY_RC=0
PROPOSITION_SPAN_CANDIDATE_COUNT=10
SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION=PASS_TESTED_SCOPE
```

Scope remains surface period-delimited span formation only; semantic proposition formation/equivalence was not proven.

## Exact Oppo recovery result

Recovery gate restricted itself to the two historical canonical roots and found exact SHA matches:

```text
PACKAGE_ROOT=.sigma_exec/HH_AUTO_INTERNET_LESSONS/V1_R21_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0
RUN_ROOT=.sigma_exec/HH_AUTO_INTERNET_LESSONS/proposition_span_candidate_formations/20260903T041145Z_19479_11375
BROAD_HOME_SCAN=NO

V18_R0_ENGINE_SOURCE_RECOVERED=YES
V18_R0_ENGINE_BYTECODE_RECOVERED=YES
V18_R0_VERIFIER_PY_RECOVERED=YES
V18_R0_RUNNER_RECOVERED=YES
V18_R0_VERIFIER_RECOVERED=YES
V18_R0_WRAPPER_RECOVERED=YES
V18_R0_INSTALLER_RECOVERED=NO
R0_SOURCE_AND_BYTECODE_RECOVERY=PASS
```

Recovered exact filenames include:

```text
15_SIGMA_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0.sigma
engines/proposition_span_candidate_formation_v18_r0.sigmab
25_RUN_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0.sh
30_VERIFY_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0.sh
32_VERIFY_PROPOSITION_SPAN_FORMATION_V18_R0.py
99_RUN_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0.sh
```

Recovery ZIP created on Oppo:

```text
/sdcard/Download/C5V3_V18_R0_RECOVERY_81523feb.zip
SHA256=7bb37b8943eee216d53e7b0e32cf9a7130d28d33aff5b9dd109e570db80506dc
BYTES=8104
```

The recovery ZIP is not yet present on the current conversation file surface. This does not invalidate the machine-local exact recovery.

## 29-byte anomaly state before R0 oracle comparison

Machine evidence already established:

```text
SIGMAC_REAL_PARSER=PASS
SIGMAC_SOURCE_SENSITIVE_EMITTER=PASS_IN_MINIMAL_DIRECT_PRINT_SCOPE
VM_REAL_BYTECODE_EXECUTION_CONTROL=PASS
VM_SIBLING_SOURCE_COUPLING=NO_OBSERVED
CURRENT_29B_CLASS=EMPTY_OR_GENERIC_EXECUTION_CAPSULE_UNDER_TESTED_ENVIRONMENT
SELF_COMPRESSION_OF_FULL_R2_R3_IN_29B=NOT_SUPPORTED_BY_CURRENT_BYTE_EVIDENCE
```

Therefore the exact historical R0 source+bytecode is now a required oracle for locating why R2/R3 full cores collapse to the valid header-only 29-byte `SIGMBC01` artifact while the same compiler/VM lineage previously emitted and executed nontrivial R0 bytecode.

## Exact next compiler oracle

Use:

```text
C5_M5/RUN_C5V3_R0_GATEA_VERSION_PROFILE_COMPILER_ORACLE_R1.sh
SCRIPT_COMMIT=fce160da5ca419e5c546a1406e136362d101811a
```

It performs no VM execution and no production mutation. It locks and freshly compiles:

```text
R0 original
Gate-A provisional-truth parent original
R3 FIX1 original
R0 with forced C5FULLR1 header
Gate-A with forced C5FULLR1 header
R3 FIX1 with Gate-A version header
```

Primary questions:

```text
Does current locked sigmac reproduce V18_R0 frozen bytecode e800eab3...?
Does it reproduce Gate-A historical bytecode 56941145...?
Does C5FULLR1 collapse otherwise-nontrivial full sources to the 29-byte header-only artifact?
Does Gate-A VERSION restore nontrivial emission for R3 FIX1?
```

No claim about the root cause is allowed until this oracle returns machine evidence.

## Boundary

```text
R3_FIX1_SOURCE_CONSTRUCTION=PASS
R3_FIX1_RUNTIME_ADMISSION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
PRODUCTION_PROMOTION_ALLOWED=NO
CLAIM_LEQ_EVIDENCE=MANDATORY
```
