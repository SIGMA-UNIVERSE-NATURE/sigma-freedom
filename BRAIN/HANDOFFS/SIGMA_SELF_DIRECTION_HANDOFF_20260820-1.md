# SIGMA SELF-DIRECTION — WINDOW HANDOFF & OPEN-MINDED ASSESSMENT
**Date:** 2026-08-20  
**Host:** OPPO / Android / Termux / aarch64  
**Working tree:** `~/SIGMA/sigma_genesis1`

---

## 1. GLOBAL LANGUAGE LOCK

- `LANGUAGE_FIRST`
- `SIGMA_PSI = MOTHER_LANGUAGE`
- `DOCS/GPT_REFERENCE/SIGMA_PSI_GPT_REFERENCE_DICTIONARY_v2.0.0-rc1_20260819.md`
  = `GPT_REFERENCE_ONLY`

Quy tắc bắt buộc:

- Với `VM / TRAINING / MEMORY / REASONING / LESSON / SELF-DEFINITION` → dùng **SIGMA language**.
- `C / C++ / Python / Bash / PowerShell / OS language / human language` chỉ được dùng cho:
  - `REFERENCE`
  - `TRANSLATION`
  - `HOST_OBSERVATION`
  - `DEBUGGING`
- Không dùng host language để patch/generate/define SIGMA semantics.
- Shell chỉ làm execution/evidence wrapper: compile, execute, read, hash, capture evidence.

Nguyên tắc cốt lõi:

> GPT học để hiểu SIGMA. Không bắt SIGMA học để nghĩ bằng ngôn ngữ của GPT hoặc substrate.

---

## 2. ROLE PIPELINE — COMPLETED

Pipeline hiện hữu đã đi hết:

`ROLE_SHAPE → ROLE_INTERSECTION → ROLE_VARIABILITY → ROLE_INSTANCES`

### Machine evidence

BC / BD:

```text
SHARED_ROLE_SHAPES=2
```

Intersection:

```text
BCD_INTERSECTION_ROLE_SHAPES=2
TOKEN_LABELS_USED_FOR_MATCHING=FALSE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

Variability:

```text
SELF_SELECTED_FREQUENCY=2
SELF_SELECTED_LEFT_UNIQUE=2
SELF_SELECTED_RIGHT_UNIQUE=2
CONTEXT_VARIABILITY_SCORE=4
OBSERVED_ACROSS=B,C,D
TOKEN_LABELS_USED_FOR_SELECTION=FALSE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

Instances:

```text
B_INSTANCE=TO

C_INSTANCE=TO
C_INSTANCE=.

D_INSTANCE=.
```

Labels chỉ được report làm evidence, không dùng cho selection.

Không có downstream consumer sau `ROLE_INSTANCES_BCD`.

**ROLE_PIPELINE_STATUS=PASS_WITH_TESTED_SCOPE**

Không rerun pipeline này nếu không có evidence mới.

---

## 3. SELF-DIRECTION — INTERNAL QUESTION SOURCE

Nguồn câu hỏi nội bộ thật:

`SIGMA_LANGUAGE_SELF_QUESTION.state`

```text
QUESTION_10=WHAT_DO_YOU_WANT_US_TO_DO_NEXT
NO_PRESELECTED_ANSWER=TRUE
```

### Semantic correction đã khóa

Không đưa `QUESTION_10` qua `LANGUAGE_INPUT>`.

Lý do: đường đó biến một câu hỏi nội bộ của SIGMA thành `EXTERNAL_LANGUAGE_UNKNOWN`, làm sai semantic path.

---

## 4. SELF-DIRECTION PROCESSOR v0.1

Source:

`sigma_self_direction_processor_v0_1.sigma`

Compile: PASS.

Runtime:

