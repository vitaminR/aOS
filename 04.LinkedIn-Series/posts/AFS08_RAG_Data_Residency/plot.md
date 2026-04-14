---
post_id: AFS08
character: Architect
status: PLOT_PROPOSED
recommended: A
---

# AFS08 — Visual Direction: "RAG and the Data Residency Question Nobody Asked"

## Plot Options

### Plot A — Storage Model Comparison (Recommended)

Two-column comparison. Left: "Basic" (default). Right: "Standard" (BYO).

Left column (Basic):

- Storage: Microsoft-managed (multitenant)
- Encryption keys: Microsoft-managed
- Private endpoints: Not available
- Visibility: Opaque
- Audit trail: Limited
- Label: "Default"

Right column (Standard):

- Storage: Customer-managed (BYO account)
- Encryption keys: Customer-managed (CMK)
- Private endpoints: Supported
- Visibility: Full (in your subscription)
- Audit trail: Customer-controlled
- Label: "Required for regulated workloads"

Bottom strip: "The choice is made at provisioning time. Not after."

**Pros:** Directly answers the post's question. Scannable. Works at mobile size. The asymmetry between the columns is the argument.
**Cons:** Table-style comparisons are common on LinkedIn — needs strong visual design to stand out.

### Plot B — Environment Boundary Diagram

Shows two Foundry resources side by side. First resource labeled "What teams do" — contains both "Dev Project" and "Prod Project" inside a single shared network boundary (red warning). Second resource pair labeled "What teams should do" — separate "Dev Foundry" and "Prod Foundry" resources, each with their own network boundary (green).

**Pros:** Communicates the environment separation point visually. Novel diagram for LinkedIn.
**Cons:** Doesn't cover the Basic/Standard storage story — only the env boundary part.

### Plot C — Data Residency Decision Tree

Simple flowchart: "Does your agent handle sensitive data?" -> Yes -> "Standard with BYO storage" / No -> "Basic is fine". Second branch: "Do you need environment isolation?" -> Yes -> "Separate Foundry resources" / No -> "Projects within one resource".

**Pros:** Actionable. Readers can use it immediately.
**Cons:** Decision trees look like blog content, not LinkedIn thought leadership. May feel too prescriptive.

## Recommended

**Plot A** — The side-by-side storage model comparison. It's the visual that makes someone stop scrolling and check their own configuration. The asymmetry between the columns IS the argument — Basic looks sparse, Standard looks complete, and the bottom strip ("The choice is made at provisioning time") delivers the urgency.

Consider adding a small environment separation callout below the main comparison as a secondary visual element.

## Art Direction Notes

- Dark or neutral background (consistent with series aesthetic)
- Sans-serif typography
- Azure-branded (this post is Azure-specific, unlike AFS01 which was vendor-neutral)
- Left column (Basic) should feel incomplete — muted colors, gaps
- Right column (Standard) should feel solid — full colors, complete
- Bottom strip text should feel like a warning, not a feature callout
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- No stock imagery — clean data visualization style
