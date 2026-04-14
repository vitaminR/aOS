# AFS05 — Research Pack

## Deep Technical Material

### 1. Azure AI Foundry Network Architecture

Azure AI Foundry uses a hub-and-project architecture where network isolation is configured at the **hub** level and inherited by projects.

**Hub-level managed network:**

- When enabled, a managed VNet is provisioned for the hub
- All compute (including agent runtimes) runs inside this managed VNet
- Outbound access is controlled via outbound rules:
  - **Allow all** — default, no isolation
  - **Allow only approved** — whitelist model, only approved FQDNs/services can be reached
  - **Disabled** — no outbound internet access (most restrictive)

**Private endpoint topology:**

```
Client VNet
  |
  +-- Private Endpoint --> Azure AI Foundry Hub
  |                          |
  |                          +-- Managed VNet (hub-owned)
  |                                |
  |                                +-- Private Endpoint --> Azure OpenAI
  |                                +-- Private Endpoint --> Azure AI Search
  |                                +-- Private Endpoint --> Storage Account
  |                                +-- [MISSING] --> Bing API (public)
  |                                +-- [MISSING] --> SharePoint Graph (public)
```

The gap is visible in the topology: there is no private endpoint path to Bing, WebSearch, or SharePoint Online. These services do not offer private endpoint connectivity for the grounding use case.

### 2. VNet Injection for Agent Compute — Technical Details

Agent compute in Azure AI Foundry runs on Azure Container Apps infrastructure.

**Subnet requirements:**

- Minimum size: /27 (32 addresses)
- Delegation: `Microsoft.App/environments`
- The subnet must be in the same region as the Foundry hub
- NSG rules: Microsoft-managed, additional rules may conflict

**What this means operationally:**

- Network team must pre-provision and delegate the subnet
- IP address planning matters — /27 per environment is non-trivial in enterprise address spaces
- The delegation means the subnet cannot be shared with other Azure services
- Container Apps environment is created automatically by Foundry when VNet injection is configured

**Configuration path:**

```python
# SDK approach
from azure.ai.projects import AIProjectClient

# Hub must be configured with network isolation BEFORE project creation
# VNet injection is configured at hub level, not project level
```

### 3. The Bing Grounding Data Flow

When Bing Grounding is enabled on an agent:

1. User sends a query to the agent (via private endpoint — OK)
2. Agent runtime decides to invoke Bing Grounding tool
3. Agent runtime makes an HTTPS call to `api.bing.microsoft.com` (PUBLIC)
4. Bing returns search results over HTTPS (PUBLIC)
5. Agent incorporates results into response
6. Response returns to user via private endpoint (OK)

Steps 3 and 4 traverse the public internet. The query content — which may include PII, proprietary terms, or confidential business context — leaves the private network boundary.

**Why Microsoft cannot easily fix this:**

- Bing is a consumer/commercial service, not an Azure PaaS resource
- Private endpoints require the target service to support the Private Link platform
- Bing's API infrastructure is separate from Azure's Private Link fabric
- SharePoint Online faces similar constraints via Microsoft Graph

### 4. Hosted Agents — Architecture Constraints

Hosted Agents are the "serverless" agent compute option:

- No infrastructure to manage
- No VNet injection
- Runs on shared Microsoft compute pools
- Cannot be placed in a customer VNet

**Why this matters for the post:**
Hosted Agents are the default experience. When a new user creates an agent in the Foundry portal, they get a Hosted Agent. The path to VNet-isolated agents requires:

1. Switching to Standard Agent compute
2. Configuring VNet injection at the hub level
3. Delegating a subnet
4. Re-deploying agents

This is not a toggle. It is an architecture change.

### 5. Workflow Agents — The Inbound-Only Gap

Workflow Agents support:

- Inbound access via private endpoint (clients can call the agent privately)

Workflow Agents do NOT support:

