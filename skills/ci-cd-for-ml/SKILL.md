---
name: ci-cd-for-ml
description: "Use when automating tests, dependency checks, model artifact validation, and controlled ML releases in CI/CD."
---

# CI/CD for ML

## Course Grounding

The course does not teach CI/CD or automated ML release workflows. [GAP]

## Workflow

1. Pin dependencies and define reproducible setup/test commands.
2. Run formatting, unit tests, data/schema checks, and dependency/security checks on change. [EXTERNAL: official GitHub Actions and package-manager documentation]
3. Validate model artifacts and evaluation gates without exposing secrets.
4. Separate test, staging, and production credentials/environments.
5. Require approval and document rollback before production deployment. [EXTERNAL: established MLOps references]

```yaml
name: tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m pytest
```

This is an illustrative workflow; pin actions and follow the organization's approved runner/security policy. [EXTERNAL: official GitHub Actions documentation]

## Checklist

- [ ] Tests run in a clean environment.
- [ ] Dependencies and CI actions are pinned/reviewed.
- [ ] Secrets use protected secret stores, not repository files.
- [ ] Model quality gate and rollback path are defined.

## Common Pitfalls

- Letting CI access production credentials for untrusted pull requests.
- Treating a passing code test as proof of model quality.

## Go Deeper

- [GAP] CI/CD and model release gates are outside the course.
- [EXTERNAL: official GitHub Actions docs and established MLOps references]