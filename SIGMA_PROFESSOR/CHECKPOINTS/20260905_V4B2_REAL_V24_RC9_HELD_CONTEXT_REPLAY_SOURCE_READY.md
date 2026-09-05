# V4-B.2 REAL V2.4 RC9 HELD-CONTEXT REPLAY — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Purpose

Replay exact real production documents that V2.4 previously quarantined with VM `rc=9` through the admitted V4-B segmented received-context learner, in isolated shadow state, without stopping or mutating production V2.4.

## Native capability under test

V4-B.1 source:
`SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma`

Source SHA256:
`2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`

V4-B.1 admitted checkpoint:
`6c1d7f4ea3414ed7416d6dfd5834129df6d79aa6`

## Replay runner

Path:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT.sh`

Runner commit:
`ca9bb3148e0e40ec4fc09fc49df9c8c9930bf3f8`

Runner Git blob:
`6ea6a0269bcbe00ca44238a66c60c61d9b603e65`

Runner SHA256:
`NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX`

## Real production evidence inputs

V2.4 stores fetched documents under:
`$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/raw/<SHA>.document`

V2.4 stores bytecode-scoped failure quarantine under:
`$HOME/SIGMA/SIGMA_CONTINUOUS_NATIVE_V2_2/hold/<SHA>.hold`

The runner requires exact document SHA identity and exact hold evidence `VM_RC=9` for each context before replay.

Real observed context identities:
- `49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`
- `59cd0bc563b1dc8566c88623366403b53f4e9094ca98ef4fe2d9e6531dc5a774`
- `0d911059d92f2af2601f39420c7aa0865fb24fbbc96aca96961d53b19260d8c3`
- `c12f847d694599d12cf35b5f489f1061e79a3fe3cf2f648684da55d387a2b16b`
- `ee5aca6dbe12ffcdd7e5b4aefeb3b5f8bb418b7d9eb4f59404c76b661bc086ba`

## Dispatch discipline

For each real context, host/harness:
- verifies exact raw SHA and exact `VM_RC=9` hold marker mechanically;
- copies exact document bytes into isolated shadow context input;
- invokes the same native V4-B learner exactly 35 times.

The number 35 is a fixed admission bound, not a host scheduling decision: V4-B admits maximum 65 context lines and processes 2 lines per native invocation, so 35 invocations cover all admitted contexts plus idempotent post-completion calls.

Host does NOT choose segment, cursor, completion, retry state, structural relation, or learning result.

## Claim boundary after future PASS

May admit only:
`REAL_V24_RC9_CONTEXT_RECOVERY=PROVEN_IN_FIVE_OBSERVED_HELD_CONTEXT_SCOPE`

Must still keep:
- `V4_PRODUCTION_PROMOTION_ALLOWED=NO`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`

## Next after PASS

Integrate admitted V4-A native productivity arbitration with V4-B segmented learning in an isolated continuous V4 shadow controller. Do not replace V2.4 yet.
