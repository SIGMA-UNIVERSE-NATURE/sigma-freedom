# V4-PK4 Completion Gate — Inference Lifecycle — SOURCE READY / NOT ADMITTED

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Purpose

Complete the governing V4-PK4 Controlled Inference contract after the machine-PASS formal `TRANSITIVE_SAME_RELATION_V1` subscope.

## Locked runtime

SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

## Artifact identity

SOURCE_PATH=SIGMA_V4_CONTROLLED_INFERENCE_LIFECYCLE_V4PK4C1.sigma
SOURCE_SHA256=40089efb86781b0a21207b5bbbae6ec3ebca38e484a010caf939f0d0545b1e2a
RUNNER_PATH=run_SIGMA_V4PK4_COMPLETION_NATIVE_ADMISSION_V1.sh
RUNNER_SHA256=44f8bc149c540a971967f9f75cc4c9152c2d2b4ef18a099a3245595f043bc491
BUNDLE_SHA256=0037f5570c4fc5f9e6355838d6e1dc75c073a3f1b32ca62161ebad6b3957e901

V4PK1_DEPENDENCY_SOURCE_SHA256=bef6fdb02c15299a07b2010fcce1664cc98e0888f97536c4d0d4298acca05bcb
V4PK2_DEPENDENCY_SOURCE_SHA256=1440f75e3f72c8ab32506500c30ac0b5966665ea331b8441186cec0cc8b8b549
V4PK4_FORMAL_DEPENDENCY_SOURCE_SHA256=36da881e1dcab88f543c9879fa69979410b62738014f4958085988faca32656e
V4PK3_ADMITTED_DEPENDENCY_CHECKPOINT_REQUIRED=YES

## Native lifecycle contract

Native lifecycle states:

- HYPOTHESIS
- SUPPORTED_INFERENCE
- REJECTED_INFERENCE
- UNRESOLVED

Declared native rule policy for the exact tested scope:

SUPPORT_BALANCE_THRESHOLD_BP=5000
MAX_SUPPORTED_UNCERTAINTY_BP=3000
HOST_THRESHOLD_DECISION=NO

Classification rule:

- any negative premise balance -> REJECTED_INFERENCE;
- any zero premise balance -> UNRESOLVED;
- both positive but threshold/uncertainty support gate not met -> HYPOTHESIS;
- both balances >= 5000 and max premise uncertainty <= 3000 -> SUPPORTED_INFERENCE.

## Required retention

The lifecycle record preserves:

- formal inference candidate ID;
- formal rule schema;
- relation;
- start/bridge/target;
- premise edge IDs;
- persistent balance class per premise;
- persistent uncertainty class per premise;
- bounded first SUPPORT provenance slot per premise;
- bounded first COUNTER provenance slot per premise.

Exact numeric balance and max uncertainty remain native runtime-derived outputs from persistent V4-PK2 evidence; numeric-to-text host/substitution is not used.

## Planned admission suite

DIRECTED_VM_INVOCATIONS=16
RANDOMIZED_VM_INVOCATIONS=32
REPLAY_VM_INVOCATIONS=2
TOTAL_VM_INVOCATIONS_EXPECTED=50

Required transition scope:

REJECTED_INFERENCE -> UNRESOLVED -> HYPOTHESIS -> SUPPORTED_INFERENCE

Required failure/refusal coverage:

- missing candidate;
- invalid input;
- malformed hypergraph;
- malformed evidence store;
- malformed formal inference store;
- malformed lifecycle store;
- exact lifecycle idempotency;
- byte-identical replay;
- source/bytecode immutability;
- no step-limit in bounded suite.

## Static audit

BASH_SYNTAX=PASS
DIRECTED_RUN_EXPECT_CALLS=16
TOTAL_PLANNED_VM_INVOCATIONS=50
DEPENDENCY_INCOMPLETE_FORCES_UNRESOLVED=YES
EXACT_FINGERPRINT_INCLUDES_BALANCE_AND_UNCERTAINTY_CLASSES=YES
NUMERIC_TO_TEXT_UNPROVEN_PATH_USED=NO

## Claim boundaries

TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
FORMAL_RULE_GENERAL_SEMANTIC_VALIDITY=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO

## Admission state

SOURCE_READY=YES
LOCKED_SIGMAC_COMPILE=NOT_RUN_ON_USER_TERMUX
LOCKED_VM_RUNTIME=NOT_RUN_ON_USER_TERMUX
ADMISSION=NOT_RUN
FULL_V4PK4_CONTROLLED_INFERENCE_ADMISSION=NOT_YET_PROVEN
V4PK5_COGNITIVE_VM_BRIDGE_UNLOCKED=NO

NEXT_TARGET=RUN V4-PK4 COMPLETION NATIVE ADMISSION V1 FULL 50-VM SUITE
