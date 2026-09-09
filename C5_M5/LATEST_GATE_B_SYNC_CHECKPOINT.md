# SIGMA C5V3 Gate B — Latest Synchronization Checkpoint

Updated: 2026-09-10 after genuine OPPO T9A Cryptographic Integrity PASS.

## Latest authoritative checkpoint

`C5_M5/CHECKPOINT_2026-09-10_T9A_CRYPTO_INTEGRITY_PASS.md`

## Latest admitted tool-substrate chain

- T0 inherited only where exact prior evidence applies.
- T1/T2/T3 admitted subsets + mixed compatibility PASS.
- `T4_FULL_LAYER=PASS`.
- `T5_FULL_LAYER=PASS`.
- `T6_FULL_LAYER=PASS`.
- `T7_FULL_LAYER=PASS`.
- `T8_FULL_LAYER=PASS`.
- T9A cryptographic integrity primitives: PASS on OPPO.
- T9B identity/provenance: PENDING.
- T9 combined: PENDING.
- T10/T11: PENDING in offline substrate lane.

## Frozen T9A artifact

- source `eba77488481b76cb66e3a14c2540ccf3da856b8f5233bb9891f63b0790f9c361`
- binary `3e88064d34af285a832ab45bcd2e0d7d998d2df35f3dd5031b87c7dc5d3479bc`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- crypto backend `OPENSSL`

## T9A admitted evidence

- deterministic compile/source/binary freeze PASS
- dynamic Ed25519 keypair generated after freeze PASS
- 16 directed + 32 randomized-after-freeze + 2 replay = 50 cases
- 56 native process invocations
- post-tool mechanical oracle PASS
- SHA-256 PASS
- SHA-512 PASS
- HMAC-SHA256 PASS
- HMAC-SHA512 PASS
- Ed25519 signature verification PASS
- OpenSSL `RAND_bytes` CSPRNG PASS
- SHA-256 content ID PASS
- domain-separated SHA-256 Merkle root PASS
- counterfactual integrity change PASS

## Critical claim boundary

- `HASH_IS_NOT_PROVENANCE=PASS`
- `T9_FULL_LAYER=NOT_YET_ADMITTED`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

T9A integrity primitives do not establish semantic trust, truth or provenance history. T9B must separately admit source/work/span identity, exact artifact fingerprint classes, authenticated receipts and linked provenance records.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

Existing R10 production-lineage synchronization evidence remains separate and does not imply live binding.

## Next offline sequence

`T9B -> T9 combined -> T10 -> T11`.
