# SIGMA VKM R6 — Frozen Transport Origin Trace Receipt

## Result

R6_TRANSPORT_SHA_TRACE=PASS
SIGMA_IDENTITY=ONE_SIGMA
MUTATION=NO
FULL_CORPUS_SCAN=NO
FULL_RECURSIVE_SCAN=NO
TERMUX_SHELL_CONTINUES=YES

## Expected frozen transport identity

EXPECTED_LONG_DOCUMENT_TRANSPORT_SOURCE_SHA256=c610083ae1f43bcbc3f941e2dace4f4e034ddedf41570a6969af199e86763921

The install audit records the same LONG_DOCUMENT_TRANSPORT_SOURCE_SHA256 under the exact component/toolchain/live-C5 freeze.

## Exact origin identified

R6_EXACT_FROZEN_TRANSPORT=/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v4_shadow/R8_CONTROL/staging/cycle_000001/r7_exec/SIGMA_GUTENBERG_LONG_DOCUMENT_TRANSPORT_R7.py

SHA256=c610083ae1f43bcbc3f941e2dace4f4e034ddedf41570a6969af199e86763921

The component-level file with the same basename is not byte-identical:

COMPONENT_TRANSPORT_SHA256=15efe44a0fc736c5cb090540707282538569ed9fd8c489d00d65233236612b02

Therefore the frozen transport referenced by the audit is specifically the cycle_000001/r7_exec staged copy, not the current components copy.

## Supporting execution references

The install audit and cycle_000001 worker log both reference the cycle_000001/r7_exec staging area for the frozen R7 execution artifacts. The audit also records Project Gutenberg long-document candidate URLs, content hashes, candidate model paths, and the frozen transport source hash.

## Boundary

This checkpoint is identity/provenance tracing only. No file, canonical state, R7 runner, transport, or production VM was mutated.

NEXT=USE_EXACT_FROZEN_TRANSPORT_FOR_R6_PATCHED_RUNNER_EXECUTION_TEST
