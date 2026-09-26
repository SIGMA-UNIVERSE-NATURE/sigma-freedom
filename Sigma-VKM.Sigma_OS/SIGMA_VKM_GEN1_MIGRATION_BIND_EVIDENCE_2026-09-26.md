# SIGMA VKM Generation 1 Migration / Bind Evidence

Date: 2026-09-26
Source: user-supplied Termux runtime output.

This checkpoint records the observed migration/bind result exactly as supplied.
It does not claim more than the runtime lines below establish.

## Runtime evidence

VKM_GEN1_BIND=PASS

VKM_GEN1_CURRENT=/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/SIGMA_VKM_GEN1_BACKEND.current

GEN1_BRAIN_HEAD=700d5c1b4845322d7c14800029c629b0

GEN1_MODEL_GENERATION=1

GEN1_MODEL_ID=25f78a8a17d8ec8957545f2f747170c0

GEN1_MODEL_ROOT_REF=25f78a8a17d8ec8957545f2f747170c0

GEN1_SNAPSHOT_SHA256=63facb281d8f511cd99653ddb9adfd1d426e951ece559a30254cd41c9c78967d

GEN1_NATIVE_STATE_ENGINE_SHA256=6041c02a81b3f4e7bedaf7d68b99b44a0bd01760522123d9844e57436d512896

STATE_COPY_CREATED=NO

STATE_MUTATED=NO

SECOND_SIGMA_CREATED=NO

DO_NOT_REDISCOVER_GEN1=YES

NEXT=WIRE_VKM_EXECUTION_TO_THIS_BACKEND

## Interpretation boundary

The supplied evidence directly establishes:
- the Gen1 backend bind step reported PASS;
- the active model generation field reported 1;
- model ID and model root reference match;
- the snapshot and native state engine hashes were emitted;
- no state copy and no second Sigma were reported;
- next integration step is to wire VKM execution to this backend.

This checkpoint is migration/bind evidence. Any stronger claim about end-to-end execution, restart retention, protected regression, or autonomous Gen1 operation requires separate runtime evidence.
