---
description: "Frame a business request as an ML/non-ML decision with baseline, metrics, feasibility, and open questions."
agent: ml-problem-framer
argument-hint: "Describe the business decision, users, known data, and constraints."
---

Read [AGENTS.md](../../AGENTS.md) and the [problem-framing skill](../../skills/problem-framing/SKILL.md).

Frame this request:

${input:request:Business request and context}

Return the problem framing canvas, current baseline, candidate metric/error costs, feasibility risks, non-ML alternatives, open questions, and a proceed/investigate/stop recommendation. Cite course claims with `[COURSE: ...]`, external recommendations with `[EXTERNAL: ...]`, and missing evidence with `[GAP]`.