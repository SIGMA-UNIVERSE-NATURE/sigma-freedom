# V4-B.1 SEGMENTED RECEIVED-CONTEXT LEARNER — ADMITTED PASS

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

## Status

`V4B1_SEGMENTED_RECEIVED_CONTEXT_LEARNER_PREFLIGHT=PASS`

`SEGMENTED_RECEIVED_CONTEXT_LEARNING=PROVEN_IN_BOUNDED_TESTED_SCOPE`

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Locked runtime evidence

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

Native source SHA256:
`2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`

Runner Git blob:
`4faf37671c591f7201c930bc5f000a542d377d8a`

Runner SHA256 canonical Termux observation:
`3e601c8a6fae5d1e5b93909d150f90e7918e4cd72936176e05b6de908e512f03`

The user-provided final runtime tail did not include the V4-B bytecode SHA line. Do not invent it.

## Admitted gates

- `TWO_LINE_NATIVE_SEGMENT_PROGRESS=PASS`
- `FRESH_VM_CURSOR_RESUME=PASS`
- `MALFORMED_CURSOR_TAIL_IGNORED=PASS`
- `LEARNED_ONLY_AFTER_ALL_SEGMENTS_COMPLETE=PASS`
- `ALREADY_COMPLETE_IDEMPOTENCY=PASS`
- `EVIDENCE_ONLY_CRASH_RETRY_NO_DUPLICATE=PASS`
- `FOREIGN_CONTEXT_CURSOR_IGNORED=PASS`
- `TOKEN_LIMIT_REFUSAL=PASS`
- `CONTEXT_LINE_LIMIT_REFUSAL=PASS`
- `FINAL_CURSOR_COMPLETION_RECOVERY=PASS`
- `CURSOR_OUT_OF_RANGE_REFUSAL=PASS`
- `SHADOW_STATE_NAMESPACE_ISOLATION=PASS`
- `PRODUCTION_BRAIN_WRITE_TARGET=NO`
- `PRODUCTION_V24_REMAINED_RUNNING_SAME_PID=PASS`
- `FETCHED_EQUALS_LEARNED=NO`
- `HOST_SEGMENT_SELECTION=NO`
- `HOST_COMPLETION_DECISION=NO`
- `HOST_RETRY_DECISION=NO`
- `HOST_LEARNING=NO`

## Important runtime observations

Final-cursor / missing-completion recovery:
- latest cursor represented the end of the 2-line context;
- native learner emitted `COMPLETION_RECOVERY_REQUIRED 1`;
- native learner emitted `COMPLETION_RECOVERY_ALLOWED 1`;
- `STATUS RECOVERED_COMPLETION`;
- no duplicate structural evidence was produced.

Out-of-range cursor refusal:
- context had 2 lines;
- latest cursor decoded to start line 3;
- `CURSOR_OUT_OF_RANGE 1`;
- `MUTATION_ALLOWED 0`;
- `STATUS REFUSE_CURSOR_OUT_OF_RANGE`.

Production V2.4 PID observed after test:
`831`

## Claim boundary

V4-B proves bounded structural received-context learning with persisted segmented progress and tested recovery/refusal behavior. It does not yet prove that the real V2.4 contexts that previously failed with VM `rc=9` can be completed by V4-B.

Keep:
- `REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `V4_PRODUCTION_PROMOTION_ALLOWED=NO`

## Next action

Replay the real V2.4 held contexts that previously emitted `SIGMA_LEARN_FAILED ... rc=9` through the isolated V4-B segmented learner. Preserve exact source context bytes, context SHA identities, every native VM return code, segment cursor progression, completion status, production V2.4 PID before/after, and shadow isolation evidence.

Known real failed context identities from production evidence include:
- `49c16c567fcbd0df0241b249e2b51dbf8e20d23ec1dc78ff8d92e3233dda9382`
- `59cd0bc563b1dc8566c88623366403b53f4e9094ca98ef4fe2d9e6531dc5a774`
- `0d911059d92f2af2601f39420c7aa0865fb24fbbc96aca96961d53b19260d8c3`
- `c12f847d694599d12cf35b5f489f1061e79a3fe3cf2f648684da55d387a2b16b`
- `ee5aca6dbe12ffcdd7e5b4aefeb3b5f8bb418b7d9eb4f59404c76b661bc086ba`

Do not stop or mutate production V2.4 for this replay gate.
