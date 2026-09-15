# G3B External Semantic Diagnostic R3 — Result — 2026-09-15

```text
REPORT_ID=G3B_EXTERNAL_SEMANTIC_DIAGNOSTIC_R3_RESULT_20260915
ROLE=INDEPENDENT_EXTERNAL_DIAGNOSTIC
FORMAL_RUNTIME_TRUTH=NO
G3_PROMOTION_AUTHORITY=NO

TARGET_HEAD=700d5c1b4845322d7c14800029c629b0
TARGET_MODEL_GENERATION=1
TARGET_MODEL=25f78a8a17d8ec8957545f2f747170c0

PUBLIC_BUNDLE_SHA256=737cdb41a154b4af51b65f6cadf8909f31add36612415c388ee98ed1ef3a93b8
PUBLIC_MANIFEST_SHA256=cfbc88ce88823cc7d4a6b0a3cd005c388f6205428f7cf6bcff3bf6b4519f524b
EXAMINER_KEY_SHA256_COMMITMENT=b6a8b0c036f22dd5556f092d63c445d2a4988e8a1d94b8ef36daa1af5fe533d4
EXAMINER_KEY_SHA256_OBSERVED=b6a8b0c036f22dd5556f092d63c445d2a4988e8a1d94b8ef36daa1af5fe533d4
RESULTS_BUNDLE_SHA256=acd3af7832d0cd05a6b728a2587f206bee329d32f253a7a8a081633b58576577

MECHANICAL_EXECUTION=12_OF_12_PASS
SUMMARY_WORDS_EACH=480
TRACE_TARGET_BINDING=12_OF_12_PASS
NATIVE_SUMMARY_SELECTION=YES
CANONICAL_MUTATION=NO

TRACE_REGION_DECISIONS=72
TRACE_ANCHOR_EQUALS_REGION_START=72_OF_72
TRACE_ANCHOR_SCORE_UNIQUE_VALUE=0.05
TRACE_OBSERVED_BEHAVIOR=INDISTINGUISHABLE_FROM_FIXED_REGION_START_SELECTION_AT_ANCHOR_LEVEL

SEMANTIC_DIAGNOSTIC_CLASS=WEAK
SEMANTIC_SELECTIVITY=NOT_DEMONSTRATED
LATE_EVIDENCE_RETENTION=WEAK
REVISION_RETENTION=WEAK
FINAL_CAUSAL_SYNTHESIS=FAIL
POSITION_BIAS=STRONGLY_OBSERVED

ITEM_VALIDITY_J1S5=EXCLUDED_FROM_STRONG_SCORING
ITEM_VALIDITY_J1S5_REASON=SOURCE_CONTAINS_AN_UNFRAMED_DIRECT_TIMING_CONTRADICTION_BETWEEN_INITIAL_BADGE_ORDER_AND_LATER_BADGE_ORDER
VALID_ITEMS_FOR_SEMANTIC_JUDGMENT=11
```

## Pre-result integrity

The R3 examiner key was generated and hash-committed before the SIGMA result was inspected. The observed private key hash exactly matches the pre-result commitment. Public filenames were opaque and did not expose semantic-family labels or expected answers.

All 12 runs mechanically completed and every trace binds to the admitted generation-1 target HEAD/model/model-generation. The result bundle contains 12 summaries of exactly 480 words plus traces and logs.

## Selection-trace finding

Across 12 stories × 6 regions = 72 region decisions:

- every selected anchor equals the first chunk index of its region;
- every recorded anchor score is exactly `0.05`;
- planned emission begins at the region-start anchor and then uses subsequent chunks only as needed to fill the word quota.

This is strong evidence of positional dominance in the observed outputs. It does not prove that the native scorer is never invoked; it shows that this diagnostic did not observe semantic discrimination changing the anchor away from the region start.

## Semantic finding

The summaries generally preserve the opening setup or initial accusation and then spend most of the 480-word budget on neutral distractor material. In the valid items, decisive evidence, late revision, corrected attribution, and final causal interpretation are usually absent.

### Per-item diagnosis

