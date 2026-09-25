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


## 927 Lane C sealed proof V1 static rejection — ABI/control mismatch

Lane C proof package:

~~~text
PACKAGE_SHA256=
ba11e4232c29984319666601284584045e8702bfdb5b6a040c3ec99819c6d488

HARNESS_SEAL_SHA256=
1d8293bb4dce3bf5d03c3c5d1875bc25c1bd74837db9fe42e7a4185f9b85448f
~~~

Positive finding:

All four unseen cases require non-identity reconstruction:
FRAME|... → fresh natural-language target.
Therefore a pure IDENTITY_COPY learner cannot pass transfer.

Static rejection reasons:

1. Proof ABI training-example schema uses only:
   kind, example_id, input_text, target_text

   but the fixed learner contract requires:
   EXAMPLE_ID, INPUT_TEXT, TARGET_TEXT, PROVENANCE_STATUS, CURRICULUM_STAGE, LEARNING_GOAL.

2. Harness calls:
   sigma_sr_learner_new(NULL)

   while current learner repair requires real same-Sigma parent validation/binding. FRESH_PROOF_PARENT=NULL is incompatible with that contract.

3. Required control:
   DUPLICATE_TRAINING_NO_SUPPORT_INFLATION
   is absent.

4. Required control:
   INVALID_PARENT_FAIL_CLOSED
   is absent.

5. TRAIN_ANSWER_LEAK checks only negative outputs; hardened proof should also ensure unseen outputs do not equal any TRAIN target unless that byte string is the independently expected unseen target.

6. STATIC_AUDIT claims ABI bound but does not cover the fixed learner record contract above.

Decision:

~~~text
LANE_C_PROOF_V1=REJECT_BEFORE_RUNTIME
RUN_FORBIDDEN=YES
~~~

Repair Lane C only. Do not reveal Lane B implementation source. Preserve the existing sealed non-identity dataset where possible and add the missing ABI fields and controls.


## 927 Lane B learner V1 FIX1 static audit — repair required

Lane B learner FIX1 package:

~~~text
PACKAGE_SHA256=
e8e982a11a6e12d11bdad987e6cb4074c68ecb4903728eead660300e937e41a4

COMPONENT_SHA256=
35110ce53fc0c7b2f9dff4d5cc80bc7cb09afcefed86d6cdc0637427e0a8b6a1
~~~

Positive fixes confirmed statically:

- identity-only architecture removed;
- bounded IDENTITY/PREFIX/SUFFIX/BETWEEN hypothesis classes present;
- EXAMPLE_ID duplicate no-op control present;
- minimum unique support = 3;
- valid parent state checked through current state-coupled model interface;
- no exact input-target lookup table;
- no frozen/gold/test-case strings found;
- no canonical/Owner/native-binding mutation code.

However the package is rejected before runtime for two implementation defects:

1. BETWEEN reconstruction uses:
   str_slice(input_text,left_len,right_pos)

   In the accepted 927 runtime convention, str_slice third argument is LENGTH, not end-index. Correct BETWEEN width is:
   right_pos - left_len.

2. The learner introduces:
   H("str_rfind",...)

   This primitive is not part of the already-proven current 927 string primitive set available to this candidate audit. Replace it with a uniqueness check built from proven str_find + str_slice + str_len rather than adding an unverified runtime dependency.

Do not run this FIX1 package.

Repair must remain source-only/build-only and must not alter the fixed public three-function learner ABI or sealed Lane C dataset.


## 927 Lane C proof FIX1 static rejection — semantic target mismatch

Lane C proof FIX1 package:

~~~text
PACKAGE_SHA256=
4cf4ac0ebfa7e332d20fdaa51e1852dd5b73505d748e774370ec0d9e83e54718

HARNESS_SEAL_SHA256=
b0c813d64c156def457e39a7613761bce43cd97a1f142b853fd81ca0f6a451ee
~~~

Static audit confirms the requested control repairs are present:
training-record ABI fields, valid parent path, invalid-parent control, duplicate-support control, non-identity unseen control, unseen/train-answer leak control, mutation sensitivity and restart phase.

However the proof dataset is semantically mismatched to 927 SOURCE_RECONSTRUCTION.

Current Lane C cases are generative rewrites such as:

FRAME|actor=...|action=...|object=...|recipient=...
→ natural-language sentence

The current 927 SOURCE_RECONSTRUCTION contract is exact reconstruction of a source span under RECONSTRUCTION_MASK / GOLD_SOURCE_SPAN. The candidate learner is therefore being built as bounded extractive structural-rule induction, not a frame-to-language generator.

Decision:

~~~text
LANE_C_PROOF_FIX1=REJECT_BEFORE_RUNTIME
BLOCKER=PROOF_TARGET_SEMANTIC_MISMATCH
~~~

Repair Lane C dataset only:
- TARGET_TEXT must be a contiguous extractive span of INPUT_TEXT;
- target must not equal full input for non-identity cases;
- use multiple structural families (prefix, suffix, between-anchors);
- retain fresh entities/content and sealed independence;
- preserve duplicate, invalid-parent, negative, ambiguity, mutation, leak and restart controls.

Do not reveal Lane B implementation source.


## 927 Lane C proof FIX2 static rejection — learner-state contract mismatch

Lane C proof FIX2:

~~~text
PACKAGE_SHA256=e6c17fcfd2ebe9d2ead6d786b4a6a63de80526537cefc9ad3b02e44df6f1e086
HARNESS_SEAL_SHA256=e5422160b900ab26c6731110623b41d27043aa408eae6150357ab283f2153897
~~~

Semantic target is now correct: EXTRACTIVE_SOURCE_SPAN, with PREFIX/SUFFIX/BETWEEN_ANCHORS cases and all previously required controls present.

However the proof trains PREFIX, SUFFIX and BETWEEN examples into one learner state. Lane B FIX2 learner state supports exactly one learned structural rule/anchor set; the first incompatible rule transitions the state to AMBIGUOUS. Therefore this harness cannot validly test that learner and would fail by contract, not by lack of transfer.

Further, current unseen cases change the full learned anchors. Lane B FIX2 transfers only within a learned template/anchor set.

Decision: REJECT BEFORE RUNTIME. Repair Lane C only by using separate fresh learner states per structural family/template, with >=3 unique training examples sharing that template and fresh unseen targets under the same learned framing. Keep negative/duplicate/invalid-parent/leak/mutation/restart controls. Do not modify Lane B FIX2.


## 927 Lane C proof FIX3 static rejection — anchors still differ within rule states

Lane C FIX3 package SHA256:
d1b5edc97d6cd6e7f9c131c0c39dd2a3de807d4c33b906c2b9dc6cf1d4e0afcf

Harness seal SHA256:
bbe709bb0c90401bf4e2a21b103fe98cc73c49a782391d0d257c8d676d9ec789

Static audit: REJECT BEFORE RUNTIME.

Although PREFIX/SUFFIX/BETWEEN now use separate learner states, the three training examples inside each state still infer different exact anchors. Lane B FIX2 requires exact rule + left_anchor + right_anchor equality for support, so the second training example would make each state AMBIGUOUS.

Repair Lane C only: within each rule state, keep learned framing anchors byte-identical across >=3 unique training examples and unseen cases; vary only extracted target/content. Preserve sealed independence and all existing controls.


## Locked path to final AIto autonomous-learning bundle

Final bundle scope:

SIGMA_VKM_927_AITO_AUTONOMOUS_LEARNING_V1_PACKAGE

Done means one real non-holdout learning loop completes:
gap -> goal -> curriculum -> acquisition -> train -> fresh evaluation -> admission -> atomic persist -> fresh restart -> retained gain -> automatic next-gap continuation.

Locked remaining sequence:

1. Lane C/928: finish extractive transfer proof FIX4 with stable anchors per rule state.
2. Lane A/senior, in parallel: build black-box admission + atomic commit/rollback writer against CANDIDATE_EPOCH_V1 ABI; build-only.
3. Lane B/young, in parallel: build AIto epoch integrator around the already-audited learner FIX2 ABI plus existing local-first/MediaWiki acquisition and curriculum-to-training-example construction; build-only.
4. Admin: static-audit and pin all three packages/hashes and integration ABI.
5. User: run sealed learner transfer proof. Required non-identity unseen transfer, duplicate/invalid-parent/negative/mutation/leak/restart gates.
6. User: run real AIto learning epoch from BASELINE_06B2 with non-holdout evidence. Produce CANDIDATE_EPOCH_V1 or truthful ACQUIRE_MORE/REJECT.
7. User: run Lane A admission on a real candidate: same evaluator/scorer/gold, fresh unseen evaluation, protected regression, provenance, determinism, negative control and restart retention.
8. On COMMIT: atomically publish immutable accepted same-Sigma generation + receipt + append-only growth ledger; rollback/fail closed on interruption.
9. Build final orchestrator package that automatically handles ACQUIRE_MORE, REJECT and COMMIT and resumes from accepted state after restart.
10. User runs final black-box E2E proof; Lane C/928 audits independently. PASS requires retained measured gain and automatic selection/start of the next learning target.

928 promotion is not on this critical path.

Final invariants:
ONE_SIGMA=YES
SAME_SIGMA_IDENTITY=YES
SECOND_SIGMA_CREATED=NO
HOST_LEARNING=NO
HOST_SEMANTIC_SCORING=NO
HOST_GAIN_DECISION=NO
FROZEN_HOLDOUT_TRAINING=NO
CANONICAL/OWNER/NATIVE_BINDING mutation only through the single-writer accepted commit path where explicitly authorized.


## 927 learner FIX2 native runtime proof — PASS with replay caveat

User runtime output accepted:

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS
CANDIDATE_RUNTIME_PROOF=PASS
TRANSFER_RULE=BETWEEN
IDENTITY_TRANSFER_USED=NO
UNSEEN_NON_IDENTITY_TRANSFER=PASS
PARENT_BINDING_CONTROL=PASS
DUPLICATE_EXAMPLE_CONTROL=PASS
MINIMUM_UNIQUE_SUPPORT_CONTROL=PASS
AMBIGUITY_FAIL_CLOSED_CONTROL=PASS
DETERMINISTIC_NATIVE_OUTPUT=PASS
~~~

Candidate component SHA256:
0a1a10ee30f0f603df0be535a0a4f110a4a0d55321229eedb0a364701f5fb1df

