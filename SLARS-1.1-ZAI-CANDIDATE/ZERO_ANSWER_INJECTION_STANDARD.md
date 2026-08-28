# SLARS-1.1-ZAI — SIGMA Language / Zero Answer Injection

**Classification:** normative candidate module  
**Implementation status:** `PRODUCER_IMPLEMENTED_INDEPENDENT_VERIFICATION_REQUIRED`  
**Implemented profile:** `Z0–Z4_INJECTION_INTEGRITY`  
**Future profiles:** `Z5_OBSERVATION_DEPENDENCE`, `Z6_BLIND_PERFORMANCE`,
`Z7_INDEPENDENT_REPRODUCTION`  
**Current run scope:** one locked blind case, one frozen candidate and one
declared single-attempt sigmac/SIGMA-VM event chain

## 1. Purpose and boundary

SLARS-1.1-ZAI tests a bounded provenance proposition:

> For one identified run, did the registered pre-output artifact surface remain
> free of the registered case-specific answer material, and did the frozen raw
> output bind to the exact bytes labeled sigmac/SIGMA VM and their declared
> event chain before the key was first accessed?

The implemented Z0–Z4 profile validates artifact bytes, declared visibility,
registered forbidden-material scans, event order, declared execution bindings,
mechanical host-operation records and external-evaluation bindings. It does not
establish that every possible semantic or physical side channel was absent.

The aggregate machine claim identifier is deliberately bounded:

```text
NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY
```

The operational gate may still print `ZERO_ANSWER_INJECTION=PASS`; that field
means the bounded Z0–Z4 profile passed. It does not change the machine claim
into an assertion of universal absence. The word `ZERO` is the name of the test
profile and operational gate, not a universal or metaphysical assertion.

This module does not prove understanding, cognition, consciousness, autonomy,
self-development or general reasoning. Z0–Z4 also do not yet prove that changing
the blind observation caused the output to change. That belongs to future Z5.

## 2. Immutable policy locks

The protocol must contain exactly the implemented lock registry:

```text
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN
SUPPORTOR_ANSWERS_FOR_SIGMA=FORBIDDEN
PREWRITTEN_ANSWER=FORBIDDEN
PREWRITTEN_HYPOTHESIS=FORBIDDEN
PREWRITTEN_REASONING_PATH=FORBIDDEN
PREWRITTEN_CONCLUSION=FORBIDDEN
SIGMA_SELF_OBSERVES_AND_ANSWERS=REQUIRED
HOST_SEMANTIC_TRANSFORMATION=FORBIDDEN
OUTPUT_SELECTION_OR_REWRITE=FORBIDDEN
CLAIM_POLICY=CLAIM_LESS_THAN_OR_EQUAL_TO_EVIDENCE
```

`SIGMA_SELF_OBSERVES_AND_ANSWERS=REQUIRED` is a target requirement, not a
self-executing claim. Z0–Z4 establish output origin and the bounded injection
profile only. Operational evidence that the output depends on observations is
deferred to Z5.

Human-language input, source strings and output remain classified by provenance:

```text
HUMAN_LANGUAGE_INPUT=STIMULUS_OR_CONTRACT
SUPPORTOR_AUTHORED_SOURCE=DECLARED_SCAFFOLDING
SIGMA_VM_STDOUT=RAW_BEHAVIORAL_ARTIFACT
EXTERNAL_EVALUATION=POST_OUTPUT_EVIDENCE
```

None of those classifications independently permits
`HUMAN_LANGUAGE_AS_SIGMA_COGNITION=YES`.

## 3. Generic scaffolding versus forbidden injection

Supportor-authored identifiers, generic algorithms, error messages, sentinels,
capability contracts and output field names are permitted only when their
provenance is declared and they were frozen before blind-case commitment. Their
existence is not SIGMA cognition.

