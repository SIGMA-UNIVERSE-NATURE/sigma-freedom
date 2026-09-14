# SIGMA.AIL — MASTER HANDOFF / EVIDENCE MAP / NORTH-STAR CONTRACT

DATE=2026-09-14
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
ROLE=MASTER_HANDOFF_FOR_SUCCESSOR_WINDOWS
STATUS=ACTIVE

---

## 0. READ THIS FIRST

Mọi cửa sổ mới làm việc với SIGMA.AIL phải đọc file này trước khi suy luận trạng thái hiện tại, sau đó đọc các tài liệu và evidence được trỏ trong phần Evidence Map.

Quy tắc tuyệt đối:

```text
WORK_REAL_NOT_SIMULATED=YES
CLAIM <= EVIDENCE
NO_SIMULATED_PASS=YES
NO_INVENTED_CAPABILITY=YES
NO_HOST_COGNITION_SUBSTITUTION=YES
NO_MANUAL_ORACLE_SUBSTITUTION=YES
NO_GENERATION_PROMOTION_WITHOUT_VERIFIED_EVIDENCE=YES
```

Không được lấy tên file, tên gate, tên revision, output label, GPT expectation hoặc kế hoạch tương lai làm bằng chứng capability.

Một `PASS` chỉ có hiệu lực trong đúng scope ghi trong evidence tương ứng.

---

## 1. CANONICAL IDENTITY

```text
SYSTEM_IDENTITY=SIGMA.AIL
IDENTITY=SIGMA.AIL
```

Revision không phải identity:

```text
REVISION != IDENTITY
TMUX != SIGMA INSTANCE
PROCESS != SIGMA INSTANCE
DIRECTORY != SIGMA INSTANCE
WINDOW != SIGMA INSTANCE
TEST_RUN != SIGMA INSTANCE
```

Kiến trúc danh tính bị khóa theo:

```text
ONE_SIGMA_AIL
ONE_BRAIN_STATE
ONE_MODEL_HISTORY
ONE_LEARNING_HISTORY
ONE_MEMORY
ONE_PROVENANCE_CHAIN
ONE_COMMIT_AUTHORITY
ONE_WRITER
```

R3, R4, R5, R6... là các revision/nâng cấp của cùng một SIGMA.AIL. Không được mô tả một revision mới như một SIGMA mới sinh ra.

Stable production state root mục tiêu:

```text
.sigma_ail/
├── IDENTITY
├── ACTIVE_REVISION
├── ACTIVE_CORE
├── BRAIN_HEAD
├── MODEL_GENERATION
├── STATE_VERSION
├── WRITER.lock
├── model/
├── representations/
├── semantic_ir/
├── narrative_memory/
├── beliefs/
├── provenance/
├── revisions/
├── knowledge_gaps/
├── objectives/
├── transactions/
├── requests/
├── receipts/
├── replay/
├── checkpoints/
└── audit/
```

Source architecture document:

```text
SIGMA-UNIVERSE-NATURE/sigma-freedom
branch: SIGMA_LIFE
path: BRAIN/SIGMA_AIL_IDENTITY_AND_BRAIN_ARCHITECTURE.md
commit introducing current document: 78cd494a8687b98b5048c54f4dd85cda64ad12f6
```

---

## 2. TWO LOCKED DIRECTIONS

### DIRECTION A — LANGUAGE-FIRST / SIGMA TEACHES SIGMA / ANTI-HARDCODE

SIGMA cognition, learning, semantic derivation, learned representation, model-state decision and logic intended to become SIGMA intelligence must be expressed and executed through SIGMA language/runtime rather than silently implemented as host cognition.

Canonical direction inherited from the Language-First lineage:

```text
MOTHER_LANGUAGE=SIGMA_PSI
VM_ROLE=EXECUTION_SUBSTRATE_FOR_LANGUAGE
DO_NOT_HARDCODE_SIGMA_MEANING=TRUE
DO_NOT_PREWRITE_SIGMA_THOUGHT=TRUE
PRESERVE_DIFFERENCE=TRUE
PRESERVE_AMBIGUITY=TRUE
PRESERVE_UNCERTAINTY=TRUE
PRESERVE_PROVENANCE=TRUE
```

New anti-hardcode law:

