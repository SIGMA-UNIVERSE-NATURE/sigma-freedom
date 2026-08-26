# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — HEADER BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime semantic claim, cognition claim, namespace semantic claim, or universal grammar claim is made from these probes.

## TEST WA-HDR-01

TEST_ID=WA-HDR-01
QUESTION=For this exact minimal block form, does removing the language header change current-compiler acceptance?
VARIANT_A=#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.ITERATION.TEST][VERSION=1.0] followed by exact minimal `⟡(Σ.MAIN) { ⚡ a: 1; }` block
VARIANT_B=Same exact minimal block with the language header absent
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=9d1b753dff2ddd4edd5ad25cc992c9828f105a70bd45d86355134a8c67eb1f80
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR01_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR01_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR01_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR01_B.sigmab
COMPILER_RC_B=3
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=37
OBSERVATION=Variant A was accepted and emitted bytecode. Variant B was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact minimal program context under the identified current compiler, the header-present form is accepted while the otherwise-matched header-absent form is rejected.
NOT_PROVEN_BEYOND=Does not by itself prove all possible files require a header, define the parser implementation, or establish runtime semantics.

## TEST WA-HDR-02

TEST_ID=WA-HDR-02
QUESTION=For this exact minimal program, does placing the same header after the block change current-compiler acceptance compared with placing it first?
VARIANT_A=Header first, then exact minimal `⟡(Σ.MAIN) { ⚡ a: 1; }` block
VARIANT_B=Same exact block first, then the same header after the block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=643560398bcf839a0c8a2f580ea69c888ce7ab5e05243d7d2b133e7410540ba2
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR02_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR02_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR02_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR02_B.sigmab
COMPILER_RC_B=3
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=37
OBSERVATION=Variant A was accepted and emitted bytecode. Variant B was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact minimal program context, current compiler acceptance distinguishes header-first from the same header displaced after the block.
NOT_PROVEN_BEYOND=Does not prove every conceivable pre-header token/comment/whitespace placement rule or parser implementation.

## TEST WA-HDR-03

TEST_ID=WA-HDR-03
QUESTION=For this exact header/block form, does removing the DOMAIN field change current-compiler acceptance?
VARIANT_A=#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.ITERATION.TEST][VERSION=1.0] followed by exact minimal block
VARIANT_B=#SIGMAUNIVERSE_LANGUAGE[VERSION=1.0] followed by the same exact minimal block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=b06375359d8cd600de4603eb0ba194cac5233ea90a511d0884e30f538a96edf5
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR03_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR03_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=153
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR03_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_HDR1_20260826_132908/HDR03_B.sigmab
COMPILER_RC_B=3
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=37
OBSERVATION=Variant A was accepted and emitted bytecode. Variant B was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact minimal program context and exact header family, current compiler acceptance distinguishes DOMAIN-present from DOMAIN-absent.
NOT_PROVEN_BEYOND=Does not define generic DOMAIN value grammar, namespace semantics, or all malformed-header behavior.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=3
COMPILER_REJECT_CASES=3
TIMEOUT_CASES=0
BYTECODE_ACCEPT_HASH=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_ACCEPT_SIZE=53
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
