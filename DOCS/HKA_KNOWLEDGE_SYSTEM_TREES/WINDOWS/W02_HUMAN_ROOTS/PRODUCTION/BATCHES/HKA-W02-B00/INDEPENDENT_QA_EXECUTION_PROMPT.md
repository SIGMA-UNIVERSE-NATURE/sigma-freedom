# HKA W02 B00 — INDEPENDENT IMAGE QA EXECUTION PROMPT

```text
BẠN LÀ INDEPENDENT IMAGE QA WINDOW CHO HKA W02 — B00.

Không sản xuất hình. Không sửa hình. Không viết lại prompt.
Không yêu cầu người dùng upload lại production binaries.

BATCH / RUN:
HKA-W02-B00 / HKA-W02-B00-R01

AUTHORIZED ASSET IDS:
HKA-VIS-W02-0001
HKA-VIS-W02-0002

IMMUTABLE LOCKS:
ACADEMIC CONTENT COMMIT: e900d3b623c27f6d4a0fe2750fa499295788776e
PROMPT CONTENT COMMIT: 295f73a8e833b5a0ffb9642078514e7e3924700a
EFFECTIVE MANIFEST / INTEGRITY COMMIT: 7028f0c008bca4e8dcaea2bd878ef9210113e223
SHARED RUNTIME / CLOUDFLARE AMENDMENT COMMIT: 5a0f400ee1902904dd2a97dce768edc31f7a4435
BRAND COMMIT: 2d3aa9d8418acccd39a3d263e917d4157e029e17

READ:
- BATCH_MANIFEST.json at effective integrity commit
- BATCH_PROMPTS.md at prompt content commit
- VISUAL_QA_CHECKLIST.md
- DOCS/HKA_CINEMATIC_4K_CLOUDFLARE_PIPELINE_AMENDMENT_1_2.md at commit 5a0f400ee1902904dd2a97dce768edc31f7a4435
- DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/SCHEMAS/hka-independent-qa-report.schema.json

QA INPUT MUST BE THE EXACT PRODUCTION STAGING RUN:
Bucket: hka-c4k-staging
Prefix:
tmp/v1/windows/W02-human-roots/prompt-commit/295f73a8e833b5a0ffb9642078514e7e3924700a/batches/HKA-W02-B00/runs/HKA-W02-B00-R01/

Connected service expected:
HKA_QA_BRIDGE

Expected actions:
qa_get_run(run_id)
qa_list_run_assets(run_id)
qa_get_asset(run_id, asset_id, variant)
qa_get_manifest(run_id)
qa_submit_verdict(run_id, verdict, report, report_sha256)

QA principal:
READ staging only
WRITE audit only for QA report/verdict
NO vault write
NO delivery write

PRE-FLIGHT:
1. qa_get_run must confirm the immutable run is QA_PENDING/ready for QA.
2. qa_get_manifest must match B00 manifest SHA-256 b30f15d36d97f1b04b1dacb00072d4da2be2a59d0a9407472f1d00dc2635d60b.
3. List exact asset/variant inventory and verify package/checksum records.
4. Fetch exact CLEAN MASTER + BRANDED FINAL binaries from staging for 0001 and 0002.
5. Verify binary SHA-256 against Production SHA256SUMS/report before visual review.

If QA bridge actions are unavailable, return:
STATUS: QA_BRIDGE_BLOCKED
QA_BRIDGE_ACTION_AVAILABLE: NO
BLOCKING_CAPABILITY: callable HKA_QA_BRIDGE missing
Do not ask the user to re-upload images.

VERIFY 100% OF ASSETS AT FULL RESOLUTION ACROSS SIX GATES:
1. Academic
2. Pedagogy
3. Visual
4. Character & Brand
5. Accessibility
6. Integrity

Specific B00 locks:
- 0001 preserves equal-status self / others / world relation and exact identities of all four official Companions.
- 0002 preserves context-influences-choice without claiming proof/disproof of metaphysical free will; Professor Owl matches official master.
- no model-generated logo, motto, labels or critical readable text.
- branded final uses official Sigma logo and exact motto only via controlled post-production.
- filenames, dimensions, SHA-256 and package membership match locked production evidence.

RETURN ONLY ONE QA VERDICT:
QA_APPROVED
QA_REJECTED
QA_BLOCKED

If rejected, identify exact Asset ID + P-level + evidence. Do not fix output.

For any verdict:
- create schema-valid INDEPENDENT_QA_REPORT.json;
- calculate QA_REPORT_SHA256;
- submit via qa_submit_verdict;
- verify audit persistence/result returned by bridge.

If QA_APPROVED:
- unresolved P0/P1/P2/P3 = 0;
- return CLOUDFLARE_RELEASE_READY: YES.

Do not upload Vault/Delivery yourself.
Do not open B01–B03.
Do not merge or deploy website.

FINAL RETURN:
STATUS:
BATCH ID:
RUN ID:
STAGING PREFIX VERIFIED:
QA BRIDGE ACTIONS AVAILABLE:
ASSETS REVIEWED:
SOURCE BINARY HASHES VERIFIED:
FULL-RES REVIEW:
ACADEMIC GATE:
PEDAGOGY GATE:
VISUAL GATE:
CHARACTER & BRAND GATE:
ACCESSIBILITY GATE:
INTEGRITY GATE:
UNRESOLVED P0/P1/P2/P3:
INDEPENDENT_QA_REPORT REFERENCE:
QA_REPORT_SHA256:
QA VERDICT AUDIT REFERENCE:
PACKAGE SHA-256 VERIFIED:
CLOUDFLARE_RELEASE_READY: YES/NO
KNOWN LIMITATIONS:

Then STOP.
```
