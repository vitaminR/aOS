# AFS05 — Brief

```yaml
id: AFS05
series: "Building an AI Platform That Actually Ships"
title_working: "The Network Isolation Exceptions Table"
type: TECH
character: Regulator
date: 2026-04-16
day: Wednesday
author: Nils Müller
status: draft
```

## Topic

The real gaps in Azure AI Foundry's VNet isolation. A tool-by-tool truth table showing what actually works behind a private endpoint, what silently fails, and what routes over public internet even inside your "isolated" environment.

## Why Now

- Enterprise AI adoption is accelerating into regulated industries (finance, health, gov)
- "End-to-end isolation" is the vendor slide. The exceptions table is the receipt.
- Most teams discover these gaps in production, after the security review, after the architecture diagram was already blessed
- Azure AI Foundry's network isolation story has improved but the gaps are poorly documented in one place
- Bing Grounding / Web Search silently going over public internet catches teams off guard

## Character: Regulator

Tone of the auditor who has seen the vendor slide deck and then checked the actual packet captures. Not angry — resigned. Methodical. The person who builds the spreadsheet nobody wanted but everybody needs.

## Structure & Tone

1. **Hook** — Open with the myth: "end-to-end network isolation." One line.
2. **Setup** — The three-column truth table framing (Works / Broken / Public Internet)
3. **The Table** — Walk through each category with specifics. No hedging.
4. **The Worst Offender** — Bing/WebSearch going public even inside VNet. Call it out.
5. **The Save** — "Here's how to check yourself" with Azure Policy + CLI framing
6. **Takeaway** — The exceptions table is the architecture. The vendor slide is not.

Short fragments. Deadpan. No exclamation marks. Lists over paragraphs. The rhythm of someone reading from a compliance checklist.

## Hashtags (5)

`#AzureAIFoundry` `#NetworkSecurity` `#VNetIsolation` `#EnterpriseAI` `#CloudSecurity`

## Key Claims

1. Azure AI Foundry's "VNet isolation" has at least 8 tools/features that do not work in isolated mode
2. Bing Grounding, Web Search, and SharePoint Grounding route over public internet even inside a VNet-configured project
3. Hosted Agents have zero VNet support; Workflow Agents are inbound-only
4. The new Foundry portal does not work in isolated environments — you must use classic portal, SDK, or CLI
5. File Search, OpenAPI Tool, Azure Functions tool, Browser Automation, Computer Use, A2A, Image Generation, and Logic Apps all break under isolation
6. Code Interpreter and Function Calling work because they route over the Microsoft backbone
7. VNet injection for agent compute requires a /27+ subnet delegated to Microsoft.App/environments
8. Azure Policy can block Bing/WebSearch grounding before it reaches production

## Anti-Slop Checklist

- [ ] No "game-changer," "unlock," "leverage," "elevate," "deep dive"
- [ ] No "excited to share," "thrilled," "proud to announce"
- [ ] No emojis in body copy
- [ ] No "Part X of Y"
- [ ] Engagement prompt is in FIRST COMMENT, not body
- [ ] Word count 250-350
- [ ] First person, self-implicating where possible
- [ ] Short fragments, deadpan delivery

## Engagement Prompt (First Comment)

"Has your security team audited which AI platform tools route over public internet even inside your VNet? What did they find?"

## Visual Direction

Network isolation exceptions table — a clean, minimal grid. Rows = Foundry tools/features. Columns = VNet status (Works / Broken / Public Internet). Color-coded: green check, red X, orange warning triangle for "public internet." {a}OS branding in corner. Dark background, monospace feel. Should look like a compliance artifact, not a marketing graphic.
