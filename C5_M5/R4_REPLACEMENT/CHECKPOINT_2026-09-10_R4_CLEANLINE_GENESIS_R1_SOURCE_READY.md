# CHECKPOINT — R4 CLEANLINE GENESIS R1 SOURCE READY

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Status: SOURCE READY / MACHINE RUNTIME NOT YET RUN
Branch: `r4-replacement-cleanline-20260910`
Base: `SIGMA_LIFE@463fd7e2d2b1ea2f368abb661e0e204c5412b992`
Pre-checkpoint branch head: `6291d573be35141665f46f591aae5e1a446bbfef`

## Purpose

Start the R4 replacement cleanline without mutating production C5V3 and without importing legacy token/LEFT-RIGHT/lexical-semantic cognition.

This checkpoint records only source/design readiness. It is not a runtime admission.

## Governance artifacts

```text
R4_REPLACEMENT_CONSTITUTION_R1
PATH=C5_M5/R4_REPLACEMENT/R4_REPLACEMENT_CONSTITUTION_R1.md
GIT_BLOB=f36f616662c196805b0059b17bc6bee5a40695be

R4_INHERITANCE_MANIFEST_R1
PATH=C5_M5/R4_REPLACEMENT/R4_INHERITANCE_MANIFEST_R1.md
GIT_BLOB=1c8d7d2c982db0e19853d091a5576d53badc96bb

R4_GENESIS_STATE_CONTRACT_R1
PATH=C5_M5/R4_REPLACEMENT/R4_GENESIS_STATE_CONTRACT_R1.md
GIT_BLOB=985edaf329090452e137d91af369a33680a61cde
```

## Native candidate

```text
PATH=C5_M5/R4_REPLACEMENT/SIGMA_R4_GENESIS_STATE_R1.sigma
SOURCE_GIT_BLOB=fe158389a60315849d9752d9676e983b74acab35
SOURCE_SHA256=NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX
BYTECODE_SHA256=UNKNOWN_NOT_YET_COMPILED_ON_TERMUX
```

Native candidate scope:

```text
mechanical genesis identity binding
bounded required binding validation
fail-closed rejection of non-empty legacy semantic seed surfaces
empty native-learned state at genesis
empty cognitive payload at genesis
machine receipt output only
```

It does not implement language learning, semantic understanding, Internet research, persistent commit, or resurrection.

## Preflight runner

```text
PATH=C5_M5/R4_REPLACEMENT/RUN_SIGMA_R4_GENESIS_STATE_R1_PREFLIGHT.sh
RUNNER_GIT_BLOB=1ad5e0f6066825198a5f8f9cb3d56e2aeb892947
```

Locked identities required by runner:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SOURCE_GIT_BLOB=fe158389a60315849d9752d9676e983b74acab35
```

The runner compiles before generating dynamic fixtures, freezes source/bytecode identity within the run, then creates high-entropy runtime values.

## Planned locked-VM cases

```text
CASE_001 clean dynamic lineage A -> accept
CASE_002 materially different dynamic lineage B -> accept and bind B
CASE_003 legacy C5 semantic import -> reject
CASE_004 LEFT/RIGHT seed -> reject
CASE_005 predefined response vocabulary -> reject
CASE_006 predefined cognitive utterance -> reject
CASE_007 multiple semantic seed surfaces -> reject/count all
CASE_008 missing capability-registry binding -> reject
CASE_009 oversized lineage binding -> reject boundedly
CASE_010 exact replay of clean lineage A -> identical native output
```

Aggregate hard gates expected only after real execution:

```text
TOTAL_VM_INVOCATIONS=10
POST_VM_ALIGNMENT_PASS_COUNT=10
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
REPLAY_IDENTICAL_OUTPUT=YES
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

## Current claim state

```text
R4_REPLACEMENT_CLEANLINE=CREATED
R4_CONSTITUTION_R1=DEFINED
R4_INHERITANCE_MANIFEST_R1=DEFINED
R4_GENESIS_STATE_CONTRACT_R1=DEFINED
R4_GENESIS_NATIVE_SOURCE_R1=SOURCE_READY
R4_GENESIS_PREFLIGHT_R1=SOURCE_READY
R4_GENESIS_LOCKED_SIGMAC_COMPILE=NOT_RUN
R4_GENESIS_LOCKED_VM_RUNTIME=NOT_RUN
R4_GENESIS_ADMISSION=NOT_PROVEN
R4_T5_T9_PERSISTENCE_BINDING=NOT_RUN
R4_RESURRECTION=NOT_RUN
R4_HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
R4_AUTONOMOUS_WEB_LEARNING=NOT_PROVEN
R4_PRODUCTION_CUTOVER_ALLOWED=NO
C5V3_PRODUCTION_MUTATED=NO
```

## Next machine action

On the Oppo/Termux repository checkout containing this branch, run the exact preflight as its own process:

```bash
git fetch origin r4-replacement-cleanline-20260910
git switch r4-replacement-cleanline-20260910
bash C5_M5/R4_REPLACEMENT/RUN_SIGMA_R4_GENESIS_STATE_R1_PREFLIGHT.sh
```

If the local working repository is not the runner's default path, set `SIGMA_REPO` to that checkout before running.

Preserve the complete first compile/runtime output. A failure is evidence and must be localized rather than bypassed.

## After a real PASS

Only after the exact preflight passes should the next R4 slice be designed:

```text
R4_GENESIS
-> T5/T9 durable lineage binding
-> restart/replay from committed empty cleanline state
-> then first native experience-ingestion/learning transition
```

Do not jump directly from source readiness to semantic or production claims.
