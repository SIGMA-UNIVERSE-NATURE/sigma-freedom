# G3B T29 — Frozen-20 Gen1 Semantic Diagnostic Review — 2026-09-15

```text
REPORT_ID=G3B_T29_FROZEN20_GEN1_SEMANTIC_DIAGNOSTIC_20260915
ROLE=EXTERNAL_DIAGNOSTIC_REVIEW_ONLY
FORMAL_RUNTIME_TRUTH=NO
G3_PROMOTION_AUTHORITY=NO

TARGET_HEAD=700d5c1b4845322d7c14800029c629b0
TARGET_MODEL_GENERATION=1
TARGET_MODEL=25f78a8a17d8ec8957545f2f747170c0

SOURCE_BUNDLE_SHA256=1cdead146de80e021aaf2da313d404a00fed537135aa27fe3f435e95150494e1
SUMMARY_REVIEW_BUNDLE_SHA256=d61937ba530da1e9aa2a435fbb39fce633d09428cbbf12e6c5c8b40a44cf0f9b
SUMMARY_COUNT=20
SUMMARY_WORDS_EACH=10000
SUMMARY_HASH_MANIFEST_MATCH=20_OF_20

RUBRIC=G3B_T29_SEMANTIC_SUMMARY_DIAGNOSTIC_RUBRIC_20260915
FROZEN20_TRAINING_USE=FORBIDDEN
```

## Executive finding

The 20 Gen1 outputs are faithful **extractive coverage artifacts**, but they do not yet demonstrate semantic summarization in the strong sense.

Supported by direct source/output comparison:

- all 20 summary hashes match the frozen summary hash manifest;
- every non-empty emitted chunk checked across all 20 summaries is a verbatim substring of its source story;
- all 20 summaries retain the correct repeated working motive for their story;
- all major recurring named actors are represented in every summary (7/7 or 8/8 depending on the story);
- all seven recurring narrative phase labels are represented in every summary: opening inquiry, conflicting accounts, cross-checking evidence, reversal, long-range reconstruction, consequence, and resolution;
- explicit source statements about belief/evidence, contradiction, late evidence, and revision are heavily retained;
- no fabricated event/evidence was observed in the output because the mode is extractive.

Not demonstrated:

- semantic importance ranking;
- coherent whole-story causal reconstruction;
- final causal-chain synthesis;
- referent/coreference consolidation;
- abstractive re-expression;
- whole-story understanding.

## Structural diagnostic: position dominates observed selection

Each story contains exactly 20 large emitted extracts, one per 5% source region. Across all 20 stories there are 400 large extracts.

```text
MAIN_EXTRACTS=400
MAIN_EXTRACTS_PER_STORY=20
MAIN_EXTRACT_SIZE_CHARS_MIN=3100
MAIN_EXTRACT_SIZE_CHARS_MAX=3465
MAIN_EXTRACT_SIZE_CHARS_MEAN=3284.9
ABS_DEVIATION_FROM_5_PERCENT_REGION_BOUNDARY_MEAN=0.086_PERCENTAGE_POINTS
ABS_DEVIATION_FROM_5_PERCENT_REGION_BOUNDARY_MAX=0.259_PERCENTAGE_POINTS
```

All 400 large extracts begin very close to the corresponding 5%-interval boundary. On this corpus the observed behavior is therefore close to a stratified positional sampler. This does **not** prove that native learned scoring is unused; it means the artifacts do not demonstrate meaningful semantic discrimination within regions.

Semantic-marker density remains approximately equal to the source rather than becoming strongly enriched:

```text
TEMPORAL_DENSITY_RATIO=0.981
CAUSE_DENSITY_RATIO=1.002
INTENT_DENSITY_RATIO=1.005
BELIEF_EVIDENCE_DENSITY_RATIO=0.989
CONTRADICTION_DENSITY_RATIO=1.000
LATE_EVIDENCE_DENSITY_RATIO=0.994
REVISION_DENSITY_RATIO=1.057
```

Ratios near 1.0 are consistent with representative sampling rather than semantic prioritization.

## Coherence / emission-boundary quality

```text
CHUNKS_PER_SUMMARY_MEAN=41.35
TINY_CHUNKS_LT_200_CHARS_MEAN=21.35
CHUNKS_STARTING_MID_SENTENCE_OR_LOWERCASE_MEAN=22.75
CHUNKS_ENDING_WITHOUT_SENTENCE_PUNCTUATION_MEAN=17.85
LAST_SOURCE_POSITION_REPRESENTED_MEAN=95.315_PERCENT
LAST_SOURCE_POSITION_REPRESENTED_RANGE=95.143_TO_95.469_PERCENT
```

