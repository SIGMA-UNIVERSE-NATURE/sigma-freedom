# V5-K1 D02 payload truncation harness failure

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Stage

```text
LEVEL=LEVEL_2_V5
STAGE=V5-K1
CAPABILITY=EXTERNAL_ACQUISITION_REQUEST_RESPONSE_PROTOCOL
```

## Observed machine evidence

```text
D02_VERIFY_A
VM_RC=0
PHASE=VERIFY
REQUEST_ID=req-a
INPUT_VALID=1
SOURCE_FAMILY_VALID=1
LEDGER_VALID=1
EVENT_MATCH=1
SUCCESS_RESPONSE_MATCH=1
NOT_FOUND_RESPONSE_MATCH=0
PAYLOAD_PRESENT=0
VERIFY_SUCCESS_ELIGIBLE=0
WRITE_ATTEMPTED=0
ACQUISITION_RETAINED=0
STATE_MUTATED=0
V5K1_STATUS=REFUSE_PAYLOAD_MISSING
POST_VM_ALIGNMENT=FAIL
```

## Admission status

```text
V5K1_V1_ADMISSION=FAIL
V5K1_NATIVE_CAPABILITY=NOT_ADMITTED
V5K2_WIKIPEDIA_ADAPTER_UNLOCKED=NO
```

## Diagnosis

The native V5-K1 source behaved correctly: successful response identity alone was insufficient; missing payload caused refusal and no state mutation.

The V1 mechanical runner function `set_req()` truncated the payload slot on every phase. The actual failing sequence was:

```text
PREPARE
-> runner initializes payload/slota.txt empty
-> mechanical transport copies fixture bytes to payload/slota.txt
-> VERIFY calls set_req VERIFY ... slota
-> runner truncates payload/slota.txt back to zero bytes
-> native SIGMA sees PAYLOAD_PRESENT=0
-> native SIGMA refuses
```

This is a harness fixture lifecycle defect, not evidence that the native protocol accepted bad transport state.

## Repair requirement

Fix only the mechanical runner:

```text
PREPARE -> clear valid destination payload slot
VERIFY  -> preserve transport-written payload bytes
```

Do not change the native request/response/provenance logic and do not weaken the D02 oracle.

## Identities

```text
LOCKED_SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
LOCKED_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
V5K1_NATIVE_SOURCE_SHA256=29670c3eca4bcd02e875d2178407259af9e76ebbcbbd6e2ee7a31f979da26537
V5K1_V1_RUNNER_SHA256=d728a84092604220fd54136967ab91e23bf8f298b263fca40fe344b26df0b8b6
V5K1_V1_BUNDLE_SHA256=9c2b04ebba7eb673002528b45083b1ef6987c03e49e23dedcd54a25dfe99e9a2
```

## Boundaries preserved

```text
HOST_COGNITION=NO
HOST_LEARNING=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_SEMANTIC_SUBSTITUTION=NO
CONTENT_TRUTH_DECISION=NOT_EXECUTED
KNOWLEDGE_PROMOTION=NOT_EXECUTED
SEMANTIC_UNDERSTANDING=NOT_PROVEN
FAILURE_IS_EVIDENCE=YES
WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN
```
