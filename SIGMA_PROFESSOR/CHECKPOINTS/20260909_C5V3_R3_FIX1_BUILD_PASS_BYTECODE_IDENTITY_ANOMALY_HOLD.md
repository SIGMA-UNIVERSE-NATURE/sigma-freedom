# C5V3 R3 FIX1 — BUILD PASS / BYTECODE IDENTITY ANOMALY HOLD

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **SOURCE CONSTRUCTION PASS / COMPILE RC0 / BYTECODE IDENTITY ANOMALY HOLD / PRODUCTION UNCHANGED**

## Operator-returned source construction evidence

```text
R3_FIX1_SOURCE_SHA256=152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8
R3_FIX1_DEF_COUNT=176
HISTORICAL_HEADER_COUNT=1
HISTORICAL_ENTRY_COUNT=1
LEGACY_LEFT_RIGHT_COGNITION=ABSENT
DIRECT_PERSISTENT_STATE_PATH=ABSENT
WRITE_TEXT_SURFACE=ONLY_STAGE_READBACK_AND_FINAL_COMMIT_INTENT
R3_FIX1_CONSTRUCTION=PASS
COGNITION_DONOR_SHA256=4d0ea071c5844938ccc264afbd76494e21279655988ad95f6bdd2842d989cb64
T1_T2_T3_TOOL_MODULE_SHA256=f48552534f2e5690b2b79a7a913cd2b5d376c13ba401b251eff63190820a8e07
```

Exact cognition parent extracted from transport container:

```text
M5_PARENT_SHA256=bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1
M5_PARENT_IDENTITY=PASS
DONOR_CONTAINER_ACCEPTED_AS_TRANSPORT_ONLY=YES
```

## Compile result

Locked compiler:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMAC_RC=0
```

Produced R3 FIX1 bytecode:

```text
R3_FIX1_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

However the earlier R2 rewrite already compiled to the exact same bytecode SHA256:

```text
R2_SOURCE_SHA256=d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0
R2_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

The R2 and R3 FIX1 sources are materially different in architecture, DEF count and active main/state behavior. Therefore source-change plus RC0 is insufficient evidence that the expected semantics reached bytecode.

## Authoritative interpretation

```text
R3_FIX1_SOURCE_CONSTRUCTION=PASS
R3_FIX1_SIGMAC_RC0=YES
R3_FIX1_BYTECODE_FREEZE_AS_FILE=YES
R3_FIX1_BYTECODE_SEMANTIC_IDENTITY=NOT_ADMITTED
R3_FIX1_RUNTIME_ADMISSION=NO
COMPILER_OUTPUT_IDENTITY_ANOMALY=HOLD
```

Do not advance to VM/runtime admission until this anomaly is explained.

## Exact next diagnostic

Use:

```text
C5_M5/RUN_C5V3_SIGMAC_OUTPUT_IDENTITY_ANOMALY_DIAGNOSTIC_R1.sh
SCRIPT_COMMIT=91f065a20fb113b84378dc5d132d98e18b0bf69d
```

The diagnostic performs only exact-path, isolated compiler checks:

```text
fresh recompile R2
fresh recompile R3 FIX1
byte-for-byte output comparison
observable main-literal counterfactual compile
negative parser control with final main brace removed
```

No VM/core execution, state access, directory scan, production binding or production mutation.

## Production locks

```text
LIVE_CORE_UNCHANGED=YES
LIVE_RUNNER_UNCHANGED=YES
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
