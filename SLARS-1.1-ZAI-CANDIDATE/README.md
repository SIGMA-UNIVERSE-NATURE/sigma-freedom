# SLARS-1.1-ZAI candidate

**SIGMA Lesson Acquisition & Independent Reasoning Standard** với module bắt
buộc **SIGMA Language / Zero Answer Injection**.

SLARS tách ba câu hỏi không được nhập làm một:

1. Artifact có được vận chuyển, compile và readback đúng không?
2. Có phát hiện answer/hypothesis/reasoning/conclusion bị đưa sẵn vào vùng
   candidate nhìn thấy không?
3. Candidate có đạt hiệu năng blind-task, retention hoặc reasoning không?

`PASS` ở câu 1 hoặc 2 không trả lời câu 3. Mọi report ZAI luôn giữ:

```text
HUMAN_LANGUAGE_AS_SIGMA_COGNITION=FORBIDDEN_UNTIL_PROVEN
SIGMA_COGNITION=NOT_PROVEN
```

## Thành phần

- `STANDARD.md`: chuẩn SLARS nền A0–A4, R1, V1.
- `ZERO_ANSWER_INJECTION_STANDARD.md`: module ZAI Z0–Z7 và claim ceiling.
- `AUDIT_SIGMA_COGNITION_CANDIDATE_ZAI.md`: audit tĩnh candidate được cung cấp;
  không phải runtime evidence.
- `PRODUCER_VERIFICATION.md`: lệnh, kết quả mutation suite và evidence ceiling.
- `schemas/zai_protocol.schema.json`: protocol ZAI khóa trước run.
- `schemas/zai_run_bundle.schema.json`: run evidence, artifact và event chain.
- `templates/zai_protocol.template.json`: template protocol, không phải evidence.
- `templates/zai_run_bundle.template.json`: template run, không phải evidence.
- `tools/zai_core.py`: strict parser, schema subset, materializer và predicates.
- `tools/validate_zai_bundle.py`: CLI validator stdlib-only cho profile ZAI.
- `tests/test_validate_zai_bundle.py`: golden control và adversarial mutations.
- Các file schema/template/validator SLARS-1.0 cũ được giữ để tương thích; chúng
  chỉ có thể phát `LEGACY_SLARS_1_0_CORE_PACKAGE_PASS`. Chúng không thay thế
  validator ZAI và không thể phát `FULL_SLARS_1_1_PACKAGE_PASS=YES`.

## Kiểm tra template

```bash
python3 tools/validate_zai_bundle.py \
  --protocol templates/zai_protocol.template.json \
  --run templates/zai_run_bundle.template.json \
  --evidence-root . \
  --mode structure
```

Kết quả đúng của template:

```text
STRICT_SCHEMA_PASS=YES
ACTUAL_ZAI_EXECUTION=UNVERIFIED
ZERO_ANSWER_INJECTION=UNVERIFIED
```

## Kiểm tra evidence thật

```bash
python3 tools/validate_zai_bundle.py \
  --protocol path/to/locked_protocol.json \
  --run path/to/run_bundle.json \
  --evidence-root path/to/sealed_evidence_root \
  --mode evidence
```

Validator không chạy source trong bundle, không sinh answer và không chấm nghĩa.
Nó dereference artifact thật, tính lại size/hash, kiểm tra path/link, policy,
role separation, channel evidence, event hash-chain gắn với bytes, registered
representations, declared toolchain-output binding, key/rubric timing,
external-report binding và claim dependency.
Semantic paraphrase vẫn cần auditor độc lập; unknown readable channel chặn PASS.

CLI receipt gắn report với SHA-256 của protocol, run bundle, validator, core,
hai schema, đặc tả ZAI và package manifest. Hash xác định bytes; việc phê duyệt
build vẫn cần expected hash/chữ ký từ nguồn tin cậy bên ngoài.

## Trạng thái phát hành

```text
SPECIFICATION_STATUS=PRODUCER_CANDIDATE
ZAI_VALIDATOR_IMPLEMENTATION=PROVIDED
INDEPENDENT_TECHNICAL_VERIFICATION=REQUIRED
ACTUAL_BLIND_ZAI_RUN=NOT_RUN
ACTUAL_ACQUISITION_EVIDENCE=UNVERIFIED
ACTUAL_REASONING_EVIDENCE=UNVERIFIED
FULL_SLARS_1_1_COMPOSITE_VALIDATOR=NOT_IMPLEMENTED
SIGMA_COGNITION=NOT_PROVEN
```