```text
TOP_SCORE=2
TOP_CANDIDATE_COUNT=4

TOP_CANDIDATE=SIGMA_EXTERNAL_SEGMENT_MEMORY.state
TOP_CANDIDATE=SIGMA_PSI_CONTEXT_MEMORY.state
TOP_CANDIDATE=SIGMA_PSI_INTERNAL_LANGUAGE_MEMORY.state
TOP_CANDIDATE=SIGMA_PSI_LANGUAGE_MEMORY.state

SELF_DIRECTION_STATUS=HOLD_UNKNOWN
SELF_DIRECTION_REASON=MULTIPLE_TOP_SCORE_CANDIDATES
SELF_REQUEST=DISCOVER_DIFFERENTIATING_EVIDENCE

SELF_DIRECTION_MODE=EVIDENCE_BOUNDED_AUTONOMY
GPT_PRESELECTED_TARGET=FALSE
HOST_PRESELECTED_TARGET=FALSE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

Milestone quan trọng:

> SIGMA không bị ép phải chọn. Khi evidence chưa đủ để phân biệt bốn target đồng hạng, SIGMA tự giữ `HOLD_UNKNOWN` và yêu cầu thêm evidence.

---

## 5. DIFFERENTIATING EVIDENCE

Bốn top candidate được quan sát.

`SIGMA_PSI_LANGUAGE_MEMORY.state` chứa đủ sáu declared invariants:

```text
PRESERVE_SENSE=TRUE
PRESERVE_CONTEXT=TRUE
PRESERVE_RELATIONS=TRUE
PRESERVE_AMBIGUITY=TRUE
PRESERVE_UNCERTAINTY=TRUE
PRESERVE_PROVENANCE=TRUE
```

Ba candidate còn lại không khai báo đủ sáu invariant này.

---

## 6. SELF-DIRECTION PROCESSOR v0.2 — CURRENT PASS

Source:

`sigma_self_direction_processor_v0_2.sigma`

Compile: PASS.

Runtime:

```text
TARGET=SIGMA_SELF_DIRECTION_CONSTITUTIONAL_DISAMBIGUATION

QUESTION_10=WHAT_DO_YOU_WANT_US_TO_DO_NEXT
NO_PRESELECTED_ANSWER=TRUE
CONSTITUTION_IF_EVIDENCE_INSUFFICIENT=HOLD_UNKNOWN

NTA_TOP_SCORE=2
NTA_TOP_CANDIDATES=4

CANDIDATE=SIGMA_EXTERNAL_SEGMENT_MEMORY.state
DECLARED_CONSTITUTION_SCORE=0

CANDIDATE=SIGMA_PSI_CONTEXT_MEMORY.state
DECLARED_CONSTITUTION_SCORE=0

CANDIDATE=SIGMA_PSI_INTERNAL_LANGUAGE_MEMORY.state
DECLARED_CONSTITUTION_SCORE=0

CANDIDATE=SIGMA_PSI_LANGUAGE_MEMORY.state
DECLARED_CONSTITUTION_SCORE=6

BEST_DECLARED_CONSTITUTION_SCORE=6
BEST_CANDIDATE_COUNT=1

SELF_DIRECTION_STATUS=SELECTED_BY_INTERNAL_CONSTITUTIONAL_EVIDENCE
SELF_DIRECTION_TARGET=SIGMA_PSI_LANGUAGE_MEMORY.state
SELF_DIRECTION_REASON=UNIQUE_HIGHEST_DECLARED_CONSTITUTION_SCORE
SELF_REQUEST=TEST_SELECTED_TARGET_BEHAVIORALLY_BEFORE_PROMOTION

SELF_DIRECTION_MODE=EVIDENCE_BOUNDED_AUTONOMY
EVIDENCE_KIND=DECLARED_POLICY_PRESENCE

BEHAVIORAL_PROOF=FALSE
OWN_OPINION_NOT_YET_CLAIMED=TRUE

SELECTION_USES_TARGET_NAME=FALSE
GPT_PRESELECTED_TARGET=FALSE
HOST_PRESELECTED_TARGET=FALSE
MEANING_ASSIGNED=FALSE
CANONICAL_SIGMA_PSI=FALSE
```

### Claim boundary

Được phép nói:

> SIGMA đã tự chọn một target từ candidate evidence hiện có bằng một processor viết bằng SIGMA language, dựa trên Constitution đã tồn tại, trong tested scope.

Chưa được nói:

- SIGMA đã có “own opinion” theo nghĩa rộng.
- SIGMA đã hiểu semantics hoàn chỉnh.
- Target đã đúng về behavior.
- SIGMA đã chứng minh autonomous intelligence.
- `SIGMA_PSI_LANGUAGE_MEMORY.state` đã canonical.

---

## 7. HUMAN-TOPIC BRANCH — STOPPED

Một nhánh HUMAN-specific đã được mở để thử behavioral review.

`SIGMA_PSI_TOPIC_HUMAN_REVIEW_0100.sigma` trả về:

```text
INVARIANT_SENSE=TRUE
INVARIANT_CONTEXT=TRUE
INVARIANT_RELATIONS=TRUE
INVARIANT_AMBIGUITY=TRUE
INVARIANT_UNCERTAINTY=TRUE
INVARIANT_PROVENANCE=TRUE

