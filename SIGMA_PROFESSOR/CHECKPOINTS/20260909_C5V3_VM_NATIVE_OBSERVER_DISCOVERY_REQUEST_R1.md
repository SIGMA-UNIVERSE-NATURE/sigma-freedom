# C5V3 VM NATIVE OBSERVER DISCOVERY REQUEST R1

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **READ-ONLY R11 DEPENDENCY DISCOVERY / NO CORE OR VM EXECUTION / NO PRODUCTION BINDING**

## Why this request exists

R10 is the latest admitted production-lineage successor candidate, but R11 activation has not been admitted.

R11 observer attempts currently end at HOLD:

```text
step-budget oracle=HOLD
FIX1 normalized output/filesystem=HOLD, observable delta 0/28
FIX2 syscall/file trace=HOLD, STRACE_AVAILABLE=NO
FIX3 FIFO fault-injection=HOLD, no calibrated trap path
```

The R11 FIX3 checkpoint requires inspection of the locked VM/runtime for an already-existing trustworthy native execution/debug/host-dispatch observation facility before inventing any further activation oracle.

## Canonical read-only probe

`C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R1.sh`

Run from a checkout containing the script while passing the actual installation root explicitly:

```bash
bash C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R1.sh "$HOME/SIGMA/sigma_genesis1"
```

If the checkout is elsewhere:

```bash
bash /path/to/checkout/C5_M5/RUN_C5V3_VM_NATIVE_OBSERVER_DISCOVERY_R1.sh "$HOME/SIGMA/sigma_genesis1"
```

Return stdout directly to Synchrony.

Do not redirect it into production state/root.

## What the probe does

Read-only/static inspection only:

- hash-lock the known VM, sigmac and production runner;
- inventory only the shallow `native/` directory;
- inspect VM ASCII strings for trace/debug/opcode/instruction/dispatch/host/profile/dump/step/event/log/observer hints;
- inspect flag-like and `SIGMA_*` environment-like tokens;
- if already installed, use `readelf`/`objdump` only as read-only symbol readers;
- inspect the runner and control scripts for existing observer/debug references.

The probe does **not** execute the VM or core and does not call a network.

## Required interpretation

A token such as `trace`, `debug`, or `dump` in a binary is only a hint. It is not proof of a usable observer.

Synchrony must classify any discovered facility as one of:

```text
A. TRUSTWORTHY_EXISTING_NATIVE_OBSERVER_CANDIDATE
   -> design an R11 follow-up using exact frozen R10 without core instrumentation or semantic expected output

B. NON_EXECUTION_OBSERVER_OR_UNRELATED_DEBUG_HINT
   -> do not use it for R11

C. NO_TRUSTWORTHY_OBSERVER_FOUND
   -> retain R11 HOLD; do not manufacture a PASS

D. RUNTIME_IDENTITY_MISMATCH
   -> HOLD and reconcile runtime identity before any further test
```

## Frozen identities

```text
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
PRODUCTION_RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
```

## Safety locks

```text
NETWORK=NO
PACKAGE_INSTALL=NO
VM_EXECUTION=NO
CORE_EXECUTION=NO
CORE_INSTRUMENTATION=NO
VM_PATCH=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
PRODUCTION_BINDING=NO
R11_ACTIVATION_PASS=NOT_CLAIMED
```

`CLAIM <= EVIDENCE`
