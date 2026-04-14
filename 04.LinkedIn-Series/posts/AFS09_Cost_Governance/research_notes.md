# AFS09 — Research Notes

## Why No Managed AI Platform Ships Cost Governance

The pattern is consistent across all three major cloud AI platforms:

**Azure AI Foundry:**

- Azure Cost Management for budgets/alerts (subscription or RG scoped)
- No per-team chargeback
- No per-user token budgets
- No real-time spend enforcement
- No agent loop circuit breaker
- Recommended path: APIM as AI Gateway

**AWS Bedrock:**

- CloudWatch billing alarms
- No per-agent cost limits
- No native chargeback by team/project
- No circuit breaker for loops

**Google Vertex AI:**

- Budget alerts via Billing
- No per-user token limits
- No agent loop detection
- No native chargeback mechanism

**Why this is structural:** Cost governance requires organizational context — team boundaries, budget owners, approval chains, escalation paths. These are different at every company. Platform vendors cannot build a universal cost governance system because governance is inherently organizational, not technical. The platform provides the metering primitives. The governance architecture is yours to build.

## The APIM AI Gateway Architecture

### Layer 1: Request Interception

```
Client → APIM (AI Gateway) → Azure AI Foundry endpoint
```

- APIM sits as reverse proxy
- Every request passes through APIM policies
- Policies can inspect, meter, throttle, or reject

### Layer 2: Metering and Attribution

- APIM logs every request with custom dimensions (team, project, user, agent ID)
- Token estimation from request/response payload
- Logs flow to Log Analytics or Event Hub
- Aggregation queries produce per-team/per-project cost views

### Layer 3: Enforcement

- Rate limiting: X requests per minute per subscription key
- Token budgets: estimated token count against a rolling budget
- Hard caps: reject requests when budget exhausted
- Kill switch: disable a product subscription or backend instantly

### Layer 4: Alerting and Escalation

- Log Analytics alerts on anomalous spend patterns
- Azure Monitor action groups for escalation (email, SMS, webhook, Logic App)
- Dashboard in Grafana or Azure Workbooks for real-time visibility

## The $22 Runaway Loop — What Actually Happened

- A local development agent entered a tool-calling loop
- The agent was calling an external API repeatedly — each call consumed tokens
- No circuit breaker existed — no max-iteration limit, no cost threshold, no timeout
- The loop ran overnight (approximately 3 AM)
- Total cost: $22 in API consumption
- Discovery: the next morning, reviewing billing

**Why $22 matters:**

- It is a small number — which is the point
- $22 on a development agent with a cheap model
- Scale that to a production agent, a more expensive model, a tool that creates resources, or an agent with write access to external systems
- The failure mode is not the dollar amount — it is the absence of any mechanism to detect and stop it
- "What if it had been $2,200? $22,000? What if the agent had been creating cloud resources instead of consuming tokens?"

**Attribution clarity:**

- This was NOT Azure AI Foundry
- This was a local agent development environment
- The lesson is universal: no managed AI platform has native circuit breakers for agent loops
- Foundry inherits this same gap — if you deploy an agent in Foundry without external cost governance, the same failure mode exists

## PTU as an Executive Cost Decision

- PTU (Provisioned Throughput Units) = committed capacity
- Billed monthly whether utilized or not
- Typically requires executive or finance approval due to cost magnitude
- Common mistake: platform team commits to PTU based on peak projections, actual usage is 30-40% of committed capacity
- Second mistake: no PTU, pay-as-you-go only, then get throttled during production spikes
- Right pattern: PTU for baseline predictable load + pay-as-you-go for burst + APIM to route between them

## Cost Governance Architecture Components

| Component | Role | Build vs Buy |
|---|---|---|
| Azure Cost Management | Budget alerts (reactive) | Native (buy) |
| APIM AI Gateway | Request-level metering, throttling, kill switch | Configure (semi-buy) |
| Log Analytics | Cost aggregation, anomaly detection | Native (buy) |
| Custom dashboard | Per-team/per-project cost visibility | Build |
| Token budget service | Rolling budget tracking per entity | Build |
| Circuit breaker logic | Detect and halt runaway agents | Build |
| Chargeback reporting | Finance-ready cost attribution | Build |
| Alert escalation | Anomaly → human notification → kill switch | Configure |

**Key insight:** The "buy" components are observability primitives. The "build" components are the governance logic. The platform gives you eyes. You build the brain and the hands.

## Engagement Angle

This is the highest-engagement post in the series because:

1. Dollar amounts create visceral reactions
2. "3 AM and nobody was watching" is a universal fear
3. Every platform team has either experienced this or knows they could
4. The fix is actionable — not "be more careful" but "build this architecture"
5. The engagement question ("What's your per-team AI spend limit?") forces self-assessment

The post should make people uncomfortable, then give them something to do about it.
