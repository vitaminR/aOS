# AFS09 — Research Pack: Cost Governance Is Not a Feature — It's an Architecture

## Core Thesis

Azure AI Foundry provides basic cost tracking through Azure Cost Management but does not natively solve per-team chargeback, per-user token budgets, real-time spend enforcement, or circuit breakers for runaway agent loops. Cost governance in an AI platform is not a feature to be enabled — it is a custom architecture that must be designed and built, typically using Azure API Management as an AI Gateway.

## Key Facts

### What Foundry Provides Natively

- Azure Cost Management budgets and alerts (subscription/resource-group scoped)
- Per-resource cost tracking (standard Azure metering)
- Evaluation token tracking within Foundry projects
- PTU (Provisioned Throughput Units) for committed capacity pricing
- Pay-as-you-go model consumption metering

### What Foundry Does NOT Provide

- Per-project or per-team chargeback
- Per-user token budgets
- Real-time spend enforcement or hard spending caps
- Circuit breakers for runaway agent loops
- Detailed cross-service cost attribution (model + search + storage combined)
- Kill switches that halt an agent mid-execution based on cost thresholds
- Native governance dashboard for cost across projects

### Cost Sources in Foundry

- **Model consumption:** Token-based billing (input + output tokens)
- **Storage:** Azure Blob Storage for agent data, file uploads
- **Search:** Azure AI Search for RAG workloads (index size + query volume)
- **Networking:** Private endpoints, VNet injection, data transfer
- **Compute:** Agent compute (Container Apps environment), evaluation runs
- **PTU commitments:** Reserved capacity — significant executive-level cost decisions, billed whether used or not

### APIM as AI Gateway Pattern

- Azure API Management positioned as a reverse proxy in front of Foundry endpoints
- Capabilities: rate limiting (per-user, per-team, per-app), token metering, request logging, cost attribution tagging
- Can enforce hard spending caps by denying requests after threshold
- Kill switch: disable a backend or product subscription immediately
- Chargeback: tag requests by team/project, aggregate in Log Analytics, export to FinOps
- Token counting: APIM policies can estimate token usage from request/response payload size
- Latency trade-off: adds ~5-15ms per request (acceptable for most enterprise workloads)

### PTU Cost Dynamics

- PTU = committed capacity, billed monthly regardless of utilization
- Significant executive cost decision — typically $10K-$100K+/month depending on model and scale
- Over-provisioning wastes money; under-provisioning causes throttling
- No automatic scaling between PTU and pay-as-you-go (must architect spillover manually)
- PTU decisions are often made without platform team input — finance/exec level

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | No native chargeback | Azure AI Foundry projects share a parent resource billing scope. No built-in mechanism to attribute costs to individual teams or projects without custom tagging and APIM metering. |
| R2 | No native token budgets | Azure Cost Management supports budget alerts but not hard enforcement. An alert fires; nothing stops the spend. |
| R3 | No circuit breaker for agent loops | No native mechanism in Foundry or Azure OpenAI to detect and halt a looping agent. Requires external monitoring + kill logic. |
| R4 | APIM is the recommended gateway pattern | Microsoft's own AI Gateway reference architecture recommends APIM for cost governance, rate limiting, and chargeback. Documented in Azure Architecture Center. |
| R5 | $22 runaway loop was local tooling | The anecdote is from a local agent development environment (agent tooling loop), not from Azure AI Foundry production. Must frame as universal agent cost lesson, not Foundry-specific. |

## Red-Team Notes

### CRITICAL: $22 Attribution

- The $22 runaway loop story is from **local agent tooling** — an agent in a development loop calling an API repeatedly
- It is **NOT** from Azure AI Foundry
- Frame as: "I learned this lesson from a local agent loop — and the lesson applies everywhere, including Foundry, because no managed platform has native circuit breakers either"
- Do NOT write or imply "Foundry cost me $22 overnight"
- The universality of the lesson is the point: if a local agent can do this, a production agent without guardrails can do worse

### Cost Numbers

- $22 is the real number from the author's experience — use it
- Do not fabricate or inflate numbers for engagement
- Do not speculate about what "could" happen with larger models — stick to what did happen

### APIM Complexity

- Do not oversimplify APIM setup — it requires networking, policy configuration, and operational knowledge
- Do not present APIM as a quick fix — it is a real infrastructure decision
- Acknowledge the trade-off: added latency, added operational surface, added cost (APIM itself is not free)

## Anti-Patterns to Avoid in Post

- Don't blame Foundry for not having cost governance — no managed AI platform does natively
- Don't present this as a Microsoft-specific problem — it's structural to the category
- Don't suggest Azure Cost Management alerts are sufficient — they are reactive, not preventive
- Don't minimize the $22 — the point is that $22 at 3 AM with no one watching is a symptom of a missing architecture
- Don't make APIM sound like a product pitch — it's the author's architectural recommendation, with trade-offs acknowledged
