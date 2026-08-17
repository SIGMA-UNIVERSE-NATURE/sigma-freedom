#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SHA40 = re.compile(r"^[0-9a-f]{40}$")
NAME = re.compile(r"^HAND TO HAND_ CỬA ([1-9][0-9]*)$")


def fail(msg: str) -> None:
    raise SystemExit("SIGMA_WINDOW_IDENTITY_CONTRACT: FAIL\n" + msg)


def load(path: Path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot parse {path}: {exc}")
    if not isinstance(value, dict):
        fail(f"not object: {path}")
    return value


def main() -> None:
    protocol = load(HERE / "WINDOW_IDENTITY_PROTOCOL.json")
    active = load(HERE / "ACTIVE_WINDOW_IDENTITY.json")

    if protocol.get("status") != "CANONICAL_REQUIRED":
        fail("identity protocol is not canonical-required")
    if protocol.get("state_match_rule") != "FIND_EXACT_WINDOW_STATE -> VERIFY_LATEST_CANONICAL_STATE -> STATE_MATCH -> CONTINUE_WORK":
        fail("state-match rule mismatch")
    if protocol.get("failure_rule") != "NO_STATE_MATCH = NO_CONTINUATION":
        fail("failure rule mismatch")

    required_active = [
        "window_id", "window_name", "window_sequence", "created_at", "purpose_short",
        "birth_certificate", "predecessor_checkpoint", "authority_role", "handoff_state",
    ]
    for key in required_active:
        if active.get(key) in (None, ""):
            fail(f"active identity missing {key}")

    match = NAME.fullmatch(str(active["window_name"]))
    if not match:
        fail("active window name does not match canonical naming pattern")
    if int(match.group(1)) != int(active["window_sequence"]):
        fail("active window name/sequence mismatch")
    if not SHA40.fullmatch(str(active["predecessor_checkpoint"])):
        fail("active predecessor checkpoint is not SHA40")

    birth_rel = Path(str(active["birth_certificate"]))
    birth_path = REPO / birth_rel
    if not birth_path.is_file():
        fail(f"birth certificate missing: {birth_rel.as_posix()}")
    birth = load(birth_path)

    for key in protocol.get("birth_certificate_required_fields", []):
        if birth.get(key) in (None, ""):
            fail(f"birth certificate missing required field {key}")

    for key in ("window_id", "window_name", "window_sequence", "created_at", "authority_role", "handoff_state", "predecessor_checkpoint"):
        if birth.get(key) != active.get(key):
            fail(f"active pointer/birth mismatch: {key}")

    birth_match = NAME.fullmatch(str(birth["window_name"]))
    if not birth_match or int(birth_match.group(1)) != int(birth["window_sequence"]):
        fail("birth window name/sequence mismatch")
    if birth.get("record_type") != "IMMUTABLE_WINDOW_BIRTH_CERTIFICATE":
        fail("birth record type mismatch")
    if birth.get("purpose") in (None, "") or birth.get("work_scope") in (None, ""):
        fail("birth purpose/work scope missing")
    if birth.get("state_match_rule") != protocol.get("state_match_rule"):
        fail("birth state-match rule mismatch")
    if birth.get("failure_rule") != protocol.get("failure_rule"):
        fail("birth failure rule mismatch")

    print("SIGMA_WINDOW_IDENTITY_CONTRACT: PASS")
    print(f"WINDOW_ID={active['window_id']}")
    print(f"WINDOW_NAME={active['window_name']}")
    print(f"WINDOW_SEQUENCE={active['window_sequence']}")
    print(f"CREATED_AT={active['created_at']}")
    print(f"PREDECESSOR_CHECKPOINT={active['predecessor_checkpoint']}")
    print(f"AUTHORITY_ROLE={active['authority_role']}")
    print(f"HANDOFF_STATE={active['handoff_state']}")


if __name__ == "__main__":
    main()
