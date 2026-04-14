# AFS05 — Post

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
word_count_target: 250-350
```

## Strategy Notes

**Audience:** Platform engineers, security architects, cloud infra leads running AI workloads in regulated environments. Secondary: CISOs and compliance teams evaluating Azure AI Foundry.

**Goal:** Position as the person who already found the gaps so you don't have to. Build trust through specificity. Drive saves and shares — this is reference material.

**Character (Regulator):** Methodical. Not angry, not sarcastic. The tone of someone reading findings into the record. Short declarative statements. Lists. The spreadsheet person.

**Positioning:** This is the most operationally valuable post in the series. It saves readers a production incident. Frame it as a gift, not a complaint.

---

## Copy/Paste

"End-to-end network isolation."

That is the slide. Here is the receipt.

I spent two weeks mapping every Azure AI Foundry tool against VNet isolation. Not the docs. The actual behavior. Here is the table nobody publishes in one place.

**What works inside your VNet:**

- Private endpoints for inbound access
- VNet injection for agent compute (needs /27+ subnet delegated to Microsoft.App/environments)
- Azure AI Search via private endpoint
- Code Interpreter, Function Calling — routed over Microsoft backbone

**What breaks under isolation:**

- File Search
- OpenAPI Tool
- Azure Functions tool
- Browser Automation
- Computer Use
- Agent-to-Agent (A2A)
- Image Generation
- Logic Apps
- Hosted Agents — zero VNet support
- Workflow Agents — inbound only
- Tracing with private Application Insights
- The new Foundry portal (use classic, SDK, or CLI)

**What goes over public internet even inside your "isolated" environment:**

- Bing Grounding
- Web Search
- SharePoint Grounding

Read that last section again. Your VNet is configured. Your private endpoints are live. And Bing Grounding is routing queries over the public internet.

The fix: block Bing and WebSearch grounding via Azure Policy on day one. Before anyone enables it in a notebook and your SOC gets a surprise.

How to verify this yourself:

- `az resource list --resource-type Microsoft.CognitiveServices/accounts`
- Check allowed network access rules per resource
- Review Azure Policy assignments for denied tool types
- Cross-reference with Microsoft's managed network isolation docs

The vendor slide is not your architecture. The exceptions table is.

I maintain this table as part of our {a}OS deployment guides. It has a "last verified" date because this list changes quarterly. Yours should too.

---

## Editorial Notes

- **Word count:** ~295 (within 250-350 target)
- **Character consistency:** Regulator voice throughout — declarative, list-heavy, no hedging
- **Self-implicating:** "I spent two weeks mapping" — positions as personal work, not pontification
- **Perishability addressed:** "last verified date" and "changes quarterly" per red-team feedback
- **Verification framing:** CLI commands and methodology included per brief
- **No engagement question in body** — moved to first comment per series rules
- **No emojis, no slop language, no "Part X"**
- **{a}OS mention:** Organic, at the end, tied to the artifact itself
- **Risk:** The broken-tools list is long. If Microsoft fixes several by publish date, update before posting. Spot-check File Search and Hosted Agents the morning of.

## First Comment

Has your security team audited which AI platform tools route over public internet even inside your VNet? What did they find?
