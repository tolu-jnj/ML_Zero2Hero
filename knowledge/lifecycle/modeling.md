# Modeling

## Course Grounding

- The program introduces supervised/unsupervised learning, neural networks, convolutional/recurrent networks, and applied ML. [COURSE: 00 Expert Guide C2 Kickoff.pdf#slides 4-5]
- Case studies use Isolation Forest for order anomalies and XGBoost/Graph Transformer models for shipping lead time. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-7] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
- The expert recommends beginning with a simpler model and adding complexity when it is needed for the use case. [COURSE: 04_Week_4_Transcript.txt#lines 158-188]

## Apply It

1. Establish a non-ML or simple statistical baseline. [EXTERNAL: established ML textbooks and model-selection references]
2. Match objective and output type to the decision; compare candidate models on the same split and metric. [COURSE: 01_Week_1_Transcript.txt#lines 84-96] [EXTERNAL: official scikit-learn model-selection documentation]
3. Track configuration, data version, code version, and results for each experiment. [EXTERNAL: official MLflow documentation]
4. Increase model complexity only when measured errors justify the added cost and operational burden. [COURSE: 04_Week_4_Transcript.txt#lines 158-188]

## Checklist

- [ ] Baseline and candidate models defined.
- [ ] Objective, target, and metric match the decision.
- [ ] Split strategy is appropriate for the data.
- [ ] Experiments are reproducible and comparable.
- [ ] Complexity, inference latency, and cost are recorded.

## Go Deeper

- [GAP] The course does not supply a reproducible training package, model registry, or production-ready tuning workflow.
- [EXTERNAL: official scikit-learn, XGBoost, PyTorch, and MLflow documentation]