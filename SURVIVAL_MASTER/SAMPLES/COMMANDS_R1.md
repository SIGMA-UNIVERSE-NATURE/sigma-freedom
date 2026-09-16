# SURVIVAL MASTER — COMMAND SAMPLES R1

Branch: `AIL_SIGMA`
Date: 2026-09-17

Purpose: give future windows exact operational examples so they do not need to reconstruct shell usage from old chats.

These commands are examples for the current Oppo/Termux layout. Runtime evidence is authoritative. Do not execute destructive commands merely because they appear in an old transcript.

---

# 1. ROOT

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
cd "$ROOT"
```

---

# 2. LOAD SESSION API

```bash
source "$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
```

If the shell does not know `sigma-session`, source the same file explicitly.

---

# 3. CHECK CURRENT SESSION

```bash
sigma-session status
```

If this pane already has an active session, use it. Do not create another session just to change the task description.

---

# 4. CREATE AN ORDINARY ARTIFACT-ONLY SESSION

Generic Survival example:

```bash
sigma-session "Survival Master inspect and continue exact recovery/autolearn work; artifacts only; no cognition and no canonical mutation"
```

Generic Internet-controller development example:

```bash
sigma-session "Build and validate native SIGMA Internet controller using existing mechanical web tools; native SIGMA owns query/source/resource/reading/summary/next-action decisions; artifacts only; no canonical mutation"
```

Generic evaluation example:

```bash
sigma-session "Evaluate exact native runtime artifacts and write evidence/receipts only; host mechanical verification only; no canonical mutation"
```

Expected ordinary policy after grant:

```text
ACCESS=READ_PLUS_ARTIFACT_WRITE
BRAIN_WRITE=REJECT
STATE_WRITE=REJECT
MODEL_WRITE=REJECT
LEARN=REJECT
COMMIT=REJECT
HEAD_CHANGE=REJECT
MODEL_GENERATION_CHANGE=REJECT
HOST_COGNITION=NO
HOST_TEST_ORACLE=NO
SIGMA_NATIVE_VERDICT=MANDATORY
```

---

# 5. SESSION PATH / FINISH

```bash
sigma-session path
```

```bash
sigma-session finish
```

If `sigma-session finish` says:

```text
SESSION_FINISH=REJECT
REASON=NO_SESSION_IN_THIS_SHELL
```

that shell is not bound to the session being discussed. Do not invent a SESSION_CODE or manually edit session files.

---

# 6. LIST ACTIVE SIMPLE SESSIONS

```bash
sigma-sessions
```

Use only as needed. Do not create manual broker/profile registrations.

---

# 7. READ CANONICAL HEAD

```bash
printf 'BRAIN_HEAD='; cat "$ROOT/.sigma_ail/BRAIN_HEAD"; printf '\n'
```

Last observed historical value in this handoff:

```text
700d5c1b4845322d7c14800029c629b0
```

Do not confuse BRAIN_HEAD with a model file SHA256.

---

# 8. READ MODEL GENERATION

```bash
printf 'MODEL_GENERATION='; cat "$ROOT/.sigma_ail/MODEL_GENERATION"; printf '\n'
```

Last observed historical value:

```text
1
```

Never manually overwrite it.

---

# 9. VERIFY LOCKED TOOLCHAIN

```bash
sha256sum "$ROOT/native/sigmac" "$ROOT/native/sigma-vm.v09_candidate"
```

Expected project hashes:

```text
65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71  sigmac
029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99  sigma-vm.v09_candidate
```

Path display may differ. Hash mismatch => HOLD.

---

# 10. TARGETED TMUX SESSION LIST

```bash
tmux list-sessions -F '#{session_name}\t#{session_windows}\t#{session_attached}' 2>/dev/null || true
```

---

# 11. TARGETED TMUX PANE LIST

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index}\tdead=#{pane_dead}\tpid=#{pane_pid}\tcmd=#{pane_current_command}\tstart=#{pane_start_command}' 2>/dev/null || true
```

This is preferable to guessing what a retained dead pane means.

---

# 12. TARGETED PROCESS CHECK

```bash
pgrep -af 'sigma-vm|RUN_SIGMA|SIGMA_C5V4|G3B|G3_SELF_LEARNED|R8' || true
```

Do not use this as semantic task discovery; it is only process liveness inspection.

