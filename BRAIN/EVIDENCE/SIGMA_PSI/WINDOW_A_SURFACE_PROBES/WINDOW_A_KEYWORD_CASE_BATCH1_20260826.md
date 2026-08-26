# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — KEYWORD CASE BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_KEYCASE1_20260826_141951
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target is compiler acceptance only: SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

## TEST WA-KEY-01

TEST_ID=WA-KEY-01
QUESTION=Does lowercase `if` compile in the same exact context as accepted uppercase `IF`?
VARIANT_A=Uppercase `IF (1 < 2) { ⚡ a: 1; }`
VARIANT_B=Otherwise-matched lowercase `if (1 < 2) { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=38c8e8a597b935be735aa9e0f498e0cfca23cb26764071bc03d9bcd418062393
SOURCE_SHA256_B=46c448983ff4ca6faace7bf27964cde281c06f6b092c9bd4dfc471c380fcb720
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=6f4ca13ad055980679b157b97c8c7dcc8af2adc8c97c5992c63a3e94cf2d974e
BYTECODE_SIZE_A=84
COMPILER_STDOUT_SIZE_A=161
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=46
OBSERVATION=Uppercase IF form was accepted; otherwise-matched lowercase if form was rejected with no bytecode.
PROVEN_SCOPE=Current compiler distinguishes the exact tested uppercase `IF` spelling from lowercase `if` in this context.
NOT_PROVEN_BEYOND=No universal case rule for every token or identifier is inferred.

## TEST WA-KEY-02

TEST_ID=WA-KEY-02
QUESTION=Does lowercase `while` compile in the same exact context as accepted uppercase `WHILE`?
VARIANT_A=Uppercase `WHILE (1 < 2) { ⚡ a: 1; }`
VARIANT_B=Otherwise-matched lowercase `while (1 < 2) { ⚡ a: 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=652815e701a88d9b27f05d0a507420060f4a00453f98dab54a34c6fc1a85d6de
SOURCE_SHA256_B=d0411942d3559f3340875da3f4afcdaf92050b127b3eaff204fe44d94ed88151
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=42965e9dbfce5a77b47b883b3ec3a054b4a5d8ff819cc9b133d4f26fab48f4c3
BYTECODE_SIZE_A=84
COMPILER_STDOUT_SIZE_A=161
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=46
OBSERVATION=Uppercase WHILE form was accepted; otherwise-matched lowercase while form was rejected with no bytecode.
PROVEN_SCOPE=Current compiler distinguishes the exact tested uppercase `WHILE` spelling from lowercase `while` in this context.
NOT_PROVEN_BEYOND=No universal case rule for every token or identifier is inferred.

## TEST WA-KEY-03

TEST_ID=WA-KEY-03
QUESTION=Does lowercase `def` compile in the same exact context as accepted uppercase `DEF`?
VARIANT_A=Uppercase `DEF f() { RETURN 1; }`
VARIANT_B=Otherwise-matched lowercase `def f() { RETURN 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=eee02bc5112af979b83b24fc6da2c5906cfe0118b4564e1ef238faf6ca27f2e2
SOURCE_SHA256_B=e01cbdb39f0fcef1e96e8553ec281592727b85edb2751989debbfd058b4c483e
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=cca3293b522a0ee07d283ea39bf58a386fdbfe731dceca696ea3d1881edd924d
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=161
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=76
OBSERVATION=Uppercase DEF form was accepted; otherwise-matched lowercase def form was rejected with no bytecode.
PROVEN_SCOPE=Current compiler distinguishes the exact tested uppercase `DEF` spelling from lowercase `def` in this context.
NOT_PROVEN_BEYOND=No universal case rule for every keyword is inferred; RETURN case was held constant in this probe.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=3
COMPILER_REJECT_CASES=3
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
