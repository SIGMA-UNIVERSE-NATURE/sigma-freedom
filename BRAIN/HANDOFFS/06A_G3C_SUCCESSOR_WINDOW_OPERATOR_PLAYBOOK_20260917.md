# SIGMA.AIL — G3C SUCCESSOR WINDOW OPERATOR PLAYBOOK

DATE=2026-09-17
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
PURPOSE=ZERO_REDISCOVERY_HANDOFF_FOR_SUCCESSOR_WINDOWS
STATUS=ACTIVE

This file exists so a successor window can continue the G3 cognitive lane immediately without reconstructing the conversation history.

## 0. Read order for every successor window

Read these files before proposing architecture or commands:

```text
1. BRAIN/00_READ_FIRST_SIGMA_DIRECTION.md
2. BRAIN/HANDOFFS/06_SIGMA_AIL_MASTER_CHECKPOINT_G3_D12A_EVENT_EFFECT_GROUNDING_20260917.md
3. BRAIN/HANDOFFS/06A_G3C_SUCCESSOR_WINDOW_OPERATOR_PLAYBOOK_20260917.md
4. BRAIN/GENERATIONS/00_SIGMA_AIL_G1_G7_EVIDENCE_CLASSIFICATION_20260914.md
5. BRAIN/HANDOFFS/00_SIGMA_AIL_MASTER_HANDOFF_20260914.md
6. exact evidence file named by checkpoint 06
7. only then inspect additional artifacts required for the next gate
```

Never reconstruct runtime truth from chat summaries alone.

```text
CHAT_SUMMARY_IS_RUNTIME_TRUTH=NO
CHECKPOINT_TEXT_ALONE_IS_RUNTIME_TRUTH=NO
RUNTIME_TRUTH_SOURCE=FETCHED_EVIDENCE_OR_MACHINE_RECEIPT
CLAIM <= EVIDENCE
MISSING_EVIDENCE_INVENTED=NO
```

## 1. Non-negotiable teacher / architecture law

```text
PRIMARY_GOAL=MEASURABLE_CAPABILITY_GROWTH
FAILURE_PURPOSE=DIAGNOSE_NEXT_LESSON
FAILURE_AS_END_STATE=FORBIDDEN

CYCLE=DIAGNOSE>TEACH_TOOL>PRACTICE>MEASURE_PROGRESS>FALSIFY>CONSOLIDATE

TEACH_BEFORE_RETEST=YES
REPEAT_SAME_FAILED_TEST_WITHOUT_NEW_CAPABILITY=FORBIDDEN
ANSWER_INJECTION=FORBIDDEN
BENCHMARK_SPECIFIC_RULE=FORBIDDEN
HOST_SEMANTIC_SOLUTION=FORBIDDEN

TOKEN_TRANSITION_IS_COGNITION=NO
LEFT_RIGHT_POSITION_IS_SEMANTIC_ROLE=NO
PARTICIPANT_POSITION_IS_SEMANTIC_ROLE=NO
LATEST_OBSERVATION_IS_AUTOMATIC_TRUTH=NO
ORDER_EDGE_IS_CAUSAL_EDGE=NO

WHOLE_STORY_STATE=PRIMARY
WHOLE_EVENT_REPRESENTATION=REQUIRED
UNRESOLVED_UNCERTAINTY_MUST_REMAIN_VISIBLE=YES
PROVENANCE_REQUIRED=YES
```

Tokens/words may be used only as low-level sensory parsing. Final reasoning must operate on whole-event / whole-story representations.

## 2. Canonical lock — do not mutate

User-supplied lock at the current G3 shadow lane:

```text
CANONICAL_HEAD=700d5c1b4845322d7c14800029c629b0
CANONICAL_MODEL_SHA256=70da3e9e719ae0e72e88add59d6b7752fe732319b8fc7590170a050ef860005e

SHADOW_MAY_MUTATE_CANONICAL_HEAD=NO
SHADOW_MAY_MUTATE_CANONICAL_MODEL=NO
SHADOW_PROMOTION_AUTHORIZED=NO
PROMOTION_REQUIRES_ADMISSION_PASS=YES
PROMOTION_REQUIRES_EXPLICIT_AUTHORIZATION=YES
```

