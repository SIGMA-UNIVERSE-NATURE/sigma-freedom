# I3B — V6 Code Export + Host-Substitution Static Audit — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: SOURCE_READY_CODE_REVIEW_GATE_ONLY

## Upstream

```text
I3A_NATIVE_ADMISSION_V1=PASS
POST_FOLLOWUP_OUTCOME_GATE_TESTED_SCOPE=PASS
I3B_FRESH_EVIDENCE_ASSESSMENT_DISPATCH_UNLOCKED_BY_I3A=YES
```

Dependency machine witness:

`DOCS/GPT_REFERENCE/SAMPLES/I3B_V6_DEPENDENCY_AUDIT_MACHINE_WITNESS_20260905.txt`

Witness commit:

`be02fb289ea39f27b74d1dc46cd08bdfb7d7421b`

## Recovered exact V6 dependency identities

```text
V6_NATIVE_SOURCE=V1_R9_SIGMA_NATIVE_CORPUS_EVIDENCE_ASSESSOR/15_SIGMA_CORPUS_EVIDENCE_ASSESSOR_V6.sigma
V6_NATIVE_SOURCE_SHA256=a3eb8c80d412be1c24b124374f12146753369c6a88d5a955c9b7927399514d76

V6_BUILD_CORPUS_VIEW=V1_R9_SIGMA_NATIVE_CORPUS_EVIDENCE_ASSESSOR/20_BUILD_CORPUS_VIEW_V6.py
V6_BUILD_CORPUS_VIEW_SHA256=8ebd9d22b7b6f649d77f8cbf056f2d2eb2df03b7ef7fc7d2b03f40022322d66e

V6_RUNNER=V1_R9_SIGMA_NATIVE_CORPUS_EVIDENCE_ASSESSOR/25_RUN_SIGMA_NATIVE_EVIDENCE_ASSESSOR_V6.sh
V6_RUNNER_SHA256=f5e2c9415a2ada5b8cea32f5b8f9bb8e514464886f9c5444547faed6713e71d1

V6_VERIFY=V1_R9_SIGMA_NATIVE_CORPUS_EVIDENCE_ASSESSOR/30_VERIFY_SIGMA_NATIVE_EVIDENCE_ASSESSOR_V6.sh
V6_VERIFY_SHA256=876c7ea2c0ace84eabcf6199a64ab44594fc0aff623bb16e26f529371b0f0cb9

V6_WRAPPER=V1_R9_SIGMA_NATIVE_CORPUS_EVIDENCE_ASSESSOR/99_RUN_SIGMA_NATIVE_EVIDENCE_ASSESSMENT_V6.sh
V6_WRAPPER_SHA256=d39b7fe9f2d3e05a3da0ecbd6bedbd535eb8e688a841b3f7ee07b1253178c8da
```

## Why a code-review gate is required

The repository-wide directive `SIGMA_EXCLUSIVE_SELF_LEARNING_UNDERSTANDING_AND_ANTI_HARDCODE_LOCK_V1.md` forbids Python/host cognition, semantic evidence selection, ranking, topic classification, truth decisions, understanding classification, and next-action substitution.

The historical V6 package contains `20_BUILD_CORPUS_VIEW_V6.py`. Its existence alone does not prove a violation, because Python may still be a purely mechanical view builder. But it MUST be inspected before I3B may reuse V6 under the new lock.

Do not infer safety from the filename or from the historical PASS.

## User artifact

```text
BUNDLE_NAME=SIGMA_I3B_V6_DEPENDENCY_EXPORT_AND_STATIC_AUDIT_V1_BUNDLE.zip
BUNDLE_SHA256=b0cc9d5a34bfd5ea5fc096c5a36dc043a0d9623d621e74bc35dd80413870feab
RUNNER_SHA256=7a6e6b784a12546c82d27a65a5713db5a38074f30601b9d2b89e33713a2444b5
```

The artifact verifies the exact known hashes, copies only V6 code/runtime-tool files, performs a mechanical static marker inventory, and produces a small code-only archive:

`SIGMA_I3B_V6_DEPENDENCY_EXPORT.tar.gz`

It does NOT:

```text
SIGMA_VM_EXECUTED=NO
LIVE_INTERNET_REQUEST_EXECUTED=NO
SEMANTIC_ASSESSMENT_EXECUTED=NO
LESSON_CONTENT_READ_BY_AUDIT=NO
QUERY_TOPIC_SOURCE_PAYLOAD_CONTENT_READ_BY_AUDIT=NO
HOST_SEMANTIC_CLASSIFICATION=NO
```

## Required next action

Run the exact export/static-audit bundle on OPPO, then provide the generated code-only tar.gz for source review.

Only after reviewing the exact code may the teacher decide one of two mechanical engineering outcomes:

```text
A) V6_VIEW_BUILDER_MECHANICAL_ONLY=PROVEN_BY_CODE_REVIEW
   -> reuse exact V6 assessment capability in I3B

B) V6_VIEW_BUILDER_OR_RUNNER_CONTAINS_HOST_COGNITION=YES
   -> DO_NOT_REUSE_ACTIVE_PATH
   -> refactor the missing preprocessing/selection logic into native SIGMA before I3B admission
```

The teacher must not change V6 assessment outputs to force compatibility with I3B.

## Claim boundary

```text
I3A_NATIVE_POST_FOLLOWUP_OUTCOME_GATE=PASS_IN_EXACT_TESTED_SCOPE
V6_NATIVE_SOURCE_IDENTITY=RECOVERED_FROM_MACHINE
V6_HOST_SUBSTITUTION_AUDIT=NOT_YET_COMPLETE
I3B_NATIVE_FRESH_EVIDENCE_ASSESSMENT_DISPATCH=NOT_YET_PROVEN
POST_FOLLOWUP_OUTCOME_CONDITIONED_CONTINUATION=NOT_YET_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
```
