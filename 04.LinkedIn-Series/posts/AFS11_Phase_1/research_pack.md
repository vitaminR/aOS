# AFS11 — Research Pack

## Phase 1 Resource Group Taxonomy — Full Detail

| Resource Group | Purpose | Key Resources | Phase 1 Priority |
|---------------|---------|---------------|-------------------|
| ai-networking | Network foundation | Hub VNet, Firewall, Private DNS Zones, Spoke VNets | Week 1-2 |
| ai-prod | Production workloads | Foundry Hub/Project, Storage, AI Search, Cosmos DB, Key Vault, App Insights | Week 4-8 |
| ai-staging | Pre-prod validation | Same as prod (parameter-driven from same IaC) | Week 6-10 |
| ai-dev | Developer iteration | Same resources, relaxed networking, lower SKUs | Week 2-4 |
| ai-governance | Policy and observability | Azure Policy, APIM AI Gateway, Log Analytics, Cost Management | Week 3-6 |
| ai-shared | Cross-environment services | Container Registry, CI/CD service connections | Week 2-4 |

## 90-Day Sequencing — Build Order

### Month 1: Foundation (Weeks 1-4)

**Week 1-2: Identity + Networking**

- Entra ID tenant configuration for AI workloads
- Managed identity provisioning (system-assigned on hubs, user-assigned for cross-cutting)
- RBAC role assignments: Azure AI User as developer default
- API key authentication disabled at hub level
- Hub VNet deployed with address space planning
- Private DNS zones created for: privatelink.api.azureml.ms, privatelink.cognitiveservices.azure.com, privatelink.blob.core.windows.net, privatelink.vaultcore.azure.net
- Spoke VNet for dev environment (relaxed: public endpoints allowed)

**Week 2-4: IaC Scaffolding + Dev Environment**

- Fork azure-ai-foundry/foundry-samples repository
- Deploy 00-basic template to dev resource group
- Parameterize for environment (dev/staging/prod)
- CI/CD pipeline: Bicep lint + what-if + deploy
- Dev Foundry hub operational with one test project
- Container Registry deployed in ai-shared

### Month 2: First Workload (Weeks 5-8)

**Week 5-6: One Model + APIM Gateway**

- Deploy single model (GPT-4o recommended) to dev Foundry project
- Managed endpoint with private endpoint (prod) or public endpoint (dev)
- APIM instance deployed in ai-governance resource group
- APIM policy: token counting, rate limiting, per-subscription-key tracking
- Model inference routed through APIM — no direct endpoint access in prod

**Week 7-8: One Agent + Production Deployment**

- Prompt agent deployed in dev project
- Single model backend, single system prompt, single grounding source
- Evolve IaC templates toward 19-hybrid-private-resources pattern
- Deploy production Foundry hub with full network isolation
- Private endpoints on all AI services in prod
- Azure Policy assignments: block Bing/Web/SharePoint grounding in prod

### Month 3: Operationalize (Weeks 9-12)

**Week 9-10: Staging + Cost Metering**

- Deploy staging environment from same IaC templates (parameter override)
- Validate staging matches prod networking configuration
- Cost Management configured with per-resource-group budgets
- APIM analytics dashboard: token usage per project, cost attribution
- Alert rules: budget threshold warnings at 70%, 90%, 100%

**Week 11-12: Observability + Handoff**

- Log Analytics workspace configured with Foundry diagnostic settings
- Application Insights connected (private endpoint workaround for network-isolated deployments)
- Custom dashboards: model latency, token throughput, error rates, cost trends
- Runbook: "How to onboard a new project to the AI platform"
- Phase 2 planning document drafted

## IaC Template Comparison

### 00-basic (Starting Point)

```
Resources deployed:
- AI Services account
- Machine Learning workspace (hub)
- Machine Learning workspace (project)
- Storage account
- Key Vault
- Application Insights
- Log Analytics workspace

Networking: None (public endpoints)
Identity: System-assigned managed identity on hub
Complexity: Low — good for learning the resource graph
```

### 19-hybrid-private-resources-agent-setup (Target State)

