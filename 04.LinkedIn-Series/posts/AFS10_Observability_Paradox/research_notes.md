# AFS10 — Research Notes

## The Observability Paradox — Core Finding

Azure AI Foundry's observability pipeline has a confirmed structural conflict with its own network isolation requirements. This is not a preview limitation or a missing feature. It is two production-grade capabilities that contradict each other when deployed together.

### What Works

**OpenTelemetry tracing (GA for prompt agents):**

- Full trace capture: prompt, completion, token usage, latency, tool calls
- Application Insights integration via OpenTelemetry SDK
- Traces appear in Application Insights transaction search and application map
- Works correctly when App Insights is deployed without private endpoints

**Built-in evaluation framework:**

- Quality evaluators: coherence, fluency, relevance, groundedness
- Safety evaluators: hate/unfairness, sexual, violence, self-harm, protected material
- Task adherence evaluators: similarity, F1 score
- CI/CD integration via GitHub Actions — can gate deployments on evaluation scores
- Continuous evaluation for production monitoring
- Genuinely useful — not a checkbox feature

### What Breaks

**Private Application Insights + Foundry tracing = broken entirely:**

- When App Insights is deployed with private endpoints (private link scope), the ingestion endpoint is only accessible within the private network
- Foundry's tracing pipeline cannot reach the private ingestion endpoint from within the VNet-isolated agent compute
- Result: zero traces arrive. No error, no degraded mode, just silence
- This is confirmed in Microsoft documentation and by field experience
- The failure mode is silent — teams do not discover this until they look for traces and find nothing

### Why This Is a Paradox

Production AI deployments in any security-conscious organization require:

1. **Network isolation** — data must not traverse public internet, private endpoints enforced
2. **Observability** — traces, metrics, and logs must be captured for debugging, audit, and compliance

Azure AI Foundry supports both capabilities independently. It breaks when you enable both simultaneously. The platform that tells you to isolate your network also requires a non-isolated path for its own telemetry.

### Scope of Impact

This affects:

- Any team deploying Foundry with private endpoints on Application Insights
- Any regulated environment (defense, healthcare, finance) where network isolation is mandatory
- Any team that needs trace-level observability for agent debugging or audit
- Most serious production deployments — this is not an edge case

This does NOT affect:

- Development environments without network isolation
- Teams using Application Insights without private endpoints
- Teams that do not need trace-level agent observability (unlikely in production)

## Workaround Architecture

### Option 1: Peered Non-Private App Insights (Recommended)

Deploy Application Insights WITHOUT private endpoints in a dedicated observability spoke VNet:

```
Hub VNet (Azure Firewall, DNS)
├── Spoke: ai-prod (Foundry Resource, private endpoints, VNet isolation)
├── Spoke: ai-observability (App Insights — NO private endpoints)
│   ├── NSG: restrict ingress to ai-prod subnet only
│   ├── NSG: restrict egress to Log Analytics only
│   └── App Insights → Log Analytics workspace
└── VNet peering: ai-prod <-> ai-observability
```

**How it works:**

- Traces flow from Foundry agent compute through VNet peering to the observability spoke
- App Insights ingestion endpoint is reachable because it is not behind a private endpoint
- NSGs restrict who can send data to this App Insights instance — only the production Foundry subnet
- Data still stays within Azure backbone — does not traverse public internet
- Log Analytics workspace provides long-term retention and cross-query capability

**Trade-offs:**

- App Insights ingestion endpoint is technically public (not behind private link)
- NSG restriction limits exposure but does not eliminate it at the endpoint level
- Acceptable for most production environments; may require additional justification for the most restrictive compliance regimes (IL5+, air-gapped)

### Option 2: Direct Log Analytics Export

Skip App Insights for Foundry traces entirely. Configure OpenTelemetry exporters to send directly to a Log Analytics workspace via the Data Collection Endpoint:

- Data Collection Endpoint supports private endpoints
- Custom OpenTelemetry exporter configuration required
- Loses some App Insights-native features (application map, smart detection)
- Retains raw trace data for querying and audit

**Trade-offs:**

- More custom engineering required
- Loses App Insights UX features
- Fully compatible with private networking
- Better for teams that already have Log Analytics as their primary observability sink

### Option 3: Hybrid — App Insights for Dev, Log Analytics for Prod

- Use standard (non-private) App Insights in dev/staging for full developer experience
- Use Log Analytics with private Data Collection Endpoint in production for compliance
- Accept reduced UX in prod in exchange for full network isolation

## Verification Methodology

### Check App Insights Network Configuration

```bash
# Check whether App Insights ingestion is publicly accessible
az monitor app-insights component show \
  --app <app-insights-name> \
  -g <resource-group> \
  --query "publicNetworkAccessForIngestion"

# Expected: "Enabled" for the workaround (non-private App Insights)
# If "Disabled" — tracing from VNet-isolated Foundry will fail silently
```

### Connectivity Test from Agent Compute

```bash
# From within the VNet (e.g., a jumpbox or test VM in the same subnet):
# Test connectivity to App Insights ingestion endpoint
nslookup <app-insights-name>.in.applicationinsights.azure.com

# If private endpoint is configured, this resolves to a private IP
# If no private endpoint, this resolves to a public IP (reachable via peering)

# Test actual ingestion connectivity
curl -I https://<region>.in.applicationinsights.azure.com/v2/track
# 200 or 307 = reachable. Timeout = blocked.
```

### Verify Traces Are Actually Arriving

```kusto
// Run in Log Analytics workspace connected to App Insights
// Check for Foundry agent traces in the last hour
traces
| where timestamp > ago(1h)
| where customDimensions has "gen_ai"
| summarize count() by bin(timestamp, 5m)
```

If this returns zero rows and your agents are running, your trace pipeline is broken.

## Trace Coverage by Agent Type

| Agent Type | Tracing Status | Notes |
|---|---|---|
| Prompt Agents | GA | Full OpenTelemetry traces, App Insights integration |
| Workflow Agents | Preview | Traces in preview, limited coverage |
| Hosted Agents | Preview | Traces in preview, no VNet support compounds the issue |

The observability gap is worst for prompt agents in private networks — the one agent type that is GA and production-ready is also the one most likely to be deployed in isolated environments.

## {a}OS L5 Connection

This post is a concrete demonstration of why L5 (Observability & Evaluation) is a separate stratum in the {a}OS model. The platform provides tracing and evaluation tools (partial L5 coverage), but the network architecture required for production deployment (L1 infrastructure decision) breaks the observability pipeline. The conflict spans two strata — which is precisely why observability must be planned as its own architectural layer, not assumed as a platform feature.

## Source References

- Azure AI Foundry network isolation documentation (confirmed gaps)
- Application Insights private link documentation
- OpenTelemetry integration for Azure AI Foundry (GA announcement)
- Series research: `c:\Users\nymil\Codepro\6.aOS\03.Research\azure-ai-foundry-enterprise-defense.md` section 2.8
- Series plan: section 3.2 key decision #5 (architect observability workaround)
