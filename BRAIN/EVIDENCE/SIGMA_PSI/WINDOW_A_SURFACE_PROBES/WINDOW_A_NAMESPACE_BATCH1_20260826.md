# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — NAMESPACE BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime namespace semantics, hierarchy, lookup, cognition, understanding, or universal grammar claim is made.

## TEST WA-NS-01

TEST_ID=WA-NS-01
QUESTION=For the same minimal addressed block, does neutral one-segment address `Σ.A` compile like observed one-segment address `Σ.MAIN`?
VARIANT_A=Header plus `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same header/body with `⟡(Σ.A) { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=d2ebbfca59de29a186c6b2b34763eeb3396e5e2030a9d10510b9d54e00730612
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS01_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS01_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=149
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS01_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS01_B.sigmab
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_B=53
COMPILER_STDOUT_SIZE_B=149
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both exact one-segment forms were accepted and emitted bytecode.
PROVEN_SCOPE=The exact tested block address form `Σ.A` is accepted by the identified current compiler in this minimal block context.
NOT_PROVEN_BEYOND=Does not define the identifier regex, arbitrary segment characters, runtime namespace meaning, or resolution semantics.

## TEST WA-NS-02

TEST_ID=WA-NS-02
QUESTION=For the same minimal block, does exact two-segment address `Σ.A.B` compile compared with accepted one-segment `Σ.A`?
VARIANT_A=Header plus `⟡(Σ.A) { ⚡ a: 1; }`
VARIANT_B=Same header/body with `⟡(Σ.A.B) { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=d2ebbfca59de29a186c6b2b34763eeb3396e5e2030a9d10510b9d54e00730612
SOURCE_SHA256_B=4fe683b3d9a23e9a54eade1dc7f69805e1a642453c1b09d8c94cd07870aeedb1
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS02_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS02_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=149
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS02_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS02_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=64
OBSERVATION=Accepted control `Σ.A` compiled; exact tested two-segment `Σ.A.B` was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact block-address context, current compiler accepts tested `Σ.A` and rejects tested `Σ.A.B`.
NOT_PROVEN_BEYOND=Does not prove all dotted namespace/address syntax is globally invalid in every source position or runtime subsystem.

## TEST WA-NS-03

TEST_ID=WA-NS-03
QUESTION=Does malformed double-dot `Σ.A..B` differ from `Σ.A.B` in compiler acceptance?
VARIANT_A=Header plus `⟡(Σ.A.B) { ⚡ a: 1; }`
VARIANT_B=Same header/body with `⟡(Σ.A..B) { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=4fe683b3d9a23e9a54eade1dc7f69805e1a642453c1b09d8c94cd07870aeedb1
SOURCE_SHA256_B=6862dfa74066f0dde15d827611a83d2c827126e6843d78fc69b99045ab1ac920
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS03_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS03_A.sigmab
COMPILER_RC_A=4
BYTECODE_CREATED_A=NO
COMPILER_STDOUT_SIZE_A=0
COMPILER_STDERR_SIZE_A=64
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS03_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_NS1_20260826_134435/NS03_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=64
OBSERVATION=Both variants were rejected and emitted no bytecode.
PROVEN_SCOPE=INCONCLUSIVE for double-dot differential because Variant A was not an accepted control.
NOT_PROVEN_BEYOND=No claim that `Σ.A..B` has a distinct rejection rule; no malformed-dot grammar is inferred from two rejected forms.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=3
COMPILER_REJECT_CASES=3
INCONCLUSIVE_PROBES=1
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
