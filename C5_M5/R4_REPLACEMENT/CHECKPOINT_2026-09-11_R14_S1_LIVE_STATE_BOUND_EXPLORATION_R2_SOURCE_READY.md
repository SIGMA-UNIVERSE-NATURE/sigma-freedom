# CHECKPOINT — R14 S1 live state-bound exploration R2 — source ready

Scope: source/package ready only. No machine PASS is claimed until Oppo executes the bundle.

## Exact inherited learned-state evidence

The live gate binds to the known C5V4 long-document/replay run:

`$HOME/SIGMA/sigma_genesis1/.sigma_c5v4_candidate/C5V4_LONG_DOCUMENT_CURRICULUM_R7_20260911T013357/test`

Exact required artifacts:

```text
model.final.inspect SHA256=90d62960e542a22d9e83239d35379e490b855557a8ff6e42ad2f7a975950388b
POST_LONGDOC_REPLAY_DECISION.stdout SHA256=93cb493cdb932c83d278ab6a87657f7593fcb49d3be6a8345b53ffb4676666fd
POST_LONGDOC_REPLAY_COMMIT_RECEIPT.stdout SHA256=3ee288dba7569a7d229c8706a0e12009e42d4ab628e6b4b75c045aa80a62eccc
WEIGHT_FINGERPRINT64=52218bad5d5069de
ACCEPTED_UPDATES=10
REJECTED_UPDATES=6
R5_REPLAY_CONSOLIDATIONS=2
```

These artifacts were received in the uploaded exact run snapshot. They bind the gate to an actually advanced C5V4 learned-state/replay evidence chain rather than a synthetic host-created drive.

## Bundle identity

```text
BUNDLE=SIGMA_C5V4_R14_S1_LIVE_STATE_BOUND_EXPLORATION_R2_BUNDLE.zip
BUNDLE_SHA256=d360b1941d841570a10e14204b13619e9e27ff24a2a1a2ffe89b8392015b1084
MANIFEST_SHA256=b3dc2b4c599c4f165d4cae458fd99e0e30d1fa5c85a87df2d8a99a0fa3191a3f
SOURCE_SHA256=d210c8422ff9758c4c89ca61c25e661278441c30c642d800ac35cb9ade6bff28
RUNNER_SHA256=5d949d19ac35f2f38171a93bdc9a24a13c80e0bab74197d5f12b0ca0bad67d3e
```

Locked toolchain remains:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Gate design

- Replays/inherits the exact D4 AVAILABLE-ONLY candidate pool.
- Selector sees only opaque exact candidate IDs, not door labels or capability classes.
- No host-created `drive_u` is accepted in this live gate.
- Native `.sigma` derives an exploration slot from exact learned-state evidence bytes.
- `NONE` remains allowed.
- No tool is acquired or executed in S1 LIVE.
- Host only verifies exact hashes/membership and transports bytes.

## Claim ceiling

Even if machine PASS:

```text
SIGMA_TOOL_SELF_SELECTION_RUNTIME=PASS_IN_STATE_BOUND_EXPLORATION_SCOPE
SIGMA_SELF_SELECTS_CAPABILITIES=NOT_PROVEN
SEMANTIC_CAPABILITY_FIT=NOT_PROVEN
TOOL_UTILITY_LEARNING=NOT_PROVEN
TOOL_EXECUTION=NO
```

The next gate after a live PASS is S2: execute only the exact native-selected candidate, return raw result unchanged, then begin learned tool-utility evidence. No host reselection is permitted.
