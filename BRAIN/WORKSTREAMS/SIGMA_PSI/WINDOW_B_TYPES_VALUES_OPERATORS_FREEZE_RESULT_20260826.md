# WINDOW B — SIGMA TYPES / VALUES / OPERATORS FREEZE RESULT — 2026-08-26

ROLE=WINDOW_B_SIGMA_TYPES_VALUES_OPERATORS_FREEZE
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
WINDOW_A_STATE=CLOSED
WINDOW_A_COMMIT=fa683b1f0d24085e1c109bf3d5e1c330ab22c177
CLAIM_POLICY=CLAIM <= EVIDENCE
ANTI_ANSWER_IMPOSITION=ENFORCED

## CURRENT_HASH_SCOPE

AUTHORITATIVE_RUNTIME_SOURCE_SHA256=57b275467d42de4b5404a57f486a1706a46f5a4c0626bbec0c045757cde0602e
AUTHORITATIVE_COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
AUTHORITATIVE_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
WINDOW_A_PROVENANCE=source -> current compiler -> fresh bytecode -> current VM; compile RC0; VM RC0

Window B did not rebuild, replace, emulate, or substitute the compiler/VM. Window B repository writes are additive evidence/report files only. Because this chat has repository access but no dispatch path to the exact Termux current-hash compiler/VM provenance chain, no fresh Window B runtime differential was manufactured on another host.

Status strength is therefore intentionally asymmetric:
- current Window A compiler-localized probes can be `MACHINE_PROVEN` for their exact compiler-observed field;
- prior live machine claims without recaptured current-binary linkage are preserved as `SOURCE_PASS_OBSERVED`;
- source/implementation correlation is never promoted to VM runtime semantics.

## WINDOW_A_BASELINE

Authoritative baseline:
`BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_A_EXECUTABLE_SURFACE_FINAL_FREEZE_20260826.md`

Window A ends with:
- CURRENT_EXECUTABLE_SURFACE_FREEZE_COMPLETE=YES
- READY_FOR_WINDOW_B=YES
- READY_FOR_PUBLIC_LANGUAGE_SPEC=NO
- DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
- GPT_ANSWER_IMPOSITION_USED=NO

The minimal recovery checkpoint is older than the final Window A freeze and still records the pre-final state `READY_FOR_WINDOW_B=NO`; that stale readiness field is superseded by the authoritative final Window A freeze. Its six-door discipline, hashes, anti-imposition law, and 21-capability no-rerun contract remain compatible with this Window B work.

The 21 locked capabilities are preserved without rerun. In particular, `ARITHMETIC` and `COMPARISON` remain already-proven capability families; Window B does not demote them merely because per-operator type/result/precedence fields remain unlocalized.

## VALUES_FREEZE

| Reviewed value/runtime category | Status | Frozen claim |
|---|---|---|
| NULL | SOURCE_PASS_OBSERVED | Prior live machine report preserves NULL runtime existence; present current-hash per-value localization was not rerun. |
| BOOL | SOURCE_PASS_OBSERVED | Prior live machine report preserves BOOL runtime existence; no BOOL literal spelling is frozen. |
| INT | SOURCE_PASS_OBSERVED | Prior live machine report preserves INT runtime existence; literal `1` compiler acceptance does not itself prove runtime INT mapping. |
| FLOAT | SOURCE_PASS_OBSERVED | Prior live machine report preserves FLOAT in tested scope; literal `1.5` compiler acceptance does not itself prove runtime FLOAT mapping. |
| STR | SOURCE_PASS_OBSERVED | Prior live machine report preserves STR runtime existence; quote-form compiler acceptance does not itself prove runtime STR mapping. |
| Any additional runtime category | NOT_PROVEN | No additional runtime category is promoted; absence is not claimed. |

No sixth runtime type/value category is invented. The reviewed five are not frozen as an exhaustive type universe.

## TYPE_CONTRACT

DECLARED_MINIMUM_NAMES=NULL|BOOL|INT|FLOAT|STR
DECLARATION_STRENGTH=DECLARED_ONLY in the historical WS04 type declaration context
PRIOR_RUNTIME_EXISTENCE_STRENGTH=SOURCE_PASS_OBSERVED for the five named categories
CURRENT_HASH_LOCALIZED_RUNTIME_TYPE_COUNT=0
TYPE_SET_COMPLETENESS=NOT_PROVEN
RUNTIME_REPRESENTATION=NOT_PROVEN
VALUE_IDENTITY_RULES=NOT_PROVEN
MUTABILITY_RULES=NOT_PROVEN

