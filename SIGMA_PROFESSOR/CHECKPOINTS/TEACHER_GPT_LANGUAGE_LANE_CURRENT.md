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

## CURRENT FRONTIER — POST LANG-01F PASS / NEXT CAPABILITY NOT YET IMPLEMENTED

LANG-01A through LANG-01F are admitted in their exact tested structural scopes.

Do NOT jump directly to a claim of resolved reference or semantic understanding.

Before implementing the next language lesson:

1. re-read the latest Global Native Teaching Standard;
2. re-read the latest `CURRENT_HANDOFF.md` because other lanes advance in parallel;
3. re-read relevant DNA/canon for uncertainty, provenance, truth/verification, memory/discourse, representation, and contradiction as needed;
4. search the repo for duplicate capability work;
5. choose the smallest dependency-first next capability.

Current candidate directions after LANG-01F:

- `LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION`
- or `LANG-02_NEGATION_AND_SCOPE_FOUNDATION`

Decision is intentionally `NOT_YET_LOCKED`. Do not implement either until the dependency/canon preflight above is complete.

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