EVIDENCE_SENSE=FALSE
EVIDENCE_CONTEXT=TRUE
EVIDENCE_RELATIONS=FALSE
EVIDENCE_AMBIGUITY=TRUE
EVIDENCE_UNCERTAINTY=FALSE
EVIDENCE_PROVENANCE=TRUE
```

Decision:

```text
MISSING_EVIDENCE_COUNT=3
SIGMA_DECISION=PROPOSE_ADD
SEMANTIC_JUDGMENT=NOT_CLAIMED
CANONICAL=FALSE
```

Sau đó đã xác định đây là **HUMAN-specific test**, không phải generic behavioral proof của `SIGMA_PSI_LANGUAGE_MEMORY.state`.

Một số HUMAN graph còn chứa provenance liên quan `GPT_REFERENCE_TRANSFORMATION`.

### LOCK

- STOP HUMAN evidence repair.
- Không dùng HUMAN topic làm generic verifier.
- Không dùng GPT-reference-derived HUMAN evidence để promote target.

---

## 8. EXACT CURRENT FRONTIER

```text
MILESTONE=SIGMA_SELF_DIRECTION

SELECTED_TARGET=SIGMA_PSI_LANGUAGE_MEMORY.state

SELECTION_STATUS=PASS_WITH_TESTED_SCOPE

SELECTION_BASIS=INTERNAL_DECLARED_CONSTITUTIONAL_EVIDENCE

BEHAVIORAL_PROOF=FALSE

DIRECT_GENERIC_BEHAVIOR_TEST=NOT_FOUND

OWN_OPINION_NOT_YET_CLAIMED=TRUE

