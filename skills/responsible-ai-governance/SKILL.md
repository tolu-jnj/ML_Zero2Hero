---
name: responsible-ai-governance
description: "Use when assessing data privacy, bias, risk, human oversight, accountability, and approvals for AI/ML work."
---

# Responsible AI Governance

## Course Grounding

Week 1 names privacy/security and data bias; later sessions discuss underrepresentation, hallucinations, guardrails, human review, and a GxP case. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7] [COURSE: 02_Week_2_Transcript.txt#lines 122-149] [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6]

## Workflow

1. Record intended use, affected users, data types, and potential harms.
2. Identify privacy, security, fairness, robustness, and regulatory review owners. [EXTERNAL: applicable organizational policies and authoritative AI risk-management references]
3. Document evidence, limitations, human oversight, escalation, and change control.
4. Ensure required approvals precede data use, deployment, or material changes.
5. Reassess after changes to data, model, prompts, tools, or workflow.

```python
review = {
    "intended_use": "",
    "data_sensitivity": "",
    "affected_groups": [],
    "known_harms": [],
    "approval_owner": "",
}
```

## Checklist

- [ ] Intended use and limits are clear.
- [ ] Data access and retention follow policy.
- [ ] Impacted groups and error consequences are assessed.
- [ ] Human review, escalation, and accountable owners are set.
- [ ] Approval and audit records are retained.

## Common Pitfalls

- Treating course examples as legal or regulatory advice. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 6] [GAP]
- Assuming a model metric alone establishes fairness or safety. [EXTERNAL: authoritative AI risk-management references]

## Go Deeper

- [GAP] The course does not define organizational governance or approval procedures.
- [EXTERNAL: applicable organizational policies, NIST AI Risk Management Framework, and relevant regulatory guidance]