#!/data/data/com.termux/files/usr/bin/bash
set -u
set -o pipefail
umask 077

P=/data/data/com.termux/files/usr
HOME_SIGMA=/data/data/com.termux/files/home/SIGMA
REPO="${SIGMA_REPO:-$HOME_SIGMA/sigma-freedom-write}"
SIGMAC="$HOME_SIGMA/sigma_genesis1/native/sigmac"
VM="$HOME_SIGMA/sigma_genesis1/native/sigma-vm.v09_candidate"

EXPECTED_SIGMAC=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
EXPECTED_VM=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
EXPECTED_VNM01_SOURCE=cd399793ebde7e5dfa4a10cf263bb97fd45d1379ce8dac02520d5277cf2ca788
EXPECTED_VNM01_BYTECODE=df323de291828d11cc7e46655f2ff5fbc326297200b1782f4c0c441389a27586
EXPECTED_VNM04_SOURCE=9b2795403157617b4b1ae15baeaa60adce3deb59f2fdd7174a8b3182f1d3a7d0
EXPECTED_VNM04_BYTECODE=352f7c848001e03cce0c7481c06987a324b13fdb54a96004eb714e3c62e831ef
EXPECTED_VNM07_SOURCE=8412ce07e6c9a53ae6bb27a88ec2847eadd54795a21dce35a3ff1ef29f75a57e
EXPECTED_VNM07_BYTECODE=50be8bc9fd4cf46f9d348d9eb72b19d9e90209af0e2f4f61649828fb1507a42b
EXPECTED_VNM07_RUNNER=ef2fe0776de85622b737a9161b4959ff4b6bba28832ac483a6a129d42463327a

SRC01="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_01_NATIVE_SURFACE_FORM_EVIDENCE_WEIGHTING_V1.sigma"
SRC04="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_04_NATIVE_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1.sigma"
SRC07="$REPO/SIGMA_PROFESSOR/artifacts/SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1.sigma"
RUN07="$REPO/SIGMA_PROFESSOR/artifacts/RUN_SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_PREFLIGHT.sh"

ROOT="$HOME_SIGMA/SIGMA_VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT"
CASES="$ROOT/cases"
LOG="$ROOT/log"
LOCK="$ROOT/preflight.lock"
BC01="$ROOT/VNM01.sigmab"
BC04="$ROOT/VNM04.sigmab"
V7ROOT="$HOME_SIGMA/SIGMA_VNM_07_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1_PREFLIGHT"

mkdir -p "$ROOT" "$LOG"
exec 9>"$LOCK"
"$P/bin/flock" -n 9 || { printf 'HOLD=VNM_08_PREFLIGHT_ALREADY_RUNNING\n'; exit 20; }
sha_of(){ "$P/bin/sha256sum" "$1" | "$P/bin/awk" '{print $1}'; }