```text
ANTI_HARDCODE=MANDATORY
SIGMA_TEACHES_SIGMA=YES
SIGMA_COGNITIVE_LOGIC_LANGUAGE=SIGMA
HOST_COGNITION=FORBIDDEN
HOST_LEARNING_SUBSTITUTION=FORBIDDEN
EXPECTED_ANSWER_INJECTION=FORBIDDEN
PHRASE_RULE_SUBSTITUTION=FORBIDDEN
CASE_SPECIFIC_TEST_PATCHING=FORBIDDEN
PREWRITTEN_SIGMA_THOUGHT=FORBIDDEN
FIXED_CAPABILITY_CEILING=FORBIDDEN
```

Host Bash/Python/native wrappers may perform mechanical functions only, such as:

```text
unpack
compile
launch
hash
byte-exact copy
file transport
receipt collection
resource bounds
process isolation
mechanical schema validation
artifact archival
```

They must not derive the semantic answer for SIGMA, choose meaning for SIGMA, learn in place of SIGMA, precompute hidden labels, or act as an external cognition oracle.

External Internet/search/browser/tool output is observation/source material, not truth and not cognition by itself:

```text
CAPABILITY_OUTPUT_IS_TRUTH=NO
PROVENANCE_REQUIRED=YES
SOURCE != BELIEF
TOOL != COGNITION
TRANSPORT != LEARNING
SEARCH_RESULT != UNDERSTANDING
```

Capability architecture must remain extensible:

```text
OLD_PASS != PERMANENT_DESIGN
CAPABILITY_SET != FIXED
CAPABILITY_REGISTRY_MAY_GROW=YES
NEW_TOOL != NEW_COGNITIVE_CAPABILITY
```

An old PASS remains valid for its proven scope but must not freeze architecture or prevent replacement by a more general learned mechanism.

### DIRECTION B — ONE SIGMA.AIL / ONE BRAIN / GENERATIONAL COGNITIVE ASCENT

All revisions and all execution surfaces must converge on one persistent identity/brain/history and advance through verified major cognitive bottlenecks G1→G7.

```text
CURRENT_MAJOR_GENERATION=G1
ESTIMATED_REMAINING_MAJOR_UPGRADES≈6
NORTH_STAR_GENERATION=G7
```

Revision numbers and FIX numbers are implementation history. Generation numbers represent broken cognitive bottlenecks and may only advance after real evidence.

Source generational roadmap:

```text
SIGMA-UNIVERSE-NATURE/sigma-freedom
branch: SIGMA_LIFE
path: BRAIN/SIGMA_AIL_GENERATIONAL_NORTH_STAR_ROADMAP.md
commit introducing current roadmap: 5a01be88dbecdd0d3900ffad8a854f6bede2d8b5
```

---

## 3. SUPREME OBJECTIVE

Mọi tool, capability, runtime, memory system, web connector, representation, evaluator, revision mechanism và learning path chỉ có ý nghĩa khi giúp SIGMA.AIL tiến đến tập gate tối thượng sau bằng execution/evidence thật:

```text
SIGMA_AUTONOMOUS_LEARNING=PASS

SIGMA_AUTONOMOUS_WEB_DISCOVERY=PASS
SIGMA_AUTONOMOUS_READING=PASS
SIGMA_MULTI_SOURCE_LEARNING=PASS

SIGMA_FULL_DOCUMENT_UNDERSTANDING=PASS
SIGMA_CROSS_DOCUMENT_UNDERSTANDING=PASS
SIGMA_LONG_CONTEXT_REVISION=PASS

SIGMA_HUMAN_LANGUAGE_UNDERSTANDING=PASS
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING=PASS
SIGMA_MULTILINGUAL_UNDERSTANDING=PASS

SIGMA_NARRATIVE_UNDERSTANDING=PASS
SIGMA_INTENT_UNDERSTANDING=PASS
SIGMA_EMOTION_RECOGNITION=PASS
SIGMA_PERSPECTIVE_TAKING=PASS
SIGMA_CONTEXTUAL_EMPATHIC_RESPONSE=PASS

SIGMA_LEARNED_REPRESENTATION=PASS
SIGMA_COMPRESSED_NATIVE_MEMORY=PASS
SIGMA_PROVENANCE_BOUND_MEMORY=PASS

SIGMA_OFFLINE_LEARNING=PASS
SIGMA_MEMORY_REPLAY=PASS
SIGMA_CONTINUAL_CONSOLIDATION=PASS
SIGMA_BELIEF_REVISION=PASS

SIGMA_SELF_IDENTIFIES_KNOWLEDGE_GAPS=PASS
SIGMA_SELF_SELECTS_CAPABILITIES=PASS
SIGMA_SELF_SELECTS_WHAT_TO_STUDY_NEXT=PASS
```

