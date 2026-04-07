# Azure AI Foundry × {a}OS-6L Vendor Mapping

> **Version:** v0.1
> **Date:** 2026-04-06
> **Status:** First mapping — subject to revision as Foundry matures

---

## Mapping Summary

Azure AI Foundry is an **L1–L4 platform with preview L5 capabilities and no L6 coverage**.

| {a}OS Layer | Foundry Coverage | Confidence |
|:-----------:|:---:|:---:|
| L6 — Human Intent, Policy & Oversight | Weak | High |
| L5 — Orchestration, Workflows & Routing | Partial (Preview) | Medium |
| L4 — Agent Logic, Skills & Execution | Good (GA) | High |
| L3 — Tools, Interfaces & External Actions | Good (GA) | High |
| L2 — Context, Memory & Semantic State | Partial (Preview) | Medium |
| L1 — Models, Data & Compute Foundation | Strong (GA) | High |

---

## Layer-by-Layer Mapping

### L1 — Models, Data & Compute Foundation

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

### L2 — Context, Memory & Semantic State

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

### L3 — Tools, Interfaces & External Actions

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

### L4 — Agent Logic, Skills & Execution Reasoning

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Single agent | Prompt Agents | GA | Production-ready, no code required |
| Container agents | Hosted Agents | Preview | No VNet support |
| Agent identity | Per-agent Entra identity | GA | Strong feature for RBAC |
| Agent versioning | Automatic versioning + rollback | GA | |
| Agent publishing | Teams, M365, BizChat | GA | Requires public endpoints |
| Evaluation | Built-in evaluators (quality, safety, task adherence) | GA | CI/CD integration via GitHub Actions |

**Gaps at L4:**

- Hosted agents have no VNet support (preview limitation)
- Publishing requires public endpoints (not viable for most defense)
- Complex skill chaining requires code-based approach (Semantic Kernel, LangGraph)

### L5 — Orchestration, Workflows & Routing

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Multi-agent workflows | Workflow Agents | Preview | Inbound VNet only |
| Model routing | Model Router | GA | Poorly documented, not auditable |
| Framework support | LangGraph, CrewAI, LlamaIndex | GA (hosted) | Via hosted agents (no VNet) |

**Gaps at L5:**

- Workflow agents are preview with partial VNet support
- No deterministic routing controls
- No circuit breakers or load balancing
- No cross-system workflow coordination
- Model Router lacks transparency for auditable environments
- Production multi-agent orchestration requires custom engineering

### L6 — Human Intent, Policy & Oversight

| Capability | Foundry Feature | Status | Notes |
|-----------|----------------|:---:|-------|
| Content filtering | Content Safety (always on) | GA | Configurable severity thresholds |
| Prompt protection | Prompt Shields | GA | Jailbreak detection |
| RBAC | Entra ID + 4 built-in roles | GA | Custom roles supported |
| Infrastructure policy | Azure Policy integration | GA | Infra-level only |
| Threat protection | Microsoft Defender integration | GA | |

**Gaps at L6:**

- No approval workflows or human-in-the-loop gates
- No governance dashboard
- No aggregated audit trail across agents/projects
- No compliance reporting
- No policy engine for agent behavior (only content and infrastructure)
- No cost governance or token budget enforcement
- No workflow-level governance (only content-level)

---

## What Must Be Built Around Foundry (The "40%")

| Need | {a}OS Layer | Recommended Approach |
|------|:-----------:|---------------------|
| Approval gates | L6 | Azure Logic Apps or custom workflow engine |
| Audit aggregation | L6 | Log Analytics + custom SIEM export |
| Compliance reporting | L6 | Power BI on Log Analytics + custom dashboards |
| Agent behavior policy | L6 | Custom policy engine (middleware) |
| Cost enforcement | L6 / L5 | APIM AI Gateway with token budgets |
| Circuit breakers | L5 | Custom middleware (Thrash Collector pattern) |
| Deterministic routing | L5 | APIM routing rules or custom router |
| Cross-agent state | L2 | Cosmos DB with access controls |
| Tool governance | L3 | API Management + Azure Policy |
| Observability in private networks | L1 | Peered App Insights workaround |
| Disaster recovery | L1 | Multi-region architecture with failover |

---

## Cross-Vendor Vocabulary Mapping

| {a}OS Concept | Azure AI Foundry | AWS Bedrock | Anthropic / Claude | LangChain |
|--------------|-----------------|------------|-------------------|-----------|
| L4 Agent | Prompt Agent / Hosted Agent | Bedrock Agent | Agent | Agent / Graph |
| L3 Tool | Function / Tool / MCP Server | Action Group | Tool use | Tool |
| L2 Memory | Agent Memory / Foundry IQ | Knowledge Base | Context | Memory |
| L5 Orchestrator | Workflow Agent / Model Router | Step Functions | System prompt | Router / Graph |
| L1 Model | Model Deployment | Foundation Model | Claude model | LLM |
| L6 Governance | Content Safety + Azure Policy | Guardrails | Constitutional AI | Callbacks |
