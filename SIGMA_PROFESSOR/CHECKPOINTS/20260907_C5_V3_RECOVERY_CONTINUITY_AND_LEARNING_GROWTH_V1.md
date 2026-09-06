# C5 V3 Recovery Continuity + Learning Growth V1

Date: 2026-09-07 (Asia/Ho_Chi_Minh)  
Branch: `SIGMA_LIFE`  
Status: `RECOVERY_PROTOCOL_SOURCE_READY / RUNTIME_ADMISSION_REQUIRES_CASE-SPECIFIC_EVIDENCE`

## Purpose

Define how the single SIGMA C5 V3 may be recovered after a process stop without creating a second SIGMA, resetting cognitive state, silently rolling state backward, or treating a mere process restart as successful learning.

Recovery is valid only when it preserves exact SIGMA identity and the same persistent state lineage. A stronger claim that SIGMA became more capable requires post-recovery learning evidence and a fixed benchmark/replay comparison; increasing counters alone is not sufficient.

## Locked SIGMA identity

The following identities must remain exact across recovery:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
C5_NATIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
C5_V3_RUNNER_SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb
SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
STATE_LINEAGE=$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
```

PID is not identity. A valid resumed V3 may receive a new PID. Runtime code must resolve the current PID dynamically and verify that it is the exact V3 runner process.

```text
PID_REUSE_AS_IDENTITY=FORBIDDEN
SECOND_SIGMA_CREATION=FORBIDDEN
SECOND_COGNITIVE_WRITER=FORBIDDEN
STATE_RESET_ON_RECOVERY=FORBIDDEN
```

## Recovery ownership boundary

Recovery may repair only mechanically provable transient/runtime inconsistencies. It must not infer semantic intent, select learning work, rewrite queries, promote knowledge, or edit cognitive tables to force progress.

```text
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_QUERY_GENERATION=NO
HOST_WORK_SELECTION=NO
HOST_KNOWLEDGE_PROMOTION=NO
HOST_SEMANTIC_RECOVERY_GUESSING=NO
```

## Proven recovery class A — stale local-active after committed EOF

Observed machine pattern:

```text
progress.offset_bytes == last_segment.next_offset_bytes
last_segment.offset_bytes + last_segment.segment_bytes == last_segment.next_offset_bytes
last_segment.eof == YES
local_active_record still present for the same entry
```

In this exact class, the bytes are already committed through EOF. Recovery may archive the stale runtime marker and remove only that stale active marker before restarting the exact V3 runner.

Required invariants:

```text
SQLITE_ROWS_MODIFIED=0
SEGMENT_HISTORY_MODIFIED=0
EVIDENCE_MODIFIED=0
KNOWLEDGE_MODIFIED=0
ORIGINAL_MARKER_ARCHIVED=YES
```

This is a runtime-marker recovery, not a cognitive-state rewrite.

## Proven recovery class B — missing CURRENT_STREAM with a single unambiguous active stream

Native core stream predicate:

```text
LOCAL_SEGMENT_READY    -> EXPECTED_STREAM=LOCAL
EXTERNAL_SEGMENT_READY -> EXPECTED_STREAM=EXTERNAL

if CURRENT_STREAM != EXPECTED_STREAM:
    ACTION=REFUSE_STREAM_STATE
