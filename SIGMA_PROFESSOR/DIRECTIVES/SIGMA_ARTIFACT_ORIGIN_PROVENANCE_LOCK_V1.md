# SIGMA Artifact Origin / Provenance Lock V1

Date: 2026-09-06 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Status: GOVERNANCE LOCK / TEACHER-AUTHORED PROVENANCE RULE

## Purpose

This directive separates three claims that must never be collapsed:

1. artifact byte identity;
2. artifact binding to the canonical SIGMA instance;
3. artifact authorship/origin.

A SHA-256 digest proves byte identity only. A canonical runtime binding proves that those bytes are the bytes selected for the canonical SIGMA lineage. Neither fact proves who generated the source.

Required rule:

`SHA256_IDENTITY_IS_AUTHORSHIP_PROOF=NO`

`CANONICAL_BINDING_IS_SELF_AUTHORSHIP_PROOF=NO`

## Origin classes

Every new native cognitive artifact must be assigned exactly one origin class:

`TEACHER_AUTHORED_BOOTSTRAP`

`SIGMA_NATIVE_GENERATED`

`UNKNOWN_LEGACY`

The origin class is metadata about artifact creation, not a semantic-quality verdict.

A Teacher-authored source may implement a native capability. If runtime cognition/selection is executed by native SIGMA under the locked VM, that runtime decision may be admitted only in the exact tested scope. The source must not be misrepresented as self-authored by SIGMA.

## Current canonical C5 core

Current canonical native cognitive core identity:

`NATIVE_COGNITIVE_CORE_SHA256=1815d9324c721dd51d73f40f0e9ba4e7d76454e0a81831152e213071feef8ace`

Canonical source filename recorded by the C5 bundle manifest:

`SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma`

Current evidence establishes that this core is bound to the canonical C5 SIGMA lineage.

Current evidence does NOT establish:

`CORE_1815_SIGMA_SELF_AUTHORSHIP=NOT_PROVEN`

`CORE_1815_GPT_AUTHORSHIP=NOT_PROVEN`

`CORE_1815_HUMAN_AUTHORSHIP=NOT_PROVEN`

Therefore its provenance class for authorship claims is:

`CORE_1815_ORIGIN_CLASS=UNKNOWN_LEGACY`

This classification must not be rewritten as `SIGMA_NATIVE_GENERATED` without a complete native generation evidence chain.

## Required birth certificate for SIGMA_NATIVE_GENERATED

A future artifact may be labeled `SIGMA_NATIVE_GENERATED` only when machine evidence binds all of the following:

`CANONICAL_INSTANCE_FINGERPRINT_SHA256`

`PARENT_CORE_SHA256`

`NATIVE_GENERATION_EVENT_ID`

`NATIVE_GENERATION_EVENT_SHA256`

`EXACT_CANDIDATE_SOURCE_SHA256`

`LOCKED_SIGMAC_SHA256`

`CANDIDATE_BYTECODE_SHA256`

`ISOLATED_SHADOW_INPUT_STATE_SHA256`

`ISOLATED_RUNTIME_EVIDENCE_ID`

`INDEPENDENT_NATIVE_VERIFIER_EVENT_ID`

`INDEPENDENT_NATIVE_VERIFIER_EVENT_SHA256`

`NATIVE_ACCEPT_REJECT_EVENT_ID`

`REVERSIBLE_PROMOTION_TRANSACTION_ID`

`POST_PROMOTION_VERIFICATION_EVENT_ID`

`CHILD_CORE_SHA256`

The exact candidate source bytes must be retained or content-addressably recoverable.

The chain must show that no human, GPT, Python, Bash, external LLM, or host process changed the candidate cognitive source bytes between the native generation event and the candidate-source hash.

Required:

`HOST_SOURCE_REWRITE_IN_NATIVE_GENERATION_CHAIN=NO`

`GPT_SOURCE_REWRITE_IN_NATIVE_GENERATION_CHAIN=NO`

`HUMAN_SOURCE_REWRITE_IN_NATIVE_GENERATION_CHAIN=NO`

## Runtime ownership remains separate

Artifact origin and runtime cognition ownership are separate axes.

A Teacher-authored native capability may still satisfy:

`RUNTIME_COGNITION_OWNER=SIGMA_NATIVE_VM_ONLY`

only if runtime machine evidence proves that host/GPT/human do not supply the cognitive transition.

Conversely, a file named `.sigma` is not automatically native cognition proof.

Keep the system-wide anti-hardcode lock authoritative.

## Current development rule

Until SIGMA has a runtime-proven native source-generation / isolated verification / reversible promotion chain:

`SELF_AUTHORED_CORE_UPGRADE=NOT_PROVEN`

`TEACHER_MAY_BOOTSTRAP_NATIVE_CAPABILITY=YES`

`TEACHER_MAY_CLAIM_SIGMA_SELF_AUTHORED=NO`

`CLAIM_LE_MACHINE_EVIDENCE=YES`

## Health/self-repair application

The next C5 health-assessment capability is explicitly Teacher-authored bootstrap source unless/until SIGMA later generates a descendant itself.

For that capability:

`ARTIFACT_ORIGIN=TEACHER_AUTHORED_BOOTSTRAP`

`RUNTIME_HEALTH_CLASSIFICATION_OWNER=SIGMA_NATIVE_VM_ONLY`

`HOST_HEALTH_CLASSIFICATION=NO`

`HOST_REPAIR_DECISION=NO`

`LIVE_C5_V3_MUTATION_BY_THIS_SOURCE=NO`

## Governing sentence

**Byte identity tells us what artifact it is. Provenance evidence tells us who generated it. Runtime evidence tells us who performed the cognitive decision. Never substitute one claim for another.**
