# Azure AI Foundry × {a}OS 7-Stratum Vendor Mapping

> **Version:** v1.0
> **Date:** 2026-04-08
> **Status:** Canonical mapping — aligned to Agentic Reference Stack v1.0
> **Supersedes:** v0.1 (6L mapping from 2026-04-06)
> **Reference model:** Agentic Reference Stack v1.0 (7 strata, locked vocabulary)

---

## Mapping Summary

Azure AI Foundry is an **L1–L3 platform with partial L4 capabilities, structural weaknesses at L5–L6, and partial L7 coverage**. The 7-stratum model reveals that what the old 6-layer analysis called "one governance gap" is actually three separate architectural problems — Experience (L7), Governance (L6), and Observability (L5) — each with different owners, interface contracts, and failure modes.

| {a}OS Stratum | Foundry Coverage | Confidence | Key Evidence |
|:---:|:---:|:---:|:---|
| L7 — Experience & Intent | Partial | Medium | Foundry Portal (classic + new), agent publishing to Teams/M365/BizChat (requires public endpoints) |
| L6 — Governance & Trust | Partial | High | Content Safety GA, RBAC GA, Azure Policy (infra-only). No approval workflows, no audit aggregation, no cost governance |
| L5 — Observability & Evaluation | Partial | High | Tracing GA for prompt agents, eval framework GA. Private App Insights breaks tracing entirely |
| L4 — Orchestration & Decisioning | Partial | Medium | Workflow agents (preview), Model Router. No circuit breakers, no deterministic routing |
| L3 — Execution & Interfaces | Good | High | Function calling GA, MCP GA, Code Interpreter, tool catalog. VNet gaps for File Search, OpenAPI, Azure Functions |
| L2 — Knowledge & Memory | Partial | Medium | Agent memory GA, AI Search GA, Foundry IQ (preview). No cross-agent state, no memory lifecycle |
| L1 — Models & Infrastructure | Strong | High | Model catalog GA, fine-tuning GA, PTU, CMK, Foundry Local |

---

## Stratum-by-Stratum Mapping

### L1 — Models & Infrastructure

> **Boundary question:** Is the model/runtime/compute/network foundation available and behaving correctly?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Model hosting | Model catalog (11K+ models) | GA | ~50-100 Azure-hosted production models |
| Model deployment | Standard, PTU, Global, Data Zone, Batch | GA | Batch not available in Gov cloud |
| Fine-tuning | SFT/DPO for GPT-4o/4.1; RFT for o4-mini | GA | Global training has no data residency |
| Encryption at rest | CMK via Azure Key Vault | GA | FIPS 140-2 compliant |
| Compute management | Managed compute for agents, evaluations | GA | VNet injection for agent compute |
| Edge inference | Foundry Local | GA | On-device model execution |

**Gaps at L1:**

- Custom model training requires Azure ML (separate service)
- Gov cloud model availability significantly reduced
- No cross-region disaster recovery (manual architecture required)
- No hybrid cloud pattern for classified environments

### L2 — Knowledge & Memory

> **Boundary question:** What context did the system know, retrieve, remember, or forget?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| RAG | Foundry IQ | Preview | Enterprise RAG engine, not production-proven |
| Vector search | Azure AI Search integration | GA | Private endpoint supported |
| Agent memory | Conversation memory per agent | GA | Within agent scope only |
| File processing | File Search tool | GA | NOT supported in VNet isolation |
| Document processing | Document Intelligence, Content Understanding | GA | Part of Foundry Tools |

**Gaps at L2:**

- No cross-agent shared state management
- No memory compaction or lifecycle management
- Foundry IQ is preview — production maturity unknown
- File Search breaks in network-isolated environments

### L3 — Execution & Interfaces

> **Boundary question:** What external action was invoked, against which interface, and what happened?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Function calling | Native function/tool calling | GA | Works in VNet |
| MCP support | MCP server integration | GA | Private MCP works in VNet |
| Enterprise connectors | 1,400+ via Logic Apps | GA | Logic Apps is separate service; not all work in VNet |
| Code execution | Code Interpreter | GA | Microsoft backbone network |
| Web search | Bing Grounding, Web Search | GA | Routes over PUBLIC internet |
| Browser automation | Browser Automation, Computer Use | Preview | NOT supported in VNet |

**Gaps at L3:**

- No tool-level access control or governance
- Logic Apps connectors don't all work in VNet isolation
- Web search tools break network isolation compliance
- OpenAPI tool not supported in VNet

### L4 — Orchestration & Decisioning

> **Boundary question:** What happens next, in what order, with which agent, under which stop conditions?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Multi-agent workflows | Workflow Agents | Preview | Inbound VNet only |
| Model routing | Model Router | GA | Poorly documented, not auditable |
| Framework support | LangGraph, CrewAI, LlamaIndex | GA (hosted) | Via hosted agents (no VNet) |
| Single agent orchestration | Prompt Agents | GA | Production-ready, no code required |
| Agent identity | Per-agent Entra identity | GA | Strong feature for RBAC |
| Agent versioning | Automatic versioning + rollback | GA | |

**Gaps at L4:**

