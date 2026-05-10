> **PREAMBLE** | Type: standard | Status: active | Goal: G1 G4
> Owner: nymil | Created: 2026-05-09 | Scope: workspace-wide
> Companion to: teach-through-every-change.md

# aOS7 Change Presentation Standard

## How to Use This Standard

Every code change or architectural decision is tagged with its **primary stratum** (the layer where the change has the most weight) and presented using that stratum's standard 80/20 explanation format and diagram type. Cross-stratum changes list all affected strata in priority order, but lead with the primary one's format. This gives Johnathon and the team a predictable, scannable shape for every change — same vocabulary, same diagrams, same depth, every time.

## The 7-Stratum Change Presentation Table

| Stratum | 80/20 Explanation Standard | Diagram Type | Standard Terminology |
|---|---|---|---|
| **L7 — Intent & Experience** | One sentence on the user outcome, one sentence on the felt change, one sentence on success criteria from the user's point of view. | User journey map or before/after storyboard | "This change shifts the user experience from `<before-state>` to `<after-state>`, measured by `<outcome-signal>`." |
| **L6 — Governance & Strategy** | The decision in one sentence, the alternatives rejected in one sentence, the policy or goal it aligns to in one sentence. | Decision tree or trade-off matrix | "We chose `<option>` over `<alternatives>` because it best advances `<goal-tag>` under constraint `<constraint>`." |
| **L5 — Evaluation & Observability** | What we are now measuring, what threshold defines success or failure, where the signal surfaces (dashboard, log, alert). | Dashboard mock or signal-flow diagram | "We now observe `<metric>` via `<surface>` and treat `<threshold>` as the pass/fail line." |
| **L4 — Orchestration & Workflow** | The sequence of steps in plain English, the trigger that starts it, the terminal state that ends it. | Sequence diagram or flowchart | "Workflow `<name>` is triggered by `<event>`, runs `<steps>`, and terminates at `<end-state>`." |
| **L3 — Execution & Skills** | What the code or skill does in one sentence, the input contract, the output contract. | Function/skill block diagram with input/output arrows | "Skill `<name>` takes `<inputs>`, performs `<operation>`, and returns `<outputs>`." |
| **L2 — Memory & Knowledge** | What is now stored or recalled, the schema or shape of the data, the retention/eviction rule. | Schema diagram or knowledge-graph snippet | "We persist `<entity>` shaped as `<schema>` with retention `<rule>` and recall via `<lookup-key>`." |
| **L1 — Runtime & Infrastructure** | Where it runs, what it costs, what fails when it fails. | Layer diagram or deployment topology | "Runs on `<host/runtime>` at approximately `<cost-unit>`, with failure mode `<mode>` and fallback `<fallback>`." |

## Quick-Reference Heuristic

- **User-facing change?** → Lead with L7
- **Policy or "should we?" decision?** → Lead with L6
- **New metric, alarm, or test?** → Lead with L5
- **New pipeline, sequence, or trigger?** → Lead with L4
- **New code, skill, or tool?** → Lead with L3
- **New data, schema, or recall behavior?** → Lead with L2
- **New host, cost, or compute change?** → Lead with L1

If a change touches three or more strata, it is an architectural decision and requires an ADR using all relevant rows, not just the primary.
