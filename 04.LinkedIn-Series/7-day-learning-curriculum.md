# Azure AI Foundry × {a}OS — 7-Day Learning Curriculum

> **Version:** v1.0
> **Date:** 2026-04-08
> **Reference model:** Agentic Reference Stack v1.0 (7 strata)
> **Companion series:** "Building an AI Platform That Actually Ships" (12 posts, Apr 8–29)
> **Companion docs:** {a}OS Explorer docs.html → Azure Setup tab

---

## How This Curriculum Works

**Goal:** Learn Azure AI Foundry from the ground up in 7 days, using the {a}OS 7-stratum model as your map.

**Structure:** Bottom-up through the strata (L1 → L7), then cross-cutting concerns, then full integration. Each day maps to specific strata, LinkedIn posts for deeper context, docs.html sections for reference, and hands-on tasks you complete in your own Azure subscription.

**Time commitment:** ~2–4 hours per day. Each day has a "Minimum Viable" track (core tasks, ~2 hours) and a "Deep Dive" track (extended exploration, ~4 hours).

**Prerequisites:**

- Azure subscription (pay-as-you-go is fine)
- Azure CLI installed (`az --version`)
- Python 3.10+ (for SDK examples)
- A terminal and a text editor

---

## Quick Reference

| Day | Strata | LinkedIn Posts | Primary Task |
|:---:|:---|:---|:---|
| 1 | L1 Models & Infrastructure | Post 1, Post 2 | Create Foundry resource, deploy model, first inference |
| 2 | L2, L3 Knowledge + Execution | Post 8, Post 5 (read-ahead) | Set up AI Search, RAG pipeline, tool calling |
| 3 | L4 Orchestration & Decisioning | Post 7 | Build prompt agent, configure identity, test versioning |
| 4 | L5 Observability & Evaluation | Post 10 | Connect App Insights, run evaluators, CI/CD gate |
| 5 | L6, L7 Governance + Experience | Post 3, Post 4, Post 6 | Harden RBAC, Content Safety, design approval gates |
| 6 | Cross-cutting concerns | Post 5, Post 9 | Private endpoints, VNet injection, APIM cost metering |
| 7 | Full integration | Post 11, Post 12 | Bicep deployment, gap analysis, {a}OS classification |

---

## Day 1: Orientation + L1 Models & Infrastructure

> **Stratum:** L1 — Models & Infrastructure
> **Boundary question:** Is the model/runtime/compute/network foundation available and behaving correctly?

### Learning Goals

