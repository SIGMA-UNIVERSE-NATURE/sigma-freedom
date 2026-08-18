# SIGMA Native Brain 54×512 — Candidate v0.1

## Mục tiêu

Bắt đầu viết lại **chương trình SIGMA bằng chính ngôn ngữ SIGMA** mà không giả rằng toàn bộ hệ thống đã được chuyển đổi.

Candidate này tạo vertical slice thực thi đầu tiên cho chương trình:

`54 CORES → 512 SKILLS → ACCURACY / TRUTH / PROVENANCE KERNEL`

Nó được tách khỏi `SIGMA_LIFE`; canonical không bị sửa.

## Những gì đã được viết bằng SIGMA

Source được tạo tại `src/sigma_native_brain_54x512_v0_1.sigma` từ các module SIGMA đã lưu trong `src/`:

- registry thực thi cho đủ 54 core IDs và tên canonical;
- router liên tục cho đủ skill IDs `1..512` theo 31 section canonical;
- phân loại epistemic state;
- provenance completeness gate;
- canonical/machine/memory reconciliation;
- anti-self-deception progress gate;
- reality-over-narrative check;
- UTF-8 Vietnamese golden output.

Vertical slice bám trực tiếp các cores:

`09, 20, 21, 26, 27, 31, 32, 43, 44, 45, 46, 52, 53`.

## Những gì chưa được tuyên bố

- Chưa phải full 54-core implementation.
- Chưa phải full 512-skill behavioral implementation.
- Chưa compile/run trên HP hoặc OPPO.
- Chưa có differential evidence.
- Chưa có independent evaluator.
- Chưa được PROMOTE.
- Không thay thế Python 54-core contracts hay canonical state.

## Lý do bắt đầu ở accuracy

Cores 20, 21, 43, 45 và 52 khóa các nguyên tắc:

- uncertainty là dữ liệu hạng nhất;
- evidence cao hơn confidence;
- metric đang tối ưu không tự chứng minh tiến bộ;
- knowledge phải có provenance đầy đủ;
- observation cao hơn internal narrative.

Mojibake ở Lesson 001 được đưa thành hard regression gate: chuỗi tiếng Việt phải khớp exact bytes.

## Chuỗi kiểm chứng bắt buộc

`SOURCE → SIGMAC → SIGMAB → SIGMA-HOSTVM → EXACT UTF-8 STDOUT → CORPUS → DETERMINISM → FOUNDATION/ABI REGRESSION → INDEPENDENT EVALUATION`

Không hoàn thành chuỗi này thì decision vẫn là `HOLD`.

## Cách tạo source compile target

```bash
python3 tools/assemble_candidate.py
python3 tools/validate_candidate.py
```

Header bắt buộc hiện là:

```sigma
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.BRAIN][VERSION=0.1]
```

Static validation hiện đạt `14/14`, nhưng chỉ chứng minh cấu trúc, UTF-8 và sự nhất quán hợp đồng; chưa phải bằng chứng biên dịch hoặc thực thi.

## Runtime đúng cho v0.1

Candidate dùng `LNEW/LPUSH/LGET` và `MNEW/MSET/MGET`, nên gate thực thi dùng `sigma-hostvm`. Không tuyên bố `sigma-vm` thuần có đủ host primitives cho vertical slice này.
