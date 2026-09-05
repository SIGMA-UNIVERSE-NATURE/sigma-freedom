# V4-B2R.2 REAL V2.4 RC9 REPLAY — SOURCE READY

Date: 2026-09-05 Asia/Ho_Chi_Minh

## Purpose

Repair the V4-B2R.1 harness idempotency failure without changing the admitted native V4-B learner.

## Native learner

Source remains:

`SIGMA_PROFESSOR/artifacts/SIGMA_V4_SEGMENTED_RECEIVED_CONTEXT_LEARNER_V4B1.sigma`

SHA256:

`2edd2d4f36d3dd9c2d03dab4218ceff1f2ef290feee711a49ef18ff53b056ad4`

No native learner logic changed in this correction.

## R2 runner

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B2R2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT.sh`

Git blob:

`977c8fa80af5eea00e21ed9c82c7e7d4394ee2bf`

Commit:

`15b070d0f3bc11be676eb6f59789974848682183`

## Correction

Each preflight run gets a fresh shadow namespace.

Each exact production raw context is mechanically installed into shadow through:

`partial file -> exact SHA verification -> chmod 0400 -> atomic rename`.

The harness does not choose a segment, completion state, retry state, or learning result.

It still invokes the same native V4-B learner exactly 35 times per real context and verifies final native completion evidence.

## Scope

Five observed V2.4 held contexts with `VM_RC=9` are replayed from production raw storage read-only.

Production BRAIN is not a write target. Production V2.4 must remain running unchanged.

## Claim boundary

Before runtime PASS keep:

`REAL_V24_RC9_CONTEXT_RECOVERY=NOT_PROVEN`

`V4_PRODUCTION_PROMOTION_ALLOWED=NO`

On PASS only the five-observed-held-context recovery scope may be admitted.
