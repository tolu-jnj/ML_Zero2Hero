# ML Zero2Hero: Agent-Agnostic ML Engineering

An internal, learning-oriented operating system for machine-learning work, from problem framing through monitoring. It combines source-cited course knowledge, actionable skills, role-based agents, end-to-end playbooks, templates, synthetic reference projects, and agent evaluations.

The J&J MTIE Expert Guide Cohort 2 materials are the foundation, not a production curriculum. Course claims, outside recommendations, uncovered topics, and uncertain auto-transcription use distinct provenance tags. The six-week program establishes foundational knowledge, while production depth remains a curriculum gap. [COURSE: 00 Expert Guide C2 Kickoff.pdf#slide 4] [GAP]

## Start Here

1. Read [AGENTS.md](AGENTS.md), the canonical tool-neutral workflow and confidentiality guide.
2. Scan the [knowledge index](knowledge/00_index.md) and [coverage matrix](curriculum/coverage_matrix.md).
3. Choose a [playbook](playbooks/) for the task; its steps link to the relevant `/skills/<name>/SKILL.md`.
4. Use the role agent under `.github/agents/` where supported, or follow its Markdown contract in any coding agent.
5. Capture decisions with the templates in `templates/`, then run project tests and relevant evals.

## Learning

Follow the sequenced [learning path](curriculum/learning_path.md) from Python and data fundamentals to deployment/monitoring. Use the [prioritized gap backlog](curriculum/gap_backlog.md) to choose external study. Tutor prompts start with course examples and then label external explanation separately.

## Runnable Projects

The examples use generated synthetic data only. From the repository root:

| Command | Example |
|---|---|
| `make run-01` | Data-quality pipeline |
| `make run-02` | Imbalance, encoding, and scaling |
| `make run-03` | Isolation Forest anomaly detection |
| `make run-04` | XGBoost lead-time regression with local MLflow tracking |
| `make run-05` | Synthetic segmentation metrics |
| `make run-06` | Local evidence/approval guardrail demo; no LLM/network call |
| `make test` | Install pinned project requirements and run all project tests |

Project requirements are pinned separately to avoid installing unrelated stacks. Run `python evals/validate_golden_tasks.py` to check the agent evaluation suite's structure; see [evals/README.md](evals/README.md) for what that validator does and does not execute.

## Agents and Tools

There are ten role contracts in `.github/agents/`: orchestrator, problem framer, data engineer, feature engineer, model trainer, model evaluator, MLOps deployer, monitor, GenAI/agent engineer, and tutor. `.github/prompts/` provides focused slash prompts. `CLAUDE.md` and `.github/copilot-instructions.md` are thin pointers; other tools should read `AGENTS.md` directly.

## Confidentiality

Treat the course and distilled internal content as confidential. Original transcripts and PDFs remain in their supplied folders and are unmodified. Do not copy these materials to public services or push them to public remotes. The current configured GitHub `origin` is public, so this repository must not be pushed there. To publish approved content, first move to an explicitly private/internal destination and review the staged files; no raw sources may be included without approval.

`.gitignore` excludes data, model artifacts, MLflow output, secrets, and `.env` files. Verify `git status` before staging.

## What's Built and What's Still Missing

- Built: cited session notes, knowledge index, lifecycle coverage, 25 skills, ten agent contracts, seven playbooks, nine prompts, eight templates, six tested synthetic examples, and 30 golden tasks.
- Still a gap: production-grade CI/CD, serving, monitoring/incident response, organizational governance, and actually executing the golden tasks against configured agent runtimes. See the [gap backlog](curriculum/gap_backlog.md). [GAP]
- Next: review P0 controls with data/security/quality owners, then run each agent against its golden tasks in the target agent runtimes and record results.