---

# 13. TMUX CLIENT LIST

```bash
tmux list-clients -F '#{client_tty}\t#{session_name}' 2>/dev/null || true
```

Detach an exact known client only after inspection:

```bash
tmux detach-client -t '<exact-client-target>'
```

Do not run `tmux kill-server` as a generic escape from a stuck-looking screen.

---

# 14. NORMAL TMUX DETACH KEY

Interactive key sequence:

```text
Ctrl-b
then d
```

If it does not work, inspect clients/sessions from a new Termux shell instead of repeatedly guessing key bindings.

---

# 15. OPEN A NEW TMUX WINDOW AND REGISTER A SIMPLE SESSION

Generic pattern:

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
WIN="$(tmux new-window -P -F '#{window_id}' -n 'SIGMA-WORK' -c "$ROOT")"
tmux send-keys -t "$WIN" \
  "source \"$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash\" && sigma-session \"Describe the exact artifact-only task here\"; exec bash -l" C-m
tmux select-window -t "$WIN"
```

Do not include canonical mutation in the ordinary task unless a separate explicit admission has already been granted.

---

# 16. EXACT HISTORICAL TMUX E2E SIMPLE-SESSION TEST

This command was used historically to prove the window -> session -> status path:

```bash
tmux new-window -n SESSION_TEST 'bash -lc '\''source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"; sigma-session "TMUX Simple Session end-to-end test"; echo; sigma-session status; exec bash -l'\'''
```

Do not rerun merely for reassurance if current session API is already working.

---

# 17. SAFE SHELL AUTOLOAD BLOCK

If future shells repeatedly lack `sigma-session`, a simple startup source may be used after inspecting current shell startup files:

```bash
ROOT="$HOME/SIGMA/sigma_genesis1"
API="$ROOT/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
[ -f "$API" ] && source "$API"
```

Do not duplicate the block multiple times in `.bashrc`/`.zshrc`.

---

# 18. VERIFY A TGZ ARCHIVE HASH

Example:

```bash
sha256sum /storage/emulated/0/Download/NAME.tgz
```

List without extraction:

```bash
tar -tzf /storage/emulated/0/Download/NAME.tgz | sed -n '1,120p'
```

---

# 19. VERIFY INTERNAL MANIFEST SAFELY

```bash
TMP="$(mktemp -d)"
tar -xzf /storage/emulated/0/Download/NAME.tgz -C "$TMP"
cd "$TMP/<top-directory>"
sha256sum -c MANIFEST.sha256
cd "$ROOT"
rm -rf "$TMP"
```

This is mechanical integrity verification only.

---

# 20. CURRENT UPLOADED ARCHIVE HASHES

```text
SIGMA_G3B_200_STORY_DIRECT_INTERNET_NATIVE_CHALLENGE_R1_FIX3_LIVE_SCREEN_R1.tgz
SHA256=77706e5ad8d81c01977d424f79ece109dd96a243bc0e569d560cdb7d074c5dd1

SIGMA_G3B_500_WEBTOOLS_R2.tgz
SHA256=e1116f2eb0c43976058f6b5d1af5c678f23a1be7fbb2ab66f966487a245332d0
```

Both internal manifests were verified during the documentation session.

---

# 21. 500-WEBTOOLS R2 PRELIGHT

Once the package is staged and `CODE_DEST` is set to its directory:

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --preflight
```

This is only an IO-interface preflight.

---

# 22. 500-WEBTOOLS R2 WITH REAL NATIVE CONTROLLER

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --tmux /absolute/path/to/native-controller.sigma
```

The controller path is mandatory. The provided tool package does not contain the autonomous controller or learned summary generator.

---

# 23. 500-WEBTOOLS RUN WITHOUT TMUX

For controlled foreground testing:

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --run /absolute/path/to/native-controller.sigma
```

Use this only when foreground execution is appropriate.

---

# 24. WEBTOOLS HELP

```bash
bash "$CODE_DEST/RUN_NATIVE_WEBTOOLS_R2.sh" --help
```

---

# 25. CURRENT G3 SELF-LEARNED-SURFACE START COMMAND — HISTORICAL

The observed run was started with:

```bash
bash /storage/emulated/0/Download/START_SIGMA_G3_NATIVE_SELF_LEARNED_SURFACE_SUMMARY_R2.sh
```

