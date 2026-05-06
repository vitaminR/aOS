> **PREAMBLE** | Type: kit-index | Status: active
> Owner: nymil | Updated: 2026-05-04 | Goal: Operating documentation for the {a}OS AzureKit — the Azure-native deployment kit for the {a}OS reference stack
> Cross-refs: `0.agentic/00_Ledger/work-environment-spec.md` (air-gap Continue.dev rules), `6.aOS/01.Reference-Model/agentic-reference-stack-v1.md` (canonical strata)

# {a}OS AzureKit

The Azure-native deployment kit for the **{a}OS Agentic Reference Stack**. AzureKit packages the {a}OS strata model into a deployable, governed AI execution substrate for Azure (commercial and Gov Cloud) plus an on-premise Agent Crucible.

**AzureKit is a multi-client product.** It serves any organization deploying agentic systems on Azure that needs:

- Hard governance boundaries against unstructured "vibe coding"
- Cost-controlled, auditable AI execution pipelines
- Cheap-first model routing (local → cloud → frontier)
- Air-gap or sovereign-cloud deployability
- Structured stratum/axis ownership of the agent stack

**Two halves, one system:**

- **Crucible (on-premise)** — unmetered experimentation, local Mistral-class models, terminal harness (Pi or Continue.dev), MCP tool boundaries. Runs the bulk of agent reasoning.
- **Azure (control plane)** — hardened runtime: AI Foundry, APIM gateway, Entra ID, Key Vault. All cloud execution passes governance gates.

The Crucible can be **air-gapped** from the public internet. See `0.agentic/00_Ledger/work-environment-spec.md` for the constraint set we use as a reference air-gap profile.

## Contents

| File | Purpose |
|---|---|
| `00-reference-architecture.md` | Canonical AzureKit reference architecture — strata implementation, hybrid bridge, governance protocols, boot sequence |
| `concepts/verifier-loop.md` | Auto-verifier (Builder/Verifier) pattern; how to spend cheap local tokens to gate expensive cloud calls |
| `concepts/atomic-claims.md` | Verification methodology — decomposing outputs into provable boolean claims |
| `concepts/harness-engineering.md` | The discipline tier model: prompt vs harness vs agentic engineering, applied to AzureKit |
| `concepts/pi-harness-primer.md` | Factual reference on the Pi coding agent (Mario Zechner / `badlogic/pi-mono`, MIT) |

Client-specific deployments live in their own folders under `50.incubations/<client>/AzureKit-deployment/` and reference these canonical docs.

## Strata Quick-Reference (AzureKit canonical mapping)

| Stratum | AzureKit instantiation |
|---|---|
| S7 — Experience & Intent | Local IDE chat (VS Code / Continue.dev / Pi TUI) or governed CLI / dashboard |
| S6 — Governance & Trust | Entra ID + APIM policies + HITL approval gates + Key Vault |
| S5 — Observability & Eval | Azure Log Analytics (metadata only) + local JSONL traces + atomic-claim scorecards |
| S4 — Orchestration | Deterministic state runners (Python / Go), 3-strike circuit breakers, future LangGraph |
| S3 — Execution & Interfaces | MCP servers + APIM endpoints. **Bash ban** is enforced here. |
| S2 — Knowledge & Memory | Git-backed Markdown + JSON (Obsidian-compatible) |
| S1 — Models & Infrastructure | Cheap-first ladder: local Mistral → Azure Gov small-model → premium frontier (gated) |

## Operating Principles (canonical)

These travel with every AzureKit deployment regardless of client:

1. **Cheap-first default.** Orchestration queries the local model first. Cloud escalation requires an explicit flag.
2. **Bash tool ban.** No raw shell execution by any agent. All filesystem and execution route through MCP endpoints.
3. **APIM mandate.** No raw cloud-model endpoints exposed to internal developers. APIM is the choke point for routing, RBAC, and token limits.
4. **Metadata-only cloud logs.** Strip prompt bodies before transmission to Azure Monitor. Full payloads stay on-prem.
5. **3-strike termination.** Verification loops fail-fast after 3 attempts to prevent token hemorrhaging.

## Standard Wedge Mission

The first autonomous act of any AzureKit deployment is to **observe, document, and map its own creation**. A Self-Documenting Scribe agent ingests provisioning telemetry and writes structured Markdown into the Git-backed knowledge stratum. This proves the execution layer can govern and document itself before any application work begins.

## Client Deployments

Each client deployment is a thin layer over the canonical kit:

- **Configuration:** which models in the cheap-first ladder, which Azure region, which compliance posture (commercial / Gov / Defense / FedRAMP)
- **Atomic-claim packs:** task-type-specific claim YAMLs tuned to the client's domain
- **Vendor-mapping overrides:** if the client uses non-default vendors at any stratum
- **Boot sequence customizations:** pre-existing identity / network / compliance constraints

The canonical AzureKit docs (this folder) stay client-agnostic. Client specifics live next to the client's other materials, never here.
