# SIGMA Minimal Primitive Toolchain ABI Self Test R1 — PASS

Date: 2026-10-03
Source: user-supplied Oppo output.

SCHEMA=SIGMA_MINIMAL_PRIMITIVE_TOOLCHAIN_ABI_SELF_TEST_R1
NO_NEW_SYMBOLS=YES
VM_RC=0
PROBE_COMMAND=RBX_CONTEXT_AWARE_NATIVE_ROUTER_R1
EXPECTED_READY=RBGATEB_CONTEXT_AWARE_SELECTOR_READY
READY_MARKER_MATCH=YES
REFUSED_COMMAND=NO

LIVE_VM_SHA256=0ad6424ccb84bfe2f44240bff8d1cf531a2fb0be88c61491ee113ba740269755
LIVE_SIGMAC_SHA256=7c7fecc20fff9b339ca62c3ddcf65253df32fa703ab60ee88e015176cff672e4
BC_SHA256=e45b31e86dbb3866f35b33add995248c176cd0460728e5f14d7a859d009140d7
ABI_STDOUT_SHA256=d5e6362c2479d3974df274e75dde616624784d7646e35e8f74cc57922045f80b

TOOLCHAIN_ABI_SELF_TEST=PASS

LIVE_MUTATION=NO
ADMISSION=NO
CUTOVER=NO

NEXT=BUILD_FAILURE_DIAGNOSIS_R1
NO_EXIT=YES

## Classification

The existing primitive/context-router command executes successfully on the current live VM with the current live toolchain, without introducing new symbols. The prior REFUSED_COMMAND compatibility blocker is resolved at the ABI probe level.

This PASS is sufficient to proceed to freezing the Gen3 AutoLearn baseline and building Gate21 survival/recovery, with failure diagnosis incorporated into that controller.
