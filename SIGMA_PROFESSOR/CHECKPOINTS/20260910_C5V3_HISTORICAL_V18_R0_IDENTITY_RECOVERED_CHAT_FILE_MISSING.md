# C5V3 — Historical V18 R0 identity recovered while chat attachment is missing

Date: 2026-09-10 +07
Window: core architecture rewrite + synchronization

## Conversation-file state

The current chat file surface no longer contains the historical V18 R0 artifact. Do not invent its contents from memory.

## Git-history recovery

Historical canonical checkpoints at commits `8a1fdf466f8af27e4a9b0463bf723a0cee8eb32e`, `d410a82dc65c179a0a24c92fe2102be5cc6624ea`, `d8d9b07bf6cee595b99116b67d90816dc5245d0e`, and `5632ec1a96f75db15f0789acecc80bc1cd4c8f26` preserve the V18 R0 identities and runtime result.

```text
V18_R0_ENGINE_SOURCE_SHA256=81523feb7c59a90b6bb5d284c65a679d3fd76ad692f84b0a6685c4d2693dcb7a
V18_R0_ENGINE_BYTECODE_SHA256=e800eab3dc6abcbddf0b9c9e0de9d76af2fba6ba1bd49c87157c62fe126a7300
V18_R0_VERIFIER_PY_SHA256=a6664245d02e92dc78f8c7c73b07a58aca27d3dfa989ec9dd675b61aa45f2104
V18_R0_RUNNER_SHA256=747e98334b12e4efff8c11d48cea70a03952c167563d27b27eaf18626c06cb5f
V18_R0_VERIFIER_SHA256=6c7e65cf12ec169186b71bb2260c67d88edb425613eab17905c60513e035a027
V18_R0_WRAPPER_SHA256=d1926a7496a3a77c60832d433f421892bac6882e28e8156dc0554ea894aa5fe3
V18_R0_INSTALLER_SHA256=55c1df76afa8b3b5f7cd39d476f2d8809b4508bfa817bd94202945491d13043f
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Canonical local roots:

```text
PACKAGE_ROOT=$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/V1_R21_SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION_V18_R0
LIVE_RUN_ROOT=$ROOT/.sigma_exec/HH_AUTO_INTERNET_LESSONS/proposition_span_candidate_formations/20260903T041145Z_19479_11375
```

Canonical live result:

```text
FORMATION_VM_RC=0
FORMATION_VERIFY_RC=0
DRIVER_RC=0
INDEPENDENT_VERIFY_RC=0
UNIQUE_EXACT_EVIDENCE_UNITS=5
PROPOSITION_SPAN_CANDIDATE_COUNT=10
FORMATION_STATE=PROPOSITION_SPAN_CANDIDATES_AVAILABLE
SIGMA_NATIVE_PROPOSITION_SPAN_CANDIDATE_FORMATION=PASS_TESTED_SCOPE
```

Scope remains surface period segmentation only; semantic proposition formation was not proven.

## Importance to current compiler investigation

The exact same compiler and VM lineage produced a nontrivial V18 R0 bytecode hash `e800eab3...` and executed it successfully. Therefore the current R2/R3 FIX1 29-byte `SIGMBC01` zero-code artifact cannot be explained by claiming the locked compiler only supports trivial direct-print programs. R0 is now a required oracle for source/header/dialect/emitter comparison.

## Recovery gate

```text
C5_M5/RUN_C5V3_RECOVER_V18_R0_EXACT_ARTIFACTS_R1.sh
SCRIPT_COMMIT=556346c7c6819f4fc936288bcab182787a6c57b9
```

The gate inspects only the two exact historical R0 roots, hashes files, selects exact known V18 R0 identities, and exports matches to `/sdcard/Download/C5V3_V18_R0_RECOVERY_81523feb.zip`.

No VM execution or production mutation occurs.

`CLAIM <= EVIDENCE`
