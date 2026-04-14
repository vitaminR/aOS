---
post_id: AFS03
character: Visionary
status: PLOT_PROPOSED
recommended: A
priority: CRITICAL — this is the framework debut visual for the entire series
---

# AFS03 — Visual Direction: "Where Governance Actually Lives"

## Context

This is the single most important visual in the 12-post series. It introduces the {a}OS 7-stratum model and maps Foundry's coverage. Every subsequent post references this framework. The visual must be clear enough to understand without reading the post, and memorable enough to become the series anchor image.

## Plot Options

### Plot A — 7-Stratum Heatmap with Foundry Overlay (Recommended)

Seven horizontal bars stacked vertically (L1 at bottom, L7 at top). Each bar color-coded by Foundry coverage strength:

| Stratum | Label | Coverage Color |
|:---:|---|---|
| L7 | Experience & Intent | Orange-red (Partial) |
| L6 | Governance & Trust | Orange-red (Partial) |
| L5 | Observability & Evaluation | Orange-red (Partial) |
| L4 | Orchestration & Decisioning | Yellow (Partial — preview) |
| L3 | Execution & Interfaces | Green (Good) |
| L2 | Knowledge & Memory | Yellow-green (Partial) |
| L1 | Models & Infrastructure | Deep green (Strong) |

Right side of each bar: brief annotation of what Foundry provides vs what you build.

A clear visual dividing line between L4 and L5 labeled: "Above this line — yours to build."

Title: "{a}OS 7-Stratum Model — Azure AI Foundry Coverage"
Subtitle: "Where the platform ends and your architecture begins"

**Pros:** Immediately communicates the coverage gradient. The visual dividing line between L4 and L5 is the thesis in one glance. Reusable as reference in all subsequent posts.
**Cons:** Seven bars is dense. Requires careful typography at LinkedIn mobile size.

### Plot B — Split Stack (Foundry vs You)

Two columns side by side. Left column: "What Foundry Ships" (L1-L4, green shading, confident). Right column: "What You Build" (L5-L7, orange/red shading, scaffolding visual). Shared L4 bar spans both columns (partial coverage).

Title: "The 7-Stratum Model"
Left label: "Platform"
Right label: "Your Architecture"

**Pros:** High contrast. Easy to scan at mobile size. Strong "sold vs shipped" energy from AFS01.
**Cons:** Loses the gradient nuance (L2 is also partial). Binary framing oversimplifies.

### Plot C — OSI Model Parallel

Side-by-side comparison: OSI 7-layer model on the left (familiar), {a}OS 7-stratum model on the right (new). Color-coding shows which OSI layers have networking coverage vs which {a}OS strata have platform coverage. Visual parallel makes the unfamiliar model instantly legible.

Title: "OSI for Networking. {a}OS for Agentic AI."

**Pros:** Leverages existing mental model. Architects immediately understand the framing. Strong authority signal.
**Cons:** Requires networking knowledge. May alienate non-infrastructure audience. Two models in one image is visually crowded.

## Recommended

**Plot A** — The 7-stratum heatmap with Foundry overlay. This is the definitive visual for the series. It communicates the coverage gradient, the architectural boundary, and the framework in a single image. Every subsequent post can reference "the heatmap from Post 3."

Plot C (OSI parallel) is a strong secondary option for a follow-up image or blog version.

## Art Direction Notes

- Dark background (matches AFS01 visual language)
- Sans-serif typography, clean and professional
- {a}OS branding: orange accent color for the framework name
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- The L4/L5 dividing line must be visually prominent — it is the thesis
- No vendor logos in the image
- Consider animated version for LinkedIn carousel (static heatmap → coverage overlay fades in)
- This image should be reusable as a reference thumbnail in Posts 4-12

## Typography Hierarchy

1. Title: "{a}OS 7-Stratum Model" (largest)
2. Stratum labels: "L7 Experience & Intent" etc. (medium, left-aligned)
3. Coverage annotations: "Strong / Partial / Weak" (small, right-aligned)
4. Dividing line label: "Above this line — yours to build" (medium, centered, high contrast)

## Color Palette

- L1: #2D8A4E (deep green — strong)
- L2: #7BB35A (yellow-green — partial)
- L3: #3DAA5F (green — good)
- L4: #D4A843 (yellow — partial/preview)
- L5: #D47B43 (orange — weak)
- L6: #D45343 (orange-red — weak)
- L7: #C44337 (red-orange — partial)
- Background: #1A1A2E or similar dark
- Text: #F0F0F0 (light on dark)
- {a}OS accent: #FF6B35 (orange)
