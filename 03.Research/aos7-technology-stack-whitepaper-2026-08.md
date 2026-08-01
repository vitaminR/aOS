# {a}OS Technology Stack Whitepaper

## The stack behind the Agentic Operating System, organized on the Agentic Reference Stack v1.0

> **Version:** 1.0 draft for founder review · **Date:** 2026-08-01
> **Framework:** Agentic Reference Stack v1.0 (7 strata, 2 axes, optional S0)
> **Method:** 15 agent research fleet, July 2026 web verified, every recommendation adversarially fact checked. Corrections ledger in Appendix B.

---

## 1. Executive summary

This paper picks the technology for every job in the {a}OS stack and says why. The doctrine in one paragraph: rent frontier reasoning at near zero marginal cost through the OAuth lanes we already pay for, run everything else as open source on the one Linux box we already own, connect it all with three wire standards (MCP for tools, OpenTelemetry GenAI for proof, AG-UI for human approval), and enforce the ally only model policy at the gateway where it physically cannot be bypassed.

**The headline number: every primary recommendation in this paper carries zero license cost.** All of them self host on the existing server or ride existing subscriptions. Spend lives in exactly three lines: the 80 dollar per month self hosted posture (which this stack fits with room to spare), frontier token spend as its own metered line (near zero today through the OAuth lanes), and the Azure commercial line for Atlas, which is spend guarded separately.

Three working adoptions are treated as load bearing and never replaced: the file floor and ticket board that coordinate the fleet, the files as memory ledgers, and the OTel GenAI tracing seam. Every recommendation layers under, beside, or behind them.

## 2. How to read this paper

The Agentic Reference Stack v1.0 divides the system into seven strata, each a stable responsibility boundary with its own owner, interface contract, and failure mode. Two axes (Governance & Trust, Observability & Evaluation) cut across all seven. Tools are substrates operating within a stratum; a product can serve more than one stratum but gets one canonical writeup and cross references elsewhere.

| Stratum | Boundary question |
|---|---|
| L7 Experience & Intent | What is the user asking, seeing, approving, or rejecting? |
| L6 Governance & Trust | Is this action allowed, safe, within budget, and auditable? |
| L5 Observability & Evaluation | Can we see, measure, and judge what actually happened? |
| L4 Orchestration & Decisioning | Who does the work, in what order, and when do we stop? |
| L3 Execution & Interfaces | How does the agent actually touch the world? |
| L2 Knowledge & Memory | What does the system know and remember? |
| L1 Models & Infrastructure | What thinks, and what does it run on? |

## 3. The stack at a glance

| Stratum | Primary picks | New license cost |
|---|---|---|
| L7 Experience & Intent | assistant-ui chat · Next.js + shadcn + Tremor dashboards · AG-UI approval wire · Pipecat voice · Typst artifacts | $0 |
| L6 Governance & Trust | Infisical machine secrets · OPA policy gate · NeMo Guardrails · LLM Guard injection defense · LiteLLM hard budgets | $0 |
| L5 Observability & Evaluation | Langfuse tracing · DeepEval evals · LiteLLM cost line · Healthchecks.io dead man switch | $0 |
| L4 Orchestration & Decisioning | Hatchet durable workflows · Dagu scheduler · Pydantic AI harness · Agent Teams on the file floor | $0 |
| L3 Execution & Interfaces | FastMCP servers · Playwright MCP browser · gVisor sandbox · Anthropic computer use · Composio integrations | $0 |
| L2 Knowledge & Memory | Qdrant vectors · LlamaIndex RAG · Docling parsing · Mem0 memory · FalkorDB graph · SQLite state | $0 |
| L1 Models & Infrastructure | Claude Opus 5 + Gemini via OAuth lanes · LiteLLM gateway · llama.cpp local · OpenAI embeddings · RunPod per second GPU · faster-whisper + Kokoro voice | $0 |

## 4. Selection doctrine (the rules every pick obeyed)

1. **Ally only AI, enforced at the gateway.** No Chinese origin models or AI products anywhere in the stack (DeepSeek, Qwen, GLM, Kimi, MiniMax, Yi, and kin are excluded by rule even where they lead benchmarks). The rule is only real if the router enforces it: the LiteLLM gateway and any OpenRouter burst use MUST run an ally only model allowlist. A router that can reach any model is a policy hole no document fixes.
2. **Three budget lines, never blended.** Self hosted infrastructure targets 80 dollars per month. Frontier token spend is a separate metered line, held near zero by the OAuth lanes. Azure commercial spend for Atlas is its own guarded line. Any recommendation that crosses a line says so out loud.
3. **Working adoptions are moats.** The file floor, the ticket board, the ledgers, and the OTel seam took years of lessons to harden. Tools layer under them; nothing replaces them.
4. **Open source and self hostable wins ties.** On this budget, a tool that runs on the existing box at zero license cost beats a slightly better hosted tool with a meter.
5. **Three wire standards.** MCP for tools, OpenTelemetry GenAI semantic conventions for proof, AG-UI for human approval. Vendors are replaceable because the wires are standard.

---

## L1 ,  Models & Infrastructure

> The foundation boundary where models, runtimes, compute, storage, and network resources actually operate.

**What we run today:** Claude, OpenAI, and Gemini through the home built provider router with OAuth free lanes; Azure AI Foundry on the commercial side; one Hetzner bare metal Linux server, no GPU.

The ally only policy bites hardest at this stratum: several Chinese origin models lead open weight benchmarks in mid 2026 and every one of them is excluded by rule, not by taste. The economic center of gravity is the OAuth free lane on existing Claude, OpenAI, and Gemini subscriptions. No commercial gateway replicates it, so the home built router stays in front and everything else layers behind it. Frontier token spend is its own budget line, separate from the 80 dollar self hosted posture, and the OAuth lane is what keeps that line near zero today.

### L1 decisions

| Job | Primary | Fallback |
|---|---|---|
| Frontier reasoning model API | **Claude Opus 5 (Anthropic)** | Gemini 3.1 Pro (Google) |
| Small local model runtime for edge and cheap tasks | **llama.cpp with Gemma 3 4B or Phi-4 Mini in GGUF** | Ollama on the dev laptop |
| Model gateway or router across providers | **LiteLLM Proxy, self hosted behind the home built OAuth lane** | OpenRouter for burst access to odd models |
| Embeddings model | **OpenAI text-embedding-3-small** | Nomic Embed Text v2 self hosted on the Hetzner CPU |
| GPU or compute hosting for self-hosted inference | **RunPod per second rental, spun up only when a job needs a GPU** | Hetzner GEX44 dedicated GPU when steady load justifies flat monthly |
| Speech to text and text to speech | **faster-whisper (STT) plus Kokoro-82M (TTS), self hosted on the Hetzner box** | Deepgram Nova-3 (STT) plus ElevenLabs (TTS) pay as you go |
| Image generation | **OpenAI GPT Image (Mini for drafts, full for finals)** | FLUX via fal.ai or Replicate |

#### Frontier reasoning model API

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Claude Opus 5 (plus Sonnet tier) | Anthropic | United States | Proprietary API | $5 in / $25 out per 1M tokens; OAuth free lane rides the existing Claude Max subscription |
| GPT-5.5 | OpenAI | United States | Proprietary API | $5 in / $30 out per 1M tokens |
| Gemini 3.1 Pro | Google | United States | Proprietary API | $2 in / $12 out per 1M tokens up to 200K context, cheapest frontier tier |
| Mistral Large | Mistral AI | France | Proprietary API (smaller models open weight) | Mid tier, below US frontier pricing |

Claude is already the workhorse across the fleet and the Claude Max OAuth lane means the marginal cost of frontier reasoning is close to zero, which is the whole game on an 80 dollar budget. Opus 5 is the current leaderboard leader at the same price as the old Opus, so there is no reason to switch. Gemini 3.1 Pro is the fallback because it is the cheapest frontier tier by far at 2 dollars in and 12 out, it is already in the router, and its huge multimodal context covers jobs Claude does not. All three are US vendors, so the ally policy is clean.

#### Small local model runtime for edge and cheap tasks

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| llama.cpp | ggml.ai community (Georgi Gerganov) | Bulgaria (EU) | MIT | Free, self hosted |
| Ollama | Ollama Inc | United States | MIT | Free, self hosted |
| vLLM | vLLM project (UC Berkeley roots) | United States | Apache 2.0 | Free, self hosted |

The Hetzner server has no GPU, and the 2026 runtime shootouts agree that when there is no GPU, llama.cpp is the runtime and everything else is a wrapper. It is MIT licensed, tiny, and serves an OpenAI style endpoint the provider router can call for cheap classify and summarize tasks at zero dollars per token. Pair it with Gemma 3 (Google, US) or Phi-4 Mini (Microsoft, US, MIT) so the ally only model policy holds; skip Qwen despite its benchmark scores because it is Chinese origin. Ollama is the fallback for the laptop where convenience beats control, and vLLM only enters the picture if a GPU is ever rented or bought.

#### Model gateway or router across providers

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| LiteLLM Proxy | BerriAI | United States | MIT (open source core) | Free self hosted; pay only underlying provider tokens |
| OpenRouter | OpenRouter Inc | United States | Proprietary hosted service | 5.5 percent credit fee on top of token cost |
| Portkey Gateway | Portkey AI | United States | Apache 2.0 gateway, proprietary managed platform | Open source core free; managed plans from about $499 per month |
| Home built provider router (incumbent) | In house | United States (in house) | Own code | Free |

Keep the home built router in front because its OAuth free lanes are the single biggest cost lever and no commercial gateway replicates them. But stop growing custom plumbing: put LiteLLM behind it as the standard gateway for all API key traffic, since it is MIT licensed, runs on the existing Linux box for free, and gives fallback chains, per project budgets, and OpenTelemetry export that match the OTel GenAI tracing already adopted for Atlas. OpenRouter is the fallback when a one off model is needed fast; its 5.5 percent fee is fine for bursts and terrible as a backbone. Portkey managed pricing blows the 80 dollar posture.

