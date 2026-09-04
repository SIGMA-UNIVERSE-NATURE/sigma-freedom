# DNA-09 NATIVE ADMISSION SOURCE READY — 2026-09-05

Branch: `SIGMA_LIFE`
Lane: 54 DNA native-only admission
Status: source-ready checkpoint only; NOT runtime admission

## DNA identity

DNA_ID=DNA-09
NAME=Independent Verification Wall
CANON_REFERENCE_BLOB_SHA1=5c4c69aee534404dd7df6a01f6ea498e6a4da399

## Native source

SOURCE_PATH=DNA09_INDEPENDENT_VERIFICATION_WALL_NATIVE_V1.sigma
SOURCE_SHA256=0eb3907b6b18a01daf96f994102cbb6a78038b34f3d6ba63e1d0d3ecee8e6ae5
RUNNER_SHA256=b819edaaa1083fec89b65ba5119e9abca7ac3081c064566b4fe43c6f8f47aade
BUNDLE_SHA256=ed5699c94921a44be39d9f39d8910fc39602a887a43ce6e07a876452def5cb31
MANIFEST_SHA256=105342491190ebaf4dcf454781b8b16d5062af328a605d0a108236e9db0ad161

## Static audit

BASH_SYNTAX=PASS
MANIFEST=PASS
ZIP_INTEGRITY=PASS
MIDFILE_HASH_COMMENT_COUNT=0
MULTI_PRINT_SAME_LINE_COUNT=0
BARE_RETURN_COUNT=0
PYTHON_SOURCE_TOKEN_COUNT=0
RUNNER_PYTHON_COMMAND_COUNT=0

## Test scope design

Dependency preflight requires DNA-01 through DNA-08 admission PASS and actual source/bytecode hash checks.

Dynamic post-compile inputs exercise:
- distinct learner/verifier requirement;
- explicit independent verifier requirement;
- non-empty independence basis;
- candidate binding equality;
- non-empty method;
- non-empty scope;
- non-empty evidence;
- verifier PASS;
- blocking on missing/invalid candidate or verification context;
- promotion eligibility only, never promotion execution.

Planned runtime count: 49 VM invocations = 15 directed + 32 randomized + 2 byte-identical replay.

## Important claim boundary

The field named `candidate_sha256` is supplied as a fresh dynamic 64-hex candidate-binding token in this admission. Equality binding is tested. Cryptographic derivation of the token from candidate content is NOT PROVEN because the exact locked-VM `crypto_digest` signature/return encoding has not been separately runtime-admitted.

CANDIDATE_DIGEST_DERIVATION=NOT_PROVEN
KNOWLEDGE_PROMOTION_EXECUTION=NOT_EXECUTED
EXTERNAL_VERIFIER_INVOCATION=NOT_EXECUTED
PERSISTENT_STATE=NA
HOST_LEARNING=NO
HOST_SEMANTIC_SUBSTITUTION=NO
PYTHON_USED=NO

## Evidence state

DNA09_SOURCE=SOURCE_ONLY
DNA09_COMPILE=NOT_RUN
DNA09_VM=NOT_RUN
DNA09_ADMISSION=NOT_RUN

NEXT_ACTION=RUN_DNA09_NATIVE_ADMISSION_V1_ON_LOCKED_DEVICE
