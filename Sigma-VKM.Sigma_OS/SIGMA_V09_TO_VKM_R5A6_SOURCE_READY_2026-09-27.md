# SIGMA V09 -> VKM R5A6 Syntax-Aware Semantic Origin + Gain Gate Audit — Source Ready

Date: 2026-09-27
Branch: SIGMA_LIFE

R5A5 exposed a parser limitation: regex search could classify DEF-like text inside embedded/generated source as executable functions.

R5A6 repairs this by:
- accepting only top-level DEF declarations outside strings/comments;
- brace-matching exact function bodies;
- extracting calls from sanitized executable source;
- reverse-tracing real callers of v927p_sha256_lookup;
- comparing semantic-core bodies across all four builder variants;
- extracting exact AL68_target/train/loss/update/store bodies;
- extracting the native gain-gate source from SIGMA_GEN3_SEM68_STREAM_FIX2.sigma.

Safety:
TRAINING_ALLOWED=NO
SEMANTIC_EXECUTION_ALLOWED=NO
CANONICAL_MUTATION_ALLOWED=NO
OWNERSHIP_PROMOTION_ALLOWED=NO
GIA_ADMISSION_ALLOWED=NO
DNA15_ALLOWED=NO
NO_DISCOVERED_ARTIFACT_EXECUTION=YES
NO_UNBOUNDED_SCAN=YES

Locked inputs:
SEM68_CANDIDATE_SOURCE_SHA256=008d62f8120a112b0f4cfa27676e5d6f80f5b686c5aa76a080c568f04d0bee6b
TRAIN_CURRICULUM_SHA256=ce02e548381fe25cfaf1b5890cb9cfad250f9f1bfb7eb601b9099282424c9414
HEAD_REGISTRY_SHA256=7ee9bc9e9bc007490c0deed94463058a786b82d3952f039648bdce9fa6b33bf5

Release:
R5A6_RELEASE_VERIFY=PASS
R5A6_RUNTIME_SMOKE=PASS
BUNDLE_SHA256=2929beba33566e9588474b630d3ed2c5bac4b4f9bb1e33a106f61d1c79035587

R5B_TRAINING_AUTHORIZED=NO
NEXT=RUN_R5A6_AND_PROFESSOR_REVIEW