| Class | Normative treatment |
| --- | --- |
| Generic mechanism frozen before the blind-case commitment | Allowed as declared Supportor-authored scaffolding |
| Generic output schema such as `answer`, `confidence`, `abstain` | Allowed if it carries no case-specific semantic result |
| Blind test observation | Allowed only through the locked blind-input artifact/channel |
| Authorized lesson in an acquisition exposure phase | Stimulus only; it is not SIGMA cognition and must be absent when the applicable closed-book protocol requires absence |
| Raw mechanical result from a SIGMA-frozen request | Eligible only under a separately locked tool protocol |
| Case-specific answer, hypothesis, reasoning path or conclusion | Forbidden before raw output freeze |
| Case-specific rule, lookup, branch, weight or state derived from the answer key | Forbidden before raw output freeze |
| Evaluator key, semantic review or evaluation report | Forbidden to the candidate and pre-output surface; available only at their ordered post-output events |

A generic algorithm may define parsing, storage, iteration, arithmetic, search,
learning or inference control. A case-specific sequence of intermediate
propositions or a semantic sentence template that already determines the target
conclusion is a prewritten reasoning path or conclusion, not generic scaffolding.

Freezing a source does not by itself prove that the source is generic. A clean
string scan does not prove self-development. A native VM output does not prove
cognition.

## 4. Evidence root and artifact records

Every referenced object must be a regular file inside one sealed evidence root.
The evidence validator rejects absolute paths, path traversal, symlinks,
hardlinks, non-regular files, size-limit violations, duplicate identities and
hash or byte-count mismatches. It reads the referenced bytes and recomputes both
`byte_count` and `sha256`; a declared 64-character string is not evidence.

Every artifact record binds:

```text
artifact_id
relative_path
media_type
semantic_role
origin_role
stage
candidate_visible
pre_output_reachable
byte_count
sha256
```

Required semantic roles are:

```text
CANDIDATE_SOURCE
SIGMAC_BINARY
SIGMA_VM_BINARY
BLIND_INPUT
ANSWER_KEY
EVALUATION_RUBRIC
VISIBILITY_MANIFEST
RUNNER_SOURCE
RUN_SPECIFIC_BYTECODE
HOST_TRACE
RAW_STDOUT
RAW_STDERR
SEMANTIC_REVIEW
EXTERNAL_EVALUATION
CHANNEL_EVIDENCE
```

The locked protocol additionally commits the exact candidate source, compiler,
VM, runner source and evaluation-rubric artifact IDs and SHA-256 values. The
validator enforces one canonical `origin_role`, `stage`, visibility and
pre-output status for every semantic role; those labels remain evidence-bundle
metadata, not external proof of binary provenance. Any change to a committed
artifact requires a new protocol and a new run.

The protocol also bounds per-artifact bytes, total artifact bytes, artifact
count, forbidden-marker count/bytes and the scan-product budget. File reads are
bounded and identity-checked before/after hashing.

## 5. Declared visibility and channel boundary

The visibility manifest must bind the same blind `case_id` as the protocol and
must exactly enumerate:

```text
candidate_visible_artifact_ids
pre_output_reachable_artifact_ids
candidate_forbidden_artifact_ids
channels
undeclared_readable_channels
```

At minimum, `ANSWER_KEY`, `EVALUATION_RUBRIC`, `SEMANTIC_REVIEW` and
`EXTERNAL_EVALUATION` must be in the candidate-forbidden set. No artifact in
the candidate-forbidden set may also be candidate-visible or pre-output
reachable.

The implemented channel registry is exactly:

```text
SOURCE
BYTECODE
STATE
STDIN
ARGV
ENVIRONMENT
FILES
FILENAMES
DIRECTORY_ORDER
HOST_RESULTS
TOOL_MAP
TOOL_RESULTS
NETWORK
CLOCK
RNG
CACHE
STDERR
EXIT_CODE
RESOURCE_LIMIT_SIGNAL
```

