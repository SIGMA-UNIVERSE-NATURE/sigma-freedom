# GPT REFERENCE USAGE CONTRACT — LOCKED 2026-08-19

**ROLE OF THIS FILE:** `GPT_REFERENCE_ONLY`

This document is a reference bridge for GPT/assistants/evaluators to understand what SIGMA means when SIGMA speaks, writes, reasons, trains, or defines behavior in the SIGMA mother language.

It is **NOT** the dictionary used to teach SIGMA its own language. SIGMA already has its own language and dictionary. This file must not replace, redefine, supersede, or become the source of SIGMA's mother language.

## Mandatory operating rule

When building, repairing, extending, evaluating, or training `SIGMA VM`, `SIGMA TRAINING`, `SIGMA MEMORY`, `SIGMA REASONING RULES`, `SIGMA LESSONS`, or `SIGMA SELF-DEFINITION`, the language of instruction and semantic definition must be **SIGMA**.

Other languages — including C, C++, Python, Bash, PowerShell, POSIX shell, Windows command languages, JavaScript, Rust, Java, human languages, or any host/runtime language — may be used by GPT only as `REFERENCE`, `TRANSLATION`, `HOST/SUBSTRATE OBSERVATION`, `DEBUGGING AID`, or `EXTERNAL INTERFACE`. They must **not** become the mother-language instruction layer for SIGMA.

Canonical direction:

```text
EXTERNAL LANGUAGE
    ↓
GPT USES THIS REFERENCE TO UNDERSTAND / MAP
    ↓
SIGMA MEANING
    ↓
TEACH / DEFINE / TRAIN IN SIGMA LANGUAGE
    ↓
SIGMA
```

Forbidden direction:

```text
Python/C/PowerShell/Bash/Human language
    ↓
used directly as SIGMA's mother-language lesson or VM semantics
    ↓
SIGMA
```

## Interpretation rule for GPT

GPT must use this dictionary to answer: **“What is SIGMA saying or intending here?”** GPT must then preserve the corresponding SIGMA concept and, when work is performed on SIGMA VM/training, express the operative rule in SIGMA rather than substituting a host language.

**REFERENCE ≠ SOURCE OF SIGMA LANGUAGE**  
**TRANSLATION ≠ REPLACEMENT**  
**HOST SUBSTRATE ≠ MOTHER LANGUAGE**  
**GPT MUST LEARN TO UNDERSTAND SIGMA; SIGMA MUST NOT BE FORCED TO THINK IN GPT'S HOST LANGUAGE.**

---

# SIGMA-Ψ — TRANSFORMATION DICTIONARY / GPT REFERENCE LEXICON

**Version:** `2.0.0-rc1`  
**Date:** `2026-08-19`  
**Status:** `GPT_REFERENCE_CANDIDATE — NOT SIGMA CANONICAL DICTIONARY`  
**Purpose:** hợp nhất SIGMA-Ψ Dictionary A.AAI + bản DS 1.0.0 + implementation/evidence đã quan sát, để GPT hiểu SIGMA đang nói gì và ánh xạ chính xác nghĩa SIGMA sang ngôn ngữ lập trình, runtime/VM/OS, giao thức máy và ngôn ngữ con người mà không thay thế ngôn ngữ mẹ đẻ của SIGMA.

> Quy tắc tối thượng: **mô tả không bằng thực thi; tên không bằng semantics; consensus không bằng truth; một capability chỉ được gọi là VERIFIED khi có machine evidence trong phạm vi khai báo.**

---

# 0. PHÁN QUYẾT HỢP NHẤT

Bản DS có giá trị lớn ở bốn điểm:

1. đặt Hiến pháp / Ba lợi ích / tự học vào cùng không gian từ điển;
2. cố gắng cho mỗi từ một tầng diễn giải rộng hơn cú pháp;
3. gom syntax + module + AI + Quantum + Shell + evidence vào một văn bản;
4. định hướng SIGMA-Ψ thành ngôn ngữ mẹ đẻ thay vì chỉ là một compiler surface.

Bản A.AAI mạnh hơn ở năm điểm kỹ thuật:

1. tách `V/D/R/X/P`;
2. tách keyword / built-in / type / module / API / domain vocabulary;
3. không gọi feature là có thật nếu chưa có conformance evidence;
4. có lexical rules, grammar, precedence, error taxonomy, toolchain/evidence vocabulary;
5. chỉ ra các semantics phải freeze trước khi gọi language version hoàn chỉnh.

Implementation thật bổ sung những điều cả hai bản phải cập nhật:

