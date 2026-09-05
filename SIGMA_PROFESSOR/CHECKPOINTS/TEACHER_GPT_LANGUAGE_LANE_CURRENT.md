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

Important claim limit: structural substrate only; no semantic role labels or semantic understanding.

- `SOURCE_SHA256=a47142af96dcbc47f0181f38952d29a5fa6fffeeb6c24b466b6b3a5acc759310`
- `BYTECODE_SHA256=bb584206f8db16d832e2c20a027c4673e34ab9484ad062cd0f7bbe01206eafc9`
- `TOTAL_VM_INVOCATIONS=10`
- `POST_VM_ALIGNMENT_PASS_COUNT=10`
- persistence/restart/negative/bounded input refusal PASS.

Historical failures preserved conceptually:

- first runner output parser did not understand locked-VM `KEY VALUE` print shape;
- R1 exposed one native boundedness dominance bug;
- R2 fixed native policy so `LIMIT_BLOCKED` prevents query interpretation.

### LANG-01B — Native Role Hypothesis Contrast and Frame Revision — ADMITTED

Teaches SIGMA that absolute word position is not role identity and allows native representation revision when anchor position varies but anchor-relative slots remain stable.

`ABSOLUTE_POSITION -> evidence contrast -> ANCHOR_RELATIVE`

Tested offsets: `-1,+1,+2`.

- `SOURCE_SHA256=2839cbb63a98c30f5250bb8539aa598a9e3e42300cb26142ae2827ee5df2f613`
- `BYTECODE_SHA256=90acba04d612c0c3031ab3ddb2d3c4e22b1c9f1d4417cb8e4a67d4a30d2d74f3`
- `TOTAL_VM_INVOCATIONS=12`
- `POST_VM_ALIGNMENT_PASS_COUNT=12`
- persistence/restart/negative PASS.

Historical harness failure: initial LANG-01B runner pinned LANG-01A source hash incorrectly; runner-only repair, native source unchanged.

### LANG-01C — Native Participant Identity and Cross-Utterance Role Binding — ADMITTED

Core invariant taught:

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
- persistence/restart/negative/bounded gates PASS.
- dependency equivalence conflict is explicitly preserved as uncertainty.

Still not proven: general coreference resolution, pronoun semantics, discourse semantics, semantic understanding.

## CURRENT FRONTIER — LANG-01F R1 — RUNTIME RERUN PENDING

Capability:

`LANG-01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY`

Teaching goal:

Given an admitted discourse reference form and exactly two structural antecedent candidates, SIGMA must maintain competing antecedent hypotheses, persist first-class ambiguity under tied contextual evidence, and revise ambiguity to a preferred antecedent hypothesis only when later raw-context evidence discriminates between the candidates.

Critical invariant:

`PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`

Scope intentionally limited to two competing candidates. Three candidates must be withheld rather than forced into the two-candidate model.

### Original LANG-01F runtime evidence — FAIL preserved

- `TOTAL_VM_INVOCATIONS=21`
- `POST_VM_ALIGNMENT_PASS_COUNT=19`
- `POST_VM_ALIGNMENT_FAIL_COUNT=2`
- `VM_NONZERO_COUNT=0`
- `STEP_LIMIT_HIT_COUNT=0`
- persistence PASS;
- restart/replay PASS;
- ambiguity-to-preference revision PASS;
- candidate encounter order is not winner policy PASS;
- bounded evidence capacity PASS.

The two failing cases were identified exactly:

- CASE 011 `THREE_CANDIDATES`
- CASE 012 `NO_CONTEXTUAL_SUPPORT`

In both cases native cognition correctly withheld:

- correct `LEARNING_STATUS`;
- correct `QUERY_STATUS`;
- `STATE_COMMIT_ALLOWED=0`;
- no VM crash;
- no state mutation.

Failure classification:

`NATIVE_OUTPUT_STATE_PROTOCOL`

Problem: with `STATE_COMMIT_ALLOWED=0` and no prior valid state, native output still emitted a non-`NONE` `NEXT_STATE_STATUS`, making rejected/withheld reasoning look like a persistable next state.

### LANG-01F R1 repair

Smallest native output-contract repair:

`IF STATE_COMMIT_ALLOWED=0 AND PREVIOUS_STATE_VALID=0 -> NEXT_STATE_STATUS=NONE`

Learning/query reason remains visible. Scoring, candidate competition, ambiguity policy, persistence policy, oracle PASS definition, and host boundary are unchanged.

R1 identities known before locked-runtime rerun:

- `R1_SOURCE_SHA256=1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`
- `R1_RUNNER_SHA256=db2673642ab471c23e1f7a067a1a16eb96b993ec75b9e6f345acb65e3ca3abd4`
- `R1_BUNDLE_SHA256=288d1b9254685310aa4b2ab79ebf18e93746ea18205e10fac81d735b94cafa2e`
- user verified R1 bundle SHA matches exactly.
- `R1_BYTECODE_SHA256=UNKNOWN` until rerun with locked sigmac.
- `R1_ADMISSION=NOT_YET_RERUN`

### EXACT NEXT ACTION

On the Termux device, run the already integrity-verified LANG-01F R1 bundle:

```bash
cp SIGMA_LANG_01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY_V1_R1_BUNDLE.zip \
   "$HOME/SIGMA/sigma_genesis1/"

cd "$HOME/SIGMA/sigma_genesis1" || exit 1

unzip -oq \
SIGMA_LANG_01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY_V1_R1_BUNDLE.zip

cd SIGMA_LANG_01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY_V1 || exit 1

bash run_SIGMA_LANG_01F_NATIVE_ADMISSION_V1.sh
```

Required success target:

- `TOTAL_VM_INVOCATIONS=21`
- `POST_VM_ALIGNMENT_PASS_COUNT=21`
- `POST_VM_ALIGNMENT_FAIL_COUNT=0`
- `NEGATIVE_TEST=PASS`
- persistence/restart/replay remain PASS;
- CASE 011 and CASE 012 preserve their real withholding reasons while `NEXT_STATE_STATUS=NONE` when commit is refused and no prior valid state exists;
- `ADMISSION=PASS` only if all original gates remain intact.

If FAIL, preserve exact first failure and repair only the narrow blocker. Do not proceed to LANG-01G until LANG-01F admission closes.

## PLANNED NEXT CAPABILITY AFTER LANG-01F PASS

Current intended dependency-first direction:

`LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_OR_NEGATION_SCOPE_FOUNDATION`

Do not implement until LANG-01F is admitted and the latest global handoff/canon files are re-read.

## CLAIM BOUNDARIES FOR THE LANGUAGE LANE

Even with LANG-01A..01E admitted:

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
