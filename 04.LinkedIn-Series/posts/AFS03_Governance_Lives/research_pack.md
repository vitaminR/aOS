# AFS03 — Research Pack: Where Governance Actually Lives

## Core Thesis

Managed AI platforms are strong at L1-L3 (models, knowledge, execution). They are structurally weak at L5-L7 (observability, governance, experience). What marketing calls "one gap" is actually three separate architectural problems with three different owners, three different interface contracts, and three different failure modes. The {a}OS 7-stratum model makes this visible before teams discover it through production failures.

## Key Facts

### {a}OS 7-Stratum Model

- Seven strata: L1 Models & Infrastructure, L2 Knowledge & Memory, L3 Execution & Interfaces, L4 Orchestration & Decisioning, L5 Observability & Evaluation, L6 Governance & Trust, L7 Experience & Intent
- Evolved from 6-layer model — separated the top "governance" layer into three distinct strata (L5, L6, L7) because they have different owners, contracts, and failure modes
- Named analogy: OSI model for networking (1984) gave teams a shared vocabulary for where network problems live. {a}OS does the same for agentic AI.

### Foundry Coverage by Stratum (from series plan section 5)

| Stratum | Coverage | Key Assets | Key Gaps |
|:---:|:---:|---|---|
| L7 | Partial | Portal, agent publishing, API | Custom UX, intent disambiguation, escalation flows, approval surfaces |
| L6 | Partial | Content Safety, RBAC, Azure Policy, Defender | Approval workflows, governance dashboard, audit aggregation, compliance reporting, cost governance |
| L5 | Partial | Tracing (GA), evaluators (GA), App Insights | **Tracing breaks with private App Insights.** End-to-end audit, custom dashboards |
| L4 | Partial | Workflow agents (preview), prompt agents (GA), Model Router | Production multi-agent, circuit breakers, deterministic routing |
| L3 | Good | Function calling, MCP, Code Interpreter, tool catalog | Tool governance, VNet-incompatible tools |
| L2 | Partial | Agent memory, AI Search, Foundry IQ (preview) | Cross-agent state, memory lifecycle, RAG governance |
| L1 | Strong | Model catalog, fine-tuning, PTU, CMK, Foundry Local | Gov cloud gaps, DR, hybrid compute |

### Why Three Strata, Not One

The old model's single "governance gap" actually decomposes into:

- **L5 Observability:** "We can't see what happened." Owner: platform engineering. Fix: telemetry architecture.
- **L6 Governance:** "Nobody approved this." Owner: security/compliance. Fix: policy enforcement.
- **L7 Experience:** "The user couldn't do what they needed." Owner: product team. Fix: UX design.

Each has a different codebase, different incident playbook, different interface contract. Conflating them means routing incidents to the wrong team.

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | L5-L7 are structurally the enterprise's responsibility | Foundry provides building blocks (Content Safety, tracing, portal) but not the assembled governance/observability/experience layer. No native approval gates, governance dashboards, audit aggregation, compliance reporting, or cost enforcement. |
| R2 | Tracing breaks with private networking | Confirmed: Application Insights tracing fails entirely in private App Insights configurations. Documented in Azure docs. This is L5 — observability — not L6 governance. |
| R3 | Public AI failures map to L5-L7, not L1 | Air Canada (L6 — no approval gate), Zillow (L5 — no circuit breaker), Amazon recruiting (L6 — no governance on training data), Google Gemini (L6 — content safety policy conflict). All publicly blamed on model (L1). |
| R4 | The 7-stratum model reveals problems the 6-layer model hid | Old 6L model: "governance is weak." 7S model: "L5 observability is broken in private networks, L6 governance has no approval pipeline, L7 experience has no escalation flow." Three different fixes, three different teams. |
| R5 | 40+ products mapped across all seven strata | {a}OS Explorer at github.com/vitaminR/aos-explorer contains mappings for Azure AI Foundry, AWS Bedrock, Vertex AI, and other AI products across all seven strata. |

## OSI Model Parallel — Source Material

The OSI model (ISO 7498, 1984) standardized networking into seven layers:

| OSI Layer | {a}OS Stratum | Parallel |
|---|---|---|
| L7 Application | L7 Experience & Intent | User-facing interface |
| L6 Presentation | L6 Governance & Trust | Data/policy formatting and enforcement |
| L5 Session | L5 Observability & Evaluation | Session/state tracking and monitoring |
| L4 Transport | L4 Orchestration & Decisioning | Routing and flow control |
| L3 Network | L3 Execution & Interfaces | Execution/addressing |
| L2 Data Link | L2 Knowledge & Memory | Data framing and access |
| L1 Physical | L1 Models & Infrastructure | Physical/compute foundation |

The parallel is structural, not literal. The value is the shared vocabulary, not a 1:1 mapping.

**Key insight from OSI history:** Before OSI, every networking vendor had proprietary layer definitions. OSI didn't replace them — it gave the industry a common language. {a}OS aims to do the same for agentic AI: not to replace vendor architectures, but to give teams a shared vocabulary for where problems live and which team owns the fix.

## {a}OS Explorer Source Material

- Open source: MIT license
- Repository: github.com/vitaminR/aos-explorer
- Contains: 40+ AI products mapped across all seven strata
- Findings: Coverage patterns are consistent regardless of vendor — strong at L1-L3, weak at L5-L7
- Author positioning: "A tool I built to name the pattern," not a product launch

## Anti-Patterns for Post

- Do NOT over-explain the model. The post is the hook; the Explorer is the depth. Curiosity gap > completeness.
- Do NOT use product-launch language. "I built a reference model" not "I'm excited to announce."
- Do NOT bash vendors. The coverage heatmap is descriptive, not judgmental. The gap is architectural.
- Do NOT use "Part 3 of 12." Post stands alone.
- Do NOT put the engagement prompt in the post body. First comment only.
- The 7-stratum heatmap visual carries most of the explanatory load. Without it, the post is abstract.

## Content Reuse Potential

- Conference talk framework slide
- {a}OS Explorer landing page narrative
- Internal training module: "How to diagnose which stratum failed"
- Reference architecture introduction for consulting engagements
- Whitepaper section 1: "The problem with 'we need governance'"