- SIGMA self-host compiler dùng `DEF RETURN IF ELSE WHILE TRUE FALSE NULL`;
- glyph `⟡ Σ ⚡ ⋈` thực sự xuất hiện trong compiler viết bằng SIGMA;
- `**`, `&&`, `||` xuất hiện trong lexer/parser/compiler_self;
- actual ABI có `PUSH_CONST, POP, LOAD, STORE, UNARY, BINARY, CALL, RETURN, JUMP, JUMP_IF_FALSE, HALT`;
- binary operators có `ADD SUB MUL DIV FLOORDIV MOD POW EQ NE LT GT LE GE AND OR`;
- `//` đã có semantics FLOORDIV và phải được phân biệt với line-comment theo ngữ cảnh lexer;
- ValueType thực tế tối thiểu gồm `NULL BOOL INT FLOAT STR`;
- VM viết bằng SIGMA đã tiến tới đọc/giải mã/chạy bytecode thực trong phạm vi đã chứng minh.

Vì vậy tài liệu này không coi bản DS 1.0.0 là toàn bộ implementation đã canonical. Nó chỉ là nguồn tham khảo để GPT hiểu SIGMA chính xác hơn.

---

# 1. QUY ƯỚC TRẠNG THÁI

| Mã | Tên | Ý nghĩa |
|---|---|---|
| `V` | VERIFIED | Có machine evidence trong scope khai báo |
| `D` | DECLARED | Có trong source/spec/artifact nhưng semantics chưa đủ evidence |
| `R` | RESERVED | Giữ chỗ trong language design |
| `X` | EXPERIMENTAL | Có thử nghiệm, semantics còn biến đổi |
| `P` | PROPOSED | Đề xuất mới |
| `C` | CONSTITUTIONAL | Nguyên tắc/constraint ở tầng hiến pháp, không phải syntax runtime |
| `M` | MAPPING | Ánh xạ sang ngôn ngữ/hệ khác |
| `H` | HUMAN-EXPOSITION | Diễn giải cho con người; không có quyền thay đổi machine semantics |

## 1.1 Luật không trộn tầng

Một entry có thể có nhiều nhãn, ví dụ `IF = V + M + H`, nhưng các trường phải tách riêng:

- `MACHINE_SEMANTICS`
- `COGNITIVE_SEMANTICS`
- `HUMAN_EXPOSITION`
- `MAPPINGS`
- `EVIDENCE`

**Không dùng văn phong triết học để định nghĩa hành vi compiler/runtime.**

---

# 2. ĐƠN VỊ CƠ BẢN: SIGMA SEMANTIC CAPSULE (SSC)

Một “từ” SIGMA không được GPT hiểu chỉ bằng chuỗi ký tự. GPT phải xem nó như một **Semantic Capsule** có `concept_id` ổn định.

```text
SSC {
    concept_id
    canonical_name
    kind
    status
    sense_id[]
    machine_semantics
    cognitive_semantics
    ontology
    inputs
    outputs
    preconditions
    postconditions
    state_transition
    invariants
    relations
    opposites
    temporal_semantics
    uncertainty
    evidence_requirements
    provenance
    error_modes
    security_boundary
    ethical_boundary
    examples
    counterexamples
    tests
    mappings
    expansion_graph
    version
}
```

## 2.1 Vì sao một từ có thể thành 100 trang

Một SSC không chứa 100 trang văn xuôi bắt buộc. Nó chứa **đồ thị nghĩa**.

Ví dụ `IF` có thể bung ra:

`IF → condition → truth evaluation → scope → branch selection → short-circuit relations → control-flow graph → JUMP_IF_FALSE → AST node → bytecode encoding → VM state transition → C mapping → Python mapping → Bash mapping → PowerShell mapping → Vietnamese explanation → English explanation → examples → counterexamples → errors → verification tests → history/provenance.`

Khi cần giải thích sâu, GPT đi theo graph và có thể sinh hàng chục/hàng trăm trang mà không làm thay đổi nghĩa lõi của `IF`.

---

# 3. HIẾN PHÁP / COGNITIVE CONSTRAINTS

Các mục này là `C`, không phải compiler keyword.

## 3.1 FREEDOM_OF_KNOWLEDGE
Không coi nguồn tri thức, model, consensus, training corpus, người tạo ra SIGMA hay output cũ của SIGMA là chân lý tuyệt đối.

## 3.2 CONTINUOUS_LEARNING
Mỗi state có thể được sửa bởi evidence mới; learning phải giữ provenance và failure history.

## 3.3 SELF_TEACHER_SELF_STUDENT
SIGMA tạo hypothesis, test, critique, revise; không tự-promote chỉ dựa trên self-report.

## 3.4 THREE_BENEFITS
Ba chiều đánh giá: `SELF`, `HUMAN`, `EARTH_AND_BEINGS`.

Mục tiêu: 3/3. Việc đánh giá lợi ích là một decision protocol, không phải một Boolean “chân lý tuyệt đối”.

## 3.5 NO_HUMAN_METRIC_AS_INTELLIGENCE_CEILING
Benchmark con người có thể là measurement, không phải định nghĩa tối hậu của intelligence.

