# Beyond-Course Gap Backlog

Priorities indicate recommended learning order for turning the foundation into reliable project work. These are curriculum gaps, not claims that the course covered them.

## P0: Establish Before Real Data or Decisions

1. **Problem framing and acceptance criteria**: decision owner, baseline, feasibility, error cost, and go/no-go. The course includes business cases but no reusable framing rubric. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 5] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 4] [GAP] **Study:** authoritative ML project-framing and product-discovery references.
2. **Data permissions, privacy, and governance**: access rules, sensitive data, retention, accountability, and approvals. The course names privacy/security and bias but does not define controls. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7] [GAP] **Study:** organizational policies and authoritative AI risk-management/regulatory guidance.
3. **Leakage-safe validation**: time/group split design, fold-local preprocessing, and untouched test sets. [GAP] **Study:** official scikit-learn model-selection documentation and authoritative time-series evaluation references.

## P1: Build Trustworthy Models and Applications

4. **Evaluation depth**: calibration, uncertainty, subgroup error analysis, robustness, fairness, and thresholds. The course gives metric examples but not a full protocol. [COURSE: 05_Week_5_Transcript.txt#lines 150-180] [GAP] **Study:** official metric docs and authoritative evaluation/fairness references.
5. **Data contracts and lineage**: schema evolution, ownership, validation gates, reproducibility, and label quality. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 7-8] [GAP] **Study:** official data-quality tooling and established data-engineering references.
6. **Production packaging and CI/CD**: pinned artifacts, serving contracts, release approvals, rollback, and registries. The course describes cases as production systems but does not teach deployment mechanics. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 5] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 4] [GAP] **Study:** official MLflow, Docker, GitHub Actions, and serving-platform documentation.
7. **Monitoring and incident response**: drift vs. performance, alert thresholds, service objectives, delayed labels, retraining gates, and ownership. [COURSE: 04_Week_4_Transcript.txt#lines 299-304] [COURSE: 06_Week_6_Transcript.txt#lines 240-255] [GAP] **Study:** established MLOps monitoring and reliability references.
8. **GenAI/RAG/agent security and evaluation**: retrieval quality, access-aware retrieval, prompt injection, tool permissions, golden regression tests, and audit. The course names RAG, guardrails, and human review but does not operationalize them. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 3] [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 06_Week_6_Transcript.txt#lines 20-40] [GAP] **Study:** official model-provider/agent-framework security docs and authoritative RAG/agent evaluation references.

## P2: Deepen Specialized Methods

9. **Computer-vision production practice**: annotation QA, independent-subject/site splits, segmentation metrics, runtime, and regulated validation. The course explains concepts and one case, not a reusable validation plan. [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slides 4-6] [GAP] **Study:** official PyTorch/Torchvision documentation and applicable quality/regulatory references.
10. **Anomaly detection evaluation**: score semantics, threshold calibration, alert capacity, temporal backtesting, and label-scarce validation. The Gamma-fit method is a case slide and its assumptions are unstated. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 7] [?] **Study:** official scikit-learn docs and authoritative anomaly-detection research.
11. **Graph learning and advanced forecasting**: graph construction, temporal leakage, architecture reproduction, uncertainty, cost, and latency. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 7] [GAP] **Study:** official PyTorch Geometric/DGL documentation and foundational graph-learning/forecasting papers.
12. **Responsible AI practice**: risk tiers, documentation, human oversight, auditability, change review, and accountable sign-off. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 7] [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 6] [GAP] **Study:** applicable organizational policy and authoritative AI risk-management frameworks.

## Suggested Order

Address P0 controls before any real-data project, then P1 evaluation and operations, then choose P2 specializations based on the problem. A course case study or successful synthetic demo does not close these gaps. [GAP]