sigmac_sha=$(sha_of "$SIGMAC"); vm_sha=$(sha_of "$VM")
s01=$(sha_of "$SRC01"); s04=$(sha_of "$SRC04"); s07=$(sha_of "$SRC07"); r07=$(sha_of "$RUN07")
printf 'SIGMA_PHASE=VNM_08_HIERARCHICAL_SPAN_FORM_WEIGHTING_INTEGRATION_PREFLIGHT\n'
printf 'INTEGRATION_ONLY_STAGE=YES\nNEW_NATIVE_SOURCE_REQUIRED=NO\n'
printf 'REUSED_VNM07_FULL_SUBSUITE=YES\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\nHOST_PAIR_GENERATION=NO\nHOST_PAIR_SELECTION=NO\nHOST_EVIDENCE_GENERATION=NO\nHOST_WEIGHT_UPDATE=NO\nHOST_LEARNING=NO\nHOST_SEMANTIC_INTERPRETATION=NO\nHOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SIGMAC_SHA256=%s\nVM_SHA256=%s\n' "$sigmac_sha" "$vm_sha"
[ "$sigmac_sha" = "$EXPECTED_SIGMAC" ] || { printf 'HOLD=SIGMAC_IDENTITY_MISMATCH\n'; exit 21; }
[ "$vm_sha" = "$EXPECTED_VM" ] || { printf 'HOLD=VM_IDENTITY_MISMATCH\n'; exit 22; }
[ "$s01" = "$EXPECTED_VNM01_SOURCE" ] || { printf 'HOLD=VNM01_SOURCE_IDENTITY_MISMATCH\n'; exit 23; }
[ "$s04" = "$EXPECTED_VNM04_SOURCE" ] || { printf 'HOLD=VNM04_SOURCE_IDENTITY_MISMATCH\n'; exit 24; }
[ "$s07" = "$EXPECTED_VNM07_SOURCE" ] || { printf 'HOLD=VNM07_SOURCE_IDENTITY_MISMATCH\n'; exit 25; }
[ "$r07" = "$EXPECTED_VNM07_RUNNER" ] || { printf 'HOLD=VNM07_RUNNER_IDENTITY_MISMATCH\n'; exit 26; }

compile_locked(){ src="$1"; out="$2"; label="$3"; "$P/bin/rm" -f -- "$out" "$out.partial"; "$SIGMAC" "$src" "$out.partial"; rc=$?; printf '%s_SIGMAC_RC=%s\n' "$label" "$rc"; [ "$rc" -eq 0 ] || exit 30; [ -s "$out.partial" ] || exit 31; "$P/bin/mv" -f -- "$out.partial" "$out" || exit 32; "$P/bin/chmod" 0400 "$out" || exit 33; }
# Freeze downstream bytecodes before the reused VNM-07 runner creates dynamic inputs.
compile_locked "$SRC01" "$BC01" VNM01
compile_locked "$SRC04" "$BC04" VNM04
b01=$(sha_of "$BC01"); b04=$(sha_of "$BC04")
printf 'VNM01_BYTECODE_SHA256=%s\nVNM04_BYTECODE_SHA256=%s\n' "$b01" "$b04"
[ "$b01" = "$EXPECTED_VNM01_BYTECODE" ] || { printf 'HOLD=VNM01_BYTECODE_IDENTITY_MISMATCH\n'; exit 34; }
[ "$b04" = "$EXPECTED_VNM04_BYTECODE" ] || { printf 'HOLD=VNM04_BYTECODE_IDENTITY_MISMATCH\n'; exit 35; }
S01_BEFORE="$s01"; S04_BEFORE="$s04"; B01_BEFORE="$b01"; B04_BEFORE="$b04"
printf 'VNM01_VNM04_FROZEN_BEFORE_VNM07_DYNAMIC_INPUT=YES\n'