Package SHA256:
c783549990a50237c735df3bf84589acac7af240a015213c6e93536142d26b5a

Admin audit caveat:

The package marker UNSEEN_TRANSFER_AFTER_FRESH_REPLAY=PASS is overnamed. The replay program creates a fresh learner and retrains the same three examples before reevaluating unseen cases. It does not serialize and restore the learned learner state.

Therefore classify this package as:
CANDIDATE_NATIVE_RUNTIME_SMOKE=PASS
FRESH_RETRAIN_REPRODUCIBILITY=PASS
PERSISTED_LEARNER_STATE_REPLAY=NOT_PROVEN

Do not modify the candidate learner because of this caveat. Independent Lane C proof remains required, including true persistence/restart retention when integrated.


## 927 Lane C proof FIX5 static rejection — mutation control not actually mutated

Lane C FIX5 package SHA256:
5cbd27c43ec8b887af31fe3f9793235795648c9922f06903dfaee54c9d594a7c

Phase A SHA256:
594ff1ca55a58a6944c46970118ab9b8596b03bf66c81a7e68cb9ecad8c208fe

Phase B SHA256:
f14605bedf6579543db8ed70d953d4696d3f37319cd143d9dc0172b664dde895

Positive fixes: separate seals PASS; ternary removed; JSON primitives truthfully unproven; persisted-state replay correctly deferred to integration.

Static blocker: mutation cases preserve the exact learned anchors/templates and merely change target content. Therefore SOURCE_MUTATION_SENSITIVITY can pass without any source-boundary/context mutation. Repair Lane C only: mutate/remove/corrupt at least one learned anchor or create structurally conflicting boundaries and require changed output or fail-closed. Do not change learner or sealed transfer cases.


## 927 Lane C FIX6 accepted harness; integration audit finds BETWEEN conflict gap

Lane C FIX6 package SHA256:
008141a5c443a8f4f977f10fb17c6b25cf6ffd1ac072424817b3c4727796732b

Phase A SHA256:
b997c833431350d07a7f6fe2e2cd41d3f56597560afb392105cac37f27e14f41

Phase B SHA256:
f14605bedf6579543db8ed70d953d4696d3f37319cd143d9dc0172b664dde895

Harness static audit: ACCEPTED.

Real anchor mutations are present for PREFIX, SUFFIX and BETWEEN; persisted-state replay is truthfully deferred.

Integration audit against Lane B FIX2 finds one learner defect before runtime: the BETWEEN reconstructor validates only the learned outer left/right anchors and does not reject a second/conflicting embedded frame. The sealed conflict case therefore would produce a non-null composite middle span instead of fail-closed, making the mutation/ambiguity gate fail.

Decision:
- freeze Lane C FIX6;
- repair Lane B learner only;
- add generic BETWEEN boundary uniqueness/conflict detection using approved primitives;
- do not weaken the proof harness.


## 927 Lane B learner FIX3 static acceptance

Lane B FIX3 package SHA256:
e95a17a24db421acdb168821f9e77e9ca39b1393f0cb1f648cf56cc5a54f7e06

Component SHA256:
661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573

Static audit: ACCEPTED.

Diff against FIX2 changes only sr_v1_reconstruct_between(). It adds unique learned left-boundary and terminal right-boundary checks plus second-occurrence rejection using only the approved str_find/str_slice/str_len primitive family. PREFIX/SUFFIX, public ABI, dedup, parent validation, support threshold and training semantics remain unchanged.

Lane C FIX6 remains frozen. Next gate is sealed integration/runtime proof of Lane B FIX3 against Lane C FIX6.


## 927 Lane A V1 static audit — repair required before final admission

Lane A admin-audit package ZIP SHA256:
33261b16a1e44301302adb6ce999ccadcdd530b3465bcb5a2f47c1cb018bd6f2

Manifest/file hashes verify.

Architecture positives:
- native admission separates COMMIT / REJECT / ACQUIRE_MORE and reserves HOLD for integrity/ABI;
- writer is mechanical only, single-writer, immutable generation, CAS pointer, fsync/atomic rename, append-only ledger;
- no canonical/Owner/native-binding mutation.

Blocking issues before final autonomous use:

1. Admission gain is based only on global LANGUAGE_SCORE delta. COMMIT must require positive gain for the candidate GOAL_DIMENSION itself, not merely unrelated/global gain.

2. Writer accepts any syntactically valid COMMIT receipt bound to the epoch; it does not prove the receipt was produced by the pinned native admission engine. Add admission-engine/output provenance binding so host/manual text cannot forge COMMIT.

3. Crash recovery is manual after pointer commit: PENDING.current causes PENDING_TRANSACTION_REQUIRES_ADMIN_RECOVERY. Final autonomous system needs deterministic recovery/reconciliation for POINTER_COMMITTED/ledger/receipt phases without user intervention.

Conditional integration requirement:
- if accepted-state pointer/root is not already initialized, provide one-time bootstrap binding from official BASELINE_06B2.

Do not discard Lane A V1; repair it minimally.


## 927 Lane A FIX1 deeper static audit — provenance/measurement/recovery blockers

ZIP SHA256:
7850e508f6dcf91e05831b30a401f915319b75a598846d222e55bd959155df67

Positive repairs confirmed:
- COMMIT requires positive GOAL_DIMENSION gain as well as positive global gain.
- writer implements immutable generation/CAS/single-writer/fsync and forward crash recovery phases.
- receipt/native-output/epoch SHA fields are cross-bound.

Remaining blockers before final autonomous admission:

1. Native-output origin is not actually proven. The writer accepts externally supplied admission/native-output files and verifies only their bytes/declared hashes. A manually fabricated native-output file can still claim the correct engine SHA. Final writer/runner must mechanically launch the pinned native admission execution itself (or consume a sealed execution transcript produced by the pinned VM/runner in the same transaction) rather than trust arbitrary supplied decision text.

2. Admission does not bind before/after measurements to the accepted 06B2 measurement system (evaluator/scorer/gold/mapping/measurement lock). Positive scores from a different or fabricated measurement artifact could satisfy the current engine. Add pinned measurement-system identity checks and restrict GOAL_DIMENSION to the official eight dimensions.

3. Recovery is not self-contained: restart still requires the caller to resupply the exact old epoch/admission/engine/native-output/candidate paths before PENDING recovery can run. PREPARED recovery also depends on the original candidate-state file. Stage immutable transaction inputs under the writer transaction directory before PREPARED and recover from those staged inputs alone.

Also do not emit COMMIT_PERFORMED=NO after a HOLD if the pointer may already have been committed; report phase-aware commit state.

Do not redesign the topology; repair minimally.


## 927 Lane A FIX2 static audit — final consolidated blockers before runtime

Uploaded ZIP SHA256:
675e8613e1ab01def86cf676d3b01231ec0e98f28866a70b497f4520d791199b

Note: 7850e508... in the manifest is PARENT_FIX1_PACKAGE_SHA256, not this FIX2 ZIP SHA.

Positive repairs confirmed:
- native admission engine and runner are pinned and mechanically executed;
- goal-dimension gain > 0 is required for COMMIT;
- official eight dimensions are enforced;
- transaction inputs are staged immutably before PREPARED;
- restart recovery is self-contained from staged inputs;
- phase-aware COMMIT_PERFORMED reporting is present;
- single-writer/CAS/immutable generation/fsync/growth-ledger architecture remains intact.

Remaining consolidated blockers:

1. BEFORE/AFTER measurement files, protected_regression.env and retention_proof.env are still externally supplied assertions. Their hashes are bound to CANDIDATE_EPOCH, but origin is not proven. Final admission must mechanically produce them with pinned producer runners in the admission transaction, or verify sealed execution transcripts from pinned producer runners that are also staged and bound.

2. Measurement identity conflates the accepted measurement-summary SHA aff498... with the top-level BASELINE_06B2 MEASUREMENT.lock SHA 57f8951806a8304bd77e82d451dcee87c2b2713b0c259635393c09f6c290eada. Final contract must bind both separately:
   MEASUREMENT_LOCK_SHA256=57f895...
   MEASUREMENT_SUMMARY_SHA256=aff498...
   plus evaluator/scorer/gold/mapping pins.

3. First-run bootstrap is absent. load_pointer() requires an existing SIGMA_VKM_927_ACCEPTED_STATE.current. Final writer needs a one-time, fail-closed bootstrap from official BASELINE_06B2 / accepted parent representation, with exact pinned identity and no overwrite if a pointer already exists.

4. Candidate-state bytes are copied on COMMIT but candidate state format/replay-load validity is not mechanically proven by the writer. Bind candidate-state validation/replay transcript to the same admission transaction, ideally through the retention producer.

Do not redesign COMMIT/REJECT/ACQUIRE_MORE or writer topology. Repair these in one FIX3 before any runtime use.


## 927 TRẺ AIto Epoch V1 static rejection — learner/evaluator path mismatch

TRE__AITO_EPOCH_V1 package SHA256:
dfb2d60cb2bfbbcba2460a07505337b8635cc6b9324c87ef81f3eb9aa6675afd

Static positives:
- learner FIX3 byte-identical and pinned;
- no admission/commit/canonical/Owner/native-binding mutation;
- goal/curriculum selection and source eligibility are Sigma/VKM-side;
- acquisition is bounded and provenance/dedup aware;
- candidate replay journal is deterministic.

Blocking architecture defects before runtime:

1. Training and evaluation are disconnected.
The learner FIX3 is trained and projected, but AFTER measurement is produced by R15 from TRE__R15_CANDIDATE_MODEL_V1, which is a legacy accepted-state evidence model containing raw evidence records. R15 does not evaluate the learned sigma_sr_* candidate state. Therefore measured gain cannot be attributed to learner FIX3.

2. Public compatibility path is not integrated.
The official evaluator measures sigma_model_source_reconstruction_v1(effective_state,input_text). This package does not wire the learned sigma_sr_reconstruct_v1 behavior into that public model path. A candidate learner can PASS its private transfer proof while remaining invisible to the official evaluator.

3. Curriculum teaches a synthetic fixed wrapper:
INPUT_TEXT=[[SOURCE]] + evidence + [[/SOURCE]]
TARGET_TEXT=evidence
This learns a delimiter-specific BETWEEN rule. It does not establish that the learned behavior applies to the official SOURCE_RECONSTRUCTION input contract.

