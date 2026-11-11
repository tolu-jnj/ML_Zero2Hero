---
description: "Prepare an evaluated model for controlled packaging, serving, tests, security review, rollback, and monitoring handoff."
agent: mlops-deployer
argument-hint: "Provide the approved model artifact, interface, environment, and release constraints."
---

Read [AGENTS.md](../../AGENTS.md), the [model-packaging skill](../../skills/model-packaging-serving/SKILL.md), and the [deployment checklist](../../templates/deployment_checklist.md).

Deployment context:

${input:release:Model, interface, runtime, security, and approval context}

Return the packaging/release plan, validations, pinned dependency requirements, rollback/fallback, approvals, and monitoring handoff. Do not deploy or push to a public remote. Flag missing organizational policies as `[GAP]`.