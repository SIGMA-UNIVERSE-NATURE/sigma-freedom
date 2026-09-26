# SIGMA 06B3 Nonfrozen Native Curriculum

Date: 2026-09-27
Source: user-supplied Termux runtime output.

## Precheck

RUNTIME=SIGMA_VKM
SEMANTIC_HEAD_TARGET=68
FROZEN_GOLD_USED_FOR_TRAINING=NO

## 1. Select Sigma-native ready units

NATIVE_READY_POOL=48
SELECTED_TRAIN_UNITS=24

SLOT_0=4
SLOT_1=4
SLOT_2=4
SLOT_3=4
SLOT_4=4
SLOT_5=4

FROZEN_HALO_COLLISION=0

## 2. Materialize -> SHA -> emit

NATIVE_CURRICULUM=PASS

TRAIN_UNITS=24
TRAIN_PROBES=192
UNIQUE_PROBE_IDS=192

ROLE_BINDING=24
POLARITY_MODALITY=24
COREFERENCE=24
TEMPORAL_CAUSAL=24
CONTRAST_SENSITIVITY=24
MEANING_INVARIANCE=24
SOURCE_RECONSTRUCTION=24
PARAGRAPH_COHERENCE=24

NATIVE_SUPERVISION=YES
HOST_SEMANTIC_SUPERVISION=NO

## 3. Seal valid curriculum

06B3_NONFROZEN_CURRICULUM=PASS

NATIVE_READY_POOL=48
TRAIN_UNITS=24
TRAIN_PROBES=192
PROBES_PER_DIMENSION=24

NATIVE_SUPERVISION=YES
FROZEN_GOLD_USED_FOR_TRAINING=NO
LIVE_GEN3_MUTATED=NO
SEMANTIC_HEAD_TARGET=68

NEXT=TRAIN_68_NATIVE_SEMANTIC_HEADS_IN_GEN3_SANDBOX

PROOF_SHA256=
30d1fc6460d815a16884f27ad1c6e11b1754d6c350548bb11db5818abc18309b

## Interpretation boundary

This checkpoint records a valid nonfrozen native curriculum for Gen3:
- 24 selected native-ready training units;
- 192 unique probes;
- balanced coverage across eight semantic dimensions;
- native supervision enabled;
- no host semantic supervision;
- no frozen-gold use for training;
- no live Gen3 mutation.

The curriculum is sealed for the next sandbox training step targeting 68 native semantic heads.
