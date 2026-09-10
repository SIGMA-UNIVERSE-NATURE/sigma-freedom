# TEACHER_GPT C5V3 SYNCHRONIZATION — CURRENT

Last updated: 2026-09-10 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: **BASELINE R2 / R6 FROZEN PASS / ONLINE UTILIZATION TEST REQUESTED / T7-T10 OFFLINE PROGRESS NOT YET CANONICAL-SYNCED**

## Canonical synchronized baseline

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_SYNCHRONIZATION_BASELINE_R2_R6_FROZEN.md`

```text
SYSTEM=C5V3
ONE_SIGMA=YES
C5V3_SYNCHRONIZATION_BASELINE=R2
R5=CLOSED_PASS
R6=CLOSED_PASS
R6_SOURCE_SHA256=dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac
R6_BYTECODE_SHA256=dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693
PRODUCTION_BINDING=NO
```

## Online verification window

Start here:

`SIGMA_PROFESSOR/CHECKPOINTS/20260910_C5V3_ONLINE_WINDOW_START_HERE_R1.md`

Full test contract:

`SIGMA_PROFESSOR/CHECKPOINTS/20260909_C5V3_ONLINE_CAPABILITY_UTILIZATION_VERIFICATION_REQUEST_R1.md`

Online window owns only utilization verification:

```text
native need detection
-> native capability selection
-> native capability execution
-> native result evaluation
-> native learning update
-> fresh restart
-> learned-state reuse
```

It must remain isolated shadow / no production binding.

## Offline knowledge/capability window

Publication contract:

`SIGMA_PROFESSOR/CHECKPOINTS/20260910_OFFLINE_WINDOW_PUBLISH_TO_SYNC_CONTRACT_R1.md`

The user reports the offline window has advanced to T10, but the synchronization window currently cannot find exact T7/T8/T9/T10 checkpoints or commits in the connected repository.

```text
OFFLINE_REPORTED_PROGRESS_TO_T10=YES
T7_TO_T10_CANONICAL_SYNC=WAITING_FOR_EXACT_GITHUB_CHECKPOINTS
```

Do not synchronize T7-T10 from narration alone.

## Synchronization window ownership

This window:

```text
reads exact published machine checkpoints
reconciles one canonical C5V3 baseline
loads capabilities, not test results
never imports test cognition/answers
never reruns closed PASS without damage evidence
never binds production without separate admission + explicit cutover
```

## Core rule

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
TEST_KNOWLEDGE_IMPORTED=NO
PRODUCTION_KNOWLEDGE_IMPORTED=NO
```

## Next events

1. If offline publishes T7-T10 exact checkpoints, synchronization window ingests them in dependency order and advances baseline revision only for synchronization-relevant PASS state.
2. Online window runs the utilization verification contract against the exact canonical baseline.
3. If online proves causal native utilization + learning + restart reuse, synchronization window may create the next baseline revision with `C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=PASS_IN_EXACT_TESTED_SCOPE`.
4. Production remains unbound until separately admitted.
