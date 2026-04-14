---
post_id: AFS02
title: "What Azure AI Foundry Actually Is (and Isn't)"
topic: "Demystifying Foundry — what it bundles, what changed in the rebrand, what the resource model actually looks like"
date: 2026-04-09
series_name: "Building an AI Platform That Actually Ships"
series_part: 2
series_total: 12
character: Architect
structure: "D8 #4 — Builder"
tone: "D3 #3 — Tired Architect"
status: "draft:COMPLETE"
art_status: "IMAGE_PENDING — needs resource model comparison table"
word_count: 282
publish:
  banner_text: "Building an AI Platform That Actually Ships"
---

# AFS02 — What Azure AI Foundry Actually Is (and Isn't)

## Strategy Notes

- Foundation post. Readers need to understand the platform before Post 3 evaluates it through the {a}OS lens.
- The hook is "the rebrand is not cosmetic." Most people assume name changes are marketing. This one changed the resource provider.
- Do NOT mention {a}OS — that is Post 3.
- Do NOT turn this into a feature list. Every feature serves the "two resource models" narrative.
- Include the `az provider show` verification command — gives readers an immediate action.
- Voice: Same as AFS01 — first person, receipts, self-implicating, deadpan.
- Engagement prompt in first comment, not body.
- Red-team: Verify "Microsoft Foundry" rebrand against live portal before publishing. If not confirmed, use "Azure AI Foundry" only. Post currently uses "Azure AI Foundry."

## Copy/Paste

I see the same question every week. "What actually is Azure AI Foundry?"

Fair question. The answer is more complicated than the marketing page suggests.

Foundry is a unified PaaS. It bundles a model catalog, an agent service, content safety, speech and vision tools, and a control plane with RBAC and networking. Most of that is GA. Some of it is preview. The catalog says 11,000 models. Realistically, about 50 to 100 Azure-hosted models matter for production.

But here is the part almost nobody talks about.

The rebrand from Azure AI Studio to Azure AI Foundry was not cosmetic. The resource provider changed. Classic runs on `Microsoft.MachineLearningServices`. New runs on `Microsoft.CognitiveServices`. Different ARM APIs. Different Bicep templates. Different RBAC surface.

Two resource models coexist right now. Classic uses Hub-to-Project topology. New uses Foundry Resource-to-Project. The classic model has more mature network isolation. The new model is where Microsoft is investing.

You have to pick one on day one. And it is not a toggle. Moving from classic to new is a resource migration.

Here is how to check which one you are on:

`az resource list --resource-type "Microsoft.CognitiveServices/accounts" -o table`

If that returns your AI resources, you are on the new model. If not, check `Microsoft.MachineLearningServices/workspaces`.

The rebrand was structural. Start wrong and you are migrating before you ship.

# AzureAI #AIArchitecture #CloudArchitecture #EnterpriseAI #AIPlatform

---

## Editorial Notes

- ~282 words. Within LinkedIn optimal range (250-350).
- Voice matches AFS01: short fragments, first person, deadpan. "Fair question." "Here is the part almost nobody talks about."
- Structure: "What is it?" (setup) → "The rebrand changed the resource provider" (contrarian reveal) → "Two models coexist" (architectural reality) → "Here's how to check" (verification) → "Start wrong and you're migrating" (punch).
- The verification command is a trust-builder — gives readers an immediate action they can take in their own subscription.
- No {a}OS mention. No "Part 2 of 12." Post stands alone.
- The "11,000 models → 50-100 matter" reframe is a mild contrarian move that builds credibility without bashing.
- "It is not a toggle" is the key line — counters the assumption that resource model choice is easily reversible.
- Post works for readers who did not see Post 1 — it is a standalone explainer.

## First Comment (post after publishing)

Are you using the classic Hub model or the new Foundry resource model? Run the command in the post and check. I'm curious how the split looks across teams actually building on this.

If you are evaluating Foundry for the first time — start with the new model unless you need VNet isolation today. That one sentence will save you a migration.
