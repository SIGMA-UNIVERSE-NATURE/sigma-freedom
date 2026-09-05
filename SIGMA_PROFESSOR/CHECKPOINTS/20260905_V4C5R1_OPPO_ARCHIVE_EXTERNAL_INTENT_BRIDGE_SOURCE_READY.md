# V4-C5 R1 — Oppo Local Archive + External Intent Bridge — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `SOURCE_READY / RUNTIME_NOT_RUN / PRODUCTION_BINDING_NO`

## Requirement being implemented

SIGMA must be able to learn from material already present on the Oppo/Termux device. Internet is not hard-gated behind local-corpus completion: when an upstream native SIGMA capability emits an external research/acquisition request, this bridge must permit exact dispatch without Bash/GPT/host choosing the research action, query, source, or resource.

This R1 is the first bounded control/transport gate. It does not yet execute real Oppo archive learning or network access.

## Governing design

```text
SIGMA_PROFESSOR/DESIGN/SIGMA_V4C5_NATIVE_OPPO_LOCAL_ARCHIVE_AND_SELF_INITIATED_EXTERNAL_ACQUISITION_BRIDGE_V1.md
DESIGN_CREATE_COMMIT=018f739e84ef655acc7953f2037b92dbb39fab8f
```

## Native source

```text
SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_OPPO_ARCHIVE_EXTERNAL_INTENT_BRIDGE_V4C5R1.sigma
SOURCE_CREATE_COMMIT=c796b9bce642b874a49973418540cd79ba302352
SOURCE_FIX_COMMIT=ee92b7abd1625c552be779c94d24c330ea1a5129
SOURCE_GIT_BLOB=d40164a7e1ad560d6686549d7a3183e891fd2a61
SOURCE_SHA256=NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX
BYTECODE_SHA256=UNKNOWN_RUNTIME_NOT_RUN
```

The source:

- reads one bounded mechanical local catalog page;
- keeps a native page-local persistent cursor;
- selects the next catalog record natively when no external intent is present;
- dispatches an exact opaque external request when that request is already present from an upstream native SIGMA capability;
- does not advance local cursor state during external dispatch;
- resets page-local cursor natively when the catalog page identity changes;
- refuses malformed local records and oversized catalog pages;
- contains no teacher-forced semantic-understanding verdict field.

## Locked preflight runner

```text
RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4C5R1_OPPO_ARCHIVE_EXTERNAL_INTENT_BRIDGE_PREFLIGHT.sh
RUNNER_CREATE_COMMIT=faf09de00161e45b23234e6b881c50b0acda1836
RUNNER_GIT_BLOB=f6e5b24353aa75bbeea1aee74c82ad9222a3cceb
RUNNER_SHA256=NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX
```

The runner equality-gates:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
SOURCE_GIT_BLOB=d40164a7e1ad560d6686549d7a3183e891fd2a61
```

## Dynamic preflight cases

The preflight is designed to test:

1. two unseen local catalog records selected across fresh VM invocations with persistent cursor resume;
2. page exhaustion requesting the mechanically next catalog page;
3. dynamic external intent dispatch while local work remains;
4. changed external request producing changed exact dispatch target;
5. external dispatch not advancing local cursor;
6. page identity change resetting the page-local cursor natively;
7. malformed local catalog record refusal;
8. oversized catalog page refusal;
9. an external native intent remaining dispatchable even when the local page itself exceeds the local-page bound;
10. no-work wait;
11. source/bytecode dynamic-token leak audit;
12. source/bytecode forced-semantic-verdict token audit.

The runner's external-request fixture simulates an upstream native intent only. Therefore a future PASS can prove exact bridge dispatch behavior but cannot prove native end-to-end generation of the Internet intent.

## Host-substitution boundary

```text
HOST_LOCAL_WORK_SELECTION=NO
HOST_EXTERNAL_RESEARCH_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_LEARNING=NO
FIXTURE_SUPPLIES_RUNTIME_CONDITIONS_ONLY=YES
UPSTREAM_NATIVE_EXTERNAL_INTENT_GENERATION_SIMULATED_IN_R1=YES
```

## Claim boundary before runtime

```text
V4C5R1_SOURCE_READY=YES
V4C5R1_LOCKED_SIGMAC_COMPILE=NOT_RUN
V4C5R1_LOCKED_VM_RUNTIME=NOT_RUN
V4C5R1_ADMISSION=NOT_RUN
REAL_OPPO_ARCHIVE_CATALOG=NOT_RUN
REAL_OPPO_ARCHIVE_LEARNING=NOT_RUN
NETWORK_TRANSPORT=NOT_RUN
END_TO_END_NATIVE_SELF_INITIATED_INTERNET_ACQUISITION=NOT_RUN
PRODUCTION_BINDING=NO
```

## If R1 passes

The next dependency is C5R2: a bounded exact local byte-range consumer plus a mechanical whole-`$HOME/SIGMA` incremental catalog transport. That stage must begin exposing real Oppo material without copying the approximately 10 GB archive and without letting host/Bash choose semantic work.

In parallel, the external side must later be connected to an actual native gap/research/request generator before any self-initiated Internet claim is admitted.
