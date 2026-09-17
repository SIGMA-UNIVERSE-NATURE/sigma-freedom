# SIGMA.AIL — G4 D20 Radius-Calibrated Uncertainty Evidence

DATE=2026-09-17
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
EVIDENCE_CLASS=USER_SUPPLIED_RUNTIME_TRANSCRIPT
PRIMARY_GENERATION_CLASSIFICATION=G4_GROUNDED_SEMANTIC_BRAIN_UNCERTAINTY_PRECURSOR
SECONDARY_RELEVANCE=G7_NORTH_STAR_INTEGRATED_BRAIN_STABILITY_PRECURSOR
GENERATION_PROMOTION=NO

## Handoff identity fields

```text
SYSTEM_IDENTITY=SIGMA.AIL
CURRENT_PROGRAM_GENERATION=G1
TARGET_GENERATION=G4
ACTIVE_REVISION=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
CANDIDATE_REVISION=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
PARENT_BRAIN_ID=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
PARENT_BRAIN_HEAD=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
ACTIVE_BRAIN_HEAD=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
MODEL_GENERATION=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
STATE_VERSION=NOT_PROVEN_FROM_SUPPLIED_TRANSCRIPT
```

No canonical revision/generation/brain identity is inferred from D20 naming, shell variables, directories, or chat context.

## Reported runtime metrics

The supplied transcript reports:

```text
FALSE_DEPENDENCY=0
UNRESOLVED=1
DEPENDENCY_RECALL=916
REOPEN_RECALL=1000
BALANCED_ACCURACY=958
OVERALL_ACCURACY=923
```

The exact metric scale is not independently specified in the supplied transcript. Values are preserved verbatim and are not silently converted into percentages.

## Gate logic shown in transcript

The supplied shell gate is:

```text
if [ "$GI" != "0" ] || \
   [ "$SI" != "0" ] || \
   [ "$MISS" != "0" ] || \
   [ "$EXTRA" != "0" ] || \
   [ "$D4V" != "0" ]; then

  echo "D20E_RESULT=INVALID_INTEGRITY"

elif [ "$FR" = "0" ] && \
     [ "$UR" -gt "0" ] && \
     [ "$RR" -gt "0" ] && \
     [ "$DR" -gt "500" ] && \
     [ "$BAL" -gt "500" ]; then

  echo "D20_RADIUS_CALIBRATED_UNCERTAINTY=PASS"

else
  echo "D20_RADIUS_CALIBRATED_UNCERTAINTY=FAIL_VALID"
fi
```

Observed emitted result:

```text
D20_RADIUS_CALIBRATED_UNCERTAINTY=PASS
```

Therefore, for this exact shell execution only:

```text
INVALID_INTEGRITY_BRANCH_TAKEN=NO
PASS_BRANCH_TAKEN=YES
PASS_CONDITION_EVALUATED_TRUE=YES
```

The transcript does not print the individual values of `GI`, `SI`, `MISS`, `EXTRA`, `D4V`, or `FR`; those variables are therefore not assigned standalone numeric values in this archival record.

## Evidence interpretation

This supplied transcript supports only the following bounded claims:

```text
D20_RADIUS_CALIBRATED_UNCERTAINTY=PASS_IN_EXACT_SUPPLIED_GATE_SCOPE
FALSE_DEPENDENCY=0
UNRESOLVED=1
DEPENDENCY_RECALL=916
REOPEN_RECALL=1000
BALANCED_ACCURACY=958
OVERALL_ACCURACY=923
INVALID_INTEGRITY_BRANCH_TAKEN=NO
PASS_BRANCH_TAKEN=YES
```

The presence of `UNRESOLVED=1` is material: the gate is not claiming uncertainty disappeared. The reported result is consistent with a calibrated behavior that preserves at least one unresolved state while maintaining the supplied dependency/reopen recall and balanced-accuracy thresholds.

Generation interpretation:

```text
G4_CALIBRATED_UNCERTAINTY_PRECURSOR=YES
G4_DEPENDENCY_RECALL_PRECURSOR=YES
G4_REVISION_REOPEN_RECALL_PRECURSOR=YES
G7_UNCERTAINTY_STABILITY_PRECURSOR=YES
G4_PROMOTION=NO
G7_PROMOTION=NO
CURRENT_GENERATION_REMAINS=G1
```

## Important boundary

This transcript does NOT independently establish:

```text
GENERAL_CALIBRATED_UNCERTAINTY=NOT_PROVEN
GENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN
GENERAL_BELIEF_REVISION=NOT_PROVEN
FULL_DOCUMENT_UNDERSTANDING=NOT_PROVEN
CROSS_DOCUMENT_UNDERSTANDING=NOT_PROVEN
LONG_CONTEXT_REVISION=NOT_PROVEN
GENERAL_HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
MODEL_GENERATION>0=NOT_PROVEN_FROM_THIS_TRANSCRIPT
EXACT_PARENT_BRAIN=NOT_PROVEN
EXACT_PARENT_BRAIN_HEAD=NOT_PROVEN
ACTIVE_BRAIN_HEAD=NOT_PROVEN
STATE_VERSION=NOT_PROVEN
G4_PROMOTION=NO
```

The gate name must not be expanded beyond the exact supplied calibration/evaluation scope.

## Relation to prior indexed evidence

Current indexed precursor chain already includes D9A/D10B/D11B/D12A/D12D1/D13B results in their own bounded scopes. D20 adds an uncertainty/reopen/dependency evaluation result. This archival record does not silently assert cryptographic model lineage from D13B or earlier artifacts because no parent/head/model receipt is shown here.

## Immediate next evidence needed

A stronger D20 proof should expose, where available:

```text
EXACT_TEST_SET_IDENTITY
EXACT_MODEL_ARTIFACT_SHA256
PARENT_MODEL_SHA256
PARENT_BRAIN_HEAD
ACTIVE_BRAIN_HEAD
CALIBRATION_BUCKETS_OR_RADIUS_DEFINITION
PER_CLASS_OR_PER_BUCKET_COUNTS
FALSE_POSITIVE_AND_FALSE_NEGATIVE_COUNTS
UNRESOLVED_CASE_IDENTITIES_OR_HASHES
REPLAY_ON_FRESH_PROCESS
NEGATIVE_CONTROLS
```

It should preserve the unresolved state rather than force a decision merely to raise accuracy.

## Runtime-truth boundary

```text
CHAT_SUMMARY_IS_RUNTIME_TRUTH=NO
THIS_FILE_IS_ARCHIVED_SUPPLIED_TRANSCRIPT_EVIDENCE=YES
INDEPENDENT_MACHINE_RECEIPT_FETCHED_FROM_RUNTIME=NO
CLAIM_SCOPE=EXACT_SUPPLIED_TRANSCRIPT_ONLY
```

## Final classification

```text
EVIDENCE_ALIAS=G4-PRECURSOR-D20-RADIUS-CALIBRATED-UNCERTAINTY
REPORTED_GATE=D20_RADIUS_CALIBRATED_UNCERTAINTY
REPORTED_GATE_RESULT=PASS
REPORTED_GATE_SCOPE=EXACT_SUPPLIED_GATE_AND_METRIC_SCOPE
GENERATION_PROMOTION_AUTHORIZED=NO
REMAINING_BOTTLENECK=G4_GROUNDED_SEMANTIC_GENERALIZATION_AND_LONG_CONTEXT_REVISION
```