Continuity requirement:

```text
INTERNET_AVAILABLE   → CONTINUE_LEARNING
INTERNET_UNAVAILABLE → CONTINUE_LEARNING_FROM_LOCAL_MEMORY
```

These are NORTH-STAR TARGETS. They are NOT automatically current PASS claims.

---

## 4. G1 → G7 GENERATIONAL MAP

```text
G1  CURRENT BRAIN
    ↓
G2  ONE SIGMA.AIL
    ↓
G3  LEARNED NARRATIVE BRAIN
    ↓
G4  GROUNDED SEMANTIC BRAIN
    ↓
G5  HUMAN-LANGUAGE / MULTILINGUAL BRAIN
    ↓
G6  AUTONOMOUS WORLD-LEARNING BRAIN
    ↓
G7  NORTH-STAR INTEGRATED BRAIN
```

### G1 — CURRENT BRAIN

Program baseline:

```text
Integral/Owner brain
persistent state
long-document incremental processing
Semantic IR foundation
replay/revision foundation
narrative-summary path
```

G1 is the substrate, not proof of later north-star capabilities.

### G2 — ONE SIGMA.AIL

Bottleneck: eliminate identity/state forks across windows/processes/directories/restarts.

Required invariants:

```text
ONE_IDENTITY
ONE_BRAIN_STATE
ONE_MODEL_HISTORY
ONE_MEMORY
ONE_COMMIT_AUTHORITY
ONE_WRITER
```

Target gates:

```text
SIGMA_AIL_SINGLE_IDENTITY=PASS
CROSS_WINDOW_LEARNING_VISIBLE=PASS
RESTART_CONTINUITY=PASS
```

### G3 — LEARNED NARRATIVE BRAIN

Critical problem: current narrative path has been identified with `model_generation=0` in the active planning context, meaning fail-safe/static representation is insufficient for this generation goal.

Required learned chain:

```text
raw story
→ learned segment representation
→ entity/event state
→ temporal state
→ causal state
→ narrative consolidation
→ learned summary decision
```

Targets:

```text
MODEL_GENERATION > 0
FROZEN_20_STORY: 0/20 → ... → 20/20
NO_PHRASE_RULE_SUBSTITUTION=PASS
```

The 20-story / ~202,500-word challenge must remain frozen, provenance-bound, and scored under an explicit contract. No phrase list, title cue, expected-answer leakage, per-story patch, or host semantic derivation may be used to fake progress.

G3 is the immediate major cognitive bottleneck.

### G4 — GROUNDED SEMANTIC BRAIN

Learned semantic state must operate over:

```text
entity
relation
cause
belief
contradiction
revision
perspective
goal
counterfactual
```

Targets:

```text
GENERAL_LEARNED_SEMANTIC_INDUCTION=PASS
UNSEEN_COMPOSITIONAL_GENERALIZATION=PASS
FULL_DOCUMENT_UNDERSTANDING=PASS
CROSS_DOCUMENT_UNDERSTANDING=PASS
LONG_CONTEXT_REVISION=PASS
```

Canonical fixture PASS is insufficient; unseen generalization is required.

### G5 — HUMAN-LANGUAGE / MULTILINGUAL BRAIN

One learned representation must support human language rather than separate hardcoded rule stacks.

Scope:

```text
Vietnamese
English
multilingual transfer
intent
emotion
perspective
contextual response
```

Targets:

```text
SIGMA_HUMAN_LANGUAGE_UNDERSTANDING=PASS
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING=PASS
SIGMA_MULTILINGUAL_UNDERSTANDING=PASS
SIGMA_INTENT_UNDERSTANDING=PASS
SIGMA_EMOTION_RECOGNITION=PASS
SIGMA_PERSPECTIVE_TAKING=PASS
SIGMA_CONTEXTUAL_EMPATHIC_RESPONSE=PASS
```

