---
post_id: AFS11
title: "Phase 1: What to Actually Build First"
topic: Concrete 90-day implementation plan for Azure AI Foundry platform
date: 2026-04-28
series_name: "Building an AI Platform That Actually Ships"
series_part: 11
series_total: 12
character: Mentor Architect
structure: Sequenced Implementation Playbook
tone: Deadpan, first-person, self-implicating
status:
  draft: COMPLETE
  art_status: IMAGE_PENDING
word_count: 322
publish:
  banner_text: "Phase 1 architecture diagram — minimal viable AI platform + Bicep reference"
---

## Strategy Notes

- Mentor Architect character: the practical playbook in 320 words
- Self-implicating open — admit the "build everything" mistake
- Six-item Phase 1 scope as the core structure
- Resource group taxonomy as the architecture skeleton
- Land on Bicep/CLI, kill portal deployments early
- Close with "scope is the strategy" — not a tagline, a survival tactic
- Engagement prompt goes in first comment only

---

## Copy / Paste

**Phase 1: What to Actually Build First**

Our first AI platform roadmap had 31 line items for Phase 1. Model catalog. Multi-agent orchestration. RAG pipelines with hybrid search. Custom evaluation frameworks. A self-service portal.

We shipped none of it.

Here is what I would tell you to build in the first 90 days. Six things. Not thirty-one.

**1. Identity.** Entra ID. Managed identities on every resource. RBAC roles assigned at project scope. API keys disabled. This is not optional infrastructure. It is the foundation everything else fails without.

**2. Networking.** Hub-spoke topology. Private endpoints on every AI service. DNS zones configured. A dev environment with relaxed networking so developers can actually iterate. Production locked down from day one.

**3. One model.** Deploy a single model behind a managed endpoint. GPT-4o, not a catalog of twelve options nobody has evaluated. One model, tested, monitored, with a prompt agent that does one thing well.

**4. One agent.** A prompt agent. Not multi-agent. Not agentic workflows with tool chains. A single agent calling a single model with a system prompt and a grounding source. Prove the platform works before you complicate it.

**5. Cost metering.** APIM as your AI Gateway from day one. Token tracking. Per-project attribution. Rate limiting. If you cannot answer "what did project X spend last week" by month two, you will lose your budget before Phase 2 starts.

**6. Infrastructure as Code.** Bicep or Terraform. Not the portal. Fork the foundry-samples templates from Microsoft. Start with the basic template, evolve toward the hybrid-private-resources setup. Portal drift will kill reproducibility by week three.

Your resource groups: ai-networking, ai-prod, ai-staging, ai-dev, ai-governance, ai-shared. Separate Foundry resources per environment. Block Bing and SharePoint grounding in prod via Azure Policy.

That is Phase 1. Everything else is Phase 2.

Scope is the strategy.

---

## Hashtags

# AzureAIFoundry #PlatformEngineering #InfrastructureAsCode #AIArchitecture #Bicep

---

## Editorial Notes

- Word count: 322 (within 250-350 target)
- No emoji in body
- No "Part X of Y" meta-language
- Self-implicating opening (31 line items, shipped none)
- Engagement prompt moved to first comment
- Absorbs cut IaC post content (Bicep/CLI, foundry-samples fork, portal drift warning)
- Absorbs cut environment separation content (resource group taxonomy, per-env Foundry resources)
- Dependencies on AFS04 (identity), AFS05 (networking), AFS06 (models), AFS07 (agents), AFS09 (cost) are implicit, not referenced directly
- "Scope is the strategy" is the closing line — earns saves

---

## First Comment

What did your Phase 1 look like? Was it scoped tight, or did scope creep hit before you shipped value?