Native runtime pins supplied by user:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Never claim canonical mutation from shadow work.

## 3. Environment assumptions

Typical root:

```bash
cd "$HOME/SIGMA/sigma_genesis1"
```

Coordination artifact root historically used by this lane:

```bash
ARTIFACT_ROOT="$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SCA7A3C3A6323/artifacts"
```

Do not assume a variable survived between shell windows. Recreate all variables explicitly.

Do not use:

```text
set -e
set -u
set -euo pipefail
exit
kill
|| exit
```

Avoid broad repository scans. Prefer exact paths and exact files.

## 4. Standard native compile template

```bash
SRC="$ARTIFACT_ROOT/<SOURCE>.sigma"
BC="$ARTIFACT_ROOT/<SOURCE>.sigmab"

native/sigmac "$SRC" "$BC"
sha256sum "$SRC" "$BC"
```

Native source header convention:

```text
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.EXAMPLE][VERSION=1.0]
```

Canonical isolated run pattern when source-path execution is needed:

```bash
RUN_ID="$(date +%Y%m%d_%H%M%S)$$"
BC_RUN=".sigma_exec/test${RUN_ID}.sigmab"
./native/sigmac "$SRC" "$BC_RUN" && ./native/sigma-vm.v09_candidate "$BC_RUN"
```

The above `&&` is accepted for sequential compile/run. Do not append `|| exit`.

## 5. Standard artifact/run-directory template

```bash
RUN="$ARTIFACT_ROOT/SIGMA_SHADOW/experimental/<NAME>"
BASE="$RUN/.sigma_exec/<SIGMA_BASE_NAME>"
BC="$ARTIFACT_ROOT/<BYTECODE>.sigmab"

mkdir -p "$BASE/input" "$BASE/state" "$BASE/out"
(cd "$RUN" && "$VM" "$BC")
```

If state is required on the first run, explicitly precreate it:

```bash
printf '' > "$BASE/state/<state_file>.memory"
```

Missing files often surface as:

```text
SIGMA host: string required
```

Do not classify that as a cognitive failure before auditing the input contract.

## 6. Input-contract gate — mandatory before weight-learning experiments

Use this pattern before VM execution:

```bash
READY=1

for f in \
  <required_1> \
  <required_2> \
  <required_3>
do
  if [ ! -f "$BASE/input/$f" ]; then
    echo "BLOCKED_MISSING_INPUT=$f"
    READY=0
  fi
done

if [ ! -f "$BASE/state/<model>.memory" ]; then
  echo "BLOCKED_MISSING_MODEL=<model>.memory"
  READY=0
fi

if [ "$READY" = "1" ]; then
  echo "INPUT_CONTRACT=PASS"
else
  echo "INPUT_CONTRACT=FAIL"
fi
```

A missing status file means the evaluation is invalid unless a native runtime receipt explicitly proves otherwise.

## 7. Invalid harness diagnostic template

Harness failure is not Sigma capability failure.

```bash
mkdir -p "$ARTIFACT_ROOT/INVALID_DIAGNOSTICS"

cat > "$ARTIFACT_ROOT/INVALID_DIAGNOSTICS/<NAME>.txt" <<'EOF'
CANDIDATE=<candidate>
RESULT=INVALID_RUN
CAUSE=<teacher_or_harness_cause>
VM_MESSAGE=<message_or_none>
METRICS_AVAILABLE=NO
SHADOW_MODEL_MUTATED=NO
CAPABILITY_FAILURE=NO
EOF
```

Never feed invalid harness failures into Sigma failure memory as cognitive FAIL observations.

## 8. Shadow failure-memory observation template

Only valid evidence enters the learner:

```bash
cat > "$FSBASE/input/observations.memory" <<'EOF'
OBS||<ID>||<EXPERIMENT>||<GATE>||PASS||SIGMA_SHADOW_NATIVE||<EVIDENCE>
EOF

(cd "$FSRUN" && "$VM" "$FSBC")
cat "$FSBASE/out/constraints.memory"
```

