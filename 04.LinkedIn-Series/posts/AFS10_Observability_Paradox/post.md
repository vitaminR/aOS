---
post_id: AFS10
title: "The Observability Paradox: Private Networks Break Their Own Tracing"
topic: "Tracing breaks with private Application Insights — the workaround architecture for network-isolated AI deployments"
date: 2026-04-24
series_name: "Building an AI Platform That Actually Ships"
series_part: 10
series_total: 12
character: Regulator
structure: "D8 #5 — Paradox Reveal"
tone: "D3 #3 — Tired Architect"
status: "draft:COMPLETE"
art_status: "IMAGE_PENDING — needs peered App Insights workaround architecture diagram"
word_count: 305
publish:
  banner_text: "Building an AI Platform That Actually Ships"
---

# AFS10 — The Observability Paradox

## Strategy Notes

- This is an {a}OS L5 (Observability & Evaluation) post. The paradox proves why L5 is structurally yours.
- Regulator voice: slightly incredulous, constructive. Not angry. "This should not be the case. It is. Here is how to survive it."
- The paradox is the hook. The workaround architecture is the value. Do not stop at naming the problem.
- Verification commands included so readers can check their own environment.
- Built-in evaluators get a brief positive mention — the platform is not all broken, the observability pipeline has a specific structural conflict.
- Engagement prompt in first comment, not body.
- Depends on Posts 5 (network isolation) and 7 (agent maturity) — readers who followed the series will already know the isolation gaps. This post reveals the collision.

## Copy/Paste

I locked down the network. Private endpoints on everything. VNet isolation enforced. Security team signed off.

Then I looked at our traces. Nothing.

OpenTelemetry tracing for Azure AI Foundry prompt agents is GA. It works. The built-in evaluators — quality, safety, task adherence — are genuinely useful. You can wire them into CI/CD and get real signal on agent behavior before it reaches production.

But there is a catch nobody mentions in the quickstart.

If your Application Insights has private endpoints — which it will, because you just locked down your network — tracing breaks. Completely. Not degraded. Gone.

The platform that told you to isolate your network also requires a non-isolated endpoint to observe what happens inside it.

I sat with that for a minute.

Here is the workaround. It is not a toggle. It is architecture.

Deploy a separate Application Insights instance without private endpoints in an observability spoke VNet. Peer it to your production spoke. Lock it down with NSGs — restrict ingress to your Foundry subnet only. Route traces through the peering. Sink everything into a Log Analytics workspace you control.

You can verify whether your tracing is actually working:

`az monitor app-insights component show --app <name> -g <rg> --query "publicNetworkAccessForIngestion"`

If that returns "Disabled" and your agents are running in a private VNet, your traces are not arriving. Test it before you need it.

The evaluators work. The tracing pipeline works. The network configuration that production requires breaks the connection between them.

Plan the workaround before your first deployment. Not after your first incident.

# EnterpriseAI #AIObservability #NetworkSecurity #AIArchitecture #CloudArchitecture

---

## Editorial Notes

- ~305 words. Within LinkedIn optimal range (250-350).
- Voice matches series: short fragments, first person, self-implicating, deadpan. "I sat with that for a minute" is the Regulator processing the absurdity.
- Structure: "I locked down the network" (setup) -> "Nothing" (paradox reveal) -> "here is the workaround" (architecture) -> "plan it before your first deployment" (punch).
- The workaround is concrete: separate App Insights, no private endpoints, peered spoke, NSG-restricted, Log Analytics sink. Not hand-waved.
- Verification command included inline — readers can check their own environment.
- Positive mention of evaluators and tracing quality prevents the post from reading as a complaint. The platform has real value. The network conflict is a specific structural issue.
- No "Part 10 of 12." Post stands alone.
- {a}OS L5 is demonstrated by the content, not name-dropped. The series reader connects it; the standalone reader gets the architecture.

## First Comment (post after publishing)

Have you tested whether your AI tracing actually works in your network-isolated environment? Serious question. Most teams assume it does because it worked in dev — where nothing was isolated.

The verification is one command:

`az monitor app-insights component show --app <name> -g <rg> --query "publicNetworkAccessForIngestion"`

If that returns "Disabled" and your agents run in a private VNet, check your trace pipeline. It may be silent.