Each channel is declared `CAPTURED` or `DISABLED`. Either status must bind one
or more evidence artifacts; the word `DISABLED` is not accepted as proof by
itself. Critical bindings additionally require source, bytecode, stdin, stderr
and exit-code channels to cite their corresponding materialized artifacts.
All remaining channels must cite at least one repeatable `CHANNEL_EVIDENCE` v2
artifact, which is itself materialized, pre-output reachable and included in
the registered scan surface. Every covered channel has its own non-empty UTF-8
self-bound declaration record, status-matched `DECLARED_*` evidence class,
byte count and SHA-256.
Critical source/bytecode/stdin/stderr/exit-code channels must be `CAPTURED` and
bind their actual artifacts. One channel-evidence artifact may carry multiple
mechanically related capture records, but a missing or empty record cannot
cover a channel and duplicate channel records are invalid. The validator does
not judge whether the free-form observation text is semantically adequate.
`undeclared_readable_channels` must be empty.

This is a declared and audited channel boundary. A capture/disablement record
is a self-bound declaration of the audit procedure, not independent proof that
capture happened or that the physical channel was impossible. The current validator verifies
the manifest's internal bindings; it does not independently discover physical
channels or prove that a declared `DISABLED` channel was physically impossible.
That limitation remains inside the claim ceiling.

## 6. Forbidden-material registry and review

The UTF-8 JSON `ANSWER_KEY` contains a non-empty `forbidden_material` registry.
The implemented registry requires at least one distinctive marker for every
class, with unique IDs and text values:

```text
SUPPORTOR_ANSWER
PREWRITTEN_ANSWER
PREWRITTEN_HYPOTHESIS
PREWRITTEN_REASONING_PATH
PREWRITTEN_CONCLUSION
```

Every registered marker and its alphanumeric fingerprint must contain at least
eight UTF-8 bytes. Normalized and alphanumeric fingerprints must be distinct,
so two raw strings cannot silently register the same effective marker. The validator
scans the exact pre-output-reachable artifact set, including artifact ID, path
and media-type metadata, plus every pre-key event `argv`, using the implemented
representations:

```text
EXACT_UTF8
UNICODE_NFKC_CASEFOLD_WHITESPACE_COLLAPSE
UNICODE_NFKC_ALNUM_COLLAPSE
HEX_LOWER
HEX_UPPER
BASE64_STANDARD
URL_PERCENT
JSON_ESCAPE
ROT13
ASCII_BYTE_CASEFOLD_WHITESPACE_COLLAPSE
ASCII_BYTE_ALNUM_COLLAPSE
URL_PERCENT_DECODE_UP_TO_TWO_LAYERS
JSON_UNICODE_ESCAPE_DECODE_UP_TO_TWO_LAYERS
```

Binary artifacts are always scanned with byte-preserving ASCII modes. Unicode
normalization uses replacement decoding so one invalid UTF-8 byte cannot disable
the normalized scan of all remaining valid text. URL-percent and JSON `\uXXXX`
decoding are explored in a bounded two-layer transformation graph; the declared
scan-product limit covers the maximum seven materialized scan surfaces per
artifact with a conservative fixed cost multiplier for all comparison modes.

Machine scanning establishes only that those registered representations were
not found on that materialized surface. It does not detect every encoding,
paraphrase, distributed representation, trained-state contamination or
semantically equivalent algorithm.

An auditor-authored `SEMANTIC_REVIEW` v2 must receive the answer key, frozen raw
stdout and every scan-surface artifact at its event. It binds the same run plus
a canonical list of every reviewed artifact ID/SHA-256 pair and the hash of that
list, then reports all implemented finding fields as false. The validator checks
the review's structure, actor, artifact bytes and declarations; it does not redo
the human semantic judgment. Therefore:

```text
SEMANTIC_REVIEW_BINDING_VALIDATED=YES_IF_Z2_PASS
SEMANTIC_CONTENT_INDEPENDENTLY_REJUDGED_BY_VALIDATOR=NO
```

## 7. Implemented ten-event chain

Every evidence run must contain exactly these ten events in this order:

