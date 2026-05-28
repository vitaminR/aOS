<!-- markdownlint-disable MD041 MD060 -->

> **PREAMBLE** | Type: aOS7 Research Brief | Status: seed | Owner: nymil
> Created: 2026-05-26 | Source PRD: `30.PRDs/PRD19-Copilot-AI-Credits-Token-Efficiency.md`
> Purpose: Ingest Copilot AI Credits and token-efficiency research into the `{a}OS` reference model before live Explorer catalog edits.

# {a}OS Research Brief — Copilot AI Credits & Token-Efficiency Routing

## 1. Research trigger

GitHub Copilot moves to **usage-based billing with GitHub AI Credits on June 1, 2026**. This changes agentic coding from a mostly hidden subscription cost into a visible token-metered infrastructure cost.

For `{a}OS`, this is not just a pricing event. It touches every stratum:

- L7: user approval and anxiety-safe billing UX
- L6: budget policy, spend controls, model rules
- L5: usage observability, cost telemetry, benchmarking
- L4: model/agent routing decisions
- L3: execution tools and coding-agent surfaces
- L2: context compression and memory reuse
- L1: model/provider/runtime economics

## 2. Canonical facts

| Fact | Value | AOS7 layer |
|---|---:|---|
| Transition date | June 1, 2026 | L6/L1 |
| Billing unit | GitHub AI Credits | L6 |
| Credit value | 1 AI Credit = $0.01 USD | L6/L5 |
| Cost basis | input + cached input + output tokens; Anthropic also cache-write | L1/L5 |
| Code completions | Not billed in AI credits on paid plans | L7/L6 |
| Copilot Chat/CLI/agents | Billed in AI credits | L3/L6 |
| Copilot code review | AI Credits + GitHub Actions minutes | L3/L5/L6 |
| Individual plan credits | Pro 1,500; Pro+ 7,000; Max 20,000 monthly | L6 |
| Business/Enterprise credits | Business 1,900/user; Enterprise 3,900/user; pooled | L6 |
| Business promo | 3,000/7,000 per user Jun 1–Sep 1 | L6 |
| Claude Max 20x | $200/month, more usage than Pro, includes Claude Code | L1/L3 |

## 3. Stratum mapping

### L7 — Experience & Intent

User-facing need: prevent cost panic from becoming tool thrash.

Candidate primitives:

- `spend_warning_prompt`
- `budget_confirmation_gate`
- `one_next_action_cost_mode`
- `agent_handoff_cost_contract`

Research questions:

- What warning thresholds reduce anxiety without creating alert fatigue?
- Should Kotana surface “cost risk” as a normal next-action score?
- How should agents explain billing risk without doom language?

### L6 — Governance & Trust

User-facing need: set policy before agents spend.

Candidate primitives:

- `ai_credit_budget`
- `model_tier_policy`
- `overage_cap`
- `frontier_model_approval`
- `subscription_vs_api_boundary`

Research questions:

- Should default Copilot overage be $0, $10, or $25 in June?
- What model rules should be enforced by repo, file type, or task class?
- Can budget policies be encoded in instruction files, tool wrappers, or both?

### L5 — Observability & Evaluation

User-facing need: know what burned credits and whether it was worth it.

Candidate primitives:

- `aic_usage_report`
- `model_cost_trace`
- `quality_per_credit_score`
- `token_waste_pattern`
- `agent_benchmark_packet`

Research questions:

- How should GitHub CSVs be normalized into Codepro telemetry?
- Which tasks should have cost-per-success benchmarks?
- Can Artificial Analysis results seed AOS7 evaluation cards?

### L4 — Orchestration & Decisioning

User-facing need: route the task to the cheapest competent executor.

Candidate primitives:

- `model_router`
- `task_classifier`
- `architectural_stop`
- `cheap_scout_then_frontier_synth`
- `context_pack_selector`

Research questions:

- What task classes can reliably use cheap/free models?
- When should architecture tasks stop and require a mini-ADR?
- How do we prevent agents from escalating model tier just because context is messy?

