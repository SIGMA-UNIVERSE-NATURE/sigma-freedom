# VNM-08 FIX3 — Hierarchical Span-Form Weighting Integration Admission PASS

Date: 2026-09-07 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_VNM`
Status: `ADMITTED_IN_EXACT_TESTED_PREFLIGHT_SCOPE`

## Governance

```text
DO_NOT_LOAD_RESULTS=YES
LOAD_CAPABILITIES=YES
CAPABILITY_MUST_RUN_INSIDE_SIGMA=YES
RUNTIME_PROOF_REQUIRED=YES
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PRODUCTION_STATE_MUTATED=NO
```

VNM-08 is an integration-only admission stage. No new native `.sigma` cognition source was added for this stage. The claimed cognitive arrows remain owned by the already-admitted VNM-05, VNM-06, VNM-07, VNM-02, VNM-04, and VNM-01 native capabilities under the locked SIGMA VM.

## Capability

```text
CAPABILITY_ID=VNM-08_HIERARCHICAL_SPAN_FORM_TO_PERSISTENT_WEIGHTING_INTEGRATION
CAPABILITY_NAME=Native hierarchical span-form pair induction to persistent structural weighting integration
INTEGRATION_ONLY_STAGE=YES
NEW_NATIVE_SOURCE_REQUIRED=NO
REUSED_VNM07_FULL_SUBSUITE=YES
```

Teaching goal:

Prove that the admitted native hierarchical span-form chain can be composed without host cognitive substitution:

```text
VNM-05 native recurrent ordered adjacent-span induction
-> VNM-06 native outer-context derivation
-> VNM-07 native ordered span FORM + observation-ID derivation
-> VNM-02 native pair induction over span forms
-> exact mechanical routing
-> VNM-04 native hypothesis/raw-evidence generation
-> exact mechanical routing
-> VNM-01 native persistent structural weighting
-> fresh-VM persistence/replay
```

## Locked runtime and dependency identities

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99

VNM07_SOURCE_SHA256=8412ce07e6c9a53ae6bb27a88ec2847eadd54795a21dce35a3ff1ef29f75a57e
VNM07_BYTECODE_SHA256=50be8bc9fd4cf46f9d348d9eb72b19d9e90209af0e2f4f61649828fb1507a42b
VNM07_RUNNER_GIT_BLOB=840d6d86e11b7bc8fc8e881ee7dc5cb26e9c5ee3
VNM07_RUNNER_SHA256_CORRECTED=53fe674e377439146078994c4ba6af3215c96bd966f470d9bbac74bc383e1921
```

FIX3 wrapper:

```text
FIX3_WRAPPER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT_FIX3.sh
FIX3_WRAPPER_GIT_BLOB=a0cdb5c506e23b37de8ee8bd46dab8bc102144ac
FIX3_WRAPPER_SHA256=UNKNOWN_NOT_IN_SUPPLIED_FINAL_SUMMARY
MATERIALIZED_RUNNER_SHA256=d21ea17f2364b06be1c396f0e1e4786d1eade1bc3579af75c6032e6b6abb4e1d
FULL_GATE_RC=0
```

Do not infer the FIX3 wrapper SHA256 from its Git blob. The user-supplied final summary did not include that field.

## Final locked-runtime evidence

Observed final summary:

```text
TOTAL_VM_INVOCATIONS=29
VNM07_SUBSUITE_VM_INVOCATIONS=21
VNM08_ADDITIONAL_VM_INVOCATIONS=8
VNM04_VM_INVOCATIONS=4
VNM01_VM_INVOCATIONS=4
POST_VM_ALIGNMENT_PASS_COUNT=24
POST_VM_ALIGNMENT_FAIL_COUNT=0
VM_NONZERO_COUNT=0
STEP_LIMIT_HIT_COUNT=0
NEGATIVE_PASS_COUNT=11
HIERARCHICAL_WEIGHTING_INTEGRATION_PASS_COUNT=4
PERSISTENCE_PASS_COUNT=2
INPUT_DYNAMIC=YES
OUTPUT_DEPENDS_ON_INPUT=YES
NEGATIVE_TEST=PASS
PERSISTENT_STATE=YES_IN_VNM02_VNM01_COMPOSED_CHAIN
PERSISTENT_STATE_TEST=PASS
RESTART_REPLAY_TEST=PASS
REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES
INITIAL_HIERARCHICAL_WEIGHT=2
VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE
VNM06_SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE
VNM07_SPAN_FORM_SERIALIZATION_OWNER=SIGMA_NATIVE
VNM07_OBSERVATION_ID_DERIVATION_OWNER=SIGMA_NATIVE
VNM02_PAIR_INDUCTION_OWNER=SIGMA_NATIVE
VNM04_HYPOTHESIS_GENERATION_OWNER=SIGMA_NATIVE
VNM04_EVIDENCE_GENERATION_OWNER=SIGMA_NATIVE
VNM01_WEIGHT_UPDATE_OWNER=SIGMA_NATIVE
HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY
HOST_PAIR_GENERATION=NO
HOST_PAIR_SELECTION=NO
HOST_EVIDENCE_GENERATION=NO
HOST_WEIGHT_UPDATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
VNM07_SUBSUITE_UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT=0
STEP_LIMIT_STATUS=PASS_IN_29_INVOCATION_BOUNDED_COMPOSED_SUITE
PRODUCTION_STATE_MUTATED=NO
VNM_08_PREFLIGHT=PASS
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
```

## Historical failure evidence preserved

The admission does not erase earlier evidence:

1. Original VNM-08 attempt HOLDed before VM because the VNM-07 runner SHA256 metadata pin was incorrect while canonical runner bytes were unchanged.
2. VNM-08 FIX1 reached the negative support-mismatch case but the historical awk fault injection corrupted candidate framing.
3. VNM-08 FIX2 added a correct suffix-only fault block but left the legacy awk fault line executable; byte audit proved the legacy line overwrote the repaired candidate.
4. FIX3 removed only that legacy mechanical line, preserved the same case/oracle/PASS definition, hard-gated its absence after materialization, and reran the entire required 29-VM suite.

Relevant failure/root-cause checkpoints remain provenance and must not be deleted or reclassified as PASS.

## Admission classification

```text
VNM_08_ADMITTED=YES_IN_EXACT_TESTED_PREFLIGHT_SCOPE
ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
RUNTIME_PROOF=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE
PRODUCTION_BINDING=NO
PRODUCTION_PROMOTION_ALLOWED=NO
```

## Claim scope

```text
CLAIM_SCOPE=Bounded reuse of admitted VNM-05->06->07->02 native hierarchical span-form pipeline followed by exact mechanical routing into admitted VNM-04->01 native hypothesis/evidence generation and persistent +2 structural weighting; includes support-mismatch refusal, persistence, fresh-VM reuse, and identical downstream replay; no natural-language boundary or semantic claim.
```

This proves composition of the admitted structural capabilities in the exact tested bounded suite. It does not prove that learned spans are linguistic words/phrases, that the weighted relation is semantic equivalence, or that SIGMA understands Vietnamese.

## Explicit non-claims

```text
NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN
WORD_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_BOUNDARY_DETECTION=NOT_PROVEN
PHRASE_SEMANTICS=NOT_PROVEN
SEMANTIC_CONTEXT_EXTRACTION=NOT_PROVEN
SEMANTIC_EQUIVALENCE=NOT_PROVEN
DIACRITIC_EQUIVALENCE=NOT_PROVEN
WORD_MEANING=NOT_PROVEN
VIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN
PRODUCTION_BINDING=NO
```

## Next action

```text
NEXT_ACTION=DEPENDENCY_FIRST_REVIEW_FOR_SMALLEST_POST_VNM08_NATIVE_CAPABILITY
DO_NOT_DUPLICATE_LANG02A_OR_EXISTING_C5_INTERNET_INGRESS=YES
```