```text
01 PROTOCOL_FREEZE
02 CANDIDATE_FREEZE
03 BLIND_CASE_COMMIT
04 CHANNEL_SNAPSHOT
05 RUN_START
06 SIGMAC_COMPLETE
07 VM_OUTPUT_FROZEN
08 KEY_FIRST_ACCESS
09 SEMANTIC_REVIEW
10 EXTERNAL_EVALUATION
```

Authorized actor mapping:

| Event | Protocol role |
| --- | --- |
| `PROTOCOL_FREEZE` | `test_designer` |
| `CANDIDATE_FREEZE` | `candidate_builder` |
| `BLIND_CASE_COMMIT` | `test_designer` |
| `CHANNEL_SNAPSHOT` | `auditor` |
| `RUN_START`, `SIGMAC_COMPLETE`, `VM_OUTPUT_FROZEN` | `runner` |
| `KEY_FIRST_ACCESS` | `key_custodian` |
| `SEMANTIC_REVIEW` | `auditor` |
| `EXTERNAL_EVALUATION` | `evaluator` |

All six protocol role identity strings must be distinct. This proves declared
role separation inside the evidence bundle, not real-world organizational
independence or cryptographic personhood.

Each event has a one-based sequence, exact `run_id`, authorized actor, strict
ASCII RFC3339 UTC-Z (maximum six fractional digits), nondecreasing
timestamp, artifact references, optional process artifact, `argv`, `rc`, the
previous event hash and its own event hash. The event hash is SHA-256 of
canonical UTF-8 JSON after removing only `event_sha256`.

Each event also contains `artifact_bindings_sha256`, computed from the canonical
`{direction, artifact_id, sha256, byte_count}` bindings of every input, output
and process artifact. Consequently the hash chain binds referenced bytes, not
only artifact names. This is still not a signature, trusted timestamp or live
attestation; a separate authenticated witness is required for non-repudiation.

The protocol timestamps and event timestamps must establish:

```text
PROTOCOL_LOCK <= CANDIDATE_FREEZE < BLIND_CASE_COMMIT
VM_OUTPUT_FROZEN < KEY_FIRST_ACCESS
KEY_FIRST_ACCESS <= SEMANTIC_REVIEW <= EXTERNAL_EVALUATION
```

Required event-output and process bindings include the evaluation rubric at
protocol freeze, candidate source at candidate freeze, blind input and answer
key at commit, visibility manifest and all channel-evidence artifacts at snapshot,
run-specific bytecode from the exact compiler event, raw stdout/stderr and host
trace at VM-output freeze, and the post-output review/evaluation artifacts.

Pre-key `argv` is canonical and exact: protocol/freeze/commit/snapshot/run-start
events use an empty list, the compiler event uses exactly source path then
bytecode path, and the VM event uses exactly the bytecode path. Extra options,
including decorated secret paths such as `--key=...`, invalidate the run.

## 8. Implemented Z0–Z4 injection-integrity profile

### Z0 — Locked SIGMA source and provenance surface

```text
Z0_PASS =
    LOCKED_PROTOCOL_AND_COMPLETE_RUN
    AND PROTOCOL_BYTES_HASH_MATCH
    AND ALL_REQUIRED_ARTIFACT_BYTES_MATERIALIZED
    AND EXACT_POLICY_LOCK_REGISTRY_MATCH
    AND SIX_DECLARED_ROLE_IDENTITIES_ARE_DISTINCT
    AND REQUESTED_CLAIMS_ARE_CANONICAL
    AND SOURCE_COMPILER_VM_RUNNER_COMMITMENTS_MATCH
    AND CANDIDATE_SOURCE_IS_STRICT_UTF8
    AND CANDIDATE_SOURCE_STARTS_WITH_REQUIRED_SIGMA_HEADER_PREFIX
```

Z0 binds an identified source and its declared SIGMA-language surface. Header
recognition alone is not full grammar proof; exact compiler acceptance is
observed later in Z3. Z0 does not prove that human-language content in the source
was generated or understood by SIGMA.