### L3 — Execution & Interfaces

User-facing need: choose execution surfaces safely.

Candidate products/tools:

| Tool | Initial role | Evidence status |
|---|---|---|
| GitHub Copilot | VS Code completions, small patches, chat/agent with budget cap | Official docs verified |
| Claude Code | heavy coding, architecture, terminal/IDE agent | Official docs verified |
| Gemini CLI | large-context scout, web fetch/search, MCP, checkpointing | Repo README verified |
| Codex | PR execution, skills, automations, worktrees | Product page verified |
| OpenCode | open-source provider-agnostic harness | Product page verified |
| Cline | IDE/CLI agent, skills/rules/MCP, scheduled/multi-agent | Repo README verified |
| Continue | source-controlled AI PR checks | Product page verified |

### L2 — Knowledge & Memory

User-facing need: stop paying agents to rediscover known context.

Candidate primitives:

- `repo_context_pack`
- `do_not_read_manifest`
- `source_register`
- `handoff_summary`
- `context_cache_key`

Research questions:

- Which Codepro folders are safe to summarize once and reuse?
- Can repo memories become the default context source before file reads?
- What context pack shape gives enough signal in ≤2 pages?

### L1 — Models & Infrastructure

User-facing need: understand the model/runtime substrate and quota boundaries.

Candidate products/tools:

| Tool/provider | Initial role | AOS7 placement |
|---|---|---|
| OpenRouter | provider broker, model fallback, cheap model experiments | L1 primary, L6 secondary |
| Claude Max | subscription-heavy reasoning pool | L1 primary, L3 secondary |
| Gemini API/CLI | large-context and free quota route | L1 primary, L3 secondary |
| GitHub AI Credits | billing substrate for Copilot models | L1/L6 cross-cut |
| Artificial Analysis | external benchmark/cost data source | L5 primary, L1 secondary |

## 4. Candidate AOS7 catalog backlog

Do **not** edit live `7.aOS-Explorer/data/products.json` until each candidate has an evidence packet and a final stratum decision.

| Candidate ID | Name | Type | Proposed primary | Proposed secondary | Evidence needed | Priority |
|---|---|---|---|---|---|---:|
| `github-ai-credits` | GitHub AI Credits | governance primitive | L6 Governance & Trust | L5, L1 | GitHub docs + pricing table | 1 |
| `copilot-billing-preview` | Copilot Billing Preview | tool | L5 Observability & Evaluation | L6 | Preview page + docs | 1 |
| `claude-max-code` | Claude Max + Claude Code | platform/tool | L1 Models & Infrastructure | L3, L4 | Anthropic pricing + Code docs | 1 |
| `gemini-cli` | Gemini CLI | tool | L3 Execution & Interfaces | L1, L4 | GitHub README + docs | 1 |
| `codex` | OpenAI Codex | agent/platform | L3 Execution & Interfaces | L4, L5 | OpenAI product/docs | 2 |
| `opencode` | OpenCode | framework/tool | L4 Orchestration & Decisioning | L3, L6 | OpenCode docs/GitHub | 2 |
| `cline` | Cline | framework/tool | L3 Execution & Interfaces | L4, L6 | GitHub README/docs | 2 |
| `continue-checks` | Continue Checks | tool | L5 Observability & Evaluation | L6 | Continue docs/pricing | 3 |
| `openrouter` | OpenRouter | infrastructure | L1 Models & Infrastructure | L6 | OpenRouter docs/pricing/privacy | 2 |
| `artificial-analysis-coding-index` | Artificial Analysis Coding Agent Index | benchmark | L5 Observability & Evaluation | L1 | Benchmark methodology | 1 |

## 5. Research source register

