# {a}OS for Government

## An Agentic Solution for Federal AI Needs: Proposal Edition

> **Version:** 1.0 draft for founder review · **Date:** 2026-08-01
> **Companion document:** [aOS7 Technology Stack Whitepaper](./aos7-technology-stack-whitepaper-2026-08.md) (the full 7 stratum tool analysis, 38 jobs, all picks web verified)
> **Method:** every factual claim in this document was researched with live web search in early August 2026 and adversarially fact checked; corrections were applied before writing. Six of the eight fleet support tickets are DELIVERED and linked below; the remaining two are marked LANDING.
> **Standing rail:** the founder is active duty military. No direct DoD funding path is proposed anywhere in this document. The lane is teaming, subcontracting, mentor protege, and civilian channels, and every ambiguous case is marked FOUNDER DECISION.

---

## 1. Executive summary

{a}OS gives an agency a complete system for agentic AI: AI that takes actions, such as filling a form, routing a case, or reconciling a record, not just answering questions.

Three things make it different.

**Cost and control.** Every layer of the reference implementation is open source with zero license cost, and the whole stack runs on one Linux server the agency owns. If the network fails, or a site must operate cut off from the internet, the system keeps working in a degraded mode using only what is on that server.

**Trust in the supply chain.** All AI requests pass through one software gateway, and that gateway only allows models from the United States and allied nations. The rule lives in the software itself as a plain text allowlist, not in a policy binder, so it cannot be bypassed by mistake and an evaluator can read it directly.

**Proof, not promises.** Every agent action produces its own evidence: an OpenTelemetry trace of what was called, a policy gate decision on whether it was allowed, and a named human approval where one was required. The paperwork federal AI rules now demand is a byproduct of running the system, not a reporting exercise bolted on afterward.

And underneath the product sits something no incumbent sells: a public, vendor neutral, 7 stratum reference model an agency can use to evaluate ANY agentic AI vendor, including our competitors. We give the buyer the scoring rubric and then compete on it.

## 2. Why now: the policy window is open

The rules of federal AI buying changed in 2025 and 2026, and each change points at this stack. All items verified against sources listed in Section 10.

| Policy | What it requires | Why it favors {a}OS |
|---|---|---|
| OMB M-25-21 (AI use) | Chief AI Officers, risk practices for high impact AI, public AI use case inventories | Our traces and approval records ARE the risk paperwork. Auditability by construction is a compliance shortcut. |
| OMB M-25-22 (AI acquisition) | Competition, performance tracking, and explicit vendor lock in avoidance | Lock in avoidance is now an official buying rule. A vendor neutral, all open source, self hostable stack answers it directly. |
| EO 14319 + OMB M-26-04 (LLM procurement) | Vendors must disclose how LLMs are built and trained; open source licensed models sit in an exception | Our open licensed ally model lane has the lighter disclosure path, and the gateway allowlist makes the disclosure story one page. |
| EO of June 2, 2026 (AI innovation and security) | AI cybersecurity clearinghouse, frontier model benchmarking | Policy is moving from capability claims to measured security proof. We are evidence native. |
| NIST COSAiS (800-53 AI overlays, in draft) | Control overlays for generative AI and, notably, single agent and multi agent AI systems | The authorization checklist for agentic systems is being written right now. Mapping our strata to the draft overlays buys a head start and a voice in the standard. DELIVERED: see the [NIST crosswalk](./gov/task-0300-nist-crosswalk.md). |
| NIST CAISI + GSA MOU (March 2026) | AI evaluation science enters federal procurement through USAi | Procurement is shifting to measured evaluations. Our gates and traces produce exactly that evidence. |

**The demand is real and it is early.** A March 2026 survey of over 200 government technology executives found 53 percent of agencies exploring or planning agentic AI pilots and another 15 percent already implementing. Pilot stage is when agencies pick their governance, evaluation, and orchestration tooling. The VA signed a 1.6 billion dollar, three year agentic enterprise agreement; the State Department CIO is moving from chatbots to agents; the DOE Genesis Mission treats agents as national scientific infrastructure. And GSA's OneGov channel signed an agentic AI agreement with CORAS in July 2026, proof that a smaller agentic vendor, not just a hyperscaler, can land a direct federal route to market.

## 3. What we sell: the standard plus its reference implementation

