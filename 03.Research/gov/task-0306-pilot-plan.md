# {a}OS 90 Day Government Pilot Plan (task-0306)

> Companion to the [Government Proposal](../aos7-government-proposal-2026-08.md) Section 6.
> Every number in this plan is a TARGET the pilot is designed to measure, not a claim of past performance. {a}OS has no federal past performance and says so; the pilot exists to produce the first measured record, inside the agency's own boundary, on the agency's own hardware.

## The offer in one paragraph

In 90 days, on one government owned Linux server, the agency gets a working agentic AI system for three of its own workflows, a live scorecard on six measurable metrics, and an evidence package (traces, policy decisions, approval records) formatted for its own authorization process. If the system fails its targets, the agency keeps the hardware, the open source stack, and every piece of evidence, and has lost only the pilot fee. There is no license to cancel and no data to repatriate, because nothing ever left.

## The six axis metrics

These come from the Agentic Reference Stack's two cross cutting axes. Each is defined, measured by a named component, and given a target band. Targets are goals; the baseline phase establishes what the agency's workflows actually cost today.

| Metric | Definition | Measured by | Target band (goal) |
|---|---|---|---|
| Cost per successful task | Total model spend divided by tasks completed and accepted | LiteLLM gateway ledger reconciled against provider usage | Declining month over month; unit cost visible per task class by day 45 |
| Trace coverage | Share of agent actions carrying a complete OpenTelemetry GenAI trace | Langfuse over OTLP | 100 percent from day 1; any untraced action is a defect, not a statistic |
| Eval pass rate | Share of scheduled evaluation cases passing per week | DeepEval suite run in CI with exit codes | Above 90 percent by day 60 on the three pilot workflows |
| Policy denial rate | Share of attempted agent actions denied by the policy gate | OPA decision logs | Nonzero and reviewed weekly; zero denials means the gate is not testing anything |
| Approval latency | Time from an agent raising a hand to a named human deciding | Decision queue timestamps | Median under 4 business hours by day 60 |
| Budget variance | Actual spend versus the hard budget set per agent per day | LiteLLM virtual key enforcement records | Overspend is impossible by construction; variance reporting proves the ceiling held |

## Phase 1, days 1 to 30: install and baseline

The stack deploys inside the agency boundary on agency hardware. The three pilot workflows are selected with the agency (candidates: a form intake, a case routing step, a records reconciliation). Each is instrumented BEFORE any automation: what it costs today in hours and rework is the baseline every later number is judged against.

Exit criteria: stack running on agency hardware with all traffic through the gateway; the disconnect test passed live (network cut, agents keep working, traces keep writing); the allowlist refusal test passed live; three workflows instrumented with baselines recorded; agency staff hold the admin credentials, not the vendor.

## Phase 2, days 31 to 60: supervised operation

Agents work the three workflows with every action requiring named human approval through the decision queue. This is deliberately slower than the end state; its purpose is trust and data. Weekly evidence reviews walk agency staff through real traces of real actions, including the failures and denials, because reviewing only successes teaches nothing.

Exit criteria: all six metrics reporting weekly; eval suite running in CI with versioned cases; at least one policy denial and one honest failure reviewed with staff; approval latency median established.

## Phase 3, days 61 to 90: measured autonomy

Action classes that earned trust in Phase 2 are promoted, by the agency's own sign off, to run gated but unattended: the policy gate and budget ceiling still check every action, the trace still writes, but no human click is required for the promoted classes. Everything else stays supervised. The final two weeks produce the scorecard against targets and the evidence package: complete traces, policy decision logs, approval records, eval history, and the SBOM, formatted as inputs to the agency's authorization process.

Exit criteria: promoted action classes running unattended for 14 consecutive days inside policy and budget gates; final scorecard delivered with every metric against its target band; evidence package handed to the agency's assessment team; a keep, grow, or stop decision the agency can make from measurements rather than a demo.

## What the agency risks and what it keeps

The pilot's honest failure mode is that the metrics miss their bands. Even then the agency keeps: the hardware, the full open source stack under its own control, staff trained on it, the baseline study of its own workflows, and an evidence corpus about how agentic AI actually behaves on its data. The vendor lock in exposure is zero by construction, which is the point of the whole architecture.
