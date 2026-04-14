---
post_id: AFS07
date: 2026-04-21
topic: "Agent Maturity: What's GA, What's Preview, What Matters"
series_name: "Building an AI Platform That Actually Ships"
series_part: 7
series_total: 12
character: Mentor Architect
structure: "D8 #4 — Builder (Hook → maturity reveal → type walkthrough → production rule → CTA)"
tone: "D3 #3 — Tired Architect"
hashtag_count: 5
status: ideate:READY
---

# AFS07 — Agent Maturity: What's GA, What's Preview, What Matters

## Topic

Technical deep-dive on the three Azure AI Foundry agent types (prompt, workflow, hosted), their maturity levels, VNet compatibility, and production readiness. The core message: prompt agents are the only GA, VNet-compatible, production-safe option. Everything else is preview with material constraints. Build first value on what's stable.

## Why Now

- Teams are adopting agents without checking maturity status — building production workloads on preview APIs
- Azure AI Foundry has three distinct agent types with materially different readiness levels
- Preview features can and do change APIs, drop capabilities, or lose support without notice
- Regulated environments need GA + VNet + audit trail — only one agent type delivers all three today
- Post 6 covered model economics; this post covers the next decision: which agent type to bet on

## Character Selection

**Mentor Architect** — This is protective guidance, not a lecture. The voice of someone who has seen teams burn months building on preview features that changed underneath them. Practical, slightly protective, "here's what I'd tell you over coffee."

## Structure & Tone

- **Structure:** D8 #4 — Builder (Hook → maturity reveal → type-by-type walkthrough → production rule → punch)
- **Tone:** D3 #3 — Tired Architect ("I've watched this happen enough times to have a simple rule")
- The post should feel like experienced advice, not documentation. The voice is someone saving you from a mistake they've already made.

## Hashtags (5)

# EnterpriseAI #AIArchitecture #AzureAI #AIAgents #ProductionAI

## Key Claims

1. Azure AI Foundry has three agent types: prompt, workflow, and hosted — with materially different maturity
2. Only prompt agents are GA with full VNet support and production readiness
3. Workflow agents are preview with partial VNet (inbound only) — not ready for regulated production
4. Hosted agents are preview with no VNet support at all — not ready for regulated production
5. Agent identity (per-agent Entra identity) is a strong feature across all types, but maturity still gates production use
6. Publishing agents to Teams/M365 requires public endpoints — a VNet conflict in isolated environments
7. The production rule: build first value on GA, prototype on preview, never bet your timeline on preview stability

## Anti-Slop Checklist

- [ ] No vendor bashing — Azure is genuinely strong here; the point is maturity, not criticism
- [ ] No "just" or "simply" — respect the deployment complexity
- [ ] No feature laundry list — focus on maturity levels and production impact
- [ ] No "Part 7 of 12" — post stands alone
- [ ] No percentage claims
- [ ] Engagement prompt in first comment, not body
- [ ] Voice is mentor, not lecturer — protective, not condescending

## Engagement Prompt

Are you building production workloads on preview features? What's your rollback plan when they change?

## Visual Direction

Agent type maturity matrix: 3 rows (Prompt / Workflow / Hosted) x 4 columns (Status / VNet Support / Entra Identity / Production Readiness). Clean table with green/yellow/red indicators.

## Content Source

Author-provided research and experience. Research base in `c:\Users\nymil\Codepro\6.aOS\03.Research\azure-ai-foundry-enterprise-defense.md`.
