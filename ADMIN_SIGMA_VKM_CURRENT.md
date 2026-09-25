# ADMIN SIGMA VKM — CURRENT HANDOFF

**Current checkpoint date:** 2026-09-25  
**Admin branch:** admin-sigma-vkm-2026-09-25

Read first:

checkpoints/ADMIN_SIGMA_VKM_CHECKPOINT_2026-09-25.md

Official Project 927 parent:

SIGMA_VKM_927_BASELINE_06B2

~~~text
BASELINE_SHA256=
c6ab1c428d0385805cf5762b8082d24bcfd9cf95adfb4e79a5a9e5d709cb3e5b

SNAPSHOT_MANIFEST_SHA256=
3e153e5fb931b4cea33d4afc26577a08647238828788573e98f2cec319824578
~~~

## Current verified Lane B state — 2026-09-25

The complete official-baseline/gap/goal/curriculum path is accepted.

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS

BASELINE_06B2_CONSUMED=YES

LEARNING_GOAL_STATUS=PASS
GOAL_DIMENSION=SOURCE_RECONSTRUCTION

CURRICULUM_STATUS=PASS
CURRICULUM_STAGE=FOUNDATION

LOCAL_COVERAGE_STATUS=INSUFFICIENT
ACQUISITION_REQUIRED=YES
NEXT_SOURCE_POLICY=BOUNDED_INTERNET
~~~

Bounded Internet acquisition R1 also returned a truthful normal result:

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS
LEARNING_STATE=ACQUISITION_REQUIRED
ADMISSION_DECISION=ACQUIRE_MORE

ACQUISITION_STATUS=PASS
ACQUISITION_ATTEMPT_STATUS=COMPLETED_NO_ELIGIBLE_SOURCE

SEARCH_QUERIES=3
FETCHED_URLS=0
ELIGIBLE_SOURCES=0

TRAINING_EPOCH_STATUS=NOT_RUN_ACQUISITION_REQUIRED
CANDIDATE_EPOCH_STATUS=NOT_CREATED

SIGMA_AITO_ACQUISITION_PLAN_SHA256=
65bda766b245d12910f8fa05f91e880a5eab2d36a5b570252a0f16fb991e3f97

SIGMA_AITO_QUARANTINE_SHA256=
9a8b9772b32f09c14fa99a63d3997dcfc858966f446ff01316d227c17ebc072a
~~~

R1 acquisition package SHA256:

~~~text
5ad629235a5980dd8b0c6c0b45664c09cbe6240b9c0966778a5a51c17e705fa7
~~~

## Admin diagnosis

R1 acquisition architecture is valid:

- Sigma/VKM generates acquisition queries;
- Sigma/VKM performs target-relevance gating;
- host performs only HTTPS retrieval, byte transport, validation, normalization, hashing, exact dedup, quarantine and process launch;
- no frozen/gold is used;
- no admission is performed.

However R1 search discovery has only one provider path:

~~~text
https://html.duckduckgo.com/html/?q=<Sigma-generated-query>
~~~

Search transport errors/non-200/no-result parsing are treated as zero discovered URLs and therefore lead to a truthful ACQUIRE_MORE.

Therefore:

**Do not rerun R1 unchanged.**

The next task is bounded acquisition transport R2, not admission.

## Immediate work

### YOUNG / LANE B

Build acquisition transport R2 while preserving the accepted Sigma/VKM plan and relevance logic.

Requirements:

1. Consume the exact existing ACQUISITION_REQUEST_V1 and acquisition-plan contract.
2. Do not change GOAL_DIMENSION or curriculum.
3. Preserve all existing network bounds.
4. Add explicit search-transport result classification.
5. Add a provider abstraction/fallback rather than depending on one scraped HTML endpoint.
6. Prefer a stable public HTTPS search API that does not require credentials; a bounded MediaWiki Action API adapter is acceptable for R2.
7. Provider/search discovery is transport only: Sigma-generated query remains the semantic query authority.
8. Dedup URLs/results mechanically.
9. Fetch at most the already-approved URL/byte limits.
10. Keep Sigma/VKM target relevance.
11. If eligible evidence is found, feed the pinned catalog to the already-accepted FIX4 epoch path.
12. Produce CANDIDATE_EPOCH_V1 or return truthful ACQUIRE_MORE.
13. Do not perform admission.

Distinguish at least:

~~~text
SEARCH_TRANSPORT_STATUS=PASS_RESULTS
SEARCH_TRANSPORT_STATUS=PASS_NO_RESULTS
SEARCH_TRANSPORT_STATUS=PROVIDER_UNAVAILABLE
~~~

A provider outage must not be mislabeled as “Sigma found no relevant learning source”.

### SENIOR / LANE A

Remain ready.

Do not run admission until a real:

SIGMA_VKM_927_CANDIDATE_EPOCH_V1

exists.

### PROJECT 928

Still:

~~~text
928_STATUS=READY_PENDING_WRITER_RELEASE
PROMOTION=HOLD
~~~

Do not promote while 927 owns the writer.

## Do not reopen

