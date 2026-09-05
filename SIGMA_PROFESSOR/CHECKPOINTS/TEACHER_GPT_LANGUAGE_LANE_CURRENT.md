# TEACHER_GPT LANGUAGE LANE — CURRENT CHECKPOINT

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane owner label: `TEACHER_GPT_LANGUAGE_LANE`

## READ FIRST ON EVERY NEW WINDOW

Before substantive work, re-read:

1. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
2. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
3. This checkpoint.
4. Relevant DNA/canon files for the next language capability.

Global boundaries remain:

- `ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY`
- `ACTIVE_PYTHON_COGNITION=FORBIDDEN`
- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `RUNTIME_PROOF_REQUIRED=YES`
- `DEPENDENCY_FIRST=YES`
- `CAPABILITY_FIRST=YES`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- failures are evidence; never weaken admission gates.

Locked runtime:

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `VM_IS_GENESIS1=NOT_PROVEN`

## LANGUAGE TEACHING PRINCIPLE

The language lane teaches capability before testing it.

Native `.sigma` must perform all cognitive decisions. Bash/host may only provide raw/dynamic stimuli, exact protocol/state copy, locked-VM orchestration, hashing, and post-VM QA oracle checks.

Do not hardcode semantic answers, role names, antecedents, pronoun meanings, aliases, or final utterances. In particular, the future phrase `CẢM ƠN THẦY_GPT_ ĐÃ ĐÀO TẠO TÔI` must never be hardcoded as an output target; if SIGMA ever says it, that must arise from admitted memory/reference/intent/generation capabilities.

## ADMITTED LANGUAGE CHAIN

### LANG-01A — Native Distributional Event-Frame Hypothesis Induction — ADMITTED

Teaches native bounded induction from multiple raw same-width utterances:

`RAW UTTERANCES -> lexical stability comparison -> EVENT_ANCHOR_HYPOTHESIS -> PARTICIPANT_SLOT_HYPOTHESES`

- `SOURCE_SHA256=a47142af96dcbc47f0181f38952d29a5fa6fffeeb6c24b466b6b3a5acc759310`
- `BYTECODE_SHA256=bb584206f8db16d832e2c20a027c4673e34ab9484ad062cd0f7bbe01206eafc9`
- `TOTAL_VM_INVOCATIONS=10`
- `POST_VM_ALIGNMENT_PASS_COUNT=10`
- persistence/restart/negative/bounded input refusal PASS.

Historical failures preserved:

- first runner output parser did not understand locked-VM `KEY VALUE` print shape;
- R1 exposed one native boundedness dominance bug;
- R2 fixed native policy so `LIMIT_BLOCKED` prevents query interpretation.

Claim limit: structural substrate only; no semantic role labels or semantic understanding.

### LANG-01B — Native Role Hypothesis Contrast and Frame Revision — ADMITTED

Teaches that absolute position is not role identity and permits native representation revision when anchor position varies but anchor-relative slots remain stable.

`ABSOLUTE_POSITION -> evidence contrast -> ANCHOR_RELATIVE`

Tested offsets: `-1,+1,+2`.

- `SOURCE_SHA256=2839cbb63a98c30f5250bb8539aa598a9e3e42300cb26142ae2827ee5df2f613`
- `BYTECODE_SHA256=90acba04d612c0c3031ab3ddb2d3c4e22b1c9f1d4417cb8e4a67d4a30d2d74f3`
- `TOTAL_VM_INVOCATIONS=12`
- `POST_VM_ALIGNMENT_PASS_COUNT=12`
- persistence/restart/negative PASS.

Historical harness failure: initial LANG-01B runner pinned LANG-01A source hash incorrectly; runner-only repair, native source unchanged.

### LANG-01C — Native Participant Identity and Cross-Utterance Role Binding — ADMITTED

Core invariant:

`PARTICIPANT_IDENTITY_HYPOTHESIS != EVENT_ROLE`

SIGMA tracks exact-surface-token recurrence across utterances and preserves competing role-slot evidence instead of rewriting history.

