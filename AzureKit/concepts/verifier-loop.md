> **PREAMBLE** | Type: concept-doc | Status: active
> Owner: nymil | Updated: 2026-05-04 | Goal: Document the auto-verifier (Builder/Verifier) pattern and how it slots into AzureKit
> Cross-refs: `00-reference-architecture.md` §3 S4/S5, §5 #3 Cheap-First Default, `concepts/atomic-claims.md`

# The Auto-Verifier Loop

## What It Is

A two-agent execution pattern where one agent (the **Builder**) produces work and a second, *unprompted* agent (the **Verifier**) immediately reviews it against structured rules. The Verifier emits a scorecard. On pass, the work is delivered. On fail, the Verifier feeds a corrective prompt back to the Builder and the loop repeats until pass — or the circuit breaker trips.

The pattern's economic claim: **trade cheap inference tokens to save expensive ones, and to save the most expensive resource of all — human review time.**

## Why It Belongs in AzureKit

The Verifier Loop is a near-perfect match for three architectural constraints in the AzureKit reference architecture:

1. **Cheap-First Default (§5 #3).** The local Mistral on the Crucible is the ideal Verifier substrate — cheap, unmetered, fast. Cloud models do the expensive build; local models do the review.
2. **3-Strike Circuit Breaker (§3 S4).** The Verifier's pass/fail boolean is *exactly* the input the circuit breaker needs. Three Verifier "fail"s in a row = fatal termination.
3. **Metadata-Only Logging (§3 S5).** Verifier scorecards are pure metadata — boolean atomic claims, latency, retry count. They never contain prompt payloads. They go to Azure Monitor without spillage risk.

It also reinforces the anti-vibe-coding stance: the Verifier acts on every Builder output without human approval, so the human can't accidentally rubber-stamp slop.

## Architectural Placement

```
                S7 — human intent (10%)
                       │
                       ▼
                S4 — orchestrator
                ┌──────────────┐
                │  state runner│
                └───┬──────────┘
                    │ task
                    ▼
                S1 ── Builder (cheap-first ladder)
                       Mistral local ──▶ cloud small ──▶ premium
                       │
                       │ output
                       ▼
                S5 ── Verifier (always Mistral local)
                       │
                       │ atomic-claim scorecard
                       ▼
                S4 — circuit breaker
                       │
            pass ◀─────┴─────▶ fail (count++)
              │                  │
              ▼                  ▼
         S2 — write          retry Builder
         to run-log          with feedback
                             (3-strike fatal)
```

## Why the Verifier Stays Local

Two reasons, both load-bearing for the cheap-first economic story:

1. **Verification is a smaller cognitive task than generation.** Checking "does this JSON have all required keys" is far below "design a state machine." A 7B–70B local model handles verification at parity with frontier cloud models for most claim types.
2. **The Verifier runs on every Builder output, including failures.** If the Verifier itself were cloud-hosted, you'd burn cloud tokens on failed builds — the worst case. Keeping it local makes failed builds *free*.

## Token-Budget Math

For a workflow that today makes one cloud call per task plus one human-review burn:

| Scenario | Cloud calls per task | Verifier calls per task | Human review |
|---|---|---|---|
| Today (no verifier) | 1 build + N rework prompts | 0 | full |
| With local verifier, first-pass success rate 70% | 1 + 0.3 retry | 1 + 0.3 retry (free, local) | spot-check only |
| With local verifier, first-pass success rate 90% | 1 + 0.1 retry | 1 + 0.1 retry (free, local) | spot-check only |

Reference projection: **30–50% reduction in cloud token spend** on tasks with structurable verification rules (provisioning, schema generation, doc writes, code patches). Larger reduction on rate-limited frontier tiers.

## Wiring Into the Self-Documenting Scribe

The Self-Documenting Scribe (`00-reference-architecture.md` §4) is already a Builder/Verifier shape — it just doesn't name it that way:

| Reference §4.1 step | Pattern role |
|---|---|
| 1. Trigger (CLI/API action) | Task input |
| 2. Ingestion (JSON to listener) | S3 interface |
| 3. Processing (local model identifies stratum) | **Builder** |
| 4. Verification (Python script validates JSON, no spillage) | **Verifier** (mechanical) |
| 5. Memory Write (run-log.md append) | S2 commit |

Today's verifier in §4.1 is a static schema check. **The upgrade path:** swap the static script for a local-model Verifier that runs atomic claims against the Builder's stratum-classification output. Now §4.1 #4 catches semantic errors (wrong stratum assigned, mis-tagged risk category) on top of structural ones.

## Verifier ↔ APIM Coupling

For the share of tasks that escalate to cloud, APIM is the choke point. The Verifier's pass/fail decision should be one of APIM's gating signals:

1. Builder (local) produces a draft.
2. Verifier (local) scores it.
3. **If Verifier passes**, orchestrator may invoke APIM-routed cloud Builder for refinement (paid).
4. **If Verifier fails**, retry locally — *no APIM call is made*.

This makes the Verifier a hard cost control: failed work never reaches the paid lane.

## Failure Modes

| Failure | Symptom | Mitigation |
|---|---|---|
| Verifier rubber-stamps everything | First-pass rate ≈ 100%, quality bugs in production | Periodic human spot-check; track false-positive rate as an S5 metric |
| Verifier rejects everything | Circuit breaker trips constantly, no progress | Tune claim thresholds; widen passing criteria |
| Claim set incomplete | Bugs slip through claims that don't exist yet | Treat each escaped bug as an atomic-claim authoring task |
| Verifier model degrades on retry | Same fail signal, no progress, breaker fatigue | 3-strike fatal termination per reference §3 S4 |
| Builder ↔ Verifier collusion (same model both sides) | Verifier blind to Builder's mistakes | Use *different* local models for Builder and Verifier |

## Implementation Notes

When this is built (separate spec):

- **Recommended host:** as a Pi extension (`@<scope>/pi-verifier`) — Pi's 25+ hook surface fits the Builder/Verifier loop natively. See `concepts/pi-harness-primer.md`.
- **Alt host:** standalone Python orchestrator (`aos7-ai-platform/04-s4-orchestration/verifier_loop.py`) for environments without Node.
- Atomic-claim definitions live in `aos7-ai-platform/04-s4-orchestration/claims/*.yaml` (one file per task type).
- Scorecards write JSONL to `aos7-ai-platform/05-s5-observability/scorecards/` (local) and metadata-only to Azure Monitor.
- The cheap-first model selector is shared with the Scribe — same local endpoint, different prompt template per role.
