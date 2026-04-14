# AFS06 — Research Pack: Models, Money, and the Reality of Model Access

## Core Thesis

The model you prototype on and the model you deploy on may not be the same model. Model availability varies dramatically by region, compliance environment, and deployment type — and most teams discover this after they have committed to an architecture. Hardcoded model names are tech debt. PTU commitments are executive financial decisions that need architectural input.

## Key Facts

- Azure AI Foundry markets 11,000+ models; ~50-100 are Azure-hosted and production-relevant
- PTU (Provisioned Throughput Units) = reserved capacity with significant monthly commitment
- Pay-as-you-go = consumption-based, no capacity guarantee, no latency SLA
- Gov cloud (IL5): GPT-4.1 available at 300K context (vs 1M commercial), no GPT-5.4, no batch deployments, no Model Router
- Gov cloud (IL6): Azure OpenAI does not exist — hard constraint
- Model Router is poorly documented and not auditable for compliance
- New Foundry resource model not documented for Gov cloud
- Model availability changes frequently — methodology for checking matters more than static lists

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | 11,000+ is marketing, ~50-100 matter | Azure AI Foundry model catalog. Filter by "Azure-hosted" deployment. Majority of catalog is marketplace/third-party requiring self-deployment. |
| R2 | Gov cloud availability is dramatically reduced | Azure Government docs: model availability lists maintained separately. GPT-5.4 absent. GPT-4.1 context reduced to 300K. No batch deployments. |
| R3 | IL6 has no Azure OpenAI | Azure Government documentation: Azure OpenAI not listed for IL6 (Gov Secret). |
| R4 | PTU is a significant financial commitment | Azure OpenAI pricing page. PTU requires reserved capacity commitment. Pricing not public but enterprise-significant. |
| R5 | Model Router is not auditable | Azure AI Foundry documentation. Model Router routes across deployments but does not provide per-request model-instance audit trail. |
| R6 | Context window assumptions break silently | Author experience: pipeline designed for 1M context deployed to Gov cloud with 300K limit. No error — just truncation and degraded quality. |

## Anti-Patterns to Avoid in Post

- Do NOT list specific model version numbers that will date within weeks
- Do NOT frame Gov cloud as "broken" — it is constrained by design for security reasons
- Do NOT disclose non-public pricing — frame PTU as "significant commitment" qualitatively
- Do NOT position this as Azure-specific failure — the pattern applies to all cloud providers
- Do NOT present abstraction layers as free — acknowledge the engineering cost of model portability
- Do NOT use classified or non-public Gov cloud information — all claims must be from public documentation

## Durability Strategy

Model availability is the fastest-changing content in this series. To keep the post durable:

1. **Teach methodology, not facts:** "Filter by region, then compliance, then deployment type" ages better than "GPT-4.1 is available in East US"
2. **Use qualitative framing:** "Significantly reduced" not "exactly 47 models"
3. **Include verification callout:** Tell readers to check current docs, not trust the post
4. **Date the research:** Readers should know when the claims were verified
5. **Focus on the principle:** "Hardcoded model names are tech debt" is permanently true regardless of which specific models are available

## Visual Strategy

Primary visual: Shrinking funnel from "11,000+ models" to "available at your compliance level."
Purpose: One image that communicates the entire constraint story.
Caveat text on visual: "Approximate. Verify current availability."
