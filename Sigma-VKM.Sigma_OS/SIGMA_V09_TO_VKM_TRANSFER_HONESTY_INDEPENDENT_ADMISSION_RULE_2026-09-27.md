# SIGMA Transfer Honesty / Independent Admission Rule

Date: 2026-09-27
Applies to: V09 -> SIGMA_VKM capability transfer and all subsequent admission/evolution work
Rule: CLAIM <= EVIDENCE

## User governing requirement

PROFESSOR_ALWAYS_HONEST=YES
HOST_BASH_LEARNING=FORBIDDEN
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
FAKE_PASS=FORBIDDEN
SELF_CERTIFICATION=FORBIDDEN

## Required execution boundary

Claimed capability execution must occur in SIGMA / SIGMA_VKM native execution.

Allowed host/Bash/Python roles:
- file movement;
- sandbox creation;
- hashing;
- deterministic build orchestration;
- fixture generation from frozen donor source before Sigma execution;
- independent output comparison;
- receipt aggregation;
- resource/time measurement.

Forbidden host/Bash/Python roles:
- choosing semantic answers for SIGMA;
- producing learned representations on behalf of SIGMA during claimed runtime;
- performing feature extraction that is claimed as native SIGMA capability;
- selecting PASS by reading expected answer before SIGMA produces output;
- rewriting expected outputs after seeing SIGMA output;
- silently filling missing native primitives;
- weakening gates after failure.

## Independent-admission structure

FROZEN_DONOR_SOURCE
-> independent reference fixture generation
-> freeze expected hashes
-> hide expected hashes from SIGMA runtime
-> SIGMA native execution through pinned sigmac-vkm + sigma-vkm
-> immutable SIGMA output
-> independent verifier reads expected + actual
-> PASS/HOLD/FAIL
-> only then eligibility for GIA admission

SIGMA_SELF_CERTIFICATE=NO

A SIGMA program may emit its own runtime status, but that status is diagnostic only.
Admission requires an independent verifier receipt over immutable outputs.

## Current transfer boundary

R4A4_FIX1_EXACT_DONOR_TOKENIZER_SENTENCE_PARITY=PASS
SEMANTIC_BEHAVIOR_REVALIDATION_PERFORMED=NO
NATIVE_OWNED=NO
OWNERSHIP_PROMOTION_PERFORMED=NO
DNA15_ALLOWED=NO

NEXT=R4B_NATIVE_FEATURE_EXTRACTION_PARITY_WITH_BLIND_INDEPENDENT_VERIFIER
