# C5 Native Experience-to-Strategy Adviser V1 — Contract

Status: `SOURCE_READY_PENDING_LOCKED_ADMISSION`

## Purpose

Add a bounded native meta-learning tool to the one existing C5 V3 SIGMA instance.

The tool does not decide truth, does not repair, does not write C5 cognitive state, does not generate work candidates, and does not encode a teacher-selected answer. It may write only bounded invocation-output files inside its isolated `.sigma_exec/.../output` scratch directory. It receives a bounded candidate catalog plus mechanically aggregated outcome history and lets native SIGMA select one currently available candidate from runtime evidence.

Target gap:

`retained experience -> native strategy arbitration -> later C5 work/tool/revisit choice`

This is intended to complement, not replace, already admitted DNA16 experience retention and DNA17 two-level learning capabilities.

## One-SIGMA binding

- Canonical instance fingerprint:
  `fa2834a009f666738129d102dff5b6f09a3c1333c2f2aec8dbd4ac8680a8d125`
- C5 native core SHA256:
  `1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace`
- Production state lineage:
  `$HOME/SIGMA/sigma_genesis1/.sigma_c5_real_shadow_v2`
- C5 V3 remains the sole cognitive-state writer.
- This adviser is stateless in production design.
- No second persistent SIGMA is created.

## Artifacts

Native source:
`SIGMA_PROFESSOR/artifacts/SOURCES/C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1.sigma`

`SOURCE_SHA256=b1f48b157a4603e19f013dae92f3792cc2b7e9e26327faec7dd9b8bbcd599304`

Mechanical builder:
`SIGMA_PROFESSOR/artifacts/TOOLS/C5_MECHANICAL_EXPERIENCE_TO_STRATEGY_INPUT_BUILDER_V1.py`

`BUILDER_SHA256=084e58de4c284020b8ed79f1173a97772fde59262e562e494df980fe69106444`

Admission runner:
`SIGMA_PROFESSOR/artifacts/RUN_C5_NATIVE_EXPERIENCE_TO_STRATEGY_ADVISER_V1_ADMISSION.sh`

## Runtime evidence fields

For each candidate, bounded to at most four candidates:

- stable candidate id
- opaque candidate token
- availability
- mechanical readiness
- attempt count
- material-producing attempt count
- evidence units persisted
- knowledge units persisted
- segment commits
- hard-failure count
- immediately repeated identical failure-fingerprint count
- unresolved-count improvement count
- unresolved-count worsening count

The builder may only aggregate these exact mechanical facts. It must not emit a selected candidate, semantic score, recommendation, relevance score, trust score, teacher choice, topic mapping, or expected answer.

Failure fingerprints are opaque SHA256 values. The native source contains no concrete failure reason such as `BINARY_OR_UTF16_UNSUPPORTED` or `SEGMENT_DENSITY_LIMIT`.

## Native arbitration rule

For each available candidate, native SIGMA derives:

`GOOD_UNITS = material_success + evidence_units + knowledge_units + segment_commits + unresolved_improve`

`BAD_UNITS = hard_failures + repeated_failures + unresolved_worsen`

Candidates are compared by empirical net yield per bounded attempt using cross multiplication; no host ranking is supplied. Ties prefer:

1. fewer repeated identical failures,
2. fewer prior attempts (bounded exploration pressure),
3. greater mechanical readiness,
4. lower stable candidate id.

This is a teacher-authored bootstrap arbitration policy, not a learned policy and not proof of semantic understanding. The selected runtime candidate is not prewritten.

## Anti-hardcode lock

`PRELOADED_SELECTED_CANDIDATE=NO`

`EXPECTED_RUNTIME_CANDIDATE_TOKEN=ABSENT`

`CONCRETE_FAILURE_TO_ACTION_MAPPING=ABSENT`

`HOST_CANDIDATE_SELECTION=NO`

`HOST_SEMANTIC_SCORING=NO`

`HOST_LEARNING=NO`

`NATIVE_SELECTION_FROM_RUNTIME_EVIDENCE=REQUIRED`

Fixed protocol/status vocabulary is not a teacher-selected cognitive conclusion.

## Admission requirements

- exact locked sigmac identity
- exact locked VM identity
- exact C5 V3 runner identity
- source and builder SHA256 identity
- C5 V3 process alive before and after
- locked compile succeeds
- locked VM executes bounded fixtures
- native output is a currently available catalog member
- replay identical input gives identical selection
- catalog reorder invariance
- history counterfactual can change selection
- availability counterfactual can change selection
- readiness can break a factual tie
- no-available-candidate path
- malformed catalog refused by builder
- duplicate candidate id refused by builder
- duplicate candidate token refused by builder
- semantic-selection keys refused by builder
- source contains no concrete observed C5 failure labels
- source contains no expected candidate token
- no production binding during admission

## Claim boundary

Passing admission would establish only a bounded native experience-conditioned candidate arbitration capability in the exact tested schema.

It would not prove:
- semantic understanding,
- globally optimal learning policy,
- autonomous software repair,
- truth,
- production C5 integration,
- production work-quality improvement,
- learned arbitration weights/policy.

Production binding must be additive and must not restart or replace the sole C5 V3 cognitive writer merely to install this capability.
