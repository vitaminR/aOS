# AFS07 — Research Pack: Agent Maturity: What's GA, What's Preview, What Matters

## Core Thesis

Azure AI Foundry has three agent types with materially different production readiness. Only prompt agents are GA with full VNet support. Everything else is preview with constraints that disqualify it from regulated production. Build first value on what's stable.

## Key Facts

- Prompt agents are GA with full VNet support, per-agent Entra identity, and production SLA
- Workflow agents are preview with inbound-only VNet support — outbound calls may route outside the VNet
- Hosted agents are preview with no VNet support — run on Microsoft-managed compute without customer VNet injection
- All three agent types share the same per-agent Entra identity model (managed identity in Entra ID)
- Per-agent identity enables per-agent RBAC scoping and audit trail — architecturally strong
- Publishing agents to Teams/M365 requires public endpoints — conflicts with VNet isolation
- Preview APIs have no SLA and can change without notice — building production on preview means budgeting for rebuild
- The orchestration graph format for workflow agents is not guaranteed stable across preview versions

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Prompt agents are GA + VNet | Azure AI Foundry docs: prompt agents listed as GA. VNet-isolated projects support prompt agent execution. Known exceptions: Bing/WebSearch route publicly. |
| R2 | Workflow agents are preview + partial VNet | Azure AI Foundry docs: workflow agents listed as preview. VNet support is inbound only — the agent can receive requests from VNet, but outbound tool calls may not respect VNet boundaries. |
| R3 | Hosted agents are preview + no VNet | Azure AI Foundry docs: hosted agents listed as preview. Run on Microsoft-managed compute. No customer VNet injection available. |
| R4 | Per-agent Entra identity | Azure AI Foundry docs: each agent gets a managed identity in Entra ID. Agents authenticate to downstream resources as themselves. RBAC can be scoped per-agent. |
| R5 | Teams publishing requires public endpoints | Azure AI Foundry docs: publishing to Teams/M365 Copilot requires the agent endpoint to be publicly reachable. This is by design — Teams architecture requires public endpoint reachability. |
| R6 | Preview API instability is real | General Azure preview terms: preview features are not covered by SLA, may be discontinued, and APIs may change without notice. Author experience: two workflow agent prototypes required rebuild when preview API changed parameter format. |

## Anti-Patterns to Avoid in Post

- Don't frame this as "Azure is bad" — the identity layer and prompt agent maturity are genuinely strong
- Don't imply preview features are useless — they're valuable for prototyping, just not for production bets
- Don't create a false equivalence between the three types — they are at materially different readiness levels
- Don't list every tool and capability — focus on maturity, VNet, and production readiness
- Don't promise a GA timeline for workflow or hosted agents — that's Microsoft's call, not ours
- Don't lecture — the Mentor Architect voice is protective advice, not condescension
