# V5-K6 Common Provenance Normalization — Source Ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN

## Dependency

I5C Wikipedia exact-fetch binding is admitted PASS in exact tested scope.

Latest dependency checkpoint:
`DOCS/GPT_REFERENCE/CHECKPOINTS/20260906_I5C_WIKIPEDIA_EXACT_FETCH_BINDING_PASS.md`

Canonical bound machine identity:

```text
PAGE_ID=19378
TITLE=Mind
REVISION_ID=1373231762
REVISION_TIMESTAMP=2026-09-04T19:05:08Z
```

These values are machine evidence only and are not embedded in the new V5-K6 native source.

## Capability

V5-K6 normalizes structural provenance into a common native protocol containing:

```text
RUN_ID
SOURCE_FAMILY
SOURCE_EDITION
RESOURCE_ID
RESOURCE_TITLE
SOURCE_VERSION
SOURCE_TIMESTAMP
REQUEST_ID
RETRIEVAL_ID
RETRIEVAL_TIMESTAMP
PAYLOAD_SHA256
TRANSPORT_RC
TRANSPORT_HTTP_CODE
BINDING_STATUS
```

The payload SHA256 is a mechanical hash over exact payload bytes. Retrieval timestamp is host-clock provenance only. Host does not make semantic, truth, knowledge-promotion, source-selection or resource-selection decisions.

## Source-ready identities

```text
BUNDLE_NAME=SIGMA_V5K6_NATIVE_ADMISSION_V1_COMMON_PROVENANCE_NORMALIZATION_BUNDLE.zip
BUNDLE_SHA256=43edd6fa674fb6bef203f23e6a96b3364a7bfac0bd3c663af923fe4d0e1e8209
SOURCE_SHA256=9e8befbc012ae81a8cf41e084a567ee86536db967970fe85514ee03f963b3bc3
RUNNER_SHA256=8cba482e84f36e2d6650af21e8e5599812a31e1822f0eced35bde508ca488395
LOCKED_SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
LOCKED_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
PLANNED_VM_INVOCATIONS=13
```

Static QA:

```text
BASH_SYNTAX_QA=PASS
NATIVE_SOURCE_CANONICAL_SOURCE_FAMILY_TOKEN_COUNT=0
NATIVE_SOURCE_CANONICAL_RESOURCE_TOKEN_COUNT=0
NATIVE_SOURCE_CANONICAL_REVISION_TOKEN_COUNT=0
PAYLOAD_HASH_ROLE=MECHANICAL_SHA256_ONLY
HOST_SEMANTIC_INTERPRETATION_QA=NO
HOST_TRUTH_DECISION_QA=NO
HOST_KNOWLEDGE_PROMOTION_QA=NO
TERMINAL_NOT_PROVEN_LINE_COUNT=0
```

## Admission gate

The runtime admission includes canonical normalization, idempotency, materially different dynamic provenance, invalid hash/hash-length refusals, missing-resource/request refusals, malformed memory, run-ID conflict, identical replay, source/bytecode immutability and step-limit audit.

No production state is mutated.

## Next action

Run the exact bundle under the locked Termux compiler/VM. Preserve the first HOLD/FAIL or final `=== V5K6 ADMISSION SUMMARY ===`.

On PASS, proceed to V5-K7 Evidence Graph integration using the exact native V5-K6 normalized event.
