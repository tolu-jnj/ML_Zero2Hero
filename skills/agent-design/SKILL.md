---
name: agent-design
description: "Use when converting a multi-step workflow into a bounded agent with explicit tools, state, approvals, and failure handling."
---

# Agent Design

## Course Grounding

Week 6 describes agentic workflows as combining GenAI with tools and other capabilities, with humans retained for some steps. [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
- The ILA case combines model output, deterministic/statistical components, and human approval. [COURSE: 06_Week_6_Transcript.txt#lines 45-160]

## Workflow

1. Map the current process and identify repetitive steps, decision points, and escalation paths.
2. Prefer a deterministic workflow unless model interpretation adds measurable value. [COURSE: 06_Week_6_Transcript.txt#lines 115-160]
3. Define narrow tool schemas, permissions, timeouts, retries, and idempotency. [EXTERNAL: official agent-framework documentation]
4. Add approval gates before consequential actions.
5. Log inputs, tool calls, outputs, approvals, and failures under the applicable data policy. [EXTERNAL: organizational security and audit policy]

```python
workflow = ["classify_request", "retrieve_evidence", "validate_action", "human_approve"]
assert "human_approve" in workflow
```

## Checklist

- [ ] Each step has owner, inputs, outputs, and failure path.
- [ ] Tools have least-privilege access.
- [ ] Approval is required for high-impact actions.
- [ ] Idempotency and audit events are defined.

## Common Pitfalls

- Giving an agent broad tools or credentials.
- Treating free-form model output as an authorized action.

## Go Deeper

- [GAP] The course does not teach a reusable agent architecture or threat model.
- [EXTERNAL: official agent-framework security docs and authoritative agent-safety references]