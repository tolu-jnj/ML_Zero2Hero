---
name: data-pipeline
description: "Use when building a repeatable batch or streaming path for collecting, ingesting, transforming, storing, and analyzing ML data."
---

# Data Pipeline

## Course Grounding

The Week 1 deck presents collection, ingestion, processing, storage, and analysis; it also names ETL/ELT. [COURSE: 01 Expert Guide C2 W1 Live Event.pdf#slide 8]

## Workflow

1. Document source owners, schema, cadence, access, and retention constraints.
2. Implement idempotent extraction and preserve source timestamps and identifiers. [EXTERNAL: official platform documentation]
3. Validate and transform data with versioned code; separate raw, cleaned, and model-ready layers.
4. Make retries, duplicate delivery, partial failure, and late data explicit.
5. Log run metadata and quality counts; alert an owner on failed invariants.

```python
def transform(batch):
    validate_schema(batch)
    cleaned = normalize_fields(batch)
    validate_business_rules(cleaned)
    return cleaned
```

## Checklist

- [ ] Re-run does not duplicate outputs.
- [ ] Schema changes and late data are handled.
- [ ] Validation failures are observable and actionable.
- [ ] Data access, retention, and lineage follow policy.

## Common Pitfalls

- Treating a one-off notebook as a reliable pipeline.
- Ignoring changing patterns or data freshness. [COURSE: 01_Week_1_Transcript.txt#lines 73-84]

## Go Deeper

- [GAP] Orchestration, lineage, streaming guarantees, SLAs, and recovery are not covered.
- [EXTERNAL: official cloud/data-platform documentation and established data-engineering references]