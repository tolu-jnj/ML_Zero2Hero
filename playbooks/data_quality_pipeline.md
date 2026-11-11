# Data Quality Pipeline Playbook

## Use When

Data arrives from one or more sources and must be profiled, validated, transformed, and prepared for analysis or modeling.

## Course Connection

Week 1 introduces collection, ingestion, processing, storage, and analysis, plus data-quality dimensions. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 7-8]

## Workflow

1. Frame data purpose, decision, owners, permissions, grain, and update cadence with `problem-framing`.
2. Profile schema, missingness, duplicates, coverage, target quality, and distributions with `data-profiling-eda`.
3. Implement repeatable schema/business checks with `data-quality-validation`.
4. Build an idempotent collection/ingestion/processing flow with `data-pipeline`. [EXTERNAL: official data-platform documentation]
5. Record a data card, lineage, failure actions, and privacy review.
6. Publish only validated model-ready data; keep generated samples synthetic.

## Exit Criteria

- [ ] Data owner and intended use are documented.
- [ ] Checks and failure actions run reproducibly.
- [ ] Data access/retention comply with policy.
- [ ] Known gaps and rejected records are traceable.

## Handoff

Hand a validated schema, profiling report, data card, and unresolved data risks to `feature-engineer`.

## Go Deeper

- [GAP] The course does not teach orchestration, lineage tooling, service levels, or recovery.
- [EXTERNAL: official platform docs and established data-engineering references]