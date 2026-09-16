# G3C Native Semantic Shadow Checkpoint — 2026-09-17

## Purpose

This checkpoint exists so any new tmux/window can resume the exact current work immediately without rescanning old sessions, rediscovering paths, or repeating failed approaches.

This work is **local-runtime-first**. GitHub is used only as durable storage/checkpoint documentation. All learning, training, testing, verdict generation, and shadow-state updates happen locally through SIGMA.

## Responsibility of this window/workstream

The assigned responsibility is:

> Improve SIGMA deep semantic understanding of whole documents/stories while preserving SIGMA-native authority. Build and test only in shadow/candidate space. SIGMA must learn from its own semantic mistakes. Host/Bash may orchestrate mechanically but must not choose answers, semantic verdicts, accepted learning, or canonical cutover. Only mechanisms with demonstrated blind whole-document semantic uplift may later request explicit admission for ownership/canonical promotion.

Primary semantic goals include whole-document understanding of:

- causal structure
- beliefs and false beliefs
- intent
- perspective / information asymmetry
- evidence vs unsupported inference
- implication / revision of beliefs
- deep narrative understanding

Summarization is **not** the learning objective here. SIGMA already has long-document summarization capability; summary may be used only as readout/evidence, not as the semantic-learning target.

## Non-negotiable rules

1. **Execution authority:** use the canonical Native VM09 binary for all authoritative learning/eval:

```bash
./native/sigma-vm.v09_candidate
```

Verified SHA256:

```text
029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Compiler:

```bash
./native/sigmac
```

Verified SHA256:

```text
65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
```

2. **Canonical baseline:**

```text
CANONICAL_HEAD=700d5c1b4845322d7c14800029c629b0
MODEL_SHA256=70da3e9e719ae0e72e88add59d6b7752fe732319b8fc7590170a050ef860005e
```

3. **Canonical mutation is forbidden in normal shadow work.** Current session contract requires separate explicit SIGMA admission for canonical mutation.

4. **All successful/failed learning experiments remain shadow-only** until blind whole-document semantic improvement is demonstrated and SIGMA-native admission allows promotion.

5. **No host cognition / no Bash verdict.** Bash/Python may create files, patch candidate source, compile, invoke VM09, hash files, and preserve receipts. They must not select the semantic answer, semantic winner, accepted learning update, or canonical cutover.

6. **Do not reintroduce narrow training paradigms** that were explicitly rejected:

```text
NO next-token objective
NO left/right window objective
NO one-word -> one-word learning
NO sentence-next objective
NO byte-hash semantic representation as the learning goal
NO keyword trick as semantic understanding
NO host-selected story/correct answer
```

7. Unit of cognition/training should be **whole document / whole story**. Internal mechanics may use primitive symbols only as substrate; they must not become the learning objective.

8. If an update improves one metric while materially degrading another semantic safety metric, reject/revert it. Current preferred update policy is Pareto-style no-regression.

9. Do not keep running the same tick after `UPDATE_KEPT=0` repeatedly. That is a plateau signal; change the mechanism rather than brute-forcing it.

10. Output shown to the operator must be bounded and wrapped:

```text
<<< SIGMA/TMUX BEGIN >>>
...
<<< SIGMA/TMUX END >>>
```

Keep diagnostic output <= 50 lines unless specifically required.

---

# Universal tmux/session protocol

Commit establishing the universal window rule:

```text
8f155d6e1bcf1bf6aec679a56aba528adc345363
```

All windows use the same front door.

## New window

```bash
source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
```

Then request a session with an exact task description. For this workstream, use wording equivalent to:

```bash
sigma-session "Resume G3C whole-document deep semantic shadow learning; Native VM09 authority; continue from GitHub checkpoint G3C_NATIVE_SEMANTIC_SHADOW_CHECKPOINT_20260917; no canonical mutation without explicit SIGMA admission"
```

Expected minimum grant:

```text
SESSION=GRANTED
ACCESS=READ_PLUS_ARTIFACT_WRITE
ARTIFACT_ROOT=...
CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION
```

## If pane already has a session

Do **not** mint another session. Use:

```bash
sigma-session status
```

## Finish

```bash
sigma-session finish
```

Never copy another pane's `SESSION_CODE`. Never invent a session code.

---

# Current local session at checkpoint time

```text
SESSION=GRANTED
SESSION_CODE=SF7049602AD71
RUN_ID=SESSION_SF7049602AD71
ACCESS=READ_PLUS_ARTIFACT_WRITE
ARTIFACT_ROOT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SF7049602AD71/artifacts
CANONICAL_MUTATION=REQUIRES_EXPLICIT_ADMISSION
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
```

If this session is gone, create a new session using the universal protocol above. Do not reuse `SF7049602AD71` in a new pane.

Convenience template to recover the currently granted artifact root dynamically:

```bash
ART="$(sigma-session status | awk -F= '$1=="ARTIFACT_ROOT"{print $2;exit}')"
```

---

# Admission state already established before this work

Explicit mechanism admission metadata exists for the prior G3C mechanism work:

```text
GATE=G3C_SEMANTIC_R2_FIX2
TASK=SEMANTIC_R2_FIX2_RUNTIME_CORE_MECHANISM
RECEIPT_LABEL=MECHANISM_EVIDENCE
ADMISSION_KEY=103cee5b11b4f439f71d2472ea318be457e56f041d58f33c97433eea67f3d64f
EXPLICIT_ADMISSION=PASS
ADMISSION_SCOPE=RUNTIME_CORE_MECHANISM
SEMANTIC_CAPABILITY_ADMISSION=NO
```

Important distinction:

```text
RUNTIME_CORE_MECHANISM admitted != semantic capability admitted
```

No semantic capability/canonical promotion should be inferred from the mechanism admission.

---

# Current methodology

## Core operating principle

Use candidates/shadow as the laboratory:

```text
EXPERIMENT
  -> NATIVE VM09 SELF-LEARNING IN SHADOW
  -> BLIND WHOLE-DOCUMENT SEMANTIC TEST
  -> NATIVE SIGMA VERDICT / NO-REGRESSION CHECK
  -> REGRESSION AGAINST EXISTING CAPABILITIES
  -> EXPLICIT ADMISSION
  -> SIGMA OWNERSHIP / CANONICAL PROMOTION
