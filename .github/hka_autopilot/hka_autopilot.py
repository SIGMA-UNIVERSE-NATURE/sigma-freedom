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
B14_FAMILY = "C01-W05-B1.4-EARTH-UNIVERSE-FAMILY"


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
    return None


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

    family = find_window(registry, B14_FAMILY)
    if family is None:
        errors.append("B1_4_FAMILY_NOT_REGISTERED")
    else:
        children = family.get("children", [])
        live_unlocked = [c for c in children if c.get("unlocked") is True and c.get("status") not in {"PASS"}]
        if len(live_unlocked) > 1:
            errors.append("MULTIPLE_UNFINISHED_B1_4_CHILDREN_UNLOCKED")

        for i, child in enumerate(children):
            if child.get("status") == "ELIGIBLE_FOR_DIRECTOR_UNLOCK_OPENING":
                if child.get("unlocked") is not False:
                    errors.append(f"ELIGIBLE_CHILD_ALREADY_UNLOCKED:{child.get('window_id')}")
                if i == 0:
                    errors.append("FIRST_CHILD_ELIGIBLE_WITHOUT_PREDECESSOR")
                else:
                    prev = children[i - 1]
                    if not (prev.get("status") == "PASS" and prev.get("director_accepted") is True and prev.get("post_acceptance_sentinel") == "TREE_ALIGNMENT_PASS"):
                        errors.append(f"SUCCESSOR_ELIGIBLE_WITHOUT_ACCEPTED_SENTINEL_PREDECESSOR:{child.get('window_id')}")

    gates = state.get("gates", {})
    subbranches = state.get("branches", [{}])[0].get("subbranches", []) if state.get("branches") else []
    b14_pass = any(sb.get("id") == "B1.4" and sb.get("status") == "PASS" for sb in subbranches if isinstance(sb, dict))
    if gates.get("B1_5_unlock") is True and not b14_pass:
        errors.append("B1_5_UNLOCKED_BEFORE_B1_4_PASS")

    active_registry = registry.get("active_transition", {})
    if active_registry.get("window_id") and state.get("active_window") and active_registry.get("window_id") != state.get("active_window"):
        if active_registry.get("status") not in {"DIRECTOR_ACCEPTED_PASS_SENTINEL_ALIGNED", "PASS"}:
            errors.append("STATE_REGISTRY_ACTIVE_WINDOW_MISMATCH")

    return {
        "ok": not errors,
        "control_plane_sha": control_head(),
        "errors": errors,
        "warnings": warnings,
        "autopilot_status": control.get("status")
    }


def inspect_worker_status(child: dict[str, Any]) -> dict[str, Any] | None:
    branch = child.get("execution_branch")
    window_id = child.get("window_id")
    if not branch or not window_id:
        return None
    path = f"{CONTROL_ROOT.as_posix()}/STATUS_REPORTS/{window_id}/STATUS.json"
    return git_show_json(branch, path)


