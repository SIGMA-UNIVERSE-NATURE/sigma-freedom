# WINDOW A — BLACK-BOX DIFFERENTIAL GRAMMAR EVIDENCE — CALL/RETURN BATCH 2

ROLE=WINDOW_A_ONLY
DATE=2026-08-26
PRIMARY_ROOT=~/SIGMA/sigma_genesis1
PROBE_DIR=.sigma_tmp/WINDOW_A_SURFACE_PROBES_CALLRET2_20260826_141723
COMPILER_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_EXECUTION_USED=NO
NO_EXPECTED_SEMANTIC_ANSWER=YES
PRIVATE_SOURCE_INSPECTED=NO
PRIVATE_SOURCE_PUBLISHED=NO
DO_NOT_RERUN_CAPABILITIES_PRESERVED=21

Evidence target is compiler acceptance only:
SOURCE FORM → CURRENT COMPILER RC → BYTECODE CREATED OR NOT.

No runtime arity, call semantics, return-value semantics, cognition, or understanding claim is made.

## TEST WA-CALLRET-01

TEST_ID=WA-CALLRET-01
QUESTION=In the exact tested named-call binding context, does zero-argument `f()` compile compared with one-argument `f(1)`?
VARIANT_A=Function `DEF f(a) { RETURN a; }` plus `⚡ x: f(1);`
VARIANT_B=Same function definition plus `⚡ x: f();`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=83ac49fa53678a2c303bce56613d4f14c0aafc488924ee4f8f27a41dd5165ff5
SOURCE_SHA256_B=9ef0f73cdff3b9f1c3650542fb9a8e020b05b1d7ba7337b6033eeab631603cf2
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=6ed3ddf131caee47f81b55a88e5e9765b171d718f5bf87889322b4399e9a2bc3
BYTECODE_SIZE_A=90
COMPILER_STDOUT_SIZE_A=169
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=39ed63ede72a1c94e49d501005d0b4bfac00e59e6282f92bc676205916edc43e
BYTECODE_SIZE_B=76
COMPILER_STDOUT_SIZE_B=169
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both exact named-call source forms were accepted and emitted bytecode.
PROVEN_SCOPE=Exact compiler acceptance of the tested zero-argument call surface `f()` and one-argument surface `f(1)` in binding-RHS position.
NOT_PROVEN_BEYOND=No runtime arity checking, parameter binding behavior, call result, callable-object grammar, or execution behavior is established.

## TEST WA-CALLRET-02

TEST_ID=WA-CALLRET-02
QUESTION=Inside the same zero-parameter DEF context, does bare `RETURN;` compile compared with `RETURN 1;`?
VARIANT_A=`DEF f() { RETURN 1; }` plus empty MAIN block
VARIANT_B=`DEF f() { RETURN; }` plus same empty MAIN block
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=eee02bc5112af979b83b24fc6da2c5906cfe0118b4564e1ef238faf6ca27f2e2
SOURCE_SHA256_B=65eaa519429290b545d1d9352cf07dea9a0c8c735ce70c873947a552aa6b62e0
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=cca3293b522a0ee07d283ea39bf58a386fdbfe731dceca696ea3d1881edd924d
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=169
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=4
BYTECODE_CREATED_B=NO
COMPILER_STDOUT_SIZE_B=0
COMPILER_STDERR_SIZE_B=53
OBSERVATION=Expression-bearing RETURN was accepted; exact bare `RETURN;` was rejected and emitted no bytecode.
PROVEN_SCOPE=In this exact DEF context, current compiler accepts `RETURN 1;` and rejects bare `RETURN;`.
NOT_PROVEN_BEYOND=Does not establish runtime return-value semantics or every possible RETURN expression form.

## TEST WA-CALLRET-03

TEST_ID=WA-CALLRET-03
QUESTION=Does exact expression-bearing RETURN compile only inside DEF, or is the same RETURN surface also accepted inside a top-level addressed block?
VARIANT_A=`DEF f() { RETURN 1; }` plus empty MAIN block
VARIANT_B=No DEF; `⟡(Σ.MAIN) { RETURN 1; }`
NO_EXPECTED_SEMANTIC_ANSWER=YES
SOURCE_SHA256_A=eee02bc5112af979b83b24fc6da2c5906cfe0118b4564e1ef238faf6ca27f2e2
SOURCE_SHA256_B=25bef3b53d2cf034cee6929fcdf0faa0fbf68a75bffe688f8589b5c4bdd52260
COMPILER_RC_A=0
BYTECODE_CREATED_A=YES
BYTECODE_SHA256_A=cca3293b522a0ee07d283ea39bf58a386fdbfe731dceca696ea3d1881edd924d
BYTECODE_SIZE_A=59
COMPILER_STDOUT_SIZE_A=169
COMPILER_STDERR_SIZE_A=0
COMPILER_RC_B=0
BYTECODE_CREATED_B=YES
BYTECODE_SHA256_B=7e9e7e2829d7ee013b43303c29c119fcc9e823d2fde06de9da0b539744c34f4d
BYTECODE_SIZE_B=44
COMPILER_STDOUT_SIZE_B=169
COMPILER_STDERR_SIZE_B=0
OBSERVATION=Both exact placements were accepted and emitted bytecode.
PROVEN_SCOPE=Exact expression-bearing `RETURN 1;` source surface is compiler-accepted both inside the tested DEF and inside the tested top-level addressed MAIN block.
NOT_PROVEN_BEYOND=No runtime legality/effect of top-level RETURN is established; compiler acceptance alone is not runtime semantic proof.

## BATCH SUMMARY

DIFFERENTIAL_PROBES_RUN=3
COMPILER_VARIANTS_RUN=6
COMPILER_ACCEPT_CASES=5
COMPILER_REJECT_CASES=1
TIMEOUT_CASES=0
GPT_ANSWER_IMPOSITION_USED=NO
CAPABILITY_RESEARCH_RERUNS=0
