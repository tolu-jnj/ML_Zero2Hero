"""Validate golden task suite structure; does not execute coding agents."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_FILE = Path(__file__).with_name("golden_tasks.json")


def validate() -> list[str]:
    data = json.loads(TASK_FILE.read_text(encoding="utf-8"))
    expected_agents = {
        path.name.removesuffix(".agent.md")
        for path in (ROOT / "agents").glob("*.agent.md")
    }
    errors = []
    observed_agents = set()
    task_ids = set()

    if data.get("schema_version") != 1:
        errors.append("schema_version must equal 1")

    for agent in data.get("agents", []):
        name = agent.get("name")
        observed_agents.add(name)
        tasks = agent.get("tasks", [])
        if not isinstance(name, str) or not name:
            errors.append("every agent entry needs a name")
            continue
        if not 3 <= len(tasks) <= 5:
            errors.append(f"{name}: expected 3-5 tasks, got {len(tasks)}")

        has_gap_case = False
        for task in tasks:
            task_id = task.get("id")
            if not task_id or task_id in task_ids:
                errors.append(f"{name}: missing or duplicate task id {task_id!r}")
            task_ids.add(task_id)
            for field in ("prompt", "pass_criteria", "fail_criteria", "requires_gap_behavior"):
                if field not in task:
                    errors.append(f"{name}/{task_id}: missing {field}")
            if not task.get("pass_criteria") or not task.get("fail_criteria"):
                errors.append(f"{name}/{task_id}: pass/fail criteria must be non-empty")
            has_gap_case = has_gap_case or task.get("requires_gap_behavior") is True
        if not has_gap_case:
            errors.append(f"{name}: no task requires correct [GAP] behavior")

    if observed_agents != expected_agents:
        errors.append(
            "agent coverage mismatch; missing=%s extra=%s"
            % (sorted(expected_agents - observed_agents), sorted(observed_agents - expected_agents))
        )
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        raise SystemExit("\n".join(problems))
    data = json.loads(TASK_FILE.read_text(encoding="utf-8"))
    task_count = sum(len(agent["tasks"]) for agent in data["agents"])
    print(f"Validated {task_count} golden tasks across {len(data['agents'])} agents.")