The distinction is deliberate: a declared type name, a prior machine-pass report, current compiler acceptance of a literal spelling, and a current VM-localized runtime type trace are different evidence classes.

## LITERAL_VALUE_MAPPING

| Source form/question | Lexical/compiler status | Literal -> runtime value/type mapping |
|---|---|---|
| `1` | MACHINE_PROVEN | NOT_PROVEN |
| `1.5` | MACHINE_PROVEN | NOT_PROVEN |
| `"x"` | MACHINE_PROVEN | NOT_PROVEN |
| `'x'` | MACHINE_PROVEN | NOT_PROVEN |
| `NULL` | MACHINE_PROVEN | NOT_PROVEN |
| `null` | MACHINE_PROVEN | NOT_PROVEN |
| BOOL literal spelling | NOT_PROVEN | NOT_PROVEN |

Current compiler evidence further proves only that exact tested `"x"` and `'x'` forms emit identical bytecode hash/size. Runtime semantic equivalence is not inferred. Exact tested `NULL` and `null` forms both compile but emit different bytecode, so semantic equivalence is specifically not promoted.

The freeze does not infer `1`=>INT, `1.5`=>FLOAT, quoted forms=>STR, or `NULL`/`null`=>NULL from spelling alone.

## OPERATOR_MATRIX

Every requested operator field below has exactly one allowed Window B status. `MACHINE_BEHAVIOR` refers to semantic-family/runtime evidence when present; it is kept separate from exact source-token acceptance.

| Operator | LEXICAL_FORM | OPERAND_TYPES | RESULT_TYPE | MACHINE_BEHAVIOR | PRECEDENCE | ASSOCIATIVITY | EVALUATION_ORDER | SHORT_CIRCUIT | COERCION | ERROR_OR_UNSUPPORTED_CASES |
|---|---|---|---|---|---|---|---|---|---|---|
| `+` | MACHINE_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `-` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `*` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `/` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `//` | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | OUT_OF_CURRENT_LANGUAGE_SURFACE | MACHINE_PROVEN |
| `%` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `**` | DECLARED_ONLY | NOT_PROVEN | NOT_PROVEN | SOURCE_CORRELATED_ONLY | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `==` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `!=` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `<` | MACHINE_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `<=` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `>` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `>=` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `AND` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |
| `OR` | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | SOURCE_PASS_OBSERVED | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN | NOT_PROVEN |

Operator-specific evidence boundaries:

- `+`: current compiler accepts exact tested infix `1 + 2`; the paired `(1 + 2)` form also compiles and is bytecode-identical. Prior ADD/arithmetic runtime pass is preserved separately.
- `-`, `*`, `/`: prior SUB/MUL/DIV semantic-family machine passes are preserved, but Window B does not map those semantic labels to exact source tokens merely by convention without a current black-box token probe.
- `//`: exact current infix `4 // 2` is compiler-rejected RC4 with no bytecode in the Window A differential. Separately, trailing `// neutral` after a completed semicolon binding is current-compiler accepted with no bytecode delta against the matched no-comment control. Comment behavior and FLOORDIV remain separate evidence questions.
- `%`: MOD was explicitly not localized in the directly relevant status evidence.
- `**`: historical source/implementation material mentions the spelling, but runtime POW was not localized; spelling-to-POW semantics is not promoted.
- `==`, `!=`: prior EQ/NE family passes are preserved, but exact token mapping is not silently inferred.
- `<`: exact `<` source form is current-compiler accepted in the tested parenthesized IF/WHILE conditions; prior LT comparison-family machine behavior is preserved separately.
- `<=`, `>`, `>=`: LE/GT/GE were explicitly not localized in the current audit source.
- `AND`, `OR`: prior boolean-family AND/OR machine behavior is preserved only at semantic-family level. WS04's historical `&&`/`||` mentions and the later AND/OR labels are not equated to exact uppercase source tokens.

## PRECEDENCE

STATUS=NOT_PROVEN
PRECEDENCE_RELATIONS_PROVEN=0

