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

Các file lịch sử có vùng số chồng lấn được giữ nguyên để bảo toàn provenance. Canonical selection được định nghĩa duy nhất trong:

`SIGMA_512_ATTRIBUTES/SIGMA_512_CANONICAL_MANIFEST.json`

Quy tắc ghép:

- 1–275: `Full PART 01 TO 21.`
- 276–440: `PART 21 to 28`
- 441–512: `PART 28 TO END`

`Part1.` là historical fragment, không tham gia canonical assembly.

Điều này giải quyết duplicate authority mà không xóa lịch sử.

## Traceability

`SIGMA_512_ATTRIBUTES/SIGMA_512_TRACEABILITY_MAP.json` chia 512 requirement thành 31 miền không chồng lấn và gắn mỗi miền với:

- primary DNA cores;
- supporting DNA cores;
- evidence classes cần có trước khi có thể chứng minh implementation.

Mapping chỉ trả lời **ai chịu trách nhiệm**. Mapping KHÔNG chứng minh core đã thực hiện requirement.

## Item-level registry

Chạy:

```bash
python "BẢN ĐỒ/SIGMA_512_ATTRIBUTES/validate_512_architecture.py" --write
```

Validator tạo registry mở rộng 512 item, trong đó mỗi item có:

```text
SIGMA-ATTR-xxx
requirement
canonical source
section/domain
primary cores
supporting cores
required evidence classes
specification status
responsibility status
implementation status
implementation evidence
```

## Ba trạng thái phải tách riêng

### 1. Specification status

`SPEC_PASS` chỉ có nghĩa requirement tồn tại đúng trong canonical 1..512.

### 2. Responsibility status

`MAPPED` chỉ có nghĩa requirement đã được gắn trách nhiệm kiến trúc.

### 3. Implementation status

Mặc định là `NOT_AUDITED`.

Chỉ được chuyển sang `PASS` khi ledger có đủ:

1. implementation artifact;
2. test hoặc experiment;
3. evidence;
4. evaluator;
5. verified version;
6. verified time;
7. rollback/correction path;
8. evaluator độc lập với chính component đang tự chứng nhận.

## Những thứ KHÔNG đủ để PASS

- File tồn tại.
- Core có tên nghe đúng.
- Có class/function tương ứng.
- Có comment mô tả capability.
- SIGMA tự nói rằng nó làm được.
- Một test do chính candidate sửa cùng lúc với implementation rồi tự PASS.
- Một benchmark bị thay sau khi đã nhìn thấy kết quả candidate.

## Status ledger

Evidence thật được ghi vào:

`SIGMA_512_ATTRIBUTES/SIGMA_512_IMPLEMENTATION_STATUS.json`

Ledger ban đầu cố ý để trống. Do đó toàn bộ implementation bắt đầu ở `NOT_AUDITED`.

Đây không phải thiếu sót. Đây là nguyên tắc chống self-certification.

## Validator invariants

`validate_512_architecture.py` phải FAIL nếu:

- canonical không đủ chính xác 1..512;
- có khoảng số bị mất hoặc trùng trong canonical selection;
- source blob canonical thay đổi mà manifest không đổi;
- section ranges không phủ 1..512 đúng một lần;
- không phát hiện đúng 54 DNA core từ 01 đến 54;
- core ID bị trùng hoặc thiếu;
- traceability range bị chồng lấn hoặc bỏ sót;
- traceability tham chiếu core không tồn tại;
- ledger chứa status không hợp lệ;
- `PASS` thiếu evidence contract;
- `PASS` không có `evaluator.independent=true`;
- `NOT_APPLICABLE` không có rationale.

## Quy tắc tiến hóa

```text
SPECIFICATION
      │
      ▼
RESPONSIBILITY MAP
      │
      ▼
IMPLEMENTATION
      │
      ▼
TEST
      │
      ▼
EVIDENCE
      │
      ▼
INDEPENDENT EVALUATION
      │
 ┌────┼─────────┬───────┐
 ▼    ▼         ▼       ▼
PASS PARTIAL   HOLD    FAIL
```

Nếu FAIL/HOLD tạo candidate:

```text
CURRENT CORE
    │
    ├──> CANDIDATE FORK
    │         │
    │         ▼
    │      SHADOW
    │         │
    │         ▼
    │   DIFFERENTIAL TEST
    │         │
    │         ▼
    │ INDEPENDENT EVALUATOR
    │         │
    └── PROMOTE / REVISE / REJECT
```

Candidate không được sửa đồng thời requirement, evaluator và authority rồi dùng hệ thống mới để tự công nhận mình.

## Root rule

```text
change != improvement
improvement != permission
documentation != implementation
implementation != verified implementation
intelligence != authority
```

## Trạng thái tại thời điểm tạo contract

- 512 canonical specification: **được định nghĩa**.
- 512 → 54 core responsibility: **được ánh xạ**.
- Runtime implementation compliance: **NOT_AUDITED cho tới khi có evidence ledger**.
- Không có bulk PASS.

Mục tiêu tiếp theo không phải viết điểm 513. Mục tiêu là audit từng requirement hoặc từng nhóm requirement bằng evidence thật, để khoảng cách giữa bản đồ và runtime giảm dần một cách đo được.