# Re-run the exact admitted VNM-07 full suite; this natively produces two hierarchical FORM observation bundles and one VNM-02 candidate.
SUBLOG="$LOG/vnm07_full_subsuite.log"
bash "$RUN07" >"$SUBLOG" 2>&1
SUBRC=$?
printf '\n=== VNM07 FULL SUBSUITE ===\nSUBSUITE_RC=%s\n' "$SUBRC"
cat "$SUBLOG"
[ "$SUBRC" -eq 0 ] || { printf 'VNM_08_PREFLIGHT=FAIL\nFAILURE=VNM07_SUBSUITE_NONZERO\n'; exit 40; }
for line in \
'TOTAL_VM_INVOCATIONS=21' \
'VNM05_VM_INVOCATIONS=2' \
'VNM06_VM_INVOCATIONS=2' \
'VNM07_VM_INVOCATIONS=16' \
'VNM02_VM_INVOCATIONS=1' \
'POST_VM_ALIGNMENT_PASS_COUNT=16' \
'POST_VM_ALIGNMENT_FAIL_COUNT=0' \
'VM_NONZERO_COUNT=0' \
'STEP_LIMIT_HIT_COUNT=0' \
'NEGATIVE_PASS_COUNT=10' \
'INTEGRATION_PASS_COUNT=3' \
'COUNTERFACTUAL_PASS_COUNT=1' \
'REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES' \
'ORDERED_SPAN_SERIALIZATION_TEST=PASS' \
'DOWNSTREAM_VNM02_PAIR_INDUCTION_TEST=PASS' \
'VNM_07_PREFLIGHT=PASS' \
'ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE' \
'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES' \
'BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES' \
'UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT_IN_SOURCE_OR_BYTECODE=0' \
'HOST_FORM_SERIALIZATION=NO' \
'HOST_OBSERVATION_ID_DERIVATION=NO' \
'HOST_PAIR_GENERATION=NO' \
'HOST_PAIR_SELECTION=NO' \
'HOST_LEARNING=NO' \
'HOST_SEMANTIC_INTERPRETATION=NO' \
'HOST_SEMANTIC_SUBSTITUTION=NO'
do grep -F -x "$line" "$SUBLOG" >/dev/null || { printf 'VNM_08_PREFLIGHT=FAIL\nFAILURE=VNM07_SUBSUITE_GATE_MISSING\nEXPECTED=%s\n' "$line"; exit 41; }; done
V7BC="$V7ROOT/SIGMA_VNM_07_NATIVE_SPAN_OBSERVATION_TO_FORM_OBSERVATION_ADAPTER_V1.sigmab"
[ -f "$V7BC" ] || { printf 'HOLD=VNM07_BYTECODE_NOT_FOUND_AFTER_SUBSUITE\n'; exit 42; }
v7bc=$(sha_of "$V7BC")
printf 'VNM07_BYTECODE_SHA256=%s\n' "$v7bc"
[ "$v7bc" = "$EXPECTED_VNM07_BYTECODE" ] || { printf 'HOLD=VNM07_BYTECODE_IDENTITY_MISMATCH\n'; exit 43; }

OBS1="$V7ROOT/native_form_observations_1.memory"
OBS2="$V7ROOT/native_form_observations_2.memory"
PAIRLOG="$V7ROOT/log/INTEGRATION_VNM02_PAIR_VNM02.log"
[ -s "$OBS1" ] && [ -s "$OBS2" ] && [ -s "$PAIRLOG" ] || { printf 'HOLD=VNM07_NATIVE_INTEGRATION_OUTPUT_MISSING\n'; exit 44; }
status=$(awk '$1=="PAIR_CANDIDATE_STATUS" {sub(/^PAIR_CANDIDATE_STATUS /,""); printf "%s",$0; exit}' "$PAIRLOG")
fa=$(awk '$1=="PAIR_CANDIDATE_FORM_A" {sub(/^PAIR_CANDIDATE_FORM_A /,""); printf "%s",$0; exit}' "$PAIRLOG")
fb=$(awk '$1=="PAIR_CANDIDATE_FORM_B" {sub(/^PAIR_CANDIDATE_FORM_B /,""); printf "%s",$0; exit}' "$PAIRLOG")
support=$(awk '$1=="PAIR_CANDIDATE_SUPPORT" {sub(/^PAIR_CANDIDATE_SUPPORT /,""); printf "%s",$0; exit}' "$PAIRLOG")
[ "$status" = PAIR_CANDIDATE_INDUCED ] && [ "$support" = 2 ] && [ -n "$fa" ] && [ -n "$fb" ] || { printf 'VNM_08_PREFLIGHT=FAIL\nFAILURE=VNM02_NATIVE_CANDIDATE_DECODE_FAIL\n'; exit 45; }