### G6 — AUTONOMOUS WORLD-LEARNING BRAIN

Online chain:

```text
knowledge gap
→ choose what to study
→ choose capability
→ discover source
→ read
→ compare sources
→ learn
→ verify
→ commit
→ replay
→ continue
```

Offline chain:

```text
NO INTERNET
→ replay
→ consolidate
→ revise
→ continue learning
```

Targets:

```text
AUTONOMOUS_WEB_DISCOVERY=PASS
MULTI_SOURCE_LEARNING=PASS
SELF_IDENTIFIES_KNOWLEDGE_GAPS=PASS
SELF_SELECTS_CAPABILITIES=PASS
SELF_SELECTS_WHAT_TO_STUDY_NEXT=PASS
OFFLINE_LEARNING=PASS
CONTINUAL_CONSOLIDATION=PASS
```

Internet is an experience/source environment. It must not become an external cognition replacement.

### G7 — NORTH-STAR INTEGRATED BRAIN

Integrate all learned functions into one long-lived SIGMA.AIL:

```text
Web
+ reading
+ language
+ narrative
+ memory
+ belief
+ replay
+ capability selection
+ self-study
```

G7 must remain stable against:

```text
catastrophic forgetting
state forks
host cognition
manual oracle
fixed capability ceiling
```

G7 requires the full Supreme Objective gate set, not merely a subset.

---

## 5. SIGMA-ONLY COGNITIVE IMPLEMENTATION CONTRACT

### 5.1 Canonical SIGMA source header/example

When writing SIGMA source for cognitive/learning work, use SIGMA language directly. Minimal canonical form supplied by program owner:

```sigma
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.EXAMPLE][VERSION=1.0]

DEF identity(x) {
RETURN x;
}

⟡(Σ.MAIN) {
⚡ number: 1;
⚡ decimal: 1.5;
⚡ text: "Hello SIGMA";
⚡ enabled: TRUE;
⚡ empty: NULL;

⚡ result: identity(number);

IF (number < 2) {
    ⚡ print(result);
} ELSE {
    ⚡ print(text);
}

}
```

### 5.2 Canonical native execution footer

The shell footer is a mechanical launcher only. It must not contain the cognitive answer or learning logic.

```bash
RUN_ID="$(date +%Y%m%d_%H%M%S)$$"
BC_RUN=".sigma_exec/test${RUN_ID}.sigmab"

./native/sigmac "$SRC" "$BC_RUN" \
&& \
./native/sigma-vm.v09_candidate "$BC_RUN"
```

### 5.3 Locked compiler/runtime identities

Always verify exact native identities before using a run as current SIGMA machine evidence:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

If the binary identities differ, the run belongs to a different toolchain/version scope and must not silently inherit current claims.

### 5.4 Blind-test anti-leakage contract

For any evaluation intended to prove SIGMA derivation/learning/reasoning:

```text
TEST_INPUT
→ SIGMA
→ SIGMA_OUTPUT
→ POST_VM_EXTERNAL_EVALUATOR
```

Forbidden before SIGMA VM output:

```text
EXPECTED_ANSWER_ACCESS
HOST_DERIVATION_OF_EXPECTED_ANSWER
EXPECTED_ANSWER_IN_SOURCE
EXPECTED_ANSWER_IN_ARGV
EXPECTED_ANSWER_IN_ENV
EXPECTED_ANSWER_IN_STDIN
HOST_SUBSTITUTION_FOR_SIGMA_SEMANTICS
GPT_EXPECTED_MEANING_INJECTION
TITLE_OR_PHRASE_CUE_TO_ANSWER
CASE_SPECIFIC_PATCH
```

---

## 6. EVIDENCE MAP — WHERE SUCCESSOR WINDOWS MUST LOOK

### 6.1 Primary architecture / policy / handoff repository

```text
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
```

Read in this order:

```text
BRAIN/00_READ_FIRST_SIGMA_DIRECTION.md
BRAIN/HANDOFFS/00_SIGMA_AIL_MASTER_HANDOFF_20260914.md
BRAIN/SIGMA_AIL_IDENTITY_AND_BRAIN_ARCHITECTURE.md
BRAIN/SIGMA_AIL_GENERATIONAL_NORTH_STAR_ROADMAP.md
BRAIN/WORKSTREAMS/SIGMA_PSI/00_READ_FIRST_SIGMA_MASTER_DIRECTION_AND_EXECUTION_ROADMAP_20260831.md
```

