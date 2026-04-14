---
post_id: AFS09
character: Builder
status: PLOT_PROPOSED
recommended: B
---

# AFS09 — Visual Direction: "Cost Governance Is Not a Feature — It's an Architecture"

## Plot Options

### Plot A — Simple Flow Diagram (Horizontal)

Left-to-right flow: `Teams/Agents` -> `APIM AI Gateway` -> `Azure AI Foundry`. Below APIM, a downward branch to three boxes: `Metering`, `Budgets`, `Kill Switch`. Clean arrows, dark background, minimal labels.

**Pros:** Simple, immediately readable at LinkedIn mobile size. Clear message: APIM is the enforcement layer.
**Cons:** May be too simple for the "highest engagement post" ambition. Does not show the feedback loop.

### Plot B — Cost Governance Architecture (Recommended)

Full architecture diagram with the enforcement feedback loop visible:

```
┌─────────────────────────────────────────────────────────┐
│                   COST GOVERNANCE LAYER                   │
│                                                           │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │ Team A   │───→│              │───→│ Azure AI     │   │
│  │ Agent    │    │   APIM       │    │ Foundry      │   │
│  ├──────────┤    │   AI Gateway │    │              │   │
│  │ Team B   │───→│              │    │ - Models     │   │
│  │ Agent    │    │  - Rate Limit│    │ - Agents     │   │
│  ├──────────┤    │  - Token Meter    │ - Search     │   │
│  │ Team C   │───→│  - Kill Switch   │ - Storage    │   │
│  │ Agent    │    │              │    │              │   │
│  └──────────┘    └──────┬───────┘    └──────────────┘   │
│                         │                                 │
│                    ┌────▼────┐                            │
│                    │  Log    │                            │
│                    │Analytics│                            │
│                    └────┬────┘                            │
│              ┌──────────┼──────────┐                     │
│         ┌────▼────┐ ┌───▼───┐ ┌───▼────┐               │
│         │Per-Team │ │Anomaly│ │Budget  │               │
│         │Dashboard│ │Alerts │ │Enforce │               │
│         └─────────┘ └───────┘ └────────┘               │
└─────────────────────────────────────────────────────────┘
```

Top section: multiple teams/agents flowing through a single APIM gateway to Foundry. Middle: metering pipeline to Log Analytics. Bottom: three outputs (dashboards, alerts, enforcement). A red feedback arrow from "Budget Enforce" back up to APIM showing the kill switch loop.

**Pros:** Tells the full story. Shows multi-team, single gateway, enforcement feedback loop. Matches the post's architecture teaching. The feedback arrow (enforcement → kill switch) is the visual punch.
**Cons:** More complex to render. Must be clean at mobile size.

### Plot C — Before/After Split

Left side: "Without Cost Governance" — agents firing directly at Foundry endpoints, no metering, a billing graph spiking upward at 3 AM with a red alert icon. Right side: "With Cost Governance" — same agents routed through APIM, flat billing graph, dashboard showing per-team breakdown.

Label left: "What happens at 3 AM"
Label right: "What should happen at 3 AM"

**Pros:** Emotional contrast. "3 AM" ties directly to the post's hook. Very shareable.
**Cons:** Less architecturally educational. Prioritizes engagement over teaching.

## Recommended

**Plot B** — The full architecture diagram. This is the highest-engagement post in the series and the teaching objective is the architecture itself. The visual must show the enforcement feedback loop — that is the key insight (cost governance is a loop, not a one-time configuration). Plot C is tempting for engagement but undersells the architecture.

**Compromise option:** Use Plot B as the primary image and Plot C framing as the alt-text or carousel second slide if publishing as a multi-image post.

## Art Direction Notes

- Dark or neutral background (consistent with series visual identity)
- Sans-serif typography, clean lines
- APIM box should be visually prominent — it is the hero of this diagram
- The feedback arrow (enforcement → kill switch → APIM) should be in a warning color (amber/orange) to draw the eye
- Team labels (A, B, C) should feel generic — this is about the pattern, not specific teams
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- No vendor logos — "APIM" and "Foundry" are sufficient labels
- Include a subtle "$" icon or cost-related visual cue to reinforce the cost governance theme
