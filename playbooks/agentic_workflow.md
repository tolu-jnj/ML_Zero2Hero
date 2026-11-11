# Agentic Workflow Playbook

## Use When

A bounded, multi-step workflow may benefit from an LLM coordinating deterministic tools and approved human decisions.

## Course Connection

The Week 6 ILA case combines automated triage/recommendations, deterministic/statistical tools, and human approval. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slides 6-8] [COURSE: 06_Week_6_Transcript.txt#lines 45-160]

## Workflow

1. Map current process, exception paths, user roles, and measurable baseline.
2. Automate deterministic steps with code before adding model decisions. [COURSE: 06_Week_6_Transcript.txt#lines 115-160]
3. Define narrow tools, schemas, permissions, idempotency, retries, and state. [EXTERNAL: official agent-framework safety documentation]
4. Gate consequential actions with human review.
5. Build golden tasks, including unsupported requests, tool failures, prompt injection, and correct `[GAP]` behavior using `agent-evals`.
6. Observe task success, unsafe actions, latency, and cost in shadow/staged use before expansion. [EXTERNAL: official provider evaluation documentation]
7. Add audit, rollback, incident owner, and periodic review.

## Exit Criteria

- [ ] Tools are least privilege and actions are bounded.
- [ ] Human approval and refusal paths are tested.
- [ ] Evaluations cover normal, edge, and adversarial cases.
- [ ] Audit, monitoring, rollback, and ownership are ready.

## Handoff

Deliver tool contracts, permissions, eval suite, release gates, and monitoring plan to `mlops-deployer` and `ml-monitor`.

## Go Deeper

- [GAP] The course does not specify a reusable agent architecture or security model.
- [EXTERNAL: official agent-framework docs and authoritative agent safety/evaluation references]