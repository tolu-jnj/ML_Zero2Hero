# Data

## Course Grounding

- The course distinguishes structured, unstructured, and semi-structured data and names completeness, accuracy, timeliness, consistency, validity, and uniqueness as quality questions. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slides 6-7]
- The Week 1 slide presents collection, ingestion, processing, storage, and analysis as high-level data-pipeline stages. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 8]
- The instructor discusses representativeness, changing data patterns, preprocessing, missing values, and the risk of incomplete data. [COURSE: 01_Week_1_Transcript.txt#lines 67-84, 117-136]
- The Week 4 case lists missing-value handling, date standardization, duplicate/outlier handling, encoding, and optional scaling. [COURSE: 04 Expert Guide C2 W4 Live Event.pdf#slide 6]

## Apply It

1. Identify source systems, owners, update cadence, target labels, and access constraints. [EXTERNAL: official data-platform documentation and organizational data governance policy]
2. Profile row counts, schema, missingness, duplicate keys, category frequencies, ranges, and time coverage. [EXTERNAL: official pandas documentation]
3. Validate business rules with domain owners; treat anomalous values as investigation candidates, not automatic deletion. [EXTERNAL: authoritative data-quality engineering references]
4. Preserve data lineage and split data before fitting learned transformations. [EXTERNAL: official scikit-learn pipeline and model-selection documentation]

## Checklist

- [ ] Schema, keys, units, and target definition recorded.
- [ ] Missingness and duplicates quantified.
- [ ] Time coverage and subgroup representation inspected.
- [ ] Data access and sensitive fields reviewed.
- [ ] Validation checks are repeatable.

## Go Deeper

- [GAP] Data contracts, lineage, schema evolution, leakage-safe preprocessing, access-control implementation, and reproducible validation are not taught.
- [EXTERNAL: official pandas and database documentation; established data-quality and data-governance references]