#### Embeddings model

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| text-embedding-3-small | OpenAI | United States | Proprietary API | $0.02 per 1M tokens |
| Nomic Embed Text v2 | Nomic AI | United States | Apache 2.0 | Free, self hosted; runs on CPU |
| voyage-4 | Voyage AI (MongoDB) | United States | Proprietary API | $0.06 per 1M tokens |
| embed-v4 | Cohere | Canada | Proprietary API | $0.01 per 1M tokens |

Embedding volume for a solo founder ledger and codebase graph is tiny, so at 2 cents per million tokens the OpenAI small model costs pennies a month, needs zero new accounts, and is the safest default in every 2026 comparison. The fallback matters more than usual here: Nomic Embed v2 is Apache 2.0, runs on the CPU only Hetzner box, and keeps family finance text from ever leaving the server, which suits Kotana. The tempting open source leaders Qwen3-Embedding and BGE-M3 are Chinese origin and excluded by policy. If retrieval quality ever gates a product, Voyage or Cohere are one line swaps through LiteLLM.

#### GPU or compute hosting for self-hosted inference

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| RunPod | RunPod Inc | United States | Proprietary service | RTX 4090 about $0.34 to $0.74 per hour, per second billing, no monthly minimum |
| Hetzner GEX dedicated GPU | Hetzner | Germany | Proprietary service | GEX44 (RTX 4000 Ada 20GB) 184 EUR per month when in stock; GEX131 (RTX PRO 6000 96GB) 889 EUR per month |
| Vast.ai | Vast.ai Inc | United States | Proprietary marketplace | RTX 4090 from about $0.35 per hour, interruptible cheaper |
| Lambda | Lambda Labs | United States | Proprietary service | 20 to 40 percent premium over RunPod, 99.9 percent uptime SLA |

There is no GPU today and the honest reading is that nothing in the stack needs one full time, so the winning move is to own zero GPUs and rent by the second. RunPod at roughly 35 to 74 cents per hour for an RTX 4090 means an occasional fine tune or batch transcription costs a few dollars, staying inside the 80 dollar posture. Vast.ai is cheaper but its community marketplace machines are a poor fit for household finance data. The fallback is the Hetzner GEX44, because it lives in the same trusted German data center as the prime server; the day self hosted inference runs around the clock, 184 EUR flat beats hourly rental and keeps one vendor.

#### Speech to text and text to speech

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| faster-whisper running Whisper large-v3-turbo | SYSTRAN (runtime, France) on OpenAI weights (US) | France / United States | MIT (runtime and weights) | Free, self hosted; INT8 CPU path works for overnight batch |
| Kokoro-82M TTS | hexgrad (open community) | United States | Apache 2.0 | Free, self hosted; runs on CPU or 2 to 3 GB VRAM |
| Deepgram Nova-3 with Flux | Deepgram | United States | Proprietary API | Pay as you go, roughly half a cent per audio minute |
| ElevenLabs (Scribe v2 STT plus TTS) | ElevenLabs | United States | Proprietary API | Free tier, paid plans from $5 per month |

Voice matters here because of the accessibility North Star, and the self hosted pair costs exactly zero forever. faster-whisper on CPU handles overnight batch transcription of journals and meetings on the existing server, and Kokoro (with Piper as the featherweight option) gives natural narration on CPU, all under MIT and Apache licenses from US and French sources. The fallback flips on when latency matters: a live voice agent needs streaming, and Deepgram Nova-3 with Flux is the 2026 leader for realtime turn taking while ElevenLabs supplies the best sounding voices, both metered so a few dollars covers real usage. No Chinese origin models are involved in either lane.

#### Image generation

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| GPT Image (1.5 and Mini) | OpenAI | United States | Proprietary API | $0.005 per image (Mini) to $0.04 (full quality) |
| FLUX family (schnell, dev, Flux 2 Pro) | Black Forest Labs | Germany | FLUX schnell Apache 2.0; dev non commercial weights; Pro proprietary API | About $0.008 to $0.04 per image on fal.ai or Replicate; Flux 2 Pro $0.055 direct |
| Imagen 4 | Google | United States | Proprietary API | $0.02 (Fast) to $0.06 (Ultra) per image |
| Stable Diffusion 3.5 | Stability AI | United Kingdom | Community License, free under $1M annual revenue | Free weights; hosted runs $0.02 to $0.10 per image |

Image generation is an occasional need here (LinkedIn branding, product art, MilForge decks), so per image pricing beats any subscription and the existing OpenAI account already covers it. GPT Image is the measured quality leader and its text rendering is the best available, which is exactly what marketing images and diagrams need; at half a cent per Mini image a heavy month costs under a dollar. FLUX is the fallback and the hedge: a German vendor with an Apache 2.0 schnell model, run through fal.ai or Replicate at aggregator prices, and it becomes the self hosted path the day a rented RunPod GPU is already spun up. All candidates are US, EU, or UK origin.

### L1 verifier notes (claims corrected by the fact check pass)

- **llama.cpp:** Gerganov is Bulgarian (correct), but Gerganov and the ggml.ai team joined Hugging Face (US) in February 2026; repo lives under the ggml-org GitHub organization. Vendor line is stale.
- **Gemma 3 4B (named in llama.cpp primary):** US origin and GGUF availability confirmed, but Gemma 3 is under the custom 'Gemma Terms of Use' with use restrictions, not MIT/Apache; do not describe the llama.cpp pairing as fully open-licensed.
- **OpenAI GPT Image (1.5 and Mini):** Both gpt-image-1.5 and gpt-image-1-mini are scheduled for API removal on December 1, 2026, with GPT Image 2 as the recommended replacement. Recommending a model four months from removal as the primary is a defect,  the whitepaper should name GPT Image 2 (or 'current GPT Image tier') instead.
- **OpenAI GPT Image (1.5 and Mini):** Mini from ~$0.005/image is confirmed, but full-quality GPT Image 1.5 at 1024x1024 runs ~$0.133/image (low quality ~$0.009). The $0.04 'full quality' ceiling understates real cost by ~3x.
- **FLUX family (Black Forest Labs):** BFL's own pricing lists FLUX.2 [pro] at ~$0.03 per megapixel (~$0.030 for a 1MP image), not $0.055; aggregator per-image prices span roughly $0.003 (schnell on Replicate) to $0.06 depending on model/resolution.
- **GPT-5.5 (candidate only, not primary/fallback):** Out-of-scope candidate flagged in passing: no 'GPT-5.5' appears in July 2026 rankings; OpenAI's current flagship on Artificial Analysis is GPT-5.6 Sol. The candidate row likely names a nonexistent or superseded model.

**Synergy:** LiteLLM is the canonical gateway writeup for the whole paper: L5 reads its cost export and L6 reads its budget enforcement. One binary, three strata served.

---

## L2 ,  Knowledge & Memory

> The context boundary where facts, documents, semantic relationships, and memory are stored and retrieved.

**What we run today:** Files as memory markdown ledgers with an index; SQLite (brain.db); the graphify knowledge graph over the codebase; no vector database in production.

The ledgers stay the source of truth. Nothing in this stratum replaces a file a human can read and git can diff. What is missing is fast semantic recall, and the whole recall lane lands free on the existing box: Docling parses documents, LlamaIndex indexes them, Qdrant stores the vectors, Mem0 adds cross session memory, and SQLite keeps transactional state. Every piece is open source, ally origin, and CPU friendly.

### L2 decisions

| Job | Primary | Fallback |
|---|---|---|
| Vector database | **Qdrant** | sqlite-vec (community fork) |
| RAG framework or engine | **LlamaIndex** | Haystack |
| Knowledge graph store | **FalkorDB** | Neo4j Community Edition |
| Long-term agent memory system | **Mem0** | Graphiti |
| Document parsing and ingestion (PDF, office docs) | **Docling** | Marker |
| Local structured store | **SQLite** | DuckDB |

#### Vector database

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Qdrant | Qdrant GmbH | Germany | Apache 2.0 | Free self-hosted; managed cloud has a free 1GB tier, paid above that |
| sqlite-vec (community fork) | Alex Garcia / community, backed by Mozilla Builders | United States | MIT / Apache 2.0 dual | Free |
| pgvector | Open source community (Andrew Kane) | United States | PostgreSQL License | Free |
| Chroma | Chroma Inc | United States | Apache 2.0 | Free self-hosted; usage-based cloud |

There is no vector DB in production today, so the pick must be cheap to run and cheap to babysit. Qdrant is a German vendor (ally), Apache 2.0, and runs as one small container on the existing Hetzner box with a cron snapshot, which fits the 80 dollar budget with zero license cost. Milvus was dropped because Zilliz has Chinese-origin roots, which fails the ally-only policy. sqlite-vec is the fallback because it lives inside brain.db with no new service at all, which matches the files-plus-SQLite habit, but its maintainer pause means it should not be the first choice for production.

#### RAG framework or engine

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| LlamaIndex | LlamaIndex Inc | United States | MIT | Free open source; LlamaCloud managed parsing/indexing is paid |
| Haystack | deepset GmbH | Germany | Apache 2.0 | Free open source; deepset AI Platform is paid |
| LangChain + LangGraph | LangChain Inc | United States | MIT | Free open source; LangSmith observability is paid |

The need is retrieval over documents and ledgers, not another agent orchestrator, because the fleet already has its own Python orchestration and a provider router. LlamaIndex is the strongest tool in 2026 for exactly that ingest-index-query job, it is MIT licensed and free, it is a US vendor, and it plugs straight into Qdrant and all three adopted model providers without replacing anything. Haystack is the fallback: Apache 2.0 from a German vendor, with a stricter pipeline style that self-hosts cleanly if LlamaIndex ever feels too loose. RAGFlow was excluded because InfiniFlow is a Chinese-origin vendor.

