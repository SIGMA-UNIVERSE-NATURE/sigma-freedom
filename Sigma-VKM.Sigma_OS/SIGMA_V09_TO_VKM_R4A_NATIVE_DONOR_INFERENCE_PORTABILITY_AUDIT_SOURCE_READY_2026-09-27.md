# SIGMA V09 -> VKM R4A Native Donor Inference Portability Audit — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Mode: READ_ONLY_PORTABILITY_AUDIT

## Why R4A exists

The exact current api410_integrate source was inspected.

api410_integrate is the integrated current SIGMA_VKM language/task pipeline and is suitable as a current-VKM regression baseline.

It is not the R13-R6 donor executor:
- no frozen R13-R6 head parameter;
- no donor feature extraction;
- no donor frozen encoder;
- no donor pair-distance path.

Therefore direct API410 replay cannot prove transfer of the accepted R13-R6 semantic substrate.

## Correct next transfer target

The exact donor inference path must be ported:

TEXT
-> feat(text)
-> frozen head encode(features, weights)
-> dist(state_a,state_b)
-> anti-shortcut same-world vs altered-world comparison

Training is not required for the first transfer gate because the accepted donor head is frozen.

## Exact donor locks

DONOR_BUNDLE_SHA256=
f5e72217d6c26b55d3fad7185e9e007814271b577e64f9ca2d658b7a604426fc

DONOR_HEAD_SHA256=
cc041d7583367104692b0d5af5753fbbbf754a86c5126543ea2456c41a43cba0

DONOR_RUN_EXPERIMENT_SHA256=
7fd12d2a1709fa1fe469ad8dc091e894eaf940afaf0bb13b4a550997ef0091cc

Critical function hashes:
h64=949a67f2aa0f03d4dc2fbc6f691550542c27fafb56bd7fd9481853fbef55f35c
bucket=085ee98d65b3832d79b73f8f91b171aa10edeb7e564608e8fdc5a7d6abb65e3a
words=54745e0eef2fd5d0b8685fdc6dd808b8b27a8f85d390f5bb23448c3310d3f3aa
sentences=4d97c58345ab752d90db8745a3dcc223af8b5c4e0aea372556f8224644fcf3f2
feat=99e93d0f12b109f96092716e5a0252d4a3eddf13576a5b3ac143a5d8b23ee9c2
layout=7f0580b7f3b9bdbc3e5f398932146aca0f695aec057afc31ef7c70194c5b89ef
encode=a092905e0088fc30c1132a2797c5ec6ba25b875733db70a506364a72c123d074
dist=2ef05a4df08b11ca50a6a736b00fd9144f02bc135b704b8978b5d2d753b93d27
substrate_eval=6d6b0b1c29007e601debb836ddbc4fe128b1a051ea974639ac3daa248c3e3424

Frozen head shape:
HASH_BUCKETS=4096
FANOUT=8
STATE_DIMENSION=256
QUESTION_LABELS_USED_TO_TRAIN_ENCODER=NO

## R4A audit purpose

Measure whether the current SIGMA_VKM source/runtime already exposes sufficient native mechanical primitives to implement the exact donor inference algorithm.

Required operation families include:
- SHA-256 string hashing;
- exact UTF-8 read;
- donor-compatible tokenization and sentence splitting;
- sparse counter/map;
- substring/character n-grams;
- sort/dedupe and pair combinations;
- sqrt normalization;
- tanh;
- integer/digest conversion and modulo;
- numeric vector loops;
- explicit frozen-state load.

R4A uses source-name evidence only to discover candidate primitives. It does not claim a primitive is semantically equivalent from a name match.

## Safety

CANONICAL_MUTATION_ALLOWED=NO
OWNER_REBIND_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
DNA15_ALLOWED=NO
SEMANTIC_BEHAVIOR_CLAIM_ALLOWED=NO

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4A_NATIVE_DONOR_INFERENCE_PORTABILITY_AUDIT_BUNDLE.zip

BUNDLE_SHA256=
f1a7f0a33036033da7143c88be8d039bf8528e0821343c05186fc419815f5e08

R4A_RELEASE_VERIFY=PASS
RUNTIME_STATUS=NOT_YET_RUN

NEXT=RUN_R4A_THEN_BUILD_R4B_EXACT_NATIVE_FROZEN_ENCODER