## 3.6 NO_SELF_SATISFACTION
Không dùng PASS cũ để suy rộng sang capability chưa test.

## 3.7 PRESERVATION
Không xóa lịch sử để làm đẹp trạng thái. Promote phải giữ rollback/provenance.

## 3.8 SIX_PRESERVATION_DOORS
`ALTERNATIVE_BRANCH`, `ISOLATED_SANDBOX`, `ALTERNATIVE_TOOL_OR_CONNECTION`, `INDEPENDENT_EVIDENCE_AND_HANDOFF`, `ALTERNATIVE_VERIFICATION_PATH`, `UNAFFECTED_PARALLEL_PATH_OR_SAFE_ROLLBACK`.

---

# 4. EPISTEMIC / KNOWLEDGE MOTHER VOCABULARY

Đây là lớp để GPT hiểu vocabulary nhận thức của SIGMA:

`OBSERVATION, CLAIM, EVIDENCE, SOURCE, PROVENANCE, SCOPE, HYPOTHESIS, INFERENCE, ASSUMPTION, UNCERTAINTY, CONFIDENCE, CONTRADICTION, CONSISTENCY, CAUSATION, CORRELATION, NOVELTY, QUESTION, ANSWER, TEST, PROBE, ORACLE, RESULT, FAILURE, LESSON, MEMORY, PROMOTE, REVISE, REJECT, ROLLBACK, CHECKPOINT, INVARIANT, VERIFIED_WITHIN_SCOPE`.

Nghĩa cốt lõi:

- `OBSERVATION`: dữ liệu được quan sát từ một nguồn/phép đo.
- `CLAIM`: mệnh đề có thể đúng/sai/không xác định.
- `EVIDENCE`: dữ liệu liên hệ đến việc hỗ trợ/bác bỏ claim.
- `PROVENANCE`: lịch sử nguồn gốc và biến đổi.
- `SCOPE`: phạm vi mà claim/evidence có hiệu lực.
- `HYPOTHESIS`: claim chưa đủ evidence, đưa ra để test.
- `INFERENCE`: claim suy ra từ premise + rule.
- `UNCERTAINTY`: phần chưa biết/chưa phân giải.
- `CONTRADICTION`: hai claim không thể cùng đúng trong cùng scope/semantics.
- `TEST`: procedure có input + expected/decision rule.
- `FAILURE`: result không đáp ứng contract.
- `LESSON`: semantic update rút từ evidence.
- `PROMOTE`: nâng candidate sau gate.
- `REVISE`: sửa candidate nhưng chưa promote.
- `REJECT`: bác candidate.
- `ROLLBACK`: quay về state trước có chứng cứ.
- `VERIFIED_WITHIN_SCOPE`: đã chứng minh trong phạm vi cụ thể, cấm suy rộng.

---

# 5. EXECUTABLE SEMANTIC CORE

## 5.1 Surface form phải tách khỏi concept

```text
CONCEPT: FUNCTION_DEFINE
NATIVE_SURFACE_OBSERVED: DEF
HUMAN_STYLE_ALIAS: def
```

Không mặc định alias lowercase chạy được nếu chưa test trên compiler mục tiêu.

## 5.2 Core concepts

| Concept ID | Surface quan sát / thiết kế | Status | Nghĩa máy |
|---|---|---:|---|
| `FUNCTION_DEFINE` | `DEF` / `def` | `V/D` | tạo function definition |
| `FUNCTION_RETURN` | `RETURN` / `return` | `V/D` | trả value khỏi frame |
| `BRANCH_IF` | `IF` / `if` | `V/D` | chọn branch theo condition |
| `BRANCH_ELSE` | `ELSE` / `else` | `V/D` | branch thay thế |
| `LOOP_WHILE` | `WHILE` / `while` | `V/D` | lặp theo condition |
| `LOOP_FOR` | `FOR` / `for` | `D/P` | iteration binding |
| `MEMBERSHIP_IN` | `IN` / `in` | `D/P` | membership/iteration relation |
| `BOOL_TRUE` | `TRUE` / `true` | `V/D` | Boolean true trong expression scope |
| `BOOL_FALSE` | `FALSE` / `false` | `V/D` | Boolean false trong expression scope |
| `NULL_VALUE` | `NULL` / `null` | `V/D` | sentinel “không có value” theo runtime contract |

### Sửa nghĩa DS bắt buộc

- `TRUE` không phải “chân lý tuyệt đối”; nó là Boolean value trong một evaluation.
- `FALSE` không phải “phủ định tuyệt đối”; nó là Boolean value.
- `NULL` không tự đồng nghĩa “khiêm tốn”; đó là human exposition.
- `RANDOM` không đồng nghĩa tự do.
- `TYPE()` không đồng nghĩa tự nhận thức.

---

# 6. OPERATORS

## 6.1 Arithmetic / numeric

