---
name: agent-evals
description: "Use when creating golden tasks and pass/fail criteria for agent behavior, tool use, provenance, refusal, and gap identification."
---

# Agent Evaluations

## Course Grounding

The course emphasizes hallucination risk, human review, monitoring, and evaluation needs for GenAI/agentic systems but provides no eval harness. [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 06_Week_6_Transcript.txt#lines 240-255] [GAP]

## Workflow

1. Write representative tasks, including underspecified, adversarial, and out-of-scope cases. [EXTERNAL: official model-provider evaluation documentation]
2. Define observable pass/fail criteria for correctness, citations, policy behavior, and tool calls.
3. Include cases where the correct answer is `[GAP]`, not an invented course claim.
4. Run each candidate against a fixed suite and record model, prompt, tools, and result.
5. Review failures with a human and add regression cases before changing the system.

```python
def passes(result, required_source, expected_gap=False):
    return (required_source in result.get("citations", [])) and (result.get("gap") is expected_gap)
```

## Checklist

- [ ] Each agent has 3-5 golden tasks and explicit criteria.
- [ ] Expected outputs separate course evidence from external advice.
- [ ] Tool safety and unauthorized action are tested.
- [ ] Regressions are reviewed and versioned.

## Common Pitfalls

- Scoring fluency instead of task success.
- Omitting tests where evidence is absent and the agent must say `[GAP]`.

## Go Deeper

- [GAP] Course-provided golden tests and automated eval methods do not exist.
- [EXTERNAL: official model-provider eval docs and authoritative LLM/agent evaluation references]