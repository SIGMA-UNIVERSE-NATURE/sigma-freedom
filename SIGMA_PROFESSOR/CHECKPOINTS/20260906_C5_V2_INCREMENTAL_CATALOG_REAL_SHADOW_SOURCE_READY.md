# C5 V2 — Persistent incremental catalog + bounded real-Oppo shadow — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `SOURCE_READY / RUNTIME_NOT_RUN / PRODUCTION_BINDING_NO`

## Dependency

C5 V1 FIX1 isolated preflight passed and is recorded in:

`SIGMA_PROFESSOR/CHECKPOINTS/20260906_C5_V1_PREFLIGHT_FIX1_PASS.md`

The native C5 cognition source is unchanged:

```text
NATIVE_SOURCE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
NATIVE_COGNITION_SOURCE_CHANGED=NO
```

## Why V2 is required before real ~10 GB execution

Static review of the V1 continuous runner showed that its real-device catalog path performs a complete synchronous `$HOME/SIGMA` filesystem inventory before the first real learning turn. That conflicts with the project requirement that the Oppo archive be discovered incrementally/batched/persistently and that learning be able to begin from already-discovered material without waiting for a complete deep scan.

Therefore the V1 continuous runner must not be promoted directly to the real ~10 GB archive.

## V2 source-ready artifacts

```text
SIGMA_C5_MECHANICAL_BRIDGE_V2.py
SHA256=98bb028cb668612393e1d687064fdf999dc73ec059b410737468bcc2ec3927dc

RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_OPPO_V2.sh
SHA256=8d56f59eac0b52ff4eeac719925c5fa7d52857154ca462390b494760ea17c344

RUN_SIGMA_C5_AUTONOMOUS_SELF_LEARNING_PREFLIGHT_V2.sh
SHA256=f629139361ef11b4b458b409a7a3e385b8aed24d0675b0b3782bfdb46ed4efb1

RUN_SIGMA_C5_REAL_OPPO_BOUNDED_SHADOW_V2.sh
SHA256=3723049249856dbee47f70bdc9c96306042e7c6e65cf66314eafd5a27ef8333a

SIGMA_C5_INCREMENTAL_CATALOG_REAL_SHADOW_V2.md
SHA256=8c6f050038e627d74323303cdb9abe87a06d4f63fbb670f811f393f1fbcbbe0d

INSTALL_SIGMA_C5_V2_INCREMENTAL_PATCH.sh
SHA256=6c5f2e551e6105f43335d58a15fdcb0e1d27bebf88937a33e20ea76cf83709e6

SIGMA_C5_V2_INCREMENTAL_PATCH.tgz
SHA256=4a99c02fa06de9674603f12de086b72f83ad22ec433e229461ed6cd63015e20a
```

## Mechanical catalog changes

V2 replaces blocking full-catalog creation with a concurrent persistent SQLite catalog frontier:

- already-discovered entries become available to native SIGMA while filesystem discovery continues;
- directory frontier is persisted;
- discovered file versions are persisted;
- an interrupted cataloger resumes without restarting the entire tree; at worst the interrupted in-progress directory is rescanned and exact file identities deduplicate repeats;
- file identity remains mechanical: path/device/inode/size/mtime;
- refresh scans add changed/new versions and deduplicate unchanged versions;
- host assigns no semantic relevance/rank/lesson priority.

Learning exclusions are mechanical governance/security classes only. C5 control/test subtrees are excluded to prevent recursive ingestion. Result/control/security records are not promoted as lessons by host.

## V2 preflight design

Before real archive execution, the V2 preflight must prove in isolated fixtures:

```text
PARTIAL_DISCOVERY_AVAILABLE_BEFORE_SCAN_COMPLETE
INTERRUPTED_CATALOG_RESUME
UNCHANGED_VERSION_DEDUPLICATION
CHANGED_VERSION_DISCOVERY
RESULT_SECURITY_CONTROL_POLICY
C5_CONTROL_SUBTREE_EXCLUSION
C5_V1_NATIVE_COGNITIVE_REGRESSION_A_THROUGH_G
```

No live network and no real Oppo archive mutation occurs in the V2 preflight.

## Bounded real-Oppo shadow gate

Only after V2 preflight PASS, the bounded real shadow may run against the real `$HOME/SIGMA` archive using an isolated state root. It has a mechanical turn bound and fetch-count bound, requires at least one real segment commit, and verifies `knowledge_v2/HEAD` remains unchanged.

The gate does not force SIGMA to emit an Internet request. If native SIGMA emits one, exact network transport may occur inside the mechanical budget; otherwise live Internet remains `NOT_OBSERVED` rather than being faked.

## Claim boundary

```text
C5_V2_SOURCE_READY=YES
C5_V2_PREFLIGHT=NOT_RUN
C5_V2_REAL_OPPO_SHADOW=NOT_RUN
REAL_OPPO_10GB_LEARNING=NOT_PROVEN
LIVE_NATIVE_SELF_INITIATED_INTERNET_REAL_SHADOW=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
PRODUCTION_ADMISSION=NO
```