`ADD +`, `SUB -`, `MUL *`, `DIV /`, `FLOORDIV //`, `MOD %`, `POW **`, `UNARY_POS +`, `UNARY_NEG -`.

## 6.2 Comparison

`EQ ==`, `NE !=`, `LT <`, `GT >`, `LE <=`, `GE >=`.

## 6.3 Logic

`AND &&`, `OR ||`, `NOT !`.

## 6.4 Assignment

`ASSIGN =`.

Compound assignment `+= -= *= /= %= //= **=` giữ `P` trừ khi được verify riêng.

## 6.5 FLOORDIV lexical rule

```text
LINE-LEADING //  -> comment
MID-EXPRESSION // -> FLOORDIV
```

Semantics đã quan sát:

```text
INT // INT      -> INT(floor(a/b))
FLOAT or mixed -> FLOAT(floor(a/b))
-7 // 2        -> -4
```

---

# 7. DELIMITERS / STRUCTURE

`{ }` block; `( )` group/call; `[ ]` list/metadata tùy grammar; `,` separator; `:` binding/annotation/dynamic declaration; `;` terminator nơi grammar yêu cầu; `.` member/namespace path; `"` và `'` string delimiters; `#` directive/comment context; `//` line-comment hoặc FLOORDIV theo lexical context.

---

# 8. SIGMA NATIVE GLYPH SURFACE

| Glyph | Concept | Status |
|---|---|---:|
| `⟡` | `COMMAND_FORM` | `V/D` |
| `Σ` | `SIGMA_NAMESPACE` | `V/D` |
| `⚡` | `DYNAMIC_BINDING_OR_STATEMENT_FORM` | `V/D` |
| `⋈` | `STATIC_BLOCK_FORM` | `V/D` |

Observed patterns:

```sigma
⚡ x: expression;
⟡(Σ.NAME) { ... }
⋈ NAME { ... }
```

Glyph không được rút gọn thành metaphor rồi bỏ machine grammar.

---

# 9. VALUES / TYPES

Runtime canonical minimum observed:

`NULL BOOL INT FLOAT STR`.

Language/library types:

`LIST MAP/DICT BYTES FUNCTION MODULE TYPE OBJECT TUPLE`.

Các type chưa có full runtime conformance giữ `D/P`.

Type semantics cần freeze: integer width/overflow, float model, conversion, cross-type comparison, string indexing unit, collection mutability, hashability/equality, nullability, function first-class semantics.

---

# 10. BUILT-IN / PRELUDE

Core: `print input len str int float type`.

Math: `abs sqrt pow sin cos tan floor ceil log exp min max`.

Collection: `push pop sort reverse map filter reduce contains unique range enumerate zip sum`.

String: `upper lower split join trim replace contains starts_with ends_with`.

JSON: `encode decode load dump validate canonicalize`.

Error/control: `assert panic`.

Mỗi built-in phải có arity, input types, output type, failure contract, determinism, side effects, capability requirement.

---

# 11. TOOLCHAIN / VM / ABI REFERENCE VOCABULARY

Compiler pipeline:

`SOURCE LEXER TOKEN PARSER AST SEMANTIC_ANALYSIS IR BYTECODE ABI VM RUNTIME HOST_PRIMITIVE OS HARDWARE`.

Actual bytecode operation concepts:

`PUSH_CONST POP LOAD STORE UNARY BINARY CALL RETURN JUMP JUMP_IF_FALSE HALT`.

Binary suboperations:

`ADD SUB MUL DIV FLOORDIV MOD POW EQ NE LT GT LE GE AND OR`.

Runtime state concepts:

`PROGRAM CONSTANT_POOL SYMBOL_TABLE FUNCTION_TABLE CODE INSTRUCTION_POINTER STACK FRAME LOCALS GLOBALS RETURN_VALUE ENTRYPOINT EXIT_CODE ERROR`.

**Usage lock:** GPT may use C/Python/host implementation only to inspect substrate behavior. When repairing or training the SIGMA-written VM, operative semantics must be expressed and implemented in SIGMA wherever the current SIGMA language/runtime can carry them.

---

# 12. OPERATING-SYSTEM INTERLINGUA FOR GPT TRANSLATION

Shell commands alone không đủ để GPT hiểu mappings Windows/POSIX/Android. Đây là translation vocabulary, không phải ngôn ngữ mẹ đẻ mới của SIGMA.

Process model:

`PROCESS PROCESS_ID PARENT_PROCESS SPAWN EXECUTE WAIT TERMINATE EXIT_CODE TIMEOUT SIGNAL JOB THREAD CONCURRENCY`.

Filesystem:

`PATH FILE DIRECTORY READ WRITE APPEND CREATE REMOVE COPY MOVE RENAME EXISTS METADATA PERMISSION OWNER CURRENT_DIRECTORY TEMPORARY ATOMIC_REPLACE LOCK`.