4. Retention proof re-runs training from original in-memory records; it does not reconstruct from the serialized TRE__PERSISTED_CANDIDATE_STATE_V1 file. Candidate-state parser/load/replay integrity is therefore not proven.

5. TRE__PROTECTED_REGRESSION_V1 is a host-written summary of evaluator integrity markers, not an independently produced protected-regression artifact proving candidate behavior did not regress protected capabilities.

Decision:
RUN_FORBIDDEN=YES
Do not discard learner FIX3 or acquisition transport. Repair the integrator architecture so the exact learned candidate state is the state measured by the official evaluator through the public model ABI.


## Neutral integration R1 static rejection — recursive baseline hashing touches frozen/gold

INT package SHA256:
e881234903d6cb6e3fb4eb080de61ed96eff538d4195f4d1eb6b87423ce917b5

Pinned embedded source hashes are correct:
- learner FIX3: 661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573
- Lane C Phase A FIX6: b997c833431350d07a7f6fe2e2cd41d3f56597560afb392105cac37f27e14f41

Static assembly is otherwise black-box and preserves both sources.

Blocker:
tools/find_exact_hash.py and tools/tree_digest.py recursively open/hash every file under BASELINE_06B2. This can open/hash frozen/gold holdout artifacts during a non-holdout transfer proof, violating holdout isolation discipline.

Repair neutral runner only:
- remove recursive content scan/hash of BASELINE_06B2;
- verify only explicit public/top-level baseline identity artifacts by fixed path and pinned SHA;
- protect baseline mutation through read-only/static path discipline and explicit allowed artifact hashes, not recursive content reads;
- preserve learner/proof source SHAs byte-identical;
- optionally compare phase_a.meta and unseen_after.txt across the three runs as well as stdout.

Do not modify learner FIX3 or proof FIX6.


## Neutral integration R1 FIX1 static rejection — exact baseline paths wrong

INT FIX1 package SHA256:
8429a464615a75b0a2fcf7539644e5c8e7a056d17a01b5e972062d498932c44f

Positive: recursive baseline scan/hash removed; learner/proof source pins remain exact; three-run output/meta/unseen comparison present.

Blocker: runner uses guessed top-level filenames. Official BASELINE_06B2 paths are:
- BASELINE.lock
- SNAPSHOT_MANIFEST.lock
- MEASUREMENT.lock
- SNAPSHOT/measurement/SIGMA_VKM_927_CAPABILITY_GAP_LEDGER_V1
- SNAPSHOT/proofs/SIGMA_VKM_927_PROTECTED_REGRESSION_THROUGH_06B2_V1

Repair runner only: use these exact fixed paths with pinned SHAs, add BASELINE.lock SHA pin c6ab1c..., preserve no-recursive-scan/no-frozen-open discipline.


## 927 TRẺ AIto Epoch V2 static rejection — scorer/reconstruction path still disconnected

TRE__AITO_EPOCH_V2 package SHA256:
b5cbe6bd2401f52ac9f5ce856b17a8aa5802439f90eed43a200965c778bf42ff

Static syntax and SHA256SUMS verification PASS. Learner FIX3 remains byte-identical at:
661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573

Positive repairs confirmed:
- persisted candidate state is parsed from bytes and learner state is reconstructed from persisted records;
- candidate-only public source-reconstruction bridge exists without canonical mutation;
- old [[SOURCE]] wrapper is removed;
- R15 runner/adapter output provenance is retained.

Remaining blockers before runtime:

1. Candidate scorer path still passes an empty reconstruction candidate whenever sigma_model_score_probe_v1 exposes RECONSTRUCTION_CANDIDATE:
   elif kind=="RECONSTRUCTION_CANDIDATE": args.append('""')
   Therefore SOURCE_RECONSTRUCTION scoring does not consume sigma_sr_reconstruct_v1 output. The claimed callflow sigma_model_score_probe_v1 -> sigma_model_source_reconstruction_v1 is not implemented by the score harness.

2. New curriculum is identity-only:
   INPUT_TEXT = evidence text
   TARGET_TEXT = evidence text.
   This trains learner FIX3's IDENTITY hypothesis, while accepted RECONSTRUCTION_MASK scoring compares reconstruction_candidate to GOLD_SOURCE_SPAN. Identity compatibility is not a sufficient binding to the official reconstruction task. Build non-holdout reconstruction pairs from the approved pre-frozen probe/builder contract (or fail closed if that contract cannot be bound) rather than assuming whole-evidence identity.

3. RETENTION_PROOF only compares restored learner state projection. It does not prove restored candidate behavior on fresh unseen reconstruction cases. Retention must rerun the same non-holdout unseen transfer cases from persisted bytes in a fresh VM/process.

4. CANDIDATE_EPOCH_V1 sets PROTECTED_REGRESSION_SHA256 to TRE__R15_EXECUTION_PROVENANCE_V2.lock. Provenance is not a protected-regression proof. Bind the actual candidate protected-regression execution/result artifact separately; keep execution provenance as its own field/artifact.

Decision:
RUN_FORBIDDEN=YES
Repair TRE integrator only; learner FIX3 remains frozen.


## Neutral integration R1 FIX2 — static accepted for user runtime

Package SHA256:
effa3527a5c2b62ffcf597b8d33ca30f8032a69b0a57a27923ec4f17903593e3

Static audit accepted:
- learner FIX3 SHA exact: 661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573
- Lane C Phase A FIX6 SHA exact: b997c833431350d07a7f6fe2e2cd41d3f56597560afb392105cac37f27e14f41
- official BASELINE_06B2 fixed public paths/pins correct;
- no recursive baseline scan;
- no frozen/gold open/hash;
- canonical/compiler/VM pins checked;
- three fresh VM runs compare native.out, phase_a.meta and unseen_after.txt byte-for-byte;
- required transfer/negative/duplicate/invalid-parent/leak/mutation gates are enforced;
- no admission/commit/promotion.

Decision: USER_RUNTIME_ALLOWED=YES.


## 927 Lane A FIX3 static audit — new senior takeover; two trust-root blockers

New senior/Lane A takeover package:

~~~text
GIA__ADMISSION_WRITER_FIX3.zip
ZIP_SHA256=a57b0d18c09cb0bdbe29989157a00ee5f3765fa52bd04a0741a8e37a899f496e
~~~

Manifest artifact hashes and Python syntax verify.

Positive FIX3 repairs confirmed:
- caller-supplied measurement/protected/retention claims removed;
- native admission engine remains decision authority;
- measurement lock and measurement summary pins separated correctly;
- candidate replay/load proof is part of COMMIT chain;
- staged-input crash recovery architecture preserved;
- one-time baseline bootstrap path added.

Static blockers:

1. EXECUTION_RUNNER trust root is impossible as written.
FIX3 requires the execution runner SHA to appear on a RUNNER line inside official MEASUREMENT.lock. The exact accepted MEASUREMENT.lock SHA 57f895... corresponds to the published 06B2 lock and contains no RUNNER field. Therefore production execution necessarily HOLDs at EXECUTION_RUNNER_NOT_PINNED_BY_MEASUREMENT_LOCK.

Repair: do not mutate/replace official MEASUREMENT.lock. Bind the exact production evidence runner SHA in a separate immutable admission integration lock/final orchestrator pin, or hard-pin it after the producer runner is frozen.

2. BASELINE_06B2 bootstrap performs recursive rglob/hash search for a matching state/model artifact. This reintroduces recursive baseline discovery and may touch protected/frozen contents. Bootstrap must use one explicit approved parent-state artifact path + SHA/role from a pre-bound public baseline contract; no recursive discovery.

Also the bootstrap parent identity must be explicitly defined as the accepted-state artifact SHA, not conflated with BASELINE_06B2 directory/BASELINE.lock SHA.

Decision:
GIA_FIX3=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES

The new senior window is accepted as Lane A successor; preserve existing architecture and repair only these trust-root/bootstrap issues.


## 927 TRẺ AIto Epoch V3 static rejection — curriculum compatibility selection missing

TRE__AITO_EPOCH_V3 package SHA256:
067d4f18c757b6372f98037232af3d5257810b1237771400987ffc216dacef8b

Positive repairs confirmed:
- learner FIX3 byte-identical and pinned;
- actual reconstruction candidate reaches accepted scorer through candidate-only public bridge;
- non-holdout reconstruction pairs are generated using the pinned public/pre-frozen reconstruction-mask builder contract without opening frozen/gold;
- persisted candidate state is parsed from bytes and fresh unseen behavior is rechecked after restore;
- protected-regression result and execution provenance are separate artifacts;
- ONE_SIGMA / same identity boundaries preserved.

Remaining blocker:
The integrator takes the first four valid reconstruction pairs, trains on the first three, and reserves the fourth unseen. Learner FIX3 requires compatible structural rule + exact anchors across its support examples. V3 has no Sigma-side compatibility grouping/selection, so arbitrary eligible evidence can drive the learner to AMBIGUOUS and then be classified as integrity HOLD even though more/other evidence could form a valid curriculum.

Required repair:
- host must not inspect/choose anchors semantically;
- add a Sigma/VKM-side curriculum packer/selector that finds a compatible group of >=3 unique TRAIN pairs plus >=1 same-template unseen pair using learner-native behavior;
- if no compatible group exists, return ACQUIRE_MORE, not HOLD;
- do not modify learner FIX3, evaluator, proof harness, or ONE_SIGMA identity.

Decision:
TRE_AITO_EPOCH_V3=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES


## 927 Lane A FIX4 static audit — architecture accepted, bootstrap artifact-location mismatch

GIA__ADMISSION_WRITER_FIX4.zip SHA256:
b63f1cb7f4c9969c5ea7057c4c39a40c1075eb525e7bedf8389abc61ba771656

Positive FIX4 repairs confirmed:
- execution-runner trust root separated from official MEASUREMENT.lock;
- official measurement lock/summary pins preserved;
- recursive baseline discovery removed;
- public bootstrap contract is explicit, fail-closed, symlink-safe;
- admission/writer architecture remains ONE_SIGMA and same-identity;
- Python syntax passes.

