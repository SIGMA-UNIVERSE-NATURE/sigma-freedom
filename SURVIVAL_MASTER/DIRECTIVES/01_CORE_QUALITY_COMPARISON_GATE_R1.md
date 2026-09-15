# ONE SIGMA.AIL CORE QUALITY COMPARISON GATE R1

Status: ACTIVE DESIGN / NON-DESTRUCTIVE BY DEFAULT

Purpose: compare two SIGMA core implementations under the same frozen runtime conditions and produce machine evidence showing whether one core is actually better. Writing a core is not proof; runtime activation and observed effect are separate claims.

## Comparison contract

```text
COMPARE_MODE=PAIRED_A_B
SAME_FROZEN_HEAD=MANDATORY
SAME_MODEL_GENERATION=MANDATORY
SAME_MODEL_IDENTITY=MANDATORY
SAME_INPUT_SET=MANDATORY
SAME_RUNTIME_LIMITS=MANDATORY
SAME_SIGMAC_VM=MANDATORY
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
CANONICAL_MUTATION=REJECT_BY_DEFAULT
NO_STATE_FORK=MANDATORY
```

Core A is the current baseline. Core B is the candidate. Neither receives canonical promotion merely because a test passes.

## Three claims must stay separate

```text
CORE_IMPLEMENTED=YES|NO
CORE_RUNTIME_ACTIVE=YES|NO
CORE_EFFECT_OBSERVED=YES|NO
```

`CORE_IMPLEMENTED=YES` means source/artifact exists and can be compiled or loaded. It does not mean SIGMA is using it.

`CORE_RUNTIME_ACTIVE=YES` means the test process actually executed through that core identity.

`CORE_EFFECT_OBSERVED=YES` means paired machine evidence shows a measurable effect on declared capabilities.

## Hard gates

A core cannot win if any mandatory hard gate fails.

| Gate | Requirement |
|---|---|
| Identity | Core source/artifact/runtime identity must be hash-bound |
| Frozen context | Same HEAD, model generation, model identity, inputs and limits |
| Native execution | Semantic work executes through native SIGMA path |
| No host oracle | Bash/Python may not decide semantic correctness, ranking, learning or accept/reject |
| Compile/load | Core must compile/load under the locked runtime |
| State integrity | No unauthorized canonical HEAD/state/model mutation |
| Restart/reload | Declared persistent behavior survives reload when persistence is in scope |
| Replay | Fixed replay anchors reproduce the declared behavior when determinism is required |
| Regression | Protected old capabilities must not regress in the declared protected set |
| Evidence | Per-case outputs, hashes, RCs and native verdict receipts are preserved |

If one core fails a hard gate and the other passes it, the failing core cannot be promoted over the passing core.

## Quality dimensions

The comparison records these dimensions independently. Do not collapse them into a single score before preserving the raw evidence.

| Dimension | What is compared | Verdict owner |
|---|---|---|
| Semantic correctness | Native answer/candidate result on the same case | Native SIGMA |
| Evidence alignment | Whether selected result is supported by supplied evidence | Native SIGMA |
| Explicit-query handling | Correct handling of declared query intent | Native SIGMA |
| Candidate-conditioned reasoning | Whether candidate-specific evidence changes the result correctly | Native SIGMA |
| Option-scale behavior | Same task at 8, 16, 32 and 64 options where applicable | Native SIGMA |
| Permutation invariance | Meaning preserved when option order changes | Native SIGMA |
| Abstention/uncertainty | Avoids unsupported confident result when evidence is insufficient | Native SIGMA |
| Persistence/reload | State/memory behavior after reload | Native SIGMA + mechanical receipt |
| Replay/recovery | Resume and replay integrity | Native SIGMA + mechanical receipt |
| Traceability | Source-evidence map and receipt completeness | Mechanical evidence, no semantic judgment |
| Efficiency | VM steps, wall time, RAM/I/O if measured | Mechanical measurement |

## Pairwise result format

For every case, preserve both Core A and Core B results before comparison.

