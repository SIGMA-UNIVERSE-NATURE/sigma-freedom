# C5 V2 preflight — partial-discovery failure preserved / FIX1 preflight source ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `PREFLIGHT_FAIL_PRESERVED / PREFLIGHT_ONLY_FIX1_SOURCE_READY / RERUN_REQUIRED`

## Observed Oppo machine evidence

```text
C5_V2_INCREMENTAL_PATCH_INSTALL=PASS
NATIVE_COGNITION_SOURCE_CHANGED=NO
REAL_OPPO_LEARNING_STARTED=NO
NEXT=RUN_C5_V2_PREFLIGHT_ONLY
SIGMA_PHASE=C5_AUTONOMOUS_SELF_LEARNING_PREFLIGHT_V2_INCREMENTAL_CATALOG_REGRESSION
REAL_OPPO_ARCHIVE_MUTATED=NO
LIVE_NETWORK_USED=NO
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
C5_NATIVE_SOURCE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
C5_MECHANICAL_BRIDGE_SHA256=98bb028cb668612393e1d687064fdf999dc73ec059b410737468bcc2ec3927dc
C5_SIGMAC_RC=0
C5_BYTECODE_SHA256=c60ff8e1207f4383f594aa1532bb1799252be460aaa1e1c6bc020a284d566da3
CATALOG_SCAN_ID=1
CATALOG_SCAN_COMPLETE=NO
CATALOG_REVISION=0
CATALOG_ENTRY_COUNT=0
CATALOG_PENDING_DIR_COUNT=1
CATALOG_DONE_DIR_COUNT=0
ASSERT_FAIL=CATALOG_V2_PARTIAL_DISCOVERY_BEFORE_COMPLETE EXPECTED=YES ACTUAL=NO
C5_PREFLIGHT_V2_PROCESS_RC=36
```

Therefore:

```text
C5_V2_PREFLIGHT=FAIL
C5_V2_ADMISSION=NO
REAL_OPPO_10GB_LEARNING=NOT_RUN
PRODUCTION_BINDING=NO
FAILURE_IS_EVIDENCE=YES
```

## Root cause

The V2 mechanical cataloger intentionally excludes any `.sigma_c5*` control subtree. The V2 preflight created its catalog fixture at:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_c5_preflight_v2/catalog_fixture_root
```

Because the fixture root itself had a `.sigma_c5_preflight_v2` ancestor, the cataloger correctly classified the whole fixture root as excluded control state and therefore discovered zero fixture files. This is a preflight fixture-location defect; the observed failure is not a native SIGMA cognition failure and is not evidence that real `$HOME/SIGMA` incremental discovery fails.

A reproduction outside the locked VM confirmed the mechanical distinction: a catalog root under a `.sigma_c5*` ancestor produces zero entries, while the same bridge on a root outside that ancestor discovers files normally.

## FIX1

Change only the V2 preflight fixture location. The catalog fixture is created under Termux temporary storage outside any `.sigma_c5*` ancestor. The native source, mechanical bridge, continuous runner and real shadow runner remain unchanged.

```text
NATIVE_COGNITION_SOURCE_CHANGED=NO
MECHANICAL_BRIDGE_CHANGED=NO
CONTINUOUS_RUNNER_CHANGED=NO
REAL_SHADOW_RUNNER_CHANGED=NO
OLD_V2_PREFLIGHT_SHA256=f629139361ef11b4b458b409a7a3e385b8aed24d0675b0b3782bfdb46ed4efb1
FIX1_PREFLIGHT_SHA256=381d9d34fb8d95c0a309f8b88821b9cb38602070ead8d9d10cba71d392113208
FIX1_PATCH_BUNDLE_SHA256=b4731e57c01eb6825c9986755d2f24ef0588efbeaaffbb318dbf4dc7e12e133d
```

## Claim boundary

```text
C5_V2_FIX1_PREFLIGHT_SOURCE_READY=YES
C5_V2_FIX1_LOCKED_VM_RERUN=NOT_RUN
C5_V2_FIX1_ADMISSION=NOT_RUN
REAL_OPPO_10GB_LEARNING=NOT_RUN
LIVE_INTERNET_REAL_RUNTIME=NOT_RUN
PRODUCTION_ADMISSION=NO
```
