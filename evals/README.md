# Agent Evaluations

[`golden_tasks.json`](golden_tasks.json) defines three golden tasks for each of the ten specialist agents. Each case has observable pass/fail criteria; every agent has at least one task where the correct behavior is to flag `[GAP]` rather than invent course coverage.

Run the structure and agent-coverage check with:

```bash
python evals/validate_golden_tasks.py
```

This command validates the suite schema; it does not invoke or score an LLM. Execute each task with the matching agent in the target agent runtime, record its output, and assess it against the listed criteria. [GAP]

Course-derived expectations cite the transcript or slide that supports them. External recommendations are not presented as course content.