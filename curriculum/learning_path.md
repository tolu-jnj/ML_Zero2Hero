# Learning Path: Foundations to Production Readiness

This path uses the course as a starting point, not a complete production curriculum. Follow the evidence tags in the knowledge base: `[COURSE]` is course evidence, `[EXTERNAL]` is outside study, and `[GAP]` identifies missing course depth.

## Stage 0: Orientation and Python

- Read [AGENTS.md](../AGENTS.md), the [knowledge index](../knowledge/00_index.md), and the [coverage matrix](coverage_matrix.md).
- Complete the kickoff's foundation overview; it expects beginner-level prior knowledge. [COURSE: 00 Expert Guide C2 Kickoff.pdf#slide 4]
- Build comfort with Python 3.11+, virtual environments, functions, data structures, exceptions, and unit tests. [EXTERNAL: official Python tutorial and packaging documentation]
- Exercise: run Project 01 and extend its synthetic data checks.
- Milestone: explain data vs. model behavior and run a test from a clean environment.

## Stage 1: Frame Problems and Understand Data

- Study the course's structured/unstructured/semi-structured data, quality dimensions, and pipeline stages. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 6-8]
- Complete `problem-framing`, `data-profiling-eda`, `data-quality-validation`, and `data-pipeline`.
- Exercise: complete the framing canvas and data card for a synthetic order use case.
- Go deeper: [GAP] data contracts, lineage, privacy implementation, label quality, and leakage prevention. [EXTERNAL: official pandas/database documentation and established data-quality engineering references]
- Milestone: identify data owner, grain, target, business checks, and prediction-time availability.

## Stage 2: Features and Evaluation Splits

- Study encoding, scaling, class imbalance, noise/outliers, and regularization. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slides 5-7]
- Complete `feature-encoding-scaling`, `class-imbalance`, and `train-test-split-and-cv`.
- Exercise: run Project 02; change class ratios and compare class-wise metrics while leaving test data untouched.
- Go deeper: [GAP] fold-safe transformations, group/time splits, calibration, and threshold governance. [EXTERNAL: official scikit-learn preprocessing/model-selection docs and imbalanced-learn documentation]
- Milestone: justify a split and metric and demonstrate that resampling is training-only.

## Stage 3: Baselines, Models, and Experiments

- Review supervised/unsupervised examples, Isolation Forest, overfitting, XGBoost lead-time, and the graph-transformer case. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slide 3] [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-7] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
- Complete `baseline-modeling`, `regularization-and-overfitting`, `gradient-boosting-xgboost`, `anomaly-detection`, `regression-forecasting`, `hyperparameter-tuning`, and `experiment-tracking`.
- Exercise: run Projects 03 and 04, then vary a feature or baseline and record the result.
- Go deeper: [GAP] uncertainty, robust temporal validation, graph-model reproduction, reproducible registries, and cost profiling. [EXTERNAL: official scikit-learn, XGBoost, MLflow docs and authoritative ML textbooks]
- Milestone: compare a simple baseline with a candidate using documented validation evidence.

## Stage 4: Evaluate and Explain

- Study metric tradeoffs and the course's defect-recall example; note that the Week 4 chart metric is unlabeled. [COURSE: 05_Week_5_Transcript.txt#lines 150-180] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8] [?]
- Complete `metric-selection`, `model-explainability`, and `responsible-ai-governance`.
- Exercise: complete the evaluation report for a synthetic model; include class/time slices and failure examples.
- Go deeper: [GAP] calibration, confidence intervals, fairness/robustness protocols, and risk review. [EXTERNAL: official metric docs and authoritative model-evaluation/responsible-AI references]
- Milestone: make a pass/iterate/stop recommendation against pre-agreed thresholds.

## Stage 5: Computer Vision

- Study CNN foundations and the classification/segmentation/detection distinction and instrument-tray case. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slides 4-6]
- Complete `computer-vision-segmentation` and `metric-selection`; run Project 05.
- Exercise: modify synthetic masks and explain metric movement; do not treat this as model training or regulated validation.
- Go deeper: [GAP] annotation quality, independent-subject splits, model architecture, regulated validation, and deployment. [EXTERNAL: official PyTorch/Torchvision docs and applicable quality/regulatory references]
- Milestone: select task-appropriate image metrics and identify false-negative risk.

## Stage 6: GenAI, RAG, and Agents

- Study the course's LLM/RAG/agent topics, hallucination discussion, deterministic-tool example, and ILA case. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slides 6-8]
- Complete `llm-guardrails`, `rag`, `agent-design`, `agent-evals`, and `responsible-ai-governance`; run Project 06.
- Exercise: add golden cases for unsupported evidence, unauthorized context, tool failure, and approval-required actions.
- Go deeper: [GAP] RAG evaluation, prompt-injection defense, least-privilege tool execution, audit, and agent release controls. [EXTERNAL: official model-provider/agent-framework docs and authoritative safety/evaluation references]
- Milestone: show evidence grounding, abstention, bounded tools, human approval, and task-level evaluation.

## Stage 7: Package, Release, and Monitor

- Complete `model-packaging-serving`, `ci-cd-for-ml`, `experiment-tracking`, and `drift-monitoring`.
- Exercise: create a local release checklist, artifact version, rollback plan, and monitoring plan for one synthetic project.
- Go deeper: [GAP] deployment, registries, CI/CD, SLOs, alert calibration, incident response, and governed retraining are not taught. [EXTERNAL: official MLflow, Docker, GitHub Actions, serving-platform docs, and established MLOps references]
- Milestone: demonstrate a clean build/test/release path with owner, monitoring, and rollback.

## Capstone

Choose a synthetic business problem. Deliver a framing canvas, data card, tested pipeline, baseline and candidate, experiment log, evaluation report, model card, deployment checklist, monitoring plan, and agent-eval tasks if applicable. All claims must retain their course/external/gap provenance tags.

Production readiness depends on the organization's data, security, quality, privacy, and regulatory controls; completing this path alone does not establish approval. [GAP] [EXTERNAL: applicable organizational policies]