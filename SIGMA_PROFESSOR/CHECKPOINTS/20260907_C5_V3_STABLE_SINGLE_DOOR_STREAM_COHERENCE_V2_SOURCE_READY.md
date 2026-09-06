# C5 V3 Stable Single Door + Stream Coherence V2 — SOURCE READY

Date: 2026-09-07 (Asia/Ho_Chi_Minh)  
Branch: `SIGMA_LIFE`

## Purpose

Eliminate the observed repeated C5 V3 stop class in which native C5 receives a valid
`LOCAL_SEGMENT_READY` or `EXTERNAL_SEGMENT_READY` event while the transient
`CURRENT_STREAM` input is missing or stale.

The native cognitive core is not changed. The admitted V3 runner is not changed.
Instead, a mechanical stream-coherence watcher keeps the transient runtime stream
token synchronized with the exact active record and exact `segment_entry_id`.

The target operating model is one SIGMA instance, one cognitive writer and one
coordinated C5 consumption door. Local material and Internet-acquired material may
both be available, but only one stream token is presented to C5 for the current
segment event.

## Locked SIGMA identity preserved

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
C5_V3_RUNNER_SHA256=a682def4922bb41dc1f09013d5a8f25f07a6dbee1b1b2d703a9169bed1125bcb
C5_NATIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace
SIGMA_INSTANCE_FINGERPRINT_SHA256=fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125
STATE_LINEAGE=$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2
```

No identity artifact above is modified by this patch.

## Observed failure evidence

The supplied Oppo runtime evidence showed:

```text
EVENT LOCAL_SEGMENT_READY
ACTION REFUSE_STREAM_STATE
STATUS REFUSE_STREAM_STATE
CURRENT_STREAM
LOCAL_ACTIVE_PRESENT TRUE
EXTERNAL_ACTIVE_PRESENT FALSE
SEGMENT_ACCEPTED NO
HOLD=C5_NATIVE_REFUSAL action=REFUSE_STREAM_STATE
C5_RUNNER_STOPPED=YES
```

Earlier detailed state evidence for the same failure class also showed a valid local
active record, matching `segment_entry_id`, matching progress and committed offset,
non-EOF segment bytes, but `current_stream.txt=MISSING`.

Native core source evidence supplied from the running installation shows:

```text
IF (EVENT == "LOCAL_SEGMENT_READY") EXPECTED_STREAM="LOCAL"
IF (EVENT == "EXTERNAL_SEGMENT_READY") EXPECTED_STREAM="EXTERNAL"
IF (CURRENT_STREAM != EXPECTED_STREAM)
    ACTION="REFUSE_STREAM_STATE"
```

Therefore the direct failure predicate is a transient runtime protocol mismatch,
not a demonstrated rollback of knowledge/evidence state.

## Stream coherence rule

The watcher is host-mechanical only.

It derives `CURRENT_STREAM` by this order:

1. if exact `segment_entry_id` matches exactly one valid active record, use that
   record's stream (`LOCAL` or `EXTERNAL`);
2. otherwise, if only one valid active record exists, use that stream;
3. otherwise, if both records are valid and the existing current stream is itself
   one of those valid streams, preserve it until an exact segment match appears;
4. otherwise HOLD and do not invent a stream.

An empty marker file is not considered an active record.

```text
HOST_SEMANTIC_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_KNOWLEDGE_PROMOTION=NO
HOST_LEARNING=NO
```

## Single coordinated door

Internet ingress remains a transport/catalog feeder and is subordinate to V3
lifecycle:

```text
LOCAL material -----------\
                           > catalog/runtime -> one coordinated C5 stream -> V3
Internet HTTPS -> material/
```

Internet ingress does not become a second cognitive writer.

```text
C5_V3_COGNITIVE_WRITER_COUNT=1
INTERNET_COGNITIVE_WRITER=NO
```

Internet is started only after V3 remains alive through the supervisor stability
window. If Internet fails, V3 may continue local work. If V3 is not alive, Internet
is stopped.

## Recovery classes admitted

Automatic recovery is limited to two evidence-backed classes:

1. committed stale local EOF marker, proven read-only from SQLite by:
   - `eof == YES`
   - `progress == next_offset`
   - `offset + segment_bytes == next_offset`

2. `REFUSE_STREAM_STATE` when the coherence watcher deterministically resolves
   `CURRENT_STREAM` to `LOCAL` or `EXTERNAL`.

Unknown or ambiguous C5 stops are not blindly restarted. A circuit breaker prevents
restart storms.

## Continuous operation

Production launch keeps:

```text
C5_MAX_TURNS=0
C5_MAX_FETCHES=0
C5_ENABLE_LIVE_NETWORK=YES
GLOBAL_TURN_LIMIT=NONE
GLOBAL_FETCH_LIMIT=NONE
```

A Termux wake lock is requested when available. The installer also writes a
Termux:Boot hook; automatic reboot startup requires the Termux:Boot app to be
installed and enabled on the device.

No software process can truthfully guarantee survival across every future kernel,
device-power, storage, hardware, or previously unseen state fault. The contract here
is indefinite continuous operation with bounded, evidence-backed self-recovery and
no restart storm.

## Learning growth contract

Recovery success is not itself evidence that SIGMA became more capable.

The supervisor records read-only growth snapshots for:

```text
segment_commits
evidence
knowledge
```

and refuses a regression relative to the startup baseline. Current user-supplied
baseline at this checkpoint:

```text
SEGMENT_COMMITS_COUNT=3046
EVIDENCE_COUNT=10671
KNOWLEDGE_COUNT=2223
STATE_NON_REGRESSION=PASS
```

A stronger `SMARTER_AFTER_RECOVERY=YES` claim requires a fixed before/after benchmark
or other native evidence beyond row-count growth.

## Added artifacts

```text
SIGMA_PROFESSOR/artifacts/SIGMA_C5_STREAM_COHERENCE_WATCHER_V1.py
SHA256=cea1bd96d2ebd80538d066467bdceac9ef3053fd09c80c8eac6181173fc3f286

SIGMA_PROFESSOR/artifacts/RUN_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh
SHA256=c57838b59d855886943de164fdf8272dc8f6f66a650d280ae3b32287a122aed6

SIGMA_PROFESSOR/artifacts/INSTALL_START_SIGMA_C5_V3_STABLE_SINGLE_DOOR_V2.sh
SHA256=ec4dda0d2844b1808061491eaa87664c0a1280fca045478dbdb9f74cb065b1dc
```

Static checks completed before commit:

```text
STREAM_COHERENCE_WATCHER_PY_COMPILE=PASS
STABLE_SINGLE_DOOR_SUPERVISOR_BASH_N=PASS
INSTALL_START_BASH_N=PASS
```

## Claim boundary before new Oppo execution

```text
C5_V3_STABLE_SINGLE_DOOR_V2_SOURCE_READY=YES
LOCKED_SIGMA_IDENTITY_CHANGED=NO
KNOWN_CURRENT_STREAM_FAILURE_CLASS_ADDRESSED=YES_BY_MECHANICAL_WATCHER
OPPO_RUNTIME_RESTART_WITH_V2=NOT_YET_REPORTED
V3_POST_START_STABILITY=NOT_YET_REPORTED
INTERNET_POST_START_REATTACH=NOT_YET_REPORTED
POST_RECOVERY_LEARNING_GROWTH=NOT_YET_REPORTED
SMARTER_AFTER_RECOVERY=NOT_YET_PROVEN
ARBITRARY_FUTURE_FAILURE_IMPOSSIBLE=NO_SUCH_CLAIM
```