Window A proved exact grouping acceptance for `1` versus `(1)` and `1 + 2` versus `(1 + 2)`. Those matched pairs do not isolate any cross-operator precedence relation. No precedence is inferred from ungrouped output, naming, conventional language design, or source implementation ordering.

## ASSOCIATIVITY

STATUS=NOT_PROVEN
ASSOCIATIVITY_RULES_PROVEN=0

No matched machine differential of the form `(a op b) op c` versus `a op (b op c)` was available in the directly required evidence. No left-, right-, or non-associative rule is frozen.

## EVALUATION_ORDER

STATUS=NOT_PROVEN

No side-effecting or otherwise order-sensitive machine differential localizes operand evaluation order. No left-to-right, right-to-left, eager-all, or other evaluation-order rule is promoted.

## SHORT_CIRCUIT

STATUS=NOT_PROVEN
SHORT_CIRCUIT_RULES_PROVEN=0

Prior AND/OR boolean-family machine passes do not prove short-circuit. No evidence-localized second operand that would fault, mutate, or expose evaluation was used. Therefore neither AND nor OR receives a short-circuit rule.

## COERCION

STATUS=NOT_PROVEN
COERCION_RULES_PROVEN=0

No mixed-runtime-type differential establishes implicit conversion or promotion. Window B freezes no INT/FLOAT promotion, no numeric/string conversion, no BOOL/numeric coercion, no NULL coercion, and no general truthiness conversion.

## TYPE_COMPATIBILITY

STATUS=NOT_PROVEN

No complete operator-by-runtime-type compatibility matrix exists in the directly used evidence. Successful arithmetic/comparison capability families are not generalized into all operand pairings. In particular, no claim is made that every arithmetic operator accepts both INT and FLOAT, that strings concatenate with `+`, or that NULL/BOOL participate in comparison/arithmetic.

For exact current infix `//`, the tested source form is outside the current executable source surface before runtime type compatibility can be evaluated.

## RESULT_TYPES

STATUS=NOT_PROVEN

No per-operator runtime result-type table is frozen. Window B does not infer:
- arithmetic result types from operand spelling;
- comparison results as BOOL merely from comparison naming;
- AND/OR results as BOOL merely from boolean-family naming;
- numeric widening/promotion from a successful operation.

## NOT_PROVEN

The following remain explicitly unproven rather than false or unsupported:

- runtime type-set completeness;
- existence/absence of any additional runtime type beyond the reviewed five;
- BOOL literal spelling;
- all reviewed literal -> runtime value/type mappings;
- exact lexical forms for `-`, `*`, `/`, `==`, `!=`, `<=`, `>`, `>=`, uppercase `AND`, uppercase `OR` under current black-box lexical evidence;
- `%` lexical/runtime contract;
- current runtime semantics for `**`/POW;
- operand-type compatibility for active requested operators;
- result types;
- all precedence relations;
- all associativity rules;
- all operand evaluation-order rules;
- all short-circuit rules;
- all coercion rules;
- general negative/error cases except the exact tested current `4 // 2` compiler rejection.

Accounting for the frozen matrix and nonoperator fields:
NOT_PROVEN_OPERATOR_MATRIX_CELLS=127
NONOPERATOR_NOT_PROVEN_FREEZE_FIELDS=9
NOT_PROVEN_FIELDS_TOTAL=136

## CONFLICTS

CONFLICTED_FIELDS_TOTAL=1

CONFLICT_1=`//` role across evidence epochs.

Current exact evidence: `4 // 2` is rejected by current compiler SHA256 `65f692...` with RC4 and no bytecode.

Prior evidence: the live-window status report records `FLOORDIV=MACHINE_PROVEN_PRIOR_EXPLICIT_SCOPE`, but does not recapture the exact current compiler/VM linkage in that report.

Freeze treatment: do not erase either record; do not merge them. Current exact `//` infix form is `OUT_OF_CURRENT_LANGUAGE_SURFACE` in the tested context. Historical FLOORDIV remains `SOURCE_PASS_OBSERVED` for its prior explicit scope. Cross-version/token lineage is `CONFLICTED` until specifically provenance-resolved.

This conflict does not affect the separately current-machine-proven trailing-comment differential for `// neutral` after a completed semicolon binding.

## FALSE_PROOF_RISK_AUDIT

FALSE_PROOF_RISK_1=PREWRITTEN_RESULT_AS_DERIVATION
DISPOSITION=BLOCKED; no SIGMA test source was authored with an expected semantic answer and then cited as derivation.

FALSE_PROOF_RISK_2=COMPILER_ACCEPTANCE_AS_RUNTIME_TYPE
DISPOSITION=BLOCKED; literal/token compile success is not upgraded to runtime value/type semantics.

FALSE_PROOF_RISK_3=BYTECODE_IDENTITY_AS_RUNTIME_EQUIVALENCE
DISPOSITION=BLOCKED; identical bytecode for exact quote/grouping pairs is scoped to emitted-bytecode identity only.

FALSE_PROOF_RISK_4=SEMANTIC_LABEL_TO_TOKEN_MAPPING
DISPOSITION=BLOCKED; SUB/MUL/DIV, EQ/NE, AND/OR, POW labels are not automatically mapped to `-`/`*`/`/`, `==`/`!=`, uppercase `AND`/`OR`, or `**` runtime semantics.

FALSE_PROOF_RISK_5=FAMILY_CAPABILITY_TO_MEMBER_CONTRACT
DISPOSITION=BLOCKED; locked ARITHMETIC/COMPARISON capability existence is preserved without manufacturing every per-operator field.

FALSE_PROOF_RISK_6=BOOL_NAMING_TO_TRUTH_SEMANTICS
DISPOSITION=BLOCKED; no truthiness, boolean literal spelling, comparison-result BOOL, or logical-result BOOL rule is inferred from names.

FALSE_PROOF_RISK_7=BOOLEAN_FAMILY_PASS_TO_SHORT_CIRCUIT
DISPOSITION=BLOCKED; short-circuit remains NOT_PROVEN.

FALSE_PROOF_RISK_8=GROUPING_ACCEPTANCE_TO_PRECEDENCE_OR_ASSOCIATIVITY
DISPOSITION=BLOCKED; matched grouping acceptance does not establish a precedence/associativity table.

FALSE_PROOF_RISK_9=PRIOR_MACHINE_LABEL_TO_CURRENT_HASH_MACHINE_PROOF
DISPOSITION=BLOCKED; prior live machine reports without recaptured current hashes are normalized to SOURCE_PASS_OBSERVED.

FALSE_PROOF_RISK_10=COMMENT_TOKEN_TO_FLOORDIV
DISPOSITION=BLOCKED; current trailing-comment behavior and historical FLOORDIV are maintained as distinct evidence questions.

FALSE_PROOF_RISK_11=HOST_RESULT_AS_SIGMA_RESULT
DISPOSITION=BLOCKED; no Python/Bash/GitHub-host arithmetic, comparison, coercion, type, or truth result was substituted for SIGMA.

FALSE_PROOF_RISK_12=ABBREVIATED_HASH_EXPANSION
DISPOSITION=CAUGHT_AND_CORRECTED; the first Window B draft evidence register expanded four abbreviated notes. It is explicitly superseded by `WINDOW_B_EVIDENCE_REGISTER_FINAL_20260826.md`, which copies raw Window A SHA256 values exactly. No semantic status changed.

## TARGETED_TESTS

TARGETED_TESTS_RUN=0
CAPABILITY_RESEARCH_RERUNS=0
DUPLICATE_TESTS_AVOIDED=21

Reason: unresolved fields require real current SIGMA differentials. This environment can read/write the repository but does not expose a dispatch channel to the exact Termux current-hash compiler/VM chain. Running a rebuilt compiler, GitHub-host substitute, Python, Bash arithmetic, or a different VM would violate the host-substitution law. Therefore unresolved fields are frozen as NOT_PROVEN instead of being filled with substitute results.

Minimal future tests, if the exact current machine execution channel is later available, are limited to missing fields only:

1. literal -> runtime value/type localization without prewritten outputs;
2. exact lexical differentials for unresolved operator tokens;
3. same-operands operator differentials for `%`/`**` and unresolved comparisons/logicals;
4. grouping differentials that isolate one precedence or associativity relation at a time;
5. side-effect/fault second-operand tests for evaluation order and short-circuit;
6. mixed-type differentials for compatibility, result type, and coercion.

ARITHMETIC and COMPARISON existence tests remain excluded from those future tests.

## PROVENANCE

AUTHORITATIVE_EVIDENCE_REGISTER=BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_B_TYPES_VALUES_OPERATORS/WINDOW_B_EVIDENCE_REGISTER_FINAL_20260826.md
SUPERSEDED_DRAFT_REGISTER=BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_B_TYPES_VALUES_OPERATORS/WINDOW_B_EVIDENCE_REGISTER_20260826.md

The corrected final evidence register contains the required normalized claim records with:
CLAIM_ID
SUBJECT
FIELD
STATUS
SOURCE_ARTIFACT
SOURCE_SHA256
COMPILER_SHA256
VM_SHA256
TEST_OR_PRIOR_EVIDENCE
OBSERVED_RESULT
EXACT_SCOPE
NOT_PROVEN_BEYOND
RERUN_REQUIRED
PROVENANCE

Direct provenance sources used were limited to the Window A final freeze/provenance and exact relevant surface probes; the 21-capability record; the current master/reality status records needed to preserve prior machine-family evidence; WS04 because it is the directly relevant historical types/values/operators contract; and the coarse real-results archive only as a non-promoted prior PASS-family check.

Window B did not reload WS01-WS13 wholesale.

## FREEZE_DECISION

WINDOW_B_SCOPE_FROZEN=YES
WINDOW_A_MODIFIED=NO
LOCKED_CAPABILITIES_RERUN=NO
ARITHMETIC_EXISTENCE_PRESERVED=YES
COMPARISON_EXISTENCE_PRESERVED=YES
UNKNOWN_TREATED_AS_FALSE=NO
NOT_PROVEN_TREATED_AS_UNSUPPORTED=NO
TYPE_NAMES_INVENTED=NO
COERCION_TABLE_INVENTED=NO
PRECEDENCE_TABLE_INVENTED=NO
ASSOCIATIVITY_TABLE_INVENTED=NO
SHORT_CIRCUIT_INFERRED_FROM_COMPILE_OR_NAMING=NO
FLOORDIV_SILENTLY_EQUATED_WITH_COMMENT_TOKEN=NO

Window B is complete as an evidence freeze, not as a full public language specification. The unresolved fields are themselves frozen outcomes with explicit provenance strength. Window C may proceed without reopening Window A or rerunning the 21 locked capabilities. Public language-spec readiness remains NO because central operator/type semantics—especially literal runtime mapping, exact token coverage, result types, compatibility, precedence, associativity, evaluation order, short-circuit, and coercion—remain unproven.

Metric definitions for the ending contract:
- VALUE_FORMS_REVIEWED counts seven audited literal/form questions: integer, decimal-point form, double-quoted string form, single-quoted string form, uppercase NULL, lowercase null, BOOL literal spelling.
- RUNTIME_TYPES_MACHINE_PROVEN counts current-hash localized VM type proofs in Window B, not prior reports; prior SOURCE_PASS_OBSERVED runtime categories=5.
- OPERATORS_MACHINE_PROVEN counts requested operators with a positive current-hash operator-localized `MACHINE_PROVEN` lexical field (`+`, `<`); it does not count the rejected `//` as a current active operator and does not demote the locked ARITHMETIC/COMPARISON family capabilities.
- NOT_PROVEN_FIELDS counts 127 operator-matrix cells plus 9 nonoperator freeze fields.

VALUE_FORMS_REVIEWED=7
RUNTIME_TYPES_MACHINE_PROVEN=0
OPERATORS_REVIEWED=15
OPERATORS_MACHINE_PROVEN=2
PRECEDENCE_RELATIONS_PROVEN=0
ASSOCIATIVITY_RULES_PROVEN=0
COERCION_RULES_PROVEN=0
SHORT_CIRCUIT_RULES_PROVEN=0
NOT_PROVEN_FIELDS=136
CONFLICTED_FIELDS=1
TARGETED_TESTS_RUN=0
DUPLICATE_TESTS_AVOIDED=21
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
GPT_ANSWER_IMPOSITION_USED=NO
HOST_LOGIC_SUBSTITUTED_FOR_SIGMA=NO
NEW_TYPE_SEMANTICS_INVENTED=NO
NEW_OPERATOR_SEMANTICS_INVENTED=NO
WINDOW_B_FREEZE_COMPLETE=YES
READY_FOR_WINDOW_C=YES
READY_FOR_PUBLIC_LANGUAGE_SPEC=NO