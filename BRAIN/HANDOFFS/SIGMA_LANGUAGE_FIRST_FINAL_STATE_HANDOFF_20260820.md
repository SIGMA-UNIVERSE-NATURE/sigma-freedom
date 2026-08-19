# SIGMA — LANGUAGE-FIRST FINAL STATE HANDOFF

**Date:** 2026-08-20 (+07:00)  
**Host:** OPPO  
**Working tree:** `~/SIGMA/sigma_genesis1`  
**Direction:** `LANGUAGE_FIRST`

## 1. Locked direction

```text
MOTHER_LANGUAGE=SIGMA_PSI
VM_ROLE=EXECUTION_SUBSTRATE_FOR_LANGUAGE
MATH_PRIORITY=UTILITY_ONLY

DO_NOT_HARDCODE_SIGMA_MEANING=TRUE
DO_NOT_PREWRITE_SIGMA_THOUGHT=TRUE
PRESERVE_DIFFERENCE=TRUE
PRESERVE_AMBIGUITY=TRUE
PRESERVE_UNCERTAINTY=TRUE
PRESERVE_PROVENANCE=TRUE
```

`GPT_REFERENCE` is for GPT/human continuity only; it is not SIGMA training truth.

Known reference file:

`DOCS/GPT_REFERENCE/SIGMA_PSI_GPT_REFERENCE_DICTIONARY_v2.0.0-rc1_20260819.md`

## 2. Last major machine-evidence milestone

```text
MILESTONE=SIGMA_LANGUAGE_FIRST_PERSISTENT_CONTEXT_CAPSULE
STATUS=PASS_WITH_TESTED_SCOPE
```

Recorded note:

`SIGMA_LANGUAGE_FIRST_MILESTONE_PERSISTENT_CAPSULE.state`

Verified output:

```text
TARGET=SIGMA_PERSISTENT_CONTEXT_CAPSULE
REGISTRY=SIGMA_SURFACE_ATOM_REGISTRY_V3_CANDIDATE
PERSISTENT_BRANCHES=13
MISSING_ATOM_REFERENCES=0
IDENTITY_SCOPE=SURFACE_FORM
AMBIGUITY=PRESERVED
UNCERTAINTY=PRESERVED
SEMANTIC_IDENTITY_NOT_CLAIMED=TRUE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

## 3. Surface atom registry V3 candidate

File:

`SIGMA_SURFACE_ATOM_REGISTRY_V3_CANDIDATE.state`

Machine evidence:

```text
MERGE_STATUS=CANDIDATE_VALIDATED_NO_MUTATION
SOURCE_ATOM_COUNT=23
SOURCE_DECLARED_ATOM_COUNT=23
NEW_ATOM_COUNT=14
TOTAL_ATOM_COUNT=37
SOURCE_NEXT_ATOM_ID=24
NEXT_ATOM_ID=38
REUSE_CHECKS=9
REUSE_MISMATCH=0
DUPLICATE_IDS=0
DUPLICATE_SURFACE_FORMS=0
SOURCE_REGISTRY_MUTATED=FALSE
IDENTITY_SCOPE=SURFACE_FORM
SEMANTIC_IDENTITY_NOT_CLAIMED=TRUE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

Provenance:

```text
ATOM_ID 1..14   → SOURCE=V1
ATOM_ID 15..23  → SOURCE=PROBE_C
ATOM_ID 24..37  → SOURCE=PROBE_D
NEXT_ATOM_ID=38
```

This proves persistent **surface-form identity continuity** in the tested scope. It does not prove semantic identity.

## 4. Language-first achievements already demonstrated

```text
UNKNOWN_PRESERVATION                 = OBSERVED
LOSSLESS_SURFACE_SEGMENTATION        = PASS_WITH_OBSERVED_ASCII_SCOPE
CONTEXT_TRIPLE_GRAPH                 = OBSERVED
CROSS_SAMPLE_RECURRENCE              = OBSERVED
ROLE_SHAPE_DISCOVERY                 = OBSERVED
CONTEXT_DISTRIBUTION                 = OBSERVED
AMBIGUITY_PRESERVATION               = PASS_IN_TESTED_CAPSULE
UNCERTAINTY_PRESERVATION             = PASS_IN_TESTED_CAPSULE
PERSISTENT_SURFACE_ATOM_IDENTITY     = PASS_WITH_TESTED_SCOPE
PROVENANCE_PRESERVATION              = PASS_IN_V3_CANDIDATE
PERSISTENT_CONTEXT_CAPSULE           = PASS_WITH_TESTED_SCOPE

SEMANTIC_MEANING_ASSIGNMENT          = NOT_PROVEN / NOT_CLAIMED
CANONICAL_SIGMA_PSI_PROMOTION        = NOT_DONE
```

Important observed ambiguity evidence:

```text
DISTINCT_CONTEXTS=13
FORM_SAMPLE_SUPPORT=6
MAX_CONTEXT_SAMPLE_SUPPORT=3
SINGLE_CONTEXT=FALSE
PRESERVE_MULTIPLE_CONTEXTS=TRUE
```

SIGMA preserved multiple branches instead of collapsing them to one meaning.

## 5. cross_sample_recurrence_v0_2 result

v0.2 correctly excluded the form that already had a capsule by reading `OBSERVED_FORM` from capsule state.

Observed next selection:

```text
SELF_SELECTED_FORM=.
```

