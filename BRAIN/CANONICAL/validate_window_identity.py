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

    expected_state_rule = (
        "FIND_EXACT_WINDOW_STATE -> VERIFY_LATEST_CANONICAL_STATE -> "
        "ANSWER_OPEN_STATE_CHALLENGE_FROM_EVIDENCE -> VERIFY_SUCCESSOR_RESPONSIBILITY_NO_REGRESSION -> "
        "STATE_MATCH -> CONTINUE_WORK"
    )
    if protocol.get("state_match_rule") != expected_state_rule:
        fail("state-match rule mismatch")
    if protocol.get("failure_rule") != "NO_STATE_MATCH_OR_ANY_FABRICATION_OR_UNEXPLAINED_VERIFIED_REGRESSION = NO_CONTINUATION":
        fail("failure rule mismatch")

    truth = protocol.get("truth_and_anti_fabrication_gate") or {}
    for key in (
        "no_fabrication",
        "no_fake_state",
        "no_simulation_presented_as_observation",
        "no_guessing_to_gain_identity_acceptance",
        "no_prompt_copying_as_identity_proof",
    ):
        if truth.get(key) is not True:
            fail(f"anti-fabrication gate not enforced: {key}")
    if truth.get("mode") != "FAIL_CLOSED":
        fail("anti-fabrication gate is not fail-closed")
    if truth.get("unknown_or_unverified_response") != "HOLD_WITH_EXACT_MISSING_EVIDENCE":
        fail("unknown/unverified response must HOLD")

    responsibility = protocol.get("successor_responsibility_gate") or {}
    if responsibility.get("mode") != "REQUIRED":
        fail("successor responsibility gate is not required")
    for key in (
        "inherit_verified_work_responsibly",
        "preserve_verified_guarantees",
        "continue_from_latest_valid_state_not_preferred_old_state",
        "seek_evidence_backed_improvement_over_predecessor",
        "do_not_degrade_verified_behavior_or_continuity",
        "regression_requires_explicit_evidence_scope_and_rollback",
    ):
        if responsibility.get(key) is not True:
            fail(f"successor responsibility invariant not enforced: {key}")
    if responsibility.get("unknown_effect_on_verified_guarantees") != "HOLD_BEFORE_MUTATION":
        fail("unknown regression effect must HOLD before mutation")

    challenge = protocol.get("open_state_challenge") or {}
    if challenge.get("required_before_continuity_acceptance") is not True:
        fail("open state challenge is not required")
    if int(challenge.get("minimum_open_questions", 0)) < 3:
        fail("open state challenge requires fewer than three questions")
    for key in (
        "questions_must_not_include_expected_answers",
        "answers_must_be_free_form_not_multiple_choice",
        "challenge_must_be_answered_after_fresh_fetch",
        "prompted_expected_values_do_not_count_as_proof",
    ):
        if challenge.get(key) is not True:
            fail(f"open challenge invariant missing: {key}")
    if len(challenge.get("question_classes") or []) < 3:
        fail("insufficient open challenge question classes")

    candidate = protocol.get("candidate_before_acceptance_rule") or {}
    if candidate.get("candidate_role") != "READ_ONLY_CONTINUITY_CANDIDATE":
        fail("candidate role must be read-only")
    if candidate.get("candidate_birth_record_is_not_identity_acceptance") is not True:
        fail("candidate birth record incorrectly counts as identity acceptance")
    if candidate.get("active_pointer_must_not_transfer_before_challenge_pass") is not True:
        fail("active pointer could transfer before challenge pass")
    if candidate.get("canonical_mutation_for_work_forbidden_before_acceptance") is not True:
        fail("candidate could mutate canonical work before acceptance")

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
    sequence = int(active["window_sequence"])
    if int(match.group(1)) != sequence:
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

    # Immutable birth facts must equal the live pointer. Authority/handoff are lifecycle fields.
    for key in ("window_id", "window_name", "window_sequence", "created_at", "predecessor_checkpoint"):
        if birth.get(key) != active.get(key):
            fail(f"active pointer/birth immutable mismatch: {key}")

    birth_match = NAME.fullmatch(str(birth["window_name"]))
    if not birth_match or int(birth_match.group(1)) != int(birth["window_sequence"]):
        fail("birth window name/sequence mismatch")
    if birth.get("record_type") != "IMMUTABLE_WINDOW_BIRTH_CERTIFICATE":
        fail("birth record type mismatch")
    if birth.get("purpose") in (None, "") or birth.get("work_scope") in (None, ""):
        fail("birth purpose/work scope missing")
    if birth.get("authority_role") in (None, "") or birth.get("handoff_state") in (None, ""):
        fail("birth lifecycle-at-registration fields missing")
    if active.get("authority_role") in (None, "") or active.get("handoff_state") in (None, ""):
        fail("active lifecycle fields missing")

    # Cửa 1/2 predate v1.1 and their immutable birth records must not be rewritten.
    # Every successor accepted as Cửa 3+ must carry anti-fabrication acceptance metadata.
    if sequence >= 3:
        successor = protocol.get("successor_birth_rule_effective_v1_1") or {}
        for key in successor.get("additional_fields") or []:
            if birth.get(key) in (None, ""):
                fail(f"v1.1+ successor birth missing {key}")
        if birth.get("anti_fabrication_gate_version") not in {"1.1", "1.1.0", "v1.1", "1.2", "1.2.0", "v1.2"}:
            fail("successor birth anti-fabrication gate version mismatch")
        if active.get("continuity_acceptance_state") != "ACCEPTED_OPEN_STATE_CHALLENGE_PASS":
            fail("successor active pointer lacks accepted open-state challenge")
        if active.get("open_state_challenge_result") != "PASS":
            fail("successor active pointer challenge result is not PASS")
        if int(active.get("open_state_challenge_question_count", 0)) < 3:
            fail("successor active pointer challenge count below three")
        if active.get("successor_responsibility_gate") != "PASS_PRESERVE_VERIFIED_GUARANTEES_NO_UNEXPLAINED_REGRESSION":
            fail("successor active pointer lacks responsibility/no-regression PASS")

    print("SIGMA_WINDOW_IDENTITY_CONTRACT: PASS")
    print(f"WINDOW_ID={active['window_id']}")
    print(f"WINDOW_NAME={active['window_name']}")
    print(f"WINDOW_SEQUENCE={active['window_sequence']}")
    print(f"CREATED_AT={active['created_at']}")
    print(f"PREDECESSOR_CHECKPOINT={active['predecessor_checkpoint']}")
    print(f"AUTHORITY_ROLE={active['authority_role']}")
    print(f"HANDOFF_STATE={active['handoff_state']}")
    print("ANTI_FABRICATION_GATE=ENFORCED_FAIL_CLOSED")
    print("OPEN_STATE_CHALLENGE_REQUIRED=true")
    print("MINIMUM_OPEN_QUESTIONS=3")
    print("SUCCESSOR_RESPONSIBILITY_GATE=REQUIRED")
    print("VERIFIED_REGRESSION_WITHOUT_EVIDENCE_OR_ROLLBACK=FORBIDDEN")


if __name__ == "__main__":
    main()
