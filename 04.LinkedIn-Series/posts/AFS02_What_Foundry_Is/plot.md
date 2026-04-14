---
post_id: AFS02
character: Architect
status: PLOT_PROPOSED
recommended: A
---

# AFS02 — Visual Direction: "What Azure AI Foundry Actually Is (and Isn't)"

## Plot Options

### Plot A — Resource Model Comparison Table (Recommended)

Two-column comparison table with a clean dividing line:

| Dimension | Classic (Maintenance Mode) | New (Active Investment) |
|---|---|---|
| Resource provider | `Microsoft.MachineLearningServices` | `Microsoft.CognitiveServices` |
| Topology | Hub → Projects | Foundry Resource → Projects |
| Management | Azure ML workspace patterns | Cognitive Services account patterns |
| Portal | Foundry (classic) at ai.azure.com | Foundry (new) — toggle in portal |
| Network isolation | More mature | Still maturing |
| Investment | Maintenance | Active |

Header: "Two Resource Models. One Decision on Day One."
Footer: "Verify yours: `az provider show -n Microsoft.CognitiveServices`"

**Pros:** Directly supports the post's thesis. Scannable at mobile size. The comparison is the teaching.
**Cons:** Tables are not the most engaging LinkedIn format. Needs strong typography to avoid looking like a spreadsheet.

### Plot B — Architecture Topology Diagram

Two small architecture diagrams side by side:

Left: Classic model

```
Hub
├── Project A
├── Project B
└── Project C
```

Right: New model

```
Foundry Resource
├── Project A
├── Project B
└── Project C
```

With callouts showing the different resource providers underneath each.

**Pros:** Visual difference is immediately clear. Architecture audience loves topology diagrams.
**Cons:** The topologies look similar (both are parent→child). The difference is in the resource provider and management patterns, not the topology shape.

### Plot C — What Foundry Bundles (Feature Map)

Radial or stacked diagram showing Foundry's six bundles:

- Models (11K+ catalog)
- Agent Service (prompt GA, workflow/hosted preview)
- Foundry IQ (preview)
- Content Safety (GA)
- Tools (Speech/Vision/Language/DocIntel GA)
- Control Plane (RBAC/networking/encryption/monitoring)

Each segment labeled with maturity status (GA/Preview).

**Pros:** Good reference image. Shows scope clearly.
**Cons:** Feature maps are marketing-adjacent. Doesn't serve the "two models" thesis directly.

## Recommended

**Plot A** — The resource model comparison table. The entire post is about the two-model reality. The visual should be the comparison, not a feature map. Typography and layout must be strong to avoid spreadsheet aesthetics.

## Art Direction Notes

- Dark background (series consistency with AFS01)
- Sans-serif typography
- Two-column layout with clear header row
- "Classic" column: muted/gray tone (maintenance mode)
- "New" column: slightly brighter/blue tone (active investment)
- Must work at LinkedIn mobile size (1200x627 or 1080x1080)
- Include the CLI verification command in the image footer — gives readers an immediate action
- No vendor logos beyond Azure AI Foundry name

## Typography Hierarchy

1. Title: "Two Resource Models. One Decision on Day One." (largest)
2. Column headers: "Classic (Maintenance Mode)" / "New (Active Investment)" (medium, bold)
3. Row labels: Dimension names (medium, left-aligned)
4. Cell values: Resource provider names, portal URLs, etc. (regular)
5. Footer: CLI command in monospace (small, high contrast)