```

Build success alone is not success.
Training-loss improvement alone is not success.
Training-set alignment alone is not success.

Only demonstrated whole-document semantic generalization is promotable.

---

# Experiments already performed — DO NOT REDO

## Early mechanical probes

Native whole-text read gateway passed:

```text
host("read_text", path) => PASS
```

Native write gateway passed through host:

```text
host("write_text", path, text) => PASS
```

Direct calls such as the following were invalid because these names are host operations, not direct SIGMA functions:

```text
understand(...) -> undefined function
learn(...) -> undefined function
str_split(...) -> undefined function when called directly
write_text(...) -> undefined function when called directly
```

Use `host("operation", ...)` when the primitive is a host operation.

## Narrow representation approaches rejected

Do not return to these as the semantic-learning architecture:

- byte-hash representation
- next-line pair loss
- sentence-level next prediction
- word vocabulary learning as objective
- token/left/right approaches
- fixed random whole-document representation plus linear mapper
- fixed random multi-view weighting as final architecture

## Candidate VM experiments

Several candidate VM builds were created to explore generic primitives, but **they are not authority**. Their build success does not count as SIGMA learning. Native VM09 remains execution authority for authoritative learning/eval.

Candidate VM experiments included generic UTF-8/vector/attention/tensor/document-state helpers. Some were mechanically valid, but no ownership transfer should occur merely because they compile.

---

# Shadow experiment results

## R9 — Native self-learning, single head

```text
EXECUTION_AUTHORITY=NATIVE_VM09
AVG_MARGIN_BEFORE=-0.0458740453
AVG_MARGIN_AFTER=-0.0450842207
POSITIVE_BEFORE=2
POSITIVE_AFTER=2
WORST_MARGIN_BEFORE=-0.1243269927
WORST_MARGIN_AFTER=-0.0980027568
SELF_ACCEPTED_UPDATES=5
SELF_REJECTED_UPDATES=1
```

Verdict for workflow purposes: insufficient. Do not promote.

## R10B — two-layer native self-learning

```text
AVG_MARGIN_BEFORE=-0.0480810787
AVG_MARGIN_AFTER=-0.0478805030
POSITIVE_BEFORE=3
POSITIVE_AFTER=3
WORST_MARGIN_BEFORE=-0.1270091082
WORST_MARGIN_AFTER=-0.1194821986
SELF_ACCEPTED_STEPS=1
SELF_REJECTED_STEPS=1
```

Insufficient. Do not promote.

## R11 — associative semantic memory

```text
AVG_MARGIN_ASSOCIATIVE=-0.0280982678
AVG_MARGIN_FINAL=-0.0192005483
POSITIVE_ASSOCIATIVE=1
POSITIVE_FINAL=3
WORST_ASSOCIATIVE=-0.0851566039
WORST_FINAL=-0.0473646375
SELF_ACCEPTED_UPDATES=37
```

Improvement but insufficient general semantic capability. Do not promote.

## R12C/R12D/R12E — semantic-head checkpointed self-learning

Important operational lesson: persistence initially had a duplicated absolute path. Correct rule is that READ and WRITE must use the **same exact `history.csv` path**.

Correct persistence form:

```sigma
⚡ history:RD("<SHADOW>/history.csv");
...
WR("<SHADOW>/history.csv",history);
```

After fixing persistence, updates accumulated across VM09 ticks.

Observed good state before plateau:

```text
AVG_MARGIN ~ -0.102534595845015
POSITIVE = 10
WORST = -0.313405073206105
```

R12E then plateaued with repeated:

```text
UPDATE_KEPT=0
```

Do not brute-force this same mechanism again.

## R13 — semantic metric geometry

R13 produced stable Pareto improvement over multiple Native VM09 ticks.

Representative progression:

```text
ALIGN_MARGIN: roughly -0.05359 -> -0.04749 and improving
ORACLE_TOP: 10 -> 12
WORST: roughly -0.33195 -> -0.20657 and improving
```

This was the strongest training-side signal before R13M.

## R13M — mass-preserving semantic metric

Purpose: prevent global metric-weight collapse while allowing semantic redistribution.

Observed:

```text
WEIGHT_MEAN_BEFORE=1
WEIGHT_MEAN_AFTER=1
```

Representative progression:

```text
ALIGN_MARGIN_BEFORE=-0.0469918341894755
ALIGN_MARGIN_AFTER=-0.0469017834882994
ORACLE_TOP=12
WORST_BEFORE=-0.203134824917274
WORST_AFTER=-0.200782131951634
```

Later:

```text
ALIGN_MARGIN ~ -0.04565200889679
ORACLE_TOP=12
WORST ~ -0.193965019642973
WEIGHT_MEAN=1
```

Then plateaued with repeated:

```text
UPDATE_KEPT=0
```

R13M is the best shadow state currently used for blind generalization testing.

## R14 — full semantic metric matrix

Started from R13M state. First tick:

```text
UPDATE_KEPT=0
```

No new path. Do not continue blindly.

## R15/R16 — global views / cross-view

R15:

```text
ALIGN_MARGIN_BEFORE=-0.00738093216721003
ALIGN_MARGIN_AFTER=-0.00738045318525929
ORACLE_TOP=6
```

R16:

```text
ALIGN_MARGIN_AFTER=-0.00737639291525006
ORACLE_TOP=6
WORST_AFTER=-0.0225868968732867
WEIGHT_NORM_BEFORE=2
WEIGHT_NORM_AFTER=2
```

Both too weak. Do not continue.

## R17 — trainable linear representation transform

Started from R13M state:

```text
UPDATE_KEPT=0
ORACLE_TOP=12
REPRESENTATION_NORM_BEFORE=4
REPRESENTATION_NORM_AFTER=4
```

Linear representation transform did not open a new learning path. Do not continue that exact approach.

---

# Best current shadow for evaluation

Use:

```text
$ART/SHADOW_R13M_MASS_PRESERVING
```

Important files:

```text
$ART/SHADOW_R13M_MASS_PRESERVING/R13M.sigma
$ART/SHADOW_R13M_MASS_PRESERVING/history.csv
```

R13M learned history must be preserved exactly.

Do not edit or regenerate `history.csv` casually.

---

# Blind generalization tests

## Blind 001

Frozen files:

```text
$ART/R13M_BLIND_GENERALIZATION_001/story.txt
$ART/R13M_BLIND_GENERALIZATION_001/interpretations.txt
```

Frozen SHA256:

```text
story.txt=28d7545f65105f466fb148ce36121fbf48b00d97bf3c4098152e2f4b3d68b6d8
interpretations.txt=df1e9da53e31050e5ce7bade10dde37430129b41514f683e5e9794e96302c671
```

Inference contract:

```text
EXECUTION_AUTHORITY=NATIVE_VM09
MODEL_UPDATE=NO
ORACLE_VISIBLE=NO
```

Observed scores:

```text
CAUSE        A=-0.434740423292618  B=-0.455473644479573
BELIEF       A=-0.400289841815499  B=-0.546717591720045
PERSPECTIVE  A=-0.131421657689724  B=-0.430664633368662
INTENT       A=-0.467292707275538  B=-0.325385537499538
UNSUPPORTED  A=-0.292374083247696  B=-0.169096366776008
TOTAL_A      -0.345223742664215
TOTAL_B      -0.385467554768765
```

Interpretation of evidence only: overall score favored A, and CAUSE/BELIEF/PERSPECTIVE favored A; INTENT and UNSUPPORTED favored B. Therefore generalization signal exists but is incomplete. **Do not promote.**

## Blind 002 — frozen, execution pending at checkpoint

Frozen files:

```text
$ART/R13M_BLIND_GENERALIZATION_002/story.txt
$ART/R13M_BLIND_GENERALIZATION_002/interpretations.txt
```

Frozen SHA256:

```text
story.txt=80c6658f367fce80caaabc7e17b43f487f7643f74c193f2a9157747b6c2b0ac4
interpretations.txt=ce35ccd9dbce3c96dc760133c905202a14fbec921473bede6598221eecd3562f
```

Blind 002 intentionally reverses the position of the semantically appropriate interpretation relative to Blind 001, specifically to test A/B position bias.

**Checkpoint resume point:** execute Blind 002 next. Do not retrain first.

---

# Exact resume action after opening a new window

After session grant:

```bash
ART="$(sigma-session status | awk -F= '$1=="ARTIFACT_ROOT"{print $2;exit}')"
```

Important: if resuming in a **new session**, the old `$ART` artifacts may live under the old workspace `SF7049602AD71`. Do not assume the new ART contains them. The checkpoint paths above refer to the old workspace. Preserve/copy only through an allowed artifact workflow; do not mutate canonical state.

The immediate pending operation is **Blind 002 inference with MODEL_UPDATE=NO** using R13M weights/history and Native VM09.

If the old workspace remains readable, use the existing Blind 001 inference program as a template and swap only Blind 001 input paths to Blind 002 paths.

Template:

```bash
OLD_ART="$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/WORKSPACES/SF7049602AD71/artifacts"
B1="$OLD_ART/R13M_BLIND_GENERALIZATION_001"
B2="$OLD_ART/R13M_BLIND_GENERALIZATION_002"
cp "$B1/R13M_BLIND.sigma" "$B2/R13M_BLIND.sigma"
sed -i \
  -e "s|$B1/story.txt|$B2/story.txt|g" \
  -e "s|$B1/interpretations.txt|$B2/interpretations.txt|g" \
  "$B2/R13M_BLIND.sigma"
