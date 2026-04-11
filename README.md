# 6.aOS — {a}OS Agentic Operating System

> The canonical home for the **{a}OS Agentic Reference Stack**, vendor mappings, architecture research, and the LinkedIn training series that teaches it.

## What Is {a}OS?

{a}OS is a **vendor-neutral, 7-stratum reference model** for describing, building, debugging, and governing agentic AI systems — inspired by the OSI networking model. It gives teams a shared operating language that works across Azure AI Foundry, AWS Bedrock, Vertex AI, OpenAI, Anthropic, and internal enterprise platforms.

**One framework. Seven strata. Every AI system failure lives in one of them.**

## The 7 Canonical Strata

| Stratum | Name | Boundary Question |
|:---:|------|------|
| **L7** | Experience & Intent | *What is the user asking, seeing, approving, or rejecting?* |
| **L6** | Governance & Trust | *Who is allowed to do this, under what policy, with what risk and budget?* |
| **L5** | Observability & Evaluation | *What actually happened, how well did it perform, and where did it fail?* |
| **L4** | Orchestration & Decisioning | *What happens next, in what order, with which agent, under which stop conditions?* |
| **L3** | Execution & Interfaces | *What external action was invoked, against which interface, and what happened?* |
| **L2** | Knowledge & Memory | *What context did the system know, retrieve, remember, or forget?* |
| **L1** | Models & Infrastructure | *Is the model/runtime/compute/network foundation available and behaving correctly?* |

### Cross-Cutting Axes

| Axis | Strongest Home | Scope |
|------|:---:|------|
| Governance & Trust | L6 | Identity, access control, policy, safety, approvals, budget, audit, compliance |
| Observability & Evaluation | L5 | Tracing, logging, metrics, evals, drift detection, cost visibility |

### Optional

| | Name | When to use |
|---|------|------|
| **S0** | Sovereignty & Deployment Constraints | When residency, air-gap, tenancy, or classification materially change the design |

## Locked Vocabulary

| Term | Definition |
|------|-----------|
| **Stratum** | Top-level layer defining a stable responsibility boundary |
| **Axis** | Cross-cutting concern intersecting multiple strata |
| **Substrate** | Tools, frameworks, runtimes operating within a stratum |
| **Construct** | Meaningful artifact, state, or object produced by a substrate |
| **Primitive** | Smallest atomic unit used inside a construct |

## Repo Structure

| Folder | Purpose |
|--------|---------|
| `00.Governance` | Repo rules, contribution guidelines, versioning |
| `01.Reference-Model` | **Canonical standard:** `agentic-reference-stack-v1.md` |
| `02.Vendor-Mappings` | Platform-specific mappings (Azure AI Foundry, AWS, etc.) |
| `03.Research` | Deep research briefs supporting the model and series content |
| `04.LinkedIn-Series` | LinkedIn training series plans, briefs, and editorial guidance |
| `05.Architecture` | Enterprise architecture patterns built on {a}OS strata |
| `.ai` | Agent context files |

## Status

- **Framework version:** v1.0 (canonical, locked)
- **First vendor mapping:** Azure AI Foundry (April 2026)
- **LinkedIn series:** In production (April 2026)
- **Supersedes:** {a}OS-6L v0.1
