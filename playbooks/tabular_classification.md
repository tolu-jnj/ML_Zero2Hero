# Tabular Classification Playbook

## Use When

The outcome is a discrete class and a structured-feature baseline is appropriate.

## Course Connection

The course introduces supervised classification, encoding/scaling, imbalance, and regularization. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slides 3, 5-7]

## Workflow

1. Define the decision, classes, baseline, error costs, and acceptance metric with `problem-framing`.
2. Profile target balance, missingness, leakage, subgroup coverage, and time/group structure.
3. Choose stratified/group/time splits as appropriate and keep transforms inside the training pipeline. [EXTERNAL: official scikit-learn model-selection documentation]
4. Build a dummy/business baseline with `baseline-modeling`.
5. Encode/scale with `feature-encoding-scaling`; apply `class-imbalance` only when justified and fold-safe.
6. Train a simple candidate; tune/regularize only on training/validation data.
7. Evaluate confusion matrix, class metrics, slices, threshold, and robustness with `metric-selection` and `model-evaluator`.
8. Package, release, and monitor only after the stage gates pass.

## Exit Criteria

- [ ] Leakage-safe split and baseline are recorded.
- [ ] Metric and threshold reflect decision costs.
- [ ] Test set remains untouched until final evaluation.
- [ ] Error slices and limitations are reported.

## Handoff

Deliver data/feature pipeline, experiment record, and evaluation report to `mlops-deployer` after evaluation approval.

## Go Deeper

- [GAP] Production classification, calibration, fairness, and release governance are not covered by the course.
- [EXTERNAL: official scikit-learn docs and authoritative classification evaluation references]