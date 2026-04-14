---
post_id: AFS11
character: Mentor Architect
status: PLOT_PROPOSED
recommended: B
---

## Visual Options

### Option A — Resource Group Tree Diagram

Vertical tree showing Azure Subscription at the top, branching into six resource groups (ai-networking, ai-prod, ai-staging, ai-dev, ai-governance, ai-shared) with key resources listed under each. Color-coded by function: blue for networking, green for workloads, orange for governance, grey for shared.

**Pros:**

- Maps directly to the post's architecture prescription
- Shows the full scope of Phase 1 at a glance
- Engineers can screenshot and use as a starting checklist

**Cons:**

- Tree diagrams are common on LinkedIn
- May feel overwhelming — six groups with multiple resources each
- Loses the "sequence" aspect (what to build first vs. last)

---

### Option B — Phase 1 Architecture Diagram with Bicep Callout (Recommended)

Minimal viable platform layout showing the six resource groups as labeled boxes with key resources inside, connected by network lines (hub-spoke). A callout strip at the bottom reads: "Deploy via Bicep/CLI — fork azure-ai-foundry/foundry-samples." Right side has a small "NOT in Phase 1" crossed-out list: multi-agent, RAG pipelines, model catalog, portal deployments.

**Pros:**

- Shows both what to build AND what to exclude — high signal
- The "NOT in Phase 1" list is the contrarian hook that drives saves
- Bicep callout gives actionable next step
- Matches Mentor Architect energy — practical, scoped, opinionated
- High screenshot and forward potential

**Cons:**

- More complex to design — needs careful layout to avoid clutter
- The "NOT" list could feel preachy if not balanced

---

### Option C — 90-Day Timeline

Horizontal timeline divided into three 30-day blocks. Month 1: identity + networking + IaC scaffolding. Month 2: one model + one agent + APIM gateway. Month 3: cost metering + observability + staging/prod parity. Key milestones marked.

**Pros:**

- Shows the sequence explicitly — what comes before what
- Timeline format is intuitive and actionable
- Easy to adapt to different team sizes

**Cons:**

- Timelines are generic LinkedIn content — may not stand out
- Loses the architecture detail (what resources, what groups)
- Harder to convey the "scope is the strategy" message

---

## Recommended Pick: Option B

The architecture diagram with the "NOT in Phase 1" callout is the most differentiated visual. It does double duty: shows the build list and the scope boundary. The Bicep reference gives engineers a concrete next action. The crossed-out items are the contrarian element that earns saves — people will forward this to team leads who are trying to boil the ocean.

## Art Direction Notes

- Dark background (#1E1E2E or similar)
- {a}OS orange (#F97316) for resource group borders and the "NOT in Phase 1" strike-through
- Light grey (#94A3B8) for resource names within groups
- Monospace font for resource group names and Bicep reference
- Hub-spoke network lines in muted blue (#3B82F6)
- Bottom strip: "Deploy: Bicep/CLI | Fork: azure-ai-foundry/foundry-samples" in orange
- "NOT Phase 1" section in red strike-through (#EF4444)
- Bottom-right: small {a}OS wordmark
- No gradients, no illustrations — infrastructure documentation aesthetic
- Aspect ratio: 1200x675 (LinkedIn recommended)