rm -rf -- "$CASES"; mkdir -p "$CASES"
ADD_VM=0; V04_VM=0; V01_VM=0; VM_NONZERO=0; STEP_HIT=0; ALIGN=0; NEG=0; PERSIST=0; HIER_PASS=0; CASE_NAME=BOOT; LAST_LOG=""
fail(){ code="$1"; why="$2"; printf 'VNM_08_PREFLIGHT=FAIL\nFAILURE_CASE=%s\nFAILURE=%s\n' "$CASE_NAME" "$why"; exit "$code"; }
runvm(){ comp="$1"; box="$2"; bc="$3"; log="$4"; ADD_VM=$((ADD_VM+1)); [ "$comp" = VNM04 ] && V04_VM=$((V04_VM+1)); [ "$comp" = VNM01 ] && V01_VM=$((V01_VM+1)); (cd "$box" || exit 90; "$VM" "$bc") >"$log" 2>&1; rc=$?; printf '\n=== %s / %s ===\nVM_RC=%s\n' "$CASE_NAME" "$comp" "$rc"; cat "$log"; [ "$rc" -eq 0 ] || { VM_NONZERO=$((VM_NONZERO+1)); fail 50 VM_NONZERO; }; grep -F 'Step limit exceeded' "$log" >/dev/null 2>&1 && { STEP_HIT=$((STEP_HIT+1)); fail 51 STEP_LIMIT_HIT; }; LAST_LOG="$log"; }
expect(){ grep -F -x "$1 $2" "$LAST_LOG" >/dev/null || { printf 'EXPECTED=%s %s\n' "$1" "$2"; fail 60 MISSING_EXPECTED_OUTPUT; }; }
route_bundle(){ bundle="$1"; hyp="$2"; ev="$3"; awk 'NR==1 {printf "%s",$0}' "$bundle" > "$hyp"; awk 'NR>1 {if(n)printf "\n"; printf "%s",$0; n=1}' "$bundle" > "$ev"; }

CAND="$ROOT/native_pair_candidate.memory"
printf 'CANDIDATE||%s||FORM_A||%s||FORM_B||%s||SUPPORT||%s' "$status" "$fa" "$fb" "$support" > "$CAND"
OBS="$ROOT/hierarchical_form_observations.memory"
{ cat "$OBS1"; printf '\n'; cat "$OBS2"; } > "$OBS"

# Native VNM-04 consumes exact VNM-07 observations + native VNM-02 candidate.
CASE_NAME=HIERARCHICAL_VNM04
B4="$CASES/base04"; X4="$B4/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"; mkdir -p "$X4/input" "$X4/output"; cp "$CAND" "$X4/input/candidate.memory"; cp "$OBS" "$X4/input/observations.memory"; : > "$X4/output/vnm01_input_bundle.memory"; runvm VNM04 "$B4" "$BC04" "$LOG/base04.log"; expect SUPPORT_PAIR_COUNT 2; expect COMPETING_RAW_PAIR_COUNT 0; expect ELIGIBLE_EVIDENCE_COUNT 2; expect SUPPORT_MATCH 1; expect BRIDGE_STATUS BRIDGE_READY; ALIGN=$((ALIGN+1)); HIER_PASS=$((HIER_PASS+1))
BUNDLE="$X4/output/vnm01_input_bundle.memory"

# Native VNM-01 learns persistent +2 structural weight over the two hierarchical span forms.
CASE_NAME=HIERARCHICAL_VNM01
B1="$CASES/base01"; X1="$B1/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"; mkdir -p "$X1/input" "$X1/state"; : > "$X1/state/surface_form_weight_state.memory"; route_bundle "$BUNDLE" "$X1/input/hypothesis.memory" "$X1/input/evidence.memory"; runvm VNM01 "$B1" "$BC01" "$LOG/base01.log"; expect NEW_SUPPORT_COUNT 2; expect NEW_COMPETING_COUNT 0; expect WEIGHT_BEFORE 0; expect WEIGHT_AFTER 2; expect STATE_MUTATED 1; ALIGN=$((ALIGN+1)); HIER_PASS=$((HIER_PASS+1)); PERSIST=$((PERSIST+1))