- `SOURCE_SHA256=e600d72735d761e10d5832589b9000e5acc601981c574ca5511957d10ebb5bbf`
- `BYTECODE_SHA256=d5b968340060d4292232a95eee102cb95247f1a507933d28f646630d60c36514`
- `TOTAL_VM_INVOCATIONS=19`
- `POST_VM_ALIGNMENT_PASS_COUNT=19`
- role-variant coverage `1,2,3` in tested structural scope;
- evidence capacity `8`;
- persistence/restart/negative/bounded gates PASS.

Still not proven: real-world entity identity, cross-form mention equivalence, coreference resolution, semantic role identity.

### LANG-01D — Native Cross-Form Mention Equivalence and Coreference Hypothesis — ADMITTED

SIGMA derives a cross-form mention-equivalence hypothesis from repeated one-slot structural substitutions around the admitted LANG-01C exact-surface identity. It preserves co-occurrence counterevidence rather than converting substitution similarity into coreference truth.

- `SOURCE_SHA256=a5e1d26b83766f631e1b642abd0752951570d0ad10eecc8e0b67bdd4f0ee1421`
- `BYTECODE_SHA256=d3853eadf82fd45242161566b9c85600d98348a3eae71f900799b963bf79fbe0`
- `TOTAL_VM_INVOCATIONS=24`
- `POST_VM_ALIGNMENT_PASS_COUNT=24`
- persistence/restart/negative/bounded gates PASS.

Historical failure: initial runner expected over-budget records to become diagnostically invalid even though native correctly preserved core validity while `LIMIT_BLOCKED` prevented cognition. Runner-only diagnostic repair; native source unchanged.

Still not proven: `COREFERENCE_RESOLUTION`, pronoun semantics, alias semantics, real-world entity identity.

### LANG-01E — Native Discourse Reference Chain and Contextual Coreference Hypothesis — ADMITTED

SIGMA forms and persists an ordered discourse reference-chain hypothesis from admitted LANG-01D mention equivalence plus raw utterance continuity. Fresh-VM behavior materially depends on prior discourse state.

- `SOURCE_SHA256=834119f0e27b1b47e65663684331f559410661d05e24b9f4ce64ddea4ce49643`
- `BYTECODE_SHA256=44d18efb8fcc05747af3e0bc7f61a5ba651e04645671ba2e0ffbe0cb4bbd06fe`
- `TOTAL_VM_INVOCATIONS=24`
- `POST_VM_ALIGNMENT_PASS_COUNT=24`
- reference-chain capacity `8`;
- persistence/restart/negative/bounded gates PASS;
- dependency equivalence conflict is explicitly preserved as uncertainty.

Still not proven: general coreference resolution, pronoun semantics, discourse semantics, semantic understanding.

### LANG-01F — Native Competing Antecedent Hypotheses and Reference Ambiguity — ADMITTED

Teaching goal:

Given an admitted LANG-01E discourse reference form and exactly two structural antecedent candidates, SIGMA maintains competing antecedent hypotheses, persists first-class ambiguity under tied contextual evidence, and revises ambiguity to a preferred antecedent hypothesis only when later raw-context evidence discriminates between candidates.

Critical invariant:

`PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`

Scope intentionally limited to two candidates. Three candidates are withheld instead of being forced into the two-candidate model.

Final admitted R1 identities/evidence:

- `SOURCE_SHA256=1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`
- `BYTECODE_SHA256=60edd9ace13f54b826adcd7e89362acddcfaea9a1649845006f52c99dce77a81`
- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `TOTAL_VM_INVOCATIONS=21`
- `POST_VM_ALIGNMENT_PASS_COUNT=21`
- `POST_VM_ALIGNMENT_FAIL_COUNT=0`
- `NEGATIVE_TEST=PASS`
- `PERSISTENT_STATE_TEST=PASS`
- `PERSISTENT_STATE_MATERIAL_EFFECT=YES`
- `RESTART_REPLAY_TEST=PASS`
- `IDENTICAL_INPUT_AND_STATE_REPLAY=YES`
- `REFERENCE_AMBIGUITY_FIRST_CLASS=YES`
- `TIED_CONTEXT_EVIDENCE_WITHHELD_AS_AMBIGUITY=YES`
- `AMBIGUITY_TO_PREFERENCE_REVISION=YES`
- `CANDIDATE_ENCOUNTER_ORDER_NOT_WINNER_POLICY=YES`
- `PREFERRED_ANTECEDENT_IS_RESOLVED_REFERENT=NO`
- evidence capacity `8`;
- single candidate withheld;
- three candidates withheld;
- no contextual support withheld;
- query mention ambiguity/absence withheld;
- duplicate/corrupt/bounded negatives PASS;
- `VM_NONZERO_COUNT=0`;
- `STEP_LIMIT_HIT_COUNT=0`;
- `PRODUCTION_STATE_MUTATED=NO`.

