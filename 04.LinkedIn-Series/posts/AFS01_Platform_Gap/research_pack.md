# AFS01 — Research Pack: Your AI Platform Doesn't Ship What You Think It Ships

## Core Thesis

Managed AI platforms (Azure AI Foundry, AWS Bedrock, Vertex AI) provide genuine value at the infrastructure and agent layers — but they structurally do not solve governance, cost enforcement, or operational observability in regulated environments. The gap is architectural, not accidental.

## Key Facts

- Azure AI Foundry has no native cost enforcement (no per-team chargeback, no token budgets, no kill switches)
- Azure AI Foundry has no governance dashboard, no approval gates, no aggregated audit trail
- Azure AI Foundry's network isolation has confirmed gaps: 10+ features don't work in VNet-isolated environments
- Tracing breaks entirely with private Application Insights — a conflict between two requirements (network isolation + observability)
- AWS Bedrock has Guardrails but no workflow-level governance or cost chargeback
- Vertex AI has model monitoring but no agentic orchestration governance
- All three platforms deliver strong L1 (models/compute) and partial L3-L4 (tools/agents)
- None of the three deliver L6 (governance/oversight) natively

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Platforms don't ship governance | Azure: no approval gates, no governance dashboard, no compliance reporting. Content Safety = content filtering, not governance. AWS: Guardrails = model I/O filtering, not workflow governance. |
| R2 | Cost enforcement is custom | Azure: requires APIM gateway. No native per-project chargeback or token budgets. AWS: no native per-agent cost limits. |
| R3 | Network isolation has gaps | Azure: File Search, OpenAPI Tool, Azure Functions, Browser Automation, Computer Use, A2A, Image Gen, Logic Apps all NOT supported in VNet. Bing/WebSearch route over public internet. |
| R4 | Observability conflicts with isolation | Azure: tracing breaks with private App Insights. This is documented and confirmed. |
| R5 | Failures happen in the gap | Author experience: the $22 runaway loop was a governance failure (L6 — no cost kill switch), not a model failure (L1). Air Canada chatbot was a tool governance failure (L3 — no action boundary), not a hallucination issue (L1). |

## Anti-Patterns to Avoid in Post

- Don't turn this into a vendor comparison — the point is structural, not competitive
- Don't use "60%" or any specific percentage — it's a heuristic, not measured
- Don't introduce {a}OS by name — that's Post 3. This post names the problem; Post 3 names the framework.
- Don't list features that DO work — the post is about what's absent, not what's present
- Don't be cynical — the platform is genuinely valuable, the gap is genuinely real