**Product one: the Agentic Reference Stack.** A public, vendor neutral 7 stratum model (L1 Models and Infrastructure up to L7 Experience and Intent, with Governance and Observability as cross cutting axes) that answers the question every agency evaluation team is asking: how do we score agentic AI vendors at all? The model gives each stratum an owner, an interface contract, and a failure mode, so a buyer can compare a hyperscaler bundle, a platform incumbent, and an open stack on the same sheet. It costs the buyer nothing, which is precisely why it earns trust.

**Product two: the {a}OS reference implementation.** The working stack described in the companion whitepaper: 38 jobs across the 7 strata, every primary pick open source, ally origin, and self hostable, wired together by three standards (MCP for tools, OpenTelemetry GenAI for proof, AG-UI for human approval). It runs today on one commodity Linux server, and its live deployment operates a real family finance platform and a real multi agent engineering fleet around the clock.

**Accessibility is the design North Star, not a checkbox.** Section 508 binds every federal buyer, yet no incumbent leads its agentic pitch with accessibility. {a}OS is designed toward users who cannot see or operate conventional interfaces, where the agent layer does the acting. An accessibility gate and VPAT skeleton are landing under task-0305.

## 4. Win themes

1. **Zero license cost that stays zero.** Introductory federal pricing snaps back: the 1 dollar and 47 cent OneGov model deals expire September 30, 2026, and GSA plans to charge for USAi in FY 2027. An open source stack on agency hardware has no meter to snap back. OMB M-25-22 tells agencies to protect taxpayer value and build exit strategies; this stack IS the exit strategy.
2. **Lock in removed by design, not by promise.** The 7 stratum model means any single layer can be swapped without rebuilding the rest. The UK Parliament's lock in findings against a major platform vendor show what the alternative costs.
3. **Ally only supply chain, enforced in software.** No Chinese origin model can be called even by accident, because the gateway allowlist refuses it and logs the refusal. M-25-21 promotes American made AI; we enforce it at runtime.
4. **Model churn insurance.** Within a single year the government designated a leading US model lab a supply chain risk, moved to strip its models from federal platforms, then reversed course. Betting a mission on any single lab is the risk; a gateway that swaps labs in one configuration line is the insurance.
5. **The audit trail is the product.** GAO's AI Accountability Framework demands traceability and monitoring, and GAO found agencies still fumbling AI acquisitions in 2026. Every {a}OS agent action carries its trace, gate decision, and named approver by construction.

## 5. Discriminators (statements an evaluation board can score live)

1. **The disconnect test.** The government may cut the offered system off from all outside networks during evaluation. Agent tasks keep running, policy gates keep deciding, audit traces keep writing, using only software and models on government owned hardware. Evaluators score it live.
2. **The random trace pull.** For any agent action the evaluation team picks at random, we produce the complete OpenTelemetry trace in the same session: the model called, the policy decision, and the named human who approved it. No proprietary tooling required to read it.
3. **The allowlist refusal test.** The evaluation team may attempt to call any model not on the allied origin allowlist. The gateway refuses, logs the refusal, and the team can read the allowlist itself as a plain text configuration file.

## 6. Compliance posture

| Requirement area | Our posture | Status |
|---|---|---|
| NIST AI RMF + 800-53 mapping | Crosswalk of all 7 strata to RMF functions and control families | DELIVERED: [NIST crosswalk](./gov/task-0300-nist-crosswalk.md), 42 mappings plus a 21 entry honest gap register |
| Supply chain (Section 889, EO 14028, SBOM) | Full component inventory with license and origin per tool; the enforced allowlist as the control | DELIVERED: [supply chain SBOM](./gov/task-0301-supply-chain-sbom.md), 76 components, 123 citations |
| Threat model | MITRE ATLAS technique mapping per stratum with named mitigations and honest residual risk | DELIVERED: [ATLAS threat model](./gov/task-0302-mitre-atlas-threat-model.md) |
| Sovereignty profile | Air gap deployment variant per stratum, degraded mode as a feature | DELIVERED: [S0 sovereignty profile](./gov/task-0303-s0-sovereignty-profile.md) |
| Section 508 | axe-core gate in CI plus VPAT 2.5 skeleton with honest statuses | LANDING, task-0305 |
| Pilot measurement | 90 day plan measured on the reference model's own axis metrics | DELIVERED: [90 day pilot plan](./gov/task-0306-pilot-plan.md), six metrics with sources and goal bands |

