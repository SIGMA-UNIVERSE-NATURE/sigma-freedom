# SIGMA R21C — Scale/Stress + Admission Candidate PASS

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Candidate build

R21C_CANDIDATE_COMPILE_DETERMINISTIC=PASS

R21C_CANDIDATE_MATCHES_R21B_BYTECODE=PASS

R21C_CANDIDATE_BYTECODE_SHA256=
672c15d6e2c7da9342f50938e5f38542f3307490550f80a8b9233b4f11ea0e69

R21C_RECOVERY_DISPATCH_PREFLIGHT=PASS

## Scale/stress run

SCALE_ROWS=160

Crash points:
17
79
143

At each crash:
R21C_AUTOMATIC_RELAUNCH_AFTER_CRASH=PASS

Recovery observations:
- after crash at step 17:
  RECOVER||COUNT||35||PACK_END||875965
- after crash at step 79:
  RECOVER||COUNT||159||PACK_END||4070081
- after crash at step 143:
  RECOVER||COUNT||287||PACK_END||7367277

CRASHES_RECOVERED=3

R21C_MULTI_CRASH_AUTO_RESUME=PASS

## Final learning result

CRASH_FINAL_TACC=
1d39fe3b08e644a50232414829cc5e2f

CRASH_STEPS=160

Reference run:
REFERENCE_FINAL_TACC=
1d39fe3b08e644a50232414829cc5e2f

REFERENCE_STEPS=160
REFERENCE_CRASHES_RECOVERED=0

R21C_FINAL_TACC_DETERMINISTIC=PASS

R21C_PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS

R21C_COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS

## Independent verifier output

VERIFY||RECORDS||321||PACK_BYTES||8243100||COMMIT_BYTES||3852||EXPECTED_FOUND||1||WHOLE_PACK_READ||NO

Initial post-verify parser step failed only at:
R21C_FAIL=RECORD_COUNT_PARSE

Observed shell warning:
awk: warning: escape sequence '\|' treated as plain '|'

This failure occurred after the independent verifier output had already been produced and after scale/crash determinism had passed.

## Parser FIX / resume

Resume script SHA256:
128851f379a6a4c747b7b7782284aceb3baae6afc963054302e7433744f3f40a

The follow-up repair reused the existing verification artifact and corrected record-count parsing.

R21C_RECORD_COUNT_PARSE_FIX=PASS

SCALE_RECORDS=321

R21C_INDEPENDENT_NATIVE_VERIFIER=PASS

## Final candidate status

R21C_SCALE_STRESS_AND_ADMISSION_CANDIDATE=PASS

SCALE_ROWS=160
SCALE_RECORDS=321

SIMULATED_CRASH_POINTS=17,79,143
CRASHES_RECOVERED=3

MULTI_CRASH_AUTO_RESUME=PASS

FINAL_TACC=
1d39fe3b08e644a50232414829cc5e2f

FINAL_TACC_DETERMINISTIC=PASS

PACK_BYTE_IDENTICAL_TO_REFERENCE=PASS
COMMIT_BYTE_IDENTICAL_TO_REFERENCE=PASS

HOT_STORE_FILES=4
ACTIVE_STATE_OBJECT_FILES=0
ACTIVE_PER_OBJECT_WRITE_RECEIPTS=0
NEW_INODES_PER_OBJECT=0
DUPLICATE_APPEND_BYTES=0

INDEPENDENT_NATIVE_VERIFIER=PASS
WHOLE_PACK_READ=NO

CANDIDATE_BYTECODE_SHA256=
672c15d6e2c7da9342f50938e5f38542f3307490550f80a8b9233b4f11ea0e69

CANONICAL_MUTATION=NO
CURRENT_CANONICAL_RUNTIME_REPLACED=NO

ADMISSION=NO

READY_FOR_PRIVATE_ADMISSION_STAGE=YES

NEXT=
R21D_PRIVATE_ADMISSION_STAGE_AND_ROLLBACK_REHEARSAL

## Interpretation boundary

This checkpoint records R21C scale/stress qualification of the packed-private-store active-learning candidate.

The supplied evidence establishes:
- deterministic candidate compile;
- candidate bytecode matches the R21B FIX1 active-integration bytecode;
- recovery dispatch preflight passes;
- a 160-row run survives three injected process crashes;
- each crash is automatically relaunched and recovered;
- final TACC exactly matches an uninterrupted reference run;
- private.pack and private.commit are byte-identical to the uninterrupted reference;
- independent verifier sees 321 records, 8,243,100 pack bytes, and 3,852 commit bytes without whole-pack read;
- no per-object state files or per-object write receipts are created;
- new inodes per object remain zero;
- duplicate append bytes remain zero.

The intermediate RECORD_COUNT_PARSE failure was a post-verifier shell parsing defect, not a learning/storage semantic failure. The supplied repair resumed from the existing result and corrected parsing without rerunning the learning sequence from zero.

ADMISSION remains NO.
CURRENT_CANONICAL_RUNTIME_REPLACED=NO.

NEXT is R21D_PRIVATE_ADMISSION_STAGE_AND_ROLLBACK_REHEARSAL.
