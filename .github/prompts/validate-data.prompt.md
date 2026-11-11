---
description: "Turn a dataset schema and business rules into repeatable validation checks and failure actions."
agent: data-engineer
argument-hint: "Provide the schema, key fields, ranges, and business rules."
---

Read [AGENTS.md](../../AGENTS.md) and the [data-quality-validation skill](../../skills/data-quality-validation/SKILL.md).

Design checks for:

${input:contract:Schema, key constraints, business rules, freshness, and owners}

Return checks, test cases, failure severity, quarantine/reporting behavior, and owners. Keep sensitive values out of examples. Distinguish course evidence, external recommendations, and gaps.