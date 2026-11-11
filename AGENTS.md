# ML Zero2Hero Agent Operating Guide

Read this file first. It is the canonical, tool-neutral operating contract for every human and coding agent working in this repository. Tool-specific files must point here rather than fork its rules.

## Confidentiality and Provenance

- Treat this repository and its course materials as internal and confidential. Do not copy its content to public services or push it to public remotes.
- Preserve the original transcript and PDF files in their existing folders unless the owner explicitly approves a move. Do not edit, rename, delete, or duplicate the originals.
- Tag every substantive ML knowledge claim: `[COURSE: <file>#<section, slide, or line>]` for course evidence, `[EXTERNAL: <recommended source type or canonical reference>]` for outside knowledge, and `[GAP]` when the course does not cover it. Mark uncertain transcript wording with `[?]`.
- Never blend external recommendations into course material without an explicit `[EXTERNAL]` tag. Use official documentation or well-established references; do not invent URLs.
- Keep secrets, `.env`, datasets, model binaries, and generated artifacts out of Git. `.gitignore` encodes common local exclusions; verify `git status` before staging.

## Task Routing

| Need | Playbook | Primary agent |
|---|---|---|
| Clarify business objective or feasibility | [Tabular classification](playbooks/tabular_classification.md) or [lead-time regression](playbooks/lead_time_regression.md) | `ml-problem-framer` |
| Inspect or validate a dataset | [Data-quality pipeline](playbooks/data_quality_pipeline.md) | `data-engineer` |
| Prepare features or imbalance handling | [Tabular classification](playbooks/tabular_classification.md) | `feature-engineer` |
| Train/evaluate a model | Relevant task playbook | `model-trainer`, then `model-evaluator` |
| Build an anomaly detector | [Anomaly detection](playbooks/anomaly_detection.md) | `model-trainer` |
| Build vision segmentation | [CV segmentation](playbooks/cv_segmentation.md) | `model-trainer` |
| Build an LLM/RAG system | [RAG/LLM app](playbooks/rag_llm_app.md) | `genai-agent-engineer` |
| Automate a multi-step workflow | [Agentic workflow](playbooks/agentic_workflow.md) | `genai-agent-engineer` |
| Package, release, or monitor a model | Relevant task playbook | `mlops-deployer`, then `ml-monitor` |
| Learn or review a concept | Knowledge index and linked skill | `ml-tutor` |
| Coordinate an end-to-end task | Select a playbook and delegate by stage | `ml-orchestrator` |

## Standard Workflow

1. Frame the decision, user, baseline, success measure, constraints, and feasibility.
2. Profile/validate data; document lineage, permissions, label quality, and leakage risks.
3. Build a simple baseline, then justified candidate models; log reproducible experiments.
4. Evaluate with a deployment-relevant split, task-aligned metrics, error slices, and explicit limitations.
5. Package and release only after tests, approvals, and rollback behavior are clear.
6. Monitor data, outcomes, service health, cost, and latency; route drift/retraining decisions to an owner.
7. For GenAI/agents, evaluate groundedness, refusal, tool safety, prompt injection, latency, and cost; retain human approval for consequential actions.

The course introduces parts of this lifecycle but does not teach a complete production workflow. [COURSE: 00 Expert Guide C2 Kickoff.pdf#slide 4] [GAP]

## Skills

Use the canonical skill in `/skills/<name>/SKILL.md`; `.github/skills/README.md` is only a discovery pointer.

`problem-framing`, `data-profiling-eda`, `data-quality-validation`, `data-pipeline`, `class-imbalance`, `feature-encoding-scaling`, `train-test-split-and-cv`, `baseline-modeling`, `regularization-and-overfitting`, `gradient-boosting-xgboost`, `anomaly-detection`, `regression-forecasting`, `computer-vision-segmentation`, `metric-selection`, `hyperparameter-tuning`, `experiment-tracking`, `model-explainability`, `model-packaging-serving`, `ci-cd-for-ml`, `drift-monitoring`, `llm-guardrails`, `rag`, `agent-design`, `agent-evals`, `responsible-ai-governance`.

## Repository Map

- `knowledge/`: cited reference notes; begin at [knowledge index](knowledge/00_index.md).
- `skills/`: reusable, agent-executable procedures.
- `playbooks/`: end-to-end stage sequences that chain skills.
- `templates/`: project records and review checklists.
- `projects/`: runnable synthetic-data examples; no real or sensitive data.
- `evals/`: agent golden tasks, expected behaviors, and pass/fail criteria.
- `curriculum/`: course coverage, learning path, and prioritized gaps.
- `sources/extracted/`: reviewed session notes and source inventory.
- `MTIE_Expert_Guide_Transcripts/` and `MTIE Expert Guide Transcripts/`: original source files, left in place.

## Agents and Handoffs

- `ml-orchestrator`: frame scope, choose playbook, sequence specialists; hands off to the first specialist.
- `ml-problem-framer`: business objective, metrics, baseline, feasibility; hands off to data engineering.
- `data-engineer`: ingestion, data quality, validation, leakage checks; hands off to feature engineering.
- `feature-engineer`: transformations, imbalance, feature selection; hands off to model training.
- `model-trainer`: baseline/candidate training, tuning, tracking; hands off to evaluation.
- `model-evaluator`: metric/split choice, error analysis, fairness/robustness; hands off to deployment only when criteria pass.
- `mlops-deployer`: packaging, serving, CI/CD, registry; hands off to monitoring.
- `ml-monitor`: drift, service health, alert/retraining criteria; reports incidents and retraining recommendations to owners.
- `genai-agent-engineer`: LLM/RAG/agent design, guardrails, evaluations; hands off operational controls to MLOps and monitoring.
- `ml-tutor`: explain course concepts first, distinguish external depth, quiz learner, and link Go Deeper resources.

Each agent file defines its invocation conditions, inputs, outputs, skills, guardrails, definition of done, and handoff contract.

## Prompts and Playbooks

Canonical agent contracts live in `agents/` and reusable prompts live in `prompts/`; both are plain Markdown and tool-neutral. VS Code discovery wrappers live in `.github/agents/` and `.github/prompts/`. Playbooks are under `playbooks/` and cover data quality, tabular classification, anomaly detection, lead-time regression, CV segmentation, RAG/LLM apps, and agentic workflows.

## Projects and Validation

- Use Python 3.11+ and the pinned project requirements; each project documents one run command and tests.
- Use only generated synthetic data in committed examples. Never add production data, credentials, or model artifacts.
- Run the touched project's tests and the repo-level checks before committing. Report any unavailable checks.
- Commit one coherent phase at a time; do not push to public remotes. Push only after verifying the destination is private/internal and explicitly authorized.

## Learning and Source Policy

- Course-backed notes are linked from [the knowledge index](knowledge/00_index.md) and [coverage matrix](curriculum/coverage_matrix.md).
- A case study is evidence about that case only, not a universal best practice or production architecture.
- When the course is shallow, state the gap and recommend source types in a Go Deeper block; do not invent missing course details.