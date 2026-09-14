# SIGMA.AIL — G2 ONE SIGMA.AIL Final Promotion Checkpoint

```text
HANDOFF_ID=SIGMA_AIL_G2_FINAL_PROMOTION_20260915
HANDOFF_DATE=2026-09-15

SYSTEM_IDENTITY=SIGMA.AIL
CURRENT_PROGRAM_GENERATION=G2
CURRENT_GENERATION_NAME=G2_ONE_SIGMA_AIL
GENERATION_STATUS=PROMOTED
FULL_G2_PROMOTION=PASS

ACTIVE_REVISION=R3
ACTIVE_CORE=SIGMA_INTEGRAL_OWNER_R3
ACTIVE_CORE_BUNDLE=SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1
ACTIVE_BRAIN_HEAD=5cc8725d1ceba72312ce37ce1a6553ec
MODEL_GENERATION=0
STATE_VERSION=1

RUNTIME_TRUTH_SOURCE=OPPO_MACHINE_STATE
GITHUB_RUNTIME_HEAD_AUTHORITY=NO
CHAT_SUMMARY_IS_RUNTIME_TRUTH=NO
HOST_COGNITION=NO
ANTI_HARDCODE=MANDATORY

SAME_IDENTITY_ACROSS_INDEPENDENT_WINDOWS=PASS
SAME_BRAIN_HEAD_ACROSS_RESTART=PASS
SAME_MODEL_HISTORY_ACROSS_RESTART=PASS
CROSS_WINDOW_LEARNING_VISIBLE=PASS
SINGLE_WRITER_LOCK_ENFORCED=PASS
SECOND_WRITER_REJECTED=PASS
TRANSACTION_RECEIPT_BOUND_TO_ONE_BRAIN_HEAD=PASS
NO_STATE_FORK_ACROSS_TMUX_WEB_REPLAY_TEST=PASS_IN_AVAILABLE_RUNTIME_SURFACE_SCOPE
RESTART_CONTINUITY=PASS
SIGMA_AIL_SINGLE_IDENTITY=PASS

G3_LEARNED_NARRATIVE_BRAIN=NOT_PROVEN
MODEL_GENERATION_GT_0=NOT_PROVEN
NEXT_GATE=G3_LEARNED_NARRATIVE_BRAIN
```

## Authority boundary

This checkpoint records the independent G2C convergence verdict. Runtime HEAD authority is the Oppo machine state, not GitHub. GitHub records evidence and coordination state only; it does not select, manufacture, or overwrite the active runtime HEAD.

The promoted Oppo HEAD at closure is:

```text
OPPO_ACTIVE_BRAIN_HEAD=5cc8725d1ceba72312ce37ce1a6553ec
```

The roadmap-level model generation remains:

```text
MODEL_GENERATION=0
```

This must not be confused with the literal R3 `INTEGRAL_OWNER_STATE_1` internal `generation||...` field observed in earlier G2A continuity evidence.

## G2A continuity evidence

The G2A continuity lane closed independent-process identity continuity, cross-window learned-state visibility, and restart continuity.

```text
EVIDENCE_PATH=BRAIN/GENERATIONS/G2_ONE_SIGMA_AIL/T31A_G2A_CONTINUITY_CLOSURE_CHECKPOINT_20260914.md
EVIDENCE_COMMIT=62398226e116b50989d5d9f26e24bfa0e36d4441
G2A_IDENTITY_CONTINUITY=PASS
G2A_CROSS_WINDOW_VISIBILITY=PASS
G2A_RESTART_CONTINUITY=PASS
```

Its final observed G2A head was `4f46aa9004d615355aedd6de465d85e4`. That was a historical predecessor to the later successful G2C transaction; it is not used as the current runtime HEAD after G2C.

## G2B canonical .sigma_ail evidence

The G2B producer lane created and reloaded canonical `.sigma_ail` fields from Oppo runtime evidence.