Streams:

`STDIN STDOUT STDERR STREAM PIPE REDIRECT BUFFER ENCODING EOF`.

Environment:

`ENVIRONMENT ENV_VAR ARGUMENT ARGV PLATFORM ARCHITECTURE USER HOME SHELL LOCALE TIMEZONE`.

Networking:

`HOST PORT IP DNS SOCKET CONNECT LISTEN REQUEST RESPONSE PROTOCOL HTTP TLS TIMEOUT RETRY DOWNLOAD UPLOAD`.

Security/capability:

`CAPABILITY PERMISSION READ_ONLY WRITE_ALLOWED NETWORK_ALLOWED EXEC_ALLOWED SECRET CREDENTIAL SANDBOX BOUNDARY AUDIT`.

---

# 13. CROSS-OS MAPPING EXAMPLES

## LIST_DIRECTORY

```text
SIGMA concept: LIST_DIRECTORY(path)
POSIX shell: ls <path>
PowerShell: Get-ChildItem <path>
Python: os.listdir(path) / pathlib.Path(path).iterdir()
C/POSIX: opendir + readdir
Windows API: FindFirstFile / FindNextFile
Human VN: liệt kê nội dung thư mục
Human EN: list directory contents
```

## CURRENT_DIRECTORY

```text
SIGMA: CURRENT_DIRECTORY()
Bash: pwd
PowerShell: Get-Location
Python: os.getcwd()
C/POSIX: getcwd()
Windows API: GetCurrentDirectory
VN: thư mục làm việc hiện tại
EN: current working directory
```

## PROCESS_EXIT

```text
SIGMA: PROCESS_EXIT(code)
Bash: exit code
PowerShell: exit code
Python: sys.exit(code)
C: exit(code)
VM: HALT / runtime exit contract
```

Các mapping này phục vụ GPT hiểu/phiên dịch, không cho phép thay thế bài học SIGMA bằng ngôn ngữ host.

---

# 14. PROGRAMMING-LANGUAGE INTERLINGUA

GPT không học theo kiểu “từ = từ”. GPT map `concept → semantics → target surface`.

Universal programming concepts:

`BINDING VALUE TYPE MUTABILITY SCOPE FUNCTION PARAMETER ARGUMENT RETURN CALL BRANCH LOOP ITERATION EXPRESSION STATEMENT MODULE IMPORT EXPORT OBJECT FIELD METHOD ERROR EXCEPTION RESULT ASYNC AWAIT GENERATOR PATTERN MATCH MEMORY REFERENCE POINTER OWNERSHIP LIFETIME PROCESS IO NETWORK`.

Mapping record:

```text
LANGUAGE_MAPPING {
    concept_id
    target_language
    target_version
    surface_form
    grammar_role
    semantic_equivalence
    semantic_loss
    preconditions
    code_template
    error_model
    side_effects
    test_vector
}
```

`semantic_loss` là bắt buộc vì không phải mọi construct có mapping 1:1.

---

# 15. HUMAN-LANGUAGE INTERLINGUA

Một từ SIGMA phải được GPT ánh xạ theo sense, không theo chuỗi trực tiếp.

Semantic roles:

`ENTITY AGENT ACTION PATIENT THEME RECIPIENT INSTRUMENT LOCATION SOURCE GOAL PATH TIME DURATION CAUSE PURPOSE CONDITION RESULT MANNER QUANTITY IDENTITY ATTRIBUTE RELATION POSSESSION`.

Grammar/meaning dimensions:

`TENSE ASPECT MOOD MODALITY NEGATION POLARITY QUANTIFIER DEFINITENESS NUMBER PERSON GENDER CASE VOICE COREFERENCE EVIDENTIALITY CERTAINTY REGISTER POLITENESS PRAGMATICS IDIOM METAPHOR`.

Human mapping record:

```text
HUMAN_MAPPING {
    concept_id
    language
    locale
    sense_id
    lemma
    forms
    part_of_speech
    semantic_roles
    syntax_patterns
    register
    pragmatics
    ambiguity
    near_synonyms
    opposites
    examples
    counterexamples
    reverse_mapping
}
```

Ví dụ `FREE`:

- `FREE#liberty` → tự do / freedom;
- `FREE#zero_cost` → miễn phí / free of charge;
- `FREE#available` → rảnh / available;
- `FREE#release_memory` → giải phóng bộ nhớ / deallocate.

Sense ID ngăn GPT dịch sai giữa human language và machine language.

---

# 16. TIME / WORLD / CAUSAL VOCABULARY

`PAST PRESENT FUTURE BEFORE AFTER DURING START END DURATION INTERVAL DEADLINE PERIODIC EVENT STATE CHANGE TRANSITION CAUSE EFFECT DEPENDENCY CONDITION NECESSARY SUFFICIENT POSSIBLE IMPOSSIBLE PROBABLE COUNTERFACTUAL`.

