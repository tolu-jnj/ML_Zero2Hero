# Evaluation

## Course Grounding

- The course discusses training/validation differences, overfitting, and why accuracy can mislead on imbalanced data. [COURSE: 02 Expert Guide C2 W2 Live Event.pdf#slides 5-7] [COURSE: 02_Week_2_Transcript.txt#lines 100-121]
- The case materials name MAE/RMSE for lead-time prediction and compare model results on normal and abnormal backorders. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
- The vision discussion explains why recall may be more important than accuracy when missed defects have higher costs. [COURSE: 05_Week_5_Transcript.txt#lines 150-180]

## Apply It

1. Choose metrics from the decision and error costs, not familiarity. [COURSE: 05_Week_5_Transcript.txt#lines 150-180]
2. Reserve an untouched test set and use a split strategy that reflects deployment conditions. [EXTERNAL: official scikit-learn model-selection documentation]
3. Inspect subgroup performance, calibration, failure examples, and uncertainty where relevant. [EXTERNAL: authoritative evaluation and responsible-AI references]
4. Compare to the baseline and have domain owners review errors before release. [COURSE: 04_Week_4_Transcript.txt#lines 190-228] [EXTERNAL: established ML evaluation references]

## Checklist

- [ ] Metric and acceptance threshold justified by stakeholders.
- [ ] Split prevents time, group, or entity leakage.
- [ ] Baseline and candidate results compared on identical data.
- [ ] Errors reviewed by slices and representative examples.
- [ ] Limitations and residual risks reported.

## Go Deeper

- [GAP] Calibration, confidence intervals, robustness testing, and fairness evaluation are not developed into a repeatable protocol.
- [EXTERNAL: official metric documentation and authoritative model-evaluation/fairness references]