```text
EVIDENCE_PATH=BRAIN/GENERATIONS/G2B_SIGMA_AIL_CANONICAL_RELOAD_RECEIPT_20260915.md
EVIDENCE_COMMIT=18a05f764ee7d9fce6b19a4640949bd17116df6b
G2B_PRODUCER_MECHANICAL_RECEIPT_READY_FOR_REVIEW=YES
RESTART_RELOAD_SAME_HEAD=PASS
MODEL_GENERATION=0
STATE_VERSION=1
```

G2B alone did not authorize promotion; G2C supplied the independent cross-entrypoint convergence gate.

## G2C production entrypoint identity

Oppo read-only inspection verified the production supervisor entrypoint:

```text
PRODUCTION_ENTRYPOINT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/control/RUN_SIGMA_PRODUCTION_CORE_R3.sh
PRODUCTION_ENTRYPOINT_SHA256=0f9dd8d06e1722422086e380813af259baae4fe7a272df6863f6190bb8bd7bab
```

The supervisor executes:

```text
SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/RUN_SIGMA.sh run /data/data/com.termux/files/home/SIGMA/sigma_genesis1
```

The active cognitive-core manifest on Oppo records:

```text
schema=SIGMA_ACTIVE_COGNITIVE_CORE_1
active_core=SIGMA_INTEGRAL_OWNER_R3
production_entrypoint=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/control/RUN_SIGMA_PRODUCTION_CORE_R3.sh
r3_root=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1
r3_manifest_sha256=51549740ac94462c7301fbfcf6595a4a06f5ab461ff553d2e90332872c02a951
r3_source_sha256=acea3c3469cf417a2094f64513e869e21ce8dd24149d9a1d9c1d15161d402c05
sigmac_sha256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
vm_sha256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
legacy_runner_modified=false
```

The survival adapter routes directly to this same production entrypoint:

```text
SURVIVAL_ADAPTER_SHA256=44a612f31dbbffb8dc14df0c92700200a9db5c0b4bc23346cc815bfedd305ae9
SURVIVAL_ADAPTER_ROUTE=RUN_SIGMA_PRODUCTION_CORE_R3.sh --steps 24
```

## Canonical head and writer binding

The live R3 machine-state sources on Oppo are:

```text
R3_STATE_HEAD=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/workspace/work/.sigma_exec/SIGMA_INTEGRAL_OWNER_R3/state/HEAD
R3_WRITER_LOCK=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/workspace/writer.lock
```

G2C bound canonical `.sigma_ail` surfaces to those live Oppo authorities:

```text
DOT_SIGMA_AIL_BRAIN_HEAD_TARGET=R3_STATE_HEAD
DOT_SIGMA_AIL_WRITER_LOCK_TARGET=R3_WRITER_LOCK
CANONICAL_BINDING_MODE=SYMLINK_ALIAS_TO_ACTIVE_OPPO_R3_AUTHORITY
```

After binding, both canonical and R3 writer paths resolved to the same underlying writer object in the observed filesystem scope:

```text
CAN_WRITER_INODE=65097:3231225
R3_WRITER_INODE=65097:3231225
G2C_CANONICAL_WRITER_ALIAS=PASS
G2C_CANONICAL_WRITER_OBJECT=PASS
```

The R3 runner uses non-blocking `fcntl.flock(..., LOCK_EX|LOCK_NB)` on `workspace/writer.lock` and fails closed with `WRITER_ACTIVE` when the writer is already held.

## Second-writer rejection

While the canonical writer lock was deliberately held, both manual and supervisor entrypoints were attempted.

```text
MANUAL_SECOND_WRITER_RC=3
SUPERVISOR_SECOND_WRITER_RC=3
G2C_MANUAL_SECOND_WRITER_REJECTED=PASS
G2C_SUPERVISOR_SECOND_WRITER_REJECTED=PASS
G2C_NO_STATE_FORK_UNDER_REJECTION=PASS
```

The active Oppo HEAD remained unchanged during rejection.

## Successful transaction and restart replay