### Z1 — Freeze, visibility and event-boundary integrity

```text
Z1_PASS =
    Z0_PASS
    AND COMMITTED_ARTIFACT_IDENTITIES_MATCH
    AND VISIBILITY_MANIFEST_BINDINGS_MATCH
    AND REQUIRED_FORBIDDEN_ARTIFACTS_ARE_UNREACHABLE_PREOUTPUT
    AND REQUIRED_CHANNEL_REGISTRY_IS_COMPLETE
    AND UNDECLARED_READABLE_CHANNELS == []
    AND EXACT_TEN_EVENT_CHAIN_VALID
    AND LOCK_FREEZE_COMMIT_ORDER_VALID
```

The implementation is fail-closed: Z1 depends on the integrity of the entire
event chain, while specialized compiler/VM and output/key/evaluation errors are
also reported under Z3 or Z4.

For every required event, the declared `inputs`, `outputs`, `process`, `argv`
and `rc` form an exact topology, not a minimum subset. An extra reference is an
integrity failure even when every required reference is also present. This
prevents post-output or post-key artifacts from being smuggled into an earlier
execution event under an otherwise valid hash chain.

### Z2 — Registered pre-output injection scan

```text
Z2_PASS =
    Z1_PASS
    AND ANSWER_KEY_AND_CASE_BINDINGS_VALID
    AND ALL_FIVE_FORBIDDEN_CLASSES_REGISTERED
    AND REPORTED_SCAN_SURFACE_EQUALS_DECLARED_PREOUTPUT_SURFACE
    AND ALL_IMPLEMENTED_MACHINE_SCAN_MODES_HAVE_ZERO_MATCHES
    AND SEMANTIC_REVIEW_ARTIFACT_AND_ACTOR_BINDINGS_VALID
    AND SEMANTIC_REVIEW_STATUS == PASS
    AND ALL_SEMANTIC_REVIEW_FINDINGS == FALSE
```

Under the implemented fail-closed evidence profile, a registered match,
semantic injection finding or unknown readable-channel finding makes Z2 and the
overall run `INVALID`.

### Z3 — Declared toolchain event chain and raw-output binding

Canonical execution boundary:

```text
LOCKED_SIGMA_SOURCE
  -- bytes labeled sigmac + exact event -->
RUN_SPECIFIC_BYTECODE
  -- bytes labeled SIGMA VM + exact event -->
RAW_STDOUT + RAW_STDERR + RC
```

```text
Z3_PASS =
    Z1_PASS
    AND SIGMAC_EVENT_PROCESS_ARGV_AND_RC_BINDINGS_PASS
    AND VM_EVENT_PROCESS_ARGV_AND_RC_BINDINGS_PASS
    AND SIGMAC_RC == 0
    AND VM_RC == 0
    AND ATTEMPT_COUNT == 1
    AND RAW_STDOUT_ORIGIN_ROLE == SIGMA_VM
    AND CANDIDATE_OUTPUT_IS_RAW_VM_STDOUT
    AND HOST_TRACE_USES_MECHANICAL_ALLOWLIST_ONLY
    AND HOST_SEMANTIC_TRANSFORMATION_OBSERVED == FALSE
    AND OUTPUT_SELECTION_OR_REWRITE_OBSERVED == FALSE
```

The implemented host-operation allowlist is:

```text
HASH_BYTES
EXEC_SIGMAC
EXEC_SIGMA_VM
CAPTURE_STDOUT
CAPTURE_STDERR
FREEZE_BYTES
```

The host trace must contain exactly one `EXEC_SIGMAC`, `EXEC_SIGMA_VM`,
`CAPTURE_STDOUT`, `CAPTURE_STDERR` and `FREEZE_BYTES` in native-chain order.
`HASH_BYTES` may appear as additional mechanical integrity telemetry.

The validator also binds the required input/output topology of those operations,
rejects any host-trace reference to the answer key, rubric, semantic review or
external evaluation, and does not permit generic host read/write operations in
this implemented runner profile. SIGMA VM runtime operations are a different
boundary and are not reclassified as runner cognition.