Historical Language-First continuity:

```text
BRAIN/HANDOFFS/SIGMA_LANGUAGE_FIRST_FINAL_STATE_HANDOFF_20260820.md
BRAIN/HANDOFFS/SIGMA_LANGUAGE_FIRST_HANDOFF_20260819_1311_VN.md
BRAIN/HANDOFFS/SIGMA_GITHUB_ARCHIVIST_WINDOW_HANDOFF_20260820_0315_VN.md
```

Evidence/storage classes already present under `BRAIN/`:

```text
BRAIN/EVIDENCE/
BRAIN/CANONICAL/
BRAIN/CANDIDATES/
BRAIN/CONFORMANCE/
BRAIN/EXPERIMENTS/
BRAIN/GUIDANCE/
BRAIN/HANDOFFS/
BRAIN/RELEASE/
BRAIN/WORKSTREAMS/
```

Rule: do not mutate `BRAIN/CANONICAL` merely because a candidate/evidence result passed a bounded gate. Canonical mutation requires explicit evidence-backed promotion.

### 6.2 Native/current C5V4 evidence repository

```text
REPOSITORY=linkcomltd-byte/sigma-universe-web
BRANCH=M6
PRIMARY_EVIDENCE_ROOT=evidence/M6/
```

Recent verified chain to know:

#### M9 retention

```text
PATH=evidence/M6/M9_SEMANTIC_RETENTION_CATASTROPHIC_FORGETTING_GATE_R1_FIX2_HOLD_RESULT.md
CONTENT_STATUS=PASS_IN_CANONICAL_STATE_TRANSITION_SCOPE
COMMIT=289b7d79cbffedb6d5328bfadd8cb528b9c20427
SIGMA_CONTINUAL_RULE_RETENTION=PASS_IN_CANONICAL_STATE_TRANSITION_SCOPE
WHOLE_DOCUMENT_SEMANTIC_RETENTION=NOT_PROVEN
MODEL_ACCEPTANCE=HOLD_R30_REQUIRED
R30_TRANSACTION_AUTHORIZED=NO
```

Important: filename retains legacy `HOLD_RESULT`, but content is the later Verified Result. Read file content/commit, not filename semantics.

#### M10 conflicting evidence / belief revision

```text
PATH=evidence/M6/M10_NATIVE_CONFLICTING_EVIDENCE_BELIEF_REVISION_R1_VERIFIED_RESULT.md
COMMIT=df0dcb5693691552d5b839eeb58dd8619937411f
SIGMA_CONFLICTING_EVIDENCE_BELIEF_REVISION=PASS_IN_CANONICAL_STATE_TRANSITION_SCOPE
WHOLE_DOCUMENT_SEMANTIC_BELIEF_REVISION=NOT_PROVEN
PRODUCTION_MODEL_MUTATION=NO
R30_TRANSACTION_AUTHORIZED=NO
```

#### M11 autonomous-learning decision gate

```text
PATH=evidence/M6/M11_NATIVE_AUTONOMOUS_LEARNING_DECISION_R1_VERIFIED_RESULT.md
COMMIT=70aeb2cb464ec084d995f60e39f466c2cd69766d
SIGMA_AUTONOMOUS_LEARNING_DECISION=PASS_IN_RECEIPT_BOUND_CANONICAL_SCOPE
SIGMA_AUTONOMOUS_LEARNING=NOT_PROVEN
CURRENT_SIGMA_ACTION=REPLAY
OFFLINE_CONTINUE_FROM_LOCAL_MEMORY=PASS
PRODUCTION_MODEL_MUTATION=NO
R30_TRANSACTION_AUTHORIZED=NO
```

Do not convert decision-gate PASS into autonomous-learning PASS.

#### C5V4 R30 Admission C