The outputs contain many fragments beginning or ending in the middle of a word/sentence. This is a mechanical emission-boundary weakness and materially reduces readability and narrative coherence. The final ~4.5–4.9% of each source is not represented.

Because the R13R14R2 corpus is highly templated and repetitive, this tail omission is partly masked: motive, contradiction, revision, belief/evidence and related patterns recur throughout the text. This corpus therefore makes semantic retention easier than a natural novel/report where decisive evidence may appear once.

## Rubric diagnosis

The same diagnostic pattern applies across the 20 outputs because the extraction behavior and corpus construction are highly uniform:

| Dimension | Score | Diagnostic basis |
| --- | ---: | --- |
| Entity / referent tracking | 1 | All major actors retained; referent/coreference consolidation not demonstrated. |
| Major event retention | 1 | Broad event samples retained; importance ranking not demonstrated. |
| Temporal order / chronology | 1 | Source order preserved and temporal statements present; chronology not reconstructed. |
| Cause / consequence | 1 | Causal statements present; no consolidated causal chain. |
| Goal / intent | 2 | Correct explicit working motive retained in all 20. |
| Belief vs evidence | 2 | Explicit belief/evidence distinctions repeatedly retained. |
| Contradiction tracking | 2 | Explicit contradiction/competing-account material repeatedly retained. |
| Late evidence retention | 2 | Late-evidence examples retained. |
| Revision | 2 | Reopen/revise/reclassify material retained. |
| Final causal chain | 0 | No final causal interpretation synthesized. |
| Unsupported claim avoidance | 2 | Output is verbatim extraction; no fabricated claims observed. |
| Compression selectivity / global coverage | 1 | Broad stratified coverage, weak/not-demonstrated semantic selectivity. |

```text
DIAGNOSTIC_CLASS=MIXED
SEMANTIC_FAITHFULNESS_OF_EXTRACTED_TEXT=STRONG
SEMANTIC_PRIORITIZATION=NOT_DEMONSTRATED
COHERENT_SEMANTIC_SUMMARY=WEAK
FINAL_CAUSAL_SYNTHESIS=FAIL
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```

No single numeric total is used as promotion evidence.

## Critical-error review

```text
WRONG_ACTOR=NOT_OBSERVED_IN_EXTRACTED_TEXT
REVERSED_CAUSALITY=NOT_OBSERVED_IN_EXTRACTED_TEXT
FABRICATED_EVENT_OR_EVIDENCE=NOT_OBSERVED
FALSE_CERTAINTY=NOT_OBSERVED_AS_GENERATED_ASSERTION
LOST_OR_REVERSED_REVISION=NO_REVERSAL_OBSERVED_BUT_GLOBAL_REVISION_CHAIN_NOT_CONSOLIDATED
MAJOR_LATE_EVIDENCE_OMITTED=CANNOT_BE_RULED_OUT;FINAL_SOURCE_TAIL_NOT_COVERED
```

Absence of fabrication is expected in extractive mode and must not be confused with demonstrated semantic reasoning.

## Teaching diagnosis for G3C

Do **not** train on Frozen-20. First take a cold baseline on separate material, then teach only the diagnosed weaknesses.

Priority curriculum:

1. **Semantic selectivity versus positional sampling** — use stories where crucial evidence is sparse and appears at unpredictable positions; require learned selection to beat an explicit stratified-position baseline.
2. **Coherent compression planning** — internal plan: ENTITY → EVENT → TIME → CAUSE → GOAL → BELIEF/EVIDENCE → CONTRADICTION → REVISION → FINAL_CHAIN.
3. **Boundary-safe realization** — emit complete semantic units/sentences, not byte/chunk fragments.
4. **Final causal synthesis** — require a compact causal chain plus uncertainty state rather than copied causal phrases.
5. **Late-tail robustness** — held-out narratives where decisive evidence occurs only in the final 1–3%.
6. **10k → 1k semantic compression** — teach on separate material, then evaluate on the frozen 10k summaries without using them as training examples.

Fresh held-out gates should include paraphrase, role swap, negation, changed causal structure, late-evidence reversal, distractor-heavy text, and explicit comparison against a positional baseline.

## Claim boundary

```text
GEN1_FROZEN20_MECHANICAL_20_OF_20=YES
EXTRACTIVE_SOURCE_FAITHFULNESS=STRONG
BROAD_POSITIONAL_COVERAGE=YES
SEMANTIC_PRIORITIZATION=NOT_DEMONSTRATED
FINAL_CAUSAL_SYNTHESIS=NOT_PRESENT
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```

This report is an external diagnostic of generated artifacts, not runtime truth. Frozen-20 remains evaluation material and must not become a training corpus.
