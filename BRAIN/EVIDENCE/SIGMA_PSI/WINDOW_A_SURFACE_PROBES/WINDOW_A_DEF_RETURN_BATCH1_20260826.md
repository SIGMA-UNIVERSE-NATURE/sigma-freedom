# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — DEF/RETURN BATCH 1

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_DEFRET1_20260826_141457
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target for this batch is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No function execution, return-value semantics, cognition, understanding, or generic function semantics are inferred.

## TEST WA-DEFRET-01

TEST_ID=WA-DEFRET-01
QUESTION=For this exact named DEF form, does removing the parameter-list parentheses change current-compiler acceptance?
VARIANT_A=`DEF f(a) { RETURN a; }` followed by empty `⟡(Σ.MAIN) { }`
VARIANT_B=`DEF f a { RETURN a; }` followed by the same empty main block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=fd73158cb0e9c6d911b219efbf05f73e1ca8160dcdcde1a57073fee73ee261ae
SOURCE_SHA256_B=431b087f442db70121b0490341f1ed659e9545f333136e496a324bfbc0eee009
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=fc25c95f3d9fca7fea5a0dffed61b1dddcc06980b8f63aacd8a085bb518fd75e
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=165
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=65
OBSERVATION=The parenthesized parameter-list form was accepted and emitted bytecode; the otherwise-matched no-parentheses form was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact named DEF context, `DEF f(a) { ... }` is accepted while the tested `DEF f a { ... }` form is rejected.
NOT_PROVEN_BEYOND=Does not define all legal DEF parameter grammar, annotations, defaults, variadics, closures, or function runtime semantics.

## TEST WA-DEFRET-02

TEST_ID=WA-DEFRET-02
QUESTION=For this exact named DEF surface, is an empty parameter list accepted compared with a one-parameter list?
VARIANT_A=`DEF f(a) { RETURN a; }` followed by empty main block
VARIANT_B=`DEF f() { RETURN 1; }` followed by the same empty main block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=fd73158cb0e9c6d911b219efbf05f73e1ca8160dcdcde1a57073fee73ee261ae
SOURCE_SHA256_B=eee02bc5112af979b83b24fc6da2c5906cfe0118b4564e1ef238faf6ca27f2e2
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=fc25c95f3d9fca7fea5a0dffed61b1dddcc06980b8f63aacd8a085bb518fd75e
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=165
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=cca3293b522a0ee07d283ea39bf58a386fdbfe731dceca696ea3d1881edd924d
BYTECODE_SIZE_B=59
COMPILER_STDOUT_SIZE_B=165
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both the one-parameter and empty-parameter exact DEF forms were accepted and emitted bytecode.
PROVEN_SCOPE=The exact tested `DEF f()` empty parameter-list form is accepted by the identified current compiler.
NOT_PROVEN_BEYOND=Does not establish runtime arity semantics, call compatibility, defaults, variadics, or anonymous functions.

## TEST WA-DEFRET-03

TEST_ID=WA-DEFRET-03
QUESTION=For this exact RETURN-with-expression inside DEF, does removing the terminating semicolon change current-compiler acceptance?
VARIANT_A=`RETURN a;`
VARIANT_B=`RETURN a` with the same surrounding DEF and empty main block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=fd73158cb0e9c6d911b219efbf05f73e1ca8160dcdcde1a57073fee73ee261ae
SOURCE_SHA256_B=0cb8ab4dea97eb36e9ab97ef967f522cc1b128ebb9995b9548cf3d694a8df4ce
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=fc25c95f3d9fca7fea5a0dffed61b1dddcc06980b8f63aacd8a085bb518fd75e
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=165
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=58
OBSERVATION=The semicolon-terminated RETURN form was accepted and emitted bytecode; the otherwise-matched no-semicolon form was rejected.
PROVEN_SCOPE=In this exact DEF-body context, tested `RETURN a;` is accepted while tested `RETURN a` is rejected.
NOT_PROVEN_BEYOND=Does not establish bare RETURN syntax, placement legality outside DEF, return-value runtime semantics, or stack effects.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=4
COMPILER_REJECT_CASES=2
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0