---
description: "Profile a dataset for schema, quality, target balance, time/group coverage, outliers, and leakage risks."
agent: data-engineer
argument-hint: "Provide the dataset path/schema, target, time fields, and intended use."
---

Read [AGENTS.md](../../AGENTS.md), the [data-profiling skill](../../skills/data-profiling-eda/SKILL.md), and the [data-quality playbook](../../playbooks/data_quality_pipeline.md).

Profile this dataset/context:

${input:data:Dataset description, schema, or safe synthetic sample}

Return a reproducible profiling checklist/code outline, findings, missing evidence, leakage risks, and follow-up checks. Do not copy real data into outputs. Tag course facts `[COURSE]`, external methods `[EXTERNAL]`, and unaddressed topics `[GAP]`.