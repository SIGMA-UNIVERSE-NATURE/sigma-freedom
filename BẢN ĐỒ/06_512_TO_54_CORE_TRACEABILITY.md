# 06 — SIGMA 512 → 54 CORE → RUNTIME TRACEABILITY

## Mục đích

512 điểm là **specification layer**. 54 DNA core là **architecture/implementation responsibility layer**. Runtime, test và evidence là **execution/verification layer**.

Không được coi ba lớp này là một.

```text
SIGMA 512 ATTRIBUTES
        │
        ▼
CANONICAL MANIFEST
        │
        ▼
TRACEABILITY MAP
        │
        ▼
54 SIGMA DNA CORES
        │
        ▼
RUNTIME IMPLEMENTATION
        │
        ▼
TEST / EXPERIMENT
        │
        ▼
EVIDENCE
        │
        ▼
INDEPENDENT EVALUATION
        │
        ▼
PASS / PARTIAL / HOLD / FAIL / NOT_AUDITED
        │
        ▼
GAP → CANDIDATE → SHADOW → EVALUATE → PROMOTE / REVISE / REJECT
```

## Canonical 512

Canonical selection được định nghĩa duy nhất trong:

`SIGMA_512_ATTRIBUTES/SIGMA_512_CANONICAL_MANIFEST.json`

Bộ source đang hoạt động hiện **không chồng lấn**:

- 1–275: `Full PART 01 TO 21.`
- 276–440: `ATTRIBUTES_276_440.md`
- 441–512: `PART 28 TO END`

Hai source cũ đã bị loại khỏi working tree vì dư thừa:

- `PART 21 to 28` — chứa vùng chồng 204–275 và 441+; phần duy nhất cần giữ đã được tách sạch thành 276–440.
- `Part1.` — bản sao của 1–12.

Path và blob SHA cũ được lưu trong manifest; Git history là recovery path. Vì vậy deduplication không xóa provenance.

## Traceability

`SIGMA_512_ATTRIBUTES/SIGMA_512_TRACEABILITY_MAP.json` chia 512 requirement thành 31 miền không chồng lấn và gắn mỗi miền với:

- primary DNA cores;
- supporting DNA cores;
- evidence class bắt buộc.

Mapping này biểu diễn **responsibility**, không phải bằng chứng implementation PASS.

## Ba trạng thái phải tách biệt

```text
SPECIFICATION STATUS
    SPEC_PASS

RESPONSIBILITY STATUS
    MAPPED

IMPLEMENTATION STATUS
    NOT_AUDITED / PARTIAL / PASS / HOLD / FAIL / NOT_APPLICABLE
```

`SPEC_PASS + MAPPED` không suy ra `PASS`.

## PASS contract

Một attribute chỉ được `PASS` khi evidence ledger có đủ tối thiểu:

- `implementation_artifacts`
- `tests`
- `evidence`
- `evaluator`
- `last_verified_at`
- `verified_version`
- `rollback_or_correction_path`

và `evaluator.independent = true`.

Tên file, class, comment, self-report hoặc việc một core tồn tại không phải implementation evidence.

## Anti-self-certification

Không subsystem nào được:

1. tạo candidate;
2. tự đổi evaluator/threshold;
3. tự chấm theo evaluator mới;
4. tự promote;
5. rồi gọi chuỗi đó là independent improvement.

Tối thiểu phải giữ separation giữa:

```text
PROPOSER / IMPLEMENTER
        ≠
INDEPENDENT EVALUATOR
        ≠
AUTHORITY / PROMOTION GATE
```

## Validator

Chạy:

```bash
python "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py"
```

Validator bắt buộc kiểm tra:

- đúng 512 canonical attributes;
- coverage 1..512 liên tục;
- source blob integrity;
- đúng 54 DNA core IDs;
- traceability 1..512 không overlap/gap;
- mọi referenced core tồn tại;
- mọi `PASS` có đủ evidence contract;
- evaluator của `PASS` là independent;
- không suy ra PASS từ code/file existence.

CI enforcement:

`.github/workflows/sigma_512_contract.yml`

## Trạng thái khởi tạo

Sau khi thiết lập contract:

```text
SPECIFICATION: PASS
CANONICAL_ATTRIBUTES: 512
CORE_CATALOG: 54
TRACEABILITY: COMPLETE
IMPLEMENTATION: NOT_AUDITED UNTIL EVIDENCE
```

Không được nâng các trạng thái implementation chỉ để làm dashboard đẹp.

## Luồng audit tiếp theo

Mỗi attribute cần đi qua:

```text
ATTRIBUTE
→ inspect responsible core(s)
→ identify runtime path
→ define executable test
→ run test
→ capture evidence
→ independent evaluation
→ assign status
→ write ledger
→ regression protection
```

Ưu tiên audit theo dependency/risk, không đơn giản từ 001 tới 512.

Suggested first audit fronts:

1. Truth / provenance / uncertainty.
2. Independent verification wall.
3. Memory integrity + persistence.
4. Tool/action reliability.
5. Self-improvement + rollback.
6. Governance/root-of-trust.
7. Runtime loop + recovery.

## Phán quyết kiến trúc

512 không còn là checklist trang trí.

Nó là **requirements contract**.

54 cores không còn được coi là proof của capability.

Chúng là **implementation responsibility graph**.

Chỉ runtime evidence được kiểm định độc lập mới có quyền chuyển một requirement sang `PASS`.

```text
CHANGE ≠ IMPROVEMENT
IMPROVEMENT ≠ PERMISSION
DOCUMENTATION ≠ IMPLEMENTATION
CORE EXISTENCE ≠ ATTRIBUTE PASS
```
