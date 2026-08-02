# {a}OS7 S0 sovereignty profile: the air-gap deployment variant

**Status:** proposed architecture profile for founder review  
**Date:** 2026-08-01  
**Reference baseline:** [{a}OS7 technology stack whitepaper](../../03.Research/aos7-technology-stack-whitepaper-2026-08.md) at commit `377faf7`  
**Scope:** fully disconnected or IL-restricted operation; architecture only, not an authorization, accreditation, compliance, procurement, past-performance, or funding claim.

## Decision boundary

S0 is a deployment profile across the seven strata, not an eighth stratum. Its contract is simple: when the external network is absent, the system keeps the smallest useful local loop standing and **honestly stops** capabilities that cannot be proved locally.

The profile uses “ally origin” as a program screening rule, not a legal certification. Origin entries below identify the named vendor, steward, or model publisher—not the nationality of every contributor. Procurement, export-control, data-classification, accreditation/RMF, and final origin determinations remain **FOUNDER DECISION / customer authority decision**. This note recommends no direct DoD funding path; any later market-entry motion must use the approved ally/protégé/subcontract lane.

## S0 substitution summary (two-column)

One row per stratum; every substitution is ally origin and self-hostable, with license stated inline. Full citations for each item appear in the detailed table below.

| Stratum | Sovereign substitution (origin; license; all self-hosted) |
|---|---|
| **L1 Models & Infrastructure** | llama.cpp (EU; MIT) + Phi-4 Mini weights (US; MIT), Nomic Embed Text v2 MoE (US; Apache-2.0), faster-whisper (France; MIT) over Whisper weights (US; MIT), Kokoro-82M (US; Apache-2.0) |
| **L2 Knowledge & Memory** | Qdrant (Germany; Apache-2.0), LlamaIndex OSS (US; MIT), Docling (US/IBM; MIT), SQLite (US; public domain, [copyright statement](https://sqlite.org/copyright.html)), local file floor (first-party code in this repository, not a third-party admission item; outbound license selection is a FOUNDER DECISION) |
| **L3 Execution & Interfaces** | FastMCP (US; Apache-2.0), Playwright/MCP (US; Apache-2.0), gVisor (US; Apache-2.0) |
| **L4 Orchestration & Decisioning** | Pydantic AI (UK; MIT), first-party file-floor task/claim protocol (this repository, not a third-party admission item; outbound license selection is a FOUNDER DECISION), systemd timers for scheduling (Linux Foundation stewardship; [LGPL-2.1-or-later](https://github.com/systemd/systemd/blob/main/LICENSES/README.md), part of the accredited OS baseline, not a separately admitted artifact) |
| **L5 Observability & Evaluation** | Langfuse core (Germany; MIT outside `ee`), DeepEval (US; Apache-2.0), LiteLLM community (US; MIT outside enterprise dir), Healthchecks (EU; BSD-3-Clause) |
| **L6 Governance, Trust & Economics** | Open Policy Agent (CNCF/Linux Foundation; Apache-2.0), NeMo Guardrails (US; Apache-2.0), LLM Guard (US; MIT) |
| **L7 Experience & Human Interaction** | assistant-ui (US; MIT), AG-UI (US; MIT), Pipecat (US; BSD-2-Clause), Typst (Germany; Apache-2.0) |

## Connected profile vs sovereign profile

Every sovereign substitution below is self-hostable and has an official license source. Product and model licenses are separate: both must be admitted to the offline bill of materials.

| Stratum | Connected profile | Sovereign / air-gap profile |
|---|---|---|
| **L1 Models & Infrastructure** | Frontier model APIs and hosted embeddings/voice may be used through the governed gateway when policy permits. | **Local inference:** `llama.cpp` (EU-origin founder; MIT, self-hosted) with Microsoft **Phi-4 Mini** (US publisher; MIT) as the default screened weight. **Local retrieval and voice:** Nomic Embed Text v2 MoE (US publisher; Apache-2.0), faster-whisper (French vendor; MIT) over OpenAI Whisper weights (US publisher; MIT), and Kokoro-82M (US-listed publisher in the baseline; Apache-2.0). All weights and runtimes are pre-staged; no model download is attempted after isolation. [llama.cpp license](https://github.com/ggml-org/llama.cpp/blob/master/LICENSE), [Phi-4 Mini model card](https://huggingface.co/microsoft/Phi-4-mini-instruct), [Nomic model card](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe), [faster-whisper license](https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE), [Whisper repository](https://github.com/openai/whisper), [Kokoro model card](https://huggingface.co/hexgrad/Kokoro-82M). |
| **L2 Knowledge & Memory** | Connected ingestion may reach approved stores and document sources; Qdrant/LlamaIndex remain the retrieval core. | **Local knowledge plane:** Qdrant (German vendor; Apache-2.0) for vectors, LlamaIndex OSS (US vendor; MIT) for retrieval, Docling (IBM-origin project; MIT) for locally supplied documents, SQLite for transactional state, and the file floor as the authoritative human-readable ledger. No remote connector is enabled. [Qdrant repository/license](https://github.com/qdrant/qdrant), [LlamaIndex license](https://github.com/run-llama/llama_index/blob/main/LICENSE), [Docling repository/license and IBM provenance](https://github.com/docling-project/docling), [SQLite public-domain statement](https://sqlite.org/copyright.html). |
| **L3 Execution & Interfaces** | Approved MCP servers, browser automation, and external integrations may be routed through policy and identity boundaries. | **Local execution plane:** FastMCP (US steward; Apache-2.0), Microsoft Playwright/MCP (US vendor; Apache-2.0), and Google gVisor (US vendor; Apache-2.0) for packaged local tools and sandboxing. External SaaS connectors, cloud computer-use endpoints, and web navigation are absent—not simulated. [FastMCP repository](https://github.com/jlowin/fastmcp), [Playwright repository/license](https://github.com/microsoft/playwright), [gVisor repository/license](https://github.com/google/gvisor). |
| **L4 Orchestration & Decisioning** | Durable orchestration may use a service-backed workflow engine plus model-routed decisioning and fleet coordination. | **Local control loop:** Pydantic AI (UK vendor; MIT) for typed agent boundaries; the file-floor task/claim/handoff protocol for authoritative coordination; an allowlisted local scheduler and OS service manager for retries. The sovereign minimum deliberately does not require a distributed control plane. [Pydantic AI license](https://github.com/pydantic/pydantic-ai/blob/main/LICENSE). **Recommendation:** treat local files as the recovery source of truth and add a heavier scheduler only after an offline load test justifies it. |
| **L5 Observability & Evaluation** | Langfuse, DeepEval, LiteLLM cost telemetry, and external dead-man alerts may be used when reachable. | **Local proof plane:** self-hosted Langfuse core (German-founded vendor; MIT outside its `ee` folders), DeepEval (US vendor; Apache-2.0), and LiteLLM community code (US vendor; MIT outside its enterprise directory) write to local storage. Healthchecks can also self-host (EU vendor; BSD-3-Clause), but e-mail/SMS delivery is unavailable without an approved local relay. [Langfuse repo, self-hosting, and license boundary](https://github.com/langfuse/langfuse), [DeepEval repository/license](https://github.com/confident-ai/deepeval), [LiteLLM license](https://github.com/BerriAI/litellm/blob/main/LICENSE), [Healthchecks repository/license](https://github.com/healthchecks/healthchecks). **Control:** features under commercial/enterprise folders are excluded unless separately licensed. |
| **L6 Governance, Trust & Economics** | Central policy, secret, identity, budget, and approval services may answer gates before an action runs. | **Local policy chain:** Open Policy Agent (CNCF/Linux Foundation stewardship; Apache-2.0), NVIDIA NeMo Guardrails (US vendor; Apache-2.0), and Protect AI LLM Guard (US vendor; MIT) run from pinned local bundles. Secrets are injected from an approved offline keystore; budgets are enforced from a signed local policy snapshot; high-impact actions still require a local human approval token. [OPA repository/license](https://github.com/open-policy-agent/opa), [NeMo Guardrails repository/license](https://github.com/NVIDIA-NeMo/Guardrails), [LLM Guard repository/license](https://github.com/protectai/llm-guard). **Control:** a guardrail library is a component, not proof of safety or compliance. |
| **L7 Experience & Human Interaction** | Web UI, streaming events, voice, and document-generation services may use approved hosted dependencies. | **Local experience:** assistant-ui (US steward; MIT) plus AG-UI (US/CopilotKit steward; MIT) provide the local interaction shell and event contract; Pipecat (US/Daily-origin project; BSD-2-Clause) links the locally staged voice components; Typst (German vendor/project; Apache-2.0) compiles local documents. [assistant-ui organization/license](https://github.com/orgs/assistant-ui/repositories), [AG-UI repository/license](https://github.com/ag-ui-protocol/ag-ui), [Pipecat repository/license](https://github.com/pipecat-ai/pipecat), [Typst repository/license](https://github.com/typst/typst). |

## Zero-network operating contract

### What still works

With power, local compute, pre-staged artifacts, and local identity/time available, the sovereign lane can:

1. accept a local text or voice request;
2. authenticate against the pre-provisioned local identity boundary;
3. apply signed local OPA/guardrail/budget policy;
4. reason with Phi-4 Mini through llama.cpp;
5. embed and retrieve from local Qdrant/SQLite/file-floor knowledge;
6. run allowlisted local MCP/browser/CLI tools inside the packaged sandbox;
7. require local human approval for bounded high-impact steps;
8. emit a local trace, evaluation result, cost estimate, policy decision, and evidence receipt;
9. render local UI, speech, and documents; and
10. queue exportable evidence for later controlled transfer.

This is a **degraded mode by design**: lower reasoning quality, older knowledge, fewer tools, and slower CPU execution are accepted in exchange for continuity and inspectability. Phi-4 Mini’s publisher identifies constrained compute as an intended use but also requires use-case evaluation; this profile therefore makes local evals and honest stops mandatory. [Phi-4 Mini model card](https://huggingface.co/microsoft/Phi-4-mini-instruct)

### Honest stops

The sovereign lane must deny or queue—with a machine-readable reason—rather than imitate:

- frontier-model, hosted embedding, image-generation, or hosted voice calls;
- fresh web search, cloud browser sessions, external e-mail/calendar/Teams/Slack actions, and SaaS MCP connectors;
- external callbacks, paging, billing reconciliation, or telemetry export;
- retrieval of documents not already admitted to the local corpus;
- actions whose identity, policy bundle, approval token, clock, dependency signature, or evidence sink cannot be validated locally; and
- any answer that requires fresher authority than the admitted corpus provides.

The operator sees one of four explicit outcomes: **completed locally**, **completed with degraded capability**, **queued for controlled reconnection**, or **denied / human decision required**.

## Isolation prerequisites

Before the boundary closes, the release authority must stage and verify:

- pinned application images/binaries, model and embedding weights, speech assets, browser binaries, and OS packages;
- an SBOM, license notices, hashes/signatures, vulnerability-review disposition, and ally-origin evidence for every admitted artifact;
- signed policy and budget bundles, local identity/role mappings, approval keys, trusted time behavior, and break-glass procedure;
- the permitted document corpus plus provenance, classification, retention, and deletion rules;
- local storage capacity, backup/restore media, trace retention, and evidence export format; and
- a zero-network acceptance test that physically blocks DNS/egress and walks the full intent-to-evidence loop.

Updates cross the boundary only through customer-approved controlled media and repeat the same admission checks. If any prerequisite is absent, the dependent capability is **unavailable**, not assumed.

## Minimum validation plan

1. **Egress proof:** run the profile with network interfaces disabled and assert zero attempted external dependency is required for the golden path.
2. **Seven-strata proof:** capture one evidence receipt per stratum for a local policy question and bounded tool action.
3. **Denial proof:** attempt one SaaS connector, one missing document, and one unsigned policy bundle; verify deterministic honest stops.
4. **Recovery proof:** restart from local files/SQLite/Qdrant and replay the last incomplete task without duplicate side effects.
5. **Supply-chain proof:** rebuild from only the admitted offline registry/media and verify all hashes, signatures, and notices.
6. **Human-control proof:** show that a high-impact action cannot run without the local approval artifact and that the approval is recorded.

Target thresholds, information-level mapping, identity mechanism, cryptographic profile, hardware sizing, approved model versions, update cadence, and the authority allowed to reconnect/export are **FOUNDER DECISION / customer authority decision**. No production claim is made until those decisions and the acceptance tests are evidenced.

## Architecture decision summary

- **Keep:** the seven-strata operating contract, local file floor, source-bounded retrieval, policy-before-action, approval gates, and evidence receipts.
- **Substitute:** hosted models, embeddings, voice, observability, policy, and UI services with the cited local components.
- **Disable:** fresh external knowledge and third-party actions while isolated.
- **Prove:** zero egress, deterministic honest stops, local recovery, supply-chain admission, and human control.
- **Escalate:** classification, accreditation, export control, procurement, funding route, and final origin determination.

The sovereign profile is successful when it is slower and narrower **without becoming ambiguous**: the system either acts within its local proof boundary or says exactly why it cannot.
