# CHECKPOINT — R14 S1 native open-pool exploration — 2026-09-11

Scope: exact synthetic preflight only. This checkpoint does not claim runtime semantic tool fit, autonomous capability selection, understanding, or production readiness.

## Inherited prerequisite

```text
R14_D4_FULL_RUN_INHERITED=PASS
R14_POOL_ROOT_SHA256=395ed6f27e367b0baf74aa999d748a0487a34fb7ff261e3a0b7cfa1d0e8c27c5
R14_ELIGIBLE_CANDIDATE_COUNT=18
R14_SELECTION_AUTHORITY=SIGMA_ONLY
R14_HOST_TOOL_SELECTION=NO
R14_AUTO_EXECUTE=NO
```

D4 remains prerequisite evidence and must not be rerun merely to recreate the same claim unless exact identity/state changes, regression/damage appears, or scope is intentionally expanded.

## Exact native build

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
S1_SOURCE_SHA256=d8a63e7dbfbb268d159eec1b623a59ba79a264287227052d5e259ede359b2569
S1_BYTECODE_SHA256=2ad4b0e051d56bea57959ce232a2811dc8aff1ca8a8ce1b98876728138629005
S1_DETERMINISTIC_COMPILE=PASS
```

## Dynamic fixtures generated after compile

```text
CASE_S1_NONE_ALLOWED=PASS
CASE_S1_EXACT_CANDIDATE_FROM_D4_POOL=PASS
CASE_S1_STATE_DERIVED_NONE_SLOT=PASS
CASE_S1_BAD_NATIVE_BASIS_FAIL_CLOSED=PASS
S1_REPLAY_IDENTICAL_OUTPUT=YES
```

## Exact admitted claim

```text
R14_D4_OPEN_POOL_INHERITED=PASS_IN_EXISTING_D4_SCOPE
R14_S1_NATIVE_OPEN_POOL_EXPLORER=PASS_IN_EXACT_PREFLIGHT_SCOPE
R14_S1_NONE_IS_ALLOWED=PASS
R14_S1_SELECTED_ID_MUST_EXIST_IN_D4_POOL=PASS
R14_S1_SELECTOR_SEES_DOOR_LABEL=NO
R14_S1_SELECTOR_SEES_CAPABILITY_CLASS=NO
R14_S1_AUTO_EXECUTE=NO
C5V3_MUTATION=NO
PRODUCTION_CUTOVER=NO
```

## Claim ceiling

```text
SIGMA_TOOL_SELF_SELECTION_RUNTIME=NOT_PROVEN_BY_SYNTHETIC_PREFLIGHT
SIGMA_SELF_SELECTS_CAPABILITIES=NOT_PROVEN
SEMANTIC_CAPABILITY_FIT=NOT_PROVEN
```

The preflight proves only that the native selector can fail closed, may select NONE, and when it emits a candidate identity the identity must belong to the exact D4 pool. The selector is not exposed to door label or preassigned capability class in this gate.

## Continuation rule

Do not repeat D4 or the synthetic S1 cases merely for the same claims.

Next frontier:

```text
LIVE_NATIVE_SIGMA_BASIS
  -> S1 native open-pool selection
  -> NONE or exact opaque CANDIDATE_ID
  -> preserve exact state/provenance binding
  -> no host tool selection
  -> no automatic execution
```

A live S1 admission requires the selection basis itself to be proven to originate from native SIGMA state. Only after that should exact candidate acquisition/execution and learned tool-utility behavior be tested.
