# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — CONTROL FLOW BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21
IF_CAPABILITY_EXISTENCE_RETESTED=NO
WHILE_CAPABILITY_EXISTENCE_RETESTED=NO

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime branch/loop semantics, cognition, understanding, or capability-existence claim is made from these probes.

## TEST WA-CF-01

TEST_ID=WA-CF-01
QUESTION=For the exact neutral IF form, does removing parentheses around the condition change current-compiler acceptance?
VARIANT_A=`IF (1 < 2) { ⚡ a: 1; }` inside the exact minimal addressed block/header context
VARIANT_B=Same exact body/context with `IF 1 < 2 { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=38c8e8a597b935be735aa9e0f498e0cfca23cb26764071bc03d9bcd418062393
SOURCE_SHA256_B=a750dc0ec47edfea8292c8b6b63c1fbcb8c227e787753ecb58190b6b206c843a
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF01_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF01_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=6f4ca13ad055980679b157b97c8c7dcc8af2adc8c97c5992c63a3e94cf2d974e
BYTECODE_SIZE_A=84
COMPILER_STDOUT_SIZE_A=149
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF01_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF01_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=54
OBSERVATION=The parenthesized IF condition form was accepted and emitted bytecode. The otherwise-matched unparenthesized condition form was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact minimal IF context, current compiler acceptance distinguishes `IF (condition) { ... }` from the tested `IF condition { ... }` form.
NOT_PROVEN_BEYOND=Does not prove IF runtime behavior, all condition-expression grammar, all whitespace variants, or IF capability existence beyond the already-locked evidence.

## TEST WA-CF-02

TEST_ID=WA-CF-02
QUESTION=For the exact neutral WHILE form, does removing parentheses around the condition change current-compiler acceptance?
VARIANT_A=`WHILE (1 < 2) { ⚡ a: 1; }` inside the exact minimal addressed block/header context
VARIANT_B=Same exact body/context with `WHILE 1 < 2 { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=652815e701a88d9b27f05d0a507420060f4a00453f98dab54a34c6fc1a85d6de
SOURCE_SHA256_B=fab9f8483debc716dfaeb6feebad2c4bde7ac1ea81f4492cbebb4eada8b4359f
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF02_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF02_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=42965e9dbfce5a77b47b883b3ec3a054b4a5d8ff819cc9b133d4f26fab48f4c3
BYTECODE_SIZE_A=84
COMPILER_STDOUT_SIZE_A=149
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF02_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_CF1_20260826_140329/CF02_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=58
OBSERVATION=The parenthesized WHILE condition form was accepted and emitted bytecode. The otherwise-matched unparenthesized condition form was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact minimal WHILE context, current compiler acceptance distinguishes `WHILE (condition) { ... }` from the tested `WHILE condition { ... }` form.
NOT_PROVEN_BEYOND=Does not prove WHILE runtime behavior, all condition-expression grammar, all whitespace variants, or WHILE capability existence beyond the already-locked evidence.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=2
COMPILER_VARIANTS_RUN=4
COMPILER_ACCEPT_CASES=2
COMPILER_REJECT_CASES=2
TIMEOUT_CASES=0
ELSE_PROBE_RUN=NO
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
