# Anomaly Detection Playbook

## Use When

Rare or unlabeled events need triage and an operational owner can review alerts.

## Course Connection

The order-monitoring case uses Isolation Forest, score thresholding, and business rules. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slides 5-7]

## Workflow

1. Define the operational anomaly and resulting action with `problem-framing`.
2. Profile temporal patterns, groups, data quality, and known exceptions.
3. Establish a rule-based/statistical baseline.
4. Train Isolation Forest using `anomaly-detection`; verify estimator score semantics. [EXTERNAL: official scikit-learn documentation]
5. Set thresholds using reviewed cases and alert capacity; do not copy the course Gamma-fit example without independent validation. [COURSE: 03 Expert Guide C2 W3 Live Event.pdf#slide 7] [GAP]
6. Evaluate false alarms, missed events, time stability, and subgroup behavior.
7. Route alerts with evidence, review outcomes, and monitor score/data changes.

## Exit Criteria

- [ ] Alert definition, owner, and response are explicit.
- [ ] Threshold is reviewed against operational capacity.
- [ ] Known exceptions and temporal holdouts are tested.
- [ ] Monitoring and retraining criteria have owners.

## Handoff

Give approved detector, threshold rationale, alert runbook, and evaluation evidence to `mlops-deployer` and `ml-monitor`.

## Go Deeper

- [GAP] Label-scarce evaluation, alert calibration, and monitoring are not taught.
- [EXTERNAL: official scikit-learn docs and authoritative anomaly-detection references]