#### Knowledge graph store

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| FalkorDB | FalkorDB Ltd | Israel | SSPL (source available) | Free self-hosted; paid cloud |
| Neo4j Community Edition | Neo4j Inc | United States (Swedish roots) | GPLv3 community; commercial enterprise | Free community edition; enterprise is paid |
| Memgraph | Memgraph Ltd | United Kingdom | BSL 1.1 (not open source) | Free community tier; enterprise around 25,000 USD per year |
| Kuzu | Kuzu Inc (archived) | Canada | MIT | Free |

graphify stays for code understanding; this pick is the runtime graph under agent memory and GraphRAG. FalkorDB wins for this founder because it is an Israeli vendor (ally), free to self-host, light on RAM for a single Hetzner box, and it is a first-class backend for Graphiti, the memory fallback below, so the two picks snap together. SSPL is fine here since nothing at this stratum is resold as a hosted service. Neo4j Community is the fallback: heavier on the JVM, but GPLv3-free, extremely proven, and every memory tool supports it. Kuzu was ruled out because it is archived.

#### Long-term agent memory system

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Mem0 | Mem0 (YC-backed) | United States | Apache 2.0 | Free open source self-hosted; hosted platform paid |
| Graphiti | Zep | United States | Apache 2.0 | Free open source; Zep Cloud is paid |
| Letta | Letta (MemGPT team, UC Berkeley spinout) | United States | Apache 2.0 | Free open source server; Letta Cloud paid |
| LangMem | LangChain Inc | United States | MIT | Free |

The files-as-memory ledgers are a working adoption and should stay the source of truth; what is missing is fast semantic recall across sessions. Mem0 wins because it is a thin Apache 2.0 layer that adds exactly that, it can point at SQLite and Qdrant already chosen above, it self-hosts free on the same box, and integration is measured in hours not weeks, which matters for a solo founder. Letta was passed over because it wants to be the agent runtime, and the fleet already has one. Graphiti is the fallback for when memories need time awareness, and it pairs directly with the FalkorDB pick.

#### Document parsing and ingestion (PDF, office docs)

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Docling | IBM Research | United States | MIT (Granite-Docling models Apache 2.0) | Free |
| Marker | Datalab | United States | Apache 2.0 code; model weights Open Rail-M, free under 2M USD revenue | Free at this founder's size; commercial license above the cap |
| Unstructured (open source library) | Unstructured.io | United States | Apache 2.0 | Free library; serverless API is paid per page |

Docling wins because it is the only free permissive tool that handles the whole office-document spread (PDF, Word, PowerPoint, Excel) with real table structure, and it runs on CPU on the existing box at zero cost. It comes from IBM (US, ally), integrates natively with LlamaIndex chosen above, and even ships an MCP server, matching the MCP adoption. MinerU was excluded because it comes from Shanghai AI Lab, a Chinese-origin vendor, which fails the ally policy. Marker is the fallback for bulk PDF to Markdown speed, and its revenue-capped weights license costs nothing at this company's size.

#### Local structured store

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| SQLite | SQLite Consortium / Hwaci | United States | Public domain | Free |
| DuckDB | DuckDB Labs / DuckDB Foundation | Netherlands | MIT | Free |
| libSQL (Turso) | Turso | United States | MIT | Free open source; Turso cloud has a free tier then paid |

SQLite stays primary on purpose: it is already deployed as brain.db, it is public domain and free, and 2026 guidance still names it the right embedded store for transactional agent state. Replacing a working adoption would burn founder time for no gain. DuckDB is the fallback and really a sidecar: it is MIT licensed from a Dutch vendor (ally), runs in-process with nothing to operate, and can read the SQLite file and Parquet exports directly, which gives fast analytics over cost ledgers and fleet history without touching the write path. Together they cover both the transactional and the analytical half at zero dollars.

### L2 verifier notes (claims corrected by the fact check pass)

- **Haystack:** Free Apache-2.0 open source confirmed, and a paid commercial offering exists, but it has been renamed: now the Haystack Enterprise Platform (formerly deepset Cloud / deepset AI Platform). Whitepaper should use the current name.
- **Marker:** The code is GPL-3.0-or-later, not Apache 2.0,  the repo's pyproject.toml and README at datalab-to/marker both say GPL (one third-party aggregator says Apache 2.0, but the repo's own files are authoritative). Weights are under a Modified AI Pubs OpenRAIL-M with a FUNDING AND revenue cap (sources conflict on $2M vs $5M; the current README is cited at $5M). The axis-note claim that 'Marker relicensed to Apache 2.0 code' is wrong. GPL is a materially different obligation than Apache for anything distributed.

**Synergy:** Docling feeds LlamaIndex natively, LlamaIndex speaks to Qdrant out of the box, and Mem0 can sit on the same Qdrant plus SQLite pair. One retrieval lane, zero new vendors.

---

## L3 ,  Execution & Interfaces

> The action boundary where external tools, APIs, scripts, and sandboxes are invoked.

**What we run today:** MCP servers; Playwright and Chromium ghost tour verification walks; ssh remote execution to the prime server; Claude Code computer use.

MCP is the settled wire standard for this stratum, so every pick is judged by how cleanly it shows up as an MCP tool. FastMCP turns the Python orchestration already on the box into clean tool servers, Playwright MCP lets the fleet drive the same browser stack the ghost tours already trust, and gVisor hardens the sandbox those tools run in for the cost of one afternoon.

### L3 decisions

| Job | Primary | Fallback |
|---|---|---|
| Tool protocol and tool servers (MCP ecosystem) | **FastMCP** | ContextForge MCP Gateway |
| Browser automation for agents | **Playwright MCP** | Stagehand |
| Secure code execution sandbox | **gVisor (runsc)** | E2B |
| Computer use or desktop automation | **Anthropic computer use tool** | Bytebot (maintained fork) |
| API integration platform or function-calling framework | **Composio** | Arcade.dev |

#### Tool protocol and tool servers (MCP ecosystem)

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| FastMCP | Prefect (PrefectHQ) | United States | Apache 2.0 | Free open source; Prefect Horizon enterprise gateway is paid |
| MCP official spec + SDKs | Model Context Protocol project (Anthropic initiated, open governance) | United States | MIT (SDKs), open specification | Free |
| ContextForge MCP Gateway | IBM (open source project) | United States | Apache 2.0 | Free, self hosted |
| TrueFoundry MCP Registry | TrueFoundry | United States | Commercial | Paid SaaS, custom pricing |

The founder already bet on MCP, so the job is building and managing servers well, not picking a protocol. FastMCP is the fastest way to turn the Python orchestration already on the Hetzner box into clean MCP tools, it is free and Apache licensed, and it tracks the official spec closely because its 1.0 version became the official Python SDK. When the fleet grows past a handful of servers, ContextForge adds a free self hosted gateway with one endpoint, access control, and logs, which fits the single server setup and the 80 dollar monthly budget without any SaaS lock in.

#### Browser automation for agents

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Playwright MCP | Microsoft | United States | Apache 2.0 | Free, runs locally via npx |
| Stagehand | Browserbase | United States | MIT (SDK); Browserbase cloud is commercial | SDK free; cloud sessions paid per use |
| Browser Use | Browser Use Inc. (YC backed, Swiss founding team) | United States | MIT | Open source free; hosted cloud paid |
| Browserbase cloud | Browserbase | United States | Commercial | Usage based paid plans |

The ghost tour verification walks already run on Playwright and Chromium, so Playwright MCP is a free straight upgrade that lets Claude and the fleet drive the same browser stack through MCP tools with no new vendor, no API key, and no cost. That keeps the 80 dollar budget untouched and stays deterministic, which matters for verification gates that must not flake. Stagehand is the fallback for the small set of steps that break when pages change, because its MIT licensed SDK adds natural language actions on top of the same Playwright base without forcing a move to a paid cloud.

#### Secure code execution sandbox

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| gVisor (runsc) | Google (open source) | United States | Apache 2.0 | Free, self hosted |
| E2B | E2B (FoundryLabs, Czech founding team) | United States | Apache 2.0 (SDK and infra) | Hobby free with 100 dollar credit and 20 concurrent sandboxes; Pro 150 dollars per month; self host needs about 1250 dollars per month of cloud quota |
| Firecracker | Amazon Web Services (open source) | United States | Apache 2.0 | Free, self hosted |
| Modal | Modal Labs | United States | Commercial (client SDK open source) | Free tier with monthly credits, then usage based |

Fleet agents mostly run code the founder's own tickets produce, which is semi trusted, and the Hetzner bare metal box is already paid for. Installing gVisor as the Docker runtime gives a real security jump over plain containers for zero dollars and one afternoon of setup, and it keeps everything on one Linux server the way the cost posture wants. Full E2B self hosting is far past budget, but the E2B free Hobby tier with its usage credit is the right escape valve when something truly untrusted needs hardware level Firecracker isolation, and its Apache licensed SDK means no lock in. Daytona was dropped because it went closed source in June 2026.

#### Computer use or desktop automation

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Anthropic computer use tool | Anthropic | United States | Commercial API (tool spec published) | Standard Claude token pricing; adds roughly 466 to 499 system prompt tokens; rides existing Claude spend |
| Bytebot (maintained fork) | Bytebot AI and community forks | United States | Apache 2.0 | Free software; roughly 10 to 20 dollars per month of hosting if not on the existing box |
| Gemini Computer Use | Google | United States | Commercial API | Usage based Gemini API pricing |
| OpenAI ChatGPT Agent / Codex computer use | OpenAI | United States | Commercial | ChatGPT subscription and API usage |