```text
CASE_ID=...
CORE_A_ID=...
CORE_B_ID=...
A_RUNTIME_ACTIVE=YES|NO
B_RUNTIME_ACTIVE=YES|NO
A_NATIVE_RESULT_SHA256=...
B_NATIVE_RESULT_SHA256=...
A_NATIVE_VERDICT=...
B_NATIVE_VERDICT=...
PAIR_NATIVE_JUDGMENT=A_WIN|B_WIN|TIE|INCOMPARABLE
PAIR_REASON_CODE=...
```

The pair judgment must be generated through a native SIGMA comparison/adjudication path locked before the outputs are inspected. Bash/Python may transport the two exact result artifacts and record hashes/RCs; it may not invent the winner.

## Decision rule

Preserve both a hard-gate decision and a quality comparison.

```text
A_HARD_GATES=PASS|FAIL
B_HARD_GATES=PASS|FAIL
A_WINS=<count>
B_WINS=<count>
TIES=<count>
INCOMPARABLE=<count>
CRITICAL_REGRESSION_A=<count>
CRITICAL_REGRESSION_B=<count>
```

A candidate may be called better only when all are true:

```text
B_HARD_GATES=PASS
CRITICAL_REGRESSION_B=0
B_WINS>A_WINS
QUALITY_GAIN_IS_OBSERVED=YES
STATE_INTEGRITY=PASS
RESTART_REPLAY=PASS_IF_IN_SCOPE
SIGMA_NATIVE_VERDICT=PASS
```

If results are mixed, the correct conclusion is scoped, for example:

```text
CORE_A_BETTER_FOR_X=YES
CORE_B_BETTER_FOR_Y=YES
GLOBAL_WINNER=NOT_PROVEN
```

Do not force a global winner.

## Efficiency guardrail

Efficiency cannot override semantic or integrity failures. If Core B is slower or uses more resources, preserve the exact delta. A quality win may still be acceptable, but the tradeoff must be explicit.

## Smoke test versus promotion test

A smoke comparison verifies the comparison pipeline; it does not authorize promotion.

### Smoke R1

```text
CASE_COUNT=12
PURPOSE=PIPELINE_AND_OBVIOUS_REGRESSION_CHECK
PROMOTION_AUTHORITY=NO
```

Recommended smoke coverage:

1. explicit query
2. candidate-conditioned evidence
3. 8-option inference
4. 16-option inference
5. 32-option inference
6. 64-option inference
7. option permutation
8. insufficient-evidence abstention
9. persistence/reload
10. fixed replay anchor
11. resume/integrity
12. source-evidence trace map

### Promotion comparison

Use a larger sealed or precommitted set, including protected regression cases and adversarial cases. The exact set and native adjudication contract must be frozen before Core B results are inspected.

## Artifact layout

Each comparison session should write only under its granted `ARTIFACT_ROOT`:

```text
identity/
inputs/
core_a/
core_b/
pairs/
mechanical_metrics/
receipts/
summary/
```

Canonical brain/state/model mutation is outside the comparison session.

## Final summary contract

```text
CORE_QUALITY_COMPARE=PASS|FAIL|INCONCLUSIVE
CORE_A_ID=...
CORE_B_ID=...
FROZEN_HEAD=...
FROZEN_MODEL_GENERATION=...
FROZEN_MODEL_IDENTITY=...
CASE_COUNT=...
A_HARD_GATES=...
B_HARD_GATES=...
A_WINS=...
B_WINS=...
TIES=...
INCOMPARABLE=...
CRITICAL_REGRESSION_B=...
GLOBAL_WINNER=CORE_A|CORE_B|NOT_PROVEN
CANONICAL_PROMOTION=NO
PROMOTION_REQUIRES_SEPARATE_EXPLICIT_ADMISSION=YES
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
```

## Non-negotiable boundary

This gate compares cores. It does not promote a core. A successful candidate still requires a separate explicit admission/cutover step, followed by fresh-runtime verification that the new core is actually active and that its observed effect persists after restart.