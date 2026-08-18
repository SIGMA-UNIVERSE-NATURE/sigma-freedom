from __future__ import annotations

import json
import os
import time
from pathlib import Path

LESSON_PATH = Path("BRAIN/CANONICAL/SIGMA_BRAIN_TRAINING_LESSON.json")
RESULT_NAME = "sigma_brain_training_bridge_result.json"
MAX_WAIT_SECONDS = 240
POLL_SECONDS = 2


def safe_id(value: object) -> str:
    text = str(value or "")
    safe = "".join(c for c in text if c.isalnum() or c in "-_")[:120]
    if not safe or safe != text:
        raise ValueError("unsafe_lesson_id")
    return safe


def atomic_write(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(raw)
    os.replace(tmp, path)


def main() -> int:
    output_dir = Path(os.environ["SIGMA_HARNESS_OUTPUT_DIR"]).resolve()
    # .../<workspace>/.CANONICAL_512/OUTPUT/<request>/<head>
    workspace = output_dir.parents[3]
    queue = workspace / "SIGMA_BOX_QUEUE"
    pending = queue / "PENDING"
    delivered = queue / "DELIVERED"
    rejected = queue / "REJECTED"
    results = queue / "RESULTS"
    for d in (pending, delivered, rejected, results):
        d.mkdir(parents=True, exist_ok=True)

    lesson = json.loads(LESSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(lesson, dict):
        raise ValueError("lesson_not_object")
    lesson_id = safe_id(lesson.get("lesson_id"))
    problem = lesson.get("problem")
    if not isinstance(problem, str) or not problem.strip():
        raise ValueError("lesson_problem_missing")

    task = {
        "problem_id": lesson_id,
        "project_id": "SIGMA_BRAIN",
        "workstream_id": "REMOTE_CONTINUITY",
        "problem": problem,
        "training_contract": {
            "target_capability": lesson.get("target_capability"),
            "previous_verified_baseline": lesson.get("previous_verified_baseline"),
            "success_metric": lesson.get("success_metric"),
            "regression_surfaces": lesson.get("regression_surfaces"),
            "teacher": "MINH_CUA_3",
            "self_promotion_allowed": False,
            "answer_must_be_evidence_labeled": True,
        },
    }

    result_path = results / f"{lesson_id}_RESULT.json"
    rejected_matches = list(rejected.glob(f"{lesson_id}*.json"))

    queued = False
    if not result_path.is_file() and not rejected_matches:
        pending_path = pending / f"{lesson_id}.json"
        if not pending_path.exists():
            atomic_write(
                pending_path,
                (json.dumps(task, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
            )
            queued = True

    deadline = time.monotonic() + MAX_WAIT_SECONDS
    sigma_raw = None
    bridge_state = "WAITING"
    reject_evidence = None
    while time.monotonic() < deadline:
        if result_path.is_file():
            sigma_raw = result_path.read_text(encoding="utf-8-sig", errors="replace")
            bridge_state = "SIGMA_RESULT_OBSERVED"
            break
        rejects = sorted(rejected.glob(f"{lesson_id}*.json"))
        if rejects:
            reject_evidence = [
                {"name": p.name, "content": p.read_text(encoding="utf-8-sig", errors="replace")[:8000]}
                for p in rejects[:4]
            ]
            bridge_state = "QUEUE_REJECTED"
            break
        time.sleep(POLL_SECONDS)

    parsed = None
    if sigma_raw is not None:
        try:
            parsed = json.loads(sigma_raw)
        except Exception:
            parsed = {"raw_text": sigma_raw[:24000]}

    observed = sigma_raw is not None
    counts = {
        "TARGET_COUNT": 1,
        "PASS": 0,
        "PARTIAL": 1 if observed else 0,
        "HOLD": 0 if observed else 1,
        "FAIL": 0,
        "NOT_AUDITED": 0,
    }
    payload = {
        "schema_version": "1.0.0",
        "harness_id": "SIGMA-BRAIN-TRAINING-BRIDGE",
        "harness_version": "0.1.0",
        "lesson_id": lesson_id,
        "target_capability": lesson.get("target_capability"),
        "bridge_state": bridge_state,
        "queued_by_this_run": queued,
        "sigma_result_observed": observed,
        "sigma_result": parsed,
        "queue_rejection_evidence": reject_evidence,
        "counts": counts,
        "target_count": 1,
        "core_modifications": 0,
        "external_side_effects": 0,
        "internal_workspace_bridge_write": True,
        "evaluation": {
            "status": "UNEVALUATED",
            "rule": "A machine-observed answer is not a PASS and not an intelligence improvement until compared against the locked baseline/metric.",
        },
    }
    out = output_dir / RESULT_NAME
    atomic_write(out, (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
