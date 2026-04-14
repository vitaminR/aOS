---
post_id: AFS04
title: "The Identity Layer Most Teams Skip"
topic: Entra ID, RBAC roles, managed identities in Azure AI Foundry
date: 2026-04-15
series_name: "Building an AI Platform That Actually Ships"
series_part: 4
series_total: 12
character: Regulator
structure: Checklist / Security Audit
tone: Deadpan, first-person, self-implicating
status:
  draft: COMPLETE
  art_status: IMAGE_PENDING
word_count: 298
publish:
  banner_text: "RBAC role comparison — 4 Foundry roles + risk level"
---

## Strategy Notes

- Regulator character: security review in 280 words
- Self-implicating open — admit the API key sin
- Four roles as quick reference, not deep dive
- Land on managed identities as the correct answer
- Close with urgency, not fear
- Engagement prompt goes in first comment only

---

## Copy / Paste

**The Identity Layer Most Teams Skip**

I found API keys in three .env files last Tuesday. All had Owner-level access to production Foundry resources. None had expiration dates.

This is the post I wish someone had forwarded me six months ago.

Azure AI Foundry ships four RBAC roles. Most teams use one. Here is what each actually grants:

**Azure AI User** — Data plane actions only. Can call models, read endpoints, run inference. Cannot create resources or manage access. This is your developer default.

**Azure AI Project Manager** — Everything User gets, plus user management within projects. For team leads who need to onboard people.

**Azure AI Account Owner** — Resource creation, model deployment, configuration. No data plane actions. For platform engineers building the infrastructure.

**Azure AI Owner** — Full control. Data plane. Control plane. Access management. Everything.

Owner is a loaded gun in production. If you cannot write a sentence justifying why someone needs it, they do not.

Now the part that keeps me up at night.

API keys bypass all of this.

Every role boundary you just read about — gone. An API key grants blanket access. No per-user audit trail. No conditional access policies. No identity lifecycle management. Just a string in a config file that works until someone revokes it.

The fix is not complicated:

Managed identities. They work at both resource and project scope. No secrets to rotate. Entra ID handles the lifecycle. Your conditional access policies actually apply.

Three things to check Monday morning:

1. Default developer role is Azure AI User, not Owner.
2. Managed identities are configured on every Foundry resource.
3. API keys are disabled or rotation-scheduled with alerts.

That is the whole security review. Forward it.

---

## Hashtags

# AzureAIFoundry #IdentityAndAccess #ManagedIdentity #EntraID #PlatformEngineering

---

## Editorial Notes

- Word count: 298 (within 250-350 target)
- No emoji in body
- No "Part X of Y" meta-language
- Self-implicating opening (API keys in .env confession)
- Engagement prompt moved to first comment
- Dependency on AFS02 is implicit (resource topology), not referenced directly
- "Loaded gun" metaphor is the one deliberate image — rest is pure checklist

---

## First Comment

Quick check: are your AI services authenticated with API keys or managed identities?

No judgment. Genuinely curious what the split looks like out there.