The founder already drives the Windows laptop with Claude Code computer use and pays for Claude through the provider router, so the Anthropic tool wins on zero added vendors, zero added subscriptions, and the deepest fit with the existing Claude first fleet. Success rates across the whole market are still modest, around 12 to 20 percent on hard multi app benchmarks, so this stratum should stay a helper, not a load bearing gate. Bytebot as a maintained Apache 2.0 fork is the fallback because it gives an agent its own containerized Linux desktop on the Hetzner box, which is safer than handing unattended agents the founder's personal machine and costs nothing but disk space.

#### API integration platform or function-calling framework

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Composio | Composio | United States | Open source SDK plus commercial platform | Free tier, then usage based paid plans |
| Arcade.dev | Arcade | United States | Open source engine components plus commercial platform | Free developer tier, then paid |
| Zapier MCP | Zapier | United States | Commercial | Free tier limits, then subscription |
| Activepieces | Activepieces | United States | MIT core (open source) | Free self hosted; paid cloud |

The fleet talks MCP already, so the integration layer should show up as MCP tools, not a new framework. Composio wins on sheer catalog breadth with hundreds of prebuilt LLM tuned toolkits, an open source SDK, and a free tier that fits inside the 80 dollar budget, which means the founder writes zero glue code for common SaaS actions like calendar, email, and project boards. Arcade is the fallback for the specific moments that need real per user OAuth delegation, like acting on the founder's own accounts with scoped tokens, because managed auth is its core strength and it is also MCP native and US based.

### L3 verifier notes (claims corrected by the fact check pass)

- **Anthropic computer use tool:** The tool type identifier is 'computer_20251124', not 'computer_use_20251124'. Everything else checks out: it is the newest computer-use tool version, adds the zoom action (enable_zoom), adds 466-499 tokens to the system prompt (plus ~735 input tokens for the tool definition on Claude 4.x), uses standard token pricing, and is available on current Claude models. Vendor Anthropic is US origin.

**Synergy:** The ghost tour stack and the agent browser stack become the same stack: one Playwright, one Chromium, walked by tours at verify time and by agents at work time.

---

## L4 ,  Orchestration & Decisioning

> The control boundary where work is routed, sequenced, delegated, retried, and stopped.

**What we run today:** The home built agent comms file floor, the Routa YAML ticket board, and the CANON v2 lifecycle; systemd timers; Claude Code workflows.

The floor and the board are a moat, not debt. They encode years of hard won rules about claims, evidence, and honest verdicts, and no vendor framework replaces that. Every pick here layers under or beside them: Hatchet gives the overnight loops durable execution so a crash resumes instead of vanishing, Dagu turns cron sprawl into YAML the fleet can commit to git, and typed agents come from Pydantic AI when a job needs a harness rather than a fleet.

### L4 decisions

| Job | Primary | Fallback |
|---|---|---|
| agent orchestration framework | **Pydantic AI** | LangGraph |
| multi-agent coordination system | **Claude Code Agent Teams layered on the existing file floor** | Microsoft Agent Framework |
| durable workflow engine | **Hatchet** | Windmill |
| scheduler and job queue | **Dagu** | Cronicle |
| human-in-the-loop task routing | **gotoHuman** | HumanLayer SDK |

#### agent orchestration framework

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Pydantic AI | Pydantic Services Inc. | United States | MIT | Free open source; optional paid Logfire observability |
| LangGraph | LangChain Inc. | United States | MIT | Free open source library; LangSmith and LangGraph Platform are paid add-ons |
| OpenAI Agents SDK | OpenAI | United States | MIT | Free SDK; pay per token |
| CrewAI | CrewAI Inc. | United States | MIT (core) | Free core; paid cloud platform |

Pydantic AI wins because it is MIT, tiny, and runs on one Linux box with no new services. It talks to all three of his providers through one interface, so the provider router and OAuth free lanes keep working. It forces typed JSON answers, which his zero-dollar LLM lane already demands, and it emits OpenTelemetry GenAI spans out of the box, matching the tracing standard he already picked for Atlas. LangGraph is the fallback for flows that need a real graph with checkpoints and pause-and-resume steps.

#### multi-agent coordination system

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Claude Code subagents and Agent Teams | Anthropic | United States | Proprietary | Included in existing Claude subscription |
| Microsoft Agent Framework | Microsoft | United States | MIT | Free open source; pay only for underlying Azure model calls |
| A2A protocol (Agent2Agent) | Linux Foundation project (started by Google) | United States | Apache 2.0 | Free open standard |
| CrewAI | CrewAI Inc. | United States | MIT (core) | Free core; paid cloud |

The home-built file floor plus Routa board encodes years of hard-won rules (CANON v2 lifecycle, claims, evidence gates), so no vendor tool should replace it. Claude Code Agent Teams adds native lead-and-teammates coordination inside the tool the fleet already lives in, at zero extra cost and zero new servers, while the floor stays the durable ledger of record. Microsoft Agent Framework is the fallback for the Atlas side on Azure because it is MIT, production GA since April 2026, and speaks both MCP and A2A, which protects him from lock-in.

#### durable workflow engine

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Hatchet | Hatchet (YC W24) | United States | MIT | Free self-hosted; paid cloud option |
| Windmill | Windmill Labs | United States (French founder) | AGPLv3 community edition | Free self-hosted CE; paid enterprise edition |
| Temporal | Temporal Technologies | United States | MIT (server) | Self-host free; Temporal Cloud from about 100 USD per month |
| Prefect | Prefect Technologies | United States | Apache 2.0 | Free open source; paid cloud |

His overnight brain loops die today when a session dies, and only files remember what happened. Hatchet gives true durable execution (persisted history, retries, replay from a step) on a single Postgres container, MIT licensed and free self-hosted, so it fits the 80 dollar budget and the one Hetzner box without a Temporal-size cluster. It also plays well with the Pydantic AI pick since both are plain Python. Windmill is the fallback when he wants a web UI, schedules, and built-in approval steps in the same box. Temporal stays the ceiling if he ever outgrows both.

#### scheduler and job queue

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Dagu | Dagu project (now Dagu Cloud); created by a Japanese developer | Japan / United States | GPL-3.0 | Free open source |
| Cronicle | PixlCore | United States | MIT | Free open source |
| systemd timers (status quo) | systemd project | Germany-rooted open source | LGPL-2.1+ | Free, already installed |
| Celery | Celery open source community | International (EU-rooted) open source | BSD | Free open source |

Dagu matches the files-as-truth style of this stack: one binary on the Hetzner box, YAML job definitions the fleet can commit to git, cron plus retries plus overlap control plus a web UI he can check from his phone. The built-in MCP server means his Claude agents can inspect and trigger jobs through the protocol he already standardized on. GPL is fine for internal tooling and the cost is zero. Cronicle is the MIT fallback if he wants a simpler cron-with-UI. systemd timers stay for OS-level chores; heavier queue work rides Hatchet from the workflow pick.

#### human-in-the-loop task routing

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| gotoHuman | gotoHuman | Germany | Proprietary SaaS | Usage-based with a free tier |
| HumanLayer SDK | HumanLayer Inc. | United States | Apache 2.0 | Free open source SDK |
| Windmill approval steps | Windmill Labs | United States (French founder) | AGPLv3 community edition | Free self-hosted |
| LangGraph interrupts | LangChain Inc. | United States | MIT | Free open source |

His founder queue is a markdown file and every alert channel that should page his phone is currently dead, so the gap is a real inbox that reaches a human, not another library. gotoHuman is a maintained product whose whole job is this: the agent posts a review card, he taps approve on his phone, and a webhook resumes the loop on prime. It is German, so it clears the ally-only policy, its free tier fits the 80 dollar budget, and its MCP server plugs into his MCP-first stack. The Apache 2.0 HumanLayer SDK is the self-owned fallback for Slack or email approvals, with the noted risk that the vendor now focuses on CodeLayer.

### L4 verifier notes (claims corrected by the fact check pass)

- **Pydantic AI:** Pydantic Services Inc. is headquartered in London, England, UK (Crunchbase/Tracxn; founder-CEO Samuel Colvin is London-based). US-incorporated 'Inc.' with Sequoia (US) backing, but the company base is the UK. Allied origin either way,  no policy issue, but the whitepaper's 'United States' label is wrong.
- **LangGraph:** The langgraph library itself is MIT (confirmed), but the langgraph-api server runtime used for self-hosted production deployments is Elastic License 2.0 and needs a commercial key,  the blanket 'MIT' label does not cover the Platform runtime. Fine for the recommended library-only use, but the whitepaper should footnote this.
- **Claude Code Agent Teams:** The feature is real and matches the description (code.claude.com/docs/en/agent-teams), but it is EXPERIMENTAL and disabled by default (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1), with documented limitations around session resumption, task coordination, and shutdown. The research presents it as a production-ready primary without flagging experimental status.
- **Windmill:** Company profiles (Tracxn) list Windmill Labs as based in Paris, France, founded 2021 by Ruben Fiszel (Paris-born, EPFL). It is YC-backed so a US Delaware entity likely exists, but the operating base is France, not the US. Allied origin either way,  no policy issue.
- **Cronicle:** Cronicle still exists and is maintained, but the vendor has shipped its successor xyOps ('Cronicle v2', 1.0 launched end of 2025, xyops.io) and Cronicle is now effectively in maintenance mode (bug fixes and security patches only, per PixlCore). As a fresh-adoption fallback the research should either name xyOps or flag Cronicle's legacy status.
- **gotoHuman:** Free tier confirmed ($0/mo, 1 user, up to ~300 reviews/month), but current pricing at gotohuman.com/pricing is tiered seat-based, not usage-based: Team $99/mo (6 seats), Growth $350/mo, Business $950/mo. Budget note: the first paid tier ($99/mo) alone exceeds the stated $80/mo spend posture if the free tier is outgrown.
- **HumanLayer SDK:** Stronger than a 'risk': the humanlayer/humanlayer repo itself states the HumanLayer SDK 'is being superseded by CodeLayer', and the repo's headline product is now CodeLayer (an AI-coding IDE). The SDK remains Apache 2.0 and usable but is vendor-declared legacy,  the whitepaper's framing understates this for a fallback recommendation.
- **L4 stratum policy sweep:** No Chinese-origin products found among the 10 primaries/fallbacks (verified vendors: UK, US, France, Germany, Japan),  zero banned-list hits, so the policy outcome holds. But the sentence as written is inaccurate on two entries: Pydantic AI is UK-based (US claimed) and Windmill is France-based (US claimed); UK is also not 'US, EU, or Japan' post-Brexit, so the blanket wording needs amending even though all origins are allied.

