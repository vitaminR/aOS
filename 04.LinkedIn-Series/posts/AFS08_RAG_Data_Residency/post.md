---
post_id: AFS08
title: "RAG and the Data Residency Question Nobody Asked"
topic: "Basic vs Standard agent storage, BYO storage, environment separation, and why regulated industries must decide before first deployment"
date: 2026-04-22
series_name: "Building an AI Platform That Actually Ships"
series_part: 8
series_total: 12
character: Architect
structure: "D8 #4 — Builder"
tone: "D3 #3 — Tired Architect"
status: "draft:COMPLETE"
art_status: "IMAGE_PENDING — needs Basic vs Standard storage comparison visual"
word_count: 320
publish:
  banner_text: "Building an AI Platform That Actually Ships"
---

# AFS08 — RAG and the Data Residency Question Nobody Asked

## Strategy Notes

- TECH post. Architect character. Hands-on, specific, slightly alarming.
- Covers two merged topics: (1) Basic vs Standard storage, (2) environment separation (absorbed from cut Post 11).
- This is the post that makes someone stop and check their Foundry configuration.
- By this point in the series, {a}OS has been introduced (Post 3) and the audience is familiar with the framework.
- Voice: First person, self-implicating, short fragments, deadpan. "I found this the hard way."
- Engagement prompt in first comment, NOT in post body.
- Foundry IQ preview status must be stated clearly.

## Copy/Paste

I deployed my first Foundry agent with the default storage configuration.

I did not ask where the documents went. I did not ask who managed the encryption keys. I did not ask whether the storage was shared with other tenants. I just uploaded the files and connected the retrieval pipeline.

That was a mistake.

Azure AI Foundry has two storage modes. "Basic" is the default. Microsoft-managed, multitenant, no customer-managed keys, no private endpoints on the storage layer. Your documents, your agent threads, your intermediate artifacts — all sitting in storage you do not control and cannot audit.

"Standard" gives you a BYO storage account. Customer-managed keys. Private endpoints. Visible in your subscription. Auditable.

The choice is made at provisioning time. Changing it later is a reprovisioning exercise, not a settings toggle.

If you handle PII, financial records, healthcare data, or anything under CMMC — "Basic" is not an option. You needed "Standard" before your first deployment.

There is a second thing nobody told me.

Projects inside a single Foundry resource share the parent's networking. Your dev project and your prod project share the same network boundary. Same blast radius. A misconfiguration in one affects the other.

Projects are organizational units. They are not environment boundaries. You need separate Foundry resources for dev, staging, and production.

One more: Foundry IQ, the managed RAG pipeline, is still preview. No SLA. Build your production retrieval on Azure AI Search with private endpoints. It is GA and it works inside the network boundary.

Check your storage configuration. Today.

# EnterpriseAI #AIArchitecture #AzureAI #DataResidency #AIGovernance

---

## Editorial Notes

- ~320 words. Within LinkedIn optimal range (250-350).
- Voice matches series pattern: short fragments, first person, self-implicating ("That was a mistake"), deadpan understatement.
- Structure: "I deployed with defaults" (hook) -> "two storage modes" (reveal) -> "Basic vs Standard" (walkthrough) -> "projects share networking" (env separation — absorbed from cut Post 11) -> "Foundry IQ is preview" (RAG caution) -> "Check your storage configuration. Today." (punch).
- Engagement prompt goes in first comment, NOT in post body — author pattern ends with a punch, not a question.
- Regulated-industry callout is explicit: "PII, financial records, healthcare data, or anything under CMMC."
- Foundry IQ preview status stated clearly — no implication it's GA.
- Environment separation content from cut Post 11 integrated naturally as "the second thing nobody told me."
- No "Part 8 of 12." Post stands alone.
- "Check your storage configuration. Today." — closing punch that drives action.

## First Comment (post after publishing)

Do you know whether your AI agent's data is stored in Microsoft-managed or customer-managed storage? Most teams I talk to don't — and it matters more than you think.
