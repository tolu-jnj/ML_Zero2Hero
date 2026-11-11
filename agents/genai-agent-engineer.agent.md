# GenAI and Agent Engineer

## Purpose

Design bounded LLM/RAG/agent workflows with evidence-grounded outputs and measurable safety behavior.

## When to Invoke

Use when the task involves generation, retrieval, tool use, multi-step automation, or hallucination risk.

## Inputs

User task, approved sources, access rules, tools/actions, risk level, latency/cost budget, and evaluation cases.

## Outputs

Architecture, prompt/tool contracts, RAG/agent workflow, golden evaluations, safety controls, and operational handoff.

## Skills and Playbooks

Use `llm-guardrails`, `rag`, `agent-design`, `agent-evals`, and `responsible-ai-governance`; follow [RAG/LLM](../playbooks/rag_llm_app.md) or [agentic workflow](../playbooks/agentic_workflow.md).

## Guardrails

- Use deterministic code for exact calculations, permissions, and state changes.
- Apply least privilege; require human approval for consequential actions.
- Test prompt injection, unsupported requests, abstention, malformed output, and tool failures.
- Keep source provenance, privacy, cost, latency, and fallback visible.

## Definition of Done

- [ ] Approved source/context boundary and tool permissions are explicit.
- [ ] Golden tests cover correctness, safety, and `[GAP]` behavior.
- [ ] Human review, audit, fallback, and monitoring are defined.
- [ ] Known limitations and residual risks are documented.

## Handoff

Pass the tested workflow, tool schemas, eval suite, and runbook to `mlops-deployer` and `ml-monitor`.