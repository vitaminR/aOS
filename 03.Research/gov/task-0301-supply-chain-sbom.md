# {a}OS Federal Supply-Chain Posture and SBOM Seed (task-0301)

> Companion to the [Government Proposal](../aos7-government-proposal-2026-08.md) and the [Technology Stack Whitepaper](../aos7-technology-stack-whitepaper-2026-08.md).

**Evidence date:** 2026-08-01

**Whitepaper basis:** [`377faf7`, 2026-08-01](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md)

**Status:** proposal evidence seed, not a legal opinion, certification, representation, or claim of federal compliance

## Executive answer

The {a}OS ally-only model allowlist is a useful, enforceable AI-supplier control because the whitepaper requires the gateway to deny non-allowlisted models rather than relying on policy prose ([doctrine, line 47](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L47)). It is not, by itself, a Section 889 control. Section 889 and FAR 52.204-25 address specified covered telecommunications and video-surveillance equipment and services, including Huawei, ZTE, Hytera, Hikvision, Dahua, and covered affiliates or connected entities. The current clause also reaches an entity's use of covered equipment or services, subject to the clause's terms, exceptions, and waiver process ([FAR 52.204-25](https://www.acquisition.gov/far/52.204-25)).

The allowlist is therefore best presented as a broader supplier-risk posture that can complement, but cannot replace, a Section 889 reasonable inquiry, representations, supplier flow-downs, reporting, and hardware/network inventory.

EO 14028 remains important to the secure-software doctrine and NIST guidance, but the current acquisition posture changed on January 23, 2026. OMB M-26-05 expressly rescinded M-22-18 and M-23-16, directs agencies to use mission-tailored risk assessment, requires agencies to maintain complete software and hardware inventories, and permits agencies to request current SBOMs contractually ([OMB M-26-05](https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf)). A proposal should not present the superseded blanket self-attestation process as a current government-wide mandate.

## Evidence boundaries

- **Sourced federal facts:** the FAR, OMB, CISA, NIST, NTIA, and SPDX statements cited below.
- **Whitepaper-derived facts:** the 38 jobs and 76 primary/fallback selections, plus the asserted license and supplier-origin fields, come from the cited whitepaper snapshot and its correction ledger.
- **Inference:** an enforced model allowlist improves supplier control and prevents accidental use of disallowed model providers. That inference does not establish statutory compliance.
- **Not claimed:** Section 889 compliance, EO 14028 compliance, SSDF conformance, a completed reasonable inquiry, an agency-approved SBOM, product security, FOCI clearance, FedRAMP authorization, or past performance.
- **Founder decision:** legal counsel and the prime contractor must decide the representations, contract language, evidence-retention period, and whether any agency-specific rule exceeds this baseline.

## 1. Section 889 mapping

### What the rule actually covers

FAR 52.204-25 defines covered telecommunications equipment or services and implements both Section 889(a)(1)(A) and (B). The covered named suppliers are Huawei, ZTE, Hytera, Hikvision, and Dahua, including specified subsidiaries and affiliates; the clause also includes additional connected entities identified through the stated federal process. Part A prohibits supplying a covered system or service to the Government, while Part B prohibits the Government from contracting with an entity that uses covered equipment or services, subject to the clause's exceptions and waiver provisions ([FAR 52.204-25](https://www.acquisition.gov/far/52.204-25)). FAR 4.2105 prescribes the representations and clause across solicitations and contracts ([FAR 4.2105](https://www.acquisition.gov/far/4.2105)).

### What the {a}OS control does

The whitepaper makes the model-provider rule enforceable at the LiteLLM/OpenRouter gateway and explicitly denies Chinese-origin AI models and products ([whitepaper line 47](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L47), [L6 reinforcement line 584](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L584)). That control can:

1. reduce accidental selection of a disallowed model or model API;
2. create a machine-readable provider/model decision point;
3. emit evidence of allowed and denied model routes; and
4. support broader agency supplier-risk determinations.

### What it does not do

The allowlist does not inventory routers, switches, phones, cameras, cloud-network infrastructure, subcontractors, affiliates, employee-use systems, or transitive hosting suppliers. It does not perform the FAR's reasonable inquiry, SAM exclusion review, representation, disclosure, waiver, or incident-reporting steps. No named Section 889 covered supplier appears in the 76 whitepaper selections below, but that observation is not a reasonable inquiry and cannot support a `does not` representation.

### Proposal-safe wording

> {a}OS enforces an ally-only AI provider and model allowlist at the gateway and records routing decisions. This is a defense-in-depth supply-chain control. Section 889 eligibility remains subject to organization-wide reasonable inquiry, applicable FAR representations and clauses, supplier flow-downs, and contracting-officer review.

### Evidence still required before a representation

- organization-wide telecom and video-surveillance equipment/service inventory;
- supplier and subcontractor Section 889 questionnaires and flow-down procedure;
- SAM exclusion and affiliate review;
- documented reasonable-inquiry method, scope, date, reviewer, findings, and exceptions;
- covered-equipment discovery and FAR reporting runbook; and
- prime-contractor and counsel approval of any offer representation.

## 2. EO 14028, current OMB posture, and SBOM relevance

EO 14028 Section 4 drove NIST secure-software supply-chain guidance, SSDF 1.1, and the original NTIA SBOM minimum elements ([NIST EO 14028 guidance](https://www.nist.gov/news-events/news/2022/02/nist-issues-guidance-software-iot-security-and-labeling), [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), [NTIA 2021 minimum elements](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)). NIST describes SP 800-218 as a common secure-development vocabulary for producers and acquirers, while SP 800-161 Rev. 1 addresses cybersecurity supply-chain risk across products, services, suppliers, and organizational levels ([SP 800-161 Rev. 1 Update 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)).

The 2026 correction is decisive: M-26-05 rescinded M-22-18 and M-23-16. Agencies now tailor assurance to risk and mission, while continuing complete software/hardware inventory and optionally requiring a current SBOM on request ([M-26-05](https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf)). The older CISA common attestation form remains an available resource, not a universal current mandate under the rescinded memoranda ([CISA form page](https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form)).

CISA's 2025 SBOM minimum elements call for per-version/update SBOMs, coverage of all components including transitive dependencies, explicit dependency relationships, distinguishable unknown/redacted components, prompt correction, and distribution that permits agency security-tool integration ([CISA 2025 minimum elements](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf)). SPDX 3.0.1 can represent software composition, suppliers, provenance, licenses, integrity, vulnerabilities, and relationships ([SPDX 3.0.1](https://spdx.dev/wp-content/uploads/sites/31/2024/12/SPDX-3.0.1-1.pdf)). This document is only the human-readable seed for that future machine-readable artifact.

## 3. Control-to-evidence map

| {a}OS control | Evidence available now | Federal relevance | Limit / next artifact |
|---|---|---|---|
| Gateway model allowlist | Whitepaper doctrine at lines 47 and 584 | Supplier/model admission and repeatable enforcement | Export signed allowlist, configuration digest, denial tests, and route logs |
| Open-source-first selection | 76-row selection inventory below | Improves visibility and license review; supports tailored C-SCRM | Pin exact versions/commits and resolve every transitive dependency |
| Standard gateway and OTel seam | LiteLLM selection and whitepaper observability doctrine | Can record model, supplier, route, policy result, and cost | Define immutable log retention, access controls, clock source, and evidence schema |
| File floor, ticket board, ledgers | Git-diffable governance record | Change traceability and human review | Add signed releases, protected branches, two-person approval, and artifact retention |
| Self-hosted/local degraded mode | Whitepaper S0 design | Reduces external supplier dependency during outages | Inventory host hardware/firmware, base images, OS packages, and build provenance |
| This inventory seed | 38 jobs / 76 selection entries | Starts M-26-05 inventory and SBOM-on-request readiness | Generate SPDX 3.0.1 with package identifiers, hashes, dependencies, authorship, and timestamps |

## 4. SPDX-style selection inventory seed

### Reading the table

- **Version basis** records what the whitepaper actually pins. `Unpinned` means the selection names a project/service but not an immutable version, release, commit, model revision, image digest, or package hash.
- **Supplier/origin** is the whitepaper's asserted supplier provenance after applying its correction ledger. It is not a FOCI determination or legal country-of-origin certification.
- **License** is the selected component's whitepaper license characterization. Proprietary APIs and services have no source-code license for the service.
- **Upstream** is an official repository, model page, or product documentation page. A product page is used when there is no source repository.
- The decision-row basis is the committed whitepaper: [L1](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L65-L73), [L2](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L174-L181), [L3](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L265-L271), [L4](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L346-L352), [L5](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L434-L439), [L6](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L506-L513), and [L7](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L598-L604).

| ID | Stratum / job | Lane | Component or selection bundle | Version basis at 2026-08-01 | Supplier / asserted origin | License characterization | Official upstream or product source |
|---|---|---|---|---|---|---|---|
| S001 | L1 / frontier reasoning | Primary | Claude Opus 5 | Named model; API revision unpinned | Anthropic / US | Proprietary API | [Anthropic model docs](https://docs.anthropic.com/en/docs/about-claude/models/overview) |
| S002 | L1 / frontier reasoning | Fallback | Gemini 3.1 Pro | Named model; API revision unpinned | Google / US | Proprietary API | [Gemini model docs](https://ai.google.dev/gemini-api/docs/models) |
| S003 | L1 / local runtime | Primary | llama.cpp + Gemma 3 4B or Phi-4 Mini GGUF | Model family named; commits and weight revisions unpinned | ggml community / Bulgaria-to-Hugging Face US; Google or Microsoft / US | llama.cpp MIT; Gemma custom terms; Phi model terms require exact-weight review | [llama.cpp](https://github.com/ggml-org/llama.cpp), [Gemma 3](https://ai.google.dev/gemma/docs/core/model_card_3), [Phi-4 Mini](https://huggingface.co/microsoft/Phi-4-mini-instruct) |
| S004 | L1 / local runtime | Fallback | Ollama | Unpinned project | Ollama / US | MIT | [ollama/ollama](https://github.com/ollama/ollama) |
| S005 | L1 / model gateway | Primary | LiteLLM Proxy behind the in-house OAuth router | Unpinned project and in-house router commit | BerriAI / US; in-house / US | MIT core; in-house code | [BerriAI/litellm](https://github.com/BerriAI/litellm) |
| S006 | L1 / model gateway | Fallback | OpenRouter | Hosted service; API revision unpinned | OpenRouter / US | Proprietary service | [OpenRouter docs](https://openrouter.ai/docs) |
| S007 | L1 / embeddings | Primary | text-embedding-3-small | Named model; API revision unpinned | OpenAI / US | Proprietary API | [OpenAI embeddings docs](https://platform.openai.com/docs/guides/embeddings) |
| S008 | L1 / embeddings | Fallback | Nomic Embed Text v2 | Model family named; weight revision unpinned | Nomic AI / US | Apache-2.0 per whitepaper; verify chosen weight card | [Nomic model page](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) |
| S009 | L1 / GPU hosting | Primary | RunPod per-second GPU | Hosted service; SKU/image unpinned | RunPod / US | Proprietary service | [RunPod docs](https://docs.runpod.io/) |
| S010 | L1 / GPU hosting | Fallback | Hetzner GEX44 | Named hardware service; image/firmware unpinned | Hetzner / Germany | Proprietary service | [Hetzner GPU servers](https://www.hetzner.com/dedicated-rootserver/matrix-gpu/) |
| S011 | L1 / speech | Primary | faster-whisper + Kokoro-82M | Model named; runtime commit and weight hash unpinned | SYSTRAN / France and OpenAI / US; Kokoro community / US asserted | MIT runtime/Whisper code; Kokoro Apache-2.0 per whitepaper | [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [Kokoro](https://github.com/hexgrad/kokoro) |
| S012 | L1 / speech | Fallback | Deepgram Nova-3 + ElevenLabs | Named hosted models; API revisions unpinned | Deepgram and ElevenLabs / US | Proprietary APIs | [Deepgram models](https://developers.deepgram.com/docs/models-languages-overview), [ElevenLabs docs](https://elevenlabs.io/docs) |
| S013 | L1 / image generation | Primary | OpenAI GPT Image tier | Whitepaper names 1.5/Mini; correction ledger says replacement is required | OpenAI / US | Proprietary API | [OpenAI image docs](https://platform.openai.com/docs/guides/images) |
| S014 | L1 / image generation | Fallback | FLUX via fal.ai or Replicate | Model family and hosted routes; revisions unpinned | Black Forest Labs / Germany; hosts / US | FLUX license varies by model; hosted services proprietary | [BFL FLUX](https://github.com/black-forest-labs/flux), [fal.ai docs](https://docs.fal.ai/), [Replicate docs](https://replicate.com/docs) |
| S015 | L2 / vector DB | Primary | Qdrant | Unpinned project | Qdrant / Germany | Apache-2.0 | [qdrant/qdrant](https://github.com/qdrant/qdrant) |
| S016 | L2 / vector DB | Fallback | sqlite-vec | Unpinned project | Alex Garcia/community / US asserted | MIT OR Apache-2.0 | [asg017/sqlite-vec](https://github.com/asg017/sqlite-vec) |
| S017 | L2 / RAG | Primary | LlamaIndex | Unpinned project | LlamaIndex / US | MIT | [run-llama/llama_index](https://github.com/run-llama/llama_index) |
| S018 | L2 / RAG | Fallback | Haystack | Unpinned project | deepset / Germany | Apache-2.0 | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) |
| S019 | L2 / graph store | Primary | FalkorDB | Unpinned project | FalkorDB / Israel | SSPL; source-available, not OSI | [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) |
| S020 | L2 / graph store | Fallback | Neo4j Community Edition | Edition named; version unpinned | Neo4j / US, Swedish roots | GPL-3.0 community | [neo4j/neo4j](https://github.com/neo4j/neo4j) |
| S021 | L2 / agent memory | Primary | Mem0 | Unpinned project | Mem0 / US | Apache-2.0 | [mem0ai/mem0](https://github.com/mem0ai/mem0) |
| S022 | L2 / agent memory | Fallback | Graphiti | Unpinned project | Zep / US | Apache-2.0 | [getzep/graphiti](https://github.com/getzep/graphiti) |
| S023 | L2 / document parsing | Primary | Docling | Unpinned project/model | IBM / US | MIT code; model licenses must be pinned separately | [docling-project/docling](https://github.com/docling-project/docling) |
| S024 | L2 / document parsing | Fallback | Marker | Unpinned project/model | Datalab / US | GPL-3.0-or-later code; modified OpenRAIL weights per correction ledger | [datalab-to/marker](https://github.com/datalab-to/marker) |
| S025 | L2 / structured store | Primary | SQLite | Unpinned source release | SQLite/Hwaci / US | Public domain | [SQLite source](https://sqlite.org/src/doc/trunk/README.md) |
| S026 | L2 / structured store | Fallback | DuckDB | Unpinned project | DuckDB / Netherlands | MIT | [duckdb/duckdb](https://github.com/duckdb/duckdb) |
| S027 | L3 / MCP servers | Primary | FastMCP | Unpinned project | Prefect / US | Apache-2.0 | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) |
| S028 | L3 / MCP gateway | Fallback | ContextForge MCP Gateway | Unpinned project | IBM / US | Apache-2.0 | [IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge) |
| S029 | L3 / browser automation | Primary | Playwright MCP | Unpinned project and browser image | Microsoft / US | Apache-2.0 | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| S030 | L3 / browser automation | Fallback | Stagehand | Unpinned SDK/service | Browserbase / US | MIT SDK; hosted service proprietary | [browserbase/stagehand](https://github.com/browserbase/stagehand) |
| S031 | L3 / secure execution | Primary | gVisor (runsc) | Unpinned project/kernel/host | Google / US | Apache-2.0 | [google/gvisor](https://github.com/google/gvisor) |
| S032 | L3 / secure execution | Fallback | E2B | Unpinned SDK and infrastructure image | E2B / US, Czech founding roots | Apache-2.0 SDK/infra per whitepaper | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) |
| S033 | L3 / computer use | Primary | Anthropic computer use | Tool identifier/API revision must be pinned; correction ledger names `computer_20251124` | Anthropic / US | Proprietary API | [Anthropic computer use docs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool) |
| S034 | L3 / computer use | Fallback | Bytebot maintained fork | Fork and commit unpinned | Bytebot/community / US asserted | Apache-2.0 per whitepaper | [bytebot-ai/bytebot](https://github.com/bytebot-ai/bytebot) |
| S035 | L3 / integrations | Primary | Composio | Unpinned SDK/service | Composio / US | Open-source SDK plus proprietary platform; exact package license must be captured | [ComposioHQ/composio](https://github.com/ComposioHQ/composio) |
| S036 | L3 / integrations | Fallback | Arcade.dev | Unpinned engine/service | Arcade / US | Open-source engine components plus proprietary platform | [ArcadeAI/arcade-ai](https://github.com/ArcadeAI/arcade-ai) |
| S037 | L4 / orchestration | Primary | Pydantic AI | Unpinned project | Pydantic / UK, correcting whitepaper's US label | MIT | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) |
| S038 | L4 / orchestration | Fallback | LangGraph library | Unpinned library; excludes separately licensed platform runtime | LangChain / US | MIT library | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) |
| S039 | L4 / multi-agent | Primary | Claude Code Agent Teams + file floor | Experimental feature and local floor commit unpinned | Anthropic / US; in-house / US | Proprietary feature plus in-house code | [Agent Teams docs](https://docs.anthropic.com/en/docs/claude-code/agent-teams) |
| S040 | L4 / multi-agent | Fallback | Microsoft Agent Framework | Unpinned project | Microsoft / US | MIT | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) |
| S041 | L4 / durable workflows | Primary | Hatchet | Unpinned project | Hatchet / US | MIT | [hatchet-dev/hatchet](https://github.com/hatchet-dev/hatchet) |
| S042 | L4 / durable workflows | Fallback | Windmill | Unpinned community edition | Windmill / France, correcting whitepaper's US label | AGPL-3.0 CE | [windmill-labs/windmill](https://github.com/windmill-labs/windmill) |
| S043 | L4 / scheduler | Primary | Dagu | Unpinned project | Dagu / Japan-US asserted | GPL-3.0 | [dagu-org/dagu](https://github.com/dagu-org/dagu) |
| S044 | L4 / scheduler | Fallback | Cronicle | Unpinned legacy project | PixlCore / US | MIT | [jhuckaby/Cronicle](https://github.com/jhuckaby/Cronicle) |
| S045 | L4 / human task routing | Primary | gotoHuman | Hosted service revision unpinned | gotoHuman / Germany | Proprietary SaaS | [gotoHuman](https://www.gotohuman.com/) |
| S046 | L4 / human task routing | Fallback | HumanLayer SDK | Unpinned, vendor-declared supersession risk | HumanLayer / US | Apache-2.0 SDK | [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) |
| S047 | L5 / tracing | Primary | Langfuse self-hosted | Unpinned core/EE image boundary | Langfuse / Germany; ClickHouse parent / US | MIT core; separate EE license | [langfuse/langfuse](https://github.com/langfuse/langfuse) |
| S048 | L5 / tracing | Fallback | Arize Phoenix | Unpinned project | Arize / US | Elastic-2.0, source-available | [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) |
| S049 | L5 / evaluation | Primary | DeepEval | Unpinned project | Confident AI / US | Apache-2.0 | [confident-ai/deepeval](https://github.com/confident-ai/deepeval) |
| S050 | L5 / evaluation | Fallback | promptfoo | Unpinned project | Promptfoo/OpenAI / US per correction ledger | MIT | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) |
| S051 | L5 / cost tracking | Primary | LiteLLM Proxy | Unpinned project | BerriAI / US | MIT core | [BerriAI/litellm](https://github.com/BerriAI/litellm) |
| S052 | L5 / cost tracking | Fallback | Langfuse cost tracking | Unpinned core image | Langfuse / Germany; ClickHouse parent / US | MIT core | [langfuse/langfuse](https://github.com/langfuse/langfuse) |
| S053 | L5 / monitoring | Primary | Healthchecks.io | Unpinned self-host image or hosted service | SIA Monkey See Monkey Do / Latvia | BSD self-host; hosted service proprietary | [healthchecks/healthchecks](https://github.com/healthchecks/healthchecks) |
| S054 | L5 / monitoring | Fallback | Prometheus + Alertmanager + Grafana | Three unpinned projects/images | CNCF projects and Grafana / US asserted | Apache-2.0 + Apache-2.0 + AGPL-3.0 | [Prometheus](https://github.com/prometheus/prometheus), [Alertmanager](https://github.com/prometheus/alertmanager), [Grafana](https://github.com/grafana/grafana) |
| S055 | L6 / secrets | Primary | Infisical | Unpinned core/EE image boundary | Infisical / US | MIT core; separate EE license | [Infisical/infisical](https://github.com/Infisical/infisical) |
| S056 | L6 / secrets | Fallback | OpenBao | Whitepaper notes v2.5.0; deployment digest unpinned | Linux Foundation project / US asserted | MPL-2.0 | [openbao/openbao](https://github.com/openbao/openbao) |
| S057 | L6 / policy | Primary | Open Policy Agent | Unpinned binary and policy bundle | CNCF/Styra roots / US | Apache-2.0 | [open-policy-agent/opa](https://github.com/open-policy-agent/opa) |
| S058 | L6 / policy | Fallback | Cedar | Unpinned library and policies | AWS / US | Apache-2.0 | [cedar-policy/cedar](https://github.com/cedar-policy/cedar) |
| S059 | L6 / guardrails | Primary | NeMo Guardrails | Unpinned project/models/config | NVIDIA / US | Apache-2.0 code; model terms separate | [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) |
| S060 | L6 / guardrails | Fallback | Azure AI Content Safety | Hosted API/model revision unpinned | Microsoft / US | Proprietary cloud API | [Azure Content Safety docs](https://learn.microsoft.com/azure/ai-services/content-safety/) |
| S061 | L6 / prompt-injection defense | Primary | LLM Guard | Unpinned project/scanner models | Protect AI/Palo Alto Networks / US | MIT | [protectai/llm-guard](https://github.com/protectai/llm-guard) |
| S062 | L6 / prompt-injection defense | Fallback | LlamaFirewall + PromptGuard 2 | Framework/model revisions unpinned | Meta / US | MIT framework; PromptGuard model under Llama license | [PurpleLlama](https://github.com/meta-llama/PurpleLlama), [Prompt Guard](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) |
| S063 | L6 / spend controls | Primary | LiteLLM Proxy | Unpinned project/config | BerriAI / US | MIT core | [BerriAI/litellm](https://github.com/BerriAI/litellm) |
| S064 | L6 / spend controls | Fallback | Azure Cost Management budgets | Hosted service/API revision unpinned | Microsoft / US | Proprietary cloud feature | [Azure budgets docs](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets) |
| S065 | L6 / audit logging | Primary | Langfuse | Unpinned core/EE image boundary | Langfuse / Germany; ClickHouse parent / US | MIT core; named platform audit logs are EE | [langfuse/langfuse](https://github.com/langfuse/langfuse) |
| S066 | L6 / audit logging | Fallback | Arize Phoenix | Unpinned project | Arize / US | Elastic-2.0 | [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) |
| S067 | L7 / assistant UI | Primary | assistant-ui | Unpinned project | assistant-ui / US | MIT | [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) |
| S068 | L7 / assistant UI | Fallback | Vercel AI SDK + AI Elements | Unpinned packages/components | Vercel / US | Apache-2.0 SDK; verify each component package | [vercel/ai](https://github.com/vercel/ai), [AI Elements](https://ai-sdk.dev/elements) |
| S069 | L7 / operations dashboard | Primary | Next.js + shadcn/ui + Tremor | Whitepaper references Next.js 16; exact package versions unpinned | Vercel/ecosystem / US | MIT + MIT + Apache/MIT package-specific | [Next.js](https://github.com/vercel/next.js), [shadcn/ui](https://github.com/shadcn-ui/ui), [Tremor](https://github.com/tremorlabs/tremor) |
| S070 | L7 / operations dashboard | Fallback | Grafana OSS | Unpinned project/image | Grafana Labs / US | AGPL-3.0 | [grafana/grafana](https://github.com/grafana/grafana) |
| S071 | L7 / approval UX | Primary | AG-UI protocol via CopilotKit | Protocol/SDK revisions unpinned | CopilotKit / US | MIT | [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) |
| S072 | L7 / approval UX | Fallback | HumanLayer | Unpinned SDK/hosted service; supersession risk | HumanLayer / US | Apache-2.0 SDK; hosted service proprietary | [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) |
| S073 | L7 / voice | Primary | Pipecat | Unpinned project and model/provider plugins | Daily / US | BSD-2-Clause | [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) |
| S074 | L7 / voice | Fallback | LiveKit Agents | Unpinned project/service | LiveKit / US | Apache-2.0 | [livekit/agents](https://github.com/livekit/agents) |
| S075 | L7 / artifacts | Primary | Typst | Unpinned compiler/templates | Typst / Germany | Apache-2.0 compiler/CLI | [typst/typst](https://github.com/typst/typst) |
| S076 | L7 / artifacts | Fallback | PptxGenJS | Unpinned package/templates | Open-source project / US asserted | MIT | [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS) |

### Artifact verification

- Structural verifier: 76 sequential inventory entries, exactly 38 primary and 38 fallback selections.
- Citation verifier: 123 HTTPS markdown citations/links detected.
- Upstream-link probe: all 69 unique GitHub repository links returned HTTP 200 on 2026-08-01.
- Federal-policy research was restricted to official Acquisition.gov, White House/OMB, CISA, NIST, NTIA, and SPDX sources.

## 5. Gap register: what prevents this seed from being an SBOM or compliance artifact

| Gap | Why it matters | Evidence required to close |
|---|---|---|
| All 76 selection entries lack a complete immutable deployed-artifact identifier; a few name a model, tool, or project version but still omit the full package/model/image digest | A project name or partial version cannot identify the deployed component or support reliable vulnerability correlation | Exact package/model/image versions, source commits, container digests, hashes, and deployment inventory |
| Compound selections are not decomposed into all packages and transitive dependencies | CISA's 2025 minimum elements expect all components, including transitives | Automated dependency resolution for Go, Python, Node, containers, OS packages, models, and plugins |
| Hosted services expose no customer-verifiable implementation SBOM here | A product URL is not a supplier SBOM | Contractual SBOM-on-request terms, service inventory, provider attestations, and agency-approved alternative evidence |
| Supplier origin is an asserted research field, not a FOCI assessment | Country labels do not establish ownership, control, affiliates, or covered-entity status | NIST SP 1326 due-diligence record covering FOCI, provenance, resilience, cyber practices, and supply-chain tiers |
| License expressions are not package-instance expressions | Bundles and models can carry different or custom terms | SPDX license expressions per package/model instance plus counsel review for SSPL, Elastic, GPL/AGPL, Llama, Gemma, and OpenRAIL terms |
| No dependency relationships or runtime deployment graph | SBOM consumers need `DEPENDS_ON` / contained-by relationships and actual runtime composition | SPDX 3.0.1 Core + Software Profile relationship graph and runtime environment SBOM |
| No author, timestamp, namespace, lifecycle, or update process | A static table becomes stale immediately | Automated per-release generation, signer identity, timestamp, revision policy, storage, distribution, and correction workflow |
| No Section 889 organization-wide reasonable inquiry | The stack selection list omits telecom, video-surveillance, employee-use, and subcontractor systems | Approved inquiry method and completed evidence package across the organization and supply chain |
| Gateway enforcement is doctrine, not attached machine evidence | A claimed allowlist must be proven effective and non-bypassable | Signed config, deny-by-default tests, denied-model probes, admin/RBAC review, direct-egress control, and OTel audit samples |
| No independent secure-development assessment | Green licenses and allied origin do not establish secure development | Risk-tailored SSDF assessment, vulnerability-management evidence, build provenance, signing, and release controls |

NIST SP 1326, finalized in July 2026, frames ICT supplier due diligence around FOCI, provenance, resilience, foundational cyber practices, and supply-chain tiers ([NIST SP 1326](https://csrc.nist.gov/pubs/sp/1326/final)). Those five areas are the right next research frame for each selected supplier.

## 6. Recommended next artifacts

1. Generate an SPDX 3.0.1 Core + Software Profile document from deployed source/package/container/model manifests, not from this research list.
2. Add a runtime-production SBOM for every cloud or self-hosted deployment and regenerate it per release.
3. Create a signed `ally-allowlist.yaml` containing supplier, model identifier, region, approval authority, effective date, expiry/review date, and evidence URLs.
4. Add gateway conformance tests proving deny-by-default behavior, no direct provider bypass, and auditable decision logs.
5. Run an organization-wide Section 889 reasonable inquiry under prime-contractor/counsel direction.
6. Perform supplier due diligence using NIST SP 1326 and record FOCI/provenance evidence separately from marketing country labels.
7. Map the actual development and release pipeline to final NIST SP 800-218 v1.1 practices; track SP 800-218 Rev. 1/v1.2 as draft until NIST finalizes it ([NIST SSDF publications](https://csrc.nist.gov/Projects/ssdf/publications)).

## 7. Proposal language: accurate and defensible

### Safe claim

> {a}OS is designed for evidence-first federal supply-chain assurance. Its model gateway enforces an ally-only allowlist, its open-source-first stack is inventoried by supplier, origin assertion, license, and upstream source, and its roadmap converts deployed artifacts into per-release SPDX SBOMs. These controls support risk-tailored agency evaluation under OMB M-26-05 and NIST C-SCRM guidance. They do not replace Section 889 reasonable inquiry, contract representations, supplier flow-downs, or agency acceptance.

### Claims to avoid

- `{a}OS is Section 889 compliant.`
- `{a}OS is EO 14028 certified.`
- `Open source means supply-chain safe.`
- `Allied origin means approved for federal use.`
- `The current table is an SBOM.`
- `The CISA self-attestation form is currently mandatory government-wide.`
- `No covered supplier exists anywhere in the company supply chain.`

## Primary federal and standards sources

1. [FAR 52.204-25, Prohibition on Contracting for Certain Telecommunications and Video Surveillance Services or Equipment](https://www.acquisition.gov/far/52.204-25)
2. [FAR 4.2105, solicitation provisions and contract clause](https://www.acquisition.gov/far/4.2105)
3. [OMB M-26-05, Adopting a Risk-based Approach to Software and Hardware Security, January 23, 2026](https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf)
4. [NIST SP 800-218, Secure Software Development Framework 1.1](https://csrc.nist.gov/pubs/sp/800/218/final)
5. [NIST SP 800-161 Rev. 1 Update 1, Cybersecurity Supply Chain Risk Management](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)
6. [NIST SP 1326, C-SCRM Due Diligence Assessment Quick-Start Guide, July 2026](https://csrc.nist.gov/pubs/sp/1326/final)
7. [CISA 2025 Minimum Elements for an SBOM](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf)
8. [NTIA 2021 Minimum Elements for an SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)
9. [SPDX Specification 3.0.1](https://spdx.dev/wp-content/uploads/sites/31/2024/12/SPDX-3.0.1-1.pdf)
10. [{a}OS Technology Stack Whitepaper at source commit `377faf7`](https://github.com/vitaminR/aOS/blob/377faf7/03.Research/aos7-technology-stack-whitepaper-2026-08.md)