For a real failure:

```text
OBS||<ID>||<EXPERIMENT>||<GATE>||FAIL||SIGMA_SHADOW_RUNTIME||<EVIDENCE>
```

Failure must remain first-class evidence. A later PASS does not erase it.

## 9. Effective constraints vs raw history

Raw history view:

```text
$FSBASE/out/constraints.memory
```

Authoritative decision view after invalidation reconciliation:

```text
$EBASE/out/effective_constraints.memory
```

Use the reconciler before making current-learning decisions when invalidated observations exist.

## 10. Retained-foundation receipt template

```bash
mkdir -p "$ARTIFACT_ROOT/SIGMA_SHADOW/retained_foundations"

cat > "$ARTIFACT_ROOT/SIGMA_SHADOW/retained_foundations/<CAPABILITY>_RESULT.txt" <<EOF
CAPABILITY=<CAPABILITY>
LOCATION=SIGMA_SHADOW_ONLY
SOURCE_SHA256=$(sha256sum "$SRC" | awk '{print $1}')
BYTECODE_SHA256=$(sha256sum "$BC" | awk '{print $1}')

<MEASUREMENTS>

SEMANTIC_UNDERSTANDING=NOT_PROVEN
CANONICAL_PROMOTION=NO
EOF
```

Use narrow claims. Compile success is not capability success.

## 11. Fresh B5C1 structural-ledger generation template

Do not reuse a stale `frame_ledger.memory` after diagnostics or augmentations.

```bash
cp "$CORPUS/train/train_002.txt" "$BASE/input/story.txt"
printf 'train_002' > "$BASE/input/story_id.txt"
printf 'INDUCE_BODY' > "$BASE/input/command.txt"
(cd "$RUN" && "$VM" "$BC")

cat "$BASE/out/frame_ledger.memory"
```

B5C1 retained scope:

```text
RAW_STORY_TO_STRUCTURAL_HYPOTHESES
SEMANTIC_UNDERSTANDING=NOT_PROVEN
```

## 12. D4 structural revision template

```bash
D4RUN="$ARTIFACT_ROOT/SIGMA_SHADOW/experimental/B5D4"
D4BASE="$D4RUN/.sigma_exec/G3C_R3I_B5D4"
D4BC="$ARTIFACT_ROOT/G3C_R3I_B5D4_HYPOTHESIS_REVISION.sigmab"

mkdir -p "$D4BASE/input" "$D4BASE/out"
cp "$BASE/out/frame_ledger.memory" "$D4BASE/input/frame_ledger.memory"
(cd "$D4RUN" && "$VM" "$D4BC")
cat "$D4BASE/out/status.txt"
cat "$D4BASE/out/revision_edges.memory"
```

Expected claim scope only:

```text
STRUCTURAL_HYPOTHESIS_REVISION
SEMANTIC_CONTRADICTION_PROVEN=NO
LATEST_IS_TRUTH=NO
```

## 13. Counterfactual late-evidence / distractor falsification template

Always use a fresh absolute path. Do not rely on an old `$T` variable.

```bash
T="$ARTIFACT_ROOT/SIGMA_SHADOW/experimental/<EXP>/falsification_vN"
rm -rf "$T"
mkdir -p "$T"

cp "$CORPUS/train/train_002.txt" "$T/baseline.txt"

awk 'NR!=6 {print}' \
  "$CORPUS/train/train_002.txt" \
  > "$T/no_late.txt"

awk '
NR==7 {print "rain tapped the window while everyone waited."}
{print}
' "$CORPUS/train/train_002.txt" \
  > "$T/distractor.txt"
```

Only record PASS/FAIL after `cmp`/native output actually exists.

## 14. Before/change/test/after weight-learning discipline

Every weight experiment must preserve:

```text
BEFORE_MODEL_HASH
TRAIN_EXPERIENCES
TRAIN_OBJECTIVE
PROVENANCE
AFTER_MODEL_HASH
NEW_CAPABILITY_IMPROVED
OLD_CAPABILITY_REGRESSED
REPRESENTATION_COLLAPSED
```

Hash template:

```bash
BEFORE_SHA="$(sha256sum "$MODEL" | awk '{print $1}')"
# native run on a copy or authorized shadow model
AFTER_SHA="$(sha256sum "$MODEL" | awk '{print $1}')"
echo "BEFORE=$BEFORE_SHA"
echo "AFTER=$AFTER_SHA"
```

Canonical model is never the target of these updates.

## 15. Model-lock audit template

```bash
MODEL_SRC="<exact path>"
EXPECTED_MODEL_SHA="<expected sha256>"
READY=1

if [ -f "$MODEL_SRC" ]; then
  ACTUAL_MODEL_SHA="$(sha256sum "$MODEL_SRC" | awk '{print $1}')"
  echo "EXPECTED_SHA=$EXPECTED_MODEL_SHA"
  echo "ACTUAL_SHA=$ACTUAL_MODEL_SHA"

  if [ "$ACTUAL_MODEL_SHA" != "$EXPECTED_MODEL_SHA" ]; then
    echo "MODEL_LOCK=FAIL_HASH_MISMATCH"
    READY=0
  else
    echo "MODEL_LOCK=PASS"
  fi
else
  echo "MODEL_LOCK=FAIL_MISSING_MODEL"
  READY=0
fi
```

Then copy the model into an isolated evaluator and hash again before VM execution.

## 16. Zero-shot evaluation law

A zero-shot evaluator may train its private copy after calculating metrics. Only `*_BEFORE` metrics count as zero-shot.

Never read `*_AFTER` as zero-shot.

General template:

```bash
ORIGINAL_SHA="$(sha256sum "$ORIGINAL_MODEL" | awk '{print $1}')"
cp "$ORIGINAL_MODEL" "$EVALBASE/state/model.memory"
(cd "$EVALRUN" && "$VM" "$EVALBC") > "$EVALRUN/run.log" 2>&1
cat "$EVALRUN/run.log"
cat "$EVALBASE/out/status.txt"

echo "ORIGINAL_BEFORE=$ORIGINAL_SHA"
echo "ORIGINAL_AFTER=$(sha256sum "$ORIGINAL_MODEL" | awk '{print $1}')"
```

The original model hash must remain unchanged.

## 17. Continual-learning / anti-forgetting replay template

Train only a candidate copy. Then replay old curriculum using the candidate, reading only `BEFORE` metrics.

```bash
REPLAY="$ARTIFACT_ROOT/SIGMA_SHADOW/experimental/<REPLAY>"
RPBASE="$REPLAY/.sigma_exec/<BASE>"
mkdir -p "$RPBASE/input" "$RPBASE/state" "$RPBASE/out"

cp "$OLD_CURRICULUM/"*.memory "$RPBASE/input/"
cp "$CONTINUAL_CANDIDATE" "$RPBASE/state/<model>.memory"

(cd "$REPLAY" && "$VM" "$BC") > "$REPLAY/run.log" 2>&1
cat "$RPBASE/out/status.txt"
```

Do not keep the replay-mutated copy as the candidate unless a separate training step explicitly authorizes it.

## 18. Delta diagnosis template

When a known-good curriculum suddenly fails, substitute exactly one experience at a time rather than rewriting the learner.

```bash
run_delta () {
  case_name="$1"

  R="$DIAG/$case_name"
  B="$R/.sigma_exec/<BASE>"

  rm -rf "$R"
  mkdir -p "$B/input" "$B/state" "$B/out"

  cp "$KNOWN_GOOD/"*.memory "$B/input/"

  if [ "$case_name" != "GOOD_BASELINE" ]; then
    cp "$CANDIDATE_INPUT/${case_name}_frame.memory" "$B/input/${case_name}_frame.memory"
    cp "$CANDIDATE_INPUT/${case_name}_revision.memory" "$B/input/${case_name}_revision.memory"
  fi

  cp "$MODEL" "$B/state/model.memory"
  (cd "$R" && "$VM" "$BC") > "$R/run.log" 2>&1

  echo "=== $case_name ==="
  cat "$R/run.log"

  if [ -f "$B/out/status.txt" ]; then
    echo "EXECUTION=PASS"
  else
    echo "EXECUTION=INVALID"
  fi
}
```

