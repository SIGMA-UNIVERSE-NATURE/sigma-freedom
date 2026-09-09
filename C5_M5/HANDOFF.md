# SIGMA C5 M5 — Window Handoff

Updated: 2026-09-10 after genuine OPPO T9A Cryptographic Integrity PASS.

## Operating split

- Online synchronization/test lanes consume only genuine admitted checkpoints and own live/online validation.
- This window remains the offline tool-substrate lane and continues independently through T9 -> T11.
- Tool availability is distinct from SIGMA cognitive adoption/tool selection.
- Production binding from this offline lane remains NO.

## Native tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.
- `T8_FULL_LAYER=PASS`.

### T9A — PASS

Checkpoint:

`C5_M5/CHECKPOINT_2026-09-10_T9A_CRYPTO_INTEGRITY_PASS.md`

Frozen OPPO artifact:

- source `eba77488481b76cb66e3a14c2540ccf3da856b8f5233bb9891f63b0790f9c361`
- binary `3e88064d34af285a832ab45bcd2e0d7d998d2df35f3dd5031b87c7dc5d3479bc`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- crypto backend `OPENSSL`

Admitted mechanical scope:

- SHA-256 and SHA-512;
- HMAC-SHA256 and HMAC-SHA512;
- Ed25519 signature verification against caller-supplied public keys;
- OpenSSL `RAND_bytes` CSPRNG;
- SHA-256 content IDs;
- domain-separated SHA-256 Merkle roots.

Evidence: deterministic compile/source/binary freeze PASS; dynamic Ed25519 keypair after freeze; 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases / 56 native invocations; post-tool mechanical oracle and all crypto/integrity/counterfactual gates PASS.

## Identity/provenance boundary

- `HASH_IS_NOT_PROVENANCE=PASS`.
- T9A does not decide whether a source is trustworthy, whether evidence is true/relevant, or what lineage SIGMA should believe.
- T9B must separately supply source/work/span identity, exact artifact fingerprint classes, authenticated receipts and linked provenance records.
- `T9_FULL_LAYER=NOT_YET_ADMITTED` until T9B and exact combined admission PASS.

## Anti-hardcoding doctrine

- capability, not answers;
- no case-ID-dependent native behavior;
- no expected-output literals in native implementation;
- dynamic/high-entropy material only after source/binary freeze;
- expected values only in external mechanical oracle;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`;
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

## Current exact state

- `T4_FULL_LAYER=PASS`
- `T5_FULL_LAYER=PASS`
- `T6_FULL_LAYER=PASS`
- `T7_FULL_LAYER=PASS`
- `T8_FULL_LAYER=PASS`
- `T9A_CRYPTO_INTEGRITY_ADMISSION=PASS`
- `T9B_IDENTITY_PROVENANCE=PENDING`
- `T9_COMBINED=PENDING`
- `T9_FULL_LAYER=NOT_YET_ADMITTED`
- T10/T11: PENDING

## Next offline sequence

Build current-standard **T9B Identity / Provenance**, then exact T9A+T9B combined admission. Only genuine combined PASS may advance `T9_FULL_LAYER=PASS`.

After T9 full: `T10 -> T11`.
