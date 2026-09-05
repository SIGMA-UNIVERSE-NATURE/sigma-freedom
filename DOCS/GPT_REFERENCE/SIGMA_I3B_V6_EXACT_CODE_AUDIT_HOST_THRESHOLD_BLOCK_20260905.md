# SIGMA I3B — V6 exact-code audit: host threshold policy blocks direct reuse

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: EXACT_CODE_AUDIT_COMPLETE / DIRECT_V6_REUSE_BLOCKED_PENDING_NATIVE_POLICY_REPAIR

## Scope

Exact OPPO-exported V6 code archive was received and verified:

```text
EXPORT_ARCHIVE_SHA256=7fc77a89e0ffcfea1e8c39611744b1f4878ea08d256d9d3fd7ed808891bb2645
```

All exported code identities match the machine-observed canonical values:

```text
V6_SOURCE_SHA256=a3eb8c80d412be1c24b124374f12146753369c6a88d5a955c9b7927399514d76
V6_BUILD_VIEW_SHA256=8ebd9d22b7b6f649d77f8cbf056f2d2eb2df03b7ef7fc7d2b03f40022322d66e
V6_RUNNER_SHA256=f5e2c9415a2ada5b8cea32f5b8f9bb8e514464886f9c5444547faed6713e71d1
V6_VERIFY_SHA256=876c7ea2c0ace84eabcf6199a64ab44594fc0aff623bb16e26f529371b0f0cb9
V6_WRAPPER_SHA256=d39b7fe9f2d3e05a3da0ecbd6bedbd535eb8e688a841b3f7ee07b1253178c8da
V6_RUNTIME_VERIFY_SHA256=1ded21c620c6aef9e130a8c59d35e3c18b961d30dbf5d38db37ccdc6f87b36c9
```

## Exact code audit findings

### 1. Python corpus-view builder — mechanical-only in inspected code

`20_BUILD_CORPUS_VIEW_V6.py`:

- validates manifest/index field counts and SHA/path shapes;
- binds lesson index rows to manifest rows by `unique_index`;
- uses `first_evidence.setdefault(unique_index, ...)` only to retain the first already-recorded structural provenance tuple for that exact index;
- verifies lesson SHA binding;
- sorts by numeric `unique_index` deterministically;
- writes `(index, query, url, lesson_path, lesson_sha)` rows;
- DOES NOT read lesson content;
- DOES NOT calculate topic overlap;
- DOES NOT calculate relevance/truth;
- DOES NOT rank semantic candidates;
- DOES NOT choose an assessment state.

Classification:

```text
PYTHON_BUILD_VIEW_ROLE=MECHANICAL_STRUCTURAL_VIEW_BUILDING_ONLY_IN_INSPECTED_CODE
PYTHON_COGNITION=NO_IN_INSPECTED_CODE
HOST_SEMANTIC_EVIDENCE_SELECTION=NO_IN_INSPECTED_CODE
```

### 2. Native V6 assessor owns content reading and state calculation

`15_SIGMA_CORPUS_EVIDENCE_ASSESSOR_V6.sigma` natively:

- reads the topic;
- reads lesson content;
- computes script compatibility;
- computes unique topic-token overlap;
- counts compatible lessons;
- counts distinct compatible source URLs;
- emits one of:
  - `UNKNOWN`
  - `INSUFFICIENT`
  - `MORE_EVIDENCE`
  - `COLLECTION_ENOUGH_FOR_NEXT_STAGE`.

The semantic/structural assessment computation itself is native SIGMA.

### 3. Direct V6 reuse is blocked by host-authored threshold policy

The canonical Bash runner `25_RUN_SIGMA_NATIVE_EVIDENCE_ASSESSOR_V6.sh` writes:

```text
min.compatible.lessons=2
min.distinct.sources=2
min.topic.token.overlap=2
```

and feeds those files into the native assessor.

Those values directly influence whether a lesson is compatible and whether the resulting state is `MORE_EVIDENCE` versus `COLLECTION_ENOUGH_FOR_NEXT_STAGE`.

Under the repository-wide exclusive SIGMA cognition / anti-hardcode lock, this means the existing V6 runtime path is not acceptable as the final I3B autonomous-assessment path because host/Bash supplies material assessment policy parameters.

```text
DIRECT_V6_REUSE_FOR_I3B=BLOCKED_PENDING_NATIVE_POLICY_OWNERSHIP
V6_HISTORICAL_PASS_REVOKED=NO
V6_HISTORICAL_PASS_SCOPE_PRESERVED=YES
NEW_EXCLUSIVE_SELF_LEARNING_GATE_SUPERSEDES_DIRECT_REUSE=YES
```

This does NOT mean the historical V6 result was fake. It means the stronger current governance standard requires moving the policy ownership into native SIGMA before reuse in the closed autonomous chain.

### 4. Independent verifier is post-VM oracle only

`30_VERIFY_SIGMA_NATIVE_EVIDENCE_ASSESSOR_V6.sh` recomputes consistency between:

- SIGMA-emitted metrics;
- the configured thresholds;
- SIGMA-emitted assessment state.

It does not feed a state back into SIGMA or alter the native output.

Classification:

```text
VERIFY_ROLE=POST_VM_ORACLE_ONLY_IN_INSPECTED_CODE
VERIFY_WRITES_SIGMA_SEMANTIC_STATE=NO
VERIFY_FEEDS_RUNTIME_DECISION=NO
```

## Required repair

Do not remove the existing V6 capability. Preserve it as historical/admitted bounded evidence.

For I3B, create an additive native successor (`V6R1` or equivalent) where the assessment-policy ownership is native SIGMA rather than Bash.

The smallest repair is:

1. preserve the exact mechanical Python corpus-view builder;
2. preserve the existing native content-reading/overlap/source-count logic;
3. remove Bash-authored runtime threshold files from the active cognitive path;
4. place the bounded assessment policy inside native SIGMA execution;
5. explicitly mark the static policy as a teacher-authored native capability scaffold, not a learned general policy;
6. dynamically test all state branches and counterexamples;
7. bind I3A `ASSESS_FRESH_EVIDENCE` event to this repaired native assessment path mechanically;
8. do not let host choose or rewrite the assessment state.

## Claim boundaries

```text
I3A_NATIVE_ADMISSION_V1=PASS_IN_EXACT_TESTED_SCOPE
I3B_RUNTIME_ADMISSION=NOT_RUN
V6R1_NATIVE_POLICY_OWNERSHIP=NOT_YET_PROVEN
STATIC_EVIDENCE_THRESHOLD_POLICY_LEARNED=NOT_PROVEN
GENERAL_RESEARCH_POLICY_LEARNED=NOT_PROVEN
SEMANTIC_UNDERSTANDING=NOT_PROVEN
CLOSED_AUTONOMOUS_NATURAL_LANGUAGE_WEB_LEARNING_LOOP=NOT_PROVEN
HOST_SEMANTIC_SUBSTITUTION=NO_ALLOWED_PATH
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
```
