#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Any

CONTROL_ROOT = Path("DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT")
AUTOPILOT_ROOT = CONTROL_ROOT / "AUTOPILOT"
STATE_PATH = CONTROL_ROOT / "HKA_CURRICULUM_STATE.json"
REGISTRY_PATH = CONTROL_ROOT / "WINDOW_REGISTRY.json"
DIRECTOR_STATUS_PATH = CONTROL_ROOT / "STATUS_REPORTS/DIRECTOR-W01/STATUS.json"
CONTINUITY_PATH = CONTROL_ROOT / "HKA_DIRECTOR_CONTINUITY_SNAPSHOT.json"
FOUNDATIONAL_PATH = CONTROL_ROOT / "HKA_FOUNDATIONAL_13_YEAR_COVERAGE_GATE.json"
CONTROL_PATH = AUTOPILOT_ROOT / "HKA_AUTOPILOT_CONTROL.json"
SENTINEL_BRANCH = "hka-tree/director-backup-sentinel"
SENTINEL_STATUS_PATH = f"{CONTROL_ROOT.as_posix()}/STATUS_REPORTS/DIRECTOR-BACKUP-S01/STATUS.json"
B14_FAMILY = "C01-W05-B1.4-EARTH-UNIVERSE-FAMILY"
B15_FAMILY = "C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY"
B1_INTEGRATION = "C01-W07-B1-INTEGRATION-LOCK"


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def git(*args: str, check: bool = True) -> str:
    p = subprocess.run(["git", *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode != 0:
        raise RuntimeError(p.stderr.strip() or f"git {' '.join(args)} failed")
    return p.stdout.strip()


def control_head() -> str:
    return git("rev-parse", "HEAD")


def git_show_json(branch: str, path: str) -> dict[str, Any] | None:
    for ref in (f"origin/{branch}", branch):
        p = subprocess.run(["git", "show", f"{ref}:{path}"], text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if p.returncode == 0:
            try:
                data = json.loads(p.stdout)
                return data if isinstance(data, dict) else None
            except json.JSONDecodeError:
                return None
    return None


def find_window(registry: dict[str, Any], window_id: str) -> dict[str, Any] | None:
    for stage in registry.get("stages", []):
        for window in stage.get("windows", []):
            if window.get("window_id") == window_id:
                return window
            for child in window.get("children", []):
                if child.get("window_id") == window_id:
                    return child
    return None


def family_windows(registry: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for stage in registry.get("stages", []):
        if stage.get("stage_id") != "CURRICULUM":
            continue
        for window in stage.get("windows", []):
            if window.get("children"):
                out.append(window)
    return out


def validate() -> dict[str, Any]:
    state = read_json(STATE_PATH)
    registry = read_json(REGISTRY_PATH)
    director = read_json(DIRECTOR_STATUS_PATH)
    continuity = read_json(CONTINUITY_PATH)
    foundational = read_json(FOUNDATIONAL_PATH)
    control = read_json(CONTROL_PATH)
    errors: list[str] = []
    warnings: list[str] = []

    if not control.get("enabled"):
        warnings.append("AUTOPILOT_DISABLED")
    if control.get("control_plane_branch") != "hka-tree/curriculum-master":
        errors.append("CONTROL_PLANE_BRANCH_MISMATCH")
    if state.get("current_stage") != "CURRICULUM":
        errors.append("CURRENT_STAGE_NOT_CURRICULUM")
    if director.get("stage") != "CURRICULUM":
        errors.append("DIRECTOR_STAGE_NOT_CURRICULUM")
    if continuity.get("pipeline_lock", {}).get("all_later_stages_gated") is not True:
        errors.append("CONTINUITY_LATER_STAGES_NOT_GATED")
    if foundational.get("stage") != "CURRICULUM":
        errors.append("FOUNDATIONAL_GATE_STAGE_NOT_CURRICULUM")

    for stage_name, status in state.get("stage_status", {}).items():
        if stage_name not in {"KNOWLEDGE", "CURRICULUM"} and status not in {"GATED", "LOCKED", "LOCKED_INPUT"}:
            errors.append(f"LATER_STAGE_NOT_GATED:{stage_name}:{status}")

    for family in family_windows(registry):
        children = family.get("children", [])
        live = [c for c in children if c.get("unlocked") is True and c.get("status") not in {"PASS"}]
        if len(live) > 1:
            errors.append(f"MULTIPLE_UNFINISHED_CHILDREN_UNLOCKED:{family.get('window_id')}")
        for i, child in enumerate(children):
            if child.get("status") == "ELIGIBLE_FOR_DIRECTOR_UNLOCK_OPENING":
                if child.get("unlocked") is not False:
                    errors.append(f"ELIGIBLE_CHILD_ALREADY_UNLOCKED:{child.get('window_id')}")
                if i == 0:
                    errors.append(f"FIRST_CHILD_ELIGIBLE_WITHOUT_FAMILY_OPEN:{child.get('window_id')}")
                else:
                    prev = children[i - 1]
                    if not (prev.get("status") == "PASS" and prev.get("director_accepted") is True and prev.get("post_acceptance_sentinel") == "TREE_ALIGNMENT_PASS"):
                        errors.append(f"SUCCESSOR_ELIGIBLE_WITHOUT_ACCEPTED_SENTINEL_PREDECESSOR:{child.get('window_id')}")

    if state.get("gates", {}).get("B1_5_unlock") is True:
        b14 = find_window(registry, B14_FAMILY)
        if not b14 or b14.get("status") != "PASS":
            errors.append("B1_5_UNLOCKED_BEFORE_B1_4_PASS")

    active_registry = registry.get("active_transition", {})
    if active_registry.get("window_id") and state.get("active_window") and active_registry.get("window_id") != state.get("active_window"):
        if active_registry.get("status") not in {"DIRECTOR_ACCEPTED_PASS_SENTINEL_ALIGNED", "PASS"}:
            errors.append("STATE_REGISTRY_ACTIVE_WINDOW_MISMATCH")

    return {"ok": not errors, "control_plane_sha": control_head(), "errors": errors, "warnings": warnings, "autopilot_status": control.get("status")}


def inspect_worker_status(child: dict[str, Any]) -> dict[str, Any] | None:
    branch = child.get("execution_branch")
    window_id = child.get("window_id")
    if not branch or not window_id:
        return None
    return git_show_json(str(branch), f"{CONTROL_ROOT.as_posix()}/STATUS_REPORTS/{window_id}/STATUS.json")


def inspect_sentinel_status(target: dict[str, Any]) -> dict[str, Any] | None:
    data = git_show_json(SENTINEL_BRANCH, SENTINEL_STATUS_PATH)
    if not data:
        return None
    fresh = data.get("fresh_alignment", {})
    if fresh.get("accepted_window") != target.get("window_id"):
        return None
    expected_sha = target.get("accepted_commit_sha")
    if expected_sha and fresh.get("accepted_commit_sha") and fresh.get("accepted_commit_sha") != expected_sha:
        return None
    expected_cp = target.get("director_acceptance_checkpoint_commit") or target.get("director_acceptance_checkpoint")
    if expected_cp and fresh.get("director_acceptance_checkpoint") and fresh.get("director_acceptance_checkpoint") != expected_cp:
        return None
    return data


def process_family(family: dict[str, Any], validation: dict[str, Any]) -> dict[str, Any] | None:
    family_status = family.get("status")
    family_id = family.get("window_id")

    if family_status in {"DIRECTOR_ACCEPTED_INTEGRATION_SENTINEL_PENDING", "FAMILY_INTEGRATION_SENTINEL_PENDING"}:
        sentinel = inspect_sentinel_status(family)
        if sentinel and sentinel.get("status") == "TREE_ALIGNMENT_PASS":
            return make_request("RUN_DIRECTOR_APPLY_FAMILY_SENTINEL_EXIT", "DIRECTOR", family_id, family.get("family_branch"), ["Fresh family-exit Sentinel TREE_ALIGNMENT_PASS is durable; Director must apply exit separately."], validation)
        if sentinel and sentinel.get("status") in {"TREE_ALIGNMENT_ALERT", "RECOVERY_REQUIRED"}:
            return make_request("RUN_DIRECTOR_SENTINEL_ALERT_REVIEW", "DIRECTOR", family_id, family.get("family_branch"), [f"Fresh family Sentinel returned {sentinel.get('status')}."], validation)
        return make_request("RUN_SENTINEL", "SENTINEL", family_id, family.get("family_branch"), ["Director family integration/mapping acceptance exists; fresh family-exit Sentinel required."], validation)

    if family_status != "IN_PROGRESS":
        return None

    children = family.get("children", [])
    for child in children:
        status = child.get("status")
        window_id = child.get("window_id")
        branch = child.get("execution_branch")

        if status == "REPAIR_REQUIRED":
            return make_request("RUN_WORKER_REPAIR", "WORKER", window_id, branch, [child.get("repair_required") or "Director repair required"], validation, prompt_path="GPT_EXECUTION_PROMPT.md")

        if status == "READY":
            worker_status = inspect_worker_status(child)
            if worker_status:
                ws = worker_status.get("status")
                if ws == "PASS_CANDIDATE":
                    return make_request("RUN_DIRECTOR_REVIEW", "DIRECTOR", window_id, branch, ["Worker durable STATUS is PASS_CANDIDATE."], validation)
                if ws in {"BLOCK", "BLOCKED", "BLOCKED_EXTERNAL"}:
                    return make_request("RUN_DIRECTOR_BLOCK_REVIEW", "DIRECTOR", window_id, branch, [f"Worker durable STATUS is {ws}."], validation)
            return make_request("RUN_WORKER", "WORKER", window_id, branch, ["Registered child is READY."], validation, prompt_path="GPT_EXECUTION_PROMPT.md")

        if status in {"DIRECTOR_ACCEPTED_PASS_SENTINEL_PENDING", "DIRECTOR_ACCEPTED_PASS_PENDING_SENTINEL"}:
            sentinel = inspect_sentinel_status(child)
            if sentinel and sentinel.get("status") == "TREE_ALIGNMENT_PASS":
                return make_request("RUN_DIRECTOR_APPLY_SENTINEL_RESULT", "DIRECTOR", window_id, branch, ["Fresh post-acceptance Sentinel TREE_ALIGNMENT_PASS is durable; Director must apply it separately."], validation)
            if sentinel and sentinel.get("status") in {"TREE_ALIGNMENT_ALERT", "RECOVERY_REQUIRED"}:
                return make_request("RUN_DIRECTOR_SENTINEL_ALERT_REVIEW", "DIRECTOR", window_id, branch, [f"Fresh Sentinel returned {sentinel.get('status')}."], validation)
            return make_request("RUN_SENTINEL", "SENTINEL", window_id, branch, ["Director acceptance exists; fresh post-acceptance Sentinel required."], validation)

        if status == "ELIGIBLE_FOR_DIRECTOR_UNLOCK_OPENING":
            return make_request("RUN_DIRECTOR_OPEN_SUCCESSOR", "DIRECTOR", window_id, branch, ["All predecessor acceptance + Sentinel gates passed; child remains unlocked=false."], validation)

        if status == "LOCKED":
            return make_request("HOLD_LOCKED", "ORCHESTRATOR", window_id, branch, ["First unfinished child is locked; predecessor gate not satisfied."], validation)

        if status == "PASS":
            continue

        return make_request("HALT_UNKNOWN_CHILD_STATUS", "ORCHESTRATOR", window_id, branch, [f"Unknown child status: {status}"], validation)

    return make_request("RUN_FAMILY_INTEGRATION_EXIT", "DIRECTOR", family_id, family.get("family_branch"), ["All registered family children are PASS; family integration, foundational coverage, external general-education mapping and exit governance are next."], validation)


def plan() -> dict[str, Any]:
    validation = validate()
    if not validation["ok"]:
        return make_request("HALT_INVALID_CONTROL_PLANE", "ORCHESTRATOR", None, None, validation["errors"], validation)

    registry = read_json(REGISTRY_PATH)
    for family in family_windows(registry):
        result = process_family(family, validation)
        if result:
            return result

    b14 = find_window(registry, B14_FAMILY)
    b15 = find_window(registry, B15_FAMILY)
    if b14 and b14.get("status") == "PASS" and b15 and b15.get("status") == "LOCKED":
        return make_request("RUN_DIRECTOR_OPEN_B1_5", "DIRECTOR", B15_FAMILY, None, ["B1.4 family exit PASS; B1.5 requires separate Director family opening resolved from frozen architecture."], validation)

    if b15 and b15.get("status") == "PASS":
        integration = find_window(registry, B1_INTEGRATION)
        if integration and integration.get("status") == "LOCKED":
            return make_request("RUN_DIRECTOR_OPEN_B1_INTEGRATION_LOCK", "DIRECTOR", B1_INTEGRATION, None, ["B1.5 family exit PASS; B1 integration lock is the next separate governance transition."], validation)

    return make_request("HOLD_NO_ELIGIBLE_TRANSITION", "ORCHESTRATOR", None, None, ["No eligible automated transition found in durable registry."], validation)


def make_request(action: str, role: str, window_id: str | None, branch: str | None, reasons: list[Any], validation: dict[str, Any], prompt_path: str | None = None) -> dict[str, Any]:
    control = read_json(CONTROL_PATH)
    material = "|".join([validation.get("control_plane_sha", ""), action, window_id or "", branch or ""])
    request_id = hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]
    return {
        "schema_version": "1.1",
        "request_id": request_id,
        "action": action,
        "role": role,
        "target_window": window_id,
        "target_branch": branch,
        "prompt_path": prompt_path,
        "control_plane_branch": control.get("control_plane_branch"),
        "control_plane_sha": validation.get("control_plane_sha"),
        "reasons": [r for r in reasons if r],
        "guardrails": {
            "stage": "CURRICULUM",
            "canonical_tree_commit": "fc799bf1104ab6352710e1801777a971b5179995",
            "b1_architecture_commit": "265bb584b5d7e36e11091289d58558408880118c",
            "scope_map_blob_sha": "bedef47958a728e3f0d56d412f7bdea3ec465856",
            "worker_cannot_self_accept": True,
            "director_acceptance_required": True,
            "fresh_post_acceptance_sentinel_required": True,
            "sentinel_cannot_unlock": True,
            "successor_opening_is_separate_transition": True,
            "accepted_academic_artifacts_immutable": True,
            "future_locked_support_must_equal": 0,
            "cross_scope_academic_mutation_must_equal": 0,
        },
    }


def api_request(method: str, url: str, token: str, payload: dict[str, Any] | None = None) -> Any:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else None


def dispatch(request_obj: dict[str, Any]) -> dict[str, Any]:
    action = request_obj.get("action", "")
    if action.startswith("HOLD_") or action.startswith("HALT_"):
        return {"dispatched": False, "mode": "none", "reason": action}
    token = os.getenv("GITHUB_TOKEN", "").strip()
    repo = os.getenv("GITHUB_REPOSITORY", "").strip()
    if not token or not repo:
        return {"dispatched": False, "mode": "none", "reason": "GitHub queue credentials unavailable"}
    marker = f"<!-- hka-autopilot-request:{request_obj['request_id']} -->"
    issues_url = f"https://api.github.com/repos/{repo}/issues"
    try:
        issues = api_request("GET", issues_url + "?state=open&per_page=100", token) or []
        for issue in issues:
            if issue.get("pull_request"):
                continue
            if marker in (issue.get("body") or ""):
                return {"dispatched": True, "mode": "github_issue_existing", "issue_number": issue.get("number")}
        body = marker + "\n\n```json\n" + json.dumps(request_obj, ensure_ascii=False, indent=2) + "\n```\n\nHKA Autopilot durable run request. Preserve role separation and Knowledge Tree alignment."
        created = api_request("POST", issues_url, token, {"title": f"[HKA AUTOPILOT] {request_obj['role']} · {request_obj['action']} · {request_obj.get('target_window') or 'control-plane'}", "body": body})
        return {"dispatched": True, "mode": "github_issue_created", "issue_number": created.get("number")}
    except Exception as exc:
        return {"dispatched": False, "mode": "none", "reason": str(exc)}


def main() -> int:
    ap = argparse.ArgumentParser(description="HKA curriculum governance autopilot")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("plan")
    dp = sub.add_parser("dispatch")
    dp.add_argument("--request", required=True)
    args = ap.parse_args()
    if args.cmd == "validate":
        result = validate()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["ok"] else 2
    if args.cmd == "plan":
        print(json.dumps(plan(), ensure_ascii=False, indent=2))
        return 0
    if args.cmd == "dispatch":
        with open(args.request, "r", encoding="utf-8") as f:
            request_obj = json.load(f)
        print(json.dumps(dispatch(request_obj), ensure_ascii=False, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
