---
description: "Create a simple, reproducible baseline and candidate training plan with a leakage-safe split and tracked results."
agent: model-trainer
argument-hint: "Provide target, feature set, split constraints, metric, and project path."
---

Read [AGENTS.md](../../AGENTS.md), the [baseline-modeling skill](../../skills/baseline-modeling/SKILL.md), and the relevant task playbook.

Training task:

${input:task:Target, features, metric, split, and runtime constraints}

Inspect the nearby code and tests first. Implement the smallest runnable baseline, add focused tests, pin dependencies in the project requirements, and record the evaluation protocol. Never tune against the final test set or use real data. Return files changed and commands run.