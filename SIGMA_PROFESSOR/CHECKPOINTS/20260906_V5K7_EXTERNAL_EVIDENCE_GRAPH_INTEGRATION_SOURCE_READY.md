# V5-K7 Native Admission V1 — External Evidence Graph Integration — SOURCE READY

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Frontier

V5-K6 machine PASS is the exact upstream dependency. V5-K7 binds the exact native V5-K6 normalized provenance event into the already-admitted V4-PK1 persistent hypergraph.

```text
V5-K6 native normalized provenance
-> V5-K7 native provenance-to-graph adapter
-> V4-PK1 admitted persistent hypergraph
```

V4-PK2 is intentionally audit-only in this admission and is not invoked on the active path.

## Locked runtime

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
```

## Artifact identities

```text
BUNDLE_NAME=SIGMA_V5K7_NATIVE_ADMISSION_V1_EXTERNAL_EVIDENCE_GRAPH_INTEGRATION_BUNDLE.zip
BUNDLE_SHA256=f2b8e38a5921ae949b6bede573fabf916f631452cb7b1def8e1c61d5ea0c5068
V5K7_SOURCE_SHA256=e8554f59391c20ccecaba81e1fba811844233e5718505e05e8991a26ccd1ca57
V5K7_RUNNER_SHA256=6e3a405ae2c14e5c4473892cbc39e45459b038faf47e99ba14b305e73eabeeba
V5K6_SOURCE_SHA256=9e8befbc012ae81a8cf41e084a567ee86536db967970fe85514ee03f963b3bc3
V4PK1_SOURCE_SHA256=bef6fdb02c15299a07b2010fcce1664cc98e0888f97536c4d0d4298acca05bcb
V4PK2_AUDIT_SOURCE_SHA256=1440f75e3f72c8ab32506500c30ac0b5966665ea331b8441186cec0cc8b8b549
V4PK2_ADMITTED_BUNDLE_SHA256=4c0fa5b8f4af9055a8e456a47a8ea9309a2911bb18a8757dc2e03ad3c41612c6
```

## V4-PK2 boundary audit

Exact admitted V4-PK2 source reads these values as runtime inputs:

```text
stance.txt
weight_bp.txt
uncertainty_bp.txt
```

Its native `stance_valid()` accepts `SUPPORT`, `COUNTER`, and `NEUTRAL`; V4-PK2 validates, persists, and aggregates supplied stance/weight/uncertainty values. It does not derive them from external content in the admitted V1 contract.

Therefore V5-K7 does not write a V4-PK2 evidence-evaluation record merely because external bytes were retrieved.

```text
V4PK2_ACTIVE_PATH=NO
V4PK2_ACTIVE_PATH_INVOCATIONS_PLANNED=0
```

## V5-K7 native graph mapping

V5-K7 creates a structural provenance hyperedge:

```text
RELATION=EXTERNAL_RETRIEVAL_PROVENANCE
WEIGHT_BP=0
UNCERTAINTY_BP=10000
RETRIEVAL_GRAPH_STORAGE_MODE=ZERO_INFLUENCE_MAX_UNCERTAINTY
```

Members bind:
1. source family + edition;
2. resource identity + title;
3. source version + source timestamp;
4. exact payload SHA256.

The hyperedge also contains deterministic evidence and provenance identifiers derived by V5-K7 native code from the exact V5-K6 event.

This stage stores retrieved material with zero graph influence and maximum uncertainty. Content evaluation and stance/weight derivation remain outside this admission.

## Host boundary

```text
HOST_RELATION_SELECTION=NO
HOST_WEIGHT_SELECTION=NO
HOST_UNCERTAINTY_SELECTION=NO
HOST_EVIDENCE_STANCE_SELECTION=NO
HOST_TRUTH_DECISION=NO
HOST_EXACT_NATIVE_EVENT_DISPATCH=MECHANICAL_ONLY
```

Bash is limited to compiler/VM invocation, exact protocol decode/copy, hashing, randomized test fixtures, exact test-prestate snapshot/restore, and post-VM oracle checks.

## Planned admission

```text
TOTAL_VM_INVOCATIONS=20
V5K6_CANONICAL_REPLAY_VM_INVOCATIONS=1
V5K7_VM_INVOCATIONS=11
V4PK1_VM_INVOCATIONS=8
V4PK2_ACTIVE_PATH_INVOCATIONS=0
POST_VM_ALIGNMENT_PASS_COUNT=19
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
```

Coverage includes canonical binding, idempotency, materially different dynamic provenance, persistent graph reuse across fresh VM processes, malformed source event refusal, transport hold, non-exact-binding hold, edge-ID conflict refusal, malformed graph refusal, exact test-prestate restore, identical replay, token-leak audits, and step-limit audit.

## Static QA

```text
BASH_SYNTAX_QA=PASS
V5K6_SOURCE_IDENTITY_QA=PASS
V4PK1_SOURCE_IDENTITY_QA=PASS
V4PK2_AUDIT_SOURCE_IDENTITY_QA=PASS
V5K7_NATIVE_SOURCE_CANONICAL_RESOURCE_TOKEN_COUNT=0
V5K7_NATIVE_SOURCE_CANONICAL_PAYLOAD_TOKEN_COUNT=0
V5K7_NATIVE_SOURCE_SUPPORT_TOKEN_COUNT=0
V5K7_NATIVE_SOURCE_COUNTER_TOKEN_COUNT=0
TERMINAL_NOT_PROVEN_LINE_COUNT=0
```

## Runtime status

```text
V5K7_SOURCE_READY=YES
V5K7_RUNTIME_ADMISSION=PENDING_OPERATOR_LOCKED_VM_RUN
```

On machine PASS, the next capability is native evaluation of the graphed external retrieval before V4-PK2 is allowed onto the active chain.