- Workflow agents are preview with partial VNet support
- No deterministic routing controls
- No circuit breakers or load balancing
- No cross-system workflow coordination
- Model Router lacks transparency for auditable environments
- Production multi-agent orchestration requires custom engineering

### L5 — Observability & Evaluation

> **Boundary question:** What actually happened, how well did it perform, and where did it fail?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Tracing | OpenTelemetry-based tracing | GA | Prompt agents only; preview for other agent types |
| Telemetry backend | Application Insights integration | GA | **Breaks entirely with private App Insights** |
| Built-in evaluators | Quality, safety, task adherence | GA | Genuinely useful for CI/CD gating |
| Custom evaluators | Configurable evaluation pipelines | GA | Supports custom dimensions and prompts |
| Continuous evaluation | Scheduled evaluation against live data | GA | 90-day trace retention |
| CI/CD integration | GitHub Actions evaluation gates | GA | Evaluation as deployment gate |

**Gaps at L5:**

- **Tracing breaks with private Application Insights** — the single largest hidden gap for production deployments
- Tracing only GA for prompt agents; preview for workflow/hosted agents
- No end-to-end audit trail aggregation across agents and projects
- No custom dashboarding for operational health (requires Log Analytics / Grafana)
- No cost visibility tied to evaluation outcomes
- Observability and network isolation are in direct tension

### L6 — Governance & Trust

> **Boundary question:** Who is allowed to do this, under what policy, with what risk and budget?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Content filtering | Content Safety (always on) | GA | Configurable severity thresholds |
| Prompt protection | Prompt Shields | GA | Jailbreak detection |
| RBAC | Entra ID + 4 built-in roles | GA | Custom roles supported |
| Infrastructure policy | Azure Policy integration | GA | Infra-level only |
| Threat protection | Microsoft Defender integration | GA | |
| Groundedness detection | Content Safety groundedness evaluator | GA | Detects hallucination in responses |

**Gaps at L6:**

- No approval workflows or human-in-the-loop gates
- No governance dashboard
- No aggregated audit trail across agents/projects
- No compliance reporting
- No policy engine for agent behavior (only content and infrastructure)
- No cost governance or token budget enforcement
- No workflow-level governance (only content-level)

### L7 — Experience & Intent

> **Boundary question:** What is the user asking, seeing, approving, or rejecting?

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Management portal | Foundry Portal (classic + new toggle) | GA | New portal doesn't support network isolation workflows |
| Agent builder | Portal-based agent builder | GA | Visual tool configuration |
| Agent publishing | Teams, M365, BizChat, Copilot Studio | GA | **Requires public endpoints** |
| API surface | REST API + Python/JS SDKs | GA | Full programmatic access |
| Agent playground | Prompt agent testing playground | GA | Interactive testing before deployment |

**Gaps at L7:**

- New Foundry Portal does not support network-isolated management (must use classic, SDK, or CLI)
- Agent publishing requires public endpoints — not viable for most security-conscious deployments
- No custom UX framework for end-user-facing experiences
- No intent disambiguation or escalation flow tools
- No approval surfaces for human-in-the-loop decisions
- The "experience" for most teams will be custom-built, not Foundry-native

---

## What Must Be Built Around Foundry

| Need | {a}OS Stratum | Recommended Approach |
|------|:---:|---------------------|
| Custom end-user experience | L7 | Custom frontend or copilot integration |
| Approval gates | L6 | Azure Logic Apps or custom workflow engine |
| Audit aggregation | L6 | Log Analytics + custom SIEM export |
| Compliance reporting | L6 | Power BI on Log Analytics + custom dashboards |
| Agent behavior policy | L6 | Custom policy engine (middleware) |
| Cost enforcement | L6 | APIM AI Gateway with token budgets |
| Observability workaround | L5 | Peered non-private App Insights or Log Analytics export |
| Custom dashboarding | L5 | Grafana / Power BI on Log Analytics |
| Circuit breakers | L4 | Custom middleware (Thrash Collector pattern) |
| Deterministic routing | L4 | APIM routing rules or custom router |
| Tool governance | L3 | API Management + Azure Policy |
| Cross-agent state | L2 | Cosmos DB with access controls |
| Disaster recovery | L1 | Multi-region architecture with failover |

---

## Cross-Vendor Vocabulary Mapping

| {a}OS Concept | Azure AI Foundry | AWS Bedrock | Anthropic / Claude | LangChain |
|:---|:---|:---|:---|:---|
| L7 Experience surface | Foundry Portal / Agent Publishing | Bedrock Console / API | Claude.ai / API | Chainlit / Gradio |
| L6 Governance | Content Safety + Azure Policy | Guardrails | Constitutional AI | Callbacks / Guards |
| L5 Observability | App Insights + Eval Framework | CloudWatch + Bedrock Logs | — | LangSmith / Langfuse |
| L4 Orchestrator | Workflow Agent / Model Router | Step Functions | System prompt | Router / Graph |
| L3 Tool | Function / Tool / MCP Server | Action Group | Tool use | Tool |
| L2 Memory | Agent Memory / Foundry IQ | Knowledge Base | Context | Memory |
| L1 Model | Model Deployment | Foundation Model | Claude model | LLM |
