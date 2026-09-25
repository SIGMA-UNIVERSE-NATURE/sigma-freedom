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


## Current MediaWiki R2 blocker — 2026-09-25

Lane B MediaWiki acquisition R2 returned:

~~~text
STATUS=HOLD
SYSTEM_INTEGRITY_STATUS=HOLD
BLOCKER=NATIVE_RUNTIME_FAILURE:SIGMA_VKM_927_AITO_MEDIAWIKI_SEARCH_SELECTION_NATIVE_R2:SIGMA C VM: undefined function H_
~~~

Static audit classification:

- integration/native harness assembly defect;
- not a Sigma capability miss;
- not a MediaWiki transport failure;
- not a baseline/measurement failure.

R2 package SHA256:

~~~text
4307b1bfdeecafa38a7a1644d8d5ab363860dc34fef32ddf7c63b34b2aa3c0ce
~~~

Cause:

The R2 controller is compiled standalone. Its acquisition-plan functions do not call H(...) and therefore pass. The first search-result relevance execution calls H("str_contains",...), which compiles to H_ but the standalone harness does not carry the approved canonical runtime substrate used by accepted 927 evaluator assemblies.

Repair direction:

- preserve exact accepted MediaWiki transport logic;
- do not redesign relevance;
- assemble relevance harness from the exact BASELINE_06B2 canonical substrate with its MAIN removed;
- append the acquisition-controller definitions with duplicate header/MAIN removed;
- append only the bounded temporary relevance MAIN;
- pin canonical SHA before use;
- require no canonical mutation;
- apply the same substrate assembly to both search-result relevance and full-content relevance;
- then continue R2 directly.

Do not reopen 06B2, goal selection, curriculum, or provider design.


## 928 FINAL RELEASE STATE — 2026-09-25

Hermeticity has now been closed.

~~~text
BUNDLE_HERMETICITY=PASS
ORIGIN_REFERENCES_NONOPERATIVE=YES
NEUTRAL_PATH_BUNDLE_VERIFY=PASS
NEUTRAL_PATH_RECONSTRUCTION=PASS
NEUTRAL_PATH_COMPILE=PASS
NEUTRAL_PATH_PROTECTED_REGRESSION=PASS
NEUTRAL_PATH_CAPABILITY_CONTRACT=PASS

COMPLETE_IMAGE_SHA256=
0b1168d1e57d3e9163973fcbf8d03b7aa439cd84c9e397bd46bb591c324f1989

BYTECODE_SHA256=
0406aae09288872a815ddfe9710828bd17ce30cc80757fdb5e64143eb982fb62

928_STATUS=READY_PENDING_927_WRITER_RELEASE
PROMOTION_PERFORMED=NO
PROMOTION=HOLD
~~~

The remaining HOLD is writer coordination only.

Read full checkpoint:

checkpoints/SIGMA_VKM_928_FINAL_BOUNDED_RELEASE_CHECKPOINT_2026-09-25.md

Do not perform more 928 proof/enhancement work unless a new integrity failure invalidates the checkpoint.

927 remains the active critical path.


## 927 MediaWiki R2 FIX1 — transport PASS, teaching-mechanism gap identified

Observed accepted runtime result:

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS

GOAL_DIMENSION=SOURCE_RECONSTRUCTION
CURRICULUM_STAGE=FOUNDATION

SEARCH_RESULT_CANDIDATES=16
SIGMA_SELECTED_PAGES=1
FETCHED_URLS=1
ELIGIBLE_SOURCES=0

LEARNING_STATE=ACQUISITION_REQUIRED
ADMISSION_DECISION=ACQUIRE_MORE

OFFICIAL_CANONICAL_SUBSTRATE_BOUND=PASS
NATIVE_H_DISPATCH_CONTROL=PASS
NATIVE_STR_CONTAINS_CONTROL=PASS
SEARCH_RELEVANCE_RUNTIME=SIGMA_VKM
CONTENT_RELEVANCE_RUNTIME=SIGMA_VKM
~~~

