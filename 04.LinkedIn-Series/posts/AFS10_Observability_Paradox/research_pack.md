# AFS10 — Research Pack: The Observability Paradox

## Core Thesis

Azure AI Foundry's OpenTelemetry tracing is GA and genuinely useful — but it breaks entirely when Application Insights is deployed with private endpoints. This creates a structural paradox: the platform requires network isolation for production security and requires a non-isolated telemetry path for production observability. The workaround is architectural (peered non-private App Insights with NSG restrictions or Log Analytics export), not a configuration toggle.

## Key Facts

- OpenTelemetry-based tracing for prompt agents is GA (not preview)
- Application Insights integration captures full trace data: prompt, completion, tokens, latency, tool calls
- Built-in evaluation framework is GA: quality, safety, task adherence evaluators
- Evaluators integrate into CI/CD via GitHub Actions — can gate deployments on scores
- Private App Insights (private link scope) blocks Foundry trace ingestion entirely
- The failure mode is silent — no error, no degraded service, just missing traces
- Workflow agent traces are in preview; hosted agent traces are in preview
- Traces for non-prompt agents have additional gaps beyond the network isolation issue
- Workaround: non-private App Insights in a peered spoke VNet with NSG-restricted ingress
- Alternative: export traces to Log Analytics via Data Collection Endpoint (supports private endpoints)

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Tracing is GA for prompt agents | Azure AI Foundry documentation: OpenTelemetry tracing GA announcement for prompt agents |
| R2 | Private App Insights breaks tracing | Confirmed in Azure documentation and series research (section 2.8). Private link scope blocks Foundry agent compute from reaching ingestion endpoint. |
| R3 | Failure is silent | No error returned to agent; traces simply do not arrive. Teams discover this only when they query for traces and find none. |
| R4 | This is a structural paradox | Production deployments require both network isolation (security/compliance) and observability (debugging/audit). Foundry supports both independently but breaks when both are enabled simultaneously. |
| R5 | Workaround is architecture, not config | Requires separate VNet spoke, App Insights without private endpoints, NSG rules, VNet peering. Cannot be solved by a portal toggle or a single CLI command. |
| R6 | Evaluators are genuinely useful | Quality (coherence, fluency, relevance, groundedness), safety (hate, sexual, violence, self-harm, protected material), task adherence (similarity, F1). CI/CD integration via GitHub Actions. |
| R7 | Non-prompt agent traces are preview | Workflow agents and hosted agents have trace support in preview, compounding the observability gap for teams using multiple agent types. |

## Verification Commands

```bash
# Check App Insights network access for ingestion
az monitor app-insights component show \
  --app <app-insights-name> \
  -g <resource-group> \
  --query "publicNetworkAccessForIngestion"
# "Disabled" + VNet-isolated Foundry = broken tracing

# Connectivity test from within VNet
nslookup <app-insights-name>.in.applicationinsights.azure.com
# Private IP = private endpoint active. Public IP = reachable.

# Verify traces arriving (KQL in Log Analytics)
traces
| where timestamp > ago(1h)
| where customDimensions has "gen_ai"
| summarize count() by bin(timestamp, 5m)
# Zero rows + running agents = broken pipeline
```

## Workaround Architecture Summary

```
Hub VNet
├── Azure Firewall + DNS Private Zones
│
├── Spoke: ai-prod
│   ├── Foundry Resource (private endpoints)
│   ├── AI Search (private endpoint)
│   ├── Storage (private endpoint)
│   └── Key Vault (private endpoint)
│
├── Spoke: ai-observability
│   ├── App Insights (NO private endpoints)
│   ├── NSG: ingress from ai-prod subnet ONLY
│   ├── NSG: egress to Log Analytics ONLY
│   └── Log Analytics Workspace
│
└── Peering: ai-prod <-> ai-observability
    (traces flow through backbone, not public internet)
```

## Anti-Patterns to Avoid in Post

- Do not frame this as a complaint or vendor attack — the paradox is structural, the workaround is constructive
- Do not skip the workaround — naming the problem without the fix is lazy. The architecture is the value.
- Do not oversimplify the workaround as "just use a non-private App Insights" — the NSG restrictions and spoke design are essential to the security posture
- Do not imply this affects all observability — evaluators, CI/CD gates, and non-network-isolated tracing all work correctly
- Do not forget the verification — readers must be able to check their own environment with the commands provided
- Do not mention this is "Part 10" or reference the series structure — post must stand alone
- Do not use "simply" or "just" — the workaround is real engineering
