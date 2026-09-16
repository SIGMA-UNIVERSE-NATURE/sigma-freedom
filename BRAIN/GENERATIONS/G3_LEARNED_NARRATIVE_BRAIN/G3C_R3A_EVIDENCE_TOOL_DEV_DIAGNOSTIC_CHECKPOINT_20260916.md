# G3C R3A Evidence-Tool DEV Diagnostic Checkpoint — 2026-09-16

```text
HANDOFF_ID=G3C_R3A_EVIDENCE_TOOL_DEV_DIAGNOSTIC_CHECKPOINT_20260916
SYSTEM_IDENTITY=SIGMA.AIL
LANE=G3C_LEARNED_NARRATIVE_CORE
CURRENT_PROGRAM_GENERATION=G2_ONE_SIGMA_AIL
TARGET_GENERATION=G3_LEARNED_NARRATIVE_BRAIN
G3_STATUS=CANDIDATE_TRACK_ACTIVE_NOT_PROMOTED
G3_PROMOTION=NO
CANONICAL_MODEL_MUTATION=NO
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
FROZEN20_TRAINING_USE=FORBIDDEN
EXTERNAL_R3_TRAINING_USE=FORBIDDEN
SEALED_G3B_R4_ACCESS=FORBIDDEN_BEFORE_REMEDIATION
RUNTIME_TRUTH_SOURCE=HASH_BOUND_MACHINE_RECEIPT_OR_EVIDENCE_ARTIFACT
CHAT_SUMMARY_IS_RUNTIME_TRUTH=NO
```

## Purpose

This checkpoint records the completed G3C R2 3x3 control pilot and the current R3A evidence-tool remediation diagnostic so another G3C continuation lane can resume without reopening completed work or inspecting sealed G3B R4.

This is not a G3 promotion artifact and not proof of semantic understanding.

## Parent G3B remediation target

G3B diagnosed the primary failure as semantic selection failing to beat fixed region-start behavior. The external trace profile was:

```text
TRACE_REGION_DECISIONS=72
TRACE_ANCHOR_EQUALS_REGION_START=72_OF_72
TRACE_ANCHOR_SCORE_UNIQUE_VALUE=0.05
POSITION_DOMINANCE=STRONGLY_OBSERVED
SEMANTIC_SELECTIVITY=WEAK
LATE_EVIDENCE_RETENTION=WEAK
REVISION_RETENTION=WEAK
FINAL_CAUSAL_SYNTHESIS=FAIL
```

Do not train on Frozen-20 or External R3. Do not inspect sealed G3B R4 before remediation is complete.

## R2 full-controls pilot — closed

R2 FIX1 completed all 3 conditions x 3 prelocked seeds.

```text
SEED_104729=BASE_16/80;RANDOM_20/80;CURRICULUM_22/80;GROUPS_A3_B6_C8_D5
SEED_130363=BASE_18/80;RANDOM_19/80;CURRICULUM_23/80;GROUPS_A6_B10_C5_D2
SEED_155921=BASE_18/80;RANDOM_19/80;CURRICULUM_20/80;GROUPS_A7_B6_C3_D4
THREE_SEEDS_REPORTED=YES
CURRICULUM_PILOT_THRESHOLD_PASS=FAIL
CURRICULUM_MORE_EFFICIENT_ALL_SEEDS=NO
G3_PROMOTION=NO
```

R2 aggregate receipt:

```text
R2_AGGREGATE_RECEIPT_SHA256=a023d6755c50345870affd3476740207fff3c80a7746783b766756af342c2d07
```

Interpretation boundary: curriculum beat the no-weight-update blind total in all three seeds, but the required per-group 18/20 threshold failed. R2 therefore did not close semantic remediation.

## R3A evidence-tool candidate — exact artifact identity

R3A was installed as a sibling diagnostic artifact and did not mutate the R2 model or canonical state.

```text
R3A_BUNDLE_SHA256=7c073b489416dee60586220944352e440e37b38664a8f24dd6b328caa1db9fec
R3A_SOURCE_SHA256=735aef9922746ed332109f312f7cf2dff78071d0e0d0ce7ed51642d7143c3590
R3A_RUNNER_SHA256=fd656709b74585a98c129276e49ab3db26baf3d6dca908ca335b43460ba8d2de
R3A_BYTECODE_SHA256=cc89f69bff7eb856127d33811d11890cee47812635c93b66a872b77fd98323ba
```

R3A supplies a native candidate-conditioned evidence scan using the existing learned representation/model. It compares candidate support using final recurrent memory, strongest context-line support, and latest context-line support. It is a diagnostic substrate, not a final semantic readout. No story-specific rule, phrase-specific rule, answer key, blind gold, or sealed-R4 content is encoded.

## R3A DEV-only machine results

R3A was evaluated only on the existing DEV set from the three curriculum-trained R2 models.