- Outbound VNet routing (agent's own tool calls may go public)
- Full managed VNet integration

**Implication:** Even if your client-to-agent path is private, the agent-to-tool path may not be. This is a half-isolation that looks complete from the client side but is not complete from the agent side.

### 6. Tracing Gap — Technical Detail

Azure AI Foundry uses Application Insights for agent tracing (OpenTelemetry-based).

**In isolated environments:**

- Application Insights resource can be configured with private endpoint (via Azure Monitor Private Link Scope / AMPLS)
- However, the Foundry managed compute's trace exporter does not route through the managed VNet's private endpoint to Application Insights
- Result: traces either fail silently or route over public internet depending on configuration

**Workaround options:**

1. Use Log Analytics workspace with private link (loses Foundry trace UI)
2. Export via diagnostic settings to a storage account with private endpoint
3. Accept the tracing gap and use alternative observability for isolated workloads

### 7. Azure Policy Remediation — Implementation Detail

**Policy definition to block Bing Grounding:**

The policy targets the connection type on Azure AI Services / Cognitive Services resources. The specific policy approach:

```json
{
  "if": {
    "allOf": [
      {
        "field": "type",
        "equals": "Microsoft.CognitiveServices/accounts/connections"
      },
      {
        "field": "Microsoft.CognitiveServices/accounts/connections/connectionType",
        "in": ["BingGrounding", "WebSearch"]
      }
    ]
  },
  "then": {
    "effect": "Deny"
  }
}
```

**Recommended deployment:**

- Assign at the management group or subscription level
- Apply BEFORE any Foundry hubs/projects are created
- Use `Deny` effect, not `Audit` — audit lets the resource through and just logs it
- Include in your landing zone policy baseline

**CLI to verify current state:**

```bash
# Check if any connections of these types exist
az rest --method GET \
  --url "https://management.azure.com/subscriptions/{sub}/providers/Microsoft.CognitiveServices/accounts?api-version=2024-10-01" \
  --query "value[].{name:name, connections:properties.connections}"

# List all policy assignments on the subscription
az policy assignment list --subscription {sub-id} --query "[].{name:displayName, policy:policyDefinitionId}"
```

### 8. The New Portal vs. Classic Portal

**New Foundry portal** (`ai.azure.com`):

- Modern UI, project-centric navigation
- Does NOT work when the hub has network isolation enabled with restricted outbound
- The portal itself makes calls that are blocked by the managed VNet's outbound rules
- Microsoft has acknowledged this as a known limitation

**Classic portal** (Azure ML Studio at `ml.azure.com`):

- Older UI, workspace-centric navigation
- Works in isolated environments
- Supports most Foundry features through the classic interface

**SDK/CLI alternative:**

```python
# Python SDK works regardless of network isolation
# (runs from your client, connects via private endpoint)
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint="https://<hub-name>.privatelink.api.azureml.ms"
)
```

```bash
# CLI also works via private endpoint
az ml workspace show --name <hub-name> --resource-group <rg>
```

### 9. Verification Methodology — How to Build Your Own Table

Steps to reproduce this analysis:

1. **Create a Foundry hub with managed network isolation** (outbound = allow only approved)
2. **Create a project under the hub**
3. **Deploy an agent with each tool type** and observe:
   - Does the tool function at all?
   - If yes, check NSG flow logs for public IP destinations
   - If no, check agent runtime logs for connection errors
4. **Use Network Watcher** to capture packet traces on the managed VNet
5. **Cross-reference** with Microsoft Learn docs for each tool's stated network requirements
6. **Document with date** — these results change with platform updates

**Recommended cadence:** Re-verify quarterly, or after any major Foundry platform update announcement.

### 10. Related Microsoft Documentation Links

Key docs to cross-reference (titles for search, as URLs change):

- "Configure a managed network for Azure AI Foundry hubs"
- "Azure AI Foundry network isolation overview"
- "Known limitations for Azure AI Agent Service"
- "Configure private endpoints for Azure AI services"
- "Azure Policy built-in definitions for Azure AI services"
- "Azure Container Apps networking — VNet integration"
- "Azure Monitor Private Link Scope (AMPLS)"

### 11. Competitive Context

For background only (not for the post — the post is tool-specific, not comparative):

- AWS Bedrock: Agents run in customer VPC via VPC endpoints. Similar gaps exist with some tool integrations.
- GCP Vertex AI: Uses VPC Service Controls. Broader perimeter model but has its own exceptions list.
- The "exceptions table" concept applies to every cloud AI platform. Azure is not uniquely bad here — it is uniquely underdocumented in one consolidated view.