- Understand what Azure AI Foundry is (and isn't)
- Create your first Foundry resource and project
- Deploy a model and make your first inference call
- Understand the two resource models (classic vs. new)

### Read First

- **LinkedIn Post 1:** "Your AI Platform Doesn't Ship What You Think It Ships" — sets the thesis
- **LinkedIn Post 2:** "What Azure AI Foundry Actually Is (and Isn't)" — demystifies the platform
- **Docs:** Azure Setup → Getting Started, L1: Models & Infrastructure

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Register the resource provider:

   ```bash
   az provider register -n Microsoft.CognitiveServices
   ```

2. Create a Foundry resource:

   ```bash
   az cognitiveservices account create \
     --name my-foundry-dev \
     --resource-group rg-ai-dev \
     --kind AIServices \
     --sku S0 \
     --location eastus2
   ```

3. Create a project within the resource
4. Deploy a model (pay-as-you-go gpt-4.1):

   ```bash
   az cognitiveservices account deployment create \
     --name my-foundry-dev \
     --resource-group rg-ai-dev \
     --deployment-name gpt41-deployment \
     --model-name gpt-4.1 \
     --model-version "2025-04-14" \
     --model-format OpenAI \
     --sku-capacity 1 \
     --sku-name GlobalStandard
   ```

5. Make your first inference call via the Python SDK
6. Verify which resource model you're on:

   ```bash
   az provider show -n Microsoft.CognitiveServices --query "resourceTypes[?resourceType=='accounts'].apiVersions" -o table
   ```

**Deep Dive (~4 hours):**

1. Compare deployment types: Standard vs. PTU vs. Global vs. DataZone
2. Explore the model catalog in the portal
3. Test Foundry Local for edge inference (if applicable)
4. Enable CMK encryption via Key Vault
5. Document: what models are available in your target region? In Gov cloud?

### Day 1 Checkpoint

You should now have: a running Foundry resource, a deployed model, and a successful inference call. You should understand the difference between classic and new resource models.

---

## Day 2: L2 Knowledge & Memory + L3 Execution & Interfaces

> **Strata:** L2 — Knowledge & Memory, L3 — Execution & Interfaces
> **L2 boundary question:** What context did the system know, retrieve, remember, or forget?
> **L3 boundary question:** What external action was invoked, against which interface, and what happened?

### Learning Goals

- Set up a RAG pipeline with Azure AI Search
- Configure tool calling and MCP integration
- Understand the Basic vs. Standard storage decision
- Learn which tools work in VNet isolation (and which don't)

### Read First

- **LinkedIn Post 8:** "RAG and the Data Residency Question Nobody Asked"
- **LinkedIn Post 5 (read-ahead):** "The Network Isolation Exceptions Table"
- **Docs:** Azure Setup → L2: Knowledge & Memory, L3: Execution & Interfaces

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Create an Azure AI Search resource
2. Upload sample documents and create a vector index
3. Configure your agent with the AI Search tool
4. Test a query — verify the agent retrieves relevant context
5. Test function calling: create a simple function tool and invoke it
6. Review the Basic vs. Standard agent storage options — **choose Standard with BYO storage** for anything beyond testing

**Deep Dive (~4 hours):**

1. Set up MCP server integration
2. Test Code Interpreter with a data analysis task
3. Test which tools work and which fail (build your personal exceptions list)
4. Configure private endpoint for AI Search
5. Block Bing Grounding and Web Search via Azure Policy
6. Explore Document Intelligence for structured document processing

### Day 2 Checkpoint

You should now have: a working RAG pipeline, function calling configured, and a clear understanding of which tools are safe for production vs. which break in isolated environments.

---

## Day 3: L4 Orchestration & Decisioning

> **Stratum:** L4 — Orchestration & Decisioning
> **Boundary question:** What happens next, in what order, with which agent, under which stop conditions?

### Learning Goals

- Build a prompt agent (GA, production-safe)
- Configure per-agent Entra identity
- Understand agent maturity levels (prompt vs. workflow vs. hosted)
- Test agent versioning and rollback

### Read First

- **LinkedIn Post 7:** "Agent Maturity: What's GA, What's Preview, What Matters"
- **Docs:** Azure Setup → L4: Orchestration & Decisioning

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Create a prompt agent with a clear system prompt
2. Add tools to your agent (function calling from Day 2)
3. Configure agent identity (Entra managed identity)
4. Test your agent in the playground
5. Create a second version — test versioning and rollback

**Deep Dive (~4 hours):**

1. Explore workflow agents (preview) — understand their limitations
2. Test Model Router — observe routing behavior, note lack of transparency
3. Compare: when would you use Semantic Kernel vs. LangGraph vs. Foundry-native?
4. Design a multi-agent architecture on paper (what Foundry provides vs. what you'd build)
5. Document your agent maturity decision: which agent types are safe for your use case?

### Day 3 Checkpoint

You should now have: a working prompt agent with tools, Entra identity, and versioning. You should understand why prompt agents are the right starting point for production.

---

## Day 4: L5 Observability & Evaluation

> **Stratum:** L5 — Observability & Evaluation
> **Boundary question:** What actually happened, how well did it perform, and where did it fail?

### Learning Goals

- Connect Application Insights and inspect agent traces
- Run built-in evaluators (quality, safety, task adherence)
- Set up CI/CD evaluation gates
- Understand the private App Insights tracing gap

### Read First

- **LinkedIn Post 10:** "The Observability Paradox: Private Networks Break Their Own Tracing"
- **Docs:** Azure Setup → L5: Observability & Evaluation

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Create an Application Insights resource
2. Connect it to your Foundry project
3. Run your agent and inspect traces in the portal
4. Run a built-in evaluator (quality) against your agent's output
5. Run a safety evaluator — verify Content Safety scoring

**Deep Dive (~4 hours):**

1. Run a task adherence evaluator with a rubric
2. Create a custom evaluation pipeline
3. Set up a GitHub Actions workflow with an evaluation gate
4. Configure continuous evaluation against a test dataset
5. **Critical test:** If you have private App Insights, verify that tracing works (it likely won't — document the gap)
6. Design an observability workaround: non-private App Insights in a peered network
7. Check trace retention (90-day default)

### Day 4 Checkpoint

You should now have: working traces in App Insights, at least one evaluation run, and a clear understanding of the tracing gap in private networks. If you're in a private network environment, you should have a workaround plan documented.

---

## Day 5: L6 Governance & Trust + L7 Experience & Intent

> **Strata:** L6 — Governance & Trust, L7 — Experience & Intent
> **L6 boundary question:** Who is allowed to do this, under what policy, with what risk and budget?
> **L7 boundary question:** What is the user asking, seeing, approving, or rejecting?

### Learning Goals

- Harden identity and access (Entra ID, RBAC roles, remove API keys)
- Configure Content Safety and Prompt Shields
- Understand the Foundry Portal experience (classic vs. new)
- Design approval gate architecture (what Foundry does NOT provide)

### Read First

- **LinkedIn Post 3:** "Where Governance Actually Lives (and Why Your Platform Doesn't Own It)" — the {a}OS 7-stratum debut
- **LinkedIn Post 4:** "The Identity Layer Most Teams Skip"
- **LinkedIn Post 6:** "Models, Money, and the Reality of Model Access"
- **Docs:** Azure Setup → L6: Governance & Trust, L7: Experience & Intent

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Switch from API key authentication to Entra ID (managed identity)
2. Assign RBAC roles: `Azure AI User` for developers (least privilege)
3. Verify `Azure AI Owner` is NOT assigned to any developer accounts
4. Configure Content Safety severity thresholds
5. Test Prompt Shields — attempt a jailbreak and verify detection
6. Navigate the Foundry Portal: toggle between classic and new portals

**Deep Dive (~4 hours):**

1. Create a custom RBAC role with granular `dataActions`
2. Configure Azure Policy assignments for your AI resources
3. Block Bing/Web Search tools via Azure Policy in production
4. Test agent publishing to Teams (note: requires public endpoints)
5. Design your approval gate architecture (Logic Apps or custom workflow)
6. Map your compliance requirements to {a}OS strata: which strata have mandatory controls?
7. Document: what governance capabilities does Foundry NOT provide that you must build?

### Day 5 Checkpoint

You should now have: Entra-only authentication, RBAC configured, Content Safety active, and a written plan for governance components you need to build. You should understand that L6 and L7 are largely your responsibility, not the platform's.

---

## Day 6: Cross-Cutting — Network Isolation + Cost Governance

> **Focus:** Cross-cutting concerns that span all strata
> **Axes:** Governance & Trust Axis, Observability & Evaluation Axis

### Learning Goals

- Lock down networking (private endpoints, VNet injection)
- Build your network isolation exceptions checklist
- Set up cost controls (budgets, APIM gateway, token metering)
- Understand the tension between isolation and functionality

### Read First

- **LinkedIn Post 5:** "The Network Isolation Exceptions Table"
- **LinkedIn Post 9:** "Cost Governance Is Not a Feature — It's an Architecture"
- **Docs:** Azure Setup → Network Isolation, Cost Governance

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Enable private endpoints for your Foundry resource
2. Test: which features still work? Which break?
3. Set up Azure Cost Management budget with alerts
4. Configure per-resource cost tracking
5. Document your network isolation exceptions (things that won't work behind VNet)

**Deep Dive (~4 hours):**

1. Configure VNet injection for agent compute (requires /27+ subnet delegated to `Microsoft.App/environments`)
2. Set up hub-and-spoke VNet topology (hub VNet with Firewall, spoke VNet for AI workloads)
3. Deploy APIM as an AI Gateway:
   - Token metering per request
   - Rate limiting per consumer
   - Cost chargeback by team/project
4. Configure DNS private zones for all private endpoints
5. Block Bing/Web Search/SharePoint Grounding via Azure Policy (these route over public internet)
6. Design token budget enforcement (APIM → custom logic → kill switch)
7. Build your "Marketing vs. Reality" table for your environment

### Day 6 Checkpoint

You should now have: private endpoints enabled (or planned), a cost budget configured, and a clear-eyed understanding of what "end-to-end network isolation" actually means (and doesn't mean). If you deployed APIM, you have the foundation for cost governance.

---

## Day 7: Integration + {a}OS Capstone

> **Focus:** Full stack — deploy Phase 1 architecture, classify your system against {a}OS

### Learning Goals

- Deploy the complete Phase 1 architecture via IaC
- Classify your own AI system against the 7-stratum model
- Identify your gap strata and custom engineering roadmap
- See the full picture: what Foundry provides vs. what you own

### Read First

- **LinkedIn Post 11:** "Phase 1: What to Actually Build First"
- **LinkedIn Post 12:** "A Framework for Every AI Platform Decision"
- **Docs:** Azure Setup → IaC & CI/CD, all strata sections (review)

### Hands-On Tasks

**Minimum Viable (~2 hours):**

1. Fork the `azure-ai-foundry/foundry-samples` Bicep templates
2. Deploy the Phase 1 architecture via Bicep:
   - Foundry resource + project
   - Private endpoints
   - One model deployment
   - One prompt agent
   - Application Insights (with tracing gap workaround if private)
   - Cost Management budget
3. Classify your system: for each stratum (L1–L7), write one sentence — what's covered, what's a gap

**Deep Dive (~4 hours):**

1. Customize the Bicep templates for your organization's policies
2. Add APIM AI Gateway to the deployment
3. Create a CI/CD pipeline (GitHub Actions) with:
   - Bicep deployment
   - Agent evaluation gate
   - Cost check gate
4. Write your full {a}OS classification:
   - For each stratum: Foundry coverage, your custom engineering needs, owner, timeline
   - For each axis: how governance and observability cut across your strata
5. Create your "Phase 2 Roadmap" — what to build in months 2-6
6. Present your classification to a colleague — can they use it to diagnose a hypothetical failure?

### Day 7 Checkpoint

You should now have: a deployed Phase 1 platform, a written {a}OS classification of your system, and a roadmap for what you need to build next. You can now look at any AI platform through the {a}OS lens and immediately identify gap strata.

---

## Post-Curriculum: What's Next

1. **Follow the LinkedIn series** (Posts 1–12, Apr 8–29) for deeper context on each topic
2. **Bookmark the {a}OS Explorer docs** (docs.html → Azure Setup tab) for ongoing reference
3. **Build Phase 2:** Tackle your identified gaps — typically L5 Observability (private network workaround), L6 Governance (approval gates, audit trail), and L4 Orchestration (production multi-agent patterns)
4. **Contribute:** The {a}OS model and the Explorer are open for feedback. Share your classification, challenge a placement, suggest a new product mapping
5. **Cross-platform exercise:** Repeat the 7-stratum classification for AWS Bedrock, GCP Vertex, or your internal platform. The strata are vendor-neutral — the gaps will show up in the same places

---

## Cross-Reference Matrix

| Day | Strata | LinkedIn Posts | Docs Sections | Primary Deliverable |
|:---:|:---|:---|:---|:---|
| 1 | L1 | Post 1, Post 2 | Getting Started, L1 Setup | Running Foundry resource + model |
| 2 | L2, L3 | Post 8, Post 5 | L2 Setup, L3 Setup | RAG pipeline + tools |
| 3 | L4 | Post 7 | L4 Setup | Working prompt agent |
| 4 | L5 | Post 10 | L5 Setup | Traces + evaluation run |
| 5 | L6, L7 | Post 3, Post 4, Post 6 | L6 Setup, L7 Setup | Hardened auth + governance plan |
| 6 | Cross-cutting | Post 5, Post 9 | Network Isolation, Cost Governance | Network lockdown + cost controls |
| 7 | All | Post 11, Post 12 | IaC & CI/CD, All review | Deployed Phase 1 + {a}OS classification |

## Post-to-Stratum Mapping

| Post # | Title | Primary Stratum | Secondary Strata |
|:---:|:---|:---:|:---|
| 1 | Platform Gap | Cross-cutting | All |
| 2 | What Foundry Is | L1 | All |
| 3 | Governance Lives Here | L6, L7 | L5 |
| 4 | Identity Layer | L6 | — |
| 5 | Network Isolation | L1 (axis: Governance) | L3, L6 |
| 6 | Models & Money | L1 | L6 (cost) |
| 7 | Agent Maturity | L4 | L3 |
| 8 | RAG & Data | L2 | L3 |
| 9 | Cost Governance | L6 (axis: Governance) | L5 |
| 10 | Observability Paradox | L5 | L1 |
| 11 | Phase 1 Build | All | — |
| 12 | Framework Capstone | All | — |
