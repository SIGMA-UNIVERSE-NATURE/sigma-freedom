# SIGMA Generalized Context-Aware Shadow Runtime Law N Skills R1

SCHEMA=SIGMA_GENERALIZED_CONTEXT_AWARE_SHADOW_RUNTIME_LAW_N_SKILLS_R1
STATUS=PASS
LAW_NAME=GENERALIZED_CONTEXT_AWARE_REPLAYABLE_SKILL_DELTA_LIBRARY
AUTHORITY=R22_SHADOW_RUNTIME_ONLY
BASE_R3_LAW_SHA256=5bb1f401b8b9991b77febc119fa5fb63aeba0f125ecd752ad53fba87ea1dcb93
RUNTIME_MODEL=BASE_PARENT_PLUS_CONTEXT_AWARE_DELTA_REPLAY
SKILL_COUNT_MODE=N
CAPABILITY_BINDING=SKILL_DECLARED_CAPABILITY_FIELD
ROLLBACK=DROP_DELTA_USE_PARENT
FULL_MODEL_DUPLICATION=NO
FULL_MODEL_CHECKPOINT=DEFERRED
LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO
NEXT=BUILD_N_SKILL_INDEX_SCHEMA_R1
GENERALIZED_CONTEXT_AWARE_SHADOW_RUNTIME_LAW_N_SKILLS_SHA256=ba0b427b0193b8334ef9e7d4d9c9b52fd024c67016a94041b2873441e3a495df

Key law rules:
- READY_SHADOW_DELTA only.
- R22 policy before bind.
- Positive TRAIN/DEV/CORE gain.
- Match task context to declared skill capability.
- Require selected/per-task replay hash match.
- Reject context mismatch, DEV/CORE regression, and missing capability binding.
- No duplicate skill ID; extensible index columns; require capability, replay SHA, and rollback semantics.

Boundary: reusable N-skill shadow law only. No live mutation, production admission, or cutover.
