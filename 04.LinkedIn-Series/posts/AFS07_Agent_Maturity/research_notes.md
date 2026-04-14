# AFS07 — Research Notes

## The Three Agent Types in Azure AI Foundry

Azure AI Foundry offers three distinct agent architectures. They share the same project context and identity layer, but differ materially in execution model, maturity, and network compatibility.

### 1. Prompt Agents (GA)

- **Execution model:** Single-turn or multi-turn conversation with tool calling. The agent receives a system prompt, user input, and optionally calls tools (functions, code interpreter, file search, Azure AI Search, Bing, OpenAPI).
- **Status:** Generally Available
- **VNet support:** Full. Prompt agents work inside VNet-isolated projects. Tool calls respect network boundaries (with documented exceptions for Bing/WebSearch).
- **Identity:** Per-agent Entra ID (managed identity). Agents authenticate to downstream resources via their own identity, not the user's.
- **Production readiness:** Ready for regulated environments. GA SLA, VNet-compatible, auditable via Entra identity, traceable via Application Insights (with the known private endpoint caveat from AFS05).
- **Limitations:** Single-agent only. No multi-step orchestration. No branching logic. If you need conditional flows, you build them in your application code.

### 2. Workflow Agents (Preview)

- **Execution model:** Multi-step orchestration with branching, loops, and conditional logic. Closer to a state machine than a chat agent. Can coordinate multiple tool calls in sequence.
- **Status:** Preview
- **VNet support:** Partial — inbound VNet only. The agent can receive requests from inside the VNet, but outbound calls (to tools, to external services) may not fully respect VNet boundaries.
- **Identity:** Per-agent Entra ID (same identity model as prompt agents).
- **Production readiness:** Not ready for regulated production. Preview status means API changes without notice, no SLA, and partial VNet means network isolation is incomplete.
- **Key risk:** Teams building workflow agents today may need to rebuild when the API changes at GA. The orchestration graph format is not guaranteed to be stable.

### 3. Hosted Agents (Preview)

- **Execution model:** Container-based agents running in Azure-managed compute. The agent runs as a service, not as a function call. Supports long-running tasks, background processing, and persistent state.
- **Status:** Preview
- **VNet support:** None. Hosted agents run on Microsoft-managed infrastructure that does not currently support customer VNet injection.
- **Identity:** Per-agent Entra ID (same identity model).
- **Production readiness:** Not ready for regulated production. No VNet = no network isolation = not compliant for most regulated environments. Preview status adds API instability risk.
- **Key risk:** The lack of VNet support is not a configuration gap — it's architectural. Hosted agents need to run on infrastructure that Microsoft manages, and VNet injection for that infrastructure is not available.

## Cross-Cutting: Agent Identity

One genuinely strong feature across all three types: per-agent Entra identity. Each agent gets its own managed identity in Entra ID. This means:

- Agents authenticate to Azure resources (Key Vault, Storage, SQL) as themselves, not as the deploying user
- RBAC can be scoped per-agent
- Audit logs show which agent took which action
- Identity is not tied to a user session — agents can act autonomously within their RBAC scope

This is architecturally sound. The identity layer is one of the strongest parts of the Foundry agent design.

## Cross-Cutting: Teams/M365 Publishing

Publishing agents to Microsoft Teams or M365 Copilot requires public endpoints. This creates a direct conflict with VNet-isolated deployments:

- If your project enforces VNet isolation, you cannot publish agents to Teams without exposing a public endpoint
- This is a policy decision, not a bug — Teams requires public reachability by design
- The workaround is an API Management gateway or Application Gateway in front of the agent, but this adds complexity and cost

## The Production Rule

The maturity spread creates a clear decision framework:

1. **Build first production value on prompt agents** — they're GA, VNet-compatible, and stable
2. **Prototype on workflow agents** — useful for validating multi-step patterns, but don't promise production dates
3. **Evaluate hosted agents** — understand the model, but don't build anything that requires network isolation
4. **Never bet your production timeline on preview stability** — preview APIs change. Budget for rebuild.

## Why This Matters for {a}OS

The {a}OS framework needs to accommodate all three agent types while being honest about which ones are production-safe. The governance layer (S6/S7) must enforce maturity-aware policies: allow prompt agents in production, gate workflow agents behind additional review, block hosted agents from regulated workloads until GA + VNet.