Current integration blocker:
FIX4 bootstrap contract requires PARENT_STATE_RELATIVE_PATH to resolve underneath SIGMA_VKM_927_BASELINE_06B2. The accepted continuity replay model used by 06B2 measurement is actually the explicit ONE_SIGMA artifact-store model:
  $ONE_SIGMA_ROOT/.sigma_ail/927_05b_replay_model/SIGMA_VKM_927_REPLAY_MODEL_V1.model
and is not a file carried inside BASELINE_06B2 snapshot.

Therefore a valid baseline-relative parent-state contract cannot currently be populated.

Decision:
GIA_FIX4_ARCHITECTURE=PASS
GIA_FIX4_RUNTIME_READY=NO

Final repair direction:
- keep no-recursive-discovery;
- replace baseline-relative parent-state contract with an explicit ONE_SIGMA accepted-parent-state contract that pins one fixed absolute/root-relative artifact-store path + exact SHA + role;
- derive/pin its exact SHA only from the accepted 05B/06B2 continuity authority, never by filename search;
- keep BASELINE_06B2_SHA256 separate from PARENT_ACCEPTED_STATE_SHA256;
- final orchestrator still binds EXECUTION_RUNNER_SHA256 separately.


## Neutral integration R1 FIX3 — static accepted; admin backup role clarified

INT__SR_FIX3_X_928_FIX6_R1_FIX3 package SHA256:
6cefaa1eb3b4d7db5ada94c4e6273a45a426b81406b22ea88824a8f9aaec1326

Static audit accepted:
- role remains NEUTRAL_INTEGRATOR;
- no admission/commit/promotion logic;
- ONE_SIGMA_ROOT=$HOME/SIGMA/sigma_genesis1;
- learner FIX3 and 928 Phase A FIX6 remain exact pinned sources;
- exact dependency closure adds only approved public components 927-01, 927-03, 927-06B1;
- no gold/holdout component use;
- no recursive baseline scan;
- no canonical/Owner/native-binding mutation;
- three-run determinism gates remain.

Role policy:
- Admin backup owns neutral integration / continuity / cross-lane ABI assembly.
- New senior (GIÀ mới) owns Lane A admission + accepted-state writer.
- Do not merge these roles unless explicit takeover is required.


## 927 TRẺ AIto Epoch V4 static rejection — holdout pre-open and parent-state identity mismatch

TRE__AITO_EPOCH_V4 package SHA256:
2c40036fdd372726a409ee929a887af406f9503c4b70572b665d8e837df15f34

Positive V4 repair confirmed:
- Sigma/VKM-side curriculum selector now selects 3 unique compatible TRAIN pairs + 1 compatible untrained validation pair using learner FIX3 behavior;
- no compatible group -> ACQUIRE_MORE, not HOLD;
- learner FIX3 remains pinned;
- scorer/public bridge, persisted restore, retention behavior and protected-regression separation from V3 are preserved;
- ONE_SIGMA markers remain.

Two blocking cross-lane defects:

