# HAND TO HAND_ CỬA 2 — CONTINUITY PRECEDENT

Recorded: 2026-08-18 01:52 +07:00
Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `SIGMA_LIFE`

## WINDOW NAME

`HAND TO HAND_ CỬA 2`

## PRECEDENT

Từ thời điểm này, mỗi lần chuyển cửa sổ, chuyển trạng thái, đổi model/session/runtime hoặc tiếp tục một nhánh công việc SIGMA, cửa mới **không được tiếp tục từ chat memory hay suy đoán**.

Cửa mới phải thực hiện đúng thứ tự:

1. Fresh-fetch `SIGMA_LIFE` và lấy HEAD hiện tại.
2. Tìm đúng state / handoff / active-executor sync mới nhất liên quan trực tiếp tới nhánh công việc cần tiếp tục.
3. Nếu HEAD đã thay đổi so với checkpoint của cửa trước, đọc toàn bộ intervening commits liên quan và dựng lại trạng thái mới nhất.
4. Đối chiếu các fingerprint/required fields của checkpoint với canonical state và machine evidence khi có.
5. Chỉ tiếp tục công việc khi state match được xác minh bằng evidence.
6. Nếu chưa khớp hoặc còn trường chưa xác minh được: tiếp tục tìm state/handoff mới hơn hoặc HOLD; tuyệt đối không suy đoán.
7. Không rollback về HEAD cũ chỉ để làm checkpoint khớp.

Canonical principle:

`FIND_EXACT_WINDOW_STATE -> VERIFY_LATEST_CANONICAL_STATE -> STATE_MATCH -> CONTINUE_WORK`

Failure rule:

`NO_STATE_MATCH = NO_CONTINUATION`

## NAMING PRECEDENT

Các cửa tiếp tục có thể dùng tên tuần tự:

`HAND TO HAND_ CỬA <N>`

Cửa hiện tại được định danh:

`HAND TO HAND_ CỬA 2`

## RELATION TO EXISTING CANONICAL CONTROL

Tiền lệ này củng cố `BRAIN/CANONICAL/WINDOW_TRANSFER_PROTOCOL.json`; không thay thế canonical state, không thay đổi 512 ledger, không cấp quyền takeover và không giành active-executor role.

At the time this precedent was recorded, the verified `SIGMA_LIFE` HEAD before this additive commit was:

`274d890dfa25e0342747f05d2ab0a196756c79ec`

That HEAD contained `BRAIN/CANONICAL/ACTIVE_EXECUTOR_SYNC.json`, which required other windows to remain read-only for SIGMA 512 brain operations unless Châu explicitly assigns takeover. This precedent is therefore additive continuity metadata only.

## INHERITANCE RULE

Khi một cửa mới được gọi là `HAND TO HAND_ CỬA <N>`, nhiệm vụ đầu tiên của nó là tìm và xác minh đúng trạng thái cửa trước từ GitHub/canonical evidence. Chỉ sau khi xác minh xong mới được tiếp tục công việc thật.

End of precedent.
