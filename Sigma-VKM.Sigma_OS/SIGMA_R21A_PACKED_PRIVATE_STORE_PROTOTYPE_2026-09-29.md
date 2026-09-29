# SIGMA R21A — Packed Private Store Prototype

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Native patch / deterministic compile

R21A_NATIVE_PATCH=PASS

R21A_COMPILE_DETERMINISTIC=PASS

BYTECODE_SHA256=
bd8a818f95bc9c7be6157b02fb8604fb0e2b935671b7d678dc5e37240b3c7b55

## Store / dedup behavior

First object:
STORE||3d56706306cafc34095029bc71a446ee||APPENDED||104||PACK_BYTES||92||COMMIT_BYTES||12

Duplicate write:
STORE||3d56706306cafc34095029bc71a446ee||APPENDED||0||PACK_BYTES||92||COMMIT_BYTES||12

DUPLICATE_APPEND_BYTES=0

## Crash / resume behavior

SIMULATED_PROCESS_CRASH=YES
R21A_FIRST_PROCESS_INTERRUPTED=PASS

Recovery:
RECOVER||COUNT||1||PACK_END||92

Second logical object after recovery:
STORE||5ff771716415ecb53ea316b177023328||APPENDED||4153||PACK_BYTES||4233||COMMIT_BYTES||24

Final status:
STATUS||COUNT||2||PACK_END||4233

R21A_AUTO_RESUME=PASS
R21A_FRESH_PROCESS_BYTE_EXACT_RESTORE=PASS

## Final prototype status

R21A_PACKED_PRIVATE_STORE=PASS

HOT_STORE_FILES=4
LOGICAL_OBJECTS=2
PER_OBJECT_FILE_COUNT=0
NEW_INODES_PER_OBJECT=0

CRASH_RECOVERY=PASS
AUTO_RESUME=PASS
FRESH_PROCESS_BYTE_EXACT_RESTORE=PASS

RETEACH=NO
FULL_STATE_COPY=NO
CANONICAL_MUTATION=NO
REAL_DATA_DELETE=NO

PROTOTYPE_ONLY=YES
ACTIVE_U_STORE_REPLACED=NO

NEXT=
R21B_INDEPENDENT_VERIFIER_AND_ACTIVE_LEARNING_INTEGRATION

## Interpretation boundary

This checkpoint records the R21A packed-private-store prototype.

The supplied evidence establishes:
- deterministic native build;
- packed storage for logical private objects;
- duplicate write is idempotent with zero appended bytes;
- simulated process interruption is recovered;
- controller/store resumes and accepts the next logical object;
- fresh-process byte-exact restore passes;
- no per-object files are created;
- new inodes per logical object remain zero;
- no reteaching occurs;
- no full-state copy occurs;
- canonical state is not mutated;
- no real-data deletion occurs.

This is explicitly PROTOTYPE_ONLY.
ACTIVE_U_STORE_REPLACED=NO.

Therefore this checkpoint does not claim the existing active private U-store has been replaced or that R21 is production-integrated.

NEXT is R21B_INDEPENDENT_VERIFIER_AND_ACTIVE_LEARNING_INTEGRATION.
