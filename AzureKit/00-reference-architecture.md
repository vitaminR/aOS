> **PREAMBLE** | Type: reference-architecture | Status: active
> Owner: nymil | Updated: 2026-05-04 | Goal: Canonical AzureKit reference architecture — client-agnostic
> Cross-refs: `README.md`, `concepts/*.md`, `6.aOS/01.Reference-Model/agentic-reference-stack-v1.md`

# {a}OS AzureKit — Reference Architecture

## 1. Mission

AzureKit deploys the {a}OS strata model as a **Governed AI Execution Substrate** on Azure plus an on-premise Agent Crucible. The objective is to establish a hard boundary against unstructured "vibe coding" by forcing all AI execution through a deterministic, auditable, and cost-controlled pipeline.

This architecture bridges:

- A localized, high-performance on-premise engineering lab (**The Agent Crucible**)
- A regulated production environment (**Azure** — commercial or Gov Cloud)

**Wedge Mission (every deployment):** the first autonomous act of the system is to observe, document, and map its own creation, proving that the execution layer governs and documents itself without administrative overhead.

## 2. System Architecture (Hybrid Bridge)

### 2.1 The Agent Crucible (On-Premise)

The unmetered experimentation engine. Isolates high-frequency, complex agentic reasoning from the cloud billing cycle.

- **Hardware:** Local bare-metal servers equipped for inference (e.g., RTX 3090/4090 configurations or Mac Mini equivalents).
- **Orchestration logic:** Python and Go state runners.
- **Harness layer:** Pi (`@mariozechner/pi-coding-agent`) and/or Continue.dev / OpenCode as the human-agent interface.
- **Local models:** Mistral-class local models (Mistral Large 3, Hermes, etc.) handle the bulk of execution.
- **Interfaces:** FastMCP / Python MCP SDK servers provide agents with restricted, version-controlled codebase access (search, validate, read).
- **Validation:** Local static analysis (Semgrep, PSScriptAnalyzer) enforces code standards before any cloud deployment.

### 2.2 Azure Control Plane

The hardened runtime. No execution occurs here without passing governance gates.

- **Core resource:** Azure AI Foundry (with associated Azure OpenAI project deployments).
- **Gatekeeper:** Azure API Management (APIM). Mandatory choke point for all internal API traffic — enforces RBAC, token limits, model routing.
- **Identity & secrets:** Microsoft Entra ID (Managed Identities) and Azure Key Vault. No hardcoded keys.
- **Telemetry:** Azure Monitor and Log Analytics handling metadata ingestion only.

### 2.3 Intelligence Ingestion Loop (optional)

Active sensing layer to map external capabilities into the {a}OS ontology.

- **Data engine:** MV3 Chrome Extension intercepts web evaluation sessions, classifies products against {a}OS strata.
- **Strategic map:** {a}OS Explorer (Next.js + Firebase Hosting) visualizes ingested telemetry and capability mapping.

## 3. Strata Implementation Protocol

| Stratum | Implementation |
|---|---|
| **S7 — Experience & Intent** | Human input via VS Code Chat / Continue.dev / Pi TUI (local) or governed CLI / Markdown dashboard (cloud). The human provides 10% intent. |
| **S6 — Governance & Trust** | Entra ID boundaries + APIM policies + HITL approval gates + Key Vault for secrets. |
| **S5 — Observability & Evaluation** | Azure Log Analytics + local JSONL logs. **Strict constraint:** metadata only (latency, token estimates, timestamps, pass/fail). Full prompt payloads restricted from cloud logs. |
| **S4 — Orchestration & Decisioning** | Deterministic Python/Go state machines. Migration target: LangGraph for v1+. **Strict constraint:** hard circuit breakers — loops terminate fatally after 3 failed verification attempts. |
| **S3 — Execution & Interfaces** | MCP servers + APIM endpoints. Agents access code via typed catalog calls (e.g., `ps_catalog.find_function`, `xml_catalog.validate`), never via raw filesystem commands. |
| **S2 — Knowledge & Memory** | Git-backed Markdown and JSON logs (Obsidian-compatible). System state is explicit, auditable, human-readable. |
| **S1 — Models & Infrastructure** | Cheap-first routing ladder. Local Mistral handles baseline reasoning; Azure cloud handles governed execution; premium frontier models locked behind APIM evaluation gates. |