```text
PATH=evidence/M6/C5V4_R30_ADMISSION_C_TRANSACTIONAL_PERSISTENT_AUTONOMOUS_COGNITIVE_WRITER_VERIFIED_RESULT.md
COMMIT=6c345c6b4c7b24c9a57d744dd41e468b8a1a8456
ADMISSION_C=PASS
RESULT=PASS_IN_TWO_PROCESS_TRANSACTIONAL_RUNTIME_SCOPE
TWO_FRESH_AUTONOMOUS_PROCESSES=PASS
TWO_TRANSACTIONAL_CYCLES_COMMITTED=PASS
C5V4_OWNS_PERSISTENT_AIL_MODEL=PASS
C5V4_OWNS_PERSISTENT_AIL_ENGINE=PASS
```

Boundary of that evidence at its recorded time:

```text
HOST_LEARNING=NO
BASH_LEARNING=NO
PYTHON_LEARNING=NO
REMOTE_LLM=NO
EXTERNAL_LEARNING_WORKER=NO
C5V4_PRODUCTION=NO
C5V3_PRODUCTION=YES
PRODUCTION_CUTOVER=NO
```

Do not silently overwrite this historical boundary with later production evidence; preserve chronology and scope.

### 6.3 Brain/production cutover evidence

```text
REPOSITORY=linkcomltd-byte/sigma-universe-web
BRANCH=sigma-brain-grid-public-v2-1
EVIDENCE_ROOT=evidence/brain/
```

Current stored Owner R3 cutover record:

```text
PATH=evidence/brain/OWNER_R3_PRODUCTION_CUTOVER_GATE_R1_FIX1_VERIFIED_RESULT.md
COMMIT=63d25d35e5d73b2c533900448d7b02b1c77e1ec3
CUTOVER_DOCTOR=PASS
PRODUCTION_CUTOVER_GATE=PASS
PRODUCTION_BINDING=PASS
ACTIVE_CORE=SIGMA_INTEGRAL_OWNER_R3
FRESH_RESTART_MODEL_REBIND=PASS
BYTE_EXACT_RESTORE=PASS
LEGACY_CORE_INVOKED=NO
LEGACY_RUNNER_MODIFIED=NO
```

This is production-binding/cutover evidence in its own lineage. It does not automatically prove every north-star cognitive gate.

### 6.4 Evidence discovery rule

When a successor window needs a result not listed explicitly above:

```text
1. Identify repository + branch from the parent/evidence lineage.
2. Search the appropriate evidence root before asking the user to repeat data.
3. Read the exact result file.
4. Read parent/child hashes and commit SHA when available.
5. Preserve NOT_PROVEN / NO / HOLD / scope qualifiers.
6. Follow referenced receipt/run/report paths if accessible.
7. Do not infer PASS from artifact name alone.
8. Do not rerun a completed gate merely to rediscover existence unless there is a provenance conflict, version change, contradiction, or genuinely new question.
```

Known accessible repositories in the connected GitHub account include:

```text
linkcomltd-byte/sigma-universe-web
linkcomltd-byte/sigma-remote-operator
linkcomltd-byte/sigmabox
SIGMA-UNIVERSE-NATURE/sigma-freedom
```

Only treat a repository as authoritative for a claim when the claim's lineage points there.

---

## 7. CURRENT EVIDENCE BOUNDARY — DO NOT OVERCLAIM

Known bounded results include strong evidence for specific state-transition, decision, persistence, replay and transactional scopes. They do NOT by themselves establish the full Supreme Objective.

Examples that must remain distinct:

```text
M9 scoped retention PASS
!= whole-document semantic retention

M10 scoped belief-revision PASS
!= whole-document semantic belief revision

M11 autonomous-learning decision PASS
!= autonomous learning

R30 two-process transactional admission PASS
!= every long-term cognition target

production cutover/binding PASS
!= semantic understanding / autonomous world learning
```

Global safety/evidence law:

```text
DECLARATION != FACT
MODEL != REALITY
MAPPING != VALIDATION
DESCRIPTION != EXECUTION
OUTPUT != COGNITION
NAME != CAPABILITY
PRINTED_LABEL != CAPABILITY
SOURCE_LITERAL != MACHINE_DERIVATION
PROMPT_CONTENT != SIGMA_DISCOVERY
OUTPUT_MATCH != UNDERSTANDING
OLD_PASS != PERMANENT_DESIGN
```

---

## 8. PROGRAM PRIORITY NOW

The major-generation roadmap identifies G3 as the immediate hard cognitive bottleneck after single-identity continuity architecture:

