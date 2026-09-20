# SIGMA VKM R6 — Canonical Integration Map Receipt

## Result

R6_CANONICAL_INTEGRATION_MAP=PASS
R6_MUTATION=NO
R7_MUTATION=NO
PRODUCTION_VM_MUTATION=NO
SIGMA_IDENTITY=ONE_SIGMA
CURRENT_GENERATION=5
NEXT=R6_REPLACE_LEGACY_COMMIT_PATH
TERMUX_SHELL_CONTINUES=YES

## Current ownership prerequisite

R5_STATUS=TAKEN_OVER
DURABLE_TRANSACTION_OWNER=VKM
TRANSACTION_JOURNAL_OWNER=VKM
JOURNAL_RECOVERY_OWNER=VKM
RULE=ONE_CAPABILITY_ONE_WRITER
RULE=NO_DUAL_CANONICAL_STATE

## Legacy R7 accept / commit path mapped

Canonical integration inspection identified the legacy R7 path in run_SIGMA_C5V4_LONG_DOCUMENT_CURRICULUM_R7.sh, including:

- MODEL="$MODEL_DIR/model.ail"
- r7_vm entry points
- AIL propose_cross calls
- AIL commit calls for accepted chunk candidates
- reject_adapt path
- post-long-document replay commit

Observed locations included lines 70, 107, 434, 474, 536, 615, 654, 702, 708, 727, 751-756, 792 and 910 in the inspected script output.

## R8 canonical promotion path mapped

Inspection of SIGMA_C5V4_CONTINUOUS_SHADOW_R8_WORKER.sh identified:

- CANON_MODEL="$CANONICAL/model/model.ail"
- STAGE_MODEL="$STAGE_SHADOW/model/model.ail"
- atomic_copy helper
- stage-to-canonical atomic_copy promotion
- AIL propose_replay
- AIL commit on STAGE_MODEL
- subsequent stage-to-canonical promotion

Observed locations included lines 14, 47, 70, 96, 379, 451, 487 and 529 in the inspected output.

## Current VKM durable transaction interface

sigma_durable_transaction_r5.py accepts seven state/input paths:
canonical, replay, generation, lineage, lexical, candidate, journal.

The mapped implementation includes:
- relation parsing/evaluation;
- parent canonical SHA capture;
- candidate SHA capture;
- PREPARED journal;
- parent→replay write;
- candidate→canonical write;
- generation/lineage durable transition;
- committed journal and post-commit verification.

## One-Sigma state identities

- canonical.memory: ffb8d846540880f6f2669b39028a1f1aba187c984f927042c6c486a3009f4fb3
- replay.memory: 614d420b945eeac49b66312ca28871a2f3ffd644adf010eed4815ff00d24811e
- generation.txt: f0b5c2c2211c8d67ed15e75e656c7862d086e9245420892a7de62cd9ec582a06
- lineage.memory: 9991207dd59e1f182baef33c7da5e99489a881e7e524cb3de08227e4d08a04c1
- sigma_durable_transaction_r5.py: 934425d1b743aa8d216c01bef6d591a424bbb96028b67833239e72e223cb4935
- sigma_journal_recovery_r5.py: 2279cbd785c9bb65abc84adddb174bfdd1af766bbf48aba4d967b4c85509152a
- sigma-vkm: 0791205449dc0d8ff982b9eae39d2f7b516e4eb46bbf69ab36808c9ae41cbe1c
- sigma-vm.v09_candidate: 029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

## Boundary

This checkpoint is a mapping/inspection proof only. No R6, R7, canonical model, or production VM mutation was performed. It identifies the legacy commit/promotion surfaces that must be replaced or bridged by the VKM durable transaction path before canonical-integration ownership can be taken over.
