# Isolation Forest

## Course Grounding

- The order-monitoring case uses an unsupervised Isolation Forest and explains that random partitions can isolate unusual points in shorter paths. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-6]
- The case slide describes fitting a Gamma distribution to the anomaly scores and thresholding via a p-value. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 7]
- The transcript says business rules and known exceptions are applied after model scoring. [COURSE: 03_Week_3_Transcript.txt#lines 30-80]

## Practical Reading

- Treat the score direction and threshold as estimator/configuration-specific; verify the exact library behavior before applying a cutoff. [EXTERNAL: official scikit-learn IsolationForest documentation]
- Validate alert usefulness against reviewed examples and business impact; a score is not a diagnosis. [EXTERNAL: authoritative anomaly-detection evaluation references]
- The Gamma/p-value step is specific to the presented case and is not justified as a general calibration technique by the course. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 7] [GAP]

## Minimal Pattern

```python
from sklearn.ensemble import IsolationForest

detector = IsolationForest(random_state=7, contamination="auto")
detector.fit(train_features)
anomaly_score = -detector.score_samples(eval_features)
```

The snippet uses a library API; check score direction and contamination semantics in the installed version. [EXTERNAL: official scikit-learn IsolationForest documentation]

## Checklist and Pitfalls

- [ ] Fit on representative data and inspect score distributions.
- [ ] Define how alerts are reviewed and acted on.
- [ ] Test known seasonal/business exceptions.
- [ ] Do not assume every statistical outlier is operationally anomalous. [EXTERNAL: authoritative anomaly-detection references]
- [GAP] Time-aware backtesting, label-scarce evaluation, and alert-volume controls are not taught.

## Go Deeper

- [EXTERNAL: official scikit-learn IsolationForest documentation and authoritative anomaly-detection evaluation papers]