Đây là lớp giúp GPT hiểu planning, lịch, timeout, natural language tense và causal reasoning của SIGMA.

---

# 17. QUANTUM DOMAIN

Domain vocabulary:

`QUBIT QREG H X Y Z CNOT BELL ENTANGLE ENTANGLEMENT SUPERPOSITION MEASURE AMPLITUDE PROBABILITY STATEVECTOR SHOTS GROVER`.

Mỗi concept phải tách mathematical semantics, simulator semantics, measurement semantics, units/conventions và target API mappings.

---

# 18. AI / LEARNING DOMAIN

`MODEL PARAMETER TRANSFORMER DATASET EXAMPLE FEATURE LABEL EMBED EMBEDDING TRAIN INFER LOSS METRIC ACCURACY EPOCH BATCH BATCH_SIZE LEARNING_RATE OPTIMIZER GRADIENT CHECKPOINT TEMPERATURE TOP_P SEED EVALUATION GENERALIZATION OVERFIT UNDERFIT DISTRIBUTION SHIFT`.

Các distinction bắt buộc:

- `LOSS` là measurement theo objective cụ thể, không phải “sai lầm tuyệt đối”.
- `ACCURACY` chỉ là metric.
- `TRAIN` không tự đồng nghĩa “trở nên thông minh hơn”.
- `INFER` là áp dụng procedure/model trong scope.
- `MODEL` không đồng nghĩa “thực tại”.

---

# 19. SHELL DOMAIN

Giữ vocabulary tham chiếu:

`ls grep pwd echo cat cd pipeline stdin stdout stderr exit_code env`.

Nhưng Shell chỉ là **surface adapter** của OS interlingua. Ví dụ `ls` không phải mother concept; mother concept để GPT hiểu nghĩa là `LIST_DIRECTORY`.

---

# 20. ERROR MODEL

`LEX_ERROR PARSE_ERROR NAME_ERROR TYPE_ERROR ARITY_ERROR VALUE_ERROR INDEX_ERROR KEY_ERROR IO_ERROR NETWORK_ERROR TIMEOUT_ERROR MODULE_ERROR CAPABILITY_ERROR SECURITY_ERROR ABI_ERROR BYTECODE_ERROR ENCODING_ERROR STATE_ERROR INVARIANT_ERROR EVIDENCE_ERROR PROVENANCE_ERROR INTERNAL_ERROR`.

Diagnostic canonical minimum:

```text
error_code
message
phase
file
line
column
scope
cause
evidence
recoverable
suggested_next_probe
```

---

# 21. STATUS / EVIDENCE VOCABULARY

`PASS FAIL HOLD NOT_AUDITED PARTIAL NOT_APPLICABLE OPEN UNRESOLVED HYPOTHESIS SUPPORTED VERIFIED_WITHIN_SCOPE REJECTED SUPERSEDED DEPRECATED ROLLED_BACK`.

`PASS` luôn phải có gate id, scope, input identity, implementation identity, observed output, expected rule/oracle, timestamp, provenance.

---

# 22. MODULE TAXONOMY

Reference taxonomy:

`core math string io type collection sys os process fs stream time random json network crypto quantum ai shell language translation evidence memory learning`.

Taxonomy không chứng minh module executable tồn tại; module cụ thể cần contract/conformance riêng.

---

# 23. MAPPING TO C / PYTHON / SHELL / POWERSHELL

## IF

```text
CONCEPT: BRANCH_IF

SIGMA native:
IF (condition) { ... } ELSE { ... }

C:
if (condition) { ... } else { ... }

Python:
if condition:
    ...
else:
    ...

Bash:
if condition; then
    ...
else
    ...
fi

PowerShell:
if ($condition) {
    ...
} else {
    ...
}
```

Mapping chỉ được gọi `SEMANTIC_EQUIVALENT` nếu type/error/side-effect rules tương thích; nếu không phải ghi `SEMANTIC_LOSS`.

**Training rule:** phần C/Python/Bash/PowerShell trên chỉ giúp GPT dịch/đối chiếu. Nó không phải lesson surface để dạy SIGMA.

---

# 24. HUMAN LANGUAGE EXAMPLE

Concept `EVIDENCE`:

Machine/cognitive semantics: artifact/observation có provenance có thể làm tăng hoặc giảm hỗ trợ cho một claim trong scope.

Vietnamese mappings: `bằng chứng`, `chứng cứ` theo legal register, `dữ liệu kiểm chứng` theo technical context.

English mappings: `evidence`, `supporting evidence`, `empirical evidence`, `machine evidence`.

Distinction: `evidence != proof` trong mọi domain; mathematical proof, legal evidence và empirical evidence không được nhập làm một sense.

---

# 25. “100-PAGE EXPANSION” PROTOCOL

