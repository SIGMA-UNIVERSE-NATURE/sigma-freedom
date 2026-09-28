# SIGMA Native Structural Codec R12 — Structured Encoder

Date: 2026-09-29
Source: user-supplied Termux runtime output.

## Deterministic compile

Source:
SIGMA_VKM_R12_STRUCTURED_ENCODER.sigma

Independent compiled bytecode outputs were compared.

R12_ENCODER_DETERMINISTIC=PASS

## Encoder runtime

WRITE_RC=0

ORIGINAL_BYTES=121

STRUCTURED_PAYLOAD_BYTES=20

CONTAINER_BYTES=98

ENCODER_LOCAL_ROUNDTRIP=PASS

ENCODER_CLAIM=NOT_ADMISSION_PROOF

REAL_DATA_DELETE=NO

## Durable output artifact

Path:
/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/NATIVE_STRUCTURAL_CODEC_R1/r11_durable/good_structured.sgc

File size:
98 bytes

SHA256:
9f7555460a4dbcae24c6cf60cc1f4ab3a38481a172adec04dd686e1355025f6f

## Interpretation boundary

This checkpoint records deterministic R12 structured-encoder compilation and a successful local roundtrip into a 98-byte durable container from a 121-byte original input, with a 20-byte structured payload.

No real data deletion occurred.

Per the runtime output, this encoder result is NOT_ADMISSION_PROOF and must not be promoted beyond encoder/roundtrip evidence without a separate admission proof.
