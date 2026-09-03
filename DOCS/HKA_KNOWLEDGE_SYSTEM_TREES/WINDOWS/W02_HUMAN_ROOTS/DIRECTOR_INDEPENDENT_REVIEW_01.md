---
title: "HKA W02 — Director Independent Review 01"
window_id: "W02"
review_status: "TARGETED_CORRECTIONS_REQUIRED_BEFORE_IMAGE_PRODUCTION"
reviewed_academic_commit: "e900d3b623c27f6d4a0fe2750fa499295788776e"
reviewed_final_commit: "73c55dc9825dc1113f444c2a5c7468ee9ef09b43"
date: "2026-09-04"
---

# HKA W02 — DIRECTOR INDEPENDENT REVIEW 01

## 1. Decision

```text
ACADEMIC PROGRAM: PASS
ACADEMIC QA: PASS
PROGRAM → VISUAL DESIGN: PASS
P18 / 18 UNIQUE VISUAL JOBS: PASS
PROMPT CONTENT QUALITY: PASS
BATCH MAP 2 / 6 / 6 / 4: PASS
PRODUCTION HANDOFF INTEGRITY: RETURN FOR TARGETED CORRECTIONS
DIRECTOR ACCEPTED FOR IMAGE PRODUCTION: NO — NOT YET
```

No rewrite of TREE/NODE/RELATION/SOURCE or the 18 visual concepts is requested.

## 2. Accepted without correction

- 21/21 canonical Human Roots concepts are covered at foundation/root depth.
- 24 nodes, 63 relations, 32 sources and 42 stable material claims form a coherent graph.
- Claim/source and certainty/content-class separation are strong.
- D1–D4 progression, misconceptions, HKA Compass, ownership boundaries and specialist handoffs are substantively handled.
- P18 is justified as the smallest sufficient package; no one-image-per-node inflation was found.
- The 18 prompt concepts preserve important truth boundaries: no face-reading, memory-camera, linguistic determinism, identity essentialism, free-will overclaim, fairness single-formula, conflict=violence, responsibility collapse, culture essentialism, history=false-equivalence, scenario=forecast or effort-only plasticity.
- B00 asset 0001 + 0002 is a good calibration pair.

## 3. Targeted blocking corrections

### W02-DIR-001 — P0 — Prompt Content Commit SHA is not the final immutable prompt package

Current prompt records/manifests point to:

```text
65c852bfd12adc94745c65a5c8e900c40ef501c5
```

But the final four `BATCH_PROMPTS.md` files were created after that commit, and `VISUAL_PROMPTS_CINEMATIC_4K.md` was subsequently changed. Therefore that SHA cannot serve as the production `PROMPT_CONTENT_COMMIT_SHA` required by the two-commit protocol.

Required correction:

1. Freeze the final prompt registry + all four final `BATCH_PROMPTS.md` files.
2. Commit them together; this new SHA becomes `PROMPT_CONTENT_COMMIT_SHA`.
3. Only afterward create/update manifests that reference that exact SHA.

Academic content SHA `e900d3...` remains unchanged.

### W02-DIR-002 — P0 — All four BATCH_MANIFEST.json records fail the canonical manifest schema

The canonical schema requires fields including:

```text
schema_version
window_id
tree_id
tree_slug
prompt_repository
prompt_branch
prompt_commit_sha
brand_repository
brand_asset_commit_sha
batch_id
run_id
asset_count
assets
status = BATCH_READY
```

and required per-asset fields including asset type, representation type, audience, depth and companion.

Current W02 manifests use a different abbreviated structure (`run_id_planned`, `PROMPT_LOCKED_NO_RUN`, extra fields not admitted by the schema, missing required fields/asset metadata).

Required correction: rebuild B00–B03 manifests exactly against the active JSON Schema. Academic SHA may remain in auxiliary W02 records, but not as an undeclared manifest field while `additionalProperties=false`.

### W02-DIR-003 — P0 — Prompt SHA-256 does not bind the complete resolved A–J record

The accepted prompt template requires hashing the canonical full A–J prompt record, excluding only the prompt-hash line. W02 states that a full record is resolved from `G-W02-PROMPT-2.0` + the asset-specific batch block, but hashes only the asset block.

This means changing inherited static A–J production locks could leave the asset hash unchanged.

Required correction: define one deterministic canonical resolved payload per asset that includes both inherited static fields and asset-specific fields, then recalculate all 18 prompt SHA-256 values. Materializing 18 separate files is optional; deterministic reproducibility is mandatory.

### W02-DIR-004 — P1 — Manifest SHA-256 sidecars are missing

Canonical batch hashing requires:

```text
BATCH_MANIFEST.sha256
```

for each batch. Current batch directories contain only manifest + prompt files.

Required correction: after schema-valid manifests are finalized, canonicalize/hash each manifest and create sidecars for B00–B03 before production handoff.

## 4. Targeted correction sequence

```text
KEEP ACADEMIC COMMIT e900d3... UNCHANGED
→ resolve/freeze all 18 complete A–J prompt records
→ recalculate 18 prompt hashes
→ commit final prompt registry + B00/B01/B02/B03 prompt files
→ NEW PROMPT_CONTENT_COMMIT_SHA
→ rebuild 4 schema-valid manifests referencing that SHA
→ calculate 4 BATCH_MANIFEST.sha256 sidecars
→ update dependent visual manifest/brief/hash references only as necessary
→ final manifest commit
→ Director recheck
```

No academic rewrite is authorized or requested by this review.

## 5. B00 gate

After targeted corrections pass Director recheck:

```text
B00 may be considered for production authorization.
B01–B03 remain closed.
B01–B03 may not open until B00 Director consistency review PASS AND B00 Independent Image QA = QA_APPROVED.
```

## 6. Current state

```text
W02 ACADEMIC PROGRAM: ACCEPTED BY DIRECTOR REVIEW 01
W02 VISUAL/PROMPT CONTENT: ACCEPTED BY DIRECTOR REVIEW 01
W02 PRODUCTION HANDOFF: NOT ACCEPTED YET
IMAGE PRODUCTION: NOT AUTHORIZED
R2: NOT AUTHORIZED
MERGE: NOT AUTHORIZED
WEBSITE: HOLD
```
