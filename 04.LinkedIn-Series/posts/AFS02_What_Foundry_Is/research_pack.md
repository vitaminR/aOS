# AFS02 — Research Pack: What Azure AI Foundry Actually Is (and Isn't)

## Core Thesis

Azure AI Foundry is not a marketing rebrand. It is a structural change to the resource model, the resource provider, and the management paradigm. Two resource models coexist. Starting on the wrong one creates migration debt. The post teaches what Foundry bundles, why the rebrand matters architecturally, and how to verify which model you are on.

## Key Facts

### What Foundry Bundles (from series plan section 2.1)

- **Foundry Models:** 11,000+ model catalog. Realistically ~50-100 Azure-hosted models matter. Fine-tuning GA. PTU, on-demand, serverless deployments.
- **Foundry Agent Service:** Prompt agents (GA), workflow agents (preview), hosted agents (preview). Agent identity via Entra.
- **Foundry IQ:** Enterprise RAG engine (preview). Not production-ready.
- **Content Safety:** Prompt shields, groundedness detection, protected material detection (all GA). This is content filtering, not governance.
- **Foundry Tools:** Speech, Vision, Language, Document Intelligence (all GA). Mature Azure AI Services repackaged.
- **Control Plane:** RBAC (four Foundry-specific roles), networking (PE, VNet injection), encryption (CMK), monitoring (App Insights, OpenTelemetry).

### The Resource Model Change (from series plan section 2.2)

| Dimension | Classic (Maintenance Mode) | New (Active Investment) |
|---|---|---|
| Resource provider | `Microsoft.MachineLearningServices` | `Microsoft.CognitiveServices` |
| Topology | Hub → Projects | Foundry Resource → Projects |
| Management | Azure ML workspace patterns | Cognitive Services account patterns |
| Portal | Foundry (classic) at ai.azure.com | Foundry (new) — toggle in portal |
| Network isolation | More mature | Still maturing |
| Investment | Maintenance mode | Active |

### Why Two Models Coexist

- Microsoft did not deprecate the classic model because enterprise customers have production workloads on it
- The new model is built on `Microsoft.CognitiveServices` — a fundamentally different ARM surface area
- Migration from classic to new is not a portal toggle — it is a resource migration with new Bicep templates, different RBAC scopes, and potentially different networking configurations
- The classic model's more mature network isolation makes it the safer choice for security-conscious teams today

### Portal and Tooling

- Classic portal: ai.azure.com
- New portal: Azure portal with Foundry toggle
- New portal does NOT support network-isolated setup — must use classic portal, CLI, or SDK
- Deploy via Bicep/CLI recommended over portal for any production environment (series plan section 3.2)

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Two resource models coexist | Classic uses `Microsoft.MachineLearningServices`; New uses `Microsoft.CognitiveServices`. Both are active in Azure portal. Toggling between them is visible in the portal UI. |
| R2 | Rebrand is structural | Resource provider changed. ARM API surface different. Bicep templates different. RBAC scope different. This is not a name change on the same backend. |
| R3 | Classic has more mature isolation | Network isolation documentation references classic model specifically. New model features that break in VNet are documented in Azure docs. Series plan section 2.4. |
| R4 | New model is where investment goes | Microsoft documentation explicitly positions the new Foundry resource model as the forward-looking path. Classic is "maintenance mode" (no new features). |
| R5 | Starting wrong = migration debt | Moving from `Microsoft.MachineLearningServices` to `Microsoft.CognitiveServices` requires new resource creation, data migration, and potentially new networking configuration. Not a toggle. |
| R6 | 11,000+ models is catalog padding | Catalog includes community, marketplace, and third-party models. Azure-hosted models with SLA-backed inference are ~50-100. The number is technically accurate but operationally misleading. |

## Verification Methodology

Readers can check their own resource model:

```bash
# Check if your resources are on the new model
az resource list --resource-type "Microsoft.CognitiveServices/accounts" -o table

# Check if your resources are on the classic model
az resource list --resource-type "Microsoft.MachineLearningServices/workspaces" -o table

# Check CognitiveServices provider registration and regions
az provider show -n Microsoft.CognitiveServices --query "resourceTypes[?resourceType=='accounts'].locations" -o table
```

## Red-Team Notes

1. **"Microsoft Foundry" rebrand:** Series plan section 2.1 references "Azure AI Foundry (rebranded to 'Microsoft Foundry' in 2026)." This MUST be verified against the live portal before publishing. If not confirmed, use "Azure AI Foundry" throughout. The structural content is valid regardless of naming.

2. **"11,000+ models":** Technically accurate but operationally misleading. Frame as "11,000+ in the catalog — realistically 50-100 Azure-hosted models matter for production." Do not dismiss the number; contextualize it.

3. **Classic deprecation timeline:** Not publicly committed. Do not predict deprecation dates. Frame as "maintenance mode" per current documentation.

4. **Gov cloud resource model:** The new Foundry resource model is not documented for Azure Government. Gov documentation only references the classic portal. This is a risk for regulated teams and should be mentioned if space permits, but the primary audience for this post is commercial Azure.

## Anti-Patterns for Post

- Do NOT turn this into a feature list. Every feature mentioned must serve the "two models" or "structural rebrand" narrative.
- Do NOT use "exciting" or "powerful" marketing language. The voice is tired architect, not product evangelist.
- Do NOT mention {a}OS. That is Post 3.
- Do NOT use "Part 2 of 12" or any series meta-language.
- Do NOT bash Microsoft. The two-model reality is a legitimate engineering trade-off, not incompetence.
- The post should be useful to someone who reads it standalone, without Post 1.
