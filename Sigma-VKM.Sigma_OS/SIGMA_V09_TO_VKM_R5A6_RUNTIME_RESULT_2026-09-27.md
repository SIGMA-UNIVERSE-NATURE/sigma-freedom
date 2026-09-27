# SIGMA V09 -> VKM R5A6 Syntax-Aware Semantic Origin/Gain Audit — Runtime Result

Date: 2026-09-27
Source: user-supplied Termux runtime output.
Branch: SIGMA_LIFE

## Identity

R5A6_LOCKED_INPUT_IDENTITIES=PASS

SEM68 candidate:
008d62f8120a112b0f4cfa27676e5d6f80f5b686c5aa76a080c568f04d0bee6b

Training curriculum:
ce02e548381fe25cfaf1b5890cb9cfad250f9f1bfb7eb601b9099282424c9414

Head registry:
7ee9bc9e9bc007490c0deed94463058a786b82d3952f039648bdce9fa6b33bf5

## Syntax-aware builder trace

v927p_sha256_lookup is a real top-level function.

Reverse closure is nontrivial:
v927p_sha256_lookup
<- v927p_probe_new
<- v927p_causal_reverse
<- v927p_coreference_change
<- v927p_irrelevant_insert
<- v927p_modality_change
<- v927p_paragraph_coherence
<- v927p_polarity_flip
<- v927p_reconstruction_mask
<- v927p_role_swap
<- v927p_temporal_reverse
<- higher probe/candidate routines.

Therefore the R5A5 self-call artifact was a parser false positive and is superseded.

## Native SEM68 target policy

Exact current AL68_target maps 17 fixed semantic classes to DIMENSION/MUTATION_OPERATOR strings in native source.

Examples:
class 0 -> CONTRAST_SENSITIVITY
class 1 -> COREFERENCE
class 2 -> MEANING_INVARIANCE
class 3 -> PARAGRAPH_COHERENCE
class 4 -> POLARITY_MODALITY
class 5 -> ROLE_BINDING
class 6 -> SOURCE_RECONSTRUCTION
class 7 -> TEMPORAL_CAUSAL
class 8 -> CAUSAL_REVERSE
...
class 15 -> ROLE_SWAP
class 16 -> TEMPORAL_REVERSE

AL68_train_one computes:
- native N_features/N_encode for original and mutated text;
- four relational views;
- 17 heads per view;
- target = AL68_target(c,dim,op);
- native squared loss;
- native gradient-like weight updates over 37 features per head.

TOTAL_HEAD_PARAMETERS=68*37=2516.

This is proven native supervised training.

Important claim boundary:
The target ontology is pre-authored/hardcoded in native source. This does not equal host runtime learning, but it also does not prove autonomous semantic-label discovery.

## Native persistence

AL68_train persists trained head weights through:
I_vsave -> U_store -> immutable object path under state/objects/<hash>.srl,
then writes SEM68.current pointer and emits HEAD_STORE_REF.

## Native gain mechanism

SIGMA_GEN3_SEM68_STREAM_FIX2.sigma contains AL68S_gate and emits HOST_GAIN_DECISION||NO.

The exact full AL68S_gate condition still needs a focused body audit before declaring exact native gain authority closed.

## Builder variants

Semantic-core fingerprints are not identical across all four builder variants:
- original and FIX1 share one fingerprint;
- FIX2 diagnostic differs;
- FIX2 safe diagnostic differs.

The historical active builder remains unbound.

## Current boundary

NATIVE_TRAINING_MECHANISM_PROVEN=YES
NATIVE_HEAD_UPDATE_PROVEN=YES
NATIVE_HEAD_PERSISTENCE_PROVEN=YES
NATIVE_TARGET_POLICY_PROVEN=YES
TARGET_ONTOLOGY_PREAUTHORED_IN_NATIVE_SOURCE=YES
AUTONOMOUS_SEMANTIC_LABEL_DISCOVERY_PROVEN=NO
HOST_RUNTIME_SEMANTIC_SUBSTITUTION_FOUND=NO_IN_TARGETED_SCOPE
ACTIVE_HISTORICAL_BUILDER_BOUND=NO
EXACT_GAIN_GATE_CONDITION_PROVEN=NOT_YET
R5B_TRAINING_AUTHORIZED=NO
GIA_ADMISSION_PERFORMED=NO
DNA15_ALLOWED=NO

NEXT=R5A7_EXACT_OPERATOR_ARGUMENT_AND_GAIN_GATE_BODY_AUDIT
