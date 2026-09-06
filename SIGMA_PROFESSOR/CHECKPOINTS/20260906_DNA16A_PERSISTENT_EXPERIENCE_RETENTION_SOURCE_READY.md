# SIGMA DNA16A — Persistent Experience Retention Ledger — SOURCE READY

Date: 2026-09-06
Branch: `SIGMA_LIFE`
Status: `SOURCE_READY_RUNTIME_NOT_RUN`

## Teaching goal

Create the first persistent native experience-memory primitive required for SIGMA to continue learning work across separate VM invocations/restarts without a human manually curating which experiences enter retained learning state.

Canon DNA-16 learning unit:

```text
observation + hypothesis + action + outcome + verification
```

Only complete experience with an independent verified verification event is eligible for retention.

## Exact artifact identities

```text
BUNDLE=SIGMA_DNA16A_NATIVE_ADMISSION_V1_FIX2_PERSISTENT_EXPERIENCE_RETENTION_LEDGER_BUNDLE.zip
BUNDLE_SHA256=e322e1e3f9106be4484b9a11e5be3e5ed6bb5f0e4dbab8b07e22514c3b184af5
DNA16A_SOURCE_SHA256=cbf32856c3d7bcad86c52ecaa03d2e3a35de0090eb05a854dca9be226fc810d4
DNA16A_RUNNER_SHA256=d34f058be586da93a4013d2aad069415e75714923041755becbbc6380c8156a3
MANIFEST_SHA256=2f7e937cf124b229654d36747da56bf7f574cad0378446c2aaadbd29575d3265
BASH_SYNTAX_QA=PASS
```

The exact native source is retained in repository at:

`SIGMA_PROFESSOR/artifacts/SOURCES/DNA16A_PERSISTENT_EXPERIENCE_RETENTION_NATIVE_V1.sigma`

Source-retention commit:

`c1314748f5b430a9870fbe97423069f767d94417`

Contract-retention commit:

`8c2d46725a8f98b61b03509938e9e01b29e99952`

## Exact DNA-12 dependency

User supplied exact previously admitted DNA-12 bundle.

```text
DNA12_BUNDLE_SHA256=a010a4671c9f110f1780f43c1b8674243dddadbcd3762f734463e306beaa873a
DNA12_SOURCE_SHA256=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
DNA12_ORIGINAL_RUNNER_SHA256=1ccd798333134e1b2e3486dd33ef6a2ffa9d44bf563446484bf790a3a73fea1a
DNA12_ADMITTED_BYTECODE_SHA256=7dc7cceab5442938a0846c811e98e8c367ab6beedfdefc7c281355f305f7fe70
```

DNA16A admission recompiles that exact DNA-12 source with the locked SIGMAC and requires reproduction of the admitted bytecode identity.

A dynamic DNA-12 runtime case supplies tool output while the caller claims `VERIFIED`. DNA-12 must still classify it as `UNVERIFIED_TOOL_OUTPUT`; DNA16A then must refuse retention of that exact classification.

## DNA-15 admitted contract dependency

```text
DNA15_SOURCE_SHA256=e0ac36559b85a189152709238e176a99e48f325f3f1308aba8b360a768e74d8f
DNA15_BYTECODE_SHA256=f81f4542d2813f69ef308bf54dff3cc0528227ea4d5100d08683d13b1b0b2028
DNA15_PASS_CHECKPOINT=61118bcf4bffb1d34a93f9a969589c6a49cae5de
DNA15_STATE_COMMIT=27661464434bbebb8f3a843572492c2d278b068c
K_SCOPE=INTERVAL_DERIVED_K
```

DNA16A supports retaining an experience whose provenance points to the exact admitted DNA-15 source identity only when the same independent-verification gate passes. DNA-15 source identity alone never bypasses verification.

Exact DNA-15 source bytes are not included in this bundle, so this is a provenance/contract binding rather than a direct DNA-15 runtime replay.

## Native ledger

Header:

```text
STATE||SIGMA_DNA16A_PERSISTENT_EXPERIENCE_LEDGER_V1||COMMIT||YES
```

Record:

```text
EXPERIENCE||EXPERIENCE_ID||OBSERVATION_SHA256||HYPOTHESIS_SHA256||ACTION_SHA256||OUTCOME_SHA256||VERIFICATION_EVENT_SHA256||VERIFICATION_STATUS||EVIDENCE_CLASS||SOURCE_CAPABILITY_ID||SOURCE_CAPABILITY_SHA256||PROVENANCE_ID||LEARNER_ID||VERIFIER_ID||VERIFIER_INDEPENDENT||COMMIT||YES
```

Capacity is bounded at 64 retained records.

## Retention invariants

A new experience is retained only when:

- all five learning-unit component references are present and hash-valid;
- verification status is `VERIFIED`;
- verifier independence is `1`;
- learner ID and verifier ID differ;
- evidence class is not `UNVERIFIED_TOOL_OUTPUT`;
- ledger is structurally valid;
- capacity remains available;
- experience ID does not conflict with an existing different record.

Persisted records are revalidated under the same invariants. Dirty prestate containing unverified retained evidence or duplicate experience IDs is refused.

## Planned locked-VM admission

```text
TOTAL_VM_INVOCATIONS=20
DNA16A_VM_INVOCATIONS=19
DNA12_INTEGRATION_VM_INVOCATIONS=1
```

Planned gates include:

- qualified experience retention;
- fresh-VM persistent reuse;
- idempotency;
- DNA-15 source-provenance structural retention;
- dynamic experience change;
- failed-verification non-retention;
- direct unverified-evidence non-retention;
- exact native DNA-12 `UNVERIFIED_TOOL_OUTPUT` contamination block;
- independent verifier gate;
- incomplete learning-unit refusal;
- malformed ledger exact-prestate preservation;
- preseeded unverified ledger refusal;
- preseeded duplicate-ID ledger refusal;
- experience-ID conflict refusal;
- bounded capacity 64 without silent eviction;
- invalid hash/status refusal;
- identical-prestate replay;
- dynamic high-entropy anti-hardcode audit;
- step-limit audit;
- source/bytecode immutability audit.

## Ownership boundary

```text
HOST_LEARNING=NO
HOST_HYPOTHESIS_GENERATION=NO
HOST_ACTION_SELECTION=NO
HOST_VERIFICATION_DECISION=NO
KNOWLEDGE_PROMOTION_EXECUTED=NO
```

DNA16A does not invent an observation, hypothesis, action, outcome, or verifier decision. It is a persistent native retention gate and learning-memory primitive.

## Next capability after machine admission

`DNA16B_NATIVE_VERIFIER_EVENT_BINDING_AND_EXPERIENCE_EVALUATION`

Parallel support-axis dependency remains exact native DNA-12 runtime binding into `TW3A -> TW2 -> TW1`, so that future autonomous execution can connect native tool-demand decisions to actual weighted tool selection.