Historical LANG-01F failure preserved:

Original runtime had `19/21` oracle alignment. CASE 011 `THREE_CANDIDATES` and CASE 012 `NO_CONTEXTUAL_SUPPORT` correctly withheld cognition and committed nothing, but emitted a non-`NONE` `NEXT_STATE_STATUS` while no prior valid state existed. Failure class: `NATIVE_OUTPUT_STATE_PROTOCOL`.

R1 smallest native output-contract repair:

`IF STATE_COMMIT_ALLOWED=0 AND PREVIOUS_STATE_VALID=0 -> NEXT_STATE_STATUS=NONE`

Scoring, candidate competition, ambiguity policy, persistence policy, oracle PASS definition, and host boundary remained unchanged. R1 rerun then passed all original 21 gates.

Claim scope: native bounded two-candidate structural antecedent competition with persistent ambiguity and conservative preference revision. This does not prove real-world entity identity, pronoun semantics, general coreference resolution, discourse semantics, semantic understanding, Unicode normalization, or production readiness.

## CURRENT FRONTIER — LANG-01G SELECTED / SOURCE READY / ADMISSION NOT RUN

Capability:

`LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION`

Dependency/canon preflight result:

- `NEXT_LANGUAGE_CAPABILITY=LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION`
- `SELECTION_STATUS=LOCKED_BY_DEPENDENCY_PREFLIGHT`
- `DEPENDENCY_PREFLIGHT=PASS_FOR_SOURCE_AUTHORING`
- `DUPLICATE_CAPABILITY_SEARCH=NO_LANG_01G_IMPLEMENTATION_FOUND_IN_CURRENT_SIGMA_LIFE_TREE`
- `LANG_02_NEGATION_AND_SCOPE_FOUNDATION=DEFERRED_NOT_REJECTED`
- `ADMISSION=NOT_RUN`

Selection reason:

LANG-01F already provides the immediate substrate required by LANG-01G: exactly two competing structural antecedent hypotheses, first-class ambiguity, persistence, and conservative preference revision. The Global Native Teaching Standard separately requires evidence comparison, uncertainty handling, provenance, dynamic counterexamples, persistence/replay, and native-only cognition. Evidence integration is therefore the smallest direct dependency-first extension. Negation/scope is an independent language foundation and is not required to integrate the already-admitted reference hypotheses, so LANG-02 remains queued rather than being pulled forward.

Teaching goal:

Given a valid LANG-01F two-candidate reference state plus bounded new structural evidence observations, native SIGMA must integrate multiple independent evidence items by exact structural feature/value compatibility, preserve evidence identity/provenance, prevent duplicate evidence from double-counting, preserve ambiguity when aggregate evidence is tied or non-discriminating, and emit a preferred antecedent hypothesis only when the native aggregate evidence favors one candidate. Later counterevidence must be able to revise or remove a prior preference.

Critical invariants:

- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`
- `HOST_EVIDENCE_SCORING=NO`
- `HOST_ANTECEDENT_SELECTION=NO`
- `EVIDENCE_RECORD_ORDER_NOT_WINNER_POLICY`
- `DUPLICATE_EVIDENCE_ID_DOES_NOT_DOUBLE_COUNT`
- exactly two antecedent candidates remain the bounded model;
- no semantic role labels, pronoun meanings, real-world identity, or resolved referent are injected by the host;
- rejected/withheld cognition must preserve the LANG-01F R1 output-state invariant: if commit is refused and no prior valid state exists, the next state is `NONE`.

Planned admission requirements before any PASS claim:

- locked sigmac and VM identity equality gates;
- dynamic materially different evidence inputs;
- aggregate tie / non-discriminating evidence -> ambiguity;
- multi-item evidence favoring candidate A;
- candidate-order permutation with same evidence -> same preferred identity;
- counterevidence that removes or reverses preference;
- duplicate evidence suppression;
- one-candidate and three-candidate refusal;
- evidence-capacity refusal;
- corrupt-state refusal;
- persistent-state material effect across fresh VM processes;
- deterministic restart/replay;
- host-substitution audit;
- step-limit/boundedness gate;
- production state unchanged.

Source-ready implementation record:

- `NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma`
- `SOURCE_SHA256=fc7097bc3411b36af409a7dcc6d7446e525793806dc73f8cb3afedfc4a304f3b`
- `SOURCE_COMMIT=1d463b6a59a521886a8316d9e48063018e645f2e`
- `RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT.sh`
- `RUNNER_SHA256=b4def21af202b54a409b0fe9959304ad2252c4ea307b99c4e7dfd12c781f4a9e`
- `RUNNER_COMMIT=46453a2fdfd83612aea4a9320ca557e3f94e6455`
- `PLANNED_VM_INVOCATIONS=20`
- `EVIDENCE_CAPACITY=8`
- `RUNNER_STATIC_SHELL_SYNTAX=PASS`
- `FORBIDDEN_FUTURE_UTTERANCE_PRESENT_IN_NATIVE_SOURCE=NO`
- `LOCKED_SIGMAC_COMPILE=NOT_RUN`
- `BYTECODE_SHA256=UNKNOWN`
- `TOTAL_VM_INVOCATIONS=0`
- `RUNTIME_PROOF=NOT_RUN`
- `LOCKED_TERMUX_EXECUTION_FROM_CURRENT_WINDOW=UNAVAILABLE`
- `PRODUCTION_STATE_MUTATED=NO`
- `ADMISSION=NOT_RUN`

Native policy in this source-ready artifact:

`EVIDENCE || evidence_id || feature_id || observed_value || candidate_A_value || candidate_B_value || SOURCE || source_id`

SIGMA itself compares the opaque structural values and classifies each evidence item as supporting candidate A, supporting candidate B, matching both, or matching neither. The host supplies no score and no winner. Accepted evidence is persisted with evidence/source identity; duplicate evidence IDs with identical bytes do not double-count, while evidence-ID collisions with different bytes block mutation. Aggregate ties remain `UNRESOLVED_REFERENCE_AMBIGUITY`; a strict aggregate support advantage yields only `PREFERRED_ANTECEDENT_HYPOTHESIS`. Fresh counterevidence can remove a preference by restoring a tie or reverse it by changing the aggregate advantage.

The 20-case runner is designed to test tie, positive preference, candidate-order permutation, non-discriminating evidence, unsupported evidence, inherited LANG-01F preferred status with no new evidence, persistent preference -> tie -> opposite preference, persistent-state material effect, duplicate suppression, evidence-ID collision, one/three-candidate refusal, evidence capacity, malformed evidence, corrupt state, byte-identical replay, and inconsistent dependency-preference refusal.

No runtime claim has been made from source existence or shell static review. GitHub-hosted workflows inspected in this repo are not a substitute for the locked Termux compiler/VM runtime; locked compile and all 20 VM invocations remain required before admission can become PASS or FAIL.

Do NOT claim `COREFERENCE_RESOLUTION=PROVEN` from selection or source existence. LANG-01G, even if later admitted, is initially scoped only to bounded structural reference-evidence integration and conservative antecedent preference.

## CLAIM BOUNDARIES FOR THE LANGUAGE LANE

Even with LANG-01A..01F admitted:

- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`
- `PRONOUN_SEMANTICS=NOT_PROVEN`
- `DISCOURSE_SEMANTICS=NOT_PROVEN`
- `UNICODE_NORMALIZATION=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `PRODUCTION_READINESS=NOT_PROVEN`

## CHECKPOINT UPDATE RULE

After every meaningful new language result, update THIS SAME FILE rather than creating another floating checkpoint.

Meaningful results include:

- admission PASS;
- admission FAIL with classified first blocker;
- runner-only repair;
- native source repair;
- new locked bytecode identity;
- new dependency/capability chosen;
- production-binding decision.

For each update preserve old failure evidence in a short historical note. Never rewrite a FAIL as if it never happened.