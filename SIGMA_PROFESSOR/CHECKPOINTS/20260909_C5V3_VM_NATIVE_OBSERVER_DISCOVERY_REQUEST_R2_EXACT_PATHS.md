# C5V3 VM NATIVE OBSERVER DISCOVERY REQUEST R2 — EXACT PATHS ONLY

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **READ-ONLY / EXACT PATHS ONLY / R1 SUPERSEDED FOR DEVICE FOOTPRINT SAFETY / NO PRODUCTION BINDING**

## Why R2 supersedes R1

The Oppo SIGMA installation is large enough that broad filesystem discovery is operationally unsafe and unnecessary for this gate.

R1 included shallow directory inventories. Do not run R1 for this dependency.

R2 follows only exact, already-attested paths and performs no directory walk.

## Exact probe

`C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R2_EXACT_PATHS.sh`

Run:

```bash
bash C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R2_EXACT_PATHS.sh "$HOME/SIGMA/sigma_genesis1"
```

If the checkout is elsewhere, invoke the script by its actual checkout path and pass the install root explicitly.

Return stdout directly to Synchrony. Do not redirect into production/state directories.

## Exact paths read

Only these known paths are identity-locked:

```text
$ROOT/native/sigma-vm.v09_candidate
$ROOT/native/sigmac
$ROOT/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh
```

After all three identities match the frozen hashes, observer discovery reads only the exact VM binary plus the exact runner:

- `strings` on the exact VM binary for observer/trace/debug/dispatch-related tokens;
- `readelf -Ws` on the exact VM binary only if `readelf` is already installed;
- exact-file `grep` on the exact runner.

## Explicitly forbidden by R2

```text
find=NO
grep -R=NO
recursive filesystem scan=NO
native directory inventory=NO
control directory inventory=NO
state tree read=NO
log tree read=NO
package install=NO
network=NO
VM execution=NO
core execution=NO
VM patch=NO
core instrumentation=NO
production write=NO
```

If any locked identity mismatches, the probe stops observer discovery fail-closed.

## Frozen identities

```text
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
PRODUCTION_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
```

## Interpretation

A matching string/symbol is only an observer candidate, not an R11 PASS.

Synchrony will classify returned evidence as:

```text
A TRUSTWORTHY_EXISTING_NATIVE_OBSERVER_CANDIDATE
B NON_EXECUTION_OR_UNRELATED_DEBUG_HINT
C NO_TRUSTWORTHY_OBSERVER_FOUND
D RUNTIME_IDENTITY_MISMATCH
```

`R11_ACTIVATION_PASS=NOT_CLAIMED`
`PRODUCTION_BINDING=NO`
`PRODUCTION_MUTATION=NO`
`CLAIM <= EVIDENCE`