BC="$B2/R13M_BLIND_$(date +%Y%m%d_%H%M%S).sigmab"
printf '<<< SIGMA/TMUX BEGIN >>>\n'
./native/sigmac "$B2/R13M_BLIND.sigma" "$BC" &&
./native/sigma-vm.v09_candidate "$BC"
echo "RC=$?"
printf '<<< SIGMA/TMUX END >>>\n'
```

Do not add a label telling the model which side is correct.
Do not update model weights during Blind 002.

---

# Command templates for future windows

## 1. Verify exact Native VM09 and compiler

```bash
printf '<<< SIGMA/TMUX BEGIN >>>\n'
sha256sum ./native/sigmac
sha256sum ./native/sigma-vm.v09_candidate
printf '<<< SIGMA/TMUX END >>>\n'
```

Expected:

```text
SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM09=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## 2. Compile and run a shadow SIGMA program

```bash
BC="$SH/<NAME>_$(date +%Y%m%d_%H%M%S).sigmab"
printf '<<< SIGMA/TMUX BEGIN >>>\n'
./native/sigmac "$SH/<NAME>.sigma" "$BC" &&
./native/sigma-vm.v09_candidate "$BC"
echo "RC=$?"
printf '<<< SIGMA/TMUX END >>>\n'
```

## 3. Run one additional checkpointed native self-learning tick

