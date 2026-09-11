# CHECKPOINT — R14 S2 exact selected-candidate acquisition R1 — SOURCE READY — 2026-09-11

Purpose: continue directly from the exact LIVE S1 selected candidate without host reselection, while preserving the D4 `AVAILABLE_NOT_OWNED`, `AUTO_ACQUIRE=NO`, and candidate-identity boundaries.

## Exact LIVE S1 prerequisite

```text
RUN=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v4_candidate/R14_S1_LIVE_STATE_BOUND_EXPLORATION_R2/20260911_15293815042
SELECTED_CANDIDATE_ID=50438f11af49f9a05947dee7e20c058c2df7565ec83387194a5c4bb8d6c5bd9e
POOL_ROOT_SHA256=395ed6f27e367b0baf74aa999d748a0487a34fb7ff261e3a0b7cfa1d0e8c27c5
STATE_BASIS_BUNDLE_SHA256=b3e93f74f93c6e66a40d343aa32fd04b18bb292fe32e9816955f4fda40e9421f
```

## S2 design

1. Verify the exact LIVE S1 run and exact selected candidate/pool/state identities.
2. Resolve the exact selected candidate from the D4 state. `CANDIDATE_ID` remains identity; door label may be used only as lookup metadata after proving it is unique for that candidate in the exact D4 pool.
3. Resolve and verify exact source/binary/ABI/evidence paths and SHA256 identities. No broad filesystem scan is permitted.
4. Native SIGMA receives candidate and artifact identities, but not door label/capability class/operation names, and emits an explicit acquisition request.
5. S2 performs no tool execution.
6. Only after S2 PASS may S3 expose the exact selected ABI to native SIGMA for operation/argument formation, exact bounded execution, and raw result return.

## Static artifact identities

```text
BUNDLE_SHA256=95c3e0b4322e8b19b00b8c67aff621fc8756c839722137248716661e0fa97521
S2_NATIVE_SOURCE_SHA256=ec8f8b2d346cfab1a394635cfb30806bfbb209422724014a843d76a3dcda5859
S2_RESOLVER_SHA256=63474af64d38a510b76ae3ed61142f2ae7960bac82f8f411c89b3c8cd7fe79f4
S2_RUNNER_SHA256=0d7db954ec30e1c3c28cb2386f51e805b9926b56de71bc65ba7ac7cdfa892d0c
ZIP_INTEGRITY=PASS
MANIFEST_VERIFY=PASS
BASH_SYNTAX=PASS
```

## Claim ceiling before machine run

```text
R14_S2_EXACT_CANDIDATE_RESOLUTION=NOT_YET_RUN
R14_S2_NATIVE_EXPLICIT_ACQUISITION_REQUEST=NOT_YET_RUN
R14_S2_SELECTED_ABI_CAPTURE=NOT_YET_RUN
TOOL_EXECUTION=NO
SIGMA_SELF_SELECTS_CAPABILITIES=NOT_PROVEN
SEMANTIC_CAPABILITY_FIT=NOT_PROVEN
TOOL_UTILITY_LEARNING=NOT_PROVEN
C5V3_MUTATION=NO
PRODUCTION_CUTOVER=NO
```