**Synergy:** Adoption order matters: Hatchet under the overnight brains first, Dagu over the systemd sprawl second, everything else only when a real job demands it. Human in the loop routing is covered canonically in L7.

---

## L5 ,  Observability & Evaluation

> The proof boundary where execution becomes visible, measurable, and judged.

**What we run today:** OpenTelemetry GenAI semantic conventions adopted as the tracing standard; the home built aos7 crucible LLM judge; ghost tour shields; no hosted observability vendor.

The standard is the seam: OpenTelemetry GenAI semantic conventions are the instrumentation layer, and every vendor here is replaceable precisely because the spans are OTel on the wire. Langfuse is where those spans land, DeepEval gives the crucible judge versioned test cases and an exit code a gate can trust, and Healthchecks.io finally gives the watch a dead man switch that lives outside the box.

### L5 decisions

| Job | Primary | Fallback |
|---|---|---|
| LLM tracing and observability platform | **Langfuse (self-hosted)** | Arize Phoenix |
| Evaluation framework and LLM-as-judge tooling | **DeepEval** | promptfoo |
| Cost tracking across providers | **LiteLLM Proxy** | Langfuse cost tracking |
| Production monitoring and alerting for agent systems | **Healthchecks.io** | Prometheus + Alertmanager + Grafana |

#### LLM tracing and observability platform

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Langfuse (self-hosted) | Langfuse GmbH, acquired by ClickHouse Inc | Germany (EU), parent now US | MIT core, separate enterprise license for ee folders | Free to self-host with no usage limits; Cloud Hobby free 50k units, Core 29 USD per month |
| Arize Phoenix | Arize AI | United States | Elastic License 2.0 (source available, not OSI) | Free to self-host with no usage limits; Phoenix Cloud paid tiers |
| MLflow 3.x tracing | Databricks and Linux Foundation | United States | Apache 2.0 | Free to self-host |
| LangSmith | LangChain Inc | United States | Proprietary | Free developer tier, then per-seat plus per-trace pricing; self-host is enterprise only |

Langfuse wins because it gives the most tool for zero dollars. It is MIT licensed, EU origin, runs fully on the Hetzner box, and speaks OTLP, so the OTel GenAI spans already emitted by Atlas and Kotana land in it without rework. It also bundles prompt management, eval scoring, and per-trace cost views, which shrinks the number of tools to run. One caution: its v3 stack needs ClickHouse and Redis, so it is the heaviest thing on the box. If that load or the setup pain is too much, Phoenix is the fallback: one lighter container, the most faithful OpenTelemetry citizen, still free to self-host, and its ELv2 license only bites if you resell it as a service, which this founder never will.

#### Evaluation framework and LLM-as-judge tooling

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| DeepEval | Confident AI | United States | Apache 2.0 | Free open source; optional Confident AI cloud has free and paid tiers |
| promptfoo | Promptfoo Inc | United States | MIT | Free open source CLI; paid enterprise cloud |
| Ragas | Exploding Gradients | United States | Apache 2.0 | Free open source |
| Braintrust | Braintrust Data | United States | Proprietary | Free tier, then paid plans |

The aos7 crucible judge already works, so the job here is not to replace it but to give it a spine: versioned test cases, repeatable metrics, and a pass or fail exit code a gate can trust. DeepEval fits that exactly. It is Apache 2.0, free, Python, and pytest-native, which matches the Python orchestration and the house rule that done means exit 0, never judgment. Its judge model is pluggable, so the existing Claude and Gemini OAuth lanes do the scoring at zero marginal cost. Memory already warns that 5 of 7 aos7 pill strata are LLM-judged and can swing; wrapping those judges in DeepEval test suites makes the swings visible and repeatable. promptfoo is the fallback and a good sidecar anyway: MIT, config files in YAML like the ticket board, and it adds red team and jailbreak testing that nothing else in the stack covers.

#### Cost tracking across providers

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| LiteLLM Proxy | BerriAI | United States | MIT (proxy core) | Free to self-host; enterprise license from about 250 USD per month, not needed here |
| Langfuse cost tracking | Langfuse GmbH, acquired by ClickHouse Inc | Germany (EU), parent now US | MIT core | Free when self-hosted |
| Helicone | Helicone, acquired by Mintlify | United States | Apache 2.0 | Free to self-host; hosted free tier |
| OpenMeter | OpenMeter Inc | United States | Apache 2.0 | Free open source; paid cloud |

House rule says cost caps must be measured server side and reconciled from provider usage, and the 2026 landscape splits into gateways that can block and telemetry that can only explain. LiteLLM is the gateway: MIT, free, self-hosted on the Hetzner box, one pricing table across Anthropic, OpenAI, Google, and Azure, and per-key budgets with hard limits so a runaway fleet agent gets cut off instead of written up. It slots behind the existing home-built provider router as the metering and enforcement layer without replacing the OAuth free lanes. Helicone would have been the easy answer a year ago, but it is in maintenance mode after its acquisition, so it fails the durability test. Fallback is Langfuse cost tracking, since it is already running for tracing and gives per-trace dollar rollups for free, just with reporting only and no ability to block spend.

#### Production monitoring and alerting for agent systems

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Healthchecks.io | SIA Monkey See Monkey Do | Latvia (EU) | BSD (self-host); hosted service | Hosted free tier with 20 checks; paid from about 17 to 20 USD per month; free to self-host |
| Prometheus + Alertmanager + Grafana | CNCF and Grafana Labs | United States | Apache 2.0 (Prometheus, Alertmanager), AGPLv3 (Grafana) | Free to self-host |
| Gatus | TwiN (open source project) | Canada | Apache 2.0 | Free to self-host |
| ntfy | ntfy (Philipp Heckel) | United States | Apache 2.0 and GPLv2 dual | Free hosted topics; free to self-host; cheap pro tier |

The agent system today is systemd timers and Python loops on one box, and memory records two live wounds: every prime alert channel is dead so nothing can page the founder, and the last outage proved there is no monitor outside the box. Healthchecks.io fixes both for zero dollars. Each timer curls a ping URL when it runs; if the ping stops, the hosted service, which lives outside Hetzner, sends the page. It is BSD licensed, EU origin, and the free tier's 20 checks cover the current fleet. Wire its notifications through ntfy so alerts actually reach the founder's phone. The Prometheus, Alertmanager, and Grafana stack is the fallback and the growth path: free, Apache and AGPL licensed, US origin, and it adds real metrics like tool call failure rates and token burn once liveness paging is solved. Uptime Kuma was deliberately skipped because its maintainer is Hong Kong based, and the ally-only posture favors avoiding that ambiguity when Gatus and Healthchecks cover the same ground.

### L5 verifier notes (claims corrected by the fact check pass)

- **Langfuse (self-hosted):** Substance confirmed: Berlin, Germany company (YC W23) acquired by ClickHouse Inc (US) on Jan 16, 2026, alongside ClickHouse's $400M Series D. Minor fix: the legal entity is Finto Technologies GmbH operating as Langfuse, not 'Langfuse GmbH'.
- **Arize Phoenix:** Free self-hosting with no feature gates or caps is confirmed. Minor fix: the paid managed ladder is branded Arize AX in 2026 (AX Free $0, AX Pro $50/month, AX Enterprise custom); Phoenix Cloud itself offers free hosted instances. 'Phoenix Cloud paid tiers' slightly misnames the paid product.
- **promptfoo:** US origin (San Francisco) confirmed, but the vendor status is stale: OpenAI announced acquisition of Promptfoo on March 9, 2026, integrating it into OpenAI Frontier. OpenAI publicly committed the tools remain open source under the current license. Note the research penalized Helicone for exactly this acquisition-durability risk while missing promptfoo's own acquisition; fallback durability rationale should be updated.
- **Healthchecks.io:** Free tier of 20 checks and free self-hosting confirmed, but the paid ladder is $5/month Supporter (same limits), $20/month Business (100 checks), $80/month Business Plus (1000 checks). Cheapest paid entry is $5, not ~$17; the ~$17-20 figure only fits the Business tier.

**Synergy:** Langfuse is the canonical trace store writeup: L6 audit logging cross references it rather than repeating it. Cost visibility reads from the LiteLLM gateway chosen in L1.

---

## L6 ,  Governance & Trust

> The policy boundary where access, safety, approval, budget, and compliance are enforced.

**What we run today:** Vaultwarden self hosted for human passwords; the founder decision queue with one click approvals; hand rolled spend guards; Azure Content Safety available on the commercial side.

Split human from machine. Vaultwarden keeps human passwords, Infisical takes machine secrets with rotation and injection, and OPA becomes the one auditable yes or no gate in front of risky tool calls. Budgets stop being advisory: LiteLLM virtual keys make overspend physically impossible per agent per day, which is the only kind of budget that survives an autonomous fleet.

### L6 decisions

