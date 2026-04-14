---
post_id: AFS07
title: "Agent Maturity: What's GA, What's Preview, What Matters"
topic: "Three agent types in Azure AI Foundry, their maturity levels, and what's actually safe for production"
date: 2026-04-21
series_name: "Building an AI Platform That Actually Ships"
series_part: 7
series_total: 12
character: Mentor Architect
structure: "D8 #4 — Builder"
tone: "D3 #3 — Tired Architect"
status: "draft:COMPLETE"
art_status: "IMAGE_PENDING"
word_count: 297
publish:
  banner_text: "Building an AI Platform That Actually Ships"
---

# AFS07 — Agent Maturity: What's GA, What's Preview, What Matters

## Strategy Notes

- Tech post (odd-numbered). Mentor Architect voice — experienced guide, protective, not condescending.
- Voice: first person, self-implicating, short fragments, deadpan. "Here's what I'd tell you over coffee."
- The post teaches the maturity spread across three agent types, then gives a clear production rule.
- Do NOT lecture. The Mentor Architect has been burned. They're saving you time, not showing off.
- Engagement prompt goes in first comment, NOT in post body.
- No "Part 7 of 12." Post stands alone.

## Copy/Paste

I have a simple rule for agents in production.

If it's GA, build on it. If it's preview, prototype on it. If you're promising a production date on a preview feature, start writing the apology email now.

Azure AI Foundry has three agent types. They share the same identity model, the same project context, and the same portal. They do not share the same maturity. Not even close.

Prompt agents are GA. Full VNet support. Per-agent Entra identity. Your agent authenticates as itself, not as the deploying user. RBAC scoped per agent. Audit trail shows which agent did what. This is production-ready and genuinely well-designed.

Workflow agents are preview. Multi-step orchestration, branching, conditional logic. Useful. But VNet support is inbound only — your agent can receive requests from inside the network, outbound calls may not stay there. The orchestration graph format is not guaranteed stable. I have rebuilt two prototypes after preview API changes. Budget for that.

Hosted agents are preview. Container-based, long-running, persistent state. Interesting architecture. No VNet support at all. None. If your compliance team requires network isolation, this is not a configuration problem. It is a "not yet" problem.

One more thing. Publishing any agent to Teams or M365 requires a public endpoint. If you enforced VNet isolation for compliance reasons, that is a direct conflict. Not a bug — Teams requires public reachability by design.

Here is the rule: build your first production value on prompt agents. Prototype the rest. Never bet your ship date on preview stability.

# EnterpriseAI #AIArchitecture #AzureAI #AIAgents #ProductionAI

---

## Editorial Notes

- ~297 words. Within LinkedIn optimal range (250-350).
- Voice matches series pattern: short fragments, first person, self-implicating ("I have rebuilt two prototypes"), deadpan understatement ("start writing the apology email now").
- Structure: production rule (hook) -> three types with maturity (walkthrough) -> Teams conflict (bonus insight) -> rule restated (punch).
- Mentor Architect voice: protective, not condescending. "I have a simple rule" not "you should know."
- "I have rebuilt two prototypes after preview API changes. Budget for that." — scar tissue, not theory.
- The Teams/M365 public endpoint conflict is a bonus insight that rewards the reader for reading to the end.
- No {a}OS mention. No series numbering. Post stands alone.

## First Comment (post after publishing)

Are you building production workloads on preview features? What's your rollback plan when they change?
