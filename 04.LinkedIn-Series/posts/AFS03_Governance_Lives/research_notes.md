# AFS03 — Research Notes

## The {a}OS 7-Stratum Model

The 7-stratum model is a reference architecture for agentic AI systems. It names seven layers from infrastructure at the bottom to experience at the top — same concept as the OSI model for networking, but for agentic AI platforms.

### The Seven Strata (L1-L7)

| Stratum | Name | What It Covers |
|:---:|---|---|
| **L7** | Experience & Intent | User-facing surfaces, intent disambiguation, approval UX, escalation flows, copilot integrations |
| **L6** | Governance & Trust | Policy enforcement, approval gates, audit trails, compliance reporting, agent behavior constraints, cost governance |
| **L5** | Observability & Evaluation | Tracing, monitoring, evaluation frameworks, dashboards, end-to-end audit trails, continuous evaluation |
| **L4** | Orchestration & Decisioning | Multi-agent routing, workflow orchestration, circuit breakers, load balancing, deterministic routing |
| **L3** | Execution & Interfaces | Function calling, tool catalogs, MCP, code execution, connectors, API management |
| **L2** | Knowledge & Memory | RAG, vector stores, agent memory, document pipelines, context window management, memory lifecycle |
| **L1** | Models & Infrastructure | Model hosting, inference, fine-tuning, compute, encryption, networking, identity |

### Why 7 Strata, Not 6 Layers

The previous 6-layer model combined observability, governance, and experience into a single "governance" layer. The 7-stratum model separates them because:

1. **Different owners.** Observability is typically owned by platform engineering. Governance is owned by security/compliance. Experience is owned by product teams.
2. **Different interface contracts.** Observability emits telemetry. Governance enforces policy. Experience receives user intent. These are different APIs, different data flows, different failure modes.
3. **Different failure modes.** Observability failure = you can't see what happened. Governance failure = nobody approved it. Experience failure = the user couldn't express what they wanted. Conflating them means you can't route the incident to the right team.

The upgrade from 6L to 7S is not cosmetic — it reveals three separate architectural problems where the old model showed one.

## How Foundry Maps to the 7-Stratum Model

### L1 — Models & Infrastructure: STRONG

- 11,000+ model catalog (realistically ~50-100 Azure-hosted that matter)
- Fine-tuning (GA), PTU deployments, managed compute
- CMK encryption, private endpoints, Entra ID
- Foundry Local for edge/hybrid scenarios

### L2 — Knowledge & Memory: PARTIAL

- Agent memory (GA) — per-agent conversation history
- Azure AI Search (GA) — vector + keyword + semantic
- Foundry IQ (preview) — enterprise RAG engine, not production-ready
- Document Intelligence (GA) for extraction
- **Gap:** No cross-agent shared state. No memory compaction or lifecycle management. No production RAG governance.

### L3 — Execution & Interfaces: GOOD

- Function calling (GA), MCP (GA), Code Interpreter
- Tool catalog with Logic Apps connectors (1,400+)
- **Gap:** Multiple tools do NOT work in VNet-isolated environments (File Search, OpenAPI Tool, Azure Functions, Browser Automation, Computer Use, A2A, Image Gen). Tool-level governance is custom.

### L4 — Orchestration & Decisioning: PARTIAL

- Prompt agents (GA) — single-agent orchestration
- Workflow agents (preview) — multi-step, partial VNet
- Hosted agents (preview) — no VNet support
- Model Router — poorly documented, not auditable
- **Gap:** No production multi-agent orchestration. No deterministic routing. No circuit breakers. No cross-system workflow coordination.

### L5 — Observability & Evaluation: WEAK

- OpenTelemetry tracing (GA for prompt agents only)
- Application Insights integration
- Built-in evaluators (quality, safety, task adherence)
- CI/CD evaluation gates via GitHub Actions
- **CRITICAL GAP:** Tracing breaks entirely with private Application Insights. This is a hard blocker for any team needing both network isolation and observability. End-to-end audit trail does not exist natively. Custom dashboarding required.

### L6 — Governance & Trust: WEAK

- Content Safety (GA) — prompt shields, groundedness detection, protected material detection
- RBAC (GA) — four Foundry-specific roles
- Azure Policy for infrastructure governance
- Microsoft Defender integration
- **CRITICAL GAP:** No approval workflows. No governance dashboard. No aggregated audit trail. No compliance reporting. No agent behavior policy engine. No cost governance or token budget enforcement. Content Safety is content filtering, not workflow governance.

### L7 — Experience & Intent: PARTIAL

- Foundry Portal (classic + new)
- Agent publishing to Teams/M365/BizChat
- API surface for custom frontends
- Playground for testing
- **Gap:** No custom UX framework. No intent disambiguation. No approval surfaces. No escalation flows. New portal doesn't support network isolation. Publishing to Teams/M365 requires public endpoints.

## The OSI Model Analogy

The OSI model (1984) gave networking a common vocabulary. Before it, "the network is broken" could mean anything from a physical cable issue (L1) to an application bug (L7). After OSI, teams could say "we have an L3 routing problem" and everyone knew the scope.

The {a}OS 7-stratum model does the same for agentic AI. "The AI broke" becomes "we have an L6 governance failure — no approval gate on customer-facing actions" or "we have an L5 observability failure — tracing is broken in our private network."

**Key parallel:** OSI didn't replace networking protocols. It named them. {a}OS doesn't replace AI platforms. It names the strata so teams can communicate about where problems live.

## Why "One Gap" Is Actually Three Strata

When teams say "we need governance," they typically mean three things simultaneously:

1. **"We can't see what happened"** — This is L5 (Observability). Missing traces, incomplete audit trails, no cost-to-evaluation visibility. The fix is telemetry architecture, not policy.

2. **"Nobody approved this"** — This is L6 (Governance). Missing approval gates, no compliance reporting, no agent behavior constraints. The fix is policy enforcement, not monitoring.

3. **"The user couldn't do what they needed"** — This is L7 (Experience). Missing approval surfaces, no escalation flows, no intent disambiguation. The fix is UX, not backend policy.

Three different owners. Three different codebases. Three different incident response playbooks. Treating them as one problem guarantees that the wrong team gets the incident.

## Public AI Failure Root Cause Analysis

| Failure | Public Blame | Actual Stratum | Root Cause |
|---|---|:---:|---|
| Air Canada chatbot (2024) | "Model hallucinated" (L1) | L6 | No approval gate on customer-facing commitments |
| Zillow iBuying (2021) | "Model was inaccurate" (L1) | L5 | No circuit breaker on automated purchasing decisions |
| Amazon recruiting tool (2018) | "Model was biased" (L1) | L6 | No governance review gate on training data |
| Google Gemini image gen (2024) | "Output quality" (L1) | L6 | Content safety policy conflict overriding model behavior |
| Author's $22 runaway loop | "Agent looped" (L4) | L6 | No cost kill switch or token budget enforcement |

**Pattern:** The public narrative consistently blames L1 (the model). The operational root cause is consistently L5-L7 (observability, governance, experience).