```text
SEED_104729_R2_DEV=9/40
SEED_104729_R3A_DEV=14/40
SEED_104729_DELTA=+5
R3A_RECEIPT_104729_SHA256=ca1de3ac064dc36b03e1020964cddd815ebe5c8e3c452e3732e6e240dce44846

SEED_130363_R2_DEV=8/40
SEED_130363_R3A_DEV=13/40
SEED_130363_DELTA=+5
R3A_RECEIPT_130363_SHA256=fa8ec2308e12d48330162f607888034b2718826f44a2a4a788935b0e6c0b251f

SEED_155921_R2_DEV=11/40
SEED_155921_R3A_DEV=11/40
SEED_155921_DELTA=0
R3A_RECEIPT_155921_SHA256=73b73ae268442437d647c8cf5785154bd4153f89102aa53bb0e9b699d20fd56e

R2_DEV_TOTAL=28/120
R3A_DEV_TOTAL=38/120
NET_DELTA=+10
WRONG_TO_RIGHT=25
RIGHT_TO_WRONG=15
BLIND_USED=NO
SEALED_R4_USED=NO
MODEL_UNCHANGED=PASS
CANONICAL_UNCHANGED=PASS
HOST_COGNITION=NO
```

Interpretation boundary: R3A improved aggregate DEV correctness by 10/120 with positive net conversions, but one seed showed no gain. This is evidence of a useful diagnostic substrate, not a stable semantic capability claim.

## R3A anchor-behavior audit

The fixed region-start pathology was mechanically broken as an absolute rule on DEV:

```text
SEED_104729_REGION_START=2/40
SEED_104729_MIDDLE=22/40
SEED_104729_LATEST=16/40

SEED_130363_REGION_START=17/40
SEED_130363_MIDDLE=11/40
SEED_130363_LATEST=12/40

SEED_155921_REGION_START=3/40
SEED_155921_MIDDLE=23/40
SEED_155921_LATEST=14/40

TOTAL_QUERIES=120
REGION_START=22/120
MIDDLE=56/120
LATEST=42/120
INVALID=0
DISTINCT_EVIDENCE_INDICES=5
FIXED_REGION_START_BEHAVIOR=BROKEN_AS_ABSOLUTE_RULE
```

Correctness conditioned on selected evidence position:

```text
START_CORRECT=5/22
MIDDLE_CORRECT=19/56
LATEST_CORRECT=14/42
```

Interpretation boundary: R3A no longer always anchors at the region start, but this does not prove that the new anchors are semantically correct or sufficient for late-evidence/revision reasoning.

## Current supported claims

```text
R2_FULL_3X3_CONTROLS=COMPLETE
R2_CURRICULUM_THRESHOLD=FAIL
R3A_DEV_ONLY_PROBE=COMPLETE_3_SEEDS
R3A_AGGREGATE_DEV_DELTA=+10_OF_120
R3A_WRONG_TO_RIGHT=25
R3A_RIGHT_TO_WRONG=15
FIXED_REGION_START_BEHAVIOR=BROKEN_AS_ABSOLUTE_RULE_ON_R3A_DEV_TRACE
R3A_MODEL_MUTATION=NO
CANONICAL_MUTATION=NO
BLIND_USED_BY_R3A=NO
SEALED_R4_USED=NO
HOST_COGNITION=NO
```

## NOT PROVEN

```text
SEMANTIC_SELECTION_CORRECTNESS=NOT_PROVEN
SEMANTIC_SELECTION_BEATS_POSITION_BASELINE_ON_HELD_OUT_GATE=NOT_PROVEN
LATE_EVIDENCE_RETENTION=NOT_PROVEN
REVISION_RETENTION=NOT_PROVEN
ROLE_SWAP_GENERALIZATION=NOT_PROVEN
CHRONOLOGY_CAUSALITY_DISCRIMINATION=NOT_PROVEN
UNRESOLVED_STATE_RETENTION=NOT_PROVEN
FINAL_CAUSAL_CHAIN_RETENTION=NOT_PROVEN
PARAPHRASE_GENERALIZATION=NOT_PROVEN
NEW_NAMES_NEW_VOCAB=NOT_PROVEN
WHOLE_STORY_UNDERSTANDING=NOT_PROVEN
G3_PROMOTION=NO
```

## Exact continuation point

Do not rerun R2. Do not rerun the three completed R3A DEV probes unless verifying byte-identical reproducibility. Do not inspect blind or sealed G3B R4.

The next remediation step should remain in G3C and remain DEV-only until a stronger readout is demonstrated.

```text
PROPOSED_NEXT_GATE=G3C_R3B_LEARNED_COMPARATOR_READOUT_DEV_ONLY
STATUS=NOT_STARTED
PURPOSE=REPLACE_R3A_FIXED_SUM_DIAGNOSTIC_READOUT_WITH_A_LEARNED_COMPARATOR_OVER_R3A_EVIDENCE_SUBSTRATE
BLIND_ACCESS=FORBIDDEN
SEALED_R4_ACCESS=FORBIDDEN
HOST_COGNITION=NO
STORY_SPECIFIC_RULES=FORBIDDEN
PHRASE_SPECIFIC_RULES=FORBIDDEN
EXPECTED_ANSWER_LEAKAGE=FORBIDDEN
SEMANTIC_VM_OPCODE=FORBIDDEN
```

R3B should preserve the R3A evidence substrate but learn how to weight/compare evidence rather than hard-coding a fixed sum. Before any blind use, require 3-seed DEV machine evidence showing reproducible improvement without new positional collapse, exact model/tool hashes, restart/provenance continuity where applicable, and no canonical mutation.

Only after a separately admitted remediation candidate closes the required G3C machine gates should control return to G3B for its precommitted sealed fresh holdout.