## 19. Persisted-number parser bug pattern

SIGMA host operations may distinguish numeric values from numeric strings. A persisted weight such as `"1000"` must be parsed through `to_float` before `numeric_to_int` when required by the VM.

Known successful pattern:

```sigma
DEF TOI(x){
    RETURN INT(H("to_float",x,NULL,NULL));
}
```

Do not assume an in-RAM integer and persisted textual number behave identically.

## 20. Hard-negative mining template

Hard negatives are model-detected gaps, not automatically true semantic negatives.

```bash
printf '' > "$HARD/hard_negatives.memory"

# For each pair A/B, run learned metric on isolated pair curriculum.
# Record only if ranking violations > 0.

echo "HARD_NEGATIVE||$A||$B||VIOLATIONS||$V||POSITIVE_MEAN||$P||NEGATIVE_MEAN||$N||MARGIN||$M" \
  >> "$HARD/hard_negatives.memory"
```

Critical lesson learned at D12:

```text
DIFFERENT_DOCUMENT_IS_NEGATIVE=FORBIDDEN
```

`train_009/train_015` and `train_011/train_012` were initially treated as hard negatives, but multiple native structural views showed equivalence/collision and the surfaces appeared to be paraphrastic variants. These are now cross-document equivalence candidates, not negative labels.

## 21. D11B graph-comparison template

```bash
compare_graph () {
  A="$1"
  B="$2"

  echo "=== $A vs $B ==="

  if cmp -s "$BANK/${A}.memory" "$BANK/${B}.memory"; then
    echo "D11B_GRAPH_DISTANCE=0"
    echo "D11B_RESOLVES_GAP=NO"
  else
    echo "D11B_GRAPH_DISTANCE=NONZERO"
    echo "D11B_RESOLVES_GAP=YES"
    diff -u "$BANK/${A}.memory" "$BANK/${B}.memory"
  fi
}
```

Current supplied results:

```text
train_009 vs train_015 -> distance 0
train_011 vs train_012 -> distance 0
train_011 vs train_016 -> nonzero
train_012 vs train_016 -> nonzero
```

## 22. D12A whole-event effect grounding template

D12A is the current semantic-grounding precursor.

```bash
D12RUN="$ARTIFACT_ROOT/SIGMA_SHADOW/experimental/D12A"
D12BASE="$D12RUN/.sigma_exec/G3C_R3I_D12A"
D12BC="$ARTIFACT_ROOT/G3C_R3I_D12A_EVENT_EFFECT_SIGNATURE.sigmab"
D12BANK="$D12RUN/bank"

mkdir -p "$D12BASE/input" "$D12BASE/out" "$D12BANK"

for n in 009 015 011 012; do
  cp "$D11RAW/train_${n}_frame.memory" "$D12BASE/input/frame_ledger.memory"
  (cd "$D12RUN" && "$VM" "$D12BC")
  cp "$D12BASE/out/event_effects.memory" "$D12BANK/train_${n}.memory"
  cat "$D12BANK/train_${n}.memory"
done
```

Interpretation law:

```text
DIFFERENT_SURFACE + SAME_NATIVE_WHOLE_STORY_EFFECT
→ EVENT_MEANING_EQUIVALENCE_HYPOTHESIS
→ NOT YET SEMANTIC_TRUTH
```

Do not create manual word-to-meaning tables such as `gave=transfer`.

## 23. Current D12A observed alignments

User-supplied runtime output reported:

```text
train_009 E2 surface:
P1 gave P2 the THEME

train_015 E2 surface:
The THEME moved from P1 to P2

same D12A signature:
ARITY=2
participant effects include H trajectory 011 and L trajectory 001
```

