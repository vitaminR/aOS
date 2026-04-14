---
post_id: AFS10
character: Regulator
status: PLOT_PROPOSED
recommended: B
---

# AFS10 — Visual Direction: "The Observability Paradox"

## Plot Options

### Plot A — Broken Pipeline (Linear Flow)

A horizontal pipeline diagram: Foundry Agent -> OpenTelemetry Traces -> Application Insights. First row shows the pipeline working (green arrows, non-isolated). Second row shows the same pipeline with a private endpoint shield around App Insights and a red X breaking the connection.

Label row 1: "Without network isolation — tracing works"
Label row 2: "With network isolation — tracing breaks"

**Pros:** Simple, immediately communicates the paradox. Easy to produce.
**Cons:** Does not show the workaround. Only names the problem.

### Plot B — Workaround Architecture (Recommended)

Split into two zones on a dark background:

**Left zone (red X overlay):** "The broken path"

- Production Spoke VNet containing Foundry Resource (private endpoint) connected to Private App Insights (private endpoint). Red dashed line with X between them. Label: "Tracing fails."

**Right zone (green check):** "The workaround"

- Hub-spoke topology. Hub VNet with Azure Firewall at center. Production Spoke with Foundry Resource (private endpoint). Observability Spoke with non-private App Insights, NSG-restricted ingress. Green arrow showing traces flowing from Foundry through VNet peering to the observability spoke. Log Analytics Workspace shown as the downstream sink.

Label: "Peered App Insights — isolated by network, not by endpoint"

**Pros:** Shows both the problem and the solution in one image. Architecture-grade visual. High save/share potential for architects. Matches the post's constructive tone.
**Cons:** More complex to produce. Requires careful layout to work at mobile size.

### Plot C — The Paradox Box

A single box with two requirements on opposite sides pointing inward, colliding in the center:

Left arrow: "Require: Network Isolation" (shield icon)
Right arrow: "Require: Observability" (telescope/trace icon)
Center collision: Red spark/conflict symbol
Below: "Both required. Mutually exclusive. Unless you architect around it."

**Pros:** Visceral paradox framing. Works at any size. High engagement as a standalone image.
**Cons:** Abstract. Does not show the architectural fix. Better suited for a slide deck than a LinkedIn teaching post.

## Recommended

**Plot B** — The workaround architecture diagram. This post's value is the fix, not just the problem. Plot B shows both the broken path and the working workaround in a single image. Architects will screenshot and share it. The split layout (broken vs working) creates visual tension that matches the paradox framing.

## Art Direction Notes

- Dark or neutral background (consistent with series visual identity)
- Two distinct zones: broken (left, muted/red tones) vs working (right, clean/green accents)
- No vendor logos — use generic "Foundry Resource," "App Insights," "VNet" labels
- Sans-serif typography, clean lines
- Must work at LinkedIn mobile size (1080x1080 square preferred for architecture diagrams)
- The peering connection should be visually prominent — it is the key insight
- NSG icon or label on the observability spoke to show it is access-restricted, not open
- Include a small legend: red X = broken, green arrow = working path
