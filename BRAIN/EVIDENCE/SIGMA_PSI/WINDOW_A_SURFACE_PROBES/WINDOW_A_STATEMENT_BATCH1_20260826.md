# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — STATEMENT BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime semantics, cognition, understanding, or universal grammar claim is made.

## TEST WA-STMT-01

TEST_ID=WA-STMT-01
QUESTION=For this exact binding statement in the exact minimal block context, does removing the semicolon change current-compiler acceptance?
VARIANT_A=Header plus `⟡(Σ.MAIN) { ⚡ a: 1; }`
VARIANT_B=Same source form with the binding semicolon absent
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=9fae9e65ba823fc870f0eaa6ea0679bf896659272020860c2f693ba6c7ac17f0
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT01_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT01_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=157
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT01_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT01_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=45
OBSERVATION=Variant A was accepted and emitted bytecode; the otherwise-matched no-semicolon binding was rejected and emitted no bytecode.
PROVEN_SCOPE=For the exact tested binding statement surface in this minimal block context, the semicolon-terminated form is accepted and the no-semicolon form is rejected.
NOT_PROVEN_BEYOND=Does not establish a universal semicolon rule for every statement kind.

## TEST WA-STMT-02

TEST_ID=WA-STMT-02
QUESTION=For this exact binding statement, does replacing the binding colon with `=` change current-compiler acceptance?
VARIANT_A=`⚡ a: 1;`
VARIANT_B=`⚡ a = 1;`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=9e663743c008d54674f4c5abd581ed3547095769e6e5c0b8297c5ccd626b48c8
SOURCE_SHA256_B=f19d94b9ee5682edbdbb37da45d1e047606f21bf3c6a8cb1efde3a9c6bcb6b3b
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT02_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT02_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=26984037391df0e06a01185177261a99fc4b7e6f6ab3998b3158a49ab7283875
BYTECODE_SIZE_A=53
COMPILER_STDOUT_SIZE_A=157
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT02_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT02_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=72
OBSERVATION=The tested colon binding form was accepted; the otherwise-matched equals-sign form was rejected and emitted no bytecode.
PROVEN_SCOPE=For this exact binding surface, `:` is accepted while the tested `=` replacement is rejected.
NOT_PROVEN_BEYOND=Does not define every legal or illegal assignment/binding operator in the language.

## TEST WA-STMT-03

TEST_ID=WA-STMT-03
QUESTION=For two exact binding statements on separate physical lines, can newline-only separation replace semicolon termination?
VARIANT_A=Two separate-line binding statements, each semicolon-terminated
VARIANT_B=The same two separate-line binding statements with both semicolons removed
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=a9008a4f6b7dee6a08f1089a491e6202ced56b0f0db0f9240512fcff28786999
SOURCE_SHA256_B=159cb602fe7c374c684a4d184f063bd40d552e560c3b840f51745185cd5b1121
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT03_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT03_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=8863a84816f82af71d6fed2c225704a7db9462e1563ac3fb4e235e196e0fbf12
BYTECODE_SIZE_A=77
COMPILER_STDOUT_SIZE_A=157
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT03_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT03_B.sigmab
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=47
OBSERVATION=The semicolon-terminated two-statement form was accepted; the newline-only variant was rejected and emitted no bytecode.
PROVEN_SCOPE=For these exact two binding statements in this block context, physical newlines alone do not substitute for the tested semicolon termination.
NOT_PROVEN_BEYOND=Does not establish line-break significance for all statement or expression kinds.

## TEST WA-STMT-04

TEST_ID=WA-STMT-04
QUESTION=For the same two semicolon-terminated binding statements, does placing both on one physical line change current-compiler acceptance?
VARIANT_A=Two semicolon-terminated bindings on separate physical lines
VARIANT_B=The same two semicolon-terminated bindings on one physical line
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=a9008a4f6b7dee6a08f1089a491e6202ced56b0f0db0f9240512fcff28786999
SOURCE_SHA256_B=786e4a01afaed1a90f59156b1947cfb61d5cf6f4e811a920afa5f240c9e2b19f
COMPILER_COMMAND_A=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT04_A.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT04_A.sigmab
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=8863a84816f82af71d6fed2c225704a7db9462e1563ac3fb4e235e196e0fbf12
BYTECODE_SIZE_A=77
COMPILER_STDOUT_SIZE_A=157
COMPILER_STDERR_SIZE_A=0
COMPILER_COMMAND_B=./native/sigmac .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT04_B.sigma .sigma_tmp/WINDOW_A_SURFACE_PROBES_STMT1_20260826_134054/STMT04_B.sigmab
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=8863a84816f82af71d6fed2c225704a7db9462e1563ac3fb4e235e196e0fbf12
BYTECODE_SIZE_B=77
COMPILER_STDOUT_SIZE_B=157
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both layouts were accepted and emitted byte-identical bytecode.
PROVEN_SCOPE=For these exact two semicolon-terminated bindings, separate physical lines are not required for compiler acceptance; the tested same-line form is also accepted.
NOT_PROVEN_BEYOND=Does not prove arbitrary same-line statement composition or whitespace equivalence for every statement kind.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=4
COMPILER_VARIANTS_RUN=8
COMPILER_ACCEPT_CASES=5
COMPILER_REJECT_CASES=3
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
