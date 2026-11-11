---
description: "Evaluate a model against its baseline using task-aligned metrics, safe splits, error analysis, fairness, and robustness checks."
agent: model-evaluator
argument-hint: "Provide the framing brief, split, baseline, candidate results, and acceptance criteria."
---

Read [AGENTS.md](../../AGENTS.md), the [metric-selection skill](../../skills/metric-selection/SKILL.md), and the [evaluation report template](../../templates/eval_report.md).

Evaluate:

${input:evidence:Model, data/split, baseline, metrics, and criteria}

Return pass/iterate/stop with evidence, metric rationale, error slices, leakage/test-set concerns, subgroup/robustness gaps, and residual risks. Do not invent missing metric labels. Mark unsupported claims `[GAP]`.