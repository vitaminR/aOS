---
post_id: AFS11
date: 2026-04-28
topic: "Phase 1: What to Actually Build First"
series_name: "Building an AI Platform That Actually Ships"
series_part: 11
series_total: 12
character: Mentor Architect
structure: Sequenced Implementation Playbook
tone: Deadpan, first-person, self-implicating, "tired architect"
hashtag_count: 5
status:
  ideate: READY
---

## Topic

Concrete, sequenced implementation plan for the first 90 days of an Azure AI Foundry platform build. What to deploy in Phase 1 whether you have a team of 5 or 50. Identity, networking, one model, one agent, cost metering, IaC. Not a model catalog. Not multi-agent. Not RAG. Absorbs the cut IaC post and environment separation content from the original series plan.

## Why Now

This is post 11 of 12. The audience has absorbed architecture, governance, identity, networking, models, agents, RAG, cost, and observability. They need the "so what do I build on Monday" post. Everything prior was theory and checklists. This is the playbook.

## Character Selection

**Mentor Architect** — the practical playbook voice. "Here is what I would tell you to build in the first 90 days." This is the post people save and forward to their team leads. Concrete, sequenced, scoped tight. No fear-mongering, no cheerleading. Just the build order.

## Structure & Tone

- Open with a confession about over-scoping Phase 1
- Lay out the 90-day sequence in clear blocks
- Reference architecture as resource group taxonomy
- Land on Bicep/CLI as deployment method, not portal
- Close with "scope is the strategy" energy
- No fluff, no analogies beyond one or two — just the build list

## Hashtags

1. #AzureAIFoundry
2. #PlatformEngineering
3. #InfrastructureAsCode
4. #AIArchitecture
5. #Bicep

## Key Claims

1. Phase 1 is identity + networking + one model + one agent + cost metering + IaC. Six things. Not twelve.
2. Deploy via Bicep/CLI, not the portal. Portal drift kills reproducibility by week three.
3. Separate Foundry resources per environment. One hub for dev, one for staging, one for prod.
4. Start with prompt agents only. Multi-agent and RAG are Phase 2 problems.
5. APIM as AI Gateway from day one for cost attribution and rate limiting.
6. Fork the foundry-samples Bicep templates. Do not write from scratch.
7. Block Bing/Web/SharePoint grounding via Azure Policy in prod from the start.
8. Plan for two resource models (classic and new) but build on classic for network isolation today.

## Anti-Slop Checklist

- [ ] No "game-changer," "unlock," "revolutionize," "dive into," "let's explore"
- [ ] No "Part X of Y" meta-language
- [ ] No emoji in body copy
- [ ] Engagement prompt in FIRST COMMENT only
- [ ] Word count 250-350
- [ ] First person, self-implicating opening
- [ ] Receipts before thesis
- [ ] No corporate cheerleading for Azure — just what works and what breaks

## Engagement Prompt

"What did your Phase 1 look like? Was it scoped tight, or did scope creep hit before you shipped value?"

## Visual Direction

Phase 1 architecture diagram showing the minimal viable platform: resource group taxonomy (ai-networking, ai-prod, ai-staging, ai-dev, ai-governance, ai-shared) with key resources in each. Clean, dark-themed, {a}OS branded. Bicep template reference callout. Think infrastructure documentation, not marketing.

## Content Source

- Azure AI Foundry reference architecture (series plan section 3.1)
- Microsoft foundry-samples Bicep templates (00-basic, 19-hybrid-private-resources-agent-setup)
- Posts AFS01-AFS10 (cumulative dependency — this post sequences everything prior)
- Cut IaC post content absorbed into this post
- Cut environment separation content absorbed into this post
