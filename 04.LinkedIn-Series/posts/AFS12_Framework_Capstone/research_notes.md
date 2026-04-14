# AFS12 — Research Notes

## The Cross-Platform Pattern

The {a}OS 7-stratum model was built from Azure AI Foundry analysis, but the same coverage pattern holds across every major managed AI platform evaluated:

### Azure AI Foundry

| Stratum | Coverage | Detail |
|---|---|---|
| L7 Experience & Intent | Partial | Portal, agent publishing. No custom UX, approval surfaces, escalation design. |
| L6 Governance & Trust | Weak | Content Safety, RBAC, Policy. No approval workflows, audit trail aggregation, compliance reporting. |
| L5 Observability & Evaluation | Weak | Tracing (GA), evaluators. Private network tracing breaks. No custom dashboards, no e2e audit. |
| L4 Orchestration & Decisioning | Partial | Workflow agents (preview). No production multi-agent, no circuit breakers, no APIM integration. |
| L3 Execution & Interfaces | Strong | Function calling, MCP, tools (GA). Tool governance and VNet-incompatible tools remain gaps. |
| L2 Knowledge & Memory | Good | Agent memory, AI Search. No cross-agent state, no memory lifecycle management. |
| L1 Models & Infrastructure | Strong | 11K+ model catalog, fine-tuning, PTU. DR and gov cloud gaps remain. |

### AWS Bedrock

| Stratum | Coverage | Detail |
|---|---|---|
| L7 Experience & Intent | Partial | Console, API endpoints. No custom UX framework, no approval surfaces. |
| L6 Governance & Trust | Weak | Guardrails (I/O filtering only). No workflow-level governance, no cost chargeback, no compliance reporting. |
| L5 Observability & Evaluation | Weak | CloudWatch integration, model invocation logging. No agent-level tracing, no evaluation framework. |
| L4 Orchestration & Decisioning | Partial | Multi-agent collaboration (preview). No deterministic routing, no circuit breakers. |
| L3 Execution & Interfaces | Strong | Action groups (GA), knowledge bases, tool integration. |
| L2 Knowledge & Memory | Good | Knowledge Bases (GA), conversation memory. No cross-agent state. |
| L1 Models & Infrastructure | Strong | 100+ models, fine-tuning, provisioned throughput. |

### Vertex AI

| Stratum | Coverage | Detail |
|---|---|---|
| L7 Experience & Intent | Partial | Vertex AI Studio, API endpoints. No custom UX or approval surfaces. |
| L6 Governance & Trust | Weak | Model monitoring, some bias detection. No workflow governance, no compliance reporting. |
| L5 Observability & Evaluation | Partial | Model monitoring, GenAI evaluation. Better than competitors but still not e2e. |
| L4 Orchestration & Decisioning | Partial | Agent Builder (GA). No production multi-agent coordination. |
| L3 Execution & Interfaces | Strong | Extensions (GA), Function calling, tool use. |
| L2 Knowledge & Memory | Good | RAG Engine (GA), grounding. No cross-agent state. |
| L1 Models & Infrastructure | Strong | Gemini family, model garden, fine-tuning. |

### Internal Platforms (Composite Pattern)

Internal platforms built on top of managed AI services follow the same pattern but often worse at L5-L7 because the team that built the platform was focused on developer experience (L3-L4), not operational governance.

Common internal platform gaps:

- L7: No standardized approval UX — every team builds their own
- L6: Governance is a spreadsheet, not a system
- L5: Observability means "we have logs" — no structured tracing, no evaluation framework
- L4: Orchestration is custom code with no circuit breakers

## Why the Pattern Is Universal

Managed AI platform vendors optimize for:

1. **Developer adoption** (L1-L3) — this is what drives product-led growth
2. **Agent capability** (L3-L4) — this is what demos well
3. **Safety guardrails** (partial L6) — this is what avoids PR disasters

They structurally do not invest in:

1. **Operational observability** (L5) — this is org-specific and hard to productize
2. **Governance enforcement** (L6) — this requires understanding each customer's compliance regime
3. **Experience design** (L7) — this is the customer's product, not the platform's

This is not negligence. It is a rational product boundary. The platform ends where the customization begins. {a}OS names where that boundary sits.

## The "Three Strata, Not One Gap" Insight

Before {a}OS, teams described the problem as "we need governance" or "we need guardrails." This collapses three distinct problems:

1. **L5 — Can I see what happened?** (Observability) — Different owner (platform/SRE team), different tools (tracing, dashboards, alerts), different failure mode (blind spots, not policy violations)
2. **L6 — Was it allowed to happen?** (Governance) — Different owner (security/compliance team), different tools (approval gates, audit trails, policy engines), different failure mode (unauthorized actions, not invisible ones)
3. **L7 — Should it have happened this way?** (Experience) — Different owner (product team), different tools (UX, escalation design, intent routing), different failure mode (bad user experience, not policy or visibility failure)

Naming the strata routes the problem to the right team. That is the operational value of the framework.

## Callback Thread

- **Post 1:** "This is not a feature gap. This is an architectural boundary." — AFS12 proves the boundary is universal.
- **Post 3:** "That gap from Post 1? Now it has coordinates." — AFS12 proves the coordinates work on any map.
- **Post 12 close:** "This started as an Azure series. It ended as a framework." — The arc is complete.