# Fresh VNM-01 invocation must materially reuse learned hierarchical state.
CASE_NAME=HIERARCHICAL_VNM01_PERSIST
: > "$X1/input/evidence.memory"; runvm VNM01 "$B1" "$BC01" "$LOG/persist01.log"; expect PREVIOUS_STATE_VALID 1; expect PRIOR_SUPPORT_COUNT 2; expect WEIGHT_BEFORE 2; expect WEIGHT_AFTER 2; expect STATE_MUTATED 0; ALIGN=$((ALIGN+1)); HIER_PASS=$((HIER_PASS+1)); PERSIST=$((PERSIST+1))

# Negative integration boundary: fault only support field 2->3; VNM-04 must detect mismatch without output mutation.
CASE_NAME=NEGATIVE_SUPPORT_MISMATCH
BN="$CASES/neg04"; XN="$BN/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"; mkdir -p "$XN/input" "$XN/output"; awk -F '\|\|' 'BEGIN{OFS="||"} {$8="3"; printf "%s",$1; for(i=2;i<=NF;i++) printf "%s%s",OFS,$i}' "$CAND" > "$XN/input/candidate.memory"; cp "$OBS" "$XN/input/observations.memory"; printf 'SENTINEL' > "$XN/output/vnm01_input_bundle.memory"; before=$(sha_of "$XN/output/vnm01_input_bundle.memory"); runvm VNM04 "$BN" "$BC04" "$LOG/neg04.log"; expect SUPPORT_PAIR_COUNT 2; expect SUPPORT_MATCH 0; expect OUTPUT_ALLOWED 0; expect BRIDGE_STATUS REFUSED_CANDIDATE_SUPPORT_MISMATCH; after=$(sha_of "$XN/output/vnm01_input_bundle.memory"); [ "$before" = "$after" ] || fail 61 REFUSAL_MUTATED_OUTPUT; ALIGN=$((ALIGN+1)); NEG=$((NEG+1))