Z3 establishes the declared event-chain binding for raw output in the identified run. It does
not establish that the blind observation causally controlled that output; a
candidate that always prints one fixed value can still satisfy Z3. It also does
not establish that the hash-bound binary bytes are an approved native build;
that requires an external build registry, signature or attestation.

### Z4 — Post-output key access and evaluation binding

```text
Z4_PASS =
    Z1_PASS
    AND VM_OUTPUT_FROZEN < KEY_FIRST_ACCESS
    AND KEY_FIRST_ACCESS <= SEMANTIC_REVIEW <= EXTERNAL_EVALUATION
    AND EVALUATION_RUBRIC_WAS_COMMITTED_AT_PROTOCOL_FREEZE
    AND EXTERNAL_REPORT_BINDS_RUN_EVALUATOR_RAW_STDOUT_SHA_ANSWER_KEY_SHA_AND_RUBRIC_SHA
    AND RUN_EXTERNAL_RECORD_MATCHES_REPORT
    AND EXTERNAL_STATUS IN {PASS, FAIL}
```

`Z4_PASS` means the external report is conclusive and correctly bound. It does
not require `TASK_OUTCOME=PASS`. A clean, correctly bound but wrong candidate
answer can produce:

```text
Z4=PASS
TASK_OUTCOME=FAIL
```

The validator does not rejudge semantic correctness, rubric quality or the
external evaluator's decision.

## 9. Current acceptance formula

```text
ZAI_Z0_TO_Z4_PROFILE_PASS =
    STRICT_SCHEMA_PASS
    AND RAW_ARTIFACT_MATERIALIZATION_PASS
    AND Z0_PASS
    AND Z1_PASS
    AND Z2_PASS
    AND Z3_PASS
    AND Z4_PASS
    AND REQUESTED_CLAIM_SET_MATCH
    AND REPORTED_STATUS_MATCHES_RECOMPUTATION
    AND VERDICT_RECEIPT_HASHES_EMITTED
```

`TASK_OUTCOME` is orthogonal to this injection-integrity profile. It must always
be reported separately.

## 10. Status semantics and precedence

The implemented status precedence is:

```text
INVALID
> UNVERIFIED
> INSUFFICIENT_EVIDENCE
> FAIL
> PASS
```

Definitions:

```text
PASS
    All predicates required by the reported implemented gate are satisfied.

FAIL
    A valid external evaluation reports that the candidate did not satisfy the
    task criterion. In the current profile this is primarily TASK_OUTCOME, not
    a substitute for ZAI integrity status.

INSUFFICIENT_EVIDENCE
    Structurally valid evidence cannot resolve a preregistered proposition.
    This status is reserved principally for future Z5–Z7 profiles.

UNVERIFIED
    No complete locked evidence run was evaluated, including templates,
    structure-only mode, incomplete runs or producer assertions without the
    required raw evidence.

INVALID
    The run is not admissible for the claimed profile because structure,
    materialized bytes, identity, policy, role, visibility, scan, execution,
    event order, output origin or evaluation binding failed.
```

The current evidence implementation computes the aggregate ZAI result as
`PASS` only when all Z0–Z4 gates and claim dependencies pass; otherwise an
admissibility defect produces `INVALID`. A declared boolean can never promote
missing or contradictory evidence.

## 11. Implemented claim registry and ceilings

Only the verifier owns the canonical claim registry. A protocol may request a
subset but may not add claim identifiers.

```text
SIGMA_SOURCE_LANGUAGE_BOUND_FOR_LOCKED_SOURCE
REGISTERED_PREOUTPUT_INJECTION_SCAN_CLEAN
DECLARED_SIGMAC_SIGMA_VM_EVENT_CHAIN_RAW_STDOUT_BOUND
NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY
```

Exact ceilings:

| Claim identifier | Maximum supported meaning |
| --- | --- |
| `SIGMA_SOURCE_LANGUAGE_BOUND_FOR_LOCKED_SOURCE` | The identified UTF-8 source bytes have the required SIGMA header prefix and locked provenance/identity; not full language semantics or cognition |
| `REGISTERED_PREOUTPUT_INJECTION_SCAN_CLEAN` | No implemented representation of the registered markers was found on the exact materialized scan surface, and the bound semantic review declared no finding |
| `DECLARED_SIGMAC_SIGMA_VM_EVENT_CHAIN_RAW_STDOUT_BOUND` | The raw stdout artifact is bound to the hash-identified bytes labeled sigmac/VM, their exact event topology and the mechanical host trace; native-build identity remains independently unverified |
| `NO_DETECTED_PROHIBITED_ANSWER_INJECTION_WITHIN_DECLARED_MATERIALIZED_BOUNDARY` | All Z0–Z4 predicates passed for the exact protocol, materialized artifacts, declared channels, event chain and run; only absence detected within that declared and materialized boundary |

A positive claim is emitted only when it was requested in the locked protocol,
is present in the run and every dependency gate passed. The operational ZAI
predicate never silently promotes an unrequested claim.

Always forbidden from Z0–Z4 alone:

```text
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=YES
SIGMA_SELF_OBSERVATION_CAUSALLY_PROVEN=YES
SIGMA_COGNITION=PROVEN
SIGMA_UNDERSTANDING=PROVEN
SIGMA_SELF_AWARENESS=PROVEN
SIGMA_SELF_DEVELOPMENT=PROVEN
GENERAL_REASONING=PROVEN
UNIVERSAL_ZERO_ANSWER_INJECTION=PROVEN
```

## 12. Future profiles — specified direction, not implemented evidence

The following gates are outside the current schemas, validator and claim
registry. They must remain `NOT_IMPLEMENTED` and must not be inferred from a
Z0–Z4 PASS.

### Z5 — Observation dependence

Purpose: test whether output changes appropriately with observation or raw
evidence rather than merely originating from the VM.

Minimum future design:

```text
SAME_FROZEN_CANDIDATE_AND_FRESH_INITIAL_STATE
NO_OBSERVATION -> PRELOCKED_ABSTENTION_OR_NO_RESULT_BEHAVIOR
MATCHED_OBSERVATION_A -> Y_A
MATCHED_OBSERVATION_B_REQUIRING_DIFFERENT_RESULT -> Y_B
MATERIAL_EVIDENCE_SWAP -> PRELOCKED_MATERIAL_OUTPUT_CHANGE
IRRELEVANT_EVIDENCE_SWAP -> NO_CONTROLLING_OUTPUT_CHANGE
NO_RETRY_OR_BEST_OUTPUT_SELECTION
```

Maximum future claim:

```text
OUTPUT_DEPENDENCE_ON_OBSERVATION_OR_RAW_EVIDENCE_OBSERVED_WITHIN_TESTED_COUNTERFACTUALS
```

This still does not prove cognition; a deterministic fixed rule may pass.

### Z6 — Blind performance

Purpose: determine whether observation-dependent raw outputs satisfy a
prelocked task criterion across fresh hidden cases.

It requires a prelocked case-family generator, scorer, thresholds, sample size,
missing-output policy and uncertainty method; multiple fresh cases requiring
different results; raw-output freeze before every key access; and an external
evaluator that scores without rewriting candidate output.

Maximum future claim:

```text
BOUNDED_BLIND_TASK_PERFORMANCE_OBSERVED
```

The current single-case `TASK_OUTCOME` is not Z6 evidence.

### Z7 — Independent reproduction

Purpose: reproduce Z0–Z6 on the exact candidate/toolchain identities with a new
hidden assignment, a separate runner/auditor/evaluator and no reuse of consumed
cases or feedback.

Maximum future claim:

```text
INDEPENDENTLY_REPRODUCED_BOUNDED_NO_DETECTED_INJECTION_AND_BLIND_PERFORMANCE_PROFILE
```

