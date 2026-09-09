# C5V3 CORE REWRITE R2 — SAME HISTORICAL CORE IDENTITY POLICY

Date: 2026-09-09 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **CANONICAL IDENTITY POLICY / REWRITE STAYS INSIDE EXISTING C5 CORE LINEAGE**

## Exact identity retained

The rewritten successor must retain the exact historical core identity:

```text
HEADER=#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.C5.AUTONOMOUS.SELF.LEARNING.CORE][VERSION=C5FULLR1]
ENTRY=Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1
PRINT_ID=SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1
FILENAME=SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
```

The earlier draft identity:

```text
DOMAIN=SIGMA.C5V3.COGNITIVE.KERNEL
VERSION=C5V3KR1
ENTRY=Σ.C5V3_COGNITIVE_KERNEL_R1
```

is superseded as a production-lineage identity. Its source remains only a rewrite template/provenance artifact.

## Architectural meaning

C5V3 is not implemented as a second cognitive kernel beside C5. The new capability-native architecture is written directly into the existing C5 autonomous self-learning core lineage.

Therefore future machine-admitted T0-T11 capability packs are synchronized into this same core architecture and selected through its native capability registry / need-detection / bounded-dispatch contract.

## Materialization gate

Canonical gate:

```text
C5_M5/RUN_C5V3_CORE_REWRITE_R2_SAME_IDENTITY_MATERIALIZE.sh
```

It derives an isolated successor source at:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_c5v3_sync/C5V3_CORE_REWRITE_R2/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
```

It does not overwrite live `.sigma_c5` and does not execute the VM/core.

## Governance

```text
SAME_HEADER_IDENTITY=MANDATORY
SAME_CORE_ENTRY_IDENTITY=MANDATORY
PARALLEL_ALTERNATE_COGNITIVE_CORE=NO
CAPABILITY_NATIVE_ARCHITECTURE_IN_EXISTING_CORE=YES
LIVE_CORE_WRITE=NO_UNTIL_ADMISSION_AND_CUTOVER
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
