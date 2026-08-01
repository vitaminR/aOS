# {a}OS7 90-day government pilot plan with axis metrics

**Status:** proposed, contracting-actionable pilot section; goals are not performance claims  
**Date:** 2026-08-01  
**Reference baseline:** [{a}OS7 technology stack whitepaper](../../03.Research/aos7-technology-stack-whitepaper-2026-08.md) at commit `377faf7`  
**Commercial boundary:** ally-only components; no fabricated past performance, authorization, accreditation, or compliance status. No direct DoD funding route is recommended. Any eligible pursuit must remain in the approved protégé/subcontract lane; ambiguity is **FOUNDER DECISION**.

## The decision the pilot is designed to support

At day 90, the customer should be able to choose one of three evidence-backed outcomes: **stop**, **extend under supervision**, or **authorize a separately governed production transition**. The pilot does not presume the third outcome.

The customer selects one bounded policy-knowledge workflow and one bounded action workflow before kickoff. Each workflow must have an accountable owner, approved data corpus, permitted users, action allowlist, human-approval points, task-success rubric, cost ceiling, and stop conditions. High-impact or legally consequential actions remain human-controlled throughout the pilot.

## Six axis metrics

All target bands below are **pilot goals**, not claimed baselines or guarantees. Phase 1 measures the customer’s actual task mix and may refine a band only through a signed change record. Langfuse tracing can capture request lifecycle, timing, cost, retrieval, and tool observations; LiteLLM exposes cost tracking; DeepEval metrics score test cases against thresholds; and OPA decision logs record policy queries, inputs, bundle metadata, results, and decision IDs. [Langfuse observability](https://langfuse.com/docs/observability/overview), [Langfuse metrics](https://langfuse.com/docs/metrics/overview), [LiteLLM proxy capabilities](https://docs.litellm.ai/), [DeepEval metric model](https://deepeval.com/docs/metrics-introduction), [OPA decision logs](https://www.openpolicyagent.org/docs/management-decision-logs).

| Metric | Definition and formula | System of record | Pilot goal band | Decision use |
|---|---|---|---|---|
| **1. Cost per successful task** | Sum of model, embedding, retrieval, and metered tool cost for completed attempts divided by tasks that meet the signed success rubric. Failed, denied, abandoned, and retried attempts remain in the numerator so the metric cannot hide waste. | LiteLLM spend records joined to Langfuse task/trace IDs and the DeepEval or human success disposition. LiteLLM documents proxy cost tracking; Langfuse documents cost and trace dimensions. [LiteLLM](https://docs.litellm.ai/), [Langfuse metrics](https://langfuse.com/docs/metrics/overview). | **Goal:** at or below the customer-approved per-task-class ceiling; forecast-to-actual unit cost between **0.85× and 1.05×** of the approved estimate after task-mix normalization. Phase 1 is measurement-only until the ceiling is signed. | Detects expensive retries, model over-routing, and cheap-but-unsuccessful behavior; supports an extend/stop decision without asserting ROI. |
| **2. Trace coverage** | Successful and unsuccessful pilot task attempts with a complete trace chain—request, identity pseudonym, route, retrieval, model, tool, policy, approval, outcome, and cost—divided by all accepted attempts. A field may be explicitly `not_applicable`; it may not silently disappear. | Langfuse traces and observations, reconciled daily against the authoritative task ledger. Langfuse describes traces as the complete request lifecycle including model, retrieval, tool, timing, input/output, and metadata. [Langfuse observability](https://langfuse.com/docs/observability/overview). | **Goal:** **95–100%** complete trace coverage overall and **100%** for high-impact attempts, denials, and approval-required actions. Missing sensitive content may be masked, but the event and reason must remain. | Proves reconstructability; pauses measured autonomy if coverage falls below the band. |
| **3. Evaluation pass rate** | Number of required evaluation assertions meeting their pre-registered thresholds divided by all required assertions executed. Report both overall and by criticality; skipped tests count as not passed unless the customer approves an exception. | DeepEval local test output linked to Langfuse trace IDs and versioned evaluation datasets. DeepEval documents threshold-based pass/fail scoring and agentic, RAG, conversational, and safety metrics. [DeepEval metrics](https://deepeval.com/docs/metrics-introduction), [DeepEval local framework](https://deepeval.com/docs/faq). | **Goal:** **90–100%** overall on the signed regression suite and **100%** on critical policy, privacy, authorization, and irreversible-action cases. No aggregate score may offset a failed critical case. | Gates releases and measured autonomy; isolates quality changes by workflow and version. |
| **4. Policy denial rate** | OPA `deny` decisions divided by all policy decisions, reported by workflow, rule, actor class, and request-risk class. Also report unexplained denials, false denials confirmed by the policy owner, and unauthorized allows as separate counts. | OPA decision logs joined by `decision_id` to the Langfuse trace. OPA documents decision results, bundle metadata, input, timestamps, IDs, and masking. [OPA decision logs](https://www.openpolicyagent.org/docs/management-decision-logs). | **Goal:** after Phase 1 baseline, mix-normalized denial rate remains within **±5 percentage points** of that baseline; **0 unexplained denials** at phase exit; **0 unauthorized allows**. A high raw denial rate is not automatically bad—it may mean policy is working. | Detects policy drift, hostile or out-of-scope demand, and unusably strict controls without optimizing for fewer denials. |
| **5. Approval latency** | Elapsed business time from a valid `approval_required` event to approve, deny, or expire, measured as median and p95 by risk class. Clock pauses only for customer-declared outages or formally returned incomplete requests. | Langfuse approval spans/events plus the signed local approval ledger; OPA decision ID provides the policy linkage. Langfuse supports timing across request observations; OPA provides auditable decision IDs. [Langfuse observability](https://langfuse.com/docs/observability/overview), [OPA decision logs](https://www.openpolicyagent.org/docs/management-decision-logs). | **Goal for bounded medium-impact pilot actions:** median **≤4 business hours**, p95 **≤1 business day**, and **100%** disposition or explicit expiry. High-impact bands are **FOUNDER DECISION / customer authority decision** before kickoff. | Shows whether human control is operationally usable; prevents autonomy from being justified by a broken approval queue. |
| **6. Budget variance** | `(actual cumulative pilot cost - approved cumulative budget) / approved cumulative budget`, reported weekly and at phase exit. Also show committed-but-not-invoiced cost and forecast-to-complete. | LiteLLM spend/cost telemetry reconciled to the customer-approved budget ledger and task IDs. LiteLLM documents proxy cost tracking; Langfuse can break down cost by trace dimensions. [LiteLLM](https://docs.litellm.ai/), [Langfuse metrics](https://langfuse.com/docs/metrics/overview). | **Goal:** weekly and phase-exit variance between **-10% and +5%**, no unapproved positive variance, and forecast-to-complete within **±10%** of the active authorization. | Gives the contracting and program teams an early stop/re-scope signal while distinguishing planned underspend from uncontrolled overspend. |

### Metric controls

- The authoritative task ledger supplies the denominator for attempts; the observability platform may not define its own smaller population.
- Success rubrics, DeepEval thresholds, risk classes, business-hour calendars, cost allocation rules, and task-class ceilings are versioned and signed before Phase 2.
- Sensitive inputs in OPA decision logs are masked according to customer policy; OPA explicitly supports remove/upsert masking of decision-log fields. [OPA decision-log masking](https://www.openpolicyagent.org/docs/management-decision-logs).
- The dashboard displays counts beside percentages. Small samples and missing events are labeled; no statistical significance is implied.
- A threshold change is prospective. It never rewrites a prior phase result.
- Provider and enterprise-only features are separately licensed and approved; self-hosted open-source components do not by themselves establish compliance.

## 90-day execution plan

### Phase 1 — Days 1–30: install, bound, and baseline

**Purpose:** prove the controlled measurement loop before live operational claims are possible.

**Work:**

1. confirm the two pilot workflows, users, owners, data boundary, action allowlist, prohibited actions, approval matrix, and stop authority;
2. deploy the customer-approved connected or sovereign profile and record the exact component/model versions and licenses;
3. load only the approved corpus; capture provenance, retention, and deletion rules;
4. instrument a common task/trace/decision ID across Langfuse, LiteLLM, DeepEval, OPA, the approval ledger, and the authoritative task ledger;
5. register the six formulas, reports, task-success rubrics, evaluation suite, cost allocation, and target bands;
6. execute golden paths, denial paths, missing-evidence paths, recovery tests, and operator training; and
7. produce a baseline report that labels every number **observed in this pilot**, not prior performance.

**Day-30 exit criteria:**

- both workflow charters and the authority matrix are signed;
- 100% of selected components and models have version, origin-screen, license, and approval records;
- critical evaluation and policy-denial tests pass at 100%;
- high-impact and denial attempts have 100% trace coverage; overall trace coverage is at least 95%;
- every metric can be reproduced from raw records using the registered formula;
- zero unresolved unauthorized allows, unapproved external connectors, or unapproved positive budget variance; and
- the customer signs **enter supervised operation**, **remediate**, or **stop**.

### Phase 2 — Days 31–60: supervised operation

**Purpose:** operate the workflows with a human reviewing every consequential output or action while measuring real task mix.

**Work:**

1. admit work only through the signed pilot intake and identify each task’s class/risk;
2. require human approval before every external side effect and before any answer class the charter marks consequential;
3. review denials, failed evaluations, incomplete traces, approval aging, and spend every business day;
4. hold weekly program, security, data-owner, and contracting evidence reviews;
5. correct prompts, retrieval, tools, or policy only through versioned changes followed by regression evaluation; and
6. compare results to the goal bands without converting goals into claims.

**Day-60 exit criteria:**

- six metric reports reconcile to the authoritative task and budget ledgers;
- overall trace coverage is 95–100% and required high-impact/denial coverage is 100%;
- evaluation pass rate is 90–100% overall and 100% for all critical cases;
- zero unauthorized allows, zero unexplained denials, and every approval has a disposition or explicit expiry;
- unit cost is at or below each approved task-class ceiling and budget variance is inside the goal band;
- no open severity-1 safety, privacy, authorization, or evidence-integrity issue; and
- the customer signs **enter measured autonomy**, **continue supervision**, **remediate**, or **stop**.

### Phase 3 — Days 61–90: measured autonomy

**Purpose:** allow only the specific low/medium-impact steps proven in Phase 2 to execute without synchronous review; human control remains at the signed boundaries.

**Work:**

1. enable autonomy by allowlisted action, user group, data set, time window, and spend cap—never as a global switch;
2. keep policy, budget, identity, critical-evaluation, trace, and evidence gates fail-closed;
3. sample successful autonomous tasks daily and review all denials, retries, anomalies, and human escalations;
4. automatically return a workflow to supervised mode on a stop condition; and
5. assemble the day-90 evidence package and options analysis.

**Day-90 exit criteria:**

- all six metrics are within their active goal bands or have a signed exception with impact and remediation;
- critical evaluation cases remain at 100%, unauthorized allows remain at zero, and required trace coverage remains at 100%;
- recovery, revocation, budget-stop, and rollback tests succeed on the deployed version;
- every autonomous action is within the signed allowlist and reconstructable from evidence;
- the customer accepts the final evidence package and disposition of all pilot findings; and
- the customer signs **stop**, **extend under supervision**, or **authorize a separately scoped production transition**.

## Governance cadence and evidence package

| Cadence | Participants | Required output |
|---|---|---|
| Daily | operator, workflow owner | exception queue: failed/denied tasks, missing traces, aging approvals, spend anomaly, and disposition owner |
| Weekly | program lead, data owner, security/policy owner, contracting representative, technical lead | signed six-metric report, change log, risk/issue log, budget forecast, and next-week authorization |
| Phase gate | customer acceptance authority plus the above owners | exit-criteria checklist and explicit stop/remediate/advance decision |
| Day 90 | customer acceptance and contracting authorities | reproducible evidence package, options analysis, final disposition, and any separately authorized next scope |

The evidence package contains the workflow charters; component/model/license and origin register; architecture and data-flow diagrams; policy and budget bundles; evaluation datasets/results; task, trace, decision, approval, and cost exports; change and issue logs; training record; recovery/rollback proof; six-metric calculations; and all signed gate decisions.

## Stop conditions

The named stop authority immediately returns the affected workflow to supervised mode—or stops it—on any unauthorized allow, confirmed sensitive-data exposure, unapproved external dependency, critical-evaluation failure, unreconstructable high-impact action, lost approval enforcement, positive budget variance above authorization, or evidence-integrity failure. Resumption requires root-cause evidence, remediation, regression proof, and a signed customer decision.

## Contracting inputs required before kickoff

1. named acceptance, data, security/policy, budget, and stop authorities;
2. two bounded workflow charters and success rubrics;
3. approved users, corpus, retention rules, deployment boundary, models, tools, and action allowlist;
4. task-class cost ceilings, total pilot authorization, and cost allocation method;
5. evaluation suite, critical cases, trace schema, evidence retention, and masking rules;
6. business-hour calendar and approval service levels by risk class;
7. incident, rollback, controlled export/reconnection, and end-of-pilot data-disposition procedures; and
8. contracting vehicle and participation structure consistent with the approved protégé/subcontract lane—**FOUNDER DECISION / contracting authority decision**.

Until these inputs are signed, day 1 does not start. This keeps the pilot an auditable test of a bounded operating contract, not an open-ended demonstration.