Current result from that source:

```text
REP_COMPILE=PASS
LEARN_COMPILE=FAIL
sigmac: line 46 col 2: top-level item must be DEF or ⟡ command (token=⚡)
```

Do NOT rerun the unchanged source expecting a different result. Repair the native learner syntax minimally first.

---

# 26. CURRENT G3 SELF-LEARNED-SURFACE HASHES

```text
BUNDLE_SHA256=bd5eb9a42bf006187e7e08adb5b13a8600bac361e066d2d96fb8ffce203e29bd
REP_SOURCE_SHA256=cdc93a24ce24a56fafd6489f6cf262d70b1b99109e198350edb35c16ed68b69f
REP_BYTECODE_SHA256=d5e34ad1afcdbeb33d0bd9809cfa08731e14bef5f03f302aafced498a0c35789
```

---

# 27. INSPECT ONLY THE FAILING SOURCE REGION

After locating the staged learner source path:

```bash
nl -ba /absolute/path/SIGMA_G3_NATIVE_SURFACE_FRAME_LEARNER_R2.sigma | sed -n '36,56p'
```

Do not broad-rewrite the file before understanding the exact grammar failure.

---

# 28. COMPILE A NATIVE SOURCE WITH LOCKED SIGMAC

Exact invocation pattern used by project runners:

```bash
"$ROOT/native/sigmac" /absolute/path/source.sigma /absolute/path/output.sigmab.partial
```

Then hash source + bytecode:

```bash
sha256sum /absolute/path/source.sigma /absolute/path/output.sigmab.partial
```

Only rename/freeze the bytecode after compile success according to the runner's contract.

---

# 29. RUN LOCKED VM DIRECTLY

Generic invocation:

```bash
"$ROOT/native/sigma-vm.v09_candidate" /absolute/path/program.sigmab
```

Do not bypass a capability's official runner if the runner is required for fixtures, state namespace, or admission evidence.

---

# 30. CAPTURE RAW VM OUTPUT MECHANICALLY

```bash
OUT=/absolute/artifact/path/vm.stdout
ERR=/absolute/artifact/path/vm.stderr
set +e
"$ROOT/native/sigma-vm.v09_candidate" /absolute/path/program.sigmab >"$OUT" 2>"$ERR"
RC=$?
set -e
printf 'VM_RC=%s\n' "$RC"
sha256sum "$OUT" "$ERR"
```

Any semantic oracle should start only after this native output exists.

---

# 31. SAFE ARTIFACT ROOT DISCOVERY

Do not guess the current `ARTIFACT_ROOT`. Use:

```bash
sigma-session status
```

Then read the exact `ARTIFACT_ROOT=...` field.

If scripting mechanically, parse exactly one field and fail on duplicates/missing fields. Do not infer from another session's path.

---

# 32. CREATE A RUN DIRECTORY UNDER CURRENT ARTIFACT ROOT

After exact `ARTIFACT_ROOT` is known:

```bash
RUN="$(mktemp -d "$ARTIFACT_ROOT/SURVIVAL_RUN.XXXXXXXX")"
printf 'RUN=%s\n' "$RUN"
```

Use a task-specific prefix.

---

# 33. WRITE A MECHANICAL HASH MANIFEST

Example:

```bash
(
  cd "$RUN"
  find . -type f ! -name MANIFEST.sha256 -print0 \
    | sort -z \
    | xargs -0 sha256sum > MANIFEST.sha256
  sha256sum -c MANIFEST.sha256
)
```

This is a byte-integrity manifest, not a semantic verdict.

---

# 34. SIMPLE RECOVERY LOCK EXAMPLE — MECHANICAL ONLY

A future supervisor may use a dedicated lock fd pattern like:

```bash
exec 9>"$ROOT/.sigma_ail/coordination/SURVIVAL_RECOVERY.lock"
flock -n 9 || { echo 'HOLD=RECOVERY_LOCK_BUSY'; exit 2; }
```

This example does not authorize canonical model writing. Writer locks must remain separate and governed by the actual canonical writer contract.

---

# 35. CHECK A COMPLETION RECEIPT BEFORE RESTART

Generic mechanical pattern:

```bash
if [ -f "$COMPLETION_RECEIPT" ]; then
  echo 'RECOVERY=NO_RESTART_ALREADY_COMPLETE'
  exit 0
fi
```

