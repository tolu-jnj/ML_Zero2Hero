---
name: problem-framing
description: "Use when translating a business need into an ML or non-ML problem, defining outcomes, metrics, feasibility, and a baseline."
---

# Problem Framing

## Course Grounding

The course connects order anomalies and lead-time prediction to supply/customer outcomes and recommends business-domain collaboration. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 5] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 4] [COURSE: 01_Week_1_Transcript.txt#lines 40-60]

## Workflow

1. Interview the decision owner and affected users; write the decision and timing in plain language. [EXTERNAL: established ML project-framing references]
2. Record current process, non-ML baseline, and measurable outcome.
3. Specify prediction target, unit, horizon, success metric, error costs, and minimum useful result.
4. Check label availability, representative data, access constraints, latency, cost, and actionability.
5. Recommend ML only if it can improve the decision over a simpler alternative.

## Deliverable

Create a one-page framing brief with objective, users, target, baseline, metrics, constraints, risks, and a go/no-go recommendation.

```python
brief = {
    "decision": "",
    "user": "",
    "target": "",
    "baseline_metric": None,
    "success_metric": "",
    "error_costs": {},
    "data_and_constraints": [],
}
```

The brief format is a working template, not a course-provided artifact. [EXTERNAL: established ML project-framing references]

## Checklist

- [ ] Business owner and decision are explicit.
- [ ] Baseline and acceptance criteria are measurable.
- [ ] Feasibility and non-ML alternatives are assessed.
- [ ] Assumptions and unresolved questions are visible.

## Common Pitfalls

- Starting with an algorithm before defining a decision. [EXTERNAL: established ML project-framing references]
- Treating a model metric as business value without validating the link. [COURSE: 04_Week_4_Transcript.txt#lines 190-228]

## Go Deeper

- [GAP] The course does not provide a complete feasibility or value-assessment method.
- [EXTERNAL: authoritative ML project-framing textbooks and organizational product/risk policies]