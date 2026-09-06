# C5 post-V3 continuous — observer + mechanical resume guard source ready

Date: 2026-09-06
Branch: `SIGMA_LIFE`

## Active runtime boundary

The currently running C5 V3 continuous learner is not modified by this checkpoint. Active device evidence supplied by the user established:

```text
SIGMA_RUNNING=YES
PID=20026
C5_V3_CONTINUOUS_STARTED=YES
C5_MAX_TURNS=0
C5_MAX_FETCHES=0
PRODUCTION_KNOWLEDGE_V2_BINDING=NO
```

No claim is made here that PID 20026 is still alive at any later time without fresh device evidence.

## Read-only live observer V1

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_C5_LIVE_OBSERVER_V1.sh`

Source SHA256:

`3e89cc516599a5c1b5e9d6df07b2a99d18a08c974558619cc1a2bab96c489539`

Properties:

- read-only PID/process observation;
- read-only C5 log observation;
- SQLite `mode=ro` + `PRAGMA query_only=ON` state reads;
- exact state counts;
- recent native knowledge records;
- recent native request records;
- HOLD/error rows;
- latest committed entry ID and catalog path when schema supports it;
- native review report observation;
- error-vault observation;
- legacy `knowledge_v2/HEAD` read-only observation;
- optional terminal refresh loop;
- `Ctrl+C` stops observer only, not SIGMA.

```text
OBSERVER_ROLE=MECHANICAL_READ_ONLY
OBSERVER_WRITES_C5_STATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
```

Static Bash syntax check passed off-device. Runtime Oppo observer execution is not yet claimed.

## Mechanical resume guard V1

Path:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_C5_V3_MECHANICAL_RESUME_GUARD_V1.sh`

Source SHA256:

`46a506af7d1f82421f0c2f1fea28a429ac44942afe038a57dadbc56457abfed5`

Properties:

- does nothing when exact V3 runner in PID file is alive;
- refuses duplicate launch if exact V3 runner is already active with stale/missing PID bookkeeping;
- verifies exact V3 runner SHA256 before launch;
- requires existing C5 state DB and catalog DB;
- may request Termux wakelock mechanically;
- starts the exact pinned V3 runner with `C5_MAX_TURNS=0`, `C5_MAX_FETCHES=0`, and live network enabled;
- performs only a process-alive/identity check after launch;
- does not claim post-restart learning progress from startup alone.

```text
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_QUERY_GENERATION=NO
HOST_WORK_SELECTION=NO
```

Static Bash syntax check passed off-device. The resume guard has NOT been enabled as a reboot hook and has NOT been runtime-tested on Oppo in this checkpoint.

## Remaining high-priority gaps

1. Real V3 native 180-second self-review + post-review resume evidence.
2. Oppo live observer runtime verification.
3. Reboot/Termux-process-loss automatic exact-state resume, after a controlled V3 restart/resume gate.
4. Long-horizon soak evidence.
5. Arbitrary crash-point recovery / stronger transactional recovery evidence.
6. Internet transport robustness beyond the current single Wikipedia search adapter while preserving native query/resource intent boundaries.
7. Native C5 persistent knowledge integration with canonical production knowledge storage, without host semantic promotion.
8. General semantic understanding, truth validation, and general autonomous reasoning remain separate unproven capabilities.

Cloudflare/R2 work is outside this lane.

## Claim boundary

```text
C5_LIVE_OBSERVER_V1_SOURCE_READY=YES
C5_LIVE_OBSERVER_V1_OPPO_RUNTIME=NOT_YET_TESTED
C5_V3_MECHANICAL_RESUME_GUARD_V1_SOURCE_READY=YES
C5_V3_MECHANICAL_RESUME_GUARD_V1_OPPO_RUNTIME=NOT_YET_TESTED
AUTO_RESUME_AFTER_REBOOT=NOT_YET_ENABLED
AUTO_RESUME_AFTER_REBOOT=NOT_PROVEN
REAL_180_SECOND_NATIVE_REVIEW=NOT_YET_PROVEN_BY_THIS_CHECKPOINT
LONG_HORIZON_CONTINUOUS_OPERATION=NOT_PROVEN
PRODUCTION_KNOWLEDGE_V2_BINDING=NO
```