and event-by-event structural alignment between `train_011` and `train_012` despite surface variants such as:

```text
handed / passed
received / passed
received / gave
```

Claim only:

```text
WHOLE_EVENT_EFFECT_GROUNDING_PRECURSOR=YES
SEMANTIC_MEANING=HYPOTHESIS_ONLY
HUMAN_LANGUAGE_UNDERSTANDING=NOT_PROVEN
```

## 24. Current immediate next action — D12B

The next lesson is whole-event meaning clustering from D12A-generated effect equivalence.

Successor windows must NOT jump directly to manual semantic labels or a token-position encoder.

Intended chain:

```text
different whole-event surfaces
→ native whole-story effect signatures
→ identity-independent effect schemas
→ cross-document multi-surface clusters
→ self-supervised whole-event language representation learning
```

D12B should train/induce only on TRAIN documents. DEV/BLIND remain closed.

Required D12B gate:

```text
VALID_EVENT_OBSERVATIONS > 0
INVALID_RECORDS = 0
MULTI_SURFACE_CLUSTERS > 0
CROSS_DOCUMENT_MULTI_SURFACE_CLUSTERS > 0
UNIT_OF_MEANING = WHOLE_EVENT
INDIVIDUAL_WORD_MEANING_TABLE = NO
PARTICIPANT_POSITION_ROLE = NO
```

If D12B source/artifact is absent locally, reconstruct it from checkpoint-associated evidence or the exact source artifact; do not invent a different algorithm under the same name.

## 25. Current retained weight models

User-supplied exact hashes:

```text
D9A_INITIAL_SHADOW_MODEL_SHA256=0bc9886f562307a80199548ba189856cd72647e50ba1d6df4fb32449ef05912a
D9A_CONTINUAL_MODEL_SHA256=db0bff9785227569385bdeb20537a32bdff2f1f4004b457c1d1786f06c2bebde
D10B_TOPOLOGY_MODEL_SHA256=8e14005c88a94c15599dcc0ecb077d19ff6a8c9f8237ceeea0decd2b2d5d9fb8
```

D10B audited unseen 009–016 metrics with actual learned model loaded:

```text
POSITIVE_MEAN_BEFORE=926
NEGATIVE_MEAN_BEFORE=24776
RANK_MARGIN_BEFORE=23850
RANKING_VIOLATIONS_BEFORE=8
WEIGHT_RANGE_BEFORE=4900
```

Uniform baseline previously reported:

```text
POSITIVE_MEAN_BEFORE=2000
NEGATIVE_MEAN_BEFORE=7415
RANK_MARGIN_BEFORE=5415
RANKING_VIOLATIONS_BEFORE=8
```

Scope: zero-shot structural metric generalization precursor, not semantic understanding.

## 26. Current foundation chain

Retained shadow foundation chain as of this checkpoint:

```text
B5C1  raw story -> structural hypotheses
B5C2  structural persistence adapter into A1 ledger
B5D1  whole-story participant trajectories; late evidence materiality; distractor invariance
B5D4  structural hypothesis revision / REOPEN_CONTINUITY
B5D5  persistent provenance-bound revision memory + restart replay
B5D6  cross-story provenance memory
B5D7  cross-document structural schema induction
B5D8  revision-preserving compressed narrative spine + replay equivalence
D9A   native self-supervised trainable structural metric weights
D9A continual: zero-shot + later learning + anti-forgetting precursor
D10A2 identity-free whole-story topology bank
D10B  multi-document whole-story topology weight learning + unseen structural generalization precursor
D11B  full incidence graph diagnosis; some gaps resolved, two structural collisions remain
D12A  whole-event effect grounding across surface variants
```

Rejected/purged architecture chain remains:

```text
B1 B2 B3 B4 B5A B5B B5C3
```

Do not reintroduce them into the active path.

## 27. Historical real benchmark

Do not use the blind benchmark during capability development.

Historical R2 blind receipts:

