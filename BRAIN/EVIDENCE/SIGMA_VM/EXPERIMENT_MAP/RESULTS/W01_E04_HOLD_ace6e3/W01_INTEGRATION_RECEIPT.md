# W01 / E04 INTEGRATION RECEIPT — HOLD

Map ID: `SIGMA-VM-EXPERIMENT-MAP-20260818-001`

Window: `W01_BOUNDARY_AUDITOR`

Node: `E04_BOUNDARY_BASELINE_005`

Pinned parent checkpoint: `ace6e3b99e96210d064f6093aabbb72733b9da8c`

Integrated verdict:

`W01_RESULT_HOLD`

Exact reason:

The pinned GitHub checkpoint did not contain directly readable copies of the current SIGMA VM candidate source, compiled VM bytecode, trusted C adapter source, compiled host binary, frozen ABI artifact, or Foundation V7 source tree. Therefore W01 correctly refused to infer the five primitive names, the absence of `math_floordiv`, or the status of `bytes_f64_le_at` from prior reports.

## Reported output hashes

- `TRUSTED_HOST_BOUNDARY_BASELINE_005.json`: `da0cf5a4696ecc23571000480b8fb899900e6397ec9f1a859078e640fd276a1f`
- `STATIC_CALLSITE_MAP.json`: `9b576b19bc512dac3fe38575b876be12394101ed5453715456a39d521f02e921`
- `BINARY_SYMBOL_OR_STRING_AUDIT.json`: `273a7b94ea758c8c424911187f6e2dc5497dc8445f5d91399f479e3d044986df`
- `W01_HANDOFF.md`: `bcf4aa3dab907bdfbe175b433e84fcf3d748cbcdd7d450177f1293b3ccea94c2`

The artifact bodies were not available in this integration window and are not represented as independently fetched GitHub files. The hashes are recorded as handoff-reported hashes, not as remote-content verification.

## Integrator discovery

The missing source/binary materials were subsequently located in retained evidence packages in the integrator runtime:

- `SIGMA_VM_TRUSTED_HOST_BOUNDARY_REDUCTION_001_20260818.zip`
  - SHA-256: `36e261aaa1ab5af3bc58df8ece202a5294247577ba549da5ba718adc2bc41c12`
- `SIGMA_FOUNDATION_FINAL_CERTIFICATION_V7_20260817.zip`
  - SHA-256: `af60963ddfcf33900fc44e4eeeb8e610279d9583f6746c2a6d93a3c49fc1e66e`

Verified contents of the retained packages include:

- candidate source `sigma_vm_self_v12c.sigma` — `9ae630ecdfedc4975215bf91465eb4319061a2eb89019e1e8f874eea07b3a50d`
- candidate bytecode `sigma_vm_self_v12c.sigmab` — `f5edf70a99821c680874afd305104a08ffdcda3dff95e4e235e7a5655f3f45c4`
- adapter source `sigma_vm_host_adapter_v12.c` — `2e9e6682168f6f8068df465e882e7f74f23edd74644cfc7ca776591324019a98`
- host binary `sigma-hostvm-v12` — `5236a300afa098694beb04bf9e146ca0d8823396b25829449930277279117899`
- frozen ABI `SIGMA_BYTECODE_ABI_v1.json` — `c48c9883c6aedaa1ca7bfbc04b2ad05335040375bed942be73ae3ace9a5b8416`

These discoveries do not convert W01 HOLD to PASS. W01 must be rerun against an immutable, readable, SHA-pinned provisioning checkpoint.

## Dependency consequence

- `E04_BOUNDARY_BASELINE_005 = HOLD_MISSING_READABLE_ARTIFACTS`
- `E06_FLOAT64_REPRESENTATION_CANDIDATE_001 = BLOCKED`
- `W03_F64_IMPLEMENTER = DO_NOT_OPEN`

`E05_FLOAT64_CORPUS_FREEZE_001` is a separate branch of the dependency graph. W01's instruction not to start E05 applied to W01 itself; it did not grant W01 authority to cancel W02. W02 may proceed only if its own frozen-ABI entry gate can be satisfied without inference.

## New required node

`E04P_ARTIFACT_PROVISIONING_001`

Purpose: persist immutable readable/reconstructable source and binary artifacts, exact SHA-256 inventory, and reconstruction instructions; then rerun W01 against that new checkpoint.

No implementation, ABI, Foundation, Phase 2, canonical, or 512 mutation occurred.
