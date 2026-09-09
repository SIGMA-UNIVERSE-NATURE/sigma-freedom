# C5V3 EXACT PRODUCTION RUNNER CONTRACT R1 — PASS

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **IMMUTABLE READ-ONLY MACHINE-EVIDENCE CHECKPOINT / EXACT RUNNER CONTRACT EXTRACTED / NO PRODUCTION MUTATION**

## Purpose

Record the operator-returned read-only extraction of the exact live production runner needed to derive an isolated R10 shadow binding mechanically rather than by assumption.

No directory walk, recursive grep, state-tree read, log read, VM/core execution, network action, or production write was performed.

## Exact runner identity

```text
RUNNER=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5/control/RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V3_REFLECTIVE.sh
RUNNER_SHA256=092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847
RUNNER_IDENTITY=PASS
```

## Exact code/state binding contract

The runner separates code install from state root:

```text
INSTALL="$ROOT/.sigma_c5"
C5="${C5_STATE_ROOT:-$INSTALL}"
SRC="$INSTALL/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma"
BRIDGE="$INSTALL/tools/SIGMA_C5_MECHANICAL_BRIDGE_V2.py"
BIN="$INSTALL/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab"
REVIEW_SRC="$INSTALL/src/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigma"
REVIEW_BRIDGE="$INSTALL/tools/SIGMA_C5_MECHANICAL_REVIEW_BRIDGE_V3.py"
REVIEW_BIN="$INSTALL/bin/SIGMA_C5_NATIVE_REFLECTIVE_REVIEW_V3.sigmab"
RUNTIME="$C5/runtime"
STATE_DB="$C5/state/state.sqlite3"
CATALOG_DB="$C5/catalog/catalog_v2.sqlite3"
EXTERNAL_ROOT="$C5/external"
DECODED_ROOT="$C5/decoded"
LOG="$C5/log"
LOCK="$C5/runner.lock"
ERROR_VAULT="$C5/error_vault"
REVIEW_REPORT_DIR="$C5/review/reports"
```

This permits an isolated successor design in which `INSTALL` points to the staged R10 install while `C5` points to a dedicated successor state root.

## Exact runtime invocation contract

The runner compiles and executes only through the locked runtime paths:

```text
SIGMAC="$ROOT/native/sigmac"
VM="$ROOT/native/sigma-vm.v09_candidate"
"$SIGMAC" "$SRC" "$BIN.partial"
"$SIGMAC" "$REVIEW_SRC" "$REVIEW_BIN.partial"
"$VM" "$BIN"
"$VM" "$REVIEW_BIN"
```

Previously attested locked identities remain:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Mutation surface

The runner writes through `$INSTALL` and `$C5` derived paths, including bytecode, state, catalog, runtime execution state, external/decoded data, logs, review reports and locks.

Therefore an admissible shadow runner must mechanically redirect both:

```text
INSTALL -> staged R10 successor install
C5      -> staged R10 successor state
```

before any execution.

## Large-tree safety boundary

The extraction exposed cataloger logic and two terminal `find` calls limited by `-maxdepth 1`. No broad filesystem scan was executed by this extraction.

Before any shadow execution, the cataloger/local-archive input contract must be reconciled so the shadow run cannot recursively traverse the approximately 30 GB SIGMA tree unintentionally.

## Synchronization consequence

```text
R10_SUCCESSOR_STAGE=PASS
RUNNER_CONTRACT_EXTRACTION=PASS
SHADOW_RUNNER_MECHANICAL_DERIVATION=ELIGIBLE
SHADOW_RUNNER_EXECUTION=NOT_YET_AUTHORIZED
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

The next step is materialization/audit only: derive a shadow runner from this exact runner, stage exact bridge/review dependencies, redirect `INSTALL` and `C5`, replace only the expected main-source identity with exact R10, perform syntax/hash/path audits, and do not execute it yet.

`CLAIM <= EVIDENCE`