| Job | Primary | Fallback |
|---|---|---|
| secrets management | **Infisical** | OpenBao |
| policy engine for agent authorization | **Open Policy Agent (OPA)** | Cedar |
| AI content safety and guardrails | **NeMo Guardrails** | Azure AI Content Safety |
| prompt injection defense | **LLM Guard** | LlamaFirewall with PromptGuard 2 |
| spend controls and budget enforcement | **LiteLLM Proxy** | Azure Cost Management budgets |
| audit logging for agent actions | **Langfuse** | Arize Phoenix |

#### secrets management

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Infisical | Infisical Inc | United States | MIT core, separate commercial license for ee features | Free self-hosted core; cloud free tier; Pro tier 18 USD per identity per month as of June 2026 |
| OpenBao | Linux Foundation (OpenBao project) | United States | MPL-2.0, fully open source | Free, self-run only; v2.5.0 shipped February 2026 |
| Vaultwarden | Community project, Bitwarden compatible (Bitwarden is US) | Community open source, EU maintainer; protocol from Bitwarden, United States | AGPL-3.0 | Free self-hosted |
| HashiCorp Vault | HashiCorp, an IBM company | United States | BUSL-1.1 (source available, not OSI open source) | Community edition free; Enterprise is quote based, community reports put it in the low six figures per year |

Keep Vaultwarden for human passwords, it already works and nothing beats it there. But the agent fleet needs machine secrets: per-agent tokens, secret rotation, and env var injection so keys stop living in files on the Hetzner box. Infisical does that with an MIT core, runs free on the same server, and is far easier for one person to operate than a Vault style system. If Infisical's paid gates (some RBAC and audit retention sit behind Pro) become a problem, OpenBao is the fallback: completely free, Linux Foundation governed, with full audit logging, at the cost of more setup and unseal ops.

#### policy engine for agent authorization

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Open Policy Agent (OPA) | CNCF graduated project, originally Styra | United States | Apache-2.0 | Free, self-hosted single binary |
| Cedar | Amazon Web Services | United States | Apache-2.0 | Free open source library |
| OpenFGA | Okta (CNCF project) | United States | Apache-2.0 | Free self-hosted |
| Permit.io | Permit.io | Israel | Commercial SaaS built on open source OPA and OPAL | Free tier, then paid per monthly active user |

The fleet already routes agent actions through a file floor and ticket board, so what is missing is one auditable yes or no check before each risky tool call. OPA wins because it is a single free binary that runs on the Hetzner box, answers over plain HTTP so Python orchestration and MCP tool wrappers can call it in one line, and every decision can be logged for the audit stratum. It replaces nothing, it wraps what exists. Cedar is the fallback: simpler and safer language with default deny, and it matches what AWS now uses for agent policy, but its ecosystem outside AWS is younger. Casbin was considered and excluded because it is a Chinese origin project, which conflicts with the ally only posture.

#### AI content safety and guardrails

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| NeMo Guardrails | NVIDIA | United States | Apache-2.0 | Free open source |
| Azure AI Content Safety | Microsoft | United States | Commercial cloud API | Pay as you go with a free monthly allowance; rides existing Azure spend guards |
| Guardrails AI | Guardrails AI Inc | United States | Apache-2.0 | Free open source plus a validator hub |
| Llama Guard 4 | Meta | United States | Llama community license (free weights, not OSI) | Free weights, but needs GPU capacity to serve |

Split by surface. For the internal fleet and Kotana, NeMo Guardrails wins: it is free, Apache licensed, runs on the existing Linux box, and does its checks by calling the models already paid for through the provider router, so there is no new GPU or vendor. It also gives topic rails, which matter for a family facing product where kids may talk to Kotana. For Atlas, keep Azure AI Content Safety, it is already wired into Foundry, sits under the existing spend guards, and enterprise buyers expect the Microsoft compliance story. The fallback relationship runs both ways: if NeMo rails prove too fiddly, the Azure API can cover internal traffic too for pennies at this volume.

#### prompt injection defense

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| LLM Guard | Protect AI, part of Palo Alto Networks | United States | MIT | Free open source, self-hosted |
| LlamaFirewall with PromptGuard 2 | Meta | United States | MIT framework code; PromptGuard 2 model under Llama license | Free |
| Lakera Guard | Lakera, acquired by Check Point in September 2025 for about 300 million USD | Switzerland (founded), now Check Point, Israel | Commercial SaaS API | Free tier to start, then enterprise contracts through Check Point |
| promptfoo | OpenAI (acquired March 2026) | United States | MIT open source | Free open source; commercial cloud tiers |

This founder's biggest injection surface is indirect: agents reading web pages, emails, and floor messages that may carry hostile instructions. LLM Guard wins because it is MIT licensed, costs nothing, runs its detector models on the CPU only Hetzner box, and can be inserted as a scan step in the Python orchestration before tool output reaches a model. That matches the memory rule that observed content is data, not commands, and now enforces it in code. LlamaFirewall is the fallback and a good future add: PromptGuard 2 is also CPU friendly and its AlignmentCheck catches goal hijack in multi step agent runs, but the stack is younger and the model weights carry the Llama license rather than a clean OSI license. Lakera Guard stays on the shelf as the managed option if self-hosting ever becomes the bottleneck. Run promptfoo style red team scans quarterly rather than at runtime.

#### spend controls and budget enforcement

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| LiteLLM Proxy | BerriAI | United States | MIT core with a separate enterprise feature set | Free self-hosted; enterprise tier paid |
| Helicone | Helicone, acquired by Mintlify in March 2026 | United States | Apache-2.0 | Free self-hosted; cloud free tier then paid |
| OpenMeter (Kong Metering and Billing) | Kong (acquired OpenMeter in 2026) | United States | Apache-2.0 core stays open | Open source free; Kong Konnect tiers paid |
| Azure Cost Management budgets | Microsoft | United States | Commercial cloud feature | Included free with Azure |

The 80 USD per month posture only holds if a runaway agent physically cannot overspend, and today the guards are hand rolled. LiteLLM Proxy wins because it is the one free self-hosted tool that enforces hard budgets, not just alerts: every agent gets a virtual key with a daily and monthly cap, and the proxy refuses calls once a cap is hit. It fronts Anthropic, OpenAI, and Gemini, so it slots behind the existing provider router without replacing it, and the OAuth free lanes simply bypass it at zero cost. Per the standing rule, treat LiteLLM numbers as the fast gate and still reconcile against provider usage pages monthly, since server side truth wins. For Atlas, the fallback is the tool already there: Azure Cost Management budgets with the existing spend guards, because commercial spend should stay inside the Azure boundary where TPM floors already apply.

#### audit logging for agent actions

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Langfuse | Langfuse GmbH | Germany | MIT core, only ee directory is commercial | Free self-hosted without usage limits; cloud free tier then paid |
| Arize Phoenix | Arize AI | United States | Elastic License 2.0 (source available, fine for internal use) | Free, no feature gates or usage caps |
| OpenTelemetry Collector plus Grafana stack | CNCF and Grafana Labs | United States | Apache-2.0 collector; AGPL-3.0 Grafana components | Free self-hosted |

Atlas already emits OTel GenAI spans, and the fleet's file ledgers record outcomes but not the step by step story of what each agent did and why. Langfuse wins because it speaks OTel on the wire, so the existing gen_ai instrumentation lands in it unchanged, and its session and user views turn raw spans into a reviewable audit trail: which agent, which tool, which cost, which decision. The MIT core license means no strings for a product family that may itself be sold, and Germany fits the ally only rule. Its one real cost is a heavier self-host stack, so if ClickHouse plus Redis is too much weight for the single Hetzner box, Arize Phoenix is the fallback: one container, zero caps, fully OTel native, and its Elastic license is only a problem if you resell Phoenix itself, which is not the plan. Either way the span format stays vendor neutral OTel, so switching later is cheap.

### L6 verifier notes (claims corrected by the fact check pass)

- **Langfuse (primary, audit logging),  'strongest MIT licensed audit trail' framing:** Core OTel tracing (sessions, users, tool spans) is genuinely MIT and free without limits, and does serve as the agent-action audit trail. But Langfuse's named 'Audit Logs' feature,  plus Data Retention Policies and server-side data masking,  sits in the commercial EE tier (langfuse.com/self-hosting/license-key, github.com/orgs/langfuse/discussions). For an L6 governance stratum the whitepaper should state that platform-level audit logs and retention policy enforcement require a paid Langfuse license, or fall to OpenBao/Phoenix-side compensating controls.

**Synergy:** The hard rule from the critic pass: the ally only policy must be ENFORCED at the gateway with a model allowlist. An open router that can reach any model is a policy hole no document fixes.

---

## L7 ,  Experience & Intent

> The human boundary where requests enter, responses render, and approvals happen.

**What we run today:** Next.js 16 Cyber Nouveau dashboards; the Compass chat pane on Atlas; the founder decision dock with approve and hold buttons; scripted deck builds.

Keep the look, standardize the wire. assistant-ui drops into the existing Next.js dashboards headless so Cyber Nouveau survives, AG-UI gives every agent the same way to raise a hand into the decision dock, Pipecat runs the whole voice loop on owned hardware which is what the accessibility North Star demands, and Typst turns agents that write plain text into agents that ship branded PDF artifacts in one command.

### L7 decisions

| Job | Primary | Fallback |
|---|---|---|
| Chat and assistant UI framework | **assistant-ui** | Vercel AI SDK + AI Elements |
| Operations dashboard stack | **Next.js + shadcn/ui + Tremor** | Grafana OSS |
| Human approval UX for agent actions | **AG-UI protocol via CopilotKit** | HumanLayer |
| Voice interface | **Pipecat** | LiveKit Agents |
| Document and artifact generation (decks, reports) | **Typst** | PptxGenJS |

