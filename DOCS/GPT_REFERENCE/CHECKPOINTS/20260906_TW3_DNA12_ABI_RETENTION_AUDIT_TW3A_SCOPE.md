# TW3 DNA-12 ABI Retention Audit — TW3A Scope Lock

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: DEPENDENCY_AUDIT_COMPLETE / TW3A_SCOPE_LOCKED

## Starting point

TW2 actual capability registry binding is machine-admitted:

```text
TW2_NATIVE_ACTUAL_CAPABILITY_REGISTRY_BINDING_V1=PASS
ACTUAL_CAPABILITY_TO_TW1_REGISTRY=PASS_IN_EXACT_TESTED_SCOPE
```

TW3 objective remains:

```text
SIGMA_NATIVE_TOOL_INTELLIGENCE
-> NATIVE_SCOPE_REQUEST
-> NATIVE_TW1_DEMAND_VECTOR
-> TW2
-> TW1
```

## DNA-12 admission evidence retained

DNA-12 Tool Intelligence has a native machine PASS checkpoint:

`SIGMA_PROFESSOR/CHECKPOINTS/20260905_DNA12_NATIVE_ADMISSION_PASS.md`

Exact retained identities:

```text
DNA12_SOURCE_SHA256=336152fca9e1112e9646249b5109c54835d52d9d0b5948d6bbf6703bf328920c
DNA12_BYTECODE_SHA256=7dc7cceab5442938a0846c811e98e8c367ab6beedfdefc7c281355f305f7fe70
DNA12_RUNNER_SHA256=1ccd798333134e1b2e3486dd33ef6a2ffa9d44bf563446484bf790a3a73fea1a
DNA12_SOURCE_READY_BUNDLE_SHA256=a010a4671c9f110f1780f43c1b8674243dddadbcd3762f734463e306beaa873a
DNA12_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
```

The post-admission state also records the canonical five tool-use signal dimensions:

```text
requires_current_external_state
requires_retrieval
requires_exact_computation
requires_observation_or_measurement
requires_external_action
```

and the four DNA-12 decision modes:

```text
THINK_ONLY
TOOL_ASSISTED_REASONING
THINK_AND_DECLARE_TOOL_GAP
THINK_AND_IDENTIFY_EVIDENCE_GAP
```

The historical Canon reference at blob `eda8a57900cd9ee88970120bc8b89eec5fd4aad3` additionally shows `candidate_tool` as part of DNA-12's decision context/decision record. This historical Python file is reference-only and is not permitted as active cognition.

## Retention audit result

The exact admitted native DNA-12 `.sigma` source bytes and admission-runner bytes are not retained as repository files on the current branch and are not present among the current conversation artifacts available to Teacher-GPT. The DNA-12 source-ready commit `07ad8ea637ac24d7c7a8bf26338364aa57dd4b73` added only the source-ready checkpoint, not the native source/runner files.

Therefore:

```text
DNA12_NATIVE_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
DNA12_EXACT_NATIVE_SOURCE_IDENTITY=KNOWN_BY_SHA256
DNA12_EXACT_NATIVE_SOURCE_BYTES_AVAILABLE_TO_CURRENT_TW3_BUILD=NO
DNA12_EXACT_NATIVE_RUNNER_BYTES_AVAILABLE_TO_CURRENT_TW3_BUILD=NO
DIRECT_DNA12_RUNTIME_REPLAY_IN_TW3=BLOCKED_BY_ARTIFACT_RETENTION
```

This is an artifact-retention/dependency-replay limitation. It is not evidence of a DNA-12 cognitive/runtime failure.

## Consequence: TW3A intermediate

Do not fabricate a native DNA-12 ABI from checkpoint prose and do not let Bash/GPT infer tool scope from natural language.

The admissible next intermediate is:

```text
TW3A_NATIVE_DNA12_DECISION_CONTRACT_TO_TOOL_DEMAND_BRIDGE
```

TW3A consumes a bounded structural DNA-12 decision-contract record containing:

- run identity;
- exact DNA-12 decision mode;
- candidate tool identity;
- tool availability;
- internal-reasoning-sufficient flag;
- the exact five canonical tool-use signal flags.

TW3A then natively:

1. validates decision-mode/signal coherence;
2. binds candidate-tool identity through a static capability-binding contract;
3. emits exact `SCOPE||...||COMMIT||YES` bytes for TW2;
4. emits the five exact TW1 demand flags without semantic rewriting;
5. refuses malformed/incoherent input;
6. exposes tool gaps and unbound candidates rather than inventing a scope.

The host may only copy exact native TW3A outputs into TW2/TW1 input files.

## Required claim boundary

```text
TW3A_DIRECT_DNA12_RUNTIME_BINDING=NOT_PROVEN
DNA12_NATIVE_EVENT_ABI_REPLAY=NOT_PROVEN
GENERAL_TOOL_CHOICE_FROM_ARBITRARY_NATURAL_LANGUAGE=NOT_PROVEN
LANG01G_AS_TOOL_INTENT_CLASSIFIER=NO
HOST_SCOPE_INFERENCE=NO
HOST_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_TOOL_RANKING=NO
SEMANTIC_UNDERSTANDING=NOT_PROVEN
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
```

LANG-01G remains a native reference/evidence-integration capability; its admitted scope does not establish tool-intent classification and it must not be repurposed as one by the host.

## Follow-on

```text
TW3A runtime PASS
-> retain/recover exact admitted native DNA-12 source+runner bytes
-> TW3B exact DNA-12 runtime event binding
-> replace decision-contract fixture with exact native DNA-12 output
-> preserve the same TW3A scope/demand bridge contract
```
