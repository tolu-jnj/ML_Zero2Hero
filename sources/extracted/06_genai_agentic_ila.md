# 06 - GenAI, Agentic AI, and ILA Error Tracking

## Summary

- The session distinguishes content-generating GenAI from agentic systems that coordinate models, tools, workflow steps, and sometimes human review. [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
- The ILA error-tracking case combines automated data ingestion, classification/triage, historical-case search, recommended resolutions, analytics, and human approval; the deck frames the work as multiple stages with different automation levels. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slides 6-8]

## Key Concepts

- The expert describes an agentic workflow as an end-to-end process using GenAI with other tools and capabilities, with humans retained for some decisions. [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
- A comparison graphic characterizes agentic AI as autonomous, goal-oriented, tool-using, and able to adapt, while characterizing generative AI as content-oriented; this is the slide's simplified framing rather than a universal taxonomy. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 5]
- The ILA deck distinguishes error ingestion, triage, error classification, guidance classification, resolution recommendations, and auto-resolution. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 7]
- The case presentation calls out health monitoring, error handling, governance, analytics, and reporting as related concerns. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 6]
- The final session explicitly notes monitoring of output quality, latency, usage, and cost as operational concerns for deployed AI applications. [COURSE: 06_Week_6_Transcript.txt#lines 240-255]

## Worked Examples and Case Studies

- ILA means Intercompany Logistics Automation in the slide; the case describes transactions between sending and receiving entities that must be recorded in SAP S/4. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 6]
- The presented system captures errors, suggests likely causes/actions, supports assignment and analytics, and retains human approval for cases that cannot be safely resolved automatically. [COURSE: 06_Week_6_Transcript.txt#lines 50-115]
- The slide estimates 75,000 transactions per year today and over 1.2 million at scale, and presents projected labor savings; these are estimates from the case slide, not independently verified results. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 8]
- The expert describes combining traditional ML/anomaly detection and forecasting with deterministic/statistical tools and LLM functions rather than assigning every step to an LLM. [COURSE: 06_Week_6_Transcript.txt#lines 115-160]

## Tools and Algorithms Named

- LLMs, agents, deterministic tools, statistical analysis, Isolation Forest, forecasting/XGBoost, SAP S/4, and human-in-the-loop review are named. [COURSE: 06_Week_6_Transcript.txt#lines 45-160]
- The optional course exercise is described as building a simple GenAI chatbot. [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 4] [COURSE: 05 Expert Guide C2 W5 Live Event.pdf#slide 8]

## Q&A

- Asked whether ML is used for pattern recognition and AI for recommendations, the expert says the described tool combines ML, deterministic/statistical methods, and GenAI. [COURSE: 06_Week_6_Transcript.txt#lines 115-160]
- Asked how the business value is measured, the response points to estimated labor hours saved and gives case estimates. [COURSE: 06_Week_6_Transcript.txt#lines 160-195] [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slide 8]
- Asked where to continue hands-on work, the expert recommends VS Code and notes that corporate Copilot access requires approval in the described environment. [COURSE: 06_Week_6_Transcript.txt#lines 285-315]

## Unclear Points

- The transcript contains repeated ASR variants such as "agent Ki" and "Gen. AI"; these are normalized to "agentic AI" and "GenAI" where the surrounding definition and deck title establish the intended term. [?] [COURSE: 06_Week_6_Transcript.txt#lines 20-40]
- The deck presents forecast transaction volume, savings, and automation percentages as estimates; assumptions, realized outcomes, and evaluation methodology are not fully documented in the materials. [?] [COURSE: 06 Expert Guide C2 W6 Live Event.pdf#slides 7-8]
- The session is a case study, not a reusable agent architecture, authorization model, or production safety standard. [GAP]

## Go Deeper

- [GAP] Agent permissions, tool-call safety, idempotency, retries, audit trails, prompt injection, deterministic fallback, offline/online evaluation, and incident response need dedicated design and testing.
- [EXTERNAL: official documentation for the selected LLM/agent framework, authoritative RAG and agent-evaluation references, and organizational security/governance standards] Define bounded tool permissions and human approval based on the consequences of each action.