# C5V3 R10 SHADOW RUNNER MATERIALIZE REQUEST R1

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **ACTIVE SYNCHRONIZATION MATERIALIZATION REQUEST / BUILD-AUDIT ONLY / SHADOW EXECUTION FORBIDDEN**

## Purpose

Advance the already-PASS staged R10 successor from static payload presence to an exact mechanically derived shadow runner binding, without executing the runner or touching live production.

Upstream PASS:

```text
R10_SUCCESSOR_STAGE=PASS
C5V3_SUCCESSOR_CAPABILITY_PAYLOAD_STAGED=YES
T1_T2_T3_PRESENT_IN_STAGED_SUCCESSOR=YES
M5_DISPATCH_BRIDGE_IDENTITY=INHERITED_EXACT_R10
LIVE_CORE_UNCHANGED=YES
LIVE_RUNNER_UNCHANGED=YES
```

Exact production-runner contract extraction is also PASS.

## Canonical script

```text
C5_M5/RUN_C5V3_R10_SHADOW_RUNNER_MATERIALIZE_R1.sh
```

Invocation:

```bash
bash C5_M5/RUN_C5V3_R10_SHADOW_RUNNER_MATERIALIZE_R1.sh "$HOME/SIGMA/sigma_genesis1"
```

If using a downloaded script, invoke it by exact downloaded path and pass the installation root explicitly.

## What this gate may write

Only under:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_c5v3_sync/C5V3_R10_SUCCESSOR_STAGE_R1
```

It may:

- copy the exact live mechanical bridge, reflective-review source/bridge/bytecode after verifying identities locked by the exact live runner;
- derive a shadow runner from the exact hash-locked production runner;
- mechanically redirect `INSTALL` to the staged R10 install;
- mechanically redirect default `C5` state to the staged successor state;
- replace only `EXPECTED_NATIVE_SOURCE` with the exact frozen R10 source SHA256;
- syntax-check and hash the derived runner;
- audit direct shared-root references.

It may not execute the shadow runner, VM, core, cataloger, network fetch, or state-learning loop.

## Exact frozen identities

```text
LIVE_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
LIVE_REVIEW_SOURCE_SHA256=95fac3da14a79b969a362d0dadd7823b66612c91d6dca4b0f4b5708f1eb010b7
LIVE_REVIEW_BYTECODE_SHA256=424742773403cfb3c0ffcce0615b2cc8ff0998c5c2e828b313820b8fe817e4d3
```

Mechanical/review bridge hashes are extracted from the exact locked runner and then checked against the exact live bridge files before staging.

## Large-tree safety

This gate uses exact paths only:

```text
DIRECTORY_WALK=NO
FIND=NO
GREP_RECURSIVE=NO
RUNNER_EXECUTION=NO
CATALOGER_EXECUTION=NO
NETWORK=NO
```

The shadow runner is deliberately **not execution-ready** after this materialization gate. Before execution, Synchrony must reconcile the exact cataloger/local-archive contract and any shared `$ROOT/.sigma_native` references so an isolated run cannot traverse the approximately 30 GB SIGMA tree unintentionally or import production knowledge.

## Expected PASS boundary

```text
SHADOW_RUNNER_MATERIALIZE=PASS
R10_SHADOW_INSTALL_BINDING_MATERIALIZED=YES
R10_SHADOW_STATE_BINDING_MATERIALIZED=YES
EXACT_BRIDGE_REVIEW_DEPENDENCIES_STAGED=YES
R10_EXPECTED_MAIN_SOURCE_IDENTITY_PATCHED=YES
SHADOW_RUNNER_EXECUTION=NO
LIVE_CORE_UNCHANGED=YES
LIVE_RUNNER_UNCHANGED=YES
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

## Next gate after PASS

```text
shadow runner materialization PASS
-> exact cataloger/local-archive/fetch block extraction from the same runner only
-> prove no broad 30 GB traversal and no production-knowledge import
-> shadow execution preflight
-> R11 native activation observation/admission
-> isolated online utilization and learning/restart/reuse
-> promotion/cutover gates
```

`CLAIM <= EVIDENCE`
