# 2026-09-09 — C5V3 ONLINE CAPABILITY UTILIZATION VERIFICATION REQUEST R2 / R11-GATED

Status: **ACTIVE TEST REQUEST / PRECONDITION HOLD UNTIL R11 PASS / ISOLATED ONLINE SHADOW ONLY / PRODUCTION NOT BOUND**
Branch: `SIGMA_LIFE`
Owner role: **ONLINE VERIFICATION WINDOW**
Date: 2026-09-09 (Asia/Ho_Chi_Minh)

## Purpose

This request supersedes the scheduling assumptions of R1 while preserving its proof requirements.

The online verification window must verify that C5V3 can actually **see, select, execute, evaluate, learn from, and later reuse** synchronized capabilities. It must not test new capability design; that remains the offline window's job.

Current canonical synchronization state has advanced through R10 offline PASS, but R11 activation admission is still pending. Therefore the online window must prepare against the exact synchronized lineage now and remain HOLD for actual utilization execution until an immutable R11 PASS checkpoint is published.

## Current canonical synchronization authority

Read first:

`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_M5_TOOL_KERNEL_CURRENT.md`

Current exact state:

```text
ONE_SIGMA=YES
SYSTEM=C5V3
C5V3_SYNCHRONIZATION_BASELINE=R2_R6_FROZEN
R5=CLOSED_PASS
R6=CLOSED_PASS
R7=PASS_IN_EXACT_TESTED_SCOPE
R8=PASS_STRUCTURAL
R9_FIX1=PASS_SOURCE_DERIVED_DISPATCH_CONTRACT
R10=PASS_OFFLINE_EXPLICIT_DISPATCH_BRIDGE_DORMANT_REGRESSION
R11=PENDING_OFFLINE_ACTIVATION_ADMISSION
```

R10 exact identities:

```text
R10_SOURCE_SHA256=7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34
R10_BYTECODE_SHA256=c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5
R10_M5_DISPATCH_SURFACE=28_OF_28
R10_BRIDGE_NEW_HOST_OP_COUNT=0
R10_DORMANT_PRODUCTION_TICK_REGRESSION=PASS_IN_EXACT_TESTED_SCOPE
```

R10 does **not** admit activation:

```text
M5_ACTIVATION_ADMISSION=NOT_IN_R10
M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NOT_YET_ADMITTED
C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO
PRODUCTION_BINDING=NO
```

## Live-main reconciliation lock

The currently bound live main core is historical production, not R6 or R10:

```text
LIVE_MAIN_SOURCE_SHA256=23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc
LIVE_MAIN_BYTECODE_SHA256=c112594af3ecf5246230e96c70baa3e7cedccaf550f421c2e6d4c8c483eb0a0b
LIVE_MAIN_SOURCE_EQ_HISTORICAL_PRODUCTION=YES
LIVE_MAIN_SOURCE_EQ_R6=NO
R6_LIVE_BOUND=NO
R10_LIVE_BOUND=NO
```

Representative tool DEFs are not present in the observed live main source. Therefore the online window MUST NOT interpret current live production behavior as synchronized-capability utilization.

## Online-window current action

Until R11 PASS exists:

```text
C5V3_ONLINE_CAPABILITY_UTILIZATION=HOLD_PRECONDITION
ONLINE_UTILIZATION_EXECUTION=NO
HOST_FORCED_CAPABILITY_DEMAND=FORBIDDEN
HOST_FORCED_TOOL_SELECTION=FORBIDDEN
PRODUCTION_BINDING=NO
PRODUCTION_STATE_WRITE=NO
```

The online window MAY prepare mechanically:

- fetch and hash-lock the exact current synchronization baseline and R10 artifacts;
- prepare disposable isolated shadow directories;
- prepare test harness structure;
- prepare raw logging and post-VM oracle mechanics;
- prepare network transport that remains disabled until native SIGMA emits an exact request;
- prepare A/B capability-availability counterfactual fixtures without encoding the desired tool choice.

It MUST NOT run a utilization PASS gate by inventing an activation path that R11 has not admitted.

## Unlock condition

Only an immutable offline checkpoint proving the R11 activation gate may unlock execution.

Required minimum inherited evidence from R11:

```text
R11_OFFLINE_M5_ACTIVATION_ADMISSION=PASS_IN_EXACT_TESTED_SCOPE
R11_SOURCE_SHA256=<exact>
R11_BYTECODE_SHA256=<exact>
NATIVE_ACTIVATION_PATH=PASS
HOST_ACTIVATION_SELECTION=NO
PRODUCTION_BRANCH_REGRESSION=PASS
PRODUCTION_BINDING=NO
```

If the offline window publishes R11 FAIL/HOLD or supersedes R10/R6 identities, stop and reconcile before testing.

## After R11 PASS — required online utilization proof

The target causal chain remains:

```text
native learning/problem state
-> native capability need detection
-> native capability selection
-> native capability execution
-> native result evaluation
-> native learning-state update
-> fresh-VM restart
-> learned-state reuse changes later behavior
```