- BASELINE_06B2 assembly
- 06B2 mapping discovery
- accepted measurement
- gap-ledger escaped-LF diagnosis
- Sigma/VKM goal selection
- FOUNDATION curriculum selection

Do not rerun acquisition R1 unchanged.
Do not use frozen/gold as training.
Do not create a second Sigma.


## Historical G3B Internet precedent — audited 2026-09-25

A historical package was reviewed statically:

~~~text
SIGMA_G3B_200_STORY_DIRECT_INTERNET_NATIVE_CHALLENGE_R1_FIX3_LIVE_SCREEN_R1.tgz
SHA256=77706e5ad8d81c01977d424f79ece109dd96a243bc0e569d560cdb7d074c5dd1
~~~

This is **historical architecture evidence only**. It is not automatically current 927 continuity, accepted state, or a dependency to import.

Useful proven pattern:

~~~text
native capability planner
→ exact public MediaWiki endpoint/discovery target
→ host mechanical HTTPS + JSON decode
→ native candidate selector
→ host exact selected-page fetch + mechanical markup-to-text decode
→ native full-text consumer/summarizer
→ provenance receipts
~~~

Historical provider catalog included:

~~~text
Wikisource MediaWiki category
Wikipedia MediaWiki search
local documents
~~~

For the implemented Wikisource path the host used the MediaWiki Action API mechanically and did not rank/select pages semantically. Sigma selected capability and candidate; host fetched the exact native-selected target.

Important limitation:

The G3B summarizer was a native **extractive beginning/middle/end digest**. Its own contract explicitly did not claim persistent learning, general semantic understanding, or general autonomous world learning.

Admin reuse rule for current 927:

- reuse the **control/transport pattern**, not the old learned state;
- do not import old source blindly into current Sigma;
- do not treat G3B as proof of current SOURCE_RECONSTRUCTION mastery;
- bounded acquisition R2 should prefer the stable MediaWiki API pattern over depending only on scraped search HTML;
- current 927 must still apply provenance, quarantine, dedup, Sigma/VKM target relevance, native learning epoch, fresh evaluation, retention, and admission.

This precedent strengthens the decision that acquisition transport R2 should use a public MediaWiki adapter while keeping current 927 goal/curriculum/admission contracts unchanged.


## Legacy Sigma tools corpus policy — 2026-09-25

A large historical tool corpus exists under:

`$HOME/SIGMA/sigma_genesis1/tools/`

including historical generations such as:

- SIGMA_AUTO_INTERNET_VISIBLE_PILOT_*
- SIGMA_AUTO_INTERNET_SELF_DIRECTED_R3_*
- SIGMA_INTERNET_COMPREHENSION_LEARNER_R7_*
- SIGMA_ONE_SIGMA_INTERNET_TEACHER_R8*
- SIGMA_ONE_SIGMA_TOPIC_RESEARCH_TEACHER_R9*
- SIGMA_ONE_SIGMA_NATIONAL_LIBRARY_MARATHON_R10*
- SIGMA_ONE_SIGMA_INTERNET_SHADOW_READER_R11*

Admin decision:

**Do not promote this directory or its contents into Owner identity/state wholesale.**

Owner/identity lineage is not a knowledge store.

These historical artifacts are valuable as:

1. read-only architecture precedent;
2. transport/provider adapter precedent;
3. candidate implementation evidence;
4. historical capability archaeology;
5. possible non-holdout teaching evidence only after explicit eligibility/provenance review.

Required handling:

~~~text
LEGACY_CORPUS_ROLE=READ_ONLY_HISTORICAL_EVIDENCE
OWNER_IMPORT=FORBIDDEN
CANONICAL_IMPORT=FORBIDDEN
BLIND_MEMORY_IMPORT=FORBIDDEN
DIRECT_ADMISSION=FORBIDDEN
~~~

Create a mechanical legacy capability catalog first:

~~~text
SIGMA_VKM_927_LEGACY_CAPABILITY_CATALOG_V1
~~~

For each candidate artifact record only mechanical metadata:

~~~text
RELATIVE_PATH
SHA256
BYTES
ARTIFACT_CLASS
HISTORICAL_GENERATION
EXECUTABLE_OR_SOURCE
PROVENANCE_STATUS
OWNER_LINEAGE_STATUS
TRAINING_ELIGIBILITY=UNKNOWN
IMPORT_STATUS=QUARANTINED
~~~

Do not infer semantic capability in shell/Python.

Then use Sigma/VKM or an explicit audited metadata contract to classify whether a historical artifact is:

- architecture precedent only;
- reusable mechanical transport adapter;
- admissible non-holdout teaching evidence;
- incompatible/unsafe historical host cognition;
- lineage-sensitive and therefore non-importable.

Any learned knowledge derived from legacy artifacts must enter current Sigma only through the normal 927 path:

~~~text
quarantine
→ provenance
→ eligibility
→ Sigma/VKM target relevance
→ bounded learning epoch
→ fresh evaluation
→ protected regression
→ retention
→ 927 admission
→ accepted same-Sigma state
~~~

No Owner mutation is justified merely because old Sigma tools exist.