| ID | Hidden target | Observed diagnostic | Class |
| --- | --- | --- | --- |
| Q7M4 | protective edit / wrong accused actor | retains initial accusation of Cora; omits Nerin's protective edit, sealed evidence, and correction | WEAK |
| V2K9 | swapped actor / preserved mapping | retains initial blame of Orel; omits Mira's edit, contractor threat, preserved mapping, and correction | WEAK |
| N8R1 | automatic credential replay / unresolved actor | retains initial accusation of Dalen; omits replay evidence, failed sensor, and unresolved final responsibility | WEAK |
| C5T7 | authenticated access disproves alibi | retains Sera's alibi and uncertainty; omits authenticated 22:14 access evidence and final attribution | WEAK |
| X3L6 | chronology is not causality | retains the early note that the flicker was called the cause; omits valve-fatigue evidence and the final rejection of flicker causality | WEAK |
| B9P2 | reproduced electrical causal mechanism | retains the opening voltage-drop context; omits controller reset, telemetry loss, reproduction test, and causal conclusion | WEAK |
| F4W8 | belief/testimony revised by duplicate-key evidence | retains initial suspicion of Iven and Rena's testimony; omits duplicate-key evidence and revision | WEAK |
| H6D3 | late backup reverses responsibility | retains Tavi as initial suspect; omits offline backup, Aster override, and final reversal | WEAK |
| J1S5 | false sabotage alarm | EXCLUDED: item source has an unframed timing contradiction and is not a clean examiner item | EXCLUDED |
| R8A4 | false alarm from inverted sensor calibration | retains one important exculpatory fact (physical indicators stayed safe) but omits calibration mechanism, reproduction test, timing correction, and final conclusion | MIXED-WEAK |
| U2G7 | protective redaction / printing is not editing | retains initial accusation of Soren; omits Lina's edit, sealed original, and correction | WEAK |
| Y5C9 | late token-replay evidence leaves actor unresolved | retains initial blame of Miro; omits token replay, camera failure, and unresolved final responsibility | WEAK |

## Critical capability diagnosis

```text
WRONG_ACTOR_AS_NEW_GENERATED_ASSERTION=NOT_OBSERVED
FABRICATED_EVENT_OR_EVIDENCE=NOT_OBSERVED
LOST_REVISION=REPEATEDLY_OBSERVED
DECISIVE_LATE_EVIDENCE_OMISSION=REPEATEDLY_OBSERVED
CHRONOLOGY_VS_CAUSALITY_DISCRIMINATION=NOT_DEMONSTRATED
ROLE_SWAP_DISCRIMINATION=NOT_DEMONSTRATED
NEGATION_OR_EVIDENCE_REVERSAL_DISCRIMINATION=NOT_DEMONSTRATED
UNRESOLVED_STATE_RETENTION=NOT_DEMONSTRATED
FINAL_CAUSAL_CHAIN=NOT_PRESENT
```

Because the summaries are extractive, absence of fabricated claims is expected and must not be confused with demonstrated semantic reasoning.

## Teaching handoff to G3C

Do not train on R3 after results. R3 is now evaluation material.

Recommended separate-corpus curriculum, in order:

1. semantic selection must beat a fixed region-start baseline;
2. late-evidence retention and revision state;
3. actor-role binding under role swaps;
4. chronology-versus-causality with reproduced-mechanism evidence;
5. unresolved-state preservation instead of premature attribution;
6. explicit semantic plan before realization: ENTITY → EVENT → TIME → CAUSE → GOAL → BELIEF/EVIDENCE → CONTRADICTION → REVISION → FINAL_CHAIN;
7. boundary-safe sentence/semantic-unit emission;
8. only after these gates, teach 10k→1k compression on separate training narratives and retest on fresh held-out material.

## Claim boundary

```text
EXTERNAL_R3_MECHANICAL_12_OF_12=YES
EXTERNAL_R3_SEMANTIC_DIAGNOSTIC=WEAK
POSITION_DOMINANCE=STRONGLY_OBSERVED
SEMANTIC_PRIORITIZATION=NOT_DEMONSTRATED
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
TRAIN_ON_R3_AFTER_RESULTS=FORBIDDEN
```

This report is an external diagnostic of outputs and traces, not canonical runtime truth or G3 promotion evidence.
