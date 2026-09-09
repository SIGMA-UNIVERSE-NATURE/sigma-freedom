# SIGMA C5 M5 — T9A Cryptographic Integrity PASS

Date: 2026-09-10
Device evidence: genuine OPPO/Termux offline admission.

## Result

- `T9A_CRYPTO_INTEGRITY_ADMISSION=PASS`
- `RESULT=T9A_PASS`
- `T9_FULL_LAYER=PENDING_T9B_IDENTITY_PROVENANCE_AND_COMBINED`

## Frozen OPPO artifact

- source SHA256 `eba77488481b76cb66e3a14c2540ccf3da856b8f5233bb9891f63b0790f9c361`
- binary SHA256 `3e88064d34af285a832ab45bcd2e0d7d998d2df35f3dd5031b87c7dc5d3479bc`
- compiler `/data/data/com.termux/files/usr/bin/clang++`
- crypto backend `OPENSSL`

## Admission evidence

- deterministic compile PASS
- source hash freeze PASS
- binary hash freeze PASS
- high-entropy literal leak audit PASS
- dynamic Ed25519 keypair generated after freeze PASS
- directed cases `16`
- randomized-after-freeze cases `32`
- replay cases `2`
- total cases `50`
- native process invocations `56`
- post-tool mechanical oracle PASS

## Admitted mechanical scope

- SHA-256
- SHA-512
- HMAC-SHA256
- HMAC-SHA512
- Ed25519 signature verification against caller-supplied public key material
- OpenSSL `RAND_bytes` CSPRNG
- SHA-256 content ID
- domain-separated SHA-256 Merkle root

Merkle mechanics are explicitly domain separated:

- leaf = `SHA256(0x00 || leaf_bytes)`
- parent = `SHA256(0x01 || left_hash || right_hash)`
- odd final node duplicates the final child
- empty root = `SHA256(0x02)`

## Counterfactual / anti-hardcoding

- `COUNTERFACTUAL_INTEGRITY_CHANGE=PASS`
- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`
- `HOST_SEMANTIC_SUBSTITUTION=NO`
- `CORE_TEST_ORACLE_CONTAMINATION=NO`

## Critical identity/provenance boundary

- `HASH_IS_NOT_PROVENANCE=PASS`
- `SIGMA_COGNITIVE_TOOL_ADOPTION=NOT_CLAIMED`

Hashes, MACs, signatures, CSPRNG output, content IDs and Merkle roots provide cryptographic/integrity mechanics only. They do not establish source semantics, truth, relevance, provenance history or SIGMA trust judgments. Source/work/span identity, exact artifact fingerprint classes, authenticated receipts and linked provenance records remain T9B.

## Production boundary

- `ONLINE_SYNC=NO`
- `PRODUCTION_STATE_WRITE=NO`
- `PRODUCTION_MUTATION=NO`
- `PRODUCTION_BINDING=NO`

Immediate offline next gate: `T9B_IDENTITY_PROVENANCE`, then exact T9A+T9B combined admission before `T9_FULL_LAYER=PASS` may be claimed.