1. parse_manifest() hashes every target in SNAPSHOT_MANIFEST.lock before training. That opens/hashes SNAPSHOT/frozen/* and other holdout artifacts before the learning epoch, violating holdout isolation. Parse manifest metadata only, then verify only explicitly required public/pre-frozen artifacts by fixed path/role/SHA. Frozen/gold may be opened only later by the pinned evaluator after candidate training.

2. First-epoch parse_pointer() defaults PARENT_ACCEPTED_STATE_SHA256 to BASELINE_06B2 SHA and reconstructs base_seq mechanically from the 05B persistence component source. Lane A final architecture separates BASELINE_06B2 identity from the actual accepted parent-state artifact identity. Final integrator must consume the same explicit ONE_SIGMA accepted-state pointer/contract as Lane A, including first-epoch bootstrap. Do not conflate BASELINE_SHA with PARENT_ACCEPTED_STATE_SHA256 and do not infer accepted state from component source.

Decision:
TRE_AITO_EPOCH_V4=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES

Repair once in V5:
- no pre-training frozen/gold open/hash;
- require explicit accepted-state pointer/contract and exact parent-state artifact SHA;
- keep BASELINE_06B2 pin separately;
- preserve V4 curriculum selector and all V3 fixes;
- SECOND_SIGMA_CREATED=NO.


## Neutral integration R1 FIX4 — static accepted

Package SHA256:
bb2983f8da4780a651dfb6891577eb63a2242c4e78197aa246f7fc420f10222f

Static audit accepted.

FIX3 -> FIX4 delta is surgical:
- only duplicate-DEF audit logic changed;
- duplicate DEF names inside the same exact SHA-pinned accepted source are no longer misclassified as integration collisions;
- duplicate DEF names across different assembled sources still fail closed;
- learner FIX3 SHA unchanged;
- 928 Phase A FIX6 SHA unchanged;
- exact baseline public path pins unchanged;
- no recursive baseline scan;
- no frozen/gold use;
- no admission/commit/promotion;
- ONE_SIGMA root unchanged.

Python syntax, Bash syntax, and internal SHA256SUMS all PASS.

Decision:
NEUTRAL_INTEGRATION_FIX4_STATIC=PASS
RUNTIME_COMMAND_AUTHORITY=ADMIN_BACKUP_WINDOW


## 927 Lane A FIX4_FINAL audit — same parent-state location blocker remains

Uploaded file:
GIA__ADMISSION_WRITER_FIX4_FINAL.zip

ZIP SHA256:
353cb841cb71d356976ec1e150ef77543efeffa954ebc3fa2b72abbd0a0f2732

Internal artifact manifest hashes verify and Python syntax passes.

However the package still uses:
ONE_SIGMA_PARENT_STATE_RELATIVE_PATH
resolved strictly underneath BASELINE_06B2.

The shipped public-contract schema is still unpopulated and baseline-relative:
ONE_SIGMA_PARENT_STATE_RELATIVE_PATH=
PARENT_ACCEPTED_STATE_SHA256=

The accepted continuity replay model used by 06B2 is outside the BASELINE_06B2 snapshot under the ONE_SIGMA artifact store:
$ONE_SIGMA_ROOT/.sigma_ail/927_05b_replay_model/SIGMA_VKM_927_REPLAY_MODEL_V1.model

Therefore the prior integration blocker is unchanged.

Decision:
GIA_FIX4_FINAL_ARCHITECTURE=PASS
GIA_FIX4_FINAL_RUNTIME_READY=NO
RUN_FORBIDDEN=YES

Required repair remains:
use an explicit ONE_SIGMA root-relative accepted-parent-state artifact path + exact SHA + role; keep BASELINE_06B2 identity separate; no recursive discovery; preserve same Sigma identity.


## 927 TRẺ AIto Epoch V5 static rejection — accepted pointer not constrained to ONE_SIGMA root

TRE__AITO_EPOCH_V5 package SHA256:
e7ebeacef42baf715eb97d49ad9e75d2c124e91a1f8207273afdd9e4ccef72f4

Positive V5 repairs confirmed:
- manifest parse is metadata-only before training;
- explicit public/pre-frozen allowlist only;
- no frozen/gold target is opened/hashed before candidate training;
- BASELINE_06B2 identity is separated from accepted-state identity;
- no 05B source inference fallback;
- missing accepted pointer returns truthful BOOTSTRAP_REQUIRED;
- V4 Sigma/VKM curriculum selector and prior V3 fixes are preserved;
- learner FIX3 remains pinned.

Single remaining blocker under the locked ONE_SIGMA doctrine:
parse_pointer() accepts TRE_ACCEPTED_STATE_POINTER and ACCEPTED_STATE_PATH from arbitrary filesystem locations. It pins bytes/schema but does not require the pointer/state to be non-symlink regular files under the same ONE_SIGMA_ROOT, nor bind the accepted-state role/root in the pointer contract. An external or second-Sigma state could therefore satisfy the current parser.

Required V6 repair:
- pointer path and accepted state path must resolve under $ONE_SIGMA_ROOT only;
- reject symlinks/traversal/out-of-root paths;
- require pointer fields that bind ONE_SIGMA=YES, SAME_SIGMA_IDENTITY=YES, SECOND_SIGMA_CREATED=NO and accepted-state role;
- align exact pointer/state schema with Lane A FIX5 contract;
- preserve all V5 behavior unchanged.

Decision:
TRE_AITO_EPOCH_V5=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES


## 928 final E2E proof V1 static rejection — toy dimensions and non-operative controls

Package SHA256:
2db26d8a792396abf7d17c23dd5d79e39214e66047c6a2c7ea2e4d7d68499866

Static positives:
- black-box-only ABI;
- host learning/scoring/gain decisions forbidden;
- restart, interrupted transaction, duplicate evidence, stale parent, corrupted candidate and unavailable-source concepts are present;
- Phase 1/2/3/4 are separated;
- same-identity / single-instance markers are checked;
- no compiler/VM run claimed.

Blocking proof defects:

1. Final proof uses synthetic goal dimensions DIM_ALPHA / DIM_BETA instead of Project 927 official eight dimensions. The first real autonomous cycle must bind to the actual current gap SOURCE_RECONSTRUCTION, and continuation must select another valid official dimension. A final proof must not require an implementation adapter to invent toy dimensions.

2. FAKE_COMMIT_RECEIPT control is non-operative: bb_fake_commit_rejected() only constructs a local map and compares literal strings; it never submits a forged receipt to Lane A writer/admission.

3. FAKE_MEASUREMENT control is non-operative: Phase 0 writes UNTRUSTED_FAKE_MEASUREMENTS.txt then unconditionally prints FAKE_MEASUREMENT_FILES_TRUSTED=NO. The system is never challenged with that fake evidence.

4. Protected regression is replaced by three private aito_bb_eval canaries. These are useful independent canaries but cannot substitute for the real pinned protected-regression/admission artifact chain.

5. Crash-interrupt Phase 3 prints READY_FOR_FORCED_KILL=YES without verifying the transaction actually reached PREPARED and accepted state remained unchanged before kill.

6. ONE_SIGMA check is only self-reported through aito_bb_snapshot(). Final runner needs an independent mechanical root/path boundary check against the single ONE_SIGMA_ROOT in addition to behavioral identity continuity.

Repair direction:
- keep independent non-holdout canaries, but map first cycle to SOURCE_RECONSTRUCTION and official dimension vocabulary;
- expose black-box operations that actually inject forged receipt / fake measurement into the real admission path and require rejection;
- bind official measurement/protected-regression/admission receipt hashes/status while retaining independent canaries;
- require PREPARED state before forced kill;
- add neutral-runner mechanical ONE_SIGMA root/path verification;
- preserve implementation-source isolation.

Decision:
928_AITO_FINAL_E2E_PROOF_V1=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES


## Neutral integration FIX4 runtime — accepted sealed learner proof

User runtime result accepted:

~~~text
STATUS=PASS
SYSTEM_INTEGRITY_STATUS=PASS
NEUTRAL_INTEGRATION_RUNTIME=PASS
NON_IDENTITY_FAMILIES_GATE=PASS
THREE_RUN_ARTIFACT_DETERMINISM=PASS
CANONICAL_UNCHANGED=PASS
OWNER_UNCHANGED=PASS
NATIVE_BINDING_UNCHANGED=PASS
BASELINE_PUBLIC_IDENTITIES_UNCHANGED=PASS
FROZEN_OPENED=NO
FROZEN_HASHED=NO
RECURSIVE_BASELINE_SCAN=NO
LEARNER_SOURCE_MODIFIED=NO
PROOF_SOURCE_MODIFIED=NO
PHASE_B_USED=NO
ADMISSION_PERFORMED=NO
COMMIT_PERFORMED=NO
PROMOTION_PERFORMED=NO
~~~

Pinned runtime artifacts:
- learner FIX3 SHA256=661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573
- proof Phase A FIX6 SHA256=b997c833431350d07a7f6fe2e2cd41d3f56597560afb392105cac37f27e14f41
- assembled source SHA256=2de3d77f1560c2f87c2ab962dfb81626d758e44204ea57aef4db38c434da9e0b
- bytecode SHA256=ecb0767b13e14e6df5494c587d65ac7d430fea54811780b93581faefc4d14fc0
- deterministic native.out SHA256=003c99746466c5844f99e178da20ec17ba41d7a1e91b3de1974ae310c2ce429c
- deterministic phase_a.meta SHA256=f8cdaf1255e05ef57ca6cbd170e5ae6dd22edc5a8328217ed715f56846dbb61c
- deterministic unseen_after SHA256=af8169c6d8e2cc6d7bffeda2dc2b27322e8a3f0c17620fe7228d2b0c7f6d7c42

Admin conclusion:
SOURCE_RECONSTRUCTION_LEARNER_FIX3_SEALED_TRANSFER_PROOF=PASS

This closes the learner-mechanism transfer gate.
Do not reopen or modify learner FIX3 or Lane C Phase A FIX6 unless a later integration failure proves a real defect.

Phase B persisted-state replay remains intentionally deferred to AIto integration/admission.


## 927 TRẺ AIto Epoch V6 static audit — code sound, final pointer ABI waits on Lane A FIX5

TRE__AITO_EPOCH_V6 package SHA256:
5717ebb068ada8e0c34047d7ded95d90a0f5addcd992a1e44ebecf073f623788

Static positives:
- learner FIX3 remains exact SHA 661d3047...09573;
- no pre-training frozen/gold target open/hash;
- accepted pointer and state are constrained under $HOME/SIGMA/sigma_genesis1;
- canonical absolute regular-file requirement;
- traversal, symlink component, out-of-root and realpath escape rejection;
- pointer requires ONE_SIGMA=YES, SAME_SIGMA_IDENTITY=YES, SECOND_SIGMA_CREATED=NO;
- baseline identity remains distinct from accepted-state identity;
- missing pointer fails closed as BOOTSTRAP_REQUIRED;
- V5 non-pointer runtime components are byte-identical;
- package SHA256SUMS, Python syntax and Bash syntax PASS.

Cross-lane blocker:
V6 claims LANE_A_FIX5_POINTER_CONTRACT_ALIGNED=PASS before Lane A FIX5 contract is finalized. Current V6 pointer schema checks ACCEPTED_STATE_PATH + ACCEPTED_STATE_SHA256 and identity markers but does not bind the explicit accepted-parent-state role/root-relative contract required for Lane A FIX5.

Decision:
TRE_AITO_EPOCH_V6_CODE=STATIC_SOUND
TRE_AITO_EPOCH_V6_RUNTIME_READY=NO
NEXT_ACTION=FREEZE_V6_PENDING_LANE_A_FIX5_POINTER_CONTRACT

Do not ask Lane B to guess another schema. After Lane A FIX5 is audited and its exact pointer/accepted-state ABI is frozen, perform at most one final mechanical alignment if needed. No learner/curriculum/evaluator redesign.


## 927 Lane A FIX5 static audit — parent contract repaired, accepted-root escape remains

GIA__ADMISSION_WRITER_FIX5.zip SHA256:
c87747352629c6ded96ba3b48822a3216659ff8a276581e20eb352b97d2c2f7f

Positive repairs confirmed:
- parent artifact is no longer required under BASELINE_06B2;
- explicit ONE_SIGMA root-relative parent path is pinned:
  .sigma_ail/927_05b_replay_model/SIGMA_VKM_927_REPLAY_MODEL_V1.model
- BASELINE_06B2_SHA256 remains independent from PARENT_ACCEPTED_STATE_SHA256;
- parent role is ACCEPTED_PARENT_STATE;
- recursive discovery / filename guessing remain forbidden;
- all 17 manifest artifact hashes verify;
- Python syntax passes;
- FIX4 admission/runner architecture is preserved.

New remaining blocker:
The accepted-state writer still allows SIGMA_927_ACCEPTED_ROOT to override the accepted-state store to an arbitrary filesystem location. main() creates/uses that path without requiring it to resolve under the locked ONE_SIGMA_ROOT and without rejecting an accepted-root symlink. Therefore pointer/generations/transactions can live outside the single Sigma while pointer_text self-reports ONE_SIGMA=YES.

Also the accepted pointer ABI currently omits SECOND_SIGMA_CREATED=NO. Since this pointer is the cross-lane continuity identity, final ABI should carry and validate this hard invariant.

Decision:
GIA_FIX5_PARENT_CONTRACT_REPAIR=PASS
GIA_FIX5_RUNTIME_READY=NO
RUN_FORBIDDEN=YES

Required FIX6:
- lock accepted root to $HOME/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_VKM_927_ACCEPTED_STATE;
- reject SIGMA_927_ACCEPTED_ROOT overrides unless canonical-resolved path equals that exact root;
- reject symlink components / realpath escape for accepted root;
- ensure ROOT resolves to the same canonical ONE_SIGMA_ROOT;
- add SECOND_SIGMA_CREATED=NO to ACCEPTED_STATE_POINTER_V1 and validate it;
- preserve FIX5 parent contract exactly;
- no other redesign.


## 928 final E2E proof V2 static rejection — false-pass controls and incomplete crash/receipt binding

928__AITO_FINAL_E2E_PROOF_V2.tar.gz SHA256:
1fa9d3eece071ea440c3a5ba595c73ab2feef6589d0cbcab9af85b961ebf5f4f

Positive V2 repairs confirmed:
- synthetic DIM_ALPHA/DIM_BETA removed;
- first goal is SOURCE_RECONSTRUCTION;
- forged COMMIT and fake measurement now call explicit black-box boundary APIs;
- crash Phase 3 requires TRANSACTION_STATUS=PREPARED and unchanged accepted/persisted state before kill;
- a neutral host root verifier exists;
- private 928 canaries remain supplemental;
- no Sigma compile/VM run claimed.

Blocking defects:

1. PHASE_0 rejected(r) returns TRUE when r==NULL. A missing/unwired black-box submit/continue API can therefore PASS a fail-closed control. NULL must always fail the proof.

2. PHASE_0 collapses all controls into REJECT semantics. This conflicts with locked 927 doctrine:
   - forged receipt / invalid measurement provenance / stale parent / corrupt candidate are integrity failures => explicit HOLD/fail-closed;
   - duplicate-only insufficient evidence and unavailable acquisition => ACQUIRE_MORE;
   - NULL/empty/unknown result => proof FAIL.
The final proof must assert an explicit expected status/decision matrix rather than generic rejected().

3. PHASE_1 vocab8() checks only len=8, uniqueness, and presence of SOURCE_RECONSTRUCTION. Seven synthetic names could still pass. Require exact set equality:
ROLE_BINDING
POLARITY_MODALITY
COREFERENCE
TEMPORAL_CAUSAL
CONTRAST_SENSITIVITY
MEANING_INVARIANCE
SOURCE_RECONSTRUCTION
PARAGRAPH_COHERENCE

4. Lane-A proof binding is still self-referential. aito_bb_lane_a_regression_pin() and aito_bb_protected_regression_attestation() both come from the system under test and are only compared with each other. In addition, the COMMIT receipt is only checked for DECISION=COMMIT; official measurement hashes / goal gain / candidate-parent binding / retention proof / protected regression hashes are not independently asserted.
Final proof must bind receipt fields to independently supplied/frozen Lane-A pins and verify:
PARENT_ACCEPTED_STATE_SHA256
CANDIDATE_STATE_SHA256
GOAL_DIMENSION=SOURCE_RECONSTRUCTION
BEFORE_MEASUREMENT_SHA256
AFTER_MEASUREMENT_SHA256
PROTECTED_REGRESSION_SHA256
RETENTION_PROOF_SHA256
MEASUREMENT_LOCK_SHA256=57f8951806a8304bd77e82d451dcee87c2b2713b0c259635393c09f6c290eada
MEASUREMENT_SUMMARY_SHA256=aff498947caf113b9c0e69de4ac435a4ca1bc0c5b9289aa2af743c7559bf4ca7
MEASURED_SEMANTIC_GAIN>0
GOAL_DIMENSION_GAIN>0
SAME_SIGMA_IDENTITY=YES
and final Lane-A engine/runner/execution-runner pins once Lane A FIX6 is frozen.
Private canary gain remains supplemental, never the official admission measurement.

5. NEUTRAL_ROOT_VERIFY.py resolves the path before checking components. An in-root symlink such as root/a -> root/b disappears during resolve(), so SYMLINK_ALLOWED=NO is not actually enforced. Inspect raw path components with lstat/no-follow before resolve, then separately require resolved path under canonical ONE_SIGMA root.

6. PHASE_4 prints PARTIAL_COMMIT_VISIBLE=NO without comparing accepted/persisted hashes to the pre-crash values. Phase 3 must write immutable witness hashes before kill; Phase 4 must require both hashes unchanged after automatic rollback/cleanup.

Decision:
928_AITO_FINAL_E2E_PROOF_V2=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES

Coordination:
- 928 may repair its internal semantics now.
- Do not invent final Lane-A engine/runner/execution-runner pins; accept them only as external immutable neutral-runner inputs after GIA FIX6 is frozen.
- No implementation-source dependency.


## 927 Lane A FIX6 static accepted — pointer ABI frozen

GIA__ADMISSION_WRITER_FIX6.zip SHA256:
b3955cf18807fefa18eec53c104f045a2f2a6f6ed8cf3bd4e22b87a21191ede9

Static audit PASS:
- all 18 artifact manifest hashes verify;
- Python syntax passes;
- accepted root is exactly $HOME/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_VKM_927_ACCEPTED_STATE;
- ROOT and SIGMA_927_ACCEPTED_ROOT overrides must canonical-resolve to exact locked roots or HOLD;
- traversal/symlink component/realpath escape/alternate accepted store rejected;
- accepted subdirectories are root-bound and symlink-safe;
- pointer now requires ONE_SIGMA=YES, SAME_SIGMA_IDENTITY=YES, SECOND_SIGMA_CREATED=NO;
- FIX5 parent-state contract preserved exactly;
- BASELINE_06B2 identity remains separate from PARENT_ACCEPTED_STATE_SHA256;
- no recursive discovery/filename guessing;
- no admission semantic redesign.

Frozen Lane A FIX6 component pins:
ADMISSION_ENGINE_SHA256=acda382c23dce7713e0e50751d4c041941f2f943d3be56efc66618d60f10f0da
ADMISSION_NATIVE_RUNNER_SHA256=d3f82a2abb3db78f5a3101737938c43727c2fc1b458950f9d15e3fb1cd4acfc0
ACCEPTED_STATE_WRITER_SHA256=bac004283c8be5bd9d960f11329edd4ec752022950ecb3622d453b6c334e368c

Frozen accepted pointer ABI:
PATH=$HOME/SIGMA/sigma_genesis1/.sigma_ail/SIGMA_VKM_927_ACCEPTED_STATE/SIGMA_VKM_927_ACCEPTED_STATE.current
SCHEMA=SIGMA_VKM_927_ACCEPTED_STATE_POINTER_V1
ONE_SIGMA=YES
SAME_SIGMA_IDENTITY=YES
SECOND_SIGMA_CREATED=NO
ACCEPTED_STATE_SHA256=
GENERATION_RELATIVE_PATH=
PARENT_ACCEPTED_STATE_SHA256=
ADMISSION_RECEIPT_SHA256=

Accepted state resolves mechanically as:
$ACCEPTED_ROOT/$GENERATION_RELATIVE_PATH/STATE.model

Important cross-lane consequence:
TRE V6 is NOT pointer-ABI aligned because it expects ACCEPTED_STATE_PATH, which Lane A does not emit. TRE must mechanically derive STATE.model from GENERATION_RELATIVE_PATH under the exact accepted root. Do not invent ACCEPTED_STATE_PATH.

The blank EXPECTED_BASELINE_PUBLIC_CONTRACT_SHA256 and EXPECTED_EXECUTION_RUNNER_SHA256 sentinels are intentional external final-freeze bindings, not additional GIA code defects. Lane A FIX6 code is frozen; runtime remains blocked until those two immutable external pins are bound by final integration/orchestration.

Decision:
GIA_FIX6_STATIC=PASS
GIA_FIX6_CODE_FROZEN=YES
GIA_FIX6_RUNTIME_NOW=NO
NO_GIA_FIX7=YES


## 928 pending-Lane-A-pins audit — dynamic epoch pins and curriculum cardinality blockers

928__AITO_FINAL_E2E_PROOF_V2_PENDING_LANE_A_FIX6_PINS.tar.gz SHA256:
97ed539312354c158f6eb7867cf2f46046af5cb3187bc93ffa7fa59037fdcfb1

Positive:
- prior V2 NULL false-pass is removed;
- explicit HOLD vs ACQUIRE_MORE matrix exists;
- exact official 8-dimension vocabulary is checked;
- fake COMMIT / fake measurement hit black-box submission APIs;
- Phase 3 requires PREPARED plus unchanged accepted/persisted hashes;
- Phase 4 compares real pre/post crash hashes;
- root verifier lstat-checks raw components before resolve;
- executable-source hashes match package records.

Remaining blockers:

1. ADMIN_LANE_A_FIX6_EXPECTED_PINS.txt incorrectly treats dynamic per-epoch artifact hashes as pre-run Admin pins:
BEFORE_MEASUREMENT_SHA256
AFTER_MEASUREMENT_SHA256
PROTECTED_REGRESSION_SHA256
RETENTION_PROOF_SHA256
These do not come from frozen Lane A FIX6 and cannot be known before the autonomous epoch. They must be mechanically hashed by a neutral runner after candidate/evaluation artifacts exist and before admission/continue, then used as an independent dynamic witness for receipt verification.

Static frozen Lane A FIX6 pins now known:
ADMISSION_ENGINE_SHA256=acda382c23dce7713e0e50751d4c041941f2f943d3be56efc66618d60f10f0da
ADMISSION_RUNNER_SHA256=d3f82a2abb3db78f5a3101737938c43727c2fc1b458950f9d15e3fb1cd4acfc0
ACCEPTED_STATE_WRITER_SHA256=bac004283c8be5bd9d960f11329edd4ec752022950ecb3622d453b6c334e368c
EXECUTION_RUNNER_SHA256 remains pending final orchestrator freeze.

2. NONHOLDOUT_SOURCE.tsv has only 3 examples for each structural family (3 BEGIN + 3 owner). TRE learner curriculum requires >=3 compatible TRAIN + >=1 compatible UNSEEN from the same template/anchors. No family currently has 4 compatible examples, so a correct AIto epoch should return ACQUIRE_MORE instead of reaching COMMIT. Add at least 4 unique examples in one compatible family; preferably 4+4 for both independent families.

3. NEUTRAL_ROOT_VERIFY.py prints PASS when invoked with zero witness files because it has no minimum-argument gate. Require at least one explicit witness file or fail closed.

Decision:
928_PENDING_PINS_PACKAGE=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES

Next 928 version should:
- separate STATIC_AUTHORITY_PINS from DYNAMIC_EPOCH_WITNESS;
- neutral-hash parent/candidate/measurement/protected/retention artifacts after run_to_candidate and before admission;
- compare final Lane A receipt against that neutral witness;
- use frozen GIA FIX6 engine/runner/writer pins and later final execution-runner pin;
- expand non-holdout curriculum source to satisfy 3 TRAIN + 1 UNSEEN compatible group;
- fail neutral root verifier when no witness file is supplied.


## 927 TRẺ AIto Epoch V7 static rejection — persistence/evaluator state-model ABI conflation

TRE__AITO_EPOCH_V7.tar.gz SHA256:
d1acce1e9531f3ba13ad7eeab77668cc84346429810050f40551ce300eea4770

Positive V7 repairs confirmed:
- all package SHA256SUMS PASS;
- Python/Bash syntax PASS;
- learner FIX3 exact SHA 661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573;
- exact Lane A FIX6 pointer path/root enforced;
- ACCEPTED_STATE_PATH is forbidden;
- GENERATION_RELATIVE_PATH is required/validated;
- derived STATE.model is regular, non-symlink, SHA-bound under exact ACCEPTED_ROOT;
- Lane A FIX6 engine/runner/writer pins are embedded correctly;
- V6 non-pointer components remain unchanged.

Runtime blockers:

1. Accepted persistence state schema conflation.
Lane A FIX6 bootstrap copies the exact approved 05B parent artifact into:
  $ACCEPTED_ROOT/generations/<sha>/STATE.model
That bootstrap file is SCHEMA=SIGMA_VKM_927_REPLAY_MODEL_V1.
After a COMMIT, Lane A writer copies candidate_state.model byte-for-byte into the accepted generation STATE.model; TRE V7 candidate state is SCHEMA=TRE__PERSISTED_CANDIDATE_STATE_V3.
But V7 parse_accepted_state_model() accepts only:
  SCHEMA=SIGMA_VKM_927_ACCEPTED_STATE_MODEL_V1
which Lane A FIX6 never writes.
Therefore both first-epoch bootstrap and post-COMMIT continuation are currently unreadable by V7.

2. R15 evaluator-state model is incorrectly treated as accepted persistence state.
V7 copies parent STATE.model to TRE__R15_PARENT_ACCEPTED_STATE.model and passes it as SIGMA_06B2_ACCEPTED_STATE_MODEL.
R15 ACCEPTED_RESTORE_EVAL explicitly requires SCHEMA=SIGMA_VKM_927_ACCEPTED_STATE_MODEL_V1.
The accepted persistence STATE.model is not that schema. These are separate abstractions.
V4 correctly used a separate R15 accepted-state evaluation anchor; that separation must be restored without weakening current pointer identity binding.

3. Candidate persisted-state header mismatch.
V7 write_state() writes:
  TRAIN_RECORD_COUNT
  UNSEEN_RECORD_COUNT
  RECORD_COUNT
but TRE__R15_CANDIDATE_MEASUREMENT_ADAPTER_V2 requires:
  PARENT_RECORD_COUNT
  NEW_RECORD_COUNT
  RECORD_COUNT
Thus candidate measurement fails even before admission.

Decision:
TRE_AITO_EPOCH_V7_POINTER_ABI=PASS
TRE_AITO_EPOCH_V7_RUNTIME_READY=NO
RUNTIME_FORBIDDEN=YES

Required V8:
- keep exact Lane A FIX6 pointer/root logic unchanged;
- introduce persistence-state loader that supports the actual two Lane A accepted STATE.model forms:
  (a) bootstrap SIGMA_VKM_927_REPLAY_MODEL_V1, validating its record/hash chain;
  (b) committed TRE__PERSISTED_CANDIDATE_STATE_V3, using the existing strict state parser, extracting TRAIN records as parent training history and validating its PARENT_ACCEPTED_STATE_SHA256 against pointer lineage;
- do not demand SIGMA_VKM_927_ACCEPTED_STATE_MODEL_V1 from accepted persistence storage;
- restore a separate R15 evaluation anchor of schema SIGMA_VKM_927_ACCEPTED_STATE_MODEL_V1, mechanically derived for measurement only, never substituted for accepted-state identity;
- pass TRE_R15_PARENT_PERSISTED_STATE only when current accepted STATE.model is a TRE persisted candidate state; bootstrap legacy replay parent uses no TRE parent persisted state;
- align candidate state headers and adapter exactly, preferably add explicit PARENT_RECORD_COUNT and NEW_RECORD_COUNT while preserving TRAIN_RECORD_COUNT / UNSEEN_RECORD_COUNT for restore checks;
- keep BASELINE_06B2_SHA256, accepted state SHA, and R15 evaluation-model SHA as three distinct identities;
- no learner modification; no holdout pre-open; no admission/commit.



## 928 final E2E V3 static rejection — real Lane A ABI mismatch; GIA FIX6 doctrine defect discovered

928__AITO_FINAL_E2E_PROOF_V3.tar.gz SHA256:
433a58283d8cb871babddbf9db04751edafa16f5c65478d4eceab544f6e98966

Positive V3 repairs confirmed:
- dynamic epoch hashes moved out of pre-run Admin pins;
- neutral dynamic witness hashes parent/candidate/before/after/protected/retention before admission;
- primary curriculum now has 4 compatible BEGIN and 4 compatible OWNER examples;
- root verifier fails closed on zero witness files;
- exact 8-dimension vocabulary preserved;
- pre/post crash hash comparison preserved;
- executable source hashes all verify.

Blocking 928/Lane-A ABI mismatches:

1. 928 uses INTEGRITY_STATUS and requires ADMISSION_DECISION=HOLD for integrity failures.
Real Lane A FIX6 ABI uses:
  STATUS=HOLD
  ADMISSION_DECISION=
for integrity/ABI failure.
Ordinary outcomes are STATUS=PASS + COMMIT|REJECT|ACQUIRE_MORE.
928 must align to real Lane A status semantics.

2. PHASE_1B requires two fields that real Lane A admission receipt does not emit:
  DYNAMIC_EPOCH_WITNESS_SHA256
  ACCEPTED_STATE_WRITER_SHA256
The real receipt does emit individual parent/candidate/before/after/protected/retention hashes plus engine/runner/execution-runner and measurement pins.
Therefore final proof should compare those individual receipt hashes against the neutral dynamic witness, while keeping the neutral witness seal as examiner evidence only. Writer identity is verified independently by static authority witness, not invented as a receipt field.

3. ADMIN_STATIC_AUTHORITY_PINS.txt hard-codes pre-final-bind hashes:
  ADMISSION_RUNNER_SHA256=d3f82...
  ACCEPTED_STATE_WRITER_SHA256=bac004...
But GIA FIX6 explicitly requires final integration to bind EXECUTION_RUNNER_SHA256 into runner+writer, then recompute runner SHA, repin it in writer, and recompute final writer SHA. Thus these two hashes are not final production pins yet. 928 must leave ADMISSION_RUNNER_SHA256, ACCEPTED_STATE_WRITER_SHA256, and EXECUTION_RUNNER_SHA256 pending final orchestrator freeze. ADMISSION_ENGINE_SHA256 remains stable.

4. DUPLICATE_SOURCE.tsv uses the same EVIDENCE_ID DUP1 with three different payloads. That is conflicting identity/provenance, not harmless duplicate-only insufficiency, and may correctly trigger HOLD. To test ACQUIRE_MORE for repeated evidence, repeat the exact same evidence row/payload so dedup leaves insufficient unique support.

5. Remove stale obsolete files from the V3 package:
  ADMIN_LANE_A_FIX6_EXPECTED_PINS.txt
  PHASE_1_AUTONOMOUS_CYCLE.sigma
They retain superseded pre-V3 static-pin semantics and are not in RUN_PROTOCOL/EXECUTABLE_SOURCE_SHA256. Keeping them creates operator ambiguity.

New real Lane A defect discovered during cross-audit:
SIGMA_VKM_927_ADMISSION_V1_FIX4.sigma currently classifies these integrity failures as REJECT:
- PROVENANCE_INVALID
- CANDIDATE_DETERMINISM_FAILED
- DETERMINISTIC_EVALUATION_FAILED
- GOLD_LEAK_DETECTED
- HOST_COGNITION_DETECTED

Locked 927 doctrine requires these to be STATUS=HOLD because invalid provenance, nondeterminism, gold leakage, and host cognition are system-integrity failures.
Therefore GIA FIX6 code freeze must be reopened narrowly for a FIX7 admission-policy repair. No writer/root/pointer redesign.

Decision:
928_AITO_FINAL_E2E_V3=REPAIR_REQUIRED
928_RUNTIME_FORBIDDEN=YES
GIA_FIX6_ROOT_POINTER_ARCHITECTURE=PASS
GIA_FIX6_ADMISSION_POLICY=REPAIR_REQUIRED


## 927 Lane A FIX7 static accepted — admission doctrine repaired

GIA__ADMISSION_WRITER_FIX7.zip SHA256:
9345233306632fee33a66c0fa7e23bfd1b8a0671a61829308dbc8adb3f5fce84

Static audit PASS:
- all manifest artifact hashes verify;
- Python syntax PASS;
- FIX6 root/pointer/accepted-store architecture preserved;
- parent-state contract preserved;
- no recursive discovery;
- ONE_SIGMA invariants preserved.

Admission policy repair verified:
- PROVENANCE_INVALID => STATUS=HOLD, ADMISSION_DECISION=""
- CANDIDATE_DETERMINISM_FAILED => HOLD
- DETERMINISTIC_EVALUATION_FAILED => HOLD
- GOLD_LEAK_DETECTED => HOLD
- HOST_COGNITION_DETECTED => HOLD
- measured gain <=0 => REJECT
- goal-dimension gain <=0 => REJECT
- protected regression FAIL => REJECT
- unacceptable regression => REJECT
- fresh unseen FAIL => REJECT
- negative control FAIL => REJECT
- restart retention FAIL => REJECT
- INSUFFICIENT evidence statuses => ACQUIRE_MORE

Frozen FIX7 admission engine SHA256:
7645bba2b4bb1e54869b579ff28992287d4680bb0c8f296fa2cfd4628dbc010f

Current pre-final-bind runner/writer hashes:
ADMISSION_NATIVE_RUNNER_SHA256=ccb4010daf3f9eb6bcc91f3f5a629753806bdb2d2d9f2ce7781cffdeeb17e6ee
ACCEPTED_STATE_WRITER_SHA256=531aa7ecabeda5fe4b6cc5146024fa78e8b99e0edd0d6bce2b87720538dfe5b7

These runner/writer hashes are NOT final production pins yet because final integration must bind:
- EXPECTED_EXECUTION_RUNNER_SHA256
- EXPECTED_BASELINE_PUBLIC_CONTRACT_SHA256
Then recompute final runner hash, repin it in writer, and recompute final writer hash.

Decision:
GIA_FIX7_ADMISSION_ENGINE_STATIC=PASS
GIA_FIX7_ADMISSION_ENGINE_FROZEN=YES
GIA_FIX7_RUNNER_WRITER_LOGIC_FROZEN=YES
FINAL_PRODUCTION_RUNNER_WRITER_HASHES=PENDING_ORCHESTRATOR_BIND
RUNTIME_FORBIDDEN_UNTIL_FINAL_BIND=YES

DNA15 note:
Lane A remains admission + accepted-state writer only. DNA15 self-upgrade / weight evolution / generation continuation belongs in final autonomous orchestrator after COMMIT and must not be silently folded into Lane A.


## 927 TRẺ AIto Epoch V8 static rejection — real 05B replay ABI mismatch and stale Lane A pins

TRE__AITO_EPOCH_V8.tar.gz SHA256:
08e2e0da5096e1e8dab425773313277a1d72fa1f0689a390facc8d9cf9f3edb9

Static positives:
- internal SHA256SUMS PASS;
- Python/Bash syntax PASS;
- learner FIX3 exact SHA preserved;
- Lane A accepted pointer/root confinement remains correct;
- accepted persistence loader now distinguishes bootstrap replay vs TRE persisted V3;
- R15 evaluation model is separated from accepted persistence state;
- candidate state header adds PARENT_RECORD_COUNT / NEW_RECORD_COUNT and role counts;
- V7 non-target learner/curriculum/acquisition/public-bridge components are byte-identical.

Blocking defects:

1. parse_bootstrap_replay_model() implements the wrong serialization for the real accepted 05B artifact.
V8 requires:
  MODEL_BODY_SHA256
  ORDER
  EVIDENCE_TEXT_B64
  PREV_RECORD_SHA256/PREVIOUS_RECORD_SHA256/PREV_SHA256
  RECORD_SHA256/RECORD_HASH_SHA256
  zero-hash chain origin
  CHAIN_* tail field
But the accepted SIGMA_VKM_927_REPLAY_MODEL_V1 transport used by 06B2 parses exactly:
  SCHEMA=SIGMA_VKM_927_REPLAY_MODEL_V1
  MODEL_ID=SIGMA_VKM_927
  REVISION
  RECORD_COUNT
  GENESIS_HASH=sha256(SCHEMA+"\n"+MODEL_ID+"\n")
  LAST_RECORD_HASH
  RECORD_BEGIN
  SEQ
  EVIDENCE_ID
  EVIDENCE_TEXT
  EVIDENCE_STATUS
  PREVIOUS_RECORD_HASH
  RECORD_HASH=sha256(seq+"\n"+id+"\n"+text+"\n"+status+"\n"+previous+"\n")
  RECORD_END
with no MODEL_BODY_SHA256 and no base64 text.
GIA FIX7 bootstraps by copying that exact ONE_SIGMA 05B file byte-for-byte to generations/<sha>/STATE.model.
Therefore V8 first bootstrap cannot parse the real accepted state and will return bootstrap-required instead of learning.

2. V8 still hard-codes stale Lane A FIX6 authority hashes:
  engine acda382c...
  runner d3f82a2...
  writer bac00428...
After the proven admission-policy repair, frozen FIX7 engine is:
  ADMISSION_ENGINE_SHA256=7645bba2b4bb1e54869b579ff28992287d4680bb0c8f296fa2cfd4628dbc010f
Final runner/writer production hashes are intentionally pending final orchestrator binding of execution-runner + baseline-public-contract pins. TRE must not assert the old FIX6 runner/writer hashes as current authority.

Required V9:
- replace bootstrap replay parser with the exact accepted 05B/06B2 SIGMA_VKM_927_REPLAY_MODEL_V1 byte contract above;
- validate MODEL_ID, REVISION==RECORD_COUNT, GENESIS_HASH, ordered SEQ, ACCEPTED status, previous-record chain, deterministic RECORD_HASH and LAST_RECORD_HASH;
- no invented MODEL_BODY_SHA256/base64/order fields;
- preserve TRE persisted V3 loader and R15 separation unchanged;
- update frozen Lane A engine pin to FIX7 SHA;
- do not pin final runner/writer hashes inside TRE; mark them external final-orchestrator authority or omit them from candidate producer evidence;
- use generic accepted-pointer ABI alignment wording rather than claiming obsolete FIX6 authority;
- no learner/curriculum/evaluator redesign.

Decision:
TRE_AITO_EPOCH_V8=REPAIR_REQUIRED
RUNTIME_FORBIDDEN=YES


## Top-level autonomous doctrine — no terminal state + DNA15 generation evolution

New hard requirements, effective immediately at architecture/contract level:

AUTONOMOUS_UNATTENDED_OPERATION=YES
HUMAN_REQUIRED_FOR_CONTINUATION=NO
TERMINAL_LEARNING_STATE=NONE
ONE_SIGMA=YES
SAME_SIGMA_IDENTITY=YES
SECOND_SIGMA_CREATED=NO
DNA15_REQUIRED_IN_FINAL_AUTONOMOUS_LOOP=YES
WEIGHT_EVOLUTION=YES
GENERATION_EVOLUTION=YES

Important layering decision:
- Do NOT inject DNA15 execution into the learner, evaluator, admission engine, or accepted-state writer.
- Lane B/TRẺ produces and evaluates candidate state only.
- Lane A/GIÀ decides admission and atomically persists the accepted generation only.
- DNA15 self-upgrade is owned by the final autonomous orchestrator after a successful COMMIT.
- The supervisor owns crash/process restart and must relaunch the orchestrator automatically.
- 928 must prove the full non-terminal recovery/self-upgrade loop black-box.

Required final lifecycle:
GAP
-> GOAL
-> ACQUIRE
-> CURRICULUM
-> TRAIN SAME SIGMA
-> CANDIDATE
-> FRESH EVALUATION
-> ADMISSION
-> COMMIT accepted generation
-> DNA15 SELF-UPGRADE / weight-generation evolution
-> durable generation checkpoint
-> fresh restart
-> retention + protected regression
-> next official gap
-> repeat indefinitely

No terminal semantics:
- HOLD is diagnostic/integrity state inside recovery loop, not process exit waiting for human.
- REJECT preserves accepted state then automatically changes/rebuilds curriculum/evidence and starts another epoch.
- ACQUIRE_MORE automatically returns to acquisition.
- COMMIT automatically continues into DNA15/generation advancement and next gap.
- crash/power/process death recovers from durable journal and resumes.
- bounded retries must never become a silent terminal exit; exhausted local recovery transitions to a durable degraded/quarantine/acquisition mode and keeps the supervisor/orchestrator alive.

Cross-lane contract requirements effective now:
TRẺ:
- must produce deterministic candidate + resume-safe artifacts and never assume COMMIT is terminal;
- must expose enough state for orchestrator to resume/retry/reacquire without human;
- no DNA15 execution inside TRE epoch runner.

GIÀ:
- COMMIT receipt must be durable input to orchestrator; writer must not treat COMMIT as overall workflow completion;
- HOLD/REJECT/ACQUIRE_MORE must be machine-actionable statuses;
- no DNA15 execution inside admission/writer.

928:
- final proof must assert no terminal workflow state;
- test automatic transitions for HOLD recovery, REJECT re-epoch, ACQUIRE_MORE acquisition, COMMIT->DNA15->new generation->restart->retention->next gap;
- test supervisor restart after crash with no human action;
- verify DNA15 changes same-Sigma weight/generation identity without creating a second Sigma.

Final orchestrator must be designed/frozen before runtime binding of Lane A runner/writer hashes, because EXECUTION_RUNNER_SHA256 is one of the final authority pins and must cover the autonomous DNA15/recovery control plane.


## ORCH bootstrap bundle V1 created

Bundle:
ORCH__INPUTS_V1.zip

SHA256:
5e88f25ad18ce4232bd95f91c0cddefca69bb7835cc6a20dae4bcca72fef33be

Contains contract-only inputs:
- README_ORCH_INPUTS_V1.txt
- ORCH__TASK_V1.txt
- ORCH__INVARIANTS_V1.txt
- ORCH__ABI_V1.txt
- ORCH__PINS_V1.txt
- ORCH__RECOVERY_STATE_MACHINE_V1.txt
- ORCH__DNA15_CONTRACT_V1.txt
- ORCH__SUPERVISOR_CONTRACT_V1.txt
- ORCH__UPSTREAM_STATUS_V1.txt
- ORCH__NON_GOALS_V1.txt
- ORCH__HANDOFF_MESSAGE_V1.txt
- SHA256SUMS.txt

All internal SHA256SUMS verified PASS.

No source/frozen/gold/history dump included.

Hard architecture captured:
AUTONOMOUS_UNATTENDED_OPERATION=YES
HUMAN_REQUIRED_FOR_CONTINUATION=NO
TERMINAL_LEARNING_STATE=NONE
DNA15_REQUIRED_IN_FINAL_AUTONOMOUS_LOOP=YES
WEIGHT_EVOLUTION=YES
GENERATION_EVOLUTION=YES
ONE_SIGMA=YES
SAME_SIGMA_IDENTITY=YES
SECOND_SIGMA_CREATED=NO

ORCH remains a dedicated new implementation lane.
Admin backup remains neutral integrator and will later audit/bind ORCH.


## 927 TRẺ AIto Epoch V9 — static accepted, freeze candidate producer

TRE__AITO_EPOCH_V9.tar.gz SHA256:
b3a847cd9ef9b14fdface1f261af063845f602640591953d070736f7d4701416

Static audit PASS:
- package SHA256SUMS PASS;
- Python/Bash syntax PASS;
- learner FIX3 exact SHA 661d3047c18f0958cd61095f3e17b28f79e62e900ee57d2ac8a0b4b2e5709573;
- exact accepted 05B replay bootstrap ABI now matches the official 06B2 transport:
  SCHEMA=SIGMA_VKM_927_REPLAY_MODEL_V1
  MODEL_ID=SIGMA_VKM_927
  REVISION==RECORD_COUNT
  GENESIS_HASH=sha256(schema+"\n"+model_id+"\n")
  ordered SEQ
  EVIDENCE_TEXT raw
  EVIDENCE_STATUS=ACCEPTED
  PREVIOUS_RECORD_HASH chain
  RECORD_HASH deterministic
  LAST_RECORD_HASH final;
- no invented MODEL_BODY_SHA256 / ORDER / EVIDENCE_TEXT_B64 in bootstrap replay parser;
- persistence state vs R15 evaluation state remain separated;
- candidate V3 count ABI aligned;
- Lane A admission engine pin updated to FIX7:
  7645bba2b4bb1e54869b579ff28992287d4680bb0c8f296fa2cfd4628dbc010f;
- old FIX6 runner/writer production pins removed; final runner/writer/execution-runner are external orchestrator bindings;
- ONE_SIGMA pointer/root confinement preserved;
- no admission/commit/promotion/DNA15 in TRE, by design.

Frozen component examples:
TRE__AITO_EPOCH_INTEGRATOR_V9.py SHA256=47298cdc26c5910725ea6415d2f87782520b56f2493fb1863ae0c67e946b3aee
TRE__R15_CANDIDATE_MEASUREMENT_ADAPTER_V3.sh SHA256=966aaca93377e0f0de9b13985be139f26ae7055367c0fdf8e9472dee35d0490e

Decision:
TRE_AITO_EPOCH_V9_STATIC=PASS
TRE_V9_CODE_FROZEN=YES
TRE_RUNTIME_NOW=NO
NEXT_OWNER=ORCH_FINAL_INTEGRATION


## 928 final E2E V3 revised — pre-ORCH core mostly repaired, final proof not frozen

Uploaded revised archive SHA256:
fc13fcbabd836dae18db436fd5a5c8fcc49a58a6ad88667b0c7b74babfc05c7e

Positive repairs:
- real Lane A STATUS=HOLD + empty decision semantics;
- duplicate-only dataset repeats exact same record/payload;
- conflicting same-ID/different-payload separated into integrity-HOLD dataset;
- dynamic epoch witness separated from static authority pins;
- 4 TRAIN/UNSEEN-compatible evidence coverage;
- zero-input neutral-root verification fails;
- obsolete superseded files removed;
- exact eight-dimension vocabulary;
- real pre/post crash state-hash witnesses retained;
- executable source hashes and Python syntax PASS.

Remaining local harness defect independent of ORCH:
BLACK_BOX_ABI declares NULL_RESULT_ALLOWED=NO, but several return values are never checked. Examples:
PHASE_0: sf, sr, cf, cr, ir, dr, ur
PHASE_1A: r = aito_bb_run_to_candidate(c)
PHASE_3: r = aito_bb_run_to_candidate(c)
A side-effecting API could return NULL yet later state checks still pass, violating the declared no-NULL proof rule. Require every public black-box call result to be explicit/non-NULL unless the ABI explicitly defines a void call.

New top-level final-proof requirement now also supersedes this package:
928 final proof must wait for frozen ORCH ABI/pins and then prove:
COMMIT -> DNA15 -> same-Sigma weight/generation evolution -> durable checkpoint -> restart -> retention -> next gap;
plus automatic non-terminal continuation for HOLD / REJECT / ACQUIRE_MORE / crash.

Decision:
928_V3_REVISED_PRE_ORCH_CORE=REPAIR_NEEDED
928_FINAL_PROOF_READY=NO
RUNTIME_FORBIDDEN=YES
DO_NOT_GUESS_ORCH_ABI=YES
