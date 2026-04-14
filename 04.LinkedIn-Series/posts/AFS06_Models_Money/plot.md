---
post_id: AFS06
character: Architect
status: PLOT_PROPOSED
recommended: B
---

# AFS06 — Visual Direction: "Models, Money, and the Reality of Model Access"

## Plot Options

### Plot A — Availability Matrix (Clean Table)

Three-column comparison table with rows for key model capabilities:

| Capability | Commercial | Gov (IL5) | Gov (IL6) |
|---|---|---|---|
| GPT-4.1 | Yes (1M context) | Yes (300K context) | No |
| GPT-5.4 | Yes | No | No |
| Embeddings (full) | Yes | Partial | No |
| Batch deployments | Yes | No | No |
| PTU available | Yes | Limited | No |
| Model Router | Yes | No | No |

Dark background, clean sans-serif, green/yellow/red color coding.

**Pros:** Factual, scannable, immediately communicates the constraint. High save/share potential.
**Cons:** Dates quickly as model availability changes. Needs methodology caveat.

### Plot B — The Shrinking Funnel (Recommended)

Visual funnel or stacked bars showing model availability narrowing:

- Top: "11,000+ models" (marketing number, wide bar, bright)
- Middle: "~50-100 Azure-hosted" (production-relevant, medium bar)
- Next: "Available in your region" (narrower)
- Next: "Available in Gov cloud" (much narrower)
- Bottom: "Available at IL6" (nearly empty or zero for AOAI)

Label: "What '11,000+ Models' Actually Means for Your Deployment"

**Pros:** Tells the story visually. High engagement — the shrinking funnel is visceral. Does not date as quickly because it teaches a pattern, not specific numbers. Works at mobile size.
**Cons:** Specific numbers in funnel could date. Use approximate ranges.

### Plot C — The Two Price Tags

Split visual showing two deployment models side by side:

Left: "Pay-as-you-go" — meter/consumption icon, label: "No commitment, no guarantee"
Right: "PTU" — locked/reserved icon, label: "$X,XXX/month committed, capacity reserved"

Below both: "The decision your CFO is about to make without asking your architect"

**Pros:** Highlights the cost governance angle. Provocative tagline.
**Cons:** Narrower than the full availability story. Better as a supporting visual than the primary.

## Recommended

**Plot B** — The shrinking funnel communicates the central thesis in one image: the number of models available to you shrinks dramatically based on deployment context. It teaches a pattern rather than listing facts that will date, and the visual progression from "11,000+" to "nearly zero at IL6" is immediately compelling.

## Art Direction Notes

- No vendor logos or classified markings
- Dark or neutral background, professional tone
- Sans-serif typography
- The funnel should feel factual, not alarmist — this is an architecture observation
- Include small text: "Approximate ranges. Verify current availability at learn.microsoft.com"
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- Use approximate ranges ("~50-100") not exact counts