```

Observed local case:

```text
LOCAL_ACTIVE entry matches segment_entry_id
progress offset matches committed next offset
segment bytes are non-empty
segment status is OK
segment EOF is NO
external active marker is absent
current_stream.txt is missing
```

When exactly one active stream exists and its state is mechanically consistent, recovery may reconstruct only the missing transient protocol field:

```text
current_stream.txt=LOCAL
```

or, for the symmetric external case:

```text
current_stream.txt=EXTERNAL
```

Required invariants:

```text
NATIVE_CORE_MODIFIED=NO
V3_RUNNER_MODIFIED=NO
SQLITE_ROWS_MODIFIED=0
ACTIVE_MARKER_MODIFIED=0
EVIDENCE_MODIFIED=0
KNOWLEDGE_MODIFIED=0
```

## Dual-active state — mandatory HOLD

A later runtime observation showed:

```text
LOCAL_ACTIVE_PRESENT=1
EXTERNAL_ACTIVE_PRESENT=1
V3_STOPPED=YES
```

This state is ambiguous unless additional mechanical evidence proves which stream transition is authoritative. Therefore:

```text
AUTO_CLEAR_LOCAL=NO
AUTO_CLEAR_EXTERNAL=NO
AUTO_SET_CURRENT_STREAM=NO
AUTO_RESTART_V3=NO
RECOVERY_DECISION=HOLD
```

The recovery layer must inspect the exact local/external active records, current event, current stream field, segment entry IDs, progress rows, recent committed segment rows, and the last native stop context before any state change.

## Unknown or non-proven crash points

Any state that is not one of the explicitly proven recovery classes must remain HOLD.

Examples:

- both local and external streams active without a mechanically proven winner;
- active non-EOF state with mismatched entry IDs or offsets;
- malformed or missing progress/segment provenance;
- multiple exact V3 processes;
- identity SHA/fingerprint mismatch;
- state counters lower than an accepted prior baseline.

```text
UNKNOWN_RECOVERY_AUTO_FIX=FORBIDDEN
UNKNOWN_RECOVERY_AUTO_RESTART_LOOP=FORBIDDEN
```

## Stable operation requirement

Recovery must not create a restart storm. Supervisors must use circuit breaking and backoff. Per-site HTTP errors such as `403`, `404`, `429`, or `5xx` are acquisition outcomes and must not be treated as V3 process-failure events.

```text
WEBSITE_HTTP_FAILURE_RESTARTS_V3=NO
WEBSITE_HTTP_FAILURE_RESTARTS_WHOLE_SYSTEM=NO
PROCESS_RESTART_STORM=FORBIDDEN
```

Internet acquisition remains a separate lane from C5 V3 cognition.

## Same-SIGMA non-regression gate

Before and after recovery, the committed state must not move backward.

Minimum mechanical counters:

```text
segment_commits_after >= segment_commits_before
evidence_after >= evidence_before
knowledge_after >= knowledge_before
```

Any regression requires HOLD.

```text
STATE_NON_REGRESSION=REQUIRED
ROLLBACK_TO_OLDER_COGNITIVE_STATE=FORBIDDEN
```

Counter growth proves committed-state growth only; it does not by itself prove semantic understanding or improved reasoning ability.

## Recovery is not enough — post-recovery growth gate

A recovery must not be called successful merely because a PID exists.

Minimum post-recovery operational gate:

1. exact identity and same state lineage PASS;
2. exact V3 runner remains alive through a stability window;
3. no immediate repeat of the same refusal condition;
4. at least one new valid native processing transition is observed;
5. committed state remains non-regressive;
6. over an appropriate learning window, new segment/evidence/knowledge progress is mechanically observed when new learnable material is available;
7. Internet acquisition, when enabled, remains a separate process and host does not generate queries or choose web results.

Suggested claim vocabulary:

```text
RECOVERY_PROCESS_ALIVE=PASS
RECOVERY_STATE_CONTINUITY=PASS
POST_RECOVERY_LEARNING_PROGRESS=OBSERVED|NOT_YET_OBSERVED
```

Do not emit `SMARTER=YES` from counters alone.

## Better-learning / capability-growth requirement

The user requirement is that recovery should preserve the same SIGMA and support continued improvement rather than merely restoring a process.

The development target is therefore:

```text
RECOVER
-> PRESERVE IDENTITY
-> PRESERVE COMMITTED MEMORY/EVIDENCE/KNOWLEDGE
-> RESUME NATIVE LEARNING
-> ACQUIRE NEW AUTHORIZED MATERIAL
-> ACCUMULATE NEW NON-DUPLICATE EVIDENCE/KNOWLEDGE
-> REPLAY FIXED BENCHMARKS
-> COMPARE PRE/POST CAPABILITY
```

A claim of improved capability requires a fixed benchmark or replay suite with comparable inputs and objective machine evidence. Acceptable examples include improved success rate, fewer native refusal/failure paths on the same benchmark set, greater evidence-supported completion, or other predeclared operational metrics.

```text
MORE_COUNTERS_EQUALS_SMARTER=NO
FIXED_BENCHMARK_REQUIRED_FOR_CAPABILITY_IMPROVEMENT_CLAIM=YES
```

## Internet learning continuity

General-web ingress may continue to provide public HTTPS material across unrestricted subjects, subject to per-request safety and rights constraints. The Internet lane must remain mechanically separate:

```text
HOST_QUERY_GENERATION=NO
HOST_QUERY_REWRITE=NO
HOST_WEB_RESULT_SELECTION=NO
NATIVE_WEB_CANDIDATE_SELECTION=YES
GLOBAL_SUBJECT_LIMIT=NONE
GLOBAL_QUERY_LIMIT=NONE
GLOBAL_FETCH_LIMIT=NONE
PAYWALL_BYPASS=NO
DRM_BYPASS=NO
```

A fetched document is not automatically learned:

```text
FETCHED_EQUALS_LEARNED=NO
```

End-to-end learning evidence requires C5 V3 itself to select/process the admitted material and produce subsequent evidence/knowledge state changes.

## Current machine baseline recorded during this recovery work

Latest supplied identity/non-regression evidence included:

```text
SAME_SIGMA_IDENTITY=PASS
SEGMENT_COMMITS_COUNT=3046
EVIDENCE_COUNT=10671
KNOWLEDGE_COUNT=2223
STATE_NON_REGRESSION=PASS
```

These counters are a continuity baseline, not an intelligence score.

## Claim boundary

This checkpoint records recovery rules and observed recovery classes. It does not claim arbitrary crash-point recovery, perfect uptime, semantic understanding, or proven intelligence improvement.

Keep:

```text
C5_V3_RECOVERY_PROTOCOL_V1=SOURCE_READY
PROVEN_STALE_EOF_RECOVERY=YES_IN_EXACT_OBSERVED_CLASS
PROVEN_MISSING_CURRENT_STREAM_RECOVERY=YES_ONLY_WHEN_SINGLE_ACTIVE_STREAM_AND_MECHANICALLY_CONSISTENT
DUAL_ACTIVE_AUTORECOVERY=NO_HOLD_REQUIRED
ARBITRARY_CRASH_POINT_RECOVERY=NOT_PROVEN
STATE_NON_REGRESSION=REQUIRED
POST_RECOVERY_LEARNING_PROGRESS=REQUIRED_FOR_GROWTH_CLAIM
FIXED_BENCHMARK=REQUIRED_FOR_SMARTER_CLAIM
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```
