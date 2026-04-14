# AFS05 — Research Notes

## Key Findings

### 1. VNet Isolation — What Microsoft Documents vs. What Actually Works

**Claim:** Azure AI Foundry supports "managed network isolation" for projects and hubs.

**Reality:** The managed network isolation feature exists and works for a subset of tools. The documentation describes the architecture correctly but the gap is that many Foundry features are simply incompatible with isolated mode. This is documented across multiple pages, not consolidated in one place.

**Source pattern:** Microsoft Learn docs spread this across:

- "Configure managed network isolation" (hub-level)
- Individual tool pages (each mentions its own network limitations in a note or warning box)
- "Known limitations" sections buried in feature-specific docs

### 2. Tools That Work Under Isolation

| Tool/Feature | Status | Mechanism |
|---|---|---|
| Private Endpoints (inbound) | Works | Standard Azure PaaS private endpoint pattern |
| VNet Injection (agent compute) | Works | Requires /27+ subnet delegated to `Microsoft.App/environments` |
| Azure AI Search | Works | Via private endpoint on the Search resource |
| Code Interpreter | Works | Runs on Microsoft backbone, does not egress to public internet |
| Function Calling | Works | Executes within the managed compute boundary |

**Key detail on VNet injection:** The subnet delegation requirement (`Microsoft.App/environments`) means the agent compute runs on Azure Container Apps infrastructure. The /27 minimum means 32 IP addresses reserved. This is a non-trivial networking commitment that needs to be planned with the network team.

### 3. Tools That Break Under Isolation

| Tool/Feature | Status | Notes |
|---|---|---|
| File Search | Broken | Cannot access file storage through private network paths |
| OpenAPI Tool | Broken | Makes external HTTP calls that cannot be routed through VNet |
| Azure Functions Tool | Broken | Function invocation does not traverse private network |
| Browser Automation | Broken | Requires public internet access by design |
| Computer Use | Broken | Similar to Browser Automation — needs external access |
| Agent-to-Agent (A2A) | Broken | Inter-agent communication not VNet-aware |
| Image Generation | Broken | DALL-E / image model endpoints not available via private endpoint |
| Logic Apps | Broken | Logic Apps connector architecture not compatible with managed VNet |

### 4. Hosted Agents vs. Standard Agents

**Hosted Agents** have zero VNet support. They run on shared Microsoft infrastructure with no network injection option. This is the most common agent deployment model that new users encounter, making it a significant gap.

**Workflow Agents** support inbound private endpoint access but cannot make outbound calls through a VNet. This means they can receive requests privately but any tool calls they make may route publicly.

**Standard Agent compute** with VNet injection is the only model that provides meaningful network isolation for the agent runtime itself.

### 5. The Public Internet Problem — Bing, WebSearch, SharePoint

This is the most consequential finding. Even when:

- The hub has managed network isolation enabled
- Private endpoints are configured
- Outbound rules are set to "Allow only approved"

The following grounding tools route queries over public internet:

- **Bing Grounding** — queries go to Bing's public API
- **Web Search** — same path as Bing Grounding
- **SharePoint Grounding** — connects to SharePoint Online via public Microsoft Graph endpoints

**Why this matters:** In regulated environments (banking, healthcare, government), the assumption is that "VNet isolation" means all traffic stays private. A data query going to Bing's public endpoint — even if the response comes back — represents a data exfiltration path that compliance teams will flag.

### 6. Foundry Portal Limitation

The new Azure AI Foundry portal (`ai.azure.com`) does not work in fully isolated environments. Teams must use:

- The classic Azure ML Studio portal
- The Azure AI Foundry SDK (Python)
- Azure CLI (`az ml` commands)

This is a significant operational friction point. Teams adopting Foundry in isolated environments lose the primary management UI.

### 7. Tracing / Application Insights

Private Application Insights is not supported for agent tracing in isolated Foundry environments. This means:

- You can run agents in a VNet
- But you cannot observe them without tracing data leaving the private network
- Workaround: export traces to a private Log Analytics workspace via diagnostic settings, but this loses the Foundry-native tracing UI

### 8. Mitigation — Azure Policy

Azure Policy can be used to deny specific tool types at the resource level:

- Deny Bing Grounding connection type
- Deny WebSearch connection type
- This should be applied at the subscription or management group level before any Foundry projects are created
- Policy effect: `Deny` on resource configurations that include these connection types

CLI verification approach:

```bash
# List Cognitive Services accounts (Foundry uses these)
az resource list --resource-type Microsoft.CognitiveServices/accounts

# Check network rules on a specific resource
az cognitiveservices account show --name <name> --resource-group <rg> --query networkRuleSet

# List policy assignments
az policy assignment list --scope /subscriptions/<sub-id>
```

## Confidence Assessment

- **High confidence:** The three-category breakdown (works/broken/public) is accurate as of research date
- **Medium confidence:** Specific tool behavior may change with monthly Azure updates. File Search and Hosted Agents are the most likely to gain VNet support in near-term updates.
- **Perishability:** This table has a ~3-month shelf life before needing re-verification. The post includes "last verified" framing to address this.
- **Verification method:** Cross-referenced Microsoft Learn docs, Azure CLI output from test deployments, and community reports (Microsoft Q&A, GitHub issues on azure-ai-foundry repos)