## 4. The Self-Documenting Scribe (Wedge Mission)

**Objective:** A lightweight observer agent on the Crucible that ingests telemetry from the Azure bootstrap process and autonomously generates the platform's foundation documentation.

### 4.1 State Flow

1. **Trigger** — engineer executes a setup action via CLI or API (e.g., provisioning an Azure resource, altering an RBAC role).
2. **Ingestion** — action emits a JSON event to a local listener socket on the Crucible.
3. **Processing** — local model processes the event, identifying actor, resource, risk profile, and corresponding {a}OS stratum.
4. **Verification** — Python script (or Verifier-Loop extension; see `concepts/verifier-loop.md`) validates the JSON structure and ensures no payload spillage.
5. **Memory write** — agent appends a structured Markdown entry into the Git-backed `aos7-ai-platform/02-s2-knowledge-memory/run-log.md` repository.

### 4.2 Event Schema

```json
{
  "event_type": "resource_provision",
  "timestamp": "ISO8601",
  "resource_id": "string",
  "actor_id": "string",
  "aos7_stratum": "S1|S2|S3|S4|S5|S6|S7",
  "risk_category": "cost|access|data",
  "decision_reference": "string"
}
```

## 5. Governance & Cost Protocols

1. **The Bash Tool Ban.** Unrestricted bash execution by any agent is strictly prohibited. All filesystem and execution tasks must be mediated through explicit MCP server endpoints.
2. **The API Gateway Mandate.** Raw cloud-model endpoints must not be exposed to internal developers. All traffic routes through APIM to enforce the cost matrix.
3. **Cheap-First Default.** All orchestration logic defaults to querying the local model endpoint. Cloud escalation requires a specific exception flag in orchestration parameters.
4. **Metadata Tracing.** Telemetry scripts strip prompt bodies before transmission to Azure Monitor.

## 6. Tactical Boot Sequence

1. **Identity & base** — provision Entra ID assignments and bootstrap the empty Azure resource group.
2. **Memory initialization** — initialize the Git-backed documentation repository and establish the S2 folder structure.
3. **Crucible ignition** — stand up the physical server, install the harness (Pi or Continue.dev), boot the local Mistral API.
4. **Scribe deployment** — deploy the Self-Documenting listener and point it at the Git repo.
5. **Cloud bootstrap** — deploy the first Azure AI Foundry model. The Scribe observes and documents this action.
6. **Gateway lock** — deploy APIM, cut off direct access to the Foundry endpoint, enforce the routing policy.
7. **Frontend wedge (optional)** — deploy the Chrome Extension and Explorer to begin ingesting capability intelligence.

## 7. Client Deployment Customization Points

When deploying AzureKit at a specific client, these are the parameters to set:

| Knob | Default | Customize per client |
|---|---|---|
| Cloud surface | Azure commercial | Azure Gov / sovereign / commercial |
| Local model | Mistral Large 3 | Hermes / Qwen / client-approved |
| Cloud model tier | GPT-4-class small | Per client compliance approval |
| Compliance posture | Standard | FedRAMP / IL4 / IL5 / DoD SRG |
| Atomic-claim packs | Default set | Domain-specific (defense, finance, health, etc.) |
| Identity authority | Entra ID | Federated to client AD if required |
| MCP server set | Default catalog | Plus client-specific connectors |
| Network egress | Restricted | Air-gap / proxy / standard |

Client-specific overrides live in `50.incubations/<client>/AzureKit-deployment/` and reference this canonical doc as the parent.
