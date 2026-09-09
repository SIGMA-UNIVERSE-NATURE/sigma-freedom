# C5V3 — 29B empty capsule confirmed / historical V18 R0 compiler oracle recovered

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization
Production mutation: NO

## 29-byte capsule classification — machine result

Locked identities:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
CANONICAL_29B_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

Exact isolated VM test:

```text
29B + sibling source A -> VM_RC=0, stdout=empty, stderr=empty
29B + sibling source B -> VM_RC=0, stdout=empty, stderr=empty
29B + no source        -> VM_RC=0, stdout=empty, stderr=empty
VM_SIBLING_SOURCE_COUPLING=NO_OBSERVED
CURRENT_29B_CLASS=EMPTY_OR_GENERIC_EXECUTION_CAPSULE_UNDER_TESTED_ENVIRONMENT
```

Positive controls:

```text
real emitted bytecode A -> BYTECODE_A_SENTINEL, VM_RC=0
real emitted bytecode B -> BYTECODE_B_SENTINEL, VM_RC=0
VM_REAL_BYTECODE_EXECUTION_CONTROL=PASS
```

Therefore:

```text
FULL_R2_R3_SELF_COMPRESSION_IN_29B=NOT_SUPPORTED
29B_SOURCE_REFERENCE_LOADER=NO_OBSERVED
R2_R3_CURRENT_BYTECODE=EMPTY_OR_GENERIC_EXECUTABLE_CAPSULE
R3_FIX1_RUNTIME_ADMISSION=NO
```

The historical SIGMA structural-compression capability is not invalidated; it is simply not the mechanism producing this 29-byte artifact.

## Historical V18 R0 oracle recovered from Git history

The chat attachment itself is currently missing from conversation file surface, but historical canonical commits preserve exact identities:

```text
V18_R0_ENGINE_SOURCE_SHA256=81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a
V18_R0_ENGINE_BYTECODE_SHA256=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300
V18_R0_VERIFIER_PY_SHA256=a6664245d02e92dc78f8c7c73b07a58aca27d3dfa989ec9dd675b61aa45f2104
V18_R0_RUNNER_SHA256=747e98334b12e4efff8c11d48cea70a03952c167563d27b27eaf18626c06cb5f
V18_R0_VERIFIER_SHA256=6c7e65cf12ec169186b71bb2260c67d88edb425613eab17905c60513e035a027
V18_R0_WRAPPER_SHA256=d1926a7496a3a77c60832d433f421892bac6882e28e8156dc0554ea894aa5fe3
V18_R0_INSTALLER_SHA256=55c1df76afa8b3b5f7cd39d476f2d8809b4508bfa817bd94202945491d13043f
```

Canonical V18 R0 live run:

```text
V18_R0_RUN=$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/proposition_span_candidate_formations/20260903T041145Z_19479_11375
FORMATION_VM_RC=0
FORMATION_VERIFY_RC=0
DRIVER_RC=0
INDEPENDENT_VERIFY_RC=0
PROPOSITION_SPAN_CANDIDATE_COUNT=10
SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION=PASS_TESTED_SCOPE
```

Same compiler/VM hashes were locked. Therefore V18 R0 is now a required oracle for understanding why R2/R3 compile to zero-code while older exact SIGMA engines compiled to nontrivial bytecode.

## Recovery gate

```text
C5_M5/RUN_C5V3_RECOVER_V18_R0_EXACT_ARTIFACTS_R1.sh
SCRIPT_COMMIT=556346c7c6819f4fc936288bcab182787a6c57b9
OUTPUT=/sdcard/Download/C5V3_V18_R0_RECOVERY_81523feb.zip
```

The gate searches only the two exact canonical R0 roots and selects files by known SHA256. No VM execution or production mutation.

## Next compiler investigation

After exact R0 source/bytecode recovery:

```text
R0 source/header/dialect/emitter comparison
-> fresh R0 recompile with locked sigmac
-> verify expected/nonzero code emission
-> isolate the smallest source/header/composition delta that turns R3 into 29B zero-code
-> repair R3 source composition or compiler-facing contract
-> re-run compiler counterfactual + negative controls
-> only then resume R3 FIX1 runtime admission
```

`CLAIM <= EVIDENCE`
