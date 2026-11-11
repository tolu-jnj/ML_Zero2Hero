---
name: drift-monitoring
description: "Use when monitoring production input shifts, model outcomes, service health, alert thresholds, and retraining decisions."
---

# Drift Monitoring

## Course Grounding

The course discusses changed data patterns, retraining/fine-tuning after observing changes, and monitoring latency/cost in an AI tool. [COURSE: 01_Week_1_Transcript.txt#lines 73-84] [COURSE: 04_Week_4_Transcript.txt#lines 299-304] [COURSE: 06_Week_6_Transcript.txt#lines 240-255]

## Workflow

1. Record training baselines for features, predictions, outcomes, and service metrics.
2. Monitor data quality and distribution separately from outcome performance. [EXTERNAL: established production-ML monitoring references]
3. Define alert windows, thresholds, owners, and investigation steps before release.
4. Use delayed labels to measure actual performance; drift alone is not proof of failure. [EXTERNAL: authoritative ML monitoring references]
5. Retrain only after data, evaluation, approval, and release gates pass.

```python
shift = abs(reference_rate - current_rate)
if shift > configured_limit:
    emit_alert(metric="feature_rate_shift", value=shift)
```

The statistic and threshold must be selected for the feature and deployment context. [EXTERNAL: authoritative drift-monitoring references]

## Checklist

- [ ] Baselines and expected ranges are versioned.
- [ ] Alerts have an owner and response runbook.
- [ ] Data quality, performance, latency, and cost are tracked.
- [ ] Retraining is not triggered on drift alone.

## Common Pitfalls

- Confusing covariate drift with degraded model performance.
- Retraining automatically without evaluating the candidate.

## Go Deeper

- [GAP] Drift measures, SLOs, alert calibration, and retraining governance are not covered.
- [EXTERNAL: official MLflow and monitoring-library documentation plus established MLOps references]