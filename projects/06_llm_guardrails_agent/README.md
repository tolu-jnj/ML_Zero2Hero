# Project 06: Local LLM Guardrails and Approval Gate

This standard-library-only demo models evidence-ID checks, abstention, access rejection, and human approval for an action. It reflects the course's discussion of hallucination, tools, and human review. [COURSE: 05_Week_5_Transcript.txt#lines 221-300] [COURSE: 06_Week_6_Transcript.txt#lines 20-40]

Run from the repository root with `make run-06`. Run tests with `make test-06`.

There is no network call or language model in this project. A citation ID check cannot prove semantic support; actual LLM evaluation, prompt-injection testing, and production authorization are `[GAP]` topics that need `[EXTERNAL: official provider safety documentation and organizational security policy]`.