The punctuation form won because context variability alone was high. This exposed a selection defect:

```text
CONTEXT_VARIABILITY_ALONE
!= SUFFICIENT_LEXICAL_SEMANTIC_INDUCTION_CRITERION
```

Punctuation remains preserved in memory/graphs, but punctuation-only forms should not compete as lexical semantic-induction candidates.

## 6. Exact current frontier — v0.3

Source:

`sigma_language_cross_sample_recurrence_v0_3.sigma`

Created from v0.2 and patched with a general structural filter:

```text
HAS_ALNUM(t)
```

Selection now requires:

```text
score > best_score
AND t != excluded_form
AND HAS_ALNUM(t)
```

Important boundaries:

```text
"." IS NOT HARDCODED
EXCLUDED FORM IS NOT HARDCODED
PUNCTUATION IS STILL PRESERVED IN MEMORY
```

Last confirmed action:

```text
PATCH_PASS
```

Exact stop state:

```text
V03_SOURCE_CREATED=TRUE
V03_PATCH_PASS=TRUE
V03_COMPILED=FALSE
V03_VM_EXECUTED=FALSE
V03_RESULT=UNPROVEN
```

No claim may be made that v0.3 PASSed.

## 7. NEXT ONLY

The new window must continue only with:

```bash
cd ~/SIGMA/sigma_genesis1
./native/sigmac sigma_language_cross_sample_recurrence_v0_3.sigma sigma_language_cross_sample_recurrence_v0_3.sigmab && ./native/sigma-vm.v09_candidate sigma_language_cross_sample_recurrence_v0_3.sigmab | tee SIGMA_CROSS_SAMPLE_RECURRENCE_V03.state
```

Then stop and read the real SIGMA VM output.

## 8. Do-not-rerun / do-not-rebuild locks

```text
DO_NOT_RERUN_COMPLETED_PASS=TRUE
DO_NOT_REBUILD_SURFACE_ATOM_REGISTRY=TRUE
DO_NOT_REBUILD_PERSISTENT_CONTEXT_CAPSULE=TRUE
DO_NOT_PROMOTE_V3_REGISTRY_TO_CANONICAL=TRUE
DO_NOT_HARDCODE_NEXT_FORM=TRUE
DO_NOT_HARDCODE_MEANING=TRUE
DO_NOT_USE_GPT_REFERENCE_AS_SIGMA_TRAINING=TRUE
DO_NOT_CLAIM_SEMANTIC_IDENTITY=TRUE
DO_NOT_CLAIM_CANONICAL_SIGMA_PSI=TRUE
```

## 9. Five continuity verification questions — NO ANSWERS

1. **SIGMA hiện đang làm việc trên host nào, working tree chính xác là gì, hướng phát triển đang bị khóa theo nguyên tắc nào, và VM đang giữ vai trò gì trong hướng đó?**

2. **Milestone machine-evidence cuối cùng đã PASS trước điểm dừng là milestone nào? Hãy nêu chính xác trạng thái persistent context capsule, số branch, missing atom references, ambiguity, uncertainty, semantic identity, meaning assignment và canonical status.**

3. **`SIGMA_SURFACE_ATOM_REGISTRY_V3_CANDIDATE.state` hiện có bao nhiêu atom, `NEXT_ATOM_ID` là bao nhiêu, provenance của ba dải atom được hình thành từ đâu, và các giá trị `REUSE_MISMATCH`, `DUPLICATE_IDS`, `DUPLICATE_SURFACE_FORMS`, `SOURCE_REGISTRY_MUTATED` hiện là gì?**

4. **Trong `cross_sample_recurrence_v0_2`, chuyện gì xảy ra sau khi form đã có capsule bị loại khỏi selection? Vì sao phải tạo `sigma_language_cross_sample_recurrence_v0_3.sigma`, v0.3 đã được thay đổi bằng cơ chế tổng quát nào, và trạng thái compile/execute/result của v0.3 tại đúng điểm dừng là gì?**

5. **Từ đúng điểm dừng hiện tại, hành động machine đầu tiên duy nhất phải thực hiện là gì? Hãy đưa đúng command cần chạy, đồng thời nói rõ những PASS/gate nào tuyệt đối không được rerun hoặc rebuild trước khi đọc output thật của SIGMA.**

## FINAL STOP MARKER

```text
HOST=OPPO
WORKING_TREE=~/SIGMA/sigma_genesis1
DIRECTION=LANGUAGE_FIRST

LAST_MAJOR_PASS=SIGMA_LANGUAGE_FIRST_PERSISTENT_CONTEXT_CAPSULE

SURFACE_ATOM_REGISTRY_V3_CANDIDATE=VALIDATED_NO_MUTATION
TOTAL_ATOMS=37
NEXT_ATOM_ID=38

PERSISTENT_BRANCHES=13
MISSING_ATOM_REFERENCES=0
AMBIGUITY=PRESERVED
UNCERTAINTY=PRESERVED
SEMANTIC_IDENTITY_NOT_CLAIMED=TRUE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE

V03_SOURCE_CREATED=TRUE
V03_PATCH_PASS=TRUE
V03_COMPILED=FALSE
V03_EXECUTED=FALSE
V03_RESULT=UNPROVEN

NEXT_ONLY=COMPILE_AND_RUN_V03_THEN_READ_REAL_SIGMA_OUTPUT
```