Only when the current mechanism is still accepting non-regressive updates:

```bash
printf '<<< SIGMA/TMUX BEGIN >>>\n'
./native/sigma-vm.v09_candidate "$BC"
echo "RC=$?"
printf '<<< SIGMA/TMUX END >>>\n'
```

If two consecutive ticks report:

```text
UPDATE_KEPT=0
```

stop that mechanism and change architecture.

## 4. Check persistence without scanning

```bash
H="$SH/history.csv"
printf '<<< SIGMA/TMUX BEGIN >>>\n'
echo -n "UPDATES_SAVED="; wc -l < "$H"
tail -5 "$H"
printf '<<< SIGMA/TMUX END >>>\n'
```

READ and WRITE paths inside the SIGMA program must match exactly.

## 5. Bound output

```bash
printf '<<< SIGMA/TMUX BEGIN >>>\n'
<command> | head -50
printf '<<< SIGMA/TMUX END >>>\n'
```

## 6. Find one exact file — no broad scan

```bash
find <KNOWN_ROOT> -type f -name '<EXACT_NAME>' -print -quit
```

Use only when the exact desired file/path is known.

## 7. Exact code excerpt <= 50 lines

```bash
sed -n '<START>,<END>p' <EXACT_FILE>
```

or:

```bash
grep -n -m20 -E '<EXACT_PATTERN>' <EXACT_FILE>
```