```text
SEED_104729=BASE_16/80;RANDOM_20/80;CURRICULUM_22/80;GROUPS_A3_B6_C8_D5
SEED_130363=BASE_18/80;RANDOM_19/80;CURRICULUM_23/80;GROUPS_A6_B10_C5_D2
SEED_155921=BASE_18/80;RANDOM_19/80;CURRICULUM_20/80;GROUPS_A7_B6_C3_D4
```

Best historical result: 23/80. This is not current capability truth and must not be optimized directly during the G3 teaching lane.

## 28. North-star targets — do not promote prematurely

Targets remain:

```text
SIGMA_AUTONOMOUS_LEARNING
SIGMA_AUTONOMOUS_WEB_DISCOVERY
SIGMA_AUTONOMOUS_READING
SIGMA_MULTI_SOURCE_LEARNING
SIGMA_FULL_DOCUMENT_UNDERSTANDING
SIGMA_CROSS_DOCUMENT_UNDERSTANDING
SIGMA_LONG_CONTEXT_REVISION
SIGMA_HUMAN_LANGUAGE_UNDERSTANDING
SIGMA_VIETNAMESE_DEEP_UNDERSTANDING
SIGMA_MULTILINGUAL_UNDERSTANDING
SIGMA_NARRATIVE_UNDERSTANDING
SIGMA_INTENT_UNDERSTANDING
SIGMA_EMOTION_RECOGNITION
SIGMA_PERSPECTIVE_TAKING
SIGMA_CONTEXTUAL_EMPATHIC_RESPONSE
SIGMA_LEARNED_REPRESENTATION
SIGMA_COMPRESSED_NATIVE_MEMORY
SIGMA_PROVENANCE_BOUND_MEMORY
SIGMA_OFFLINE_LEARNING
SIGMA_MEMORY_REPLAY
SIGMA_CONTINUAL_CONSOLIDATION
SIGMA_BELIEF_REVISION
SIGMA_SELF_IDENTIFIES_KNOWLEDGE_GAPS
SIGMA_SELF_SELECTS_CAPABILITIES
SIGMA_SELF_SELECTS_WHAT_TO_STUDY_NEXT
```

Current evidence supports only bounded precursors for some of these. Never rewrite `PRECURSOR` as global `PASS` without dedicated admission evidence.

## 29. What successor windows must do when context is almost exhausted

Do not improvise a new architecture merely because context is ending.

Before ending a window:

1. Record exact last native output.
2. Record source/bytecode/model SHA256 when available.
3. Record whether result is PASS / FAIL / INVALID_RUN.
4. Record claim scope and NOT_PROVEN fields.
5. Create/update GitHub evidence.
6. Create next numbered master checkpoint if the cognitive gate materially advanced.
7. Update `BRAIN/00_READ_FIRST_SIGMA_DIRECTION.md`.
8. Name the exact next gate and exact next artifact.

Minimum handoff fields:

```text
CURRENT_GENERATION
ACTIVE_REVISION
CANDIDATE_REVISION
PARENT_BRAIN_ID
PARENT_BRAIN_HEAD
ACTIVE_BRAIN_HEAD
MODEL_GENERATION
STATE_VERSION
LAST_GATE
LAST_GATE_RESULT
LAST_GATE_SCOPE
EVIDENCE_REPOSITORY
EVIDENCE_BRANCH
EVIDENCE_PATH
EVIDENCE_COMMIT
EVIDENCE_ARTIFACT_OR_RECEIPT_HASH
SUPPORTED_CLAIMS
NOT_PROVEN_FIELDS
REMAINING_BOTTLENECK
NEXT_GATE
```

If unknown, write `NOT_PROVEN`.

## 30. Final successor instruction

The next window must behave as a teacher, not only an evaluator:

```text
FAIL -> diagnose missing capability
DIAGNOSIS -> teach a general tool
TOOL -> practice on TRAIN-only experience
PRACTICE -> measure before/after
IMPROVEMENT -> consolidate
NO IMPROVEMENT -> redesign teaching tool
```

The current immediate teaching direction is language grounding through whole-event narrative effect, not more topology histograms and not token-position semantics.