```
Resources deployed:
- All of 00-basic, plus:
- Virtual Network with subnets
- Private endpoints for all services
- Private DNS zones
- Network Security Groups
- Agent runtime configuration
- AI Search (for agent grounding)
- Cosmos DB (for agent state)

Networking: Full private endpoint isolation
Identity: System-assigned + user-assigned managed identities
Complexity: High — production-grade reference
```

### Migration Path: 00 to 19

1. Start with 00-basic deployed to dev environment
2. Add VNet module and private endpoint module incrementally
3. Test private DNS resolution before adding to all services
4. Add AI Search and Cosmos DB when agent grounding is needed
5. Final state: 19-equivalent deployed to prod, 00-equivalent (with identity hardening) to dev

## Azure Policy Assignments for Phase 1

| Policy | Scope | Effect | Purpose |
|--------|-------|--------|---------|
| Deny public network access on AI Services | ai-prod, ai-staging | Deny | Enforce private endpoints |
| Deny public network access on Storage | ai-prod, ai-staging | Deny | Enforce private endpoints |
| Require managed identity on ML workspaces | All RGs | Audit/Deny | Prevent key-based auth |
| Block Bing grounding connection type | ai-prod | Deny | Prevent data exfiltration to Bing |
| Block SharePoint grounding connection type | ai-prod | Deny | Prevent uncontrolled data access |
| Block Web grounding connection type | ai-prod | Deny | Prevent external web calls |
| Require diagnostic settings on AI resources | All RGs | DeployIfNotExists | Ensure observability |
| Allowed VM SKUs (if compute used) | All RGs | Deny | Cost control |

## APIM AI Gateway Configuration

### Token Counting Policy (XML fragment)

```xml
<policies>
  <inbound>
    <set-variable name="prompt-tokens" value="@(context.Request.Body.As<JObject>()["usage"]?["prompt_tokens"]?.ToString() ?? "0")" />
  </inbound>
  <outbound>
    <set-variable name="completion-tokens" value="@(context.Response.Body.As<JObject>()["usage"]?["completion_tokens"]?.ToString() ?? "0")" />
    <set-variable name="total-tokens" value="@(context.Response.Body.As<JObject>()["usage"]?["total_tokens"]?.ToString() ?? "0")" />
    <log-to-eventhub logger-id="token-logger">@{
      return new JObject(
        new JProperty("subscription", context.Subscription.Id),
        new JProperty("product", context.Product.Id),
        new JProperty("total-tokens", context.Variables["total-tokens"]),
        new JProperty("timestamp", DateTime.UtcNow)
      ).ToString();
    }</log-to-eventhub>
  </outbound>
</policies>
```

### Rate Limiting Policy

```xml
<rate-limit-by-key calls="100" renewal-period="60" counter-key="@(context.Subscription.Id)" />
```

## Two Resource Models — Coexistence Plan

### Classic Model (Build on This Today)

- AI Services resource (Microsoft.CognitiveServices/accounts)
- Machine Learning workspace as hub (Microsoft.MachineLearningServices/workspaces kind=hub)
- Machine Learning workspace as project (kind=project)
- Full network isolation support via private endpoints
- Mature, well-documented, production-proven

### New Model (Plan for This)

- Foundry resource (Microsoft.CognitiveServices/accounts with new capabilities)
- Simplified resource graph
- Better portal experience
- Network isolation support still maturing
- Will become the default — plan abstractions that survive the transition

### Coexistence Strategy

1. Build Phase 1 on classic model — it works today for network-isolated production
2. Abstract environment configuration into parameter files, not hardcoded resource types
3. Monitor Microsoft announcements on new model network isolation parity
4. Plan Phase 3 or Phase 4 migration when new model reaches feature parity
5. Estimated coexistence period: 12-18 months from April 2026

## Source References

- Azure AI Foundry reference architecture documentation
- azure-ai-foundry/foundry-samples GitHub repository (Bicep templates)
- Azure APIM AI Gateway documentation
- Azure Policy built-in definitions for Cognitive Services
- Microsoft Learn: Deploy Azure AI Foundry with Bicep
- Microsoft Learn: Azure AI Foundry networking and security
- Series plan section 3.1 (reference architecture)
- Posts AFS01-AFS10 cumulative research (identity, networking, models, agents, cost, observability)