R2 FIX1 package SHA256:

~~~text
eef4256f2795a7b4e0563933bace367159357222794695fe6124e6031ccb918b
~~~

Admin audit conclusion:

MediaWiki transport and native relevance execution are working.

Do not keep widening search blindly.

The current relevance policy detects documents that *talk about* extractive/extraction/reconstruction/retrieval concepts. That is meta-topic relevance, not necessarily teaching suitability for SOURCE_RECONSTRUCTION.

More importantly, accepted 06B1 model coupling is episodic semantic-extension memory:

- incremental_update stores evidence text in knowledge;
- sigma_model_semantic_signature_v1 searches learned evidence whose semantic signature extends the current input;
- source reconstruction proof reconstructs accepted learned evidence from a semantically anchored related input.

Therefore unrelated Internet documents do not by themselves prove or create a general source-reconstruction rule. Current acquisition can otherwise loop ACQUIRE_MORE or store unrelated episodic evidence without measurable transfer.

Next task for Lane B is not broader search. It is a bounded SOURCE_RECONSTRUCTION teaching-mechanism design/proof using only non-holdout evidence.

Required direction:

1. keep MediaWiki transport as proven;
2. preserve frozen/gold isolation;
3. distinguish SOURCE_MATERIAL_SUITABILITY from META_TOPIC_RELEVANCE;
4. build a Sigma/VKM-side FOUNDATION curriculum constructor that can turn non-holdout public source material into semantically anchored source-reconstruction training pairs/examples compatible with the existing model-learning ABI;
5. prove on fresh non-holdout canaries that the learned rule/behavior transfers beyond the exact training item;
6. only then resume Internet acquisition → learning epoch → candidate evaluation;
7. if the existing canonical learning primitive cannot express transferable source-reconstruction learning, return a truthful LEARNING_MECHANISM_GAP / ACQUIRE_MORE rather than fabricating gain.

Do not use frozen text to design the examples.
Do not train on acceptance-test fixtures.
Do not perform admission until CANDIDATE_EPOCH_V1 exists.


## Runtime execution authority policy — 2026-09-25

Admin decision after repeated coder self-run failures:

~~~text
CODER_EXECUTION_POLICY=BUILD_ONLY
CODER_STATIC_AUDIT_ALLOWED=YES
CODER_PACKAGE_HASH_VERIFY_ALLOWED=YES
CODER_SIGMA_COMPILE_RUN=NO
CODER_SIGMA_VM_RUN=NO
CODER_END_TO_END_RUNTIME_RUN=NO
USER_RUNTIME_EXECUTOR=YES
ADMIN_RUNTIME_RESULT_AUDITOR=YES
~~~

Coders may:

- inspect only the component they are authorized to modify;
- patch source/bundle;
- run static syntax/text/package-manifest checks that do not invoke Sigma compiler or VM;
- compute SHA256;
- create immutable package and notes;
- return exact run command for the user.

Coders must not:

- invoke sigmac-vkm;
- invoke sigma-vkm;
- run end-to-end Sigma tests;
- mutate canonical/Owner/native binding;
- claim behavioral PASS from static checks.

The user runs the provided bundle command in Termux and returns the real output to admin for classification.

This separation prevents a coder from burning context/time on repeated runtime attempts and keeps runtime evidence independent from implementation.

Current transfer-gate R1 package:

~~~text
PACKAGE_SHA256=
e3f1900173cc6c487d8cacc628511569587d334f401605de1ab3effe8f96d80e
~~~

Static audit localized the current failure to generated Sigma output formatting:

~~~text
"UNSEEN_BEFORE_RECONSTRUCTION_PASS_COUNT=" + before_count
"UNSEEN_AFTER_RECONSTRUCTION_PASS_COUNT=" + after_count
"UNSEEN_TRANSFER_DELTA=" + delta
"REPLAY_UNSEEN_PASS_COUNT=" + replay_count
~~~

The operands on the right are numeric. This is consistent with the observed runtime error:

~~~text
SIGMA C VM: incompatible binary operands_
~~~

Repair the bundle mechanically without running Sigma. Prefer the already-proven 06B2 native numeric-output convention or an explicit bounded integer-to-text printer. Then return a new package + SHA + user run command only.


## 927 SOURCE_RECONSTRUCTION transfer gate — EPISODIC_ONLY

Runtime result accepted:

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS
SOURCE_RECONSTRUCTION_TRANSFER_GATE=PASS

TRAIN_CASE_COUNT=3
UNSEEN_CASE_COUNT=3

TRAIN_ITEM_RECALL=PASS
EPISODIC_RECALL=PASS

UNSEEN_BEFORE_RECONSTRUCTION_PASS_COUNT=0
UNSEEN_AFTER_RECONSTRUCTION_PASS_COUNT=0
UNSEEN_TRANSFER_DELTA=0
UNSEEN_TRANSFER=FAIL

UNRELATED_EVIDENCE_CONTROL=PASS
UNSEEN_TRANSFER_AFTER_RESTART=NOT_APPLICABLE_NO_TRANSFER

LEARNING_MECHANISM_STATUS=EPISODIC_ONLY
LEARNING_STATE=MECHANISM_UPGRADE_REQUIRED
ADMISSION_DECISION=ACQUIRE_MORE
NEXT_ACTION=BUILD_TRANSFERABLE_SOURCE_RECONSTRUCTION_MECHANISM
~~~

Additional integrity facts:

~~~text
TRAIN_UPDATE_RUNTIME=SIGMA_VKM
REPLAY_PERSISTENCE_MODE=APPEND_ONLY_EVIDENCE_REPLAY
REPLAY_MODEL_SHA256=bd92f7127775c26736554a584af6906236dca5bebcc88acee974de8907613e9c
FRESH_PROCESS_EVALUATION_MATCH=PASS
DETERMINISTIC_EVALUATION=PASS
TRAIN_UNSEEN_EXACT_SOURCE_OVERLAP=NO

GATE_NATIVE_SOURCE_SHA256=
1b2e5f97af9df06155d3cb3da4cd97a3f1f716575c3c576f673492d3902d68f1

GATE_NATIVE_BYTECODE_SHA256=
e5f411e18cd6a43027423776706db81ae7a2b6cb305f09e2a00f2fa47b5572fd

TESTER_SHA256=
8ea644a73231959c2447ea3084176c3e0c02109520f4ecf498cf392a0aef6924
~~~

Admin conclusion:

**Current accepted 927 learning primitive is episodic-only for SOURCE_RECONSTRUCTION.**

This is not a system failure and not a reason to reopen 06B2.

Do not resume Internet acquisition yet.

More data cannot by itself repair a mechanism that recalls TRAIN evidence but shows zero transfer to unseen source-reconstruction cases.

Current critical path:

~~~text
EPISODIC_ONLY proven
→ define transferable SOURCE_RECONSTRUCTION learner ABI
→ implement isolated candidate learning mechanism
→ independent unseen/negative/restart proof
→ integrate with AIto epoch
→ CANDIDATE_EPOCH_V1
→ Lane A admission
~~~

Parallel lane assignment:

- Lane B / young coder: implement candidate transferable learner against a fixed ABI, build-only, no Sigma VM run.
- Lane C / 928 coder: independently build the behavioral proof harness against that fixed ABI; do not modify 928 candidate or Lane B source.
- Lane A / senior: remain admission/convergence standby.

Do not use frozen/gold to design the learner.
Do not hard-code the synthetic transfer cases.
Do not mutate canonical, Owner, or native binding during candidate development.


## 927 parallel mechanism-upgrade phase — fixed ABI

After the accepted SOURCE_RECONSTRUCTION transfer gate:

