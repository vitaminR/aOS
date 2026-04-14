# AFS11 — Research Notes

## Key Findings

### Phase 1 Scope — The Six Essentials

The minimum viable AI platform requires exactly six capabilities deployed in sequence. Every team that ships value in under 90 days shares this same skeleton. Teams that try to ship more than six things in Phase 1 consistently ship zero.

1. **Identity** — Entra ID + managed identities + RBAC at project scope + API keys disabled. This is prerequisite infrastructure, not a feature. Everything downstream depends on identity working correctly.

2. **Networking** — Hub-spoke VNet topology with private endpoints on all AI services. DNS zones for private link resolution. Dev environment with relaxed networking for developer velocity. Prod locked from day one.

3. **One model** — A single model deployed behind a managed endpoint. Not a model catalog. The purpose is to prove the deployment pipeline works end-to-end, not to offer choice.

4. **One agent** — A prompt agent (not multi-agent). Single model, single system prompt, single grounding source. Proves the agent runtime and observability pipeline before complexity is added.

5. **Cost metering** — APIM as AI Gateway for token tracking, per-project cost attribution, and rate limiting. Budget visibility must exist before Phase 2 funding conversations happen.

6. **Infrastructure as Code** — Bicep or Terraform, deployed via CLI. Not portal clicks. Fork foundry-samples, do not write from scratch.

### Reference Architecture — Resource Group Taxonomy

```
Azure Subscription
├── RG: ai-networking
│   ├── Hub VNet
│   ├── Azure Firewall
│   ├── Private DNS Zones
│   └── Spoke VNets (per environment)
├── RG: ai-prod
│   ├── Foundry Hub + Project(s)
│   ├── Storage Account
│   ├── AI Search
│   ├── Cosmos DB
│   ├── Key Vault
│   └── Application Insights
├── RG: ai-staging
│   └── [same pattern as prod]
├── RG: ai-dev
│   └── [relaxed networking, same resources]
├── RG: ai-governance
│   ├── Azure Policy assignments
│   ├── APIM AI Gateway
│   ├── Log Analytics workspace
│   └── Cost Management configuration
└── RG: ai-shared
    ├── Container Registry
    └── CI/CD service connections
```

### Key Architecture Decisions

1. **Separate Foundry resources per environment.** One hub for dev, one for staging, one for prod. Shared hubs across environments create blast radius and compliance problems.

2. **Classic resource model for production.** The new Foundry resource model does not yet support full network isolation. Use the classic model (AI Services + ML workspace) for production. Plan for migration when the new model catches up.

3. **Deploy via Bicep/CLI, not portal.** Portal deployments create configuration drift within days. Teams that start with portal "to get going fast" spend weeks reconciling state later.

4. **APIM as AI Gateway from day one.** Retrofitting cost metering after models are in production is significantly harder than deploying APIM first. Token tracking and rate limiting are governance prerequisites, not optimization features.

5. **Block Bing/Web/SharePoint grounding in prod via Azure Policy.** These grounding sources send data to external services. Block them by default, allow them explicitly per project with justification.

6. **Start with prompt agents only.** Multi-agent orchestration, tool chains, and complex workflows are Phase 2. Phase 1 proves the platform. Phase 2 proves the patterns.

7. **Plan for two resource models.** The classic model (AI Services resource + ML workspace) and the new model (Foundry resource) will coexist for 12-18 months. Build abstractions that survive the transition.

### IaC Templates — Microsoft Foundry Samples

Microsoft maintains Bicep templates in the `azure-ai-foundry/foundry-samples` repository:

- **00-basic** — Minimal Foundry deployment. Hub, project, AI Services, storage. No networking. Good starting scaffold to understand the resource structure.

- **19-hybrid-private-resources-agent-setup** — Production-grade. Private endpoints, VNet integration, DNS zones, agent runtime configuration. This is the target state for a network-isolated production deployment.

**Recommendation:** Fork the repository. Start with 00-basic to understand the dependencies. Evolve toward 19 for production. Do not write Bicep from scratch — the resource dependencies between Foundry hub, AI Services, storage, and Key Vault are non-obvious.

### Environment Separation Strategy

- **Dev:** Relaxed networking (no private endpoints required). Developers can access Foundry portal and endpoints directly. Lower-tier SKUs. Faster iteration.

- **Staging:** Production-equivalent networking. Private endpoints enabled. Used for integration testing and security validation. Should be deployable from the same IaC templates as prod with parameter overrides.

- **Prod:** Full network isolation. Private endpoints on every service. No public endpoints. Azure Policy enforced. APIM as sole ingress for model inference. Separate Foundry hub from dev/staging.

### Common Phase 1 Failures

- **Scope inflation:** Teams add "just one more thing" until Phase 1 is a 6-month program
- **Portal-first deployment:** Creates drift that IaC must later reconcile
- **Shared hub across environments:** Dev experimentation impacts prod stability
- **No cost metering:** Budget conversations happen without data, leading to cuts
- **Multi-agent before single-agent:** Debugging orchestration before the base platform works
- **RAG before basic inference:** Adding data pipelines before the model deployment path is proven

## Patterns Observed

- Teams of 5 and teams of 50 need the same Phase 1 scope. The difference is parallelism, not breadth.
- The most successful AI platform teams treat Phase 1 as a "prove the plumbing" exercise, not a feature showcase.
- Cost metering deployed in Phase 1 consistently correlates with Phase 2 getting funded.
- Teams that deploy via portal in Phase 1 spend 2-4 weeks in Phase 2 migrating to IaC.

## Supporting Examples

- Common anti-pattern: 31 Phase 1 line items, model catalog, RAG, multi-agent, custom eval — ships nothing in 90 days
- Common anti-pattern: one Foundry hub shared across dev/staging/prod with public endpoints
- Correct pattern: six scoped items, Bicep from day one, APIM gateway for cost visibility
- Correct pattern: dev with relaxed networking for velocity, prod locked down from the start
