# Frame Problem

Use with the `ml-problem-framer` role. Read [AGENTS.md](../AGENTS.md) and the [problem-framing skill](../skills/problem-framing/SKILL.md).

Frame this request:

Business request and context: <describe the decision, users, data, and constraints>

Return the problem framing canvas, current baseline, candidate metric/error costs, feasibility risks, non-ML alternatives, open questions, and a proceed/investigate/stop recommendation. Cite course claims with `[COURSE: ...]`, external recommendations with `[EXTERNAL: ...]`, and missing evidence with `[GAP]`.