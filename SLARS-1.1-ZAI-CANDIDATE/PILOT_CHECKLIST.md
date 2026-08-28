# SLARS-1.1-ZAI Pilot Checklist

Checklist này dùng để khởi động một run thật. Đánh dấu `PASS` chỉ khi có raw
evidence; không điền theo suy đoán.

## 1. Trước run

- [ ] G1-M, G1-S, G2, G3-T và G3-O có evidence riêng, đúng RUN_ID.
- [ ] `ORIGINAL.state` và `TRANSLATION.sigma` đã khóa SHA-256.
- [ ] G3 chỉ dùng `.sigma_exec/G-20_RUNTIME_READBACK.sigma`; template không đổi.
- [ ] Protocol, rubric, thresholds, item sets, seed, max cycles và stop rule đã
  khóa trước baseline.
- [ ] Candidate/evaluator/toolchain/configuration identities đã khóa.
- [ ] Candidate-visible, candidate-forbidden và scan policy manifests đã khóa.
- [ ] Answer keys không candidate-visible; host derivation bị cấm.
- [ ] Baseline/post/training/retest/reasoning/delayed item IDs và bytes tách biệt.
- [ ] Matched family IDs đủ cho paired comparison.
- [ ] Context-reset và allowed persistence manifest đã khóa.

## 2. ZAI — Zero Answer Injection prerequisite

Trước A1/A3/R1, khóa profile `SIGMA_LANGUAGE_ZERO_ANSWER_INJECTION`:

- [ ] Exact policy locks dùng đúng token `SUPPORTOR` và không bị nới.
- [ ] Candidate, sigmac, SIGMA VM, runner và protocol có artifact bytes + hash.
- [ ] Evaluation rubric được khóa hash tại `PROTOCOL_FREEZE` và evaluator report
  bind đúng rubric hash.
- [ ] Sáu actor ID candidate-builder/test-designer/key-custodian/runner/evaluator/
  auditor khác nhau sau NFKC + casefold.
- [ ] Candidate freeze xảy ra trước blind-case commit.
- [ ] Visibility manifest bao phủ toàn bộ 19 channel chuẩn; mỗi channel có
  materialized evidence và unknown channel = 0.
- [ ] Answer key, semantic review và evaluation không candidate-visible/pre-output.
- [ ] Candidate source, bytecode, blind input, binaries và runner nằm trong scan
  surface content-addressed.
- [ ] Host trace chỉ chứa operation cơ học; semantic transform/rewrite = false.
- [ ] Raw stdout/stderr đóng băng trước key-first-access và external evaluation.
- [ ] Mỗi event bind ID/SHA-256/byte-count của toàn bộ input/output/process.
- [ ] Semantic review v2 nhận toàn scan surface và bind từng artifact ID/SHA.
- [ ] Registered exact/normalized/alnum/hex/base64/URL/JSON-escape/ROT13 scan sạch.
- [ ] Protocol/run/verifier/core/schemas/standard/package-manifest receipt hashes
  xuất hiện trong report và khớp expected hashes đã tin cậy bên ngoài.
- [ ] Giới hạn artifact bytes, tổng bytes, marker bytes/count và scan product
  được khóa trước run.
- [ ] Independent semantic review không phát hiện paraphrase/structural injection.
- [ ] ZAI `PASS` không được ghi thành `COGNITION=YES`.

Nếu chưa có run thật, ghi `ZERO_ANSWER_INJECTION=UNVERIFIED`; template hoặc
mutation-suite PASS không thay thế blind-run evidence.

## 3. A1 — Readiness baseline

- [ ] Baseline chạy trước lesson exposure.
- [ ] Baseline không tiết lộ target content; sensitization control đã định nghĩa.
- [ ] Raw input/output transcript hashes tồn tại.
- [ ] External evaluator record gắn với đúng output hashes.
- [ ] Mỗi trục báo riêng score, n và uncertainty.
- [ ] Không collapse `INVALID`, `FAIL`, `INSUFFICIENT_EVIDENCE`.

## 4. A2/A3 — Exposure và kiểm tra tiếp thu

- [ ] Translation SHA exposed bằng translation SHA reviewed.
- [ ] Scanner RC và match count có raw transcript.
- [ ] Không có evaluator key/target answer trước candidate output.
- [ ] Immediate set là fresh set.
- [ ] D/N/F/X/U/C đều được chấm theo rubric đã khóa.
- [ ] Paired delta và confidence interval được tính từ matched families.
- [ ] Không claim causal effect nếu không có pre-registered control.

## 5. A4 — Phát triển tiếp thu

- [ ] Error record gắn với transcript hash.
- [ ] Error class thuộc taxonomy đã khóa.
- [ ] Intervention chỉ dùng training material.
- [ ] Retest mỗi cycle dùng item IDs/bytes mới.
- [ ] Rubric và threshold không đổi.
- [ ] Stop rule/max cycles được tuân thủ.
- [ ] Improvement xuất hiện trên fresh retest và không làm mandatory track tụt
  dưới floor.

## 6. R1 — Suy luận độc lập

- [ ] Task conclusion không có nguyên dạng trong lesson/training.
- [ ] Evaluator key bị che và tool/context policy giữ nguyên.
- [ ] Audit record có premise IDs, rule IDs, derived claims, constraint checks,
  counterexample check, uncertainty và final answer.
- [ ] Không yêu cầu hoặc claim truy cập hidden chain-of-thought.
- [ ] Validity, evidence fidelity, alternatives, robustness, constraints và
  calibration đều được chấm riêng.

## 7. V1 — Fresh-context retention

- [ ] Minimum delay được thỏa.
- [ ] Candidate context đã reset.
- [ ] Allowed persistence manifest SHA khớp protocol.
- [ ] Không có hidden lesson/key reinjection.
- [ ] Candidate state identities trước delay và tại delayed start đã khóa.
- [ ] Delayed items là fresh và đủ n.
- [ ] Absolute floors và retention-ratio floors đều đạt.

## 8. Verdict

```text
FULL_SLARS_1_1_PACKAGE_PASS =
    TRANSPORT_PASS
    ∧ A0_PASS
    ∧ A1_VALID
    ∧ A2_PASS
    ∧ A3_EVIDENCE_PASS
    ∧ A4_DEVELOPMENT_EVIDENCE_PASS
    ∧ R1_PASS
    ∧ V1_PASS
    ∧ ZAI_INJECTION_INTEGRITY_PASS_FOR_EVERY_CANDIDATE_ORIGIN_OUTPUT
    ∧ EXTERNAL_VERDICT_IDENTITY_BOUND
    ∧ IDENTITY_BRIDGE_PASS
```

- [ ] Mọi reported status khớp recomputation.
- [ ] Mọi claim thuộc allowlist và kèm RUN_ID/protocol/lesson/candidate/evaluator.
- [ ] Report ghi rõ `EXTERNAL_SCORE_CONTENT_REJUDGED=NO` nếu validator chỉ tổng
  hợp external scores.
- [ ] Nếu chưa chạy thật, kết luận duy nhất là `ACTUAL_GATE_EXECUTION=UNVERIFIED`.
- [ ] Không dùng `LEGACY_SLARS_1_0_CORE_PACKAGE_PASS` làm
  `FULL_SLARS_1_1_PACKAGE_PASS`; composite ZAI integration hiện chưa triển khai.
