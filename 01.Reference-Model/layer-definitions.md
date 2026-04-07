# {a}OS-6L Reference Model — Layer Definitions

> **Version:** v0.1 (pre-release)
> **Date:** 2026-04-06
> **Status:** Internal working draft — not yet publicly released

---

## Design Principles

1. **Vendor-neutral** — No platform-specific terminology in layer names
2. **Debuggable** — "This is a Layer 3 issue" must be a complete, useful sentence
3. **Additive** — Coexists with MLOps, TOGAF, and existing enterprise frameworks
4. **Minimal** — 6 layers. Enough to be useful, few enough to memorize.

## Inspiration

The OSI Model (ISO 7498-1) succeeded because it gave networking engineers a shared language. When someone says "Layer 2 issue," every network engineer knows it's about data link / MAC addressing — not routing (L3) or application bugs (L7).

The {a}OS-6L model provides the same diagnostic precision for AI/ML systems.

---

## The Six Layers

### L6 — Human Intent, Policy & Oversight

**Scope:** Governance, approval gates, human-in-the-loop, compliance enforcement, policy engine, audit trail, budget controls

**Who owns it:** Leadership, compliance officers, program managers

**Diagnostic signal:** "The system did something it shouldn't have been allowed to do" → L6 issue

**Examples:**

- Approval workflow before agent sends external communication
- Cost budget enforcement (kill switch at $X/day)
- Compliance reporting for FedRAMP audit
- Human review gate for high-risk agent actions

---

### L5 — Orchestration, Workflows & Routing

**Scope:** Multi-agent coordination, task decomposition, routing decisions, circuit breakers, load balancing, workflow state management

**Who owns it:** Platform engineers, orchestration architects

**Diagnostic signal:** "The wrong agent got the task" or "The workflow hung" → L5 issue

**Examples:**

- Router selects model based on task complexity and cost
- Circuit breaker kills runaway agent loop
- Multi-agent pipeline: research → analysis → formatting
- Workflow state machine with retry logic

---

### L4 — Agent Logic, Skills & Execution Reasoning

**Scope:** Individual agent behavior, skill invocation, reasoning chains, prompt engineering, agent-level decision making

**Who owns it:** AI engineers, prompt engineers, agent developers

**Diagnostic signal:** "The agent made a bad decision" or "The skill didn't execute correctly" → L4 issue

**Examples:**

- Agent selects wrong tool for the task
- Prompt engineering produces inconsistent results
- Skill execution fails due to malformed input
- Agent reasoning chain hallucinates intermediate steps

---

### L3 — Tools, Interfaces & External Actions

**Scope:** API calls, MCP servers, function calling, external integrations, database queries, file operations

**Who owns it:** Backend engineers, integration specialists

**Diagnostic signal:** "The API call failed" or "The tool returned unexpected data" → L3 issue

**Examples:**

- MCP server connection timeout
- Function call returns malformed JSON
- External API rate limit hit
- Database query returns stale data

---

### L2 — Context, Memory & Semantic State

**Scope:** RAG pipelines, vector stores, conversation history, semantic search, context window management, memory lifecycle

**Who owns it:** Data engineers, ML engineers, knowledge architects

**Diagnostic signal:** "The system didn't know something it should have" or "The context was wrong" → L2 issue

**Examples:**

- RAG retrieves irrelevant documents
- Context window overflow drops critical information
- Vector embeddings are stale or misaligned
- Cross-session state is lost

---

### L1 — Models, Data & Compute Foundation

**Scope:** LLMs, fine-tuning, infrastructure, model hosting, encryption, compute resources, networking

**Who owns it:** Infrastructure engineers, ML platform team, cloud architects

**Diagnostic signal:** "The model is slow/wrong/unavailable" or "The infrastructure is down" → L1 issue

**Examples:**

- Model deployment in wrong region
- GPU capacity insufficient for PTU commitment
- Encryption key rotation breaks model access
- Network isolation misconfiguration blocks inference