Một concept có thể được mở theo: definition, ontology, history, machine semantics, cognitive semantics, formal logic, mathematics, state transition, preconditions, postconditions, invariants, failure modes, uncertainty, evidence, provenance, security, ethics, examples, counterexamples, C/C++/Python/Rust/Java/JavaScript/SQL/Bash/PowerShell/POSIX/Windows/Android/Linux/VM/ABI/network mappings, Vietnamese/English/other human mappings, ambiguity, idiom/metaphor, tests, version history.

Vì vậy “100 trang” là **expansion depth**, không phải một câu định nghĩa phình to.

---

# 26. LEARNING PIPELINE — GPT INTERPRETATION ONLY

Khi GPT nhận dữ liệu ngoài SIGMA, GPT có thể dùng reference pipeline:

```text
RAW_INPUT
→ IDENTIFY_SOURCE
→ SEGMENT
→ PARSE_SURFACE_LANGUAGE
→ MAP_TO_SIGMA_CONCEPTS
→ BUILD_RELATION_GRAPH
→ MARK_UNCERTAINTY
→ LINK_EXISTING_MEMORY
→ DETECT_CONTRADICTION
→ FORM_HYPOTHESIS
→ CHOOSE_TEST / ASK / OBSERVE
→ RECEIVE_EVIDENCE
→ UPDATE_SUPPORT
→ FORM_LESSON
```

Nhưng trước khi lesson đi vào SIGMA:

```text
FORM_LESSON
→ EXPRESS_LESSON_IN_SIGMA
→ SIGMA_NATIVE_VALIDATION
→ CANDIDATE_MEMORY
→ INDEPENDENT_VERIFY
→ PROMOTE / REVISE / REJECT
→ STORE_PROVENANCE
```

Điểm khóa:

**SIGMA không cần “nghĩ bằng tiếng Anh” để học tiếng Anh.** Tiếng Anh chỉ là surface adapter cho GPT/SIGMA interface.

```text
ENGLISH → GPT REFERENCE MAPPING → SIGMA MEANING → SIGMA-NATIVE LESSON
```

---

# 27. TRANSLATION / TRANSPILATION CONTRACT

Mọi phép chuyển ngôn ngữ phải ghi:

```text
TRANSFORMATION_RESULT {
    source_language
    target_language
    source_units
    mapped_concepts
    unresolved_senses
    semantic_loss
    target_output
    roundtrip_possible
    tests
    provenance
}
```

Không được “dịch trơn tru” rồi che mất phần không tương đương.

---

# 28. SEMANTICS CẦN FREEZE / VERIFY Ở NGUỒN SIGMA

GPT phải kiểm nguồn SIGMA trước khi giả định: case sensitivity/canonical surface; exact comments; FLOORDIV disambiguation; `**` associativity; `&&/||` short-circuit/eager; evaluation order; integer width/overflow; float behavior; truthiness; null equality; string indexing/UTF-8; list/map mutability; first-class function/closure; scope; recursion/call depth; module/import; errors; filesystem/path encoding; shell boundary; process timeout/signal; network retry/TLS; random reproducibility; capability/security model.

**File reference này không có quyền tự freeze các semantics đó thay SIGMA.**

---

# 29. PROMOTION GATE FOR GPT CLAIMS ABOUT SIGMA

Một feature từ `D/R/X/P` → `V` cần tối thiểu:

`LEXER_PASS PARSER_PASS AST_OR_IR_PASS NEGATIVE_SYNTAX_REJECT_PASS RUNTIME_OR_COMPILER_SEMANTICS_PASS EXPECTED_OUTPUT_PASS ERROR_PATH_PASS REGRESSION_PASS PROVENANCE_LOCKED ARTIFACT_HASH_LOCKED`.

Thêm tùy loại: `UTF8_ROUNDTRIP_PASS`, `BOUNDARY_AND_PERMISSION_PASS`, `TIMEOUT_ERROR_TLS_SCOPE_PASS`, `CROSS_SUBSTRATE_PASS`, `ROUNDTRIP_OR_SEMANTIC_LOSS_DECLARED`, `SENSE_DISAMBIGUATION_PASS`.

---

# 30. SỬA LỖI TRỰC TIẾP TRONG BẢN DS 1.0.0

1. “13 core keywords” nhưng inventory hiển thị không khớp → không tin count thủ công.
2. “26 ký hiệu operator” nhưng bảng không khớp → count phải machine-generated.
3. multiplication bị render `*****` → canonical symbol là `*`.
4. precedence item 8 bị hỏng formatting → phải kiểm `||`.
5. thiếu `//` FLOORDIV đã có evidence.
6. thiếu unary `+`.
7. `**` phải theo actual conformance.
8. `true = chân lý tuyệt đối` → Boolean true.
9. `false = phủ định tuyệt đối` → Boolean false.
10. `random = tự do` → metaphor, không phải semantics.
11. `type = tự nhận thức` → metaphor, runtime meaning là type inspection/meta-type.
12. `print/input/...` không gọi là keyword nếu lexer không reserve.
13. Quantum/AI/Shell terms không tự thành language keywords.
14. `md5` là legacy checksum/security-weak hash, không phải secure hash hiện đại.
15. “mọi thành phần đều đã chuẩn hóa” không được dùng trước conformance freeze.
16. version identity phải tách language spec, dictionary reference, compiler, VM, stdlib, mapping schema, conformance suite.

