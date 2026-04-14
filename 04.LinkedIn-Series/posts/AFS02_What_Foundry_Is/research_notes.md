# AFS02 — Research Notes

## What Azure AI Foundry Actually Bundles

Azure AI Foundry is Microsoft's unified PaaS for AI. It bundles six components under one resource:

### 1. Foundry Models (Model Catalog)

- 11,000+ models in the catalog
- Realistically ~50-100 Azure-hosted models that matter for production use
- The rest is community/marketplace catalog padding
- Fine-tuning support (GA)
- Deployment types: PTU (provisioned throughput), on-demand, serverless

### 2. Foundry Agent Service

- Prompt agents (GA) — single-agent, tool-using agents. Production-ready.
- Workflow agents (preview) — multi-step orchestration. Partial VNet support (inbound only).
- Hosted agents (preview) — container-based. No VNet support at all.
- Agent identity via Entra managed identities (strong feature)
- Publishing to Teams/M365/BizChat (requires public endpoints)

### 3. Foundry IQ

- Enterprise RAG engine (preview)
- Not production-ready as of research date
- Intended to simplify retrieval-augmented generation
- Competes with/complements Azure AI Search

### 4. Content Safety

- Prompt shields (GA)
- Groundedness detection (GA)
- Protected material detection (GA)
- This is content filtering, not governance — important distinction for Post 3

### 5. Foundry Tools

- Speech (GA)
- Vision (GA)
- Language (GA)
- Document Intelligence (GA)
- These are mature Azure AI Services repackaged under the Foundry umbrella

### 6. Control Plane

- RBAC with four Foundry-specific roles
- Networking (private endpoints, VNet injection)
- Encryption (CMK support)
- Monitoring (Application Insights, OpenTelemetry)

## The Rebrand Is Structural, Not Cosmetic

### What Changed

The rebrand from "Azure AI Studio" to "Azure AI Foundry" (and reportedly toward "Microsoft Foundry") reflects a fundamental resource model change:

| Dimension | Classic | New |
|---|---|---|
| Resource provider | `Microsoft.MachineLearningServices` | `Microsoft.CognitiveServices` |
| Topology | Hub → Projects | Foundry Resource → Projects |
| Management paradigm | Azure ML workspace patterns | Cognitive Services account patterns |
| Portal | Foundry (classic) at ai.azure.com | Foundry (new) — toggle visible in portal |
| Network isolation | More mature, more tested | Still maturing, some features unsupported |
| Microsoft investment | Maintenance mode | Active investment |

### Why This Matters

1. **Two models coexist.** Teams starting today must choose. The portal has a toggle between classic and new views.
2. **Classic has more mature network isolation.** Teams needing VNet isolation today should start with classic.
3. **New is where Microsoft invests.** All new features land on the new model first. Classic gets maintenance.
4. **Starting wrong creates migration debt.** Moving from classic to new is not a toggle — it is a resource migration.
5. **The resource provider change is fundamental.** `Microsoft.MachineLearningServices` vs `Microsoft.CognitiveServices` means different ARM APIs, different Bicep templates, different RBAC surface areas.

### Verification Command

```bash
az provider show -n Microsoft.CognitiveServices --query "resourceTypes[?resourceType=='accounts'].locations" -o table
```

This shows which regions support the new Foundry resource model. If your resources are under `Microsoft.MachineLearningServices`, you are on classic.

Additional check:

```bash
az resource list --resource-type "Microsoft.CognitiveServices/accounts" -o table
az resource list --resource-type "Microsoft.MachineLearningServices/workspaces" -o table
```

Whichever returns your AI resources tells you which model you are on.

## Red-Team Note: "Microsoft Foundry" Rebrand

The series plan references a rebrand to "Microsoft Foundry" in 2026. This must be verified against the live portal before publishing.

- If confirmed: Use "Microsoft Foundry" as the current name, note "Azure AI Foundry" as the previous name.
- If NOT confirmed: Use "Azure AI Foundry" throughout. Do not speculate on unreleased rebrands.
- The post should work regardless of which name is current — the structural content (two resource models, resource provider change) is the same either way.

## Portal Reality

- Foundry classic: ai.azure.com (Azure AI Studio legacy URL, redirects to Foundry classic)
- Foundry new: accessible via a toggle in the Azure portal
- The new portal does NOT support network-isolated setup workflows — must use classic portal, Azure CLI, or SDK for VNet-isolated deployments
- This is a confirmed gap, not a temporary limitation — the portal is designed for the common path, not the secure path

## Key Architectural Decision: Which Model to Start With

| Scenario | Recommendation |
|---|---|
| Greenfield, no VNet requirement | New model |
| Greenfield, VNet required | Classic model, plan migration |
| Existing Azure ML workloads | Classic model (already on it) |
| Evaluating only, no production yet | New model (where features land) |
| Gov cloud | Classic model (new model not documented for Gov) |

This decision must be made on day one. It is not easily reversible.
