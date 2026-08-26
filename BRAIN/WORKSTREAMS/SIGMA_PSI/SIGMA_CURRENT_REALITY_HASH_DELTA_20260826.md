# SIGMA CURRENT REALITY — HASH DELTA — 2026-08-26

SOURCE=live OPPO/Termux report supplied by user
ROOT=~/SIGMA/sigma_genesis1
CLAIM_POLICY=CLAIM<=EVIDENCE

## CURRENT SHA256

- ./native/sigmac = 65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
- ./native/sigma-vm.v09_candidate = 029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
- ./sigmac.c = e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452
- ./sigma_vm.c = aff15cc5d1a3466f1ab374f6b31d9c36c125dff6290dacaaafa1c635e068745c
- ./compiler_self.sigma = dd91d5c67b8300e9c48cb79b99a08ad519c45bd535110439f5e50de57d290ac1

## COMPARISON TO PRIOR RECORDED OPPO FINGERPRINTS

Prior recorded fingerprints used in earlier evidence:
- sigmac.c = e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452
- sigma_vm.c = 8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2
- compiler_self.sigma = b00b415cc49d042ef152196633c5de4e7fffdf35da84bd900d31b599a9b60af7

Delta:
- sigmac.c = UNCHANGED relative to prior recorded fingerprint
- sigma_vm.c = CHANGED relative to prior recorded fingerprint
- compiler_self.sigma = CHANGED relative to prior recorded fingerprint
- native/sigmac = CURRENTLY_HASHED; no prior live-native binary hash in this note is used for equality claim
- native/sigma-vm.v09_candidate = CURRENTLY_HASHED; no prior live-native binary hash in this note is used for equality claim

Therefore:
BINARY_OR_SOURCE_CHANGED=YES

Scope note: this proves hash inequality/equality only. It does not identify when, why, or by which commit/process the changed files changed, and it does not invalidate unrelated earlier PASS evidence outside claims that depend on the changed implementation identity.

NEXT_MISSING_REPORT_GROUPS:
1. exact list of 21 CURRENT_VERIFIED_CAPABILITIES with evidence/test IDs and DO_NOT_RERUN status
2. exact scope of CURRENT_VM_RUNTIME_PROVEN=YES for VM execution/opcode decode/stack effects/CALL-RETURN/JUMP/HALT
