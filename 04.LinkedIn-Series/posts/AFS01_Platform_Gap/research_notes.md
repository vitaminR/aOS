# AFS01 — Research Notes

## The Structural Gap Pattern

Every major managed AI platform follows the same coverage pattern:

**Strong (L1 — Models/Compute):**
- Model catalogs (Azure: 11K+, Bedrock: 100+, Vertex: 100+)
- Deployment types (PTU, on-demand, serverless)
- Fine-tuning support
- Encryption at rest and in transit

**Good (L3-L4 — Tools/Agents):**
- Function/tool calling
- Agent frameworks (prompt agents, retrieval agents)
- Connector ecosystems
- Evaluation frameworks

**Partial (L2 — Context/Memory):**
- RAG integration with vector stores
- Per-agent conversation memory
- No cross-agent state management on any platform
- No memory lifecycle management on any platform

**Weak-to-Absent (L5-L6 — Orchestration/Governance):**
- Orchestration in preview (Azure Workflow Agents, Bedrock multi-agent)
- No deterministic routing on any platform
- No circuit breakers natively
- No approval gates natively
- No governance dashboards natively
- No cost enforcement natively
- No compliance reporting natively

## Why This Gap Exists

These platforms are built by cloud infrastructure teams, not enterprise governance teams. They optimize for developer adoption, not operational safety. Governance is inherently custom to the organization — approval workflows, compliance standards, cost policies, and audit requirements differ by industry, company size, and regulatory environment.

The gap is not a missing feature request. It's a category boundary. The platform vendors would need to become governance vendors, which is a different business entirely.

## Where Failures Actually Happen

Reviewing public AI deployment failures:
- **Air Canada chatbot (2024):** Hallucination blamed, but root cause was no action boundary (L3) and no approval gate (L6) on customer-facing commitments
- **Zillow iBuying (2021):** Model accuracy blamed, but root cause was no circuit breaker (L5) on automated purchasing decisions
- **Amazon recruiting tool (2018):** Bias blamed (L1), but root cause was no governance review gate (L6) on model training data
- **Google Gemini image generation (2024):** Output quality blamed (L1), but root cause was content safety policy conflict (L6) overriding model behavior

Pattern: the public narrative blames L1 (the model). The operational root cause is almost always L5-L6 (orchestration/governance).

## Competitive Landscape (not for use in post — vendor-neutral framing)

| Capability | Azure AI Foundry | AWS Bedrock | Vertex AI |
|---|---|---|---|
| L6 Governance | Content Safety only | Guardrails (I/O only) | Model monitoring only |
| L6 Cost enforcement | None native | None native | None native |
| L5 Multi-agent | Preview | Preview | Preview |
| L5 Circuit breakers | None | None | None |
| L4 Agents | GA (prompt) | GA (agents) | GA (agents) |
| L3 Tools | GA (MCP, functions) | GA (action groups) | GA (extensions) |
| L2 RAG | Preview (IQ) + GA (Search) | GA (Knowledge Bases) | GA (RAG Engine) |
| L1 Models | Strong | Strong | Strong |

All three follow the same pattern. The gap is structural to managed AI platforms as a category.
