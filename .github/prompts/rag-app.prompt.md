---
description: "Design or evaluate a RAG application with approved sources, access-aware retrieval, grounded answers, abstention, and golden tests."
agent: genai-agent-engineer
argument-hint: "Describe users, approved corpus, access rules, questions, and failure impact."
---

Read [AGENTS.md](../../AGENTS.md), the [RAG skill](../../skills/rag/SKILL.md), and the [RAG/LLM playbook](../../playbooks/rag_llm_app.md).

RAG task:

${input:task:Users, sources, permissions, intended questions, and constraints}

Return a bounded architecture, retrieval/generation evaluation plan, source-grounding and abstention behavior, prompt-injection tests, privacy controls, and operational gaps. Tag claims; never present external knowledge as course content.