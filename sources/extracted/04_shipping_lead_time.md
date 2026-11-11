# 04 - Shipping Lead-Time Prediction

## Summary

- The Available-to-Promise case responds to customer complaints about inaccurate or unavailable delivery dates; its stated goal is to provide more reliable shipping/delivery dates and improve customer experience. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 4]
- The presentation compares a baseline and re-engineered XGBoost model with a graph-transformer model for order shipping lead time. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8]
- The described data includes historical orders, inventory, scheduling, and backlog information; the models are separated for normal and abnormal backorders. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]

## Key Concepts

- The slide pipeline includes preprocessing, feature engineering, feature selection, model training, and separate test evaluation/comparison. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]
- Examples of engineered features include time features, operational metrics, lag features, and rolling-window statistics; named preprocessing includes missing-value handling, date standardization, deduplication, outlier handling, encoding, and optional scaling. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]
- The graph-transformer illustration represents orders and materials as connected nodes and describes information passing across three graph layers. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 7]
- The transcript says model retraining/fine-tuning is triggered by observed pattern changes, not a fixed calendar cadence. [COURSE: 04_Week_4_Transcript.txt#lines 299-304]

## Worked Examples and Case Studies

- The regression target is lead time between order creation and shipment; the transcript discusses that classification into time bands can be useful for some settings, while the case's primary model predicts a continuous lead time. [COURSE: 02_Week_2_Transcript.txt#lines 7-20] [COURSE: 04_Week_4_Transcript.txt#lines 124-157]
- The chart reports 0.41/0.68/0.72 for normal backorders and 0.30/0.49/0.57 for abnormal backorders across XGBoost baseline, re-engineered XGBoost, and Graph Transformer. The metric is not labeled, so the numbers must not be interpreted without clarification. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 8]
- The transcript discusses business-aligned acceptance targets and differentiates the harder abnormal-backorder case; these are case-specific targets, not general thresholds. [COURSE: 04_Week_4_Transcript.txt#lines 190-228]

## Tools and Algorithms Named

- XGBoost, graph transformer, RMSE/MAE, Bayesian hyperparameter search, mutual information, permutation importance, correlation analysis, lag/rolling-window statistics, and AWS ML are named in the case materials or week recap. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slides 6-8] [COURSE: 04_Week_4_Transcript.txt#lines 22-38]

## Q&A

- The expert recommends starting with a less complex model and adding complexity only when the simpler approach does not meet the use case's needs. [COURSE: 04_Week_4_Transcript.txt#lines 158-188]
- Questions cover interpreting graph layers, feature vs. record counts, data sufficiency, retraining cadence, and alignment of model goals with business needs. [COURSE: 04_Week_4_Transcript.txt#lines 230-309]
- A question about why the case includes both normal and abnormal backorders is answered in terms of materially different information availability and behavior. [COURSE: 04_Week_4_Transcript.txt#lines 124-157]

## Unclear Points

- The deck's regression objective says "predict shipping date" while the transcript describes predicting lead time; the transcript clarifies the target as the time difference between order creation and shipping. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6] [COURSE: 04_Week_4_Transcript.txt#lines 124-157]
- The slide shows a target constraint "within 3 days" and also lists MAE/RMSE; the exact relationship between that constraint and the reported chart metric is not defined. [?] [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]

## Go Deeper

- [GAP] Time-based splits, leakage checks for rolling/lag features, uncertainty intervals, subgroup error analysis, reproducible tuning, model registry, deployment, and alert/retraining criteria are not specified.
- [EXTERNAL: official XGBoost documentation, official scikit-learn model-selection documentation, and authoritative graph-learning references] Use time-aware validation and compare against simple operational baselines before adopting a more complex graph model.