---
post_id: AFS04
date: 2026-04-15
topic: "The Identity Layer Most Teams Skip"
series_name: "Building an AI Platform That Actually Ships"
series_part: 4
series_total: 12
character: Regulator
structure: Checklist / Security Audit
tone: Deadpan, first-person, self-implicating, "tired architect"
hashtag_count: 5
status:
  ideate: READY
---

## Topic

Azure AI Foundry identity and access control: Entra ID, RBAC roles, managed identities, and the danger of API key authentication. The four Foundry-specific roles, what each one actually grants, and why `Azure AI User` should be the developer default.

## Why Now

Teams are spinning up Foundry projects fast. Most copy-paste API keys from the portal and never look back. The identity layer is the first thing skipped and the last thing audited. With enterprise AI deployments scaling, one leaked key means blanket access with zero role restrictions.

## Character Selection

**Regulator** — the post that tells you what to lock down. Reads like a security review forwarded to your CISO. Short fragments, imperative tone, checklist energy.

## Structure & Tone

- Open with a confession (API keys in .env)
- Walk the four Foundry roles as a quick-reference table
- Land on managed identities as the correct default
- Close with "forward this to your security team" energy
- No fluff, no analogies, just receipts

## Hashtags

1. #AzureAIFoundry
2. #IdentityAndAccess
3. #ManagedIdentity
4. #EntraID
5. #PlatformEngineering

## Key Claims

1. Azure AI User is the correct developer default — data actions only, no resource creation.
2. Azure AI Owner is a loaded gun — full control, should never be assigned without explicit justification.
3. API keys bypass every RBAC role you set — they grant blanket access with no audit trail per user.
4. Managed identities work at both resource and project scope — no secrets to rotate.
5. Custom roles with granular dataActions are supported and recommended for production.

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

"Quick check: are your AI services authenticated with API keys or managed identities?"

## Visual Direction

RBAC role comparison table showing 4 Foundry-specific roles with columns: Role, Grants, Risk Level, When to Use. Clean, dark-themed, {a}OS branded. Think security documentation, not marketing.

## Content Source

- Azure AI Foundry RBAC documentation
- Entra ID managed identity docs
- Post AFS02 (dependency — resource topology context)
- Real-world incident patterns from API key leaks
