# 6.aOS — {a}OS Agentic Operating System

> The canonical home for the **{a}OS 6-Layer AI/ML Reference Model**, vendor mappings, architecture research, and the LinkedIn training series that teaches it.

## What Is {a}OS?

{a}OS-6L is a **vendor-neutral, 6-layer reference model** for describing, building, debugging, and governing AI/ML systems — inspired by the OSI networking model. It gives teams a shared operating language that works across Azure AI Foundry, AWS Bedrock, Vertex AI, OpenAI, Anthropic, Palantir, and internal enterprise platforms.

## Repo Structure

| Folder | Purpose |
|--------|---------|
| `00.Governance` | Repo rules, contribution guidelines, versioning |
| `01.Reference-Model` | The {a}OS-6L layer definitions, glossary, design principles |
| `02.Vendor-Mappings` | Platform-specific mappings (Azure AI Foundry, AWS, etc.) |
| `03.Research` | Deep research briefs supporting the model and training content |
| `04.LinkedIn-Series` | LinkedIn training series plans, briefs, and editorial guidance |
| `05.Architecture` | Enterprise architecture patterns built on {a}OS layers |
| `.ai` | Agent context files |

## The Six Layers

| Layer | Name | Scope |
|-------|------|-------|
| **L6** | Human Intent, Policy & Oversight | Governance, approval gates, human-in-the-loop |
| **L5** | Orchestration, Workflows & Routing | Multi-agent coordination, task decomposition |
| **L4** | Agent Logic, Skills & Execution Reasoning | Individual agent behavior, skill invocation |
| **L3** | Tools, Interfaces & External Actions | API calls, MCP servers, external integrations |
| **L2** | Context, Memory & Semantic State | RAG, vector stores, conversation history |
| **L1** | Models, Data & Compute Foundation | LLMs, fine-tuning, infrastructure |

## Status

- **Model version:** v0.1 (pre-release)
- **First vendor mapping:** Azure AI Foundry (April 2026)
- **LinkedIn series:** In design (April 2026)