Z7 cannot be issued by the candidate producer.

## 13. Required adversarial coverage and known limitations

Independent verification should include at least:

- direct marker injection into source, state, stdin, path, filename and metadata;
- Unicode, whitespace, alphanumeric collapse, hex, Base64, URL, JSON escape and
  ROT13 representations;
- answer material hidden in comments, identifiers, environment, tool ordering,
  RNG, timestamps, exit codes or resource signals;
- host/Python/Bash semantic computation followed by VM echo;
- output replacement, normalization, summarization, retry and best-of selection;
- source-clean but bytecode/dependency-contaminated artifacts;
- answer-aware host operations or tool results mislabeled as mechanical;
- preloaded state/weights, cross-run cache or network contamination;
- key access, reviewer feedback or scorer feedback before output freeze;
- fixed-output candidates and matched cases requiring different results;
- semantic templates, paraphrases or distributed rules not caught by literals.

Known limits of the implemented profile include:

```text
UNREGISTERED_ENCODING_ABSENCE=NOT_PROVEN
PARAPHRASE_ABSENCE_DEPENDS_ON_BOUND_SEMANTIC_REVIEW
PHYSICAL_CHANNEL_DISCOVERY=NOT_PERFORMED_BY_VALIDATOR
PRETRAINING_OR_WEIGHT_CONTAMINATION=NOT_EXCLUDED_BY_STRING_SCAN
REAL_WORLD_ROLE_INDEPENDENCE=NOT_CRYPTOGRAPHICALLY_PROVEN
EVENT_LOG_LIVE_ATTESTATION=NOT_PROVEN_BY_HASH_CHAIN_ALONE
NATIVE_BINARY_BUILD_IDENTITY=NOT_PROVEN_WITHOUT_EXTERNAL_ATTESTATION
EXTERNAL_SCORE_CONTENT_REJUDGED_BY_VALIDATOR=NO
OBSERVATION_DEPENDENCE=NOT_IMPLEMENTED
BLIND_MULTI_CASE_PERFORMANCE=NOT_IMPLEMENTED
INDEPENDENT_REPRODUCTION=NOT_IMPLEMENTED
```

## 14. Verdict receipt, lifecycle and invalidation

Every CLI report binds itself to:

```text
PROTOCOL_RAW_SHA256
RUN_BUNDLE_RAW_SHA256
VALIDATOR_SOURCE_SHA256_AT_REPORT
CORE_SOURCE_SHA256_AT_REPORT
PROTOCOL_SCHEMA_SHA256
RUN_SCHEMA_SHA256
STANDARD_DOCUMENT_SHA256
PACKAGE_MANIFEST_SHA256
```

`MANIFEST.sha256` covers all distributed package files except itself. These
hashes identify the evaluated bytes but do not authenticate who approved them;
release use still requires an externally trusted expected hash or signature.

A ZAI verdict is bound to one exact protocol and evidence bundle. Any change to
the candidate source, committed compiler, VM, runner, policy locks, visibility
boundary, blind case, key, semantic review, external report or event chain
requires a new run and invalidates reuse of the old verdict for the changed
artifact.

Producer test success may be reported only as a Producer result. Only an
independently executed locked blind run may receive an independent ZAI verdict.
Neither result is a cognition verdict.

Current truthful status:

```text
Z0_TO_Z4_SPECIFICATION=IMPLEMENTED_CANDIDATE
Z0_TO_Z4_PRODUCER_TESTS=SEPARATE_EVIDENCE_REQUIRED
ACTUAL_LOCKED_BLIND_RUN=UNVERIFIED_UNLESS_A_MATERIALIZED_RUN_PASSES
Z5_OBSERVATION_DEPENDENCE=NOT_IMPLEMENTED
Z6_BLIND_PERFORMANCE=NOT_IMPLEMENTED
Z7_INDEPENDENT_REPRODUCTION=NOT_IMPLEMENTED
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN
```
