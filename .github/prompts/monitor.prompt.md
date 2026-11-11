---
description: "Design monitoring signals, thresholds, owners, incident responses, and retraining criteria for a released ML/AI system."
agent: ml-monitor
argument-hint: "Provide system purpose, baseline, label delay, service needs, and owners."
---

Read [AGENTS.md](../../AGENTS.md), the [drift-monitoring skill](../../skills/drift-monitoring/SKILL.md), and the [monitoring plan template](../../templates/monitoring_plan.md).

Design monitoring for:

${input:system:System, baseline, outcomes, latency/cost needs, and owners}

Return signals, baseline/threshold method, window, severity, owner, response, rollback, and retraining gate. Distinguish data drift from measured performance decay. Mark missing evidence `[GAP]`.