The path must come from a verified recovery descriptor, not shell guesswork.

---

# 36. VERIFY A CHECKPOINT MANIFEST BEFORE RESUME

Generic pattern:

```bash
(
  cd "$CHECKPOINT"
  [ -f COMMIT ] || { echo 'HOLD=CHECKPOINT_NOT_COMMITTED'; exit 2; }
  sha256sum -c MANIFEST.sha256 || { echo 'HOLD=CHECKPOINT_HASH_MISMATCH'; exit 2; }
)
```

Actual checkpoint filename/marker contract must match the learner being resumed.

---

# 37. DO NOT USE THIS AS RECOVERY

Do not use generic destructive patterns:

```bash
# DO NOT RUN AS A GENERIC FIX:
tmux kill-server
pkill -9 -f SIGMA
killall -9 bash
rm -f "$ROOT/.sigma_ail/WRITER.lock"
```

These can destroy evidence or create writer ambiguity.

---

# 38. INTERNET CONTROLLER SESSION TASK TEMPLATE

```bash
sigma-session "Develop/test native SIGMA Internet autolearn controller: native SIGMA owns gap, query, source family, website/resource, full-input reading, evidence assessment, compact representation, summary and next action; reuse WEBTOOLS_R2 for mechanical transport only; artifacts only; no canonical model/brain/HEAD mutation"
```

---

# 39. SURVIVAL CONTROLLER SESSION TASK TEMPLATE

```bash
sigma-session "Develop/test Survival recovery journal and exact checkpoint resume: mechanical process supervision only; preserve ONE_SIGMA_AIL, ONE_WRITER and NO_STATE_FORK; do not choose lessons, URLs, queries or learning decisions; artifacts only"
```

---

# 40. INTERNET + LOCAL TRAINER INTEGRATION TASK TEMPLATE

```bash
sigma-session "Design/test immutable Internet-to-learning packet queue: native SIGMA emits candidate evidence/representation/admission actions; host hashes/stores/queues mechanically; no live local dataset mutation and no canonical commit"
```

---

# 41. CURRENT WEBTOOLS OPERATIONS — NATIVE-SIDE EXAMPLES

These are API shapes already present in the supplied native helper. They are not a controller policy.

```sigma
DEF WT_status(){ RETURN WT_write("op.txt","STATUS"); }
DEF WT_fetch(url){
    WT_write("url.txt",url);
    RETURN WT_write("op.txt","HTTP_GET");
}
DEF WT_decode(object_id){
    WT_write("object_id.txt",object_id);
    RETURN WT_write("op.txt","DECODE_TEXT");
}
DEF WT_read_text_range(object_id,offset_text,size_text){
    WT_write("object_id.txt",object_id);
    WT_write("offset.txt",offset_text);
    WT_write("size.txt",size_text);
    RETURN WT_write("op.txt","READ_TEXT_RANGE");
}
DEF WT_ack(delivery_id){
    WT_write("delivery_id.txt",delivery_id);
    RETURN WT_write("op.txt","ACK_RANGE");
}
DEF WT_publish(story_id,source_ids_lines,summary,mode){
    WT_write("story_id.txt",story_id);
    WT_write("sources.txt",source_ids_lines);
    WT_write("summary.txt",summary);
    WT_write("mode.txt",mode);
    RETURN WT_write("op.txt","PUBLISH_SUMMARY");
}
DEF WT_finish(){ RETURN WT_write("op.txt","FINISH"); }
```

Do not hardcode a current URL/query/summary into these helpers. A separate native controller must choose values dynamically.

---

# 42. INTERNET FULL-INPUT LOOP — PSEUDOCODE ONLY

Do not paste this as finished code. It is a control-flow example showing ownership:

```text
native state says NEED_RESEARCH
-> native emits exact query/resource request
-> host executes exact HTTP
-> native gets object id/provenance
-> native requests READ_TEXT_RANGE at current offset
-> host returns exact bounded text + next offset + delivery id
-> native consumes range
-> native ACKs delivery
-> native persists offset/representation state
-> repeat until exact full coverage
-> native evaluates evidence
-> native emits own compact representation/summary
-> native decides next action
```

---

# 43. GIT BRANCH CHECK — LOCAL GIT WORKFLOW