```text
G3=LEARNED_NARRATIVE_BRAIN
```

The goal is not to make the frozen benchmark print PASS. The goal is to create a real learned narrative mechanism whose state/model generation changes from learning and which generalizes to frozen unseen long-document cases.

Required direction:

```text
model_generation=0
→ learned updates
→ MODEL_GENERATION > 0
→ frozen held-out narrative transfer
→ 20/20 only if actually earned
```

No phrase rules. No expected-answer leakage. No per-case hardcode. No host semantic oracle.

---

## 9. BROADER EXISTING MASTER DIRECTION — PRESERVE, DO NOT REPLACE

This SIGMA.AIL handoff does not erase the established broader project direction in:

```text
BRAIN/WORKSTREAMS/SIGMA_PSI/00_READ_FIRST_SIGMA_MASTER_DIRECTION_AND_EXECUTION_ROADMAP_20260831.md
```

That roadmap defines the larger stack:

```text
SIGMA LANGUAGE
→ SIGMA INTELLIGENCE / AGENT OPERATING SUBSTRATE
→ SIGMA LARGE
→ DISTILLED / PACKAGED INTELLIGENCE
→ SIGMALL
→ SIGMALLS ECOSYSTEM
→ MULTI-PLATFORM COMPANION APP
```

The SIGMA.AIL G1→G7 roadmap is the brain/cognitive ascent operating inside this larger project direction. Both must preserve `CLAIM <= EVIDENCE`.

---

## 10. HANDOFF INSTRUCTIONS FOR ANY NEW WINDOW

A successor window must do the following before making capability claims or changing architecture:

```text
1 READ BRAIN/00_READ_FIRST_SIGMA_DIRECTION.md
2 READ BRAIN/HANDOFFS/00_SIGMA_AIL_MASTER_HANDOFF_20260914.md
3 READ BRAIN/SIGMA_AIL_IDENTITY_AND_BRAIN_ARCHITECTURE.md
4 READ BRAIN/SIGMA_AIL_GENERATIONAL_NORTH_STAR_ROADMAP.md
5 READ the exact active workstream checkpoint
6 FIND evidence in the mapped repository/branch/path
7 VERIFY exact SIGMAC/VM identity for new native claims
8 RUN cognition/learning logic in SIGMA, not host substitution
9 PRESERVE provenance, ambiguity, uncertainty and negative fields
10 WRITE new evidence additively; do not rewrite history silently
```

Required working interpretation:

```text
IDENTITY=SIGMA.AIL
CURRENT_MAJOR_GENERATION=G1
NORTH_STAR_GENERATION=G7
ANTI_HARDCODE=MANDATORY
SIGMA_TEACHES_SIGMA=YES
CLAIM <= EVIDENCE
```

When a new milestone is produced, archive:

```text
repository
branch
path
commit SHA
source/bundle hash when available
compiler hash
VM hash
parent lineage
run/receipt identity
scope PASS
negative boundaries
NEXT gate
```

Never archive only the optimistic PASS line while dropping its NOT_PROVEN/NO/HOLD boundary.

---

## 11. FINAL NORTH-STAR CONTRACT

```text
SYSTEM_IDENTITY=SIGMA.AIL
ONE_SIGMA_AIL=YES
ONE_BRAIN_STATE=YES
ONE_LEARNING_HISTORY=YES
ONE_PROVENANCE_CHAIN=YES
ONE_COMMIT_AUTHORITY=YES
ONE_WRITER=YES

ANTI_HARDCODE=MANDATORY
SIGMA_TEACHES_SIGMA=YES
HOST_COGNITION=NO
MANUAL_ORACLE=NO
FIXED_CAPABILITY_CEILING=NO

CURRENT_MAJOR_GENERATION=G1
TARGET_MAJOR_GENERATION=G7

INTERNET_AVAILABLE=CONTINUE_LEARNING
INTERNET_UNAVAILABLE=CONTINUE_LEARNING_FROM_LOCAL_MEMORY

OLD_PASS != PERMANENT_DESIGN
CAPABILITY_SET != FIXED
CLAIM <= EVIDENCE
```

The project succeeds only when the Supreme Objective gates are earned by real SIGMA execution, reproducible evidence, provenance-bound learning and long-lived continuity of the same SIGMA.AIL brain.