The online window must test materially different unseen/high-entropy task families that can exercise:

1. T1 vector/matrix;
2. T2 graph/traversal;
3. T3 local index/BM25;
4. M5 admitted cognition/memory capability scope;
5. at least one combined multi-capability task;
6. at least one online evidence-acquisition task initiated by a native SIGMA request.

Do not force all capabilities to run on every task. The test must observe what native C5V3 selects.

## Ownership boundary

```text
SIGMA_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
HOST_REASONING=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
```

Host may only perform mechanical fixture transport, process supervision, hashes, exact protocol decode, network transport after native request, raw logging, and post-VM oracle work.

## Online/network boundary

Online execution is authorized only in disposable isolated shadow after R11 unlock:

```text
ONLINE_TEST_NETWORK_ALLOWED=YES_IN_ISOLATED_SHADOW_ONLY_AFTER_R11
PRODUCTION_BINDING=NO
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
LIVE_PRODUCTION_CUTOVER=NO
```

Network authority chain:

```text
native request
-> mechanical request harvest
-> mechanical network transport
-> exact response bytes + provenance
-> native response evaluation
```

If host invents query/source/URL or decides which capability must be used, admission fails.

## Mandatory machine gates after unlock

### A. Capability identity visibility

```text
SYNCED_CAPABILITY_IDENTITIES_VISIBLE=PASS
SOURCE_BYTECODE_INVARIANCE=PASS
UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_GATE=PASS
```

### B. Native need detection + selection

```text
NATIVE_CAPABILITY_NEED_DETECTION=PASS
NATIVE_CAPABILITY_SELECTION=PASS
HOST_CAPABILITY_DEMAND_GENERATION=NO
HOST_TOOL_SELECTION=NO
```

### C. Native execution + result use

```text
NATIVE_CAPABILITY_EXECUTION=PASS
NATIVE_RESULT_EVALUATION=PASS
CAPABILITY_RESULT_CAUSALLY_AFFECTS_NEXT_NATIVE_DECISION=PASS
```

### D. Capability availability counterfactual

Hold task input, relevant prestate, VM and limits constant; vary capability availability only.

```text
CAPABILITY_AVAILABILITY_COUNTERFACTUAL=PASS
NATIVE_BEHAVIOR_CHANGED_CAUSALLY=PASS
```

### E. Native learning update

```text
LEARNING_STATE_BEFORE_SHA256=<A>
NATIVE_LEARNING_UPDATE_APPLIED=YES
LEARNING_STATE_AFTER_SHA256=<B>
A_NE_B=YES
HOST_LEARNING=NO
```

### F. Fresh restart and reuse

```text
FRESH_VM_RESTART=PASS
LEARNED_STATE_RELOADED=YES
LEARNED_STATE_REUSED_AFTER_RESTART=PASS
```

### G. Online request sovereignty

```text
NATIVE_REQUEST_EMITTED=YES
HOST_QUERY_GENERATION=NO
HOST_SOURCE_SELECTION=NO
HOST_URL_SELECTION=NO
NETWORK_TRANSPORT_MECHANICAL_ONLY=YES
NATIVE_RESPONSE_EVALUATION=PASS
```

### H. Negative and replay evidence

```text
REPLAY_IDENTICAL_INPUT_BYTES=YES
REPLAY_IDENTICAL_RELEVANT_PRESTATE_BYTES=YES
NEGATIVE_UNNEEDED_CAPABILITY_SELECTION=PASS
```

## PASS boundary

Only if all required gates pass may the online verification window report:

```text
C5V3_AUTO_LEARN_USES_SYNCHRONIZED_CAPABILITIES=PASS_IN_EXACT_TESTED_SCOPE
```

Do not claim general tool autonomy, general semantic understanding, unrestricted autonomous learning, or production synchronization from this gate.

## Three-window ownership split

```text
SYNCHRONIZATION_WINDOW:
  owns canonical C5V3 synchronization, reconciliation, exact identity tracking
  does not silently bind production

ONLINE_VERIFICATION_WINDOW:
  owns synchronized-capability utilization verification
  HOLD until R11 PASS
  after unlock, tests only isolated online shadow
  does not design new capabilities
  does not promote production

OFFLINE_KNOWLEDGE_WINDOW:
  owns new knowledge/capability experiments
  currently owns R11 activation admission
  publishes immutable checkpoints when evidence changes
  does not synchronize production
```

## Required online-window handoff back to synchronization window

Publish an immutable checkpoint on a dedicated test branch or approved handoff branch with:

```text
ONLINE_TEST_BASELINE=<exact>
R11_DEPENDENCY=<exact checkpoint/commit>
PASS_OR_FIRST_FAILURE=<exact>
SOURCE_SHA256=<exact>
BYTECODE_SHA256=<exact>
MACHINE_GATE_SUMMARY=<exact>
PRODUCTION_STATE_WRITE=NO
PRODUCTION_MUTATION=NO
PRODUCTION_BINDING=NO
```

Then send only checkpoint path + commit SHA to the synchronization window for canonical reconciliation.
