# APR004 — Research Notes: {a}OS 6-Layer AI/ML Model

## Problem Statement

The AI/ML industry lacks a universal reference architecture for describing system components. Multiple platforms use different terminology for equivalent concepts:

| Concept | Azure / Semantic Kernel | LangChain / LangGraph | Anthropic / Claude |
|---|---|---|---|
| Callable unit | Tool / Skill | Tool | Tool use |
| Autonomous decision-maker | Agent | Agent / Graph | Agent |
| Context window | Memory / State | Memory | Context |
| Control layer | Orchestrator / Kernel | Router / Graph | System prompt |

This vocabulary collision creates:

- Miscommunication across vendor boundaries
- Debugging friction ("Where does this failure live?")
- Onboarding tax for engineers switching ecosystems

## Prior Art

- **OSI Model (networking)**: 7-layer reference that gave networking a shared vocabulary. Direct inspiration for {a}OS-6L.
- **TOGAF / Zachman (enterprise architecture)**: Heavy frameworks that work for governance but are too abstract for AI system debugging.
- **MLOps maturity models**: Focus on ML lifecycle (training → deployment → monitoring) but don't cover agentic orchestration, memory, or human oversight.
- **Anthropic's agent patterns**: Practical but vendor-specific. No formal layering.
- **Microsoft Semantic Kernel / AutoGen**: Implementation frameworks, not reference architectures.
- **MCP (Model Context Protocol)**: Standardizes tool interfaces (L3 in {a}OS) but doesn't address the full stack.

## The {a}OS-6L Model

| Layer | Name | Scope |
|---|---|---|
| L6 | Human Intent, Policy & Oversight | Governance, approval gates, human-in-the-loop |
| L5 | Orchestration, Workflows & Routing | Multi-agent coordination, task decomposition |
| L4 | Agent Logic, Skills & Execution Reasoning | Individual agent behavior, skill invocation |
| L3 | Tools, Interfaces & External Actions | API calls, MCP servers, external integrations |
| L2 | Context, Memory & Semantic State | RAG, vector stores, conversation history |
| L1 | Models, Data & Compute Foundation | LLMs, fine-tuning, infrastructure |

## Design Principles

1. **Vendor-neutral**: No platform-specific terminology in layer names
2. **Debuggable**: "This is a Layer 3 issue, not a Layer 1 issue" should be a complete sentence
3. **Additive to existing frameworks**: Designed to coexist with MLOps, TOGAF, etc.
4. **Minimal**: 6 layers, not 12. Enough to be useful, few enough to memorize

## Key Analogy

The OSI Model succeeded because it gave networking engineers a shared language. When someone says "Layer 2 issue," every network engineer knows it's about data link / MAC addressing, not about a routing problem (Layer 3) or an application bug (Layer 7). The {a}OS-6L model aims for the same diagnostic precision in AI/ML systems.

## Sources

- Author's direct experience building multi-agent systems across Azure, OpenAI, Anthropic
- OSI Model analogy (ISO 7498-1)
- Industry observation: vocabulary collision across vendor docs (2024-2026)
- MCP specification (Anthropic, 2024-2025)