Nothing in this table will be claimed as complete until its deliverable exists with evidence. That discipline is itself part of the offer.

## 7. Sovereign availability of the hosted lane

The self hosted core (LiteLLM, llama.cpp, Qdrant, Langfuse, OPA, Infisical, LLM Guard, gVisor) requires no FedRAMP authorization of its own: FedRAMP covers cloud services offered to agencies, not software an agency installs and operates inside its own boundary. The hosting environment carries the authorization; the software rides the agency's own ATO. That is exactly how the reference implementation runs.

Where an agency wants hosted frontier models, every major lab in our gateway has a verified government path as of August 2026:

| Hosted model | Government status | Path |
|---|---|---|
| Anthropic Claude | FedRAMP High (Claude for Government); also FedRAMP High and DoD IL4/IL5 via Bedrock in AWS GovCloud | OneGov agreement or GovCloud Bedrock |
| OpenAI models | FedRAMP High as Azure OpenAI in Azure Government | Azure Government tenant or OneGov |
| Google Gemini | FedRAMP High (Gemini for Government) | OneGov agreement or Vertex AI with Assured Workloads |
| AWS Bedrock | FedRAMP High and IL4/IL5 in GovCloud, multi model | GovCloud account |
| Azure AI Foundry | Partial: Azure Government catalog is OpenAI model set only as of mid 2026 | Use for OpenAI lane; other labs via their own paths |

The gateway makes these interchangeable: an agency can start on one lab's OneGov deal and move to another in one configuration change, which is the churn insurance of Win Theme 4 made concrete.

## 8. The competitive field, honestly

Three tiers exist in mid 2026. **Platform incumbents** (Palantir AIP, Microsoft Copilot agents, Salesforce Agentforce for Government at FedRAMP High, ServiceNow) win by entrenchment, and each moat is also a weakness: documented lock in complaints, government cloud agent features arriving quarters late, model choice controlled by the platform, and metered pricing with no ceiling. **Mission specialists** (Scale AI's Thunderforge, Anduril Lattice, Ask Sage inside BigBear.ai at IL6) win accreditation depth but sell proprietary, services heavy offerings an agency cannot own or independently audit. **Frontier labs sold direct** win on model quality and near free introductory pricing, but the 2026 record shows single lab dependence is fragile.

We do not out entrench Palantir or out install Microsoft. We sell the thing none of them can: the neutral rubric, the ownable stack, the enforced supply chain, and evidence by construction. Where an agency already runs an incumbent, the reference model still wins: it is how the agency scores that incumbent honestly, and {a}OS layers around what stays.

## 9. Route to market (FOUNDER GATED)

The founder is active duty military, so this proposal recommends no direct DoD award path. The lanes under study are: teaming and subcontracting under primes on vehicles like the VA agentic enterprise agreement, GSA channels including OneGov once product and compliance stories are ready (the CORAS precedent), civilian agency pilots, mentor protege relationships, and consortium membership. The full eligibility and ethics study, including conflict of interest rules for the founder's status, is LANDING under task-0307 and every path in it lands on the founder's desk as a decision, not a recommendation.

## 10. Source register

Every claim above traces to one of the sources gathered and fact checked in the research run of 2026-08-01, including: OMB M-25-21 and M-25-22; EO 14319 and OMB M-26-04; the June 2, 2026 executive order; NIST COSAiS project pages; the NIST CAISI and GSA MOU announcement; GSA USAi and OneGov press releases including the CORAS agreement of July 28, 2026; the VA Salesforce agentic enterprise agreement reporting; State Department and DOE Genesis Mission reporting; the Nextgov agency survey of March 2026; GAO's AI Accountability Framework (GAO-21-519SP) and 2026 AI acquisition findings; Anthropic, Microsoft, Google, and AWS government authorization documentation; and UK parliamentary reporting on platform lock in. Full URL register with per claim citations lives in the research artifacts alongside this document.

## 11. What lands next

Fleet tickets task-0300 through task-0307 (research, development, and synergy planning) integrate into this document as they complete. The companion whitepaper carries the full per stratum tool analysis, the selection doctrine, the S0 degraded mode commitment, and the corrections ledger that shows every claim our own fact checkers changed. We keep that ledger public on purpose: a proposal about trustworthy AI should be visibly trustworthy about itself.