#### Chat and assistant UI framework

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| assistant-ui | assistant-ui (YC W25) | United States | MIT (open source library; optional paid cloud for persistence) | Free self-hosted; cloud tier optional |
| Vercel AI SDK + AI Elements | Vercel | United States | Apache-2.0 (SDK); open source components | Free |
| CopilotKit | CopilotKit Inc. | United States | MIT | Free open source; paid hosted cloud optional |
| Chainlit | Chainlit (Literal AI) | France | Apache-2.0 | Free |

assistant-ui wins because it drops straight into the Next.js 16 dashboards the founder already ships. It is MIT, US-made, and free, so it fits the 80 dollar budget with zero spend. It is headless, so the Cyber-Nouveau look and the Compass pane style survive. It also speaks AG-UI and LangGraph, which means the same chat surface can later render agent approvals and tool calls without a rewrite. AI Elements is the fallback since it comes from Vercel, matches the same stack, and would be the least risky swap if assistant-ui stalls as a small startup.

#### Operations dashboard stack

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Next.js + shadcn/ui + Tremor | Vercel (Tremor acquired Jan 2025) | United States | MIT / Apache-2.0 (all Tremor components and blocks now free open source) | Free |
| Grafana OSS | Grafana Labs | United States | AGPL-3.0 | Free self-hosted |
| Appsmith | Appsmith | United States | Apache-2.0 | Free self-hosted; paid business tier |
| Retool | Retool | United States | Proprietary | Free tier, then per-user monthly |

Keep the stack that already works. The founder has Next.js 16 dashboards live for Kotana today, and Tremor going fully free and open source after the Vercel buy means 300 ready chart blocks in the exact same React and Tailwind world, at zero cost. No new server, no new login, no ranking of tools over what is proven. Grafana OSS is the fallback for the machine-level view: it self-hosts on the Hetzner box for free and covers systemd timers, disk, and service health with real alerting, which a product dashboard should not have to reinvent.

#### Human approval UX for agent actions

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| AG-UI protocol via CopilotKit | CopilotKit Inc. | United States | MIT (open protocol and SDK) | Free self-hosted |
| HumanLayer | HumanLayer (YC) | United States | Open source SDK (Apache-2.0); hosted service proprietary | Free tier around 1000 operations per month, then paid |
| gotoHuman | gotoHuman | Germany | Proprietary SaaS | Usage-based with free tier |
| LangGraph interrupt | LangChain | United States | MIT | Free self-hosted |

The founder already has a decision dock with approve and hold buttons. The gap is a standard wire format so every agent in the fleet can raise a hand the same way. AG-UI is that wire: MIT, free, self-hosted, US-made, and now backed by the big cloud vendors and the frameworks already in the stack, so the dock becomes a renderer of a standard event stream instead of a one-off. Each approval card can show evidence, expected result, and downside, which matches how this founder gates work. HumanLayer is the fallback for the away-from-keyboard case: its free tier pushes approvals to email or Slack when nobody is watching the dashboard, which suits a solo operator who sleeps.

#### Voice interface

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Pipecat | Daily | United States | BSD-2-Clause | Free open source; pay only for any hosted STT or TTS you plug in |
| LiveKit Agents | LiveKit | United States | Apache-2.0 | Free self-hosted; LiveKit Cloud usage-priced |
| Piper TTS (community fork) | Rhasspy community (originated by Michael Hansen) | United States | GPL-3.0 (active fork); archived original was MIT | Free |
| OpenAI Realtime API | OpenAI | United States | Proprietary | Usage-priced per audio minute and tokens |

Pipecat wins because it runs the whole voice loop on hardware the founder already owns. Local Whisper for ears and Piper for the mouth means zero dollars per minute and no cloud outage between a blind user and the assistant, which matters for the accessibility North Star. It is BSD licensed, US-made, Python, and pipeline-shaped, so it drops into the existing Flask and systemd world on the Hetzner box. Vendor swaps are one-line changes, so an OpenAI Realtime lane can be added later just for premium moments. LiveKit Agents is the fallback: same ally origin and Apache license, and the better choice if the product ever needs real phone calls or multi-party rooms.

#### Document and artifact generation (decks, reports)

| Candidate | Vendor | Origin | License | Pricing |
|---|---|---|---|---|
| Typst | Typst GmbH | Germany | Apache-2.0 (compiler and CLI) | Free CLI; optional paid web app |
| PptxGenJS | Open source (Brent Ely and community) | United States | MIT | Free |
| Marp | Marp team (Yuki Hattori) | Japan | MIT | Free |
| Pandoc | Open source (John MacFarlane) | United States | GPL-2.0-or-later | Free |

Agents write plain text far better than they drive drawing APIs, and Typst compiles plain text into clean, branded PDF reports in milliseconds on the Hetzner box. It is Apache licensed, EU-made, and free, so daily briefs, family finance reports, and WAR-style documents become one templated pipeline any fleet agent can feed. PptxGenJS stays as the fallback rather than being replaced: military and enterprise audiences need real editable PPTX files, the founder already has working scripted deck builds on it, and it is MIT and free. Typst for anything read as a page, PptxGenJS for anything presented as slides.

### L7 verifier notes (claims corrected by the fact check pass)

- **HumanLayer:** License and pricing check out: SDK is Apache-2.0 on GitHub, free tier of 1000 operations/month confirmed, YC F24 (US, founder Dex Horthy). BUT the company has pivoted: its flagship is now CodeLayer, an IDE for orchestrating AI coding agents ($100/user/month Pro), built on Claude Code. The original approval SDK remains open source but is no longer the company's primary product, so long-term support of the hosted approval service (the exact capability this fallback recommendation relies on) is a real continuity risk. The whitepaper should flag this pivot and consider gotoHuman (Germany) or LangGraph interrupt as the async-approval fallback.

**Synergy:** This stratum is the canonical human in the loop writeup: the dock, AG-UI as the wire, gotoHuman or HumanLayer only if a hosted inbox is ever wanted. L4 routing cross references here.

---

## The two axes

The axes are not extra strata; they are how the whole stack is measured and constrained. The Observability & Evaluation axis is carried by the OTel GenAI semantic conventions: every stratum emits spans on that wire, and Langfuse, DeepEval, and the cost line all read from it. The Governance & Trust axis is carried by the policy chain: OPA answers whether an action is allowed, LiteLLM answers whether it is affordable, the decision dock answers whether a human approves, and Langfuse keeps the audit trail that proves it all happened. When a new tool is evaluated, the two axis questions are simply: does it emit the spans, and does it pass through the gates.

## S0 Sovereignty and the degraded mode

S0 is invoked only when residency or ownership changes the design. For {a}OS it means one commitment: **the stack must degrade to a fully local lane when frontier providers or the network are unavailable.** That lane exists in this paper by construction: llama.cpp with ally origin open weights keeps reasoning alive, Nomic Embed keeps retrieval alive, Qdrant and SQLite hold knowledge, faster-whisper and Kokoro keep the voice interface up, and the file floor keeps coordinating. Slower and dumber, but standing, and for an assistive OS that a family depends on, standing is the requirement.

## Open gaps (the next decisions, from the completeness critic)

- High throughput inference server: when a GPU is ever rented for real load, vLLM is the serving layer; llama.cpp covers CPU edge only.
- Fine tuning posture: stated plainly, we do not fine tune today; when we do, it is LoRA via Axolotl or Unsloth on rented GPU, never a new subscription.
- Reranker: retrieval currently ships without rerank; the ally clean options are Cohere Rerank (Canada, metered) or a self hosted cross encoder; decide when RAG quality gates a product.
- Fresh web retrieval: agents need a search and crawl lane; SearXNG self hosted plus Crawl4AI or Firecrawl is the zero to low cost default.
- Event bus: if multi agent traffic outgrows the file floor, NATS is the ally clean substrate; adopt only on measured need.
- External synthetic probe: Healthchecks.io catches dead loops, but nothing yet checks the stack from outside the box; a minimal external uptime probe closes the known monitoring gap.
- PII detection and redaction: Microsoft Presidio self hosted covers the DLP job the guardrail picks do not.
- MCP supply chain vetting: third party MCP servers need a trust gate before install; treat every new server as untrusted code and review it like a dependency.
- Agent identity and credential brokering: Infisical stores secrets, but runtime issuance of scoped, short lived agent credentials is an open design job.
- Outbound paging: the approval dock exists but no channel reliably reaches the founder; ntfy self hosted or Pushover is the cheap fix, and it also closes the dead alert channel wound.
- Accessibility tooling: for an assistive OS, axe-core in CI and a screen reader pass on every L7 surface should be a shipped gate, not an aspiration.

## Appendix A ,  Method

Seven research agents (one per stratum) each compared 2 to 4 real candidates per job with live web search in July 2026. Seven adversarial verifiers then re searched every primary and fallback claim: origin country, license, pricing, and whether the product still exists under that name. A completeness critic swept the full set for gaps, policy leaks, and duplicates. 38 jobs, roughly 120 candidates, 23 corrections applied. The corrections are kept visible below because honesty is the brand.

## Appendix B ,  Corrections ledger (what the verifiers changed)

