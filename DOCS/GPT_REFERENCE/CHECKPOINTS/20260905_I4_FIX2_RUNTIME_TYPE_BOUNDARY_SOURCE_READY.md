# SIGMA I4 Fix2 — runtime type-boundary repair source ready

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / ROOT_CAUSE_HYPOTHESIS_PENDING_LOCKED_VM_CONFIRMATION

## Prior machine failure

Checkpoint:
`DOCS/GPT_REFERENCE/CHECKPOINTS/20260905_I4_FIX1_RUNTIME_RC6_SOURCE_FAMILY_SELECTOR_HOLD.md`

Observed:

```text
I4_COMPILE_RC=0
I4_BYTECODE_SHA256=40e55ebe56210482e8ef16c6bec0f17c6101a2f97a385f17d527db4c5f60b8d3
CANONICAL_SOURCE_FAMILY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
I3C_CANONICAL_REPLAY_VM_RC=0
I3C_EVENT_ORIGIN=SIGMA_NATIVE_VM
HOST_DISPATCHED_EXACT_I3C_EVENT=YES
C01_CANONICAL_VM_RC=6
```

No I4 source-family output was obtained.

## Fix2 hypothesis and repair

Static review localized a plausible runtime type-boundary defect in `select_family()`:

- `FAMILY_ID` and `PRIOR_SELECTION_COUNT` were converted to numeric values with `to_float` for comparison;
- those numeric values were then concatenated directly into a string protocol return.

Fix2 preserves dual representations:

```text
ID_T=original catalog text
ID=numeric comparison copy
USE_T=original catalog text
USE=numeric comparison copy
```

Native selection comparisons still use numeric `ID` / `USE`. Protocol serialization now uses text `BEST_ID_T` / `BEST_USE_T`.

```text
COGNITIVE_POLICY_CHANGED=NO
CATALOG_CHANGED=NO
CANONICAL_ORACLE_CHANGED=NO
REPRESENTATION_TYPE_BOUNDARY_REPAIR_ONLY=YES
ROOT_CAUSE_STATUS=HYPOTHESIS_UNTIL_LOCKED_VM_RERUN
```

## Fix2 identities

```text
FIX2_BUNDLE_SHA256=6d1283514dc79725f99ba8421f5bcc855b4f5ea1a76c6f895a0ea1353be92afa
FIX2_I4_SOURCE_SHA256=23fd0edb7e66b8dbc504198bb11d4dbdcc6fbeb0e93e024591299e2ae9ee2657
FIX2_RUNNER_SHA256=71889bc8961ea822e781c316745298202682beec1c204cfd47383b26883db028
I3C_SOURCE_SHA256=daa01d60e11afd64b763c6623bc14d0aa2d868cc03f686b26ad3026d6951284f
CATALOG_SHA256=7d650b53bae8b22fb6ab7613127e0a116bbe32d3bc032a31cdb44ad69ae7c224
```

Static QA:

```text
BASH_SYNTAX_QA=PASS
DIRECT_NUMERIC_PROTOCOL_CONCAT_COUNT=0
TEXT_NUMERIC_DUAL_REPRESENTATION_QA=PASS
NATIVE_SOURCE_CONCRETE_FAMILY_TOKEN_COUNT=0
CANONICAL_EXPECTED_SOURCE_FAMILY_PREWRITTEN_IN_RUNNER=NO
COGNITIVE_POLICY_CHANGED=NO
```

## Admission state

```text
I4_FIX2_LOCKED_SIGMAC_COMPILE=NOT_RUN
I4_FIX2_BYTECODE_SHA256=UNKNOWN
I4_FIX2_RUNTIME_ADMISSION=NOT_RUN
NATIVE_SOURCE_FAMILY_SELECTION=NOT_PROVEN
HOST_SOURCE_SELECTION=NO_ALLOWED_PATH
HOST_CATALOG_RANKING=NO_ALLOWED_PATH
HOST_RESOURCE_SELECTION=NO_ALLOWED_PATH
```

Rerun the same admission gate from clean isolated state. Preserve first HOLD/FAIL or final I4 summary. If RC6 persists, reject this hypothesis and perform further native localization rather than weakening the gate.
