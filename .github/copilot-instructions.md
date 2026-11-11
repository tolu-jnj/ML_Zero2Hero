# GitHub Copilot Workspace Notes

Read the root [AGENTS.md](../AGENTS.md) first; it is canonical for every agent.

- Canonical role contracts are in `/agents/*.agent.md` and reusable prompts are in `/prompts/*.prompt.md`.
- `.github/agents/*.agent.md` and `.github/prompts/*.prompt.md` are thin VS Code discovery wrappers; keep workflow content in the top-level files.
- Load the matching canonical procedure from `/skills/<name>/SKILL.md`; `.github/skills/README.md` points to that directory.
- Preserve the source tags and confidentiality rules in `AGENTS.md`; never send this internal content to a public remote.