| Source | URL | Status |
|---|---|---|
| GitHub Copilot Billing Preview | `https://copilot-billing-preview.github.com/` | Verified |
| GitHub Copilot usage-based billing blog | `https://gh.io/copilot-billing-blog` | Verified |
| GitHub individual usage-based billing docs | `https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-individuals` | Verified |
| GitHub organization usage-based billing docs | `https://docs.github.com/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises` | Verified |
| GitHub model pricing docs | `https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing` | Verified |
| GitHub raw model pricing data | `https://raw.githubusercontent.com/github/docs/main/data/tables/copilot/models-and-pricing.yml` | Verified |
| GitHub annual multiplier docs | `https://docs.github.com/en/copilot/reference/copilot-billing/model-multipliers-for-annual-plans` | Verified |
| GitHub Community FAQ | `https://github.com/orgs/community/discussions/192948` | Verified, community comments are leads only |
| Anthropic Claude Max support | `https://support.claude.com/en/articles/11049741-what-is-the-max-plan` | Verified |
| Anthropic Claude Code support | `https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan` | Verified |
| Claude Code docs | `https://docs.anthropic.com/en/docs/claude-code/overview` | Verified |
| Gemini CLI repo | `https://github.com/google-gemini/gemini-cli` | Verified |
| OpenAI Codex | `https://openai.com/codex/` | Verified |
| OpenCode | `https://opencode.ai/` | Verified |
| Cline | `https://github.com/cline/cline` | Verified |
| Continue | `https://www.continue.dev/` | Verified |
| OpenRouter | `https://openrouter.ai/` | Verified |
| Artificial Analysis Coding Agents | `https://artificialanalysis.ai/agents/coding-agents` | Verified |

## 6. Next ingestion actions

1. Build evidence packets for the ten candidate backlog items.
2. Decide whether `github-ai-credits` is a product card, concept card, or governance primitive in the Explorer schema.
3. Add `cost-awareness` / `token-efficiency` as concept tags if the Explorer schema supports them.
4. After PRD Phase 2c catalog SSoT is resolved, insert the verified candidates into the canonical catalog.
5. Add a periodic `tool-watch` report under L5/L6 for billing/pricing drift.

## 7. Preliminary `{a}OS` thesis

Token-metered AI shifts agentic systems from “model selection as UX choice” to “model selection as runtime governance.” In `{a}OS`, model routing is no longer only L4 orchestration. It is a cross-stratum behavior:

- L1 knows which models/providers exist and what they cost.
- L2 minimizes context sent to them.
- L3 invokes them through safe interfaces.
- L4 chooses the cheapest competent route.
- L5 measures quality-per-credit.
- L6 enforces budget, privacy, and spend policy.
- L7 keeps the user informed and in control.

That makes Copilot AI Credits a useful stress test for the whole `{a}OS` reference model.

## 8. Ingestion recommendation

**Recommended placement:** `L5 — Orchestration & Evaluation` with a hard cross-link to `L6 — Governance & Trust`.

**Why this placement wins:**

- The evidence packets now show the cost-efficiency problem is operational before it is policy-only.
- The stack needs routing, measurement, and cache-aware evaluation first.
- Governance still matters, but it is the guardrail on top of the operating layer, not the entire concept.

**Recommended exemplar set for the live AOS7 card:**

- Gateway / routing: `LiteLLM`, `OpenRouter`, `RouteLLM`
- Execution surfaces: `Claude Code`, `Gemini CLI`, `Codex`, `OpenCode`, `Cline`
- Observability / evaluation: `Helicone`, `Artificial Analysis`, `Copilot Billing Preview`
- Governance primitive: `GitHub AI Credits`

**Canonical research artifacts:**

- `0.agentic/00_Ledger/COST-MIGRATION/research/findings.md`
- `0.agentic/00_Ledger/COST-MIGRATION/adoption-shortlist.md`

**Tag cluster:** `#cost-efficiency #llmops #modelrouting #promptcaching #tokenefficiency #agenticai #observability`

**Final note:** if Phase 2c SSoT is green, ingest the concept card as L5-first and link it to Governance rather than duplicating the full evidence packet in the live catalog.
