# SIGMA C5V3 — R9 HOLD / FIX1 Prepared

Updated: 2026-09-09

This checkpoint is **non-admitted** and exists only so a future synchronization/test window does not misread the R9 state if the current chat becomes unavailable.

## R9 machine result — HOLD

Original R9 machine output:

- `DISPATCH_CONTRACT_EXTRACTION=PASS`
- production equality-condition variables: `CURRENT_REQUEST_BYTES,EVENT`
- M5 equality-condition variable: `EVENT`
- `BRANCH_UNRESOLVED_SYMBOL_UNION_COUNT=0`
- `M5_ONLY_DEF_FULL_REACHABILITY=PASS`
- `R10_EXPLICIT_DISPATCH_DESIGN_ELIGIBLE=NO`
- `R10_AUTOMATIC_ADDITIVE_BUILD_ELIGIBLE=NO`
- `R9_DISPATCH_CONTRACT=FAIL`
- `RESULT=HOLD`

This HOLD does **not** invalidate R5/R6/R7/R8.

## Methodology defect identified

The original R9 parser incorrectly required exactly one equality-condition selector variable in each universe and incorrectly treated repeated production event literals across guarded branches as an ambiguity.

Production source actually contains:

- a selector identifier also present in M5 source (`EVENT` in the observed output), and
- an additional production-only request-byte guard identifier (`CURRENT_REQUEST_BYTES`).

The correction must be source-derived and must not hardcode either identifier name.

## FIX1 prepared

Bundle:

`SIGMA_C5V3_OFFLINE_M5_DISPATCH_CONTRACT_R9_FIX1_BUNDLE_20260909.zip`

Bundle SHA256:

`b3ea9221ada0a9739986464ee876000b88e823f4346f6ef39cbab867fc7ccbbc`

FIX1 logic:

- derive the shared primary selector as the set intersection of equality-condition variable identifiers found independently in production and M5 source;
- classify other production-only equality variables as guarded-routing selectors rather than forcing them to disappear;
- allow repeated production event literals across multiple guarded branches;
- compute primary-event literal collisions only on the source-derived shared selector;
- retain the 63/63 M5-only DEF reachability gate;
- require zero unresolved M5 branch symbols;
- map production/M5 universe-prelude assignment differences so the next stage cannot copy the M5 prelude wholesale.

FIX1 static QA passed for:

- shell syntax;
- parser syntax;
- multi-guard selector classification;
- duplicate guarded event handling;
- full 63-function reachability synthetic case;
- no dispatch graft/build.

Static QA is not machine admission. FIX1 remains pending execution on OPPO.

## Current canonical state

- R5: PASS
- R6: PASS
- R7: PASS in exact tested offline ABI scope
- R8: PASS structural dispatch map
- original R9: HOLD / non-admitted
- R9 FIX1: prepared, machine result pending

Hard boundary remains:

- `M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO`
- `C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO`
- `ONLINE_SYNC_FROM_TEST_WINDOW=NO`
- `PRODUCTION_MUTATION_FROM_TEST_WINDOW=NO`
- `PRODUCTION_BINDING_FROM_TEST_WINDOW=NO`