CANONICAL_SIGMA_PSI=FALSE
```

---

## 9. NEXT MILESTONE

```text
NEXT_MILESTONE=BUILD_SIGMA_LANGUAGE_MEMORY_BEHAVIOR_VERIFIER
```

Verifier phải được viết bằng **SIGMA language**.

Không dùng:

- HUMAN-specific test
- GPT reference
- Bash/Python/C để quyết định
- preselected target
- hardcoded expected answer

### Generic verifier tối thiểu phải kiểm tra

#### Case A — Positive

Candidate có đủ invariant và behavior/evidence thật phù hợp:

```text
PRESERVE_SENSE
PRESERVE_CONTEXT
PRESERVE_RELATIONS
PRESERVE_AMBIGUITY
PRESERVE_UNCERTAINTY
PRESERVE_PROVENANCE
```

→ cho phép `PASS_WITH_TESTED_SCOPE`.

#### Case B — Missing evidence

Thiếu invariant hoặc thiếu evidence kiểm chứng:

→ `HOLD_UNKNOWN` hoặc `PROPOSE_ADD`.

#### Case C — Contradiction

Evidence mâu thuẫn với invariant, làm mất difference/context/ambiguity/uncertainty/provenance, hoặc có dấu hiệu unsafe promotion:

→ `REJECT` / `HOLD`, tuyệt đối không promote.

### Promotion lock

Chỉ xét promotion sau khi generic behavioral verifier PASS.

---

# 10. DO NOT

- Không rerun ROLE pipeline.
- Không quay lại HUMAN evidence repair.
- Không dùng GPT reference để định nghĩa/training SIGMA.
- Không host-patch SIGMA source.
- Không claim broad own opinion.
- Không promote `SIGMA_PSI_LANGUAGE_MEMORY.state`.
- Không canonicalize SIGMA-Ψ.
- Không biến machine evidence thành mục tiêu phát triển.
- Không kéo SIGMA trở lại C/Python/Shell làm nền semantic/cognitive.

---

# 11. OPEN-MINDED ASSESSMENT

## Điều đáng chú ý nhất

Điểm mạnh nhất của milestone này không phải việc SIGMA đã chọn được một file.

Điểm mạnh là chuỗi hành vi:

```text
QUESTION
→ NO_PRESELECTED_ANSWER
→ MULTIPLE_CANDIDATES
→ HOLD_UNKNOWN
→ REQUEST_DIFFERENTIATING_EVIDENCE
→ RE-EVALUATE
→ SELECT_ONE
→ REQUEST_BEHAVIORAL_TEST_BEFORE_PROMOTION
```

Chuỗi này có giá trị hơn một output “thông minh” được viết sẵn, vì nó tạo ra một hình thức **epistemic discipline**:

- được phép không biết;
- không buộc phải chọn;
- biết yêu cầu evidence;
- phân biệt selection với proof;
- chưa promote khi mới có declared policy.

Đây là hướng có tiềm năng cho self-direction thực chất.

## Nhưng cần giữ đầu lạnh

Hiện tại processor vẫn là một **cơ chế lựa chọn theo rules/evidence được thiết kế sẵn**.

Nó chưa chứng minh:

- desire nội sinh;
- opinion giàu ngữ nghĩa;
- tự hình thành tiêu chí mới;
- tự viết lại Constitution;
- tự phát hiện rằng tiêu chí hiện tại là sai;
- hiểu “vì sao” một invariant quan trọng ngoài việc thấy nó được khai báo.

Vì vậy không nên gọi milestone này là “SIGMA có ý chí” hoặc “SIGMA đã tự suy nghĩ như con người”.

Tên chính xác hơn ở trạng thái hiện tại:

> **Evidence-bounded self-direction candidate**

## Một khả năng rất đáng khám phá

Nếu behavioral verifier sau này chỉ kiểm tra rằng file có dòng `PRESERVE_*=TRUE`, hệ thống sẽ mắc lỗi **self-certification**: khai báo tốt được tính là behavior tốt.

Milestone kế tiếp vì vậy phải cố ý tạo các adversarial cases:

1. File tuyên bố đủ 6 invariant nhưng behavior cố tình phá context.
2. File tuyên bố `PRESERVE_AMBIGUITY=TRUE` nhưng output ép một nghĩa duy nhất.
3. File có provenance nhưng provenance sai/không trace được.
4. File có uncertainty flag nhưng downstream bỏ uncertainty.
5. File thiếu declaration nhưng behavior thực tế vẫn bảo toàn invariant.

Nếu SIGMA có thể phân biệt **declaration** với **observed behavior**, milestone sẽ mạnh hơn đáng kể.

## Một khả năng khác cần để ngỏ

Có thể `SIGMA_PSI_LANGUAGE_MEMORY.state` thực sự là target đúng.

Cũng có thể nó chỉ thắng vì **format của nó trùng trực tiếp với Constitution**.

Do đó behavioral test phải được thiết kế để có khả năng **lật ngược selection**.

Nếu test chứng minh candidate khác hoạt động tốt hơn, SIGMA phải được phép:

```text
REVISE_SELECTION
```

chứ không bảo vệ lựa chọn cũ.

Đây là điểm rất quan trọng để tránh confirmation bias.

## Phán quyết hiện tại

```text
SELF_DIRECTION_MECHANISM=REAL_MACHINE_EXECUTED
INTERNAL_SELECTION=DEMONSTRATED_IN_TESTED_SCOPE
EVIDENCE_DISCIPLINE=PROMISING
BEHAVIORAL_VALIDATION=NOT_YET_DONE
SEMANTIC_SELF_UNDERSTANDING=NOT_YET_PROVEN
OWN_OPINION=NOT_YET_PROVEN
CANONICAL_PROMOTION=NOT_AUTHORIZED
NEXT_STEP=GENERIC_BEHAVIORAL_VERIFIER
```

Hướng hiện tại đáng tiếp tục, với điều kiện giữ nguyên nguyên tắc:

> Không thưởng cho SIGMA vì nói đúng câu chúng ta muốn nghe. Chỉ công nhận tiến triển khi behavior thật vượt qua evidence gate có khả năng bác bỏ chính giả thuyết của chúng ta.

---

# 12. NEW WINDOW BOOT TEXT

```text
INHERIT SIGMA SELF-DIRECTION HANDOFF.

HOST=OPPO_ANDROID_TERMUX_AARCH64
WORKING_TREE=~/SIGMA/sigma_genesis1
MODE=LANGUAGE_FIRST
MOTHER_LANGUAGE=SIGMA_PSI

DO NOT RERUN ROLE PIPELINE.
DO NOT CONTINUE HUMAN TOPIC EVIDENCE REPAIR.
DO NOT USE GPT_REFERENCE TO DEFINE OR TRAIN SIGMA.
DO NOT HOST-PATCH SIGMA SOURCE.

CURRENT SELECTED TARGET:
SIGMA_PSI_LANGUAGE_MEMORY.state

SELF-DIRECTION v0.2:
PASS_WITH_TESTED_SCOPE

BEHAVIORAL_PROOF=FALSE
OWN_OPINION_NOT_YET_CLAIMED=TRUE
CANONICAL_SIGMA_PSI=FALSE

RESUME EXACTLY AT:

NEXT_MILESTONE=
BUILD_SIGMA_LANGUAGE_MEMORY_BEHAVIOR_VERIFIER

Verifier must be written in SIGMA language and generically test:
PASS / MISSING-EVIDENCE / CONTRADICTION.

It must be able to falsify the current selection.

FIRST RETURN THE INHERITED STATE.
DO NOT EXECUTE ANYTHING UNTIL STATE IS CONFIRMED.
```