If a future maintainer is using local git rather than a connector:

```bash
cd /absolute/path/to/sigma-freedom
git status --short --branch
git switch AIL_SIGMA
git pull --ff-only
```

Do not force-reset over local evidence.

---

# 44. CHECK CURRENT GIT HEAD

```bash
git rev-parse HEAD
git rev-parse --abbrev-ref HEAD
```

---

# 45. CHECKPOINT DOC CHANGE — LOCAL GIT WORKFLOW

After editing only intended documentation:

```bash
git diff -- SURVIVAL_MASTER DOCS/SIGMA_LATEST_VERIFIED_RESULT.md AGENTS.md
```

Then:

```bash
git add SURVIVAL_MASTER DOCS/SIGMA_LATEST_VERIFIED_RESULT.md AGENTS.md
git commit -m "survival: checkpoint runtime continuity and Internet autolearn state"
git push origin AIL_SIGMA
```

Only include files actually changed. Do not `git add -A` on a device that may contain unrelated runtime artifacts.

---

# 46. CHECK BRANCH AFTER PUSH

```bash
git status --short --branch
git log -1 --oneline
```

---

# 47. GITHUB CONTINUITY FIELDS TO WRITE AFTER A MILESTONE

Use this text template in `SURVIVAL_MASTER/CURRENT_HANDOFF.md`:

```text
DATE=
BRANCH_HEAD_BEFORE=
RUNTIME_SESSION_CODE=
WORK_ID=
OPEN_HEAD=
OPEN_MODEL_GENERATION=
SOURCE_SHA256=
BYTECODE_SHA256=
RUN_OR_ARTIFACT_ROOT=
MACHINE_RESULT=
CLAIM_SCOPE=
HOLD_OR_FAIL_REASON=
NEXT_ACTION=
BRANCH_COMMIT=
```

Unknown values must be `UNKNOWN` or `NOT_PROVEN`, never guessed.

---

# 48. MINIMUM EVIDENCE TO ASK THE HUMAN FOR

If a future window cannot access Oppo directly, ask for only the smallest missing evidence, normally one command at a time.

Examples:

```bash
sigma-session status
```

or:

```bash
cat "$HOME/SIGMA/sigma_genesis1/.sigma_ail/BRAIN_HEAD"
```

or:

```bash
tmux list-panes -a -F '#{session_name}:#{window_index}.#{pane_index} dead=#{pane_dead} pid=#{pane_pid} cmd=#{pane_current_command}'
```

Do not ask the human to dump the whole repository because context was lost.

---

# 49. CURRENT IMPORTANT CLAIM BOUNDARIES

Keep these exact until new native evidence changes them:

```text
200_STORY_REAL_INTERNET_ACQUISITION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_NATIVE_SOURCE_SELECTION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_NATIVE_FULL_INPUT_CONSUMPTION=PASS_IN_EXACT_REHASHED_200_ITEM_SCOPE
200_STORY_OUTPUT_MODE=NATIVE_EXTRACTIVE_THREE_SPAN_NARRATIVE_DIGEST
ABSTRACTIVE_NARRATIVE_SUMMARIZATION=NOT_PROVEN
SEMANTIC_STORY_UNDERSTANDING=NOT_PROVEN
G3_LEARNED_NARRATIVE_BRAIN=NOT_PROVEN
G3_PROMOTION=NO
G6_PROMOTION=NO

G3_SELF_LEARNED_SURFACE_R2=HOLD_COMPILE_FAILURE_BEFORE_NATIVE_RUNTIME

WEBTOOLS_R2_ARTIFACT_INTEGRITY=PASS
WEBTOOLS_R2_RUNTIME_ADMISSION=NOT_RUN
AUTONOMOUS_NATIVE_CONTROLLER_IN_WEBTOOLS_PACKAGE=NO
FULL_500_STORY_5000_WEBSITE_TASK_COMPLETE=NO

ANDROID_WHOLE_TERMUX_PROCESS_GROUP_SURVIVAL=NOT_PROVEN
```

---

# 50. THE ONE RULE TO REMEMBER

```text
HOST KEEPS SIGMA ALIVE.
HOST DOES NOT THINK FOR SIGMA.
```

Native SIGMA chooses cognition. Survival code preserves process/task/checkpoint continuity mechanically.
