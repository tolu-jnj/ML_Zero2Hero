---
name: anomaly-detection
description: "Use when identifying unusual observations without complete anomaly labels, selecting score thresholds, and routing alerts."
---

# Anomaly Detection

## Course Grounding

The order-monitoring case uses Isolation Forest, short path lengths, a Gamma-score threshold example, and downstream business rules. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-7] [COURSE: 03_Week_3_Transcript.txt#lines 30-80]

## Workflow

1. Define what operational event counts as anomalous and what action follows.
2. Profile time, group, and seasonal patterns; verify input features are available at scoring time.
3. Fit a baseline detector and review score distributions with domain experts. [EXTERNAL: official scikit-learn IsolationForest documentation]
4. Choose threshold from reviewed cases and alert capacity; measure missed events and false alarms.
5. Add business-rule exceptions only with explicit owners and tests.

```python
from sklearn.ensemble import IsolationForest

detector = IsolationForest(random_state=7, contamination="auto").fit(train_features)
scores = -detector.score_samples(eval_features)
alerts = scores >= reviewed_threshold
```

Verify the score direction and threshold semantics for the chosen estimator. [EXTERNAL: official scikit-learn IsolationForest documentation]

## Checklist

- [ ] Anomaly definition and response owner are explicit.
- [ ] Threshold is reviewed against operational capacity.
- [ ] Seasonal and known exceptional cases are checked.
- [ ] Alerts are logged with evidence and outcome labels.

## Common Pitfalls

- Assuming statistical rarity equals business importance. [EXTERNAL: authoritative anomaly-detection evaluation references]
- Copying the course Gamma-fit thresholding method without validating its assumptions. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 7] [GAP]

## Go Deeper

- [EXTERNAL: official scikit-learn documentation and authoritative anomaly-detection evaluation papers]