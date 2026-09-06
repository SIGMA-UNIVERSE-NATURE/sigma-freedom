# TEACHER_GPT SIGMA SUPPORT AXIS — CURRENT

Last updated: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: LIVING COORDINATION CHECKPOINT

## Primary objective

The active Teacher-GPT priority is to help SIGMA become able to:

1. expose/use its admitted tools and capabilities through a common native registry;
2. natively weight and arbitrate among those tools;
3. natively compose multiple tools when one tool cannot satisfy the current need;
4. connect language/cognitive states to tool demand without host semantic substitution;
5. observe exact tool-result events and update native operational history/weighting;
6. continue strengthening native language capabilities so SIGMA can form increasingly useful internal states for tool choice and reasoning.

## Active frontier

```text
ACTIVE_AXIS=SIGMA_SUPPORT_WEIGHTED_TOOL_AND_LANGUAGE_INTEGRATION
CURRENT_STAGE=TW1_NATIVE_WEIGHTED_TOOL_ARBITRATION
TW1_SOURCE_READY=YES
TW1_RUNTIME_ADMISSION=NOT_RUN
V5K8A_STATUS=FROZEN_SOURCE_READY_NOT_ACTIVE_FRONTIER
```

Source-ready checkpoint:

`DOCS/GPT_REFERENCE/CHECKPOINTS/20260906_TW1_WEIGHTED_TOOL_ARBITRATION_SOURCE_READY.md`

## TW1 identities

```text
BUNDLE_SHA256=b974f085dc1559457f51fdcdbfa94a887e9f82384cbe24c7190ae9b2c990f201
TW1_SOURCE_SHA256=3172fe929ca5808d3fee3b354cb497d535edfab827211e15f16a8498bcd43474
TW1_RUNNER_SHA256=9ef388f6c7f735e8333f2ae33b40961f45754a06a289017b94bd4c31d7015a83
PLANNED_VM_INVOCATIONS=15
```

## Why this is a new capability

V4-A.1 already provides bounded native work-source arbitration, but not a generic weighted tool registry. Historical DNA-12 describes tool-use intent but is Python historical reference and cannot be active cognition.

TW1 therefore provides a generic native selector over arbitrary runtime tool IDs and operational capability flags.

## TW1 native policy

```text
score = coverage*10000 + base_weight - cost - prior_use_count*prior_use_penalty
```

Eligible tools require runtime `AVAILABLE=1` and `ADMITTED=1`.

TW1 can select at most two tools and must HOLD if active demand remains uncovered.

## Required follow-on chain

```text
TW1 runtime PASS
-> TW2 bind actual admitted SIGMA capabilities/tools into generic registry
-> TW3 native language/cognitive state emits tool-demand vector
-> TW4 exact tool-result feedback updates native weighting/history
-> native selected-tool execution/composition
-> result/evidence returns to SIGMA native state
```

## Language axis

Current language lane evidence remains reusable:

```text
LANG-01A..LANG-01G=ADMITTED_IN_EXACT_TESTED_STRUCTURAL_SCOPES
LANG-02A=SOURCE_READY_R1_ADMISSION_NOT_RUN
```

Do not equate admitted structural language capabilities with general language understanding. The immediate integration objective after TW2 is to make native language/cognitive outputs drive TW1 demand signals rather than having host/GPT choose a tool.

## Governance

```text
SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY
ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY
ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
HOST_TOOL_COMPOSITION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
ANTI_HARDCODE=MANDATORY_ADMISSION_CONTROL
RUNTIME_PROOF_REQUIRED=YES
```

## Immediate next action

Run the exact TW1 source-ready bundle under the locked Termux SIGMAC/VM and preserve the first HOLD/FAIL or the complete `=== TW1 ADMISSION SUMMARY ===`.

On PASS, immediately checkpoint machine evidence and begin TW2 actual-capability registry binding. Do not return to V5K8A until this support axis reaches an explicit dependency reason to do so.
