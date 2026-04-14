---
post_id: AFS07
character: Mentor Architect
status: PLOT_PROPOSED
recommended: A
---

# AFS07 — Visual Direction: "Agent Maturity: What's GA, What's Preview, What Matters"

## Plot Options

### Plot A — Agent Maturity Matrix (Recommended)

Clean table/matrix with 3 rows and 4 columns:

| Agent Type | Status | VNet Support | Production Readiness |
|---|---|---|---|
| Prompt Agents | GA (green) | Full (green) | Ready (green) |
| Workflow Agents | Preview (amber) | Partial (amber) | Not Ready (red) |
| Hosted Agents | Preview (amber) | None (red) | Not Ready (red) |

Dark background. Status indicators are colored pills/badges, not text. A single horizontal rule separates the GA row from the preview rows — visually reinforcing the "line" between production-safe and not.

**Pros:** Immediate clarity. One glance tells the entire story. Matches the "tired architect" voice — no fluff, just the matrix.
**Cons:** Simple. But that's also the point.

### Plot B — Traffic Light Stack

Three agent types stacked vertically like a traffic light. Prompt Agents = green light (go). Workflow Agents = amber light (caution). Hosted Agents = red light (stop). Each light has a one-line annotation: "GA + VNet", "Preview + Partial VNet", "Preview + No VNet".

**Pros:** Visceral metaphor. Instantly communicates risk gradient.
**Cons:** May oversimplify — workflow agents aren't "stop", they're "caution." Could feel reductive.

### Plot C — The Maturity Staircase

Three steps ascending left to right. Bottom step (widest, green): Prompt Agents / GA / Full VNet. Middle step (amber): Workflow Agents / Preview / Partial VNet. Top step (narrowest, red outline, dashed): Hosted Agents / Preview / No VNet. Label: "Build from the bottom."

**Pros:** Implies a progression and a recommendation (start at the bottom).
**Cons:** May imply hosted agents are "better" because they're at the top. Needs careful visual weighting.

## Recommended

**Plot A** — The matrix. It matches the post's voice (no metaphor, just facts), communicates the entire message at mobile size, and serves as a reference the reader can screenshot. The Mentor Architect doesn't need a clever visual — they need a clear one.

## Art Direction Notes

- Dark or neutral background (consistent with series)
- Green / amber / red color coding — accessible (add icons or text labels, not color alone)
- Sans-serif typography
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- The horizontal line between GA and Preview rows is the visual thesis — "this is the production line"
- No vendor logos. "Azure AI Foundry" can appear as context text but not as branding.
- Consider a small lock icon next to VNet entries to reinforce "network isolation" visually