# Two identical downstream branches from empty state prove integration replay determinism.
replay(){ tag="$1"; CASE_NAME="REPLAY_${tag}_VNM04"; R4="$CASES/r${tag}04"; Y4="$R4/.sigma_exec/SIGMA_VNM_04_PAIR_CANDIDATE_TO_WEIGHT_INPUT_BRIDGE_V1"; mkdir -p "$Y4/input" "$Y4/output"; cp "$CAND" "$Y4/input/candidate.memory"; cp "$OBS" "$Y4/input/observations.memory"; : > "$Y4/output/vnm01_input_bundle.memory"; runvm VNM04 "$R4" "$BC04" "$LOG/r${tag}04.log"; expect BRIDGE_STATUS BRIDGE_READY; ALIGN=$((ALIGN+1)); CASE_NAME="REPLAY_${tag}_VNM01"; R1="$CASES/r${tag}01"; Y1="$R1/.sigma_exec/SIGMA_VNM_01_SURFACE_FORM_EVIDENCE_WEIGHTING_V1"; mkdir -p "$Y1/input" "$Y1/state"; : > "$Y1/state/surface_form_weight_state.memory"; route_bundle "$Y4/output/vnm01_input_bundle.memory" "$Y1/input/hypothesis.memory" "$Y1/input/evidence.memory"; runvm VNM01 "$R1" "$BC01" "$LOG/r${tag}01.log"; expect WEIGHT_AFTER 2; ALIGN=$((ALIGN+1)); RBLOG=$(sha_of "$LOG/r${tag}04.log"); RBUNDLE=$(sha_of "$Y4/output/vnm01_input_bundle.memory"); RWLOG=$(sha_of "$LOG/r${tag}01.log"); RSTATE=$(sha_of "$Y1/state/surface_form_weight_state.memory"); }
replay A; A1="$RBLOG"; A2="$RBUNDLE"; A3="$RWLOG"; A4="$RSTATE"
replay B; REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=NO; [ "$A1" = "$RBLOG" ] && [ "$A2" = "$RBUNDLE" ] && [ "$A3" = "$RWLOG" ] && [ "$A4" = "$RSTATE" ] && REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=YES; [ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail 80 REPLAY_MISMATCH; HIER_PASS=$((HIER_PASS+1))

s01a=$(sha_of "$SRC01"); s04a=$(sha_of "$SRC04"); s07a=$(sha_of "$SRC07"); b01a=$(sha_of "$BC01"); b04a=$(sha_of "$BC04"); v7bca=$(sha_of "$V7BC")
SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=NO; BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=NO
[ "$S01_BEFORE" = "$s01a" ] && [ "$S04_BEFORE" = "$s04a" ] && [ "$EXPECTED_VNM07_SOURCE" = "$s07a" ] && SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
[ "$B01_BEFORE" = "$b01a" ] && [ "$B04_BEFORE" = "$b04a" ] && [ "$EXPECTED_VNM07_BYTECODE" = "$v7bca" ] && BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=YES
TOTAL=$((21 + ADD_VM)); PASS_ALIGN=$((16 + ALIGN)); NEG_TOTAL=$((10 + NEG))
printf '\n=== VNM-08 FINAL SUMMARY ===\n'
printf 'CAPABILITY_ID=VNM-08_HIERARCHICAL_SPAN_FORM_TO_PERSISTENT_WEIGHTING_INTEGRATION\nCAPABILITY_NAME=Native hierarchical span-form pair induction to persistent structural weighting integration\n'
printf 'INTEGRATION_ONLY_STAGE=YES\nNEW_NATIVE_SOURCE_REQUIRED=NO\nREUSED_VNM07_FULL_SUBSUITE=YES\n'
printf 'TOTAL_VM_INVOCATIONS=%s\nVNM07_SUBSUITE_VM_INVOCATIONS=21\nVNM08_ADDITIONAL_VM_INVOCATIONS=%s\nVNM04_VM_INVOCATIONS=%s\nVNM01_VM_INVOCATIONS=%s\n' "$TOTAL" "$ADD_VM" "$V04_VM" "$V01_VM"
printf 'POST_VM_ALIGNMENT_PASS_COUNT=%s\nPOST_VM_ALIGNMENT_FAIL_COUNT=0\nVM_NONZERO_COUNT=%s\nSTEP_LIMIT_HIT_COUNT=%s\nNEGATIVE_PASS_COUNT=%s\nHIERARCHICAL_WEIGHTING_INTEGRATION_PASS_COUNT=%s\nPERSISTENCE_PASS_COUNT=%s\n' "$PASS_ALIGN" "$VM_NONZERO" "$STEP_HIT" "$NEG_TOTAL" "$HIER_PASS" "$PERSIST"
printf 'INPUT_DYNAMIC=YES\nOUTPUT_DEPENDS_ON_INPUT=YES\nNEGATIVE_TEST=PASS\nPERSISTENT_STATE=YES_IN_VNM02_VNM01_COMPOSED_CHAIN\nPERSISTENT_STATE_TEST=PASS\nRESTART_REPLAY_TEST=PASS\nREPLAY_IDENTICAL_INPUT_PRESTATE_DECISION=%s\nINITIAL_HIERARCHICAL_WEIGHT=2\n' "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION"
printf 'VNM05_CANDIDATE_GENERATION_OWNER=SIGMA_NATIVE\nVNM06_SPAN_CONTEXT_DERIVATION_OWNER=SIGMA_NATIVE\nVNM07_SPAN_FORM_SERIALIZATION_OWNER=SIGMA_NATIVE\nVNM07_OBSERVATION_ID_DERIVATION_OWNER=SIGMA_NATIVE\nVNM02_PAIR_INDUCTION_OWNER=SIGMA_NATIVE\nVNM04_HYPOTHESIS_GENERATION_OWNER=SIGMA_NATIVE\nVNM04_EVIDENCE_GENERATION_OWNER=SIGMA_NATIVE\nVNM01_WEIGHT_UPDATE_OWNER=SIGMA_NATIVE\n'
printf 'HOST_EXACT_PROTOCOL_DECODE=MECHANICAL_ONLY\nHOST_PAIR_GENERATION=NO\nHOST_PAIR_SELECTION=NO\nHOST_EVIDENCE_GENERATION=NO\nHOST_WEIGHT_UPDATE=NO\nHOST_LEARNING=NO\nHOST_SEMANTIC_INTERPRETATION=NO\nHOST_SEMANTIC_SUBSTITUTION=NO\n'
printf 'SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\nBYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST=%s\nVNM07_SUBSUITE_UNSEEN_HIGH_ENTROPY_TOKEN_LEAK_COUNT=0\nSTEP_LIMIT_STATUS=PASS_IN_29_INVOCATION_BOUNDED_COMPOSED_SUITE\nPRODUCTION_STATE_MUTATED=NO\n' "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST"
printf 'NATURAL_LANGUAGE_TOKENIZATION=NOT_PROVEN\nWORD_BOUNDARY_DETECTION=NOT_PROVEN\nPHRASE_BOUNDARY_DETECTION=NOT_PROVEN\nPHRASE_SEMANTICS=NOT_PROVEN\nSEMANTIC_EQUIVALENCE=NOT_PROVEN\nWORD_MEANING=NOT_PROVEN\nVIETNAMESE_SEMANTIC_UNDERSTANDING=NOT_PROVEN\nGENERAL_SEMANTIC_UNDERSTANDING=NOT_PROVEN\n'
printf 'CLAIM_SCOPE=Bounded reuse of admitted VNM-05->06->07->02 native hierarchical span-form pipeline followed by exact routing into admitted VNM-04->01 native hypothesis/evidence generation and persistent +2 structural weighting; includes support-mismatch refusal and identical downstream replay; no natural-language boundary or semantic claim\n'
[ "$TOTAL" -eq 29 ] || fail 90 TOTAL_VM_INVOCATIONS_MISMATCH
[ "$ADD_VM" -eq 8 ] || fail 91 ADDITIONAL_VM_INVOCATIONS_MISMATCH
[ "$V04_VM" -eq 4 ] || fail 92 VNM04_VM_INVOCATIONS_MISMATCH
[ "$V01_VM" -eq 4 ] || fail 93 VNM01_VM_INVOCATIONS_MISMATCH
[ "$PASS_ALIGN" -eq 24 ] || fail 94 ALIGNMENT_PASS_COUNT_MISMATCH
[ "$VM_NONZERO" -eq 0 ] || fail 95 VM_NONZERO_COUNT_NONZERO
[ "$STEP_HIT" -eq 0 ] || fail 96 STEP_LIMIT_HIT_COUNT_NONZERO
[ "$NEG_TOTAL" -eq 11 ] || fail 97 NEGATIVE_PASS_COUNT_MISMATCH
[ "$HIER_PASS" -eq 4 ] || fail 98 HIERARCHICAL_PASS_COUNT_MISMATCH
[ "$PERSIST" -eq 2 ] || fail 99 PERSISTENCE_PASS_COUNT_MISMATCH
[ "$REPLAY_IDENTICAL_INPUT_PRESTATE_DECISION" = YES ] || fail 100 REPLAY_NOT_IDENTICAL
[ "$SOURCE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail 101 SOURCE_CHANGED
[ "$BYTECODE_UNCHANGED_AFTER_DYNAMIC_TEST" = YES ] || fail 102 BYTECODE_CHANGED
printf 'VNM_08_PREFLIGHT=PASS\nADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE\n'
