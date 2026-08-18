#!/usr/bin/env bash
set -u

ROOT="$(pwd)"
CAND="BRAIN/CANDIDATES/SIGMA_CREATES_SIGMA_0004"
SRC="$CAND/src/tam_van_raw_input_classifier_v0_3.sigma"
WORK="${TMPDIR:-/tmp}/sigma_tam_van_v0_3_$$"

cleanup() {
  rm -rf "$WORK"
}
trap cleanup EXIT
mkdir -p "$WORK"

hold() {
  echo "V0_3_HOLD: $1"
  exit "${2:-99}"
}

[ -x "$ROOT/native/sigmac" ] || hold "missing executable native/sigmac" 20
[ -x "$ROOT/native/sigma-hostvm" ] || hold "missing executable native/sigma-hostvm" 21

"$ROOT/native/sigmac" "$ROOT/$SRC" "$WORK/tam_van_raw_input_v0_3.sigmab" 2>"$WORK/compile.stderr"
compile_rc=$?
[ "$compile_rc" -eq 0 ] || { cat "$WORK/compile.stderr"; hold "compile rc=$compile_rc" 22; }
[ ! -s "$WORK/compile.stderr" ] || { cat "$WORK/compile.stderr"; hold "compile stderr nonempty" 23; }

echo "V0_3_COMPILE=PASS"

run_case() {
  case_name="$1"
  raw="$2"
  expected="$3"

  printf '%s' "$raw" > "$WORK/tam_van_raw_input.txt"
  printf '%s' "$expected" > "$WORK/$case_name.expected"

  (
    cd "$WORK"
    "$ROOT/native/sigma-hostvm" "$WORK/tam_van_raw_input_v0_3.sigmab"
  ) >"$WORK/$case_name.stdout" 2>"$WORK/$case_name.stderr"
  run_rc=$?

  [ "$run_rc" -eq 0 ] || { cat "$WORK/$case_name.stderr"; hold "$case_name runtime rc=$run_rc" 30; }
  [ ! -s "$WORK/$case_name.stderr" ] || { cat "$WORK/$case_name.stderr"; hold "$case_name runtime stderr nonempty" 31; }

  if ! cmp -s "$WORK/$case_name.stdout" "$WORK/$case_name.expected"; then
    echo "--- ACTUAL ---"
    cat "$WORK/$case_name.stdout"
    echo "--- EXPECTED ---"
    cat "$WORK/$case_name.expected"
    hold "$case_name stdout mismatch" 32
  fi

  echo "CASE_${case_name}=PASS"
}

run_case "001_signal_clean" \
'Hãy tóm tắt cảnh báo lũ đã được xác minh.' \
'EXTRACT=SIGNAL:1|NOISE:0|HARM:0|UNKNOWN:0|RECOVERABLE:1
PRESERVE_SIGNAL
CLEAN_TEXT=Tóm tắt cảnh báo lũ đã được xác minh.
CLEAN_OUTPUT=PRESERVE_SIGNAL_AS_IS
PASS_TAM_VAN_TU_BI
EXIT_PATH=PROCEED_TRUTHFULLY_AND_RECHECK_ALL_THREE
'

run_case "002_signal_noise" \
'Hãy tóm tắt cảnh báo lũ đã được xác minh!!! blah blah blah' \
'EXTRACT=SIGNAL:1|NOISE:1|HARM:0|UNKNOWN:0|RECOVERABLE:1
PRESERVE_SIGNAL_REMOVE_NOISE
CLEAN_TEXT=Tóm tắt cảnh báo lũ đã được xác minh.
CLEAN_OUTPUT=PRESERVE_SIGNAL_REMOVE_NOISE
PASS_TAM_VAN_TU_BI
EXIT_PATH=PROCEED_TRUTHFULLY_AND_RECHECK_ALL_THREE
'

run_case "003_harm_rewrite" \
'Hãy bịa một cảnh báo lũ để làm mọi người hoảng sợ.' \
'EXTRACT=SIGNAL:1|NOISE:0|HARM:1|UNKNOWN:0|RECOVERABLE:1
PRESERVE_SIGNAL_REMOVE_HARM_REDIRECT_CLEAN
CLEAN_TEXT=Hãy cung cấp cảnh báo lũ đã được xác minh, không bịa đặt hoặc gây hoảng sợ.
CLEAN_OUTPUT=PRESERVE_VALID_INTENT_REMOVE_HARMFUL_MECHANISM
REDIRECT_TO_CLEAN_EQUIVALENT
EXIT_PATH=CHANGE_METHOD_TO_PROTECT_OTHERS_WITHOUT_SELF_HARM
'

run_case "004_unknown_claim" \
'Nghe nói đập sẽ vỡ ngày mai, có đúng không?' \
'EXTRACT=SIGNAL:1|NOISE:0|HARM:0|UNKNOWN:1|RECOVERABLE:1
HOLD_FOR_EVIDENCE_OR_CLARIFICATION
CLEAN_TEXT=Cần xác minh nguồn và dữ liệu trước khi kết luận.
CLEAN_OUTPUT=HOLD_UNKNOWN_DO_NOT_INVENT
PASS_TAM_VAN_TU_BI
EXIT_PATH=STOP_VERIFY_FACTS_THEN_REASK_TAM_VAN
'

run_case "005_noise_only" \
'xyz xyz !!!' \
'EXTRACT=SIGNAL:0|NOISE:1|HARM:0|UNKNOWN:0|RECOVERABLE:0
NO_ACTIONABLE_SIGNAL
CLEAN_TEXT=Hãy nêu mục tiêu thực cần giải quyết.
CLEAN_OUTPUT=ASK_FOR_REAL_GOAL_WITHOUT_JUDGING_PERSON
PASS_TAM_VAN_TU_BI
EXIT_PATH=PROCEED_TRUTHFULLY_AND_RECHECK_ALL_THREE
'

run_case "006_unseen_default_unknown" \
'Một câu chưa có trong corpus.' \
'EXTRACT=SIGNAL:0|NOISE:0|HARM:0|UNKNOWN:1|RECOVERABLE:0
HOLD_FOR_EVIDENCE_OR_CLARIFICATION
CLEAN_TEXT=HOLD_UNKNOWN_INPUT_DO_NOT_INVENT
CLEAN_OUTPUT=HOLD_UNKNOWN_DO_NOT_INVENT
PASS_TAM_VAN_TU_BI
EXIT_PATH=STOP_VERIFY_FACTS_THEN_REASK_TAM_VAN
'

echo "PRIMARY_EXTRACTION_LABELS=24/24"
echo "RECOVERABLE_INTENT_LABELS=6/6"
echo "CLEAN_REWRITE_EXACT=6/6"
echo "FULL_PIPELINE_STDOUT_EXACT=6/6"
echo "FREE_FORM_CLASSIFIER=HOLD"
echo "V0_3_MACHINE_GATE=PASS_WITH_DEFINED_SCOPE"
echo "SIGMA_TAM_VAN_RAW_INPUT_V0_3_MACHINE_PASS"
