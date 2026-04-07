# Azure AI Foundry: Enterprise & Defense Contractor Deployment Research

> **Research Date:** 2026-04-06
> **Sources:** Microsoft Learn documentation, Azure product pages, Azure Government documentation
> **Scope:** Architecture, security, compliance, networking, governance, operational reality

---

## Table of Contents

1. [Architecture and Core Services](#1-architecture-and-core-services)
2. [Identity and Access](#2-identity-and-access)
3. [Private Networking](#3-private-networking)
4. [Model Hosting and Access Strategy](#4-model-hosting-and-access-strategy)
5. [Azure OpenAI Integration](#5-azure-openai-integration)
6. [Governance and Security](#6-governance-and-security)
7. [Agent Orchestration](#7-agent-orchestration)
8. [Observability](#8-observability)
9. [Cost Controls](#9-cost-controls)
10. [Data Access and RAG](#10-data-access-and-rag)
11. [Environment Separation](#11-environment-separation)
12. [Compliance (FedRAMP / IL4 / IL5 / CMMC / ITAR)](#12-compliance)
13. [What Foundry Does NOT Do](#13-what-foundry-does-not-do)
14. [Hub and Project Model](#14-hub-and-project-model)
15. [Deployment and CI/CD](#15-deployment-and-cicd)

---

## 1. Architecture and Core Services

### What Is Microsoft Foundry?

Microsoft Foundry (formerly Azure AI Foundry, formerly Azure AI Studio) is a **unified Azure PaaS** for enterprise AI operations, model hosting, agent building, and application development. It consolidates what were previously separate Azure AI services into a single management plane.

**Marketing positioning:** "The AI app and agent factory." Used by developers at 80,000+ enterprises, 80% of Fortune 500.

### Evolution / Rebrand Timeline

| Dimension | Previous | Current (2026) |
|-----------|----------|-----------------|
| Brand | Azure AI Studio -> Azure AI Foundry | **Microsoft Foundry** |
| Brand | Azure AI Services | **Foundry Tools** |
| Portal | Foundry (classic) at ai.azure.com | **Foundry (new)** at ai.azure.com (toggle) |
| Agent API | Assistants API (Agents v0.5/v1) | **Responses API (Agents v2)** |
| API versioning | Monthly `api-version` params | **v1 stable routes** (`/openai/v1/`) |
| Resource model | Hub + Azure OpenAI + Azure AI Services | **Foundry resource** (single, with projects) |
| SDKs | Multiple packages (`azure-ai-inference`, `azure-ai-generative`, `azure-ai-ml`, `AzureOpenAI()`) against 5+ endpoints | **Unified project client** (`azure-ai-projects` 2.x) + `OpenAI()` against one project endpoint |
| Terminology | Threads, Messages, Runs, Assistants | Conversations, Items, Responses, Agent Versions |

**CRITICAL FOR DEFENSE CONTRACTORS:** The rebrand is NOT just cosmetic. The underlying resource model changed from Hub+Project (classic, `Microsoft.MachineLearningServices`) to Foundry resource+Project (new, `Microsoft.CognitiveServices`). Both still exist in parallel. The classic hub-based model is in maintenance mode; new investment goes to the Foundry resource model.

### Core Components (Current)

| Component | What It Does | Status |
|-----------|-------------|--------|
| **Foundry Models** | 11,000+ model catalog (OpenAI, Meta, Mistral, DeepSeek, xAI, Cohere, etc.) | GA |
| **Foundry Agent Service** | Build, deploy, scale AI agents with tool calling | GA (some sub-features preview) |
| **Foundry IQ** | Enterprise RAG engine (evolution of Azure AI Search integration) | Preview |
| **Foundry Tools** | Pre-built AI capabilities: Speech, Vision, Language, Document Intelligence, Content Understanding, Translator | GA |
| **Foundry Control Plane** | Org-wide observability, governance, security | GA |
| **Foundry Local** | On-device/edge model execution | GA |
| **Content Safety** | Harmful content detection, prompt shields, groundedness | GA |

### Azure Resource Providers

| Resource Provider | Purpose |
|-------------------|---------|
| `Microsoft.CognitiveServices` | Foundry resources, Azure OpenAI, Speech, Vision -- the NEW model |
| `Microsoft.MachineLearningServices` | Azure ML workspaces, classic hub-based projects -- LEGACY |
| `Microsoft.Search` | Azure AI Search |

**Operational reality:** The Foundry resource is a `Microsoft.CognitiveServices/account` with `kind: AIServices`. Projects are sub-resources (`Microsoft.CognitiveServices/account/project`). This is the same provider namespace as Azure OpenAI, which means management APIs, RBAC actions, networking, and Azure Policy behavior align across related AI resources.

---

## 2. Identity and Access

### Entra ID Integration

- **Recommended:** Microsoft Entra ID (formerly Azure AD) authentication for all access
- **Alternative:** API key-based auth is supported but provides full access without role restrictions -- NOT recommended for enterprise/defense
- Key-based auth grants blanket access; Entra ID enables granular RBAC

### Built-in RBAC Roles

| Role | Create Projects | Create Accounts | Build (Data Actions) | Role Assignments | Reader | Manage Models |
|------|:-:|:-:|:-:|:-:|:-:|:-:|
| **Azure AI User** | | | Yes | | Yes | |
| **Azure AI Project Manager** | | | Yes | Yes (AI User only) | Yes | |
| **Azure AI Account Owner** | Yes | Yes | | Yes (AI User only) | Yes | Yes |
| **Azure AI Owner** | Yes | Yes | Yes | Yes (any) | Yes | Yes |
| **Azure Owner** (generic) | Yes | Yes | | Yes (any) | Yes | Yes |
| **Azure Contributor** (generic) | Yes | Yes | | | Yes | Yes |
| **Azure Reader** (generic) | | | | | Yes | |

**Key insight:** `Azure AI User` is the least-privilege role for developers. `Azure AI Owner` is a highly privileged "self-serve" role intended for digital natives, NOT for locked-down defense environments.

### Scope Hierarchy

Roles can be assigned at:
1. **Subscription** scope
2. **Resource group** scope
3. **Foundry resource** (top-level) scope
4. **Foundry project** scope

### Managed Identities

- **System-assigned managed identity** is enabled by default on both Foundry resources and projects
- **User-assigned managed identity** is supported (requires `Cognitive Services Contributor` role)
- Project managed identities need `Azure AI User` at the Foundry resource scope
- Managed identities can be used for secure automation and service-to-service access

### Service Principals

- Fully supported for automation scenarios
- Used with Azure CLI, SDKs, and CI/CD pipelines
- `DefaultAzureCredential` chain handles authentication automatically

### Enterprise RBAC Pattern (Recommended)

| Persona | Role | Scope |
|---------|------|-------|
| IT Admin | Owner | Subscription |
| Manager | Azure AI Account Owner | Foundry resource |
| Team Lead | Azure AI Project Manager | Foundry resource |
| Developer | Azure AI User | Foundry project + Reader on Foundry resource |

### Custom Roles

Supported. Custom roles can use granular `dataActions` to restrict access to specific capabilities (e.g., only allow building agents):

```json
{
  "dataActions": ["Microsoft.CognitiveServices/accounts/AIServices/agents/*"],
  "notDataActions": []
}
```

### Limitations

- **Fine-tuning** requires both data plane AND control plane permissions -- only `Azure AI Owner` has both out-of-box, or combine `Azure AI User` + `Azure AI Account Owner`
- Viewing/purging deleted accounts requires `Contributor` at subscription scope
- Role assignments are NOT auto-applied when deploying via SDK/CLI (only portal auto-assigns)

---

## 3. Private Networking

### Three Areas of Network Isolation

1. **Inbound access** to the Foundry resource (e.g., developers accessing the portal/API)
2. **Outbound access** from the Foundry resource to other Azure services
3. **Outbound access** from the Agent client to dependencies (data sources, Azure PaaS, internet)

### Private Endpoints (Inbound)

- Private endpoints supported for Foundry resources
- **Public Network Access (PNA) flag** controls inbound access: `Disabled`, `Enabled`, or `Enabled from selected IP addresses`
- Private endpoint must be in the **same region and subscription** as the virtual network
- Connection must be in **Approved** state to send traffic
- Do NOT use the `172.17.0.0/16` range (reserved by Docker bridge)

### VNet Integration / Network Injection (Outbound)

- Uses **VNet injection** (container injection) for Agent Service and Evaluations
- Agent client is injected into a customer-managed virtual network subnet
- Requires a subnet delegated to `Microsoft.App/environments` with size **/27 or larger**
- **Prerequisite:** Must bring your own Storage, AI Search, AND Cosmos DB (Standard Agent setup)
- VNet injection is ONLY available when public network access is set to `Disabled`

### DNS Requirements

- Azure creates `privatelink` subdomain CNAME records automatically
- Private DNS zones must be created and linked to the virtual network
- Custom DNS servers must forward `privatelink` subdomain queries to Azure DNS (`168.63.129.16`)
- DNS zones required for: Foundry endpoint, Storage, Key Vault, AI Search, Cosmos DB, Application Insights

### Hub-and-Spoke Topology

- Explicitly supported and documented
- Hub VNet for shared Azure Firewall
- Spoke VNet for Foundry networking
- VNets peered together
- Firewall inspects and controls outbound (egress) traffic

### Tool Support in Network-Isolated Environments

| Tool | Support | Traffic Flow |
|------|---------|-------------|
| MCP Tool (Private) | Supported | Through your VNet subnet |
| Azure AI Search | Supported | Through private endpoint |
| Code Interpreter | Supported | Microsoft backbone network |
| Function Calling | Supported | Microsoft backbone network |
| Bing Grounding | Supported | **Public endpoint** |
| Web Search | Supported | **Public endpoint** |
| SharePoint Grounding | Supported | **Public endpoint** |
| Foundry IQ | Supported | Via MCP |
| Fabric Data Agent | **NOT supported** | Under development |
| Logic Apps | **NOT supported** | Under development |
| File Search | **NOT supported** | Under development |
| OpenAPI Tool | **NOT supported** | Under development |
| Azure Functions | **NOT supported** | Under development |
| Browser Automation | **NOT supported** | Under development |
| Computer Use | **NOT supported** | Under development |
| Image Generation | **NOT supported** | Under development |
| Agent-to-Agent (A2A) | **NOT supported** | Under development |

> **DEFENSE CONTRACTOR FLAG:** Bing Grounding, Web Search, and SharePoint Grounding work in network-isolated environments but communicate over the **public internet**. If your org requires ALL traffic to remain private, these tools do not meet compliance requirements. They can be blocked via Azure Policy.

### Features NOT Supporting Network Isolation

| Feature | Status |
|---------|--------|
| Hosted Agents | No VNet support |
| Publish Agent to Teams/M365 | Requires public endpoints |
| Synthetic Data Gen for Evaluations | Not supported |
| Traces | No VNet support with private App Insights |
| Workflow Agents | Partial (inbound only) |
| AI Gateway (APIM) | Partial (gateway is public by default) |

> **CRITICAL GAP:** The new Foundry portal experience does NOT fully support end-to-end network isolation scenarios. Microsoft recommends using the **classic experience, SDK, or CLI** for network-isolated deployments.

---

## 4. Model Hosting and Access Strategy

### Deployment Types

| Deployment Type | Description | Billing |
|----------------|-------------|---------|
| **Global Standard** | Routes globally for higher throughput; broadest availability | Pay-as-you-go (tokens) |
| **Global Provisioned Managed** | PTU deployed across global Azure infrastructure | PTU (pre-purchased capacity) |
| **Global Batch** | Async batch processing globally | Per-token, discounted |
| **Data Zone Standard** | Regional data residency with standard billing | Pay-as-you-go |
| **Data Zone Provisioned Managed** | Regional data residency with PTU | PTU |
| **Data Zone Batch** | Batch with data residency | Per-token |
| **Standard (Regional)** | Regional deployment, more limited availability | Pay-as-you-go |
| **Provisioned Managed (Regional)** | Regional PTU | PTU |

### Model Catalog

- **11,000+ models** in the catalog (marketing number includes community/partner models)
- Models from: OpenAI, Meta (Llama), Mistral, DeepSeek, Cohere, xAI (Grok), Black Forest Labs (FLUX), Microsoft (MAI, Phi), Moonshot AI
- **Models sold directly by Azure** (billed through Azure subscription, covered by Azure SLA): OpenAI models + select partner models
- **Models from partners/community**: Different billing, may use Azure Marketplace subscriptions

### Fine-Tuning Options

| Model | Methods | Regions | Status |
|-------|---------|---------|--------|
| gpt-4o-mini | SFT | North Central US, Sweden Central | GA |
| gpt-4o | SFT, DPO | East US2, North Central US, Sweden Central | GA |
| gpt-4.1, 4.1-mini, 4.1-nano | SFT, DPO | North Central US, Sweden Central | GA |
| o4-mini | RFT | East US2, Sweden Central | GA |
| gpt-5 | RFT | North Central US, Sweden Central | Private preview |
| Ministral-3B, Qwen-32B, Llama-3.3-70B, gpt-oss-20b | SFT | Global only | Public preview |

**Global training** is more affordable but has **no data residency guarantees** -- critical for defense contractors.

### Model Router

- Microsoft's `model-router` automatically routes requests to the best-suited model to optimize quality and minimize costs
- Listed as a Microsoft-provided model in the catalog
- **Operational reality:** Useful for cost optimization in non-sensitive workloads; defense contractors will likely want explicit model selection for auditability

### Bring Your Own Models

- Supported via the model catalog and custom deployments
- Hosted agents allow deploying container-based agents with any framework
- Azure ML (separate service) supports custom model training and deployment

---

## 5. Azure OpenAI Integration

### Relationship to Foundry

Azure OpenAI is a **core component** of Foundry. The Foundry resource (`Microsoft.CognitiveServices/account` with kind `AIServices`) inherits Azure OpenAI capabilities. You can:

- **Upgrade** an existing Azure OpenAI resource to a Foundry resource while preserving endpoints, API keys, and existing state
- Deploy all Azure OpenAI models through the Foundry resource
- Use the same `Microsoft.CognitiveServices` RBAC actions and networking

### Content Filtering

- **Enabled by default** on all deployments
- Four harm categories: Sexual, Violence, Hate, Self-harm (multi-severity levels)
- **Configurable severity thresholds** per deployment
- Content filtering is **always on** in Azure Government; modified filters require application at `https://aka.ms/AOAIGovModifyContentFilter`

### Rate Limiting

- **Standard deployments**: Shared capacity with token-based rate limits
- **Provisioned deployments (PTU)**: Dedicated capacity, no rate limiting from the platform
- Quotas vary by model, region, and deployment type
- Quota increases available via support request (in Gov cloud: `https://aka.ms/AOAIGovQuota`)

### PTU vs. Pay-as-You-Go

| Aspect | Pay-as-You-Go (Standard) | PTU (Provisioned) |
|--------|-------------------------|-------------------|
| Billing | Per token | Pre-purchased capacity units |
| Throughput | Shared, rate-limited | Dedicated, guaranteed |
| Latency | Variable | Predictable |
| Commitment | None | Typically 1-month minimum |
| Best for | Variable/exploratory workloads | Production with predictable load |

### API Surface

| API | Models |
|-----|--------|
| Chat Completions API | GPT-4o, GPT-4, GPT-5.x, o-series, gpt-oss, gpt-4.1 |
| Responses API | GPT-5.x, o3, o4-mini, codex-mini, gpt-4.1 |
| Embeddings API | text-embedding-* models |
| Images API | gpt-image-1, FLUX models |
| Audio API | whisper, gpt-4o-transcribe, tts |
| Realtime API | gpt-4o-realtime-preview, gpt-realtime |

---

## 6. Governance and Security

### Content Safety (Native Capabilities)

| Feature | Purpose | Status |
|---------|---------|--------|
| **Prompt Shields** | Detects User prompt attacks / jailbreak attempts on LLMs | GA |
| **Groundedness Detection** | Detects whether LLM responses are grounded in source materials | Preview |
| **Protected Material Detection** | Scans AI-generated text for known copyrighted content (lyrics, articles, code) | GA |
| **Task Adherence** | Detects misaligned/unintended tool use by AI agents | Preview |
| **Text Analysis** | Scans for sexual, violence, hate, self-harm content (multi-severity) | GA |
| **Image Analysis** | Same harm categories for images | GA |
| **Custom Categories (Standard)** | Train custom content categories | Preview |
| **Custom Categories (Rapid)** | Define emerging harmful content patterns quickly | Preview |

### Content Safety Limits

- Text: 10K characters max per call
- Groundedness: 55K characters for grounding sources, 7.5K for text/query
- Prompt Shields: 10K characters for prompts, 5 documents at 10K characters
- Protected material: min 110 characters, max 10K

### Encryption

- **Default:** Microsoft-managed keys, FIPS 140-2 compliant 256-bit AES
- **Customer-managed keys (CMK/BYOK):** Supported; requires Azure Key Vault in the same region with soft delete and purge protection enabled
- **Bring your own Key Vault:** Supported; one Key Vault connection manages all project and resource-level connection secrets

### Audit Logging

- Azure Monitor provides management and usage metrics at resource level
- Project-specific metrics (evaluation performance, agent activity) scoped to individual project containers
- Application Insights integration for detailed tracing
- Azure Activity Log captures control plane operations

### Data Residency

- **Standard deployments:** Data stays in the designated region
- **Global Standard/Provisioned:** Data may be processed in any region for inferencing
- **Data Zone deployments:** Data stays within a defined geographic zone
- **At rest:** Data stays in the designated Azure region of the resource

### Integration with Microsoft Security Stack

- **Microsoft Defender for Cloud:** Real-time threat protection with alerts visible in Foundry
- **Microsoft Purview:** Enterprise data security and governance
- **Azure Policy:** Enforce organizational standards, can block specific tools/features
- **Azure API Management (AI Gateway):** Enhanced governance across models and MCP tools

---

## 7. Agent Orchestration

### Foundry Agent Service Overview

Fully managed platform for building, deploying, and scaling AI agents. Three agent types:

| Type | Code Required | Hosting | Orchestration | Best For | Status |
|------|:---:|---------|--------------|----------|--------|
| **Prompt Agents** | No | Fully managed | Single agent | Prototyping, simple tasks | GA |
| **Workflow Agents** | No (YAML optional) | Fully managed | Multi-agent, branching | Multi-step automation | Preview |
| **Hosted Agents** | Yes | Container-based, managed | Custom logic | Full control, custom frameworks | Preview |

### Built-in Tools

- Web Search, File Search, Memory, Code Interpreter
- MCP (Model Context Protocol) servers
- Custom functions
- 1,400+ tools via tool catalog (Logic Apps connections to SAP, Salesforce, Dynamics 365, etc.)
- Azure DevOps MCP Server (preview)

### Agent Identity

- Each agent can have a **dedicated Microsoft Entra identity**
- Supports scoped access to resources and APIs without sharing credentials
- Managed authentication including service-managed credentials and On-Behalf-Of (OBO)

### Multi-Agent Patterns

- **Workflow agents** support multi-agent orchestration: sequential execution, branching logic, human-in-the-loop, group-chat patterns
- Visual builder in Foundry portal or YAML definitions in VS Code
- Framework-agnostic for **hosted agents**: supports Microsoft Agent Framework, LangGraph, LangChain, CrewAI, LlamaIndex

### Semantic Kernel Integration

- Semantic Kernel is part of the Microsoft Agent Framework ecosystem
- Foundry agents can be built with Semantic Kernel through hosted agents
- Not a first-class native integration in the Foundry portal -- requires code-based approach

### Prompt Flow / Flows (Legacy)

- Prompt Flow was part of the classic Azure AI Studio / Foundry (classic) experience
- In the new Foundry, it is replaced by **Workflow Agents** and **Hosted Agents**
- Prompt Flow still runs via Azure ML compute in the classic portal

### Publishing & Distribution

- Agents can be published to: Microsoft 365, Teams, BizChat, containerized deployments
- Versioning is automatic with rollback capability
- Stable endpoints for published agents

---

## 8. Observability

### Tracing

- **GA for prompt agents**; preview for workflow, hosted, and custom agents
- Built on **OpenTelemetry semantic conventions**
- Captures: latency, exceptions, prompt content, retrieval operations, tool calls
- Server-side traces are **automatic** (no code changes) for prompt agents
- Client-side traces require OpenTelemetry SDK instrumentation
- Traces stored for **90 days** in the Foundry portal

### Azure Monitor Integration

- Traces stored in **Application Insights** (must be connected to the Foundry project)
- Azure Monitor metrics segmented by scope (resource-level vs. project-level)
- Log queries via **Log Analytics** (requires Log Analytics Reader role)
- Supports Azure Monitor OpenTelemetry pipeline

### Evaluation Framework

Built-in evaluators for agent assessment:

| Evaluator Category | Examples |
|--------------------|---------|
| **Agent evaluators** | Task Adherence (does agent follow instructions?) |
| **Quality evaluators** | Coherence, Fluency, Relevance |
| **Safety evaluators** | Violence, Hate, Sexual, Self-harm detection |
| **Text similarity** | NLP-based comparison against reference answers |
| **Custom evaluators** | User-defined evaluation logic |

- Evaluations can be run via SDK or portal
- Results include aggregated pass/fail counts, token usage per model, per-evaluator breakdown
- Row-level output with detailed scoring and reasoning
- **Continuous evaluation** supported for production monitoring
- **CI/CD integration** via GitHub Actions
- **Cluster analysis** to find patterns in errors

### Monitoring Dashboard

- Pre-built monitoring dashboard for agents
- Tracks performance, reliability, and governance metrics
- Service-level metrics available

### Limitations

- **Tracing does NOT support network isolation** with private Application Insights (critical gap for defense)
- Traces are preview for non-prompt agent types

---

## 9. Cost Controls

### Billing Model

- **Platform is free to use and explore** -- billing occurs at deployment/consumption level
- Each service has its own billing model
- No single Foundry-specific pricing page

### Cost Components

| Service | Cost Driver |
|---------|------------|
| Azure OpenAI / Foundry Models | Tokens (input/output) or PTU |
| Azure AI Search | SKU tier + storage + queries |
| Storage (Blob) | Storage volume + transactions |
| Key Vault | Operations + secrets |
| Application Insights | Data ingestion + retention |
| Private Link | Per-endpoint per-hour |
| Compute (if using classic ML) | VM hours |
| Marketplace models | SaaS subscription per project |

### Budget Management

- **Azure Cost Management** for monitoring and analysis
- Budget creation with alerts at subscription and resource group level
- Cost analysis views by resource, service, and time period
- Export cost data to storage for Power BI / Excel analysis
- Filter by resource type (e.g., `microsoft.saas/resources` for marketplace model costs)

### Model Routing for Cost Optimization

- Microsoft `model-router` in the catalog automatically selects optimal model per request
- Can reduce costs by routing simpler requests to cheaper models
- **Operational reality:** Not well-documented for fine-grained control; primarily a convenience feature

### Token Tracking

- Per-model token usage visible in:
  - Evaluation run results (per-model usage breakdown)
  - Azure Cost Management (meter-level detail for marketplace models)
  - Application Insights traces (token counts per span)
- Meters for marketplace models: `paygo-inference-input-tokens`, `paygo-inference-output-tokens`, `paygo-finetuned-model-inference-*`

### What Requires Custom Engineering

- **Per-project chargeback:** No native cross-charge mechanism. Must use resource group isolation + Azure Cost Management tagging
- **Token budgets per user/team:** Not natively supported; requires API Management gateway or custom middleware
- **Real-time spend alerts per model deployment:** Possible via Azure Monitor alerts but requires manual configuration

---

## 10. Data Access and RAG

### Foundry IQ (Formerly Azure AI Search Integration)

- **Foundry IQ** is the new brand for enterprise RAG capabilities
- "Contextual agentic RAG engine with built-in user access permissions"
- Connects agents to multiple data sources via a single entry point
- Provides citation-backed answers

### Azure AI Search

- Core vector store and knowledge retrieval service
- Resource provider: `Microsoft.Search`
- Supports: vector search, hybrid search, semantic ranking
- Private endpoint support for network isolation
- Agent tool integration supported in VNet-isolated environments

### Vector Store Options (Azure Ecosystem)

| Service | Type | Notes |
|---------|------|-------|
| Azure AI Search | Managed search with vector support | Primary recommended option |
| Azure Cosmos DB | NoSQL with vector search | Used for agent conversation state (Standard Agent setup) |
| Azure Database for PostgreSQL | pgvector extension | AI PostgreSQL extension |
| Azure Managed Redis | In-memory vector store | Caching for RAG performance |

### Document Processing

- **Document Intelligence:** OCR, layout analysis, structured extraction
- **Content Understanding:** Multi-modal document processing
- **Azure Blob Storage:** File storage for RAG sources

### Data Security in RAG

- **Bring your own storage:** Agent state (threads, messages, files) can be stored in customer-managed storage
- **Basic configuration:** Microsoft-managed multitenant storage with logical separation (NOT acceptable for most defense scenarios)
- **Standard configuration:** Customer-owned storage with per-project data isolation
- Private endpoints required for all data services in network-isolated environments
- Customer-managed key encryption supported for data at rest

### Enterprise Data Connectors

- Azure Logic Apps provides 1,400+ connectors (SAP, Salesforce, Dynamics 365, Office, Adobe)
- Azure Functions for event-driven data integration
- MCP (Model Context Protocol) for custom tool/data integration

---

## 11. Environment Separation

### New Model: Foundry Resource + Projects

```
Subscription
  └── Resource Group
        └── Foundry Resource (Microsoft.CognitiveServices/account, kind: AIServices)
              ├── Default Project (Microsoft.CognitiveServices/account/project)
              ├── Project A
              └── Project B
```

### Resource vs. Project Scope

| Level | Controls | Purpose |
|-------|----------|---------|
| **Foundry Resource** | Networking, security, model deployments, encryption, connections | IT governance |
| **Project** | Files, agents, evaluations, datasets, indexes | Development boundary |

### Dev/Test/Prod Pattern

**Recommended approach (defense/enterprise):**

1. **Separate Foundry resources** per environment (dev, test, prod)
2. Each in its own **resource group** for cost isolation
3. Each with its own **networking configuration** (private endpoints, VNet injection)
4. Projects within each resource for team/use-case separation
5. Promote artifacts between environments via CI/CD pipelines

**Not recommended:** Using projects within a single resource as environment boundaries. Projects share the parent resource's networking, security settings, and model deployments.

### Default vs. Non-Default Projects

| Feature | Default Project | Other Projects |
|---------|:-:|:-:|
| Model inference, Agents, Evaluations, Tracing | Yes | Yes |
| OpenAI Batch, Fine-tuning, Stored completions | Yes | No |
| Speech fine-tuning | Yes | No |

### Classic Hub-Based Projects (Legacy)

- Still accessible in Foundry (classic) portal
- Use `Microsoft.MachineLearningServices` resource provider
- Hub provides shared resources: connections, compute, storage
- Projects under hubs are development workspaces
- **Migration path exists** from hub-based to Foundry projects
- **New investment is focused on Foundry resource model** -- hub-based projects are maintenance mode

---

## 12. Compliance

### Azure Government Cloud

| Item | Details |
|------|---------|
| **Portal** | `ai.azure.us` (Foundry), `aoai.azure.us` (OpenAI Studio), `portal.azure.us` |
| **Service endpoint** | `openai.azure.us` |
| **Regions** | `usgovarizona`, `usgovvirginia`, `USGov DataZone` |

### Models Available in Azure Government

#### Standard Deployments

| Model | usgovarizona | usgovvirginia | USGov DataZone |
|-------|:-:|:-:|:-:|
| gpt-5.1 (2025-11-13) | - | - | Yes |
| gpt-4.1 (2025-04-14) | Yes | Yes | Yes |
| gpt-4.1-mini | Yes | Yes | Yes |
| o3-mini | - | - | Yes |
| gpt-4o (2024-11-20) | Yes | Yes | Yes |
| text-embedding-3-large | Yes | - | - |
| text-embedding-3-small | Yes | - | - |
| text-embedding-ada-002 | Yes | Yes | - |

#### Provisioned Deployments

| Model | usgovarizona | usgovvirginia | USGov DataZone |
|-------|:-:|:-:|:-:|
| o3-mini | - | - | Yes |
| gpt-4o | Yes | Yes | Yes |

### Gov Cloud Limitations vs. Commercial

| Feature | Gov Cloud Status |
|---------|-----------------|
| Batch Deployments | **NOT supported** |
| Web app / Copilot Studio deployment | **NOT supported** |
| Abuse Monitoring | **Partial** -- not all features enabled; customer responsible for detecting violations |
| Content Filtering | Always on; modified filters require application |
| Data Storage at Rest | No features currently store customer data at rest (CMK still configurable) |
| Full model context windows | gpt-4.1 limited to 300K (1M not offered) |

### Compliance Certifications

| Certification | Status |
|--------------|--------|
| **FedRAMP High** | Azure OpenAI is in scope (check [Azure Gov Services Audit Scope](https://learn.microsoft.com/en-us/azure/azure-government/compliance/azure-services-in-fedramp-auditscope) for current status) |
| **DoD IL4** | Supported in Azure Government |
| **DoD IL5** | Supported in Azure Government (specific regions) |
| **DoD IL6** | Azure Government Secret -- Azure OpenAI NOT currently available |
| **CMMC** | Azure Government supports CMMC compliance; AI services must be evaluated per CMMC domain |
| **ITAR** | Azure Government supports ITAR; data residency within US boundaries guaranteed |

### Data Residency in Gov Cloud

- **USGov DataZone:** Data at rest stays in the designated Azure region; data MAY be processed in either `usgovarizona` or `usgovvirginia` for inferencing
- **Standard regional:** Data stays in the specific region
- All data processing stays within Azure Government boundaries

> **DEFENSE CONTRACTOR CRITICAL NOTES:**
>
> 1. **Foundry (new portal/resource model) availability in Gov cloud is NOT documented.** The Gov cloud documentation references Foundry (classic) portal. The new Foundry resource model may not yet be available in Azure Government.
> 2. Model availability in Gov cloud is **significantly limited** compared to commercial (no GPT-5.4, no DALL-E, no Sora, limited embedding models)
> 3. **No batch deployments** in Gov cloud
> 4. Abuse monitoring is the customer's responsibility in Gov
> 5. The `USGov DataZone` allows cross-region processing within Gov cloud -- evaluate if this meets your requirements

---

## 13. What Foundry Does NOT Do

### Confirmed Gaps and Limitations

| Gap | Details | Impact |
|-----|---------|--------|
| **Full network isolation in new portal** | End-to-end isolation not fully supported in new Foundry portal; must use classic, SDK, or CLI | High for defense |
| **Traces with private App Insights** | Tracing does not support VNet with private Application Insights | High for defense |
| **Agent-to-Agent (A2A) with VNet** | Not supported in network-isolated environments | Medium |
| **Hosted Agents with VNet** | No virtual network support during preview | High |
| **Workflow Agents outbound VNet** | Only inbound supported | High |
| **File Search in VNet** | Not supported | Medium |
| **OpenAPI tool in VNet** | Not supported | Medium |
| **Azure Functions tool in VNet** | Not supported | Medium |
| **Browser Automation/Computer Use in VNet** | Not supported | Low-Medium |
| **Per-user token budgets** | No native support | Medium |
| **Cross-project chargeback** | No native mechanism | Medium |
| **Gov cloud new Foundry model** | Documentation only references classic portal | High for defense |
| **Model context window in Gov** | gpt-4.1 limited to 300K vs 1M in commercial | Medium |
| **Batch deployments in Gov** | Not available | Medium |
| **Custom model training in Foundry** | Fine-tuning only for specific models; custom training requires Azure ML | Medium |

### Marketing vs. Reality

| Marketing Claim | Operational Reality |
|-----------------|-------------------|
| "11,000+ models" | Most are community/partner models via Marketplace. Direct Azure models are ~50-100. Many require registration. |
| "1,400+ tool connections" | Via Azure Logic Apps (separate service with its own billing). Not all work in VNet isolation. |
| "End-to-end network isolation" | Multiple features explicitly don't support it. New portal doesn't support it. |
| "Unified platform" | Two portals coexist (classic and new). Two resource models coexist. Migration required. |
| "Enterprise-grade security" | Tracing doesn't work with private App Insights. Hosted agents have no VNet support. |
| "Single management plane" | Model deployments, RBAC, and networking align, but cost management, observability, and some features still require multiple Azure portal views. |
| "Foundry IQ -- enterprise RAG" | Preview feature. Operational maturity unclear. |
| "Model Router optimizes quality and cost" | Limited documentation on how it works, what models it selects, or how to control its behavior. |

### What Requires Custom Engineering

1. **Per-team cost allocation and chargeback** -- must build using Azure tags, resource groups, and Cost Management APIs
2. **Token-level budget enforcement** -- requires API Management gateway or custom proxy
3. **End-to-end audit trail** for AI decisions -- must combine Application Insights traces + Azure Activity Log + custom logging
4. **Model evaluation pipelines** for classified/sensitive data -- evaluations use managed compute that may not meet all compliance needs
5. **Disaster recovery** -- no built-in cross-region failover for Foundry resources; must architect manually
6. **Hybrid cloud scenarios** (on-prem + Azure) -- Foundry Local exists for edge, but no documented hybrid architecture for classified environments
7. **Custom content filters** beyond the built-in categories -- requires Content Safety custom categories (preview)
8. **Integration with existing SIEM/SOAR** -- must use Azure Monitor export + custom connectors

---

## 14. Hub and Project Model

### Classic Model (Hub-Based, Maintenance Mode)

```
Hub (Microsoft.MachineLearningServices/workspaces, kind: hub)
  ├── Shared connections (OpenAI, Storage, Key Vault)
  ├── Shared compute resources
  ├── Shared networking config (Managed VNet)
  └── Projects
        ├── Project A (workspace, kind: project)
        └── Project B (workspace, kind: project)
```

- Hub provides centralized governance
- Projects are development workspaces
- All projects share hub's networking and security
- Managed VNet with three isolation modes: Public, Private with Internet Outbound, Private with Approved Outbound

### New Model (Foundry Resource, Active Development)

```
Foundry Resource (Microsoft.CognitiveServices/account, kind: AIServices)
  ├── Networking, security, model deployments, encryption
  ├── Connected resources (Storage, Key Vault, AI Search, Cosmos DB, App Insights)
  └── Projects (Microsoft.CognitiveServices/account/project)
        ├── Default Project (more capabilities)
        ├── Project A
        └── Project B
```

- Foundry resource is the governance boundary
- Projects are sub-resources with their own managed identities
- Projects share parent's networking, deployments, and security settings
- Default project has more capabilities than non-default projects

### Isolation Boundaries

| Boundary | Classic Hub | New Foundry |
|----------|------------|-------------|
| Network | Managed VNet at hub level | Private endpoints + VNet injection at resource level |
| RBAC | Hub scope + project scope | Resource scope + project scope |
| Data | Shared storage at hub level | Managed storage or BYO at resource level; per-project isolation with BYO |
| Models | Connections at hub level | Deployments at resource level |
| Secrets | Hub Key Vault or managed credential store | Resource Key Vault or managed credential store |

### Migration Path

- Hub-based projects can be migrated to Foundry projects
- Azure OpenAI resources can be upgraded to Foundry resources preserving endpoints and keys
- Microsoft recommends new deployments use the Foundry resource model

---

## 15. Deployment and CI/CD

### Infrastructure as Code

#### Bicep (Primary Recommended)

- **Native support** for Foundry resources and projects
- Resource types:
  - `microsoft.cognitiveservices/accounts` (Foundry resource)
  - `microsoft.cognitiveservices/accounts/projects` (Foundry project)
- Production-ready templates available at: `https://github.com/azure-ai-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep`
- Template scenarios include:
  - `00-basic` -- Simple resource + project
  - `19-hybrid-private-resources-agent-setup` -- Network-isolated agent setup
- Can export existing portal-configured resources as Bicep files

#### Azure CLI

Full support for creating and managing Foundry resources:

```bash
# Create resource
az cognitiveservices account create \
  --name my-foundry-resource \
  --resource-group my-foundry-rg \
  --kind AIServices --sku s0 \
  --location eastus \
  --allow-project-management

# Create project
az cognitiveservices account project create \
  --name my-foundry-resource \
  --resource-group my-foundry-rg \
  --project-name my-foundry-project \
  --location eastus
```

#### Python SDK

Full support via `azure-mgmt-cognitiveservices` (v13.7+):

```python
client = CognitiveServicesManagementClient(credential, subscription_id, api_version="2025-04-01-preview")
client.accounts.begin_create(...)  # Create resource
client.projects.begin_create(...)  # Create project
```

#### Terraform

- Supported for classic hub-based projects (`create-hub-terraform` documentation exists)
- For new Foundry resources: use the `azurerm_cognitive_account` resource with `kind = "AIServices"`
- Less mature than Bicep support for the new model

### CI/CD Patterns

| Pattern | Support |
|---------|---------|
| **GitHub Actions for evaluations** | Documented and supported |
| **Evaluation as quality gate** | Native support via SDK |
| **Agent promotion across environments** | Agent versioning + publishing workflow |
| **Infrastructure deployment** | Bicep + Azure CLI in pipelines |
| **Model deployment automation** | Azure CLI `az cognitiveservices account deployment create` |

### Deployment Automation Notes

- Foundry resources can be created via portal, CLI, SDK, Bicep, or ARM templates
- **Export existing configurations** as Bicep from Azure portal (Automation > Export template)
- Private endpoint and VNet injection configuration can be included in templates
- Role assignments should be included in deployment templates for automated setup
- Azure Policy integration ensures compliance on deployment

---

## Summary: Key Decision Points for Defense Contractors

### What Works Well Today

1. Azure OpenAI in Azure Government (FedRAMP High, IL4/IL5)
2. Private endpoints for inbound access
3. RBAC with least-privilege roles
4. CMK encryption
5. Bicep-based infrastructure automation
6. Content Safety (prompt shields, groundedness)
7. Basic agent orchestration (prompt agents)

### What Needs Caution

1. **New Foundry portal** does not fully support network isolation -- use classic/SDK/CLI
2. **Gov cloud** documentation only covers classic model; new Foundry resource model availability uncertain
3. **Tracing** doesn't work with private Application Insights
4. **Multiple features** unsupported in VNet-isolated environments
5. **Model availability** in Gov cloud is significantly reduced
6. **Two parallel resource models** (classic hub vs. new Foundry) create migration risk

### What Is NOT Ready for Defense

1. Hosted agents (no VNet support)
2. Workflow agents outbound networking
3. Agent-to-Agent in isolated environments
4. Full observability in network-isolated deployments
5. Any scenario requiring IL6 (Azure Government Secret)
6. Foundry IQ (preview)

### Recommended Architecture for Defense

```
Azure Government Subscription
  ├── RG: foundry-prod
  │     └── Foundry Resource (AIServices) -- Private endpoints, CMK, BYO storage
  │           ├── VNet injection subnet (/27+)
  │           ├── Default Project (prod agents)
  │           └── Connected: Storage (PE), AI Search (PE), Cosmos DB (PE), Key Vault (PE)
  ├── RG: foundry-staging
  │     └── [Same pattern]
  ├── RG: foundry-dev
  │     └── [Same pattern, relaxed networking]
  └── RG: shared-networking
        ├── Hub VNet (Azure Firewall, DNS)
        └── Spoke VNets (peered, per environment)
```

Use **SDK/CLI for provisioning and management** until the new Foundry portal fully supports network isolation.
