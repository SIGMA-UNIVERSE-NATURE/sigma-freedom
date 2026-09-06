# V5-K8A Native External Evidence Content Assessment — Source Ready

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: `SOURCE_READY / RUNTIME_ADMISSION_NOT_RUN`

## Dependency frontier

V5-K7 has machine PASS in the exact tested scope:

```text
V5K7_NATIVE_EXTERNAL_EVIDENCE_GRAPH_INTEGRATION_V1=PASS
EXTERNAL_RETRIEVAL_TO_PERSISTENT_GRAPH=PASS_IN_EXACT_TESTED_SCOPE
RESULT=PASS_IN_EXACT_TESTED_SCOPE
V4PK2_ACTIVE_PATH=NO
RETRIEVAL_GRAPH_STORAGE_MODE=ZERO_INFLUENCE_MAX_UNCERTAINTY
```

Machine PASS checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/20260906_V5K7_NATIVE_EXTERNAL_EVIDENCE_GRAPH_INTEGRATION_PASS.md`

Machine sample:
`SIGMA_PROFESSOR/artifacts/SAMPLES/V5K7_USER_SUPPLIED_MACHINE_PASS_SUMMARY_20260906.txt`

## Capability contract

```text
CAPABILITY_ID=V5K8A
CAPABILITY_NAME=NATIVE_EXTERNAL_EVIDENCE_CONTENT_ASSESSMENT_FOR_GRAPHED_RETRIEVAL
TEACHING_GOAL=SIGMA_NATIVE_VM_READS_EXACT_RETRIEVED_CONTENT_AND_EMITS_BOUNDED_ASSESSMENT_STATE_FROM_RUNTIME_EVIDENCE
```

Exact active chain under test:

```text
V5K7 graphed retrieval record
+ exact I5C/V5K2 raw payload bytes
+ exact native research-topic bytes
-> exact JSON protocol decode only
-> admitted native V6R1 content assessor
-> native V6R1 assessment state
-> native V5K8A persistent graph-evaluation binder
```

V5K8A does not derive or emit evidence stance, evidence weight, evidence uncertainty, truth, knowledge promotion, or understanding state.

## Reused admitted native assessor

Exact admitted source:
`SIGMA_I3B_NATIVE_CORPUS_EVIDENCE_ASSESSOR_V6R1.sigma`

```text
V6R1_SOURCE_SHA256=c2c34f0df600910fa4ccfa7deb8344ab83a61b86bfeaf369bafced4ad7b73938
V6R1_STATE_VOCABULARY=UNKNOWN|INSUFFICIENT|MORE_EVIDENCE|COLLECTION_ENOUGH_FOR_NEXT_STAGE
V6R1_ASSESSMENT_POLICY_OWNER=SIGMA_NATIVE_V6R1
```

V6R1 is reused only inside its bounded content/collection evidence-assessment semantics. Collection sufficiency is not reinterpreted as truth or support/counter stance.

## Single-resource binding boundary

The V5K8A binder accepts only:

```text
INSUFFICIENT
MORE_EVIDENCE
```

It refuses `COLLECTION_ENOUGH_FOR_NEXT_STAGE` at the single-resource binder. This prevents a multi-source collection state from being silently widened into a single-resource semantic/evidence judgment.

`UNKNOWN` is also not persisted as a successful single-resource evaluation; missing/unreadable canonical payload is a harness HOLD before assessment.

## V4-PK2 boundary

Exact admitted V4-PK2 source is included audit-only:

```text
V4PK2_AUDIT_SOURCE_SHA256=1440f75e3f72c8ab32506500c30ac0b5966665ea331b8441186cec0cc8b8b549
V4PK2_ACTIVE_PATH=NO
V4PK2_ACTIVE_PATH_INVOCATIONS_PLANNED=0
```

V4-PK2 receives stance/weight/uncertainty as runtime inputs; it does not derive them from content. Therefore it remains outside the active V5K8A chain.

## Source-ready artifact identities

```text
BUNDLE_NAME=SIGMA_V5K8A_NATIVE_ADMISSION_V1_EXTERNAL_EVIDENCE_CONTENT_ASSESSMENT_BUNDLE.zip
BUNDLE_SHA256=2c1102554303be3ee410943b9c60c3d24367cde78cb8efb9ed56e03a38973463
V5K8A_SOURCE_SHA256=dcb02dcd7b22986aec2ebf092129ae142f16a1c7df4717634934f0e9a14ce56e
V5K8A_RUNNER_SHA256=6396d094bb3ab72cf07e84e052a0af73b307d8024437bd6e62b7ae2411625e42
V6R1_SOURCE_SHA256=c2c34f0df600910fa4ccfa7deb8344ab83a61b86bfeaf369bafced4ad7b73938
V4PK2_AUDIT_SOURCE_SHA256=1440f75e3f72c8ab32506500c30ac0b5966665ea331b8441186cec0cc8b8b549
```

Locked runtime identities remain:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Canonical byte-binding plan

The runner obtains the canonical V5-K7 graph edge from the machine-PASS artifact, mechanically derives its `RUN_ID`, and binds that ID to the already native-produced topic file:

```text
$HOME/SIGMA/sigma_genesis1/.sigma_exec/HH_AUTO_INTERNET_LESSONS/runs/<RUN_ID>/raw_topic.txt
```

The raw Wikipedia payload is taken from the already-admitted I5C/V5-K2 isolated runtime. Its SHA256 must equal the payload SHA256 stored in the V5-K7 graph record.

Host `jq` is used only for exact structural JSON protocol decode of:

```text
query.pages[0].pageid
query.pages[0].title
query.pages[0].extract
```

The host does not summarize, rank, classify, semantically filter, or score the extracted content.

## Planned admission matrix

```text
TOTAL_VM_INVOCATIONS=19
V6R1_VM_INVOCATIONS=8
V5K8A_VM_INVOCATIONS=11
V4PK2_ACTIVE_PATH_INVOCATIONS=0
```

Coverage includes:

- canonical real V5-K7 graphed Wikipedia retrieval;
- raw-payload SHA256 to graph binding;
- exact JSON extract decode;
- native V6R1 read of the exact decoded content;
- native persistent V5K8A evaluation binding;
- fresh-VM idempotency;
- materially different high-entropy content;
- counterfactual content change causing native assessment-state change;
- script mismatch;
- malformed graph refusal;
- refusal to bind multi-source `COLLECTION_ENOUGH_FOR_NEXT_STAGE` as a single-resource state;
- malformed evaluation-store refusal;
- evaluation-ID conflict refusal;
- exact-prestate replay;
- source/bytecode token-leak audit;
- step-limit scan;
- read-only verification of V5-K7 graph, I5C payload, and native topic bytes.

## Host-substitution boundary

```text
HOST_CONTENT_SEMANTIC_INTERPRETATION=NO
HOST_EVIDENCE_SELECTION=NO
HOST_EVIDENCE_SCORING=NO
HOST_EVIDENCE_STANCE_SELECTION=NO
HOST_WEIGHT_SELECTION=NO
HOST_UNCERTAINTY_SELECTION=NO
HOST_TRUTH_DECISION=NO
HOST_KNOWLEDGE_PROMOTION=NO
V4PK2_ACTIVE_PATH=NO
```

## Runtime proof state

```text
V5K8A_SOURCE_READY=YES
V5K8A_LOCKED_SIGMAC_COMPILE=NOT_RUN
V5K8A_BYTECODE_SHA256=UNKNOWN
V5K8A_RUNTIME_ADMISSION=NOT_RUN
```

## Exact next action

Run the source-ready bundle on the locked Termux SIGMAC/VM and preserve the first HOLD/FAIL or final `V5K8A ADMISSION SUMMARY` exactly.

On machine PASS only, the next frontier becomes:

```text
NATIVE_EVIDENCE_STANCE_WEIGHT_UNCERTAINTY_DERIVATION_BEFORE_V4PK2
```
