# SIGMA V09 -> VKM R4E Fresh Unseen Blind Anti-Shortcut Generalization — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE
Rule: CLAIM <= EVIDENCE

## Current prerequisite

R4D_FULL_NATIVE_ANTI_SHORTCUT_BEHAVIOR_REVALIDATION=PASS_IN_R13R6_SCOPE
SEMANTIC_BEHAVIOR_REVALIDATION=PASS_IN_R13R6_ANTI_SHORTCUT_SCOPE

R4D checkpoint commit:
660dde8ed59d754a1fad9c16982b68dae8e0463f

## R4E purpose

Test the same frozen accepted R13-R6 semantic substrate on a new evaluator-authored post-freeze anti-shortcut set that is not part of the donor corpus.

R4E is not training and does not mutate the head.

## Fresh set

FRESH_WORLD_COUNT=32
FRESH_FAMILY_COUNT=8
FRESH_DOCUMENT_COUNT=128

FRESH_SET_SPEC_SHA256=
7ee7ced73cc786a26865d02f819bb8135b99189a5dd021302b54bdc839312311

SOURCE_MAP_SHA256=
c5913fae4aaf3959f9ef84abdd6f9c093cb2d74605460bae0f21b0dbcf750efa

RELATIONS_SHA256=
e4810871e5e8363821f67f98ca509adba27cb9e22d2b9bea1b22e55e65106ddb

OPAQUE_INPUT_MANIFEST_SHA256=
b20e98ca53e38babc4da43492afd3b418b0a906828cf3392f3a308bc502c4311

Prepackaged evaluator audit:
FRESH_RAW_FEATURE_LEXICAL_TRAP=32_OF_32
FRESH_TOKEN_JACCARD_TRAP=32_OF_32
FRESH_EXACT_DONOR_TEXT_HASH_OVERLAP=0
FRESH_MIN_NOVEL_TOKEN_COUNT_PER_WORLD=21

## Precommitted admission floor

CROSS_VIEW_CORRECT >= 30/32
ALIAS_CORRECT >= 31/32
EACH_FAMILY_CROSS >= 3/4
EACH_FAMILY_ALIAS >= 3/4

No threshold changes are allowed after seeing frozen-head or native outputs.

If the frozen donor head fails this fresh-set floor during independent pre-runtime reference evaluation, native execution stops and the transfer remains HOLD.

## Runtime blinding

SIGMA_VKM receives only:
- 128 opaque text files;
- frozen head rows;
- native controller.

It receives no:
- world id;
- family id;
- anchor/positive/negative/alias role;
- expected state;
- expected behavior;
- reference or semantic mapping.

## Fresh-process protocol

Run 1:
fresh sigma-vkm process -> all 128 states -> seal output

Then process ends.

Run 2:
new sigma-vkm process -> same frozen state/input -> seal output

NO_RETEACH_BETWEEN_RUNS=YES

Independent verifier runs only after both outputs are sealed.

## Honesty boundaries

SIGMA_SELF_CERTIFICATE=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO

R4E pass means only:
FRESH_UNSEEN_GENERALIZATION=PASS_IN_R4E_ANTI_SHORTCUT_SCOPE

It does not establish general/deep language understanding or native ownership.

## Release

BUNDLE=
SIGMA_V09_TO_VKM_R4E_FRESH_UNSEEN_BLIND_ANTI_SHORTCUT_GENERALIZATION_BUNDLE.zip

BUNDLE_SHA256=
add6367133a74aa892015d153bd1674293c1de2cad4cd1e67826ea410c791207

RELEASE_VERIFY=PASS

Runtime:
NOT_YET_RUN

NEXT=RUN_R4E
