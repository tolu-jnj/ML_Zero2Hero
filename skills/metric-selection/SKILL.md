---
name: metric-selection
description: "Use when choosing and explaining classification, regression, anomaly, vision, or LLM evaluation metrics tied to decision costs."
---

# Metric Selection

## Course Grounding

The course warns that accuracy can hide minority-class failures, discusses precision/recall for defects, and names MAE/RMSE for lead time. [COURSE: 02_Week_2_Transcript.txt#lines 100-121] [COURSE: 05_Week_5_Transcript.txt#lines 150-180] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]

## Workflow

1. Identify the decision and relative costs of false positives, false negatives, and magnitude errors.
2. Select a primary metric and supporting diagnostics; state threshold and averaging method. [EXTERNAL: official scikit-learn metrics documentation]
3. Compare to baseline and report performance by important groups/time slices.
4. Align acceptance criteria with domain owners before final test evaluation. [COURSE: 04_Week_4_Transcript.txt#lines 190-228]

```python
from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(actual, predicted))
print(classification_report(actual, predicted, zero_division=0))
```

## Checklist

- [ ] Primary metric is connected to business error cost.
- [ ] Threshold and averaging are documented.
- [ ] Class-wise and subgroup results are included.
- [ ] Test data is not used to select the metric threshold.

## Common Pitfalls

- Treating one score as sufficient for a high-impact workflow.
- Calling the Week 4 chart metric "precision" when the slide does not label it. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8]

## Go Deeper

- [GAP] Calibration, uncertainty, robustness, and fairness metrics are not covered in depth.
- [EXTERNAL: official scikit-learn metrics documentation and authoritative evaluation references]