---
title: "HKA W02 — CINEMATIC 4K Prompt Registry"
version: "2.1-snapshot"
status: "PROMPT_CONTENT_FROZEN_FOR_HANDOFF_BINDING"
window_id: "W02"
tree_id: "HKA-TREE-00-HROOT"
package: "P18"
asset_count: 18
academic_content_commit: "e900d3b623c27f6d4a0fe2750fa499295788776e"
reviewed_prompt_package_commit: "73c55dc9825dc1113f444c2a5c7468ee9ef09b43"
brand_asset_commit: "2d3aa9d8418acccd39a3d263e917d4157e029e17"
date: "2026-09-04"
---

# HKA W02 — CINEMATIC 4K PROMPT CONTENT SNAPSHOT

Director Independent Review 01 (`164775dd7d3aef0e0179440a88eb323eb8c23fa0`) accepted the academic program and all 18 visual/prompt concepts, but returned production-handoff integrity. This snapshot changes no generation language, learning objective, scene, truth lock, P18 package, Asset ID, VCU ID or 2/6/6/4 batch map. **IMAGE PRODUCTION IS NOT AUTHORIZED.**

## Canonical full A–J resolver — HKA-W02-AJ-TEXT-V1

The four `PRODUCTION/BATCHES/HKA-W02-B00..B03/BATCH_PROMPTS.md` files in this same Git snapshot are the frozen asset-specific prompt content. Their inherited static A–J values are exactly `G-W02-PROMPT-2.0/A..J` from the reviewed prompt registry at commit `73c55dc9825dc1113f444c2a5c7468ee9ef09b43`; the W01 field order and semantics are exactly `PROMPT_ASSET_RECORD_TEMPLATE.md` at accepted W01 base `5805f60f7f60d15675f669bc21565dda73f3443c`.

For each Asset ID, deterministically resolve one complete A–J record as follows:

1. Take the asset-specific A–J block from its frozen batch prompt file.
2. Expand each `INHERITED STATIC FIELDS: G-W02-PROMPT-2.0/<section>` marker with the exact reviewed static fields from `73c55dc...`.
3. Map the abbreviated batch labels back to their W01 template fields without changing values (for example `VCU ID` → `VISUAL COVERAGE UNIT ID`; `AUDIENCE / DEPTH` → `PRIMARY AUDIENCE` + `ACADEMIC DEPTH`; `CLAIMS SHOWN` → `ACADEMIC CLAIMS SHOWN`; `OUTPUT` → `OUTPUT SIZE` + `COLOR SPACE` + `MASTER FORMAT`).
4. Resolve integrity metadata only: `PROMPT RECORD VERSION = 2.1`; `PROMPT CONTENT COMMIT SHA = the 40-hex Git SHA of this snapshot commit itself`. The historical `65c852...` value inside the frozen reviewed blocks is superseded for canonical hashing and production binding; prompt content is unchanged.
5. Serialize the full record in W01 A→J template order with the accepted section-divider text.
6. Canonicalize as UTF-8, LF, no BOM, stripping trailing whitespace on every line.
7. Remove exactly the entire line beginning `PROMPT SHA-256:` and no other line.
8. SHA-256 all remaining resolved A–J bytes; lowercase 64-hex output.

This profile binds both inherited static locks and asset-specific content. Changing any inherited A–J production lock therefore changes the asset hash.

## Frozen package map

```text
P18: 18 assets / 18 unique VCUs
HKA-W02-B00: 0001–0002 = 2
HKA-W02-B01: 0003–0008 = 6
HKA-W02-B02: 0009–0014 = 6
HKA-W02-B03: 0015–0018 = 4
```

## Production boundary

```text
ACADEMIC: ACCEPTED BY DIRECTOR REVIEW 01
VISUAL/PROMPT CONTENT: ACCEPTED BY DIRECTOR REVIEW 01
PRODUCTION HANDOFF: PROMPT SNAPSHOT FROZEN; MANIFEST/HASH BINDING PENDING
B00 IMAGE PRODUCTION: NOT AUTHORIZED
B01–B03: CLOSED
R2: NOT AUTHORIZED
MERGE: NOT AUTHORIZED
WEBSITE: HOLD
```