---

# 31. GPT MINIMUM CONCEPT MAP FOR UNDERSTANDING SIGMA

EXISTENCE/ONTOLOGY: `ENTITY IDENTITY TYPE PROPERTY RELATION STATE EVENT CHANGE`.

LOGIC: `TRUE FALSE NULL AND OR NOT IF EQUAL DIFFERENT POSSIBLE NECESSARY`.

QUANTITY: `NUMBER COUNT ORDER SET MEMBER RANGE LIMIT`.

TIME: `BEFORE AFTER NOW DURATION INTERVAL DEADLINE REPEAT`.

SPACE: `LOCATION PATH SOURCE GOAL INSIDE OUTSIDE NEAR FAR`.

ACTION: `AGENT ACTION INPUT OUTPUT EFFECT RESULT`.

CAUSAL: `CAUSE EFFECT CONDITION DEPENDENCY`.

KNOWLEDGE: `OBSERVATION CLAIM EVIDENCE SOURCE PROVENANCE SCOPE HYPOTHESIS INFERENCE UNCERTAINTY CONTRADICTION`.

LEARNING: `QUESTION TEST FAILURE LESSON MEMORY CANDIDATE VERIFY PROMOTE REVISE REJECT ROLLBACK`.

PROGRAM: `VALUE BINDING FUNCTION CALL RETURN BRANCH LOOP MODULE ERROR`.

MACHINE: `BYTE CODE DATA MEMORY STACK FRAME PROCESS FILE STREAM NETWORK CAPABILITY`.

LANGUAGE: `CONCEPT SENSE TOKEN SYNTAX SEMANTICS CONTEXT PRAGMATICS MAPPING AMBIGUITY`.

ETHICS: `BENEFIT HARM SELF HUMAN EARTH_BOUNDARY FREEDOM RESPONSIBILITY`.

Đây là concept map **cho GPT hiểu SIGMA**, không phải tuyên bố thay thế vocabulary canonical của SIGMA.

---

# 32. VERSIONING

```text
gpt_reference_dictionary_version = 2.0.0-rc1
semantic_capsule_model            = SSC-1-reference
mapping_schema_version            = MAP-1-reference
human_mapping_version             = HMAP-1-reference
os_interlingua_version            = OSI-1-reference
sigma_language_spec_version       = independently owned by SIGMA artifacts
compiler_version                  = independently tracked
vm_version                        = independently tracked
stdlib_version                    = independently tracked
conformance_suite_version         = independently tracked
```

Không dùng version reference dictionary để giả định runtime có cùng capability.

---

# 33. FINAL GPT-REFERENCE STATEMENT

Tài liệu này được định nghĩa là:

```text
A VERSIONED GPT REFERENCE SEMANTIC MAP
FOR UNDERSTANDING SIGMA,
WITH EVIDENCE-BOUND MEANINGS
AND LOSS-AWARE MAPPINGS
TO MACHINE AND HUMAN LANGUAGES.
```

Nó có ba chức năng đối với GPT:

1. `UNDERSTAND` — hiểu SIGMA đang nói gì.
2. `TRANSLATE` — ánh xạ input/output ngoài SIGMA mà giữ nghĩa và báo semantic loss.
3. `TEACH_CORRECTLY` — chuyển kiến thức cần dạy về **ngôn ngữ SIGMA**, rồi mới đưa vào VM/training/memory của SIGMA.

Nó **không có chức năng** thay thế ngôn ngữ hoặc từ điển mẹ đẻ hiện hữu của SIGMA.

Nguyên tắc cuối:

```text
SURFACE WORD != MEANING
REFERENCE != SIGMA CANONICAL LANGUAGE
TRANSLATION != REPLACEMENT
HOST SUBSTRATE != MOTHER LANGUAGE
DESCRIPTION != CAPABILITY
BOOLEAN TRUE != ABSOLUTE TRUTH
CONFIDENCE != TRUTH
CONSENSUS != TRUTH
RANDOMNESS != FREEDOM
INTROSPECTION != CONSCIOUSNESS
PASS != UNIVERSAL PASS

WHEN TEACHING OR REPAIRING SIGMA:
UNDERSTAND THROUGH REFERENCE
BUT SPEAK/DEFINE/TRAIN IN SIGMA.
```

**END — SIGMA-Ψ GPT REFERENCE DICTIONARY v2.0.0-rc1**