- **L1 / llama.cpp:** claimed "Vendor ggml.ai (Georgi Gerganov), origin Bulgaria (EU)"; verified: Gerganov is Bulgarian (correct), but Gerganov and the ggml.ai team joined Hugging Face (US) in February 2026; repo lives under the ggml-org GitHub organization. Vendor line is stale.
- **L1 / Gemma 3 4B (named in llama.cpp primary):** claimed "Google (US) ally-policy-clean open model for GGUF use"; verified: US origin and GGUF availability confirmed, but Gemma 3 is under the custom 'Gemma Terms of Use' with use restrictions, not MIT/Apache; do not describe the llama.cpp pairing as fully open-licensed.
- **L1 / OpenAI GPT Image (1.5 and Mini):** claimed "Product still current and safe to recommend as primary"; verified: Both gpt-image-1.5 and gpt-image-1-mini are scheduled for API removal on December 1, 2026, with GPT Image 2 as the recommended replacement. Recommending a model four months from removal as the primary is a defect,  the whitepaper should name GPT Image 2 (or 'current GPT Image tier') instead.
- **L1 / OpenAI GPT Image (1.5 and Mini):** claimed "$0.005 per image (Mini) to $0.04 (full quality)"; verified: Mini from ~$0.005/image is confirmed, but full-quality GPT Image 1.5 at 1024x1024 runs ~$0.133/image (low quality ~$0.009). The $0.04 'full quality' ceiling understates real cost by ~3x.
- **L1 / FLUX family (Black Forest Labs):** claimed "$0.008 to $0.04 per image on aggregators; Flux 2 Pro $0.055 direct"; verified: BFL's own pricing lists FLUX.2 [pro] at ~$0.03 per megapixel (~$0.030 for a 1MP image), not $0.055; aggregator per-image prices span roughly $0.003 (schnell on Replicate) to $0.06 depending on model/resolution.
- **L1 / GPT-5.5 (candidate only, not primary/fallback):** claimed "Exists as OpenAI's current frontier model at $5/$30"; verified: Out-of-scope candidate flagged in passing: no 'GPT-5.5' appears in July 2026 rankings; OpenAI's current flagship on Artificial Analysis is GPT-5.6 Sol. The candidate row likely names a nonexistent or superseded model.
- **L2 / Haystack:** claimed "Free open source; deepset AI Platform is paid"; verified: Free Apache-2.0 open source confirmed, and a paid commercial offering exists, but it has been renamed: now the Haystack Enterprise Platform (formerly deepset Cloud / deepset AI Platform). Whitepaper should use the current name.
- **L2 / Marker:** claimed "License: Apache 2.0 code; model weights Open Rail-M, free under 2M USD revenue"; verified: The code is GPL-3.0-or-later, not Apache 2.0,  the repo's pyproject.toml and README at datalab-to/marker both say GPL (one third-party aggregator says Apache 2.0, but the repo's own files are authoritative). Weights are under a Modified AI Pubs OpenRAIL-M with a FUNDING AND revenue cap (sources conflict on $2M vs $5M; the current README is cited at $5M). The axis-note claim that 'Marker relicensed to Apache 2.0 code' is wrong. GPL is a materially different obligation than Apache for anything distributed.
- **L3 / Anthropic computer use tool:** claimed "Current tool version 'computer_use_20251124' with zoom support; standard Claude token pricing plus roughly 466-499 system prompt tokens; Anthropic, US origin, commercial API"; verified: The tool type identifier is 'computer_20251124', not 'computer_use_20251124'. Everything else checks out: it is the newest computer-use tool version, adds the zoom action (enable_zoom), adds 466-499 tokens to the system prompt (plus ~735 input tokens for the tool definition on Claude 4.x), uses standard token pricing, and is available on current Claude models. Vendor Anthropic is US origin.
- **L4 / Pydantic AI:** claimed "Origin: United States (vendor Pydantic Services Inc.)"; verified: Pydantic Services Inc. is headquartered in London, England, UK (Crunchbase/Tracxn; founder-CEO Samuel Colvin is London-based). US-incorporated 'Inc.' with Sequoia (US) backing, but the company base is the UK. Allied origin either way,  no policy issue, but the whitepaper's 'United States' label is wrong.
- **L4 / LangGraph:** claimed "License: MIT"; verified: The langgraph library itself is MIT (confirmed), but the langgraph-api server runtime used for self-hosted production deployments is Elastic License 2.0 and needs a commercial key,  the blanket 'MIT' label does not cover the Platform runtime. Fine for the recommended library-only use, but the whitepaper should footnote this.
- **L4 / Claude Code Agent Teams:** claimed "Exists as a Claude Code feature (lead plus teammates, shared task list, direct teammate messaging)"; verified: The feature is real and matches the description (code.claude.com/docs/en/agent-teams), but it is EXPERIMENTAL and disabled by default (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1), with documented limitations around session resumption, task coordination, and shutdown. The research presents it as a production-ready primary without flagging experimental status.
- **L4 / Windmill:** claimed "Origin: United States (French founder)"; verified: Company profiles (Tracxn) list Windmill Labs as based in Paris, France, founded 2021 by Ruben Fiszel (Paris-born, EPFL). It is YC-backed so a US Delaware entity likely exists, but the operating base is France, not the US. Allied origin either way,  no policy issue.
- **L4 / Cronicle:** claimed "Exists under this name, not deprecated or renamed"; verified: Cronicle still exists and is maintained, but the vendor has shipped its successor xyOps ('Cronicle v2', 1.0 launched end of 2025, xyops.io) and Cronicle is now effectively in maintenance mode (bug fixes and security patches only, per PixlCore). As a fresh-adoption fallback the research should either name xyOps or flag Cronicle's legacy status.
- **L4 / gotoHuman:** claimed "Pricing: usage-based with a free tier"; verified: Free tier confirmed ($0/mo, 1 user, up to ~300 reviews/month), but current pricing at gotohuman.com/pricing is tiered seat-based, not usage-based: Team $99/mo (6 seats), Growth $350/mo, Business $950/mo. Budget note: the first paid tier ($99/mo) alone exceeds the stated $80/mo spend posture if the free tier is outgrown.
- **L4 / HumanLayer SDK:** claimed "Exists; company focus has shifted to CodeLayer, treat SDK maintenance as a risk"; verified: Stronger than a 'risk': the humanlayer/humanlayer repo itself states the HumanLayer SDK 'is being superseded by CodeLayer', and the repo's headline product is now CodeLayer (an AI-coding IDE). The SDK remains Apache 2.0 and usable but is vendor-declared legacy,  the whitepaper's framing understates this for a fallback recommendation.
- **L4 / L4 stratum policy sweep:** claimed "Every recommended vendor is US, EU, or Japan origin, satisfying the ally-only policy"; verified: No Chinese-origin products found among the 10 primaries/fallbacks (verified vendors: UK, US, France, Germany, Japan),  zero banned-list hits, so the policy outcome holds. But the sentence as written is inaccurate on two entries: Pydantic AI is UK-based (US claimed) and Windmill is France-based (US claimed); UK is also not 'US, EU, or Japan' post-Brexit, so the blanket wording needs amending even though all origins are allied.
- **L5 / Langfuse (self-hosted):** claimed "Origin: Germany (EU), vendor Langfuse GmbH, parent now US after ClickHouse Inc acquisition"; verified: Substance confirmed: Berlin, Germany company (YC W23) acquired by ClickHouse Inc (US) on Jan 16, 2026, alongside ClickHouse's $400M Series D. Minor fix: the legal entity is Finto Technologies GmbH operating as Langfuse, not 'Langfuse GmbH'.
- **L5 / Arize Phoenix:** claimed "Pricing: free to self-host with no usage limits; Phoenix Cloud paid tiers"; verified: Free self-hosting with no feature gates or caps is confirmed. Minor fix: the paid managed ladder is branded Arize AX in 2026 (AX Free $0, AX Pro $50/month, AX Enterprise custom); Phoenix Cloud itself offers free hosted instances. 'Phoenix Cloud paid tiers' slightly misnames the paid product.
- **L5 / promptfoo:** claimed "Vendor: Promptfoo Inc, United States, independent company"; verified: US origin (San Francisco) confirmed, but the vendor status is stale: OpenAI announced acquisition of Promptfoo on March 9, 2026, integrating it into OpenAI Frontier. OpenAI publicly committed the tools remain open source under the current license. Note the research penalized Helicone for exactly this acquisition-durability risk while missing promptfoo's own acquisition; fallback durability rationale should be updated.
- **L5 / Healthchecks.io:** claimed "Pricing: hosted free tier with 20 checks; paid from about 17 to 20 USD per month; free to self-host"; verified: Free tier of 20 checks and free self-hosting confirmed, but the paid ladder is $5/month Supporter (same limits), $20/month Business (100 checks), $80/month Business Plus (1000 checks). Cheapest paid entry is $5, not ~$17; the ~$17-20 figure only fits the Business tier.
- **L6 / Langfuse (primary, audit logging),  'strongest MIT licensed audit trail' framing:** claimed "Rationale presents Langfuse sessions/traces as the MIT-licensed audit trail for governance events."; verified: Core OTel tracing (sessions, users, tool spans) is genuinely MIT and free without limits, and does serve as the agent-action audit trail. But Langfuse's named 'Audit Logs' feature,  plus Data Retention Policies and server-side data masking,  sits in the commercial EE tier (langfuse.com/self-hosting/license-key, github.com/orgs/langfuse/discussions). For an L6 governance stratum the whitepaper should state that platform-level audit logs and retention policy enforcement require a paid Langfuse license, or fall to OpenBao/Phoenix-side compensating controls.
- **L7 / HumanLayer:** claimed "HumanLayer (YC, United States); open source SDK Apache-2.0, hosted service proprietary; free tier ~1000 operations/month then paid; approval-routing product active under that name"; verified: License and pricing check out: SDK is Apache-2.0 on GitHub, free tier of 1000 operations/month confirmed, YC F24 (US, founder Dex Horthy). BUT the company has pivoted: its flagship is now CodeLayer, an IDE for orchestrating AI coding agents ($100/user/month Pro), built on Claude Code. The original approval SDK remains open source but is no longer the company's primary product, so long-term support of the hosted approval service (the exact capability this fallback recommendation relies on) is a real continuity risk. The whitepaper should flag this pivot and consider gotoHuman (Germany) or LangGraph interrupt as the async-approval fallback.