~~~text
TRAIN_ITEM_RECALL=PASS
UNSEEN_BEFORE_RECONSTRUCTION_PASS_COUNT=0
UNSEEN_AFTER_RECONSTRUCTION_PASS_COUNT=0
UNSEEN_TRANSFER_DELTA=0
UNSEEN_TRANSFER=FAIL
LEARNING_MECHANISM_STATUS=EPISODIC_ONLY
LEARNING_STATE=MECHANISM_UPGRADE_REQUIRED
~~~

Admin decision:

- stop bounded Internet acquisition until a transferable mechanism exists;
- preserve MediaWiki transport as proven infrastructure;
- build the mechanism as an isolated additive candidate, not by mutating canonical;
- use separate implementation and proof lanes.

Fixed candidate ABI:

~~~text
SCHEMA=SIGMA_VKM_927_SOURCE_RECONSTRUCTION_LEARNER_V1

TRAIN:
sigma_sr_learner_new(parent_state)
sigma_sr_learner_train(learner_state,training_example)

INFERENCE:
sigma_sr_reconstruct_v1(learner_state,input_text)

TRAINING_EXAMPLE required semantic fields:
EXAMPLE_ID
INPUT_TEXT
TARGET_TEXT
PROVENANCE_STATUS
CURRICULUM_STAGE
LEARNING_GOAL

PUBLIC_COMPATIBILITY_TARGET:
sigma_model_source_reconstruction_v1(effective_state,input_text)
~~~

Contract:

- training target may come only from non-holdout curriculum;
- exact training-item recall is insufficient;
- unseen transfer is mandatory;
- unseen cases must differ in entities/objects/surface strings;
- no frozen/gold used for design;
- ambiguous reconstruction must fail closed;
- negative unrelated evidence must not create success;
- restart retention required if transfer exists;
- host may transport/serialize but may not perform learning or semantic reconstruction.

Parallel lanes:

~~~text
LANE_B_YOUNG:
implement isolated candidate learner component against the fixed ABI
BUILD_ONLY
NO_SIGMA_VM_RUN

LANE_C_928_CODER:
build independent sealed behavioral proof harness against the fixed ABI
DO_NOT_READ_LANE_B_SOURCE
BUILD_ONLY
NO_SIGMA_VM_RUN
928_MUTATED=NO

LANE_A_SENIOR:
admission/convergence standby
~~~

Integration occurs only after both packages are statically audited by admin and then executed by the user.

No canonical/Owner/native-binding mutation during mechanism development.


## 927 candidate learner V1 static rejection — identity-copy trap

Lane B candidate package:

~~~text
PACKAGE_SHA256=
a033163b66769d8533de4e2bf6a4c3dd0665067fd619a28c0a81d7b8295885b6

COMPONENT_SHA256=
8ac1b8d683b28490bf218185c5d21a70528e0e40e8594be55bd51e5c2755f1cb
~~~

Static audit verdict:

**REJECT BEFORE RUNTIME.**

The component does not memorize exact training pairs, but it hard-codes one preselected rule:

~~~text
after >=3 cases where TARGET_TEXT == INPUT_TEXT
→ LEARNED_RULE=IDENTITY_COPY
→ reconstruction returns input_text for every unseen input
~~~

This is vulnerable to a transfer-harness false PASS if the proof dataset accidentally uses identity reconstruction cases.

Additional defects:

1. parent_state is only checked for non-null and then PARENT_BOUND=YES is asserted; actual parent identity/state is not validated.
2. EXAMPLE_ID is checked for presence but not retained/deduplicated; replaying one example three times can satisfy the support threshold.
3. contradiction handling proves only incompatibility with IDENTITY_COPY, not general source-reconstruction learning.
4. the mechanism does not infer a reconstruction transform from training examples; the transform class is fixed before training.

Admin repair direction:

- preserve the three-function ABI;
- replace fixed IDENTITY_COPY with bounded structural-rule induction from training pairs;
- identity may be one hypothesis but must not be sufficient proof of general transfer;
- require unique-example support/dedup;
- bind actual parent state identity/validity;
- Lane C proof harness must include at least one non-identity reconstruction family and mutation sensitivity so identity-copy cannot self-certify.

Do not run the rejected V1 package.