Do not dump whole binaries/source trees.

## 8. Blind-test rule

Blind files must be frozen before inference:

```bash
sha256sum "$B/story.txt" "$B/interpretations.txt"
```

Then inference must declare:

```text
MODEL_UPDATE=NO
ORACLE_VISIBLE=NO
EXECUTION_AUTHORITY=NATIVE_VM09
```

No answer label may be inserted into the model input.

## 9. Shadow-to-SIGMA ownership rule

Do **not** promote based on training metrics.

Promotion sequence:

```text
shadow mechanism works
-> multiple frozen blind tests generalize
-> no A/B position bias
-> no regression on existing SIGMA abilities
-> native SIGMA verdict/evidence
-> explicit admission
-> transfer only the demonstrated mechanism/weights
-> canonical verification receipt
```

---

# How other windows should divide work

If multiple windows work in parallel, each must have its own granted session and artifact root. Do not share a live writer/session code.

Recommended roles:

### Window A — Current deep-semantic learning owner

Continue from this checkpoint. Immediate task: Blind 002, then design next architecture only if generalization remains insufficient.

### Window B — Blind evaluation only

May create additional **frozen unseen whole-document semantic tests**. It must not expose oracle labels to the learning window/model before inference. Prefer balanced answer-position tests and paraphrase/adversarial controls.

### Window C — Regression / existing capability protection

Check that any candidate proposed for ownership does not damage long-document summary, native execution, deterministic/runtime invariants, or previously established capabilities. No semantic training decisions.

### Window D — Candidate tool engineering

May build generic substrate/tools in a candidate copy if necessary, but candidate VM results are non-authoritative until the mechanism is exercised through the approved native SIGMA path. Generic tools must not encode answers, story rules, semantic labels, or test-specific knowledge.

All windows must preserve receipts and use native SIGMA for semantic verdicts.

---

# What NOT to do after reading this checkpoint

Do not spend time rediscovering:

- the universal session protocol
- VM09 hash
- compiler hash
- canonical head/model hash
- whether R9/R10/R11/R14/R15/R16/R17 worked
- why R12 persistence initially failed
- whether R13M preserves mean weight
- whether Blind 001 was already run

Those facts are recorded above.

Do not repeat the rejected token/left-right/next-line approaches.

Do not claim a mechanism is successful because it builds or because training metrics move.

Do not promote R13M yet. Blind generalization is incomplete and Blind 002 is still pending.

---

# Immediate next checkpoint condition

Create a new checkpoint when one of these occurs:

1. Blind 002 completes.
2. A new shadow mechanism materially beats R13M on multiple frozen blind tests.
3. A candidate becomes eligible for explicit admission / SIGMA ownership.
4. The active session/window is about to close.

Each checkpoint must record:

```text
session/task
canonical baseline
VM/compiler hashes
shadow path
history/model hashes
frozen blind hashes
latest native outputs
failed/rejected approaches
exact next command
```

This file is the authoritative human-readable resume note for this workstream as of 2026-09-17.