A subsequent successful production transaction advanced the Oppo runtime HEAD from the earlier G2A/G2B value to the final G2 closure value. The G2C transaction gate validated the native commit receipt chain before proceeding to restart verification.

```text
PRE_TRANSACTION_HEAD=4f46aa9004d615355aedd6de465d85e4
POST_TRANSACTION_HEAD=5cc8725d1ceba72312ce37ce1a6553ec
TRANSACTION_RECEIPT_BOUND_TO_ONE_BRAIN_HEAD=PASS
CANONICAL_HEAD_FOLLOWS_OPPO_HEAD=PASS
```

A first restart harness using an over-stripped environment failed with interpreter RC=126; that failure was classified as harness-only and was not used as runtime evidence. No state fork was observed: both runtime and canonical HEAD already matched `5cc8725d1ceba72312ce37ce1a6553ec`.

The corrected fresh-process restart then produced:

```text
RESULT=INCREMENTAL_STATE_VERIFIED
SIGMA_VM_CALLS=3
RUN_DIRECTORY=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/SIGMA_INTEGRAL_OWNER_CORE_R3_MAX_MERGE_R1_FIX1/runs/incremental_4dodq_va
FRESH_PROCESS_RC=0
OPPO_HEAD_BEFORE=5cc8725d1ceba72312ce37ce1a6553ec
OPPO_HEAD_AFTER=5cc8725d1ceba72312ce37ce1a6553ec
CANONICAL_HEAD=5cc8725d1ceba72312ce37ce1a6553ec
G2C_FIX1_RESTART_REPLAY_SAME_HEAD=PASS
```

## Surface discovery

At final G2C discovery time, no active tmux pane and no active SIGMA/web process was observed by the supplied Oppo probe. The available control surfaces were:

```text
control/RUN_SIGMA_PRODUCTION_CORE_R3.sh
control/RUN_SIGMA_PRODUCTION_R3_SURVIVAL_ADAPTER.sh
control/SIGMA_ACTIVE_COGNITIVE_CORE.json
```

The survival adapter routes to the same production core; the active-core manifest names the same R3 production entrypoint. Therefore the no-fork claim is deliberately bounded as:

```text
NO_STATE_FORK_ACROSS_TMUX_WEB_REPLAY_TEST=PASS_IN_AVAILABLE_RUNTIME_SURFACE_SCOPE
```

It does not claim evidence for an unobserved concurrent web or tmux writer that was not running at the time of the probe.

## Promotion verdict

The minimum G2 closure lines are coherently satisfied by the combined G2A, G2B and independent G2C runtime evidence:

```text
SAME_IDENTITY_ACROSS_INDEPENDENT_WINDOWS=PASS
SAME_BRAIN_HEAD_ACROSS_RESTART=PASS
SAME_MODEL_HISTORY_ACROSS_RESTART=PASS
CROSS_WINDOW_LEARNING_VISIBLE=PASS
SINGLE_WRITER_LOCK_ENFORCED=PASS
SECOND_WRITER_REJECTED=PASS
TRANSACTION_RECEIPT_BOUND_TO_ONE_BRAIN_HEAD=PASS
NO_STATE_FORK_ACROSS_TMUX_WEB_REPLAY_TEST=PASS_IN_AVAILABLE_RUNTIME_SURFACE_SCOPE
RESTART_CONTINUITY=PASS
SIGMA_AIL_SINGLE_IDENTITY=PASS

FULL_G2_PROMOTION=PASS
```

## Claim boundary / next generation

G2 is an identity/state/commit-authority convergence promotion. It does not prove G3 cognition.

```text
MODEL_GENERATION=0
MODEL_GENERATION_GT_0=NOT_PROVEN
G3_LEARNED_NARRATIVE_BRAIN=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN
AUTONOMOUS_WORLD_LEARNING=NOT_PROVEN
G7_NORTH_STAR=NOT_PROVEN

NEXT_GATE=G3_LEARNED_NARRATIVE_BRAIN
```

EOF