def plan() -> dict[str, Any]:
    validation = validate()
    if not validation["ok"]:
        return make_request("HALT_INVALID_CONTROL_PLANE", "ORCHESTRATOR", None, None, validation["errors"], validation)

    registry = read_json(REGISTRY_PATH)
    family = find_window(registry, B14_FAMILY)
    if family is None:
        return make_request("HALT_MISSING_FAMILY", "ORCHESTRATOR", None, None, ["B1.4 family not registered"], validation)

    children = family.get("children", [])
    for child in children:
        status = child.get("status")
        window_id = child.get("window_id")
        branch = child.get("execution_branch")

        if status == "REPAIR_REQUIRED":
            return make_request("RUN_WORKER_REPAIR", "WORKER", window_id, branch,
                                [child.get("repair_required") or "Director repair required"], validation)

        if status == "READY":
            worker_status = inspect_worker_status(child)
            if worker_status:
                ws = worker_status.get("status")
                if ws == "PASS_CANDIDATE":
                    return make_request("RUN_DIRECTOR_REVIEW", "DIRECTOR", window_id, branch,
                                        ["Worker durable STATUS is PASS_CANDIDATE"], validation)
                if ws in {"BLOCK", "BLOCKED", "BLOCKED_EXTERNAL"}:
                    return make_request("RUN_DIRECTOR_BLOCK_REVIEW", "DIRECTOR", window_id, branch,
                                        [f"Worker durable STATUS is {ws}"], validation)
            return make_request("RUN_WORKER", "WORKER", window_id, branch,
                                ["Registered child is READY"], validation, prompt_path="GPT_EXECUTION_PROMPT.md")

        if status in {"DIRECTOR_ACCEPTED_PASS_SENTINEL_PENDING", "DIRECTOR_ACCEPTED_PASS_PENDING_SENTINEL"}:
            return make_request("RUN_SENTINEL", "SENTINEL", window_id, branch,
                                ["Director acceptance exists; fresh post-acceptance Sentinel required"], validation)

        if status == "ELIGIBLE_FOR_DIRECTOR_UNLOCK_OPENING":
            return make_request("RUN_DIRECTOR_OPEN_SUCCESSOR", "DIRECTOR", window_id, branch,
                                ["All predecessor acceptance + Sentinel gates passed; child remains unlocked=false"], validation)

        if status == "LOCKED":
            return make_request("HOLD_LOCKED", "ORCHESTRATOR", window_id, branch,
                                ["First unfinished child is locked; predecessor gate not satisfied"], validation)

        if status == "PASS":
            continue

    if family.get("status") == "PASS":
        return make_request("RUN_DIRECTOR_OPEN_B1_5", "DIRECTOR", "C01-W06-B1.5-INFORMATION-COMPUTATION-FAMILY", None,
                            ["B1.4 family PASS; B1.5 requires a separate Director opening"], validation)

    return make_request("RUN_B1_4_FAMILY_INTEGRATION_EXIT", "DIRECTOR", B14_FAMILY, family.get("family_branch"),
                        ["All B1.4 children appear PASS; family integration/exit governance is next"], validation)


def make_request(action: str, role: str, window_id: str | None, branch: str | None,
                 reasons: list[Any], validation: dict[str, Any], prompt_path: str | None = None) -> dict[str, Any]:
    control = read_json(CONTROL_PATH)
    material = "|".join([validation.get("control_plane_sha", ""), action, window_id or "", branch or ""])
    request_id = hashlib.sha256(material.encode("utf-8")).hexdigest()[:24]
    return {
        "schema_version": "1.0",
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
            "worker_cannot_self_accept": True,
            "director_acceptance_required": True,
            "fresh_post_acceptance_sentinel_required": True,
            "successor_opening_is_separate_transition": True,
            "accepted_academic_artifacts_immutable": True,
            "future_locked_support_must_equal": 0,
            "cross_scope_academic_mutation_must_equal": 0
        }
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

    webhook = os.getenv("HKA_AGENT_WEBHOOK_URL", "").strip()
    webhook_token = os.getenv("HKA_AGENT_WEBHOOK_TOKEN", "").strip()
    if webhook:
        data = json.dumps(request_obj).encode("utf-8")
        req = urllib.request.Request(webhook, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        if webhook_token:
            req.add_header("Authorization", f"Bearer {webhook_token}")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return {"dispatched": True, "mode": "webhook", "status": resp.status}
        except Exception as exc:
            webhook_error = str(exc)
    else:
        webhook_error = "HKA_AGENT_WEBHOOK_URL not configured"

    token = os.getenv("GITHUB_TOKEN", "").strip()
    repo = os.getenv("GITHUB_REPOSITORY", "").strip()
    if not token or not repo:
        return {"dispatched": False, "mode": "none", "reason": webhook_error}

    marker = f"<!-- hka-autopilot-request:{request_obj['request_id']} -->"
    issues_url = f"https://api.github.com/repos/{repo}/issues"
    try:
        issues = api_request("GET", issues_url + "?state=open&per_page=100", token) or []
        for issue in issues:
            if issue.get("pull_request"):
                continue
            if marker in (issue.get("body") or ""):
                return {"dispatched": True, "mode": "github_issue_existing", "issue_number": issue.get("number")}

        body = marker + "\n\n```json\n" + json.dumps(request_obj, ensure_ascii=False, indent=2) + "\n```\n\n"
        body += "This issue is an HKA Autopilot run request. The executing agent must preserve role separation and durable GitHub governance."
        created = api_request("POST", issues_url, token, {
            "title": f"[HKA AUTOPILOT] {request_obj['role']} · {request_obj['action']} · {request_obj.get('target_window') or 'control-plane'}",
            "body": body
        })
        return {"dispatched": True, "mode": "github_issue_created", "issue_number": created.get("number"), "webhook_error": webhook_error}
    except Exception as exc:
        return {"dispatched": False, "mode": "none", "reason": f"{webhook_error}; issue fallback failed: {exc}"}


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
