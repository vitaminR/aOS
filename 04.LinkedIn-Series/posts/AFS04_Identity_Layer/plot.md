---
post_id: AFS04
character: Regulator
status: PLOT_PROPOSED
recommended: B
---

## Visual Options

### Option A — Role Hierarchy Diagram

Vertical stack showing the four Foundry roles from least to most privilege, with color-coded risk bands (green/yellow/orange/red). Arrows show what each role can and cannot touch.

**Pros:**

- Immediately communicates privilege escalation
- Familiar mental model (pyramid of access)

**Cons:**

- Hierarchy diagrams are overused on LinkedIn
- Doesn't show the API key bypass problem
- May read as generic RBAC content

---

### Option B — RBAC Comparison Table (Recommended)

Four-row table with columns: Role | What It Grants | Risk Level | Default For. Clean dark theme, {a}OS orange accent on the "Azure AI Owner" row flagged as HIGH risk. A callout box below: "API Keys bypass all of the above."

**Pros:**

- Instantly scannable — people screenshot tables
- Shows the API key danger as a separate callout
- Matches "security review" energy of the post
- High save/share potential

**Cons:**

- Tables can feel dry without strong design
- Needs careful typography to stay readable at mobile scale

---

### Option C — Before/After Split

Left side: "What most teams do" (API key in .env, everyone is Owner). Right side: "What ships safely" (managed identity, least-privilege roles). Red/green contrast.

**Pros:**

- Strong contrast drives the point home
- Before/after is a proven LinkedIn format

**Cons:**

- Oversimplifies the four-role nuance
- Loses the table reference value
- Feels more like a meme than a security doc

---

## Recommended Pick: Option B

The table is the artifact people will screenshot and forward. It matches the Regulator character — structured, auditable, no flair. The API key callout box adds the "oh no" moment without cluttering the table itself.

## Art Direction Notes

- Dark background (#1E1E2E or similar)
- {a}OS orange (#F97316) for high-risk highlights and the API key warning box
- Monospace font for role names
- Subtle grid lines, not heavy borders
- Bottom-right: small {a}OS wordmark
- No gradients, no illustrations — pure information design
- Aspect ratio: 1200x675 (LinkedIn recommended)
