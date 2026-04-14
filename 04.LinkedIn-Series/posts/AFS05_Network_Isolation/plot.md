# AFS05 — Visual Plot

## Option A: The Exceptions Table (Recommended)

A clean, dark-background truth table styled like a terminal or compliance document.

**Layout:**

- Title bar: "Azure AI Foundry — Network Isolation Exceptions" with a "Last Verified: 2026-04" tag
- Three status columns: WORKS (green), BROKEN (red), PUBLIC INTERNET (orange/amber)
- Rows grouped into sections:
  - **Infrastructure** — Private Endpoints, VNet Injection, AI Search
  - **Agent Tools** — Code Interpreter, Function Calling, File Search, OpenAPI, Azure Functions, Browser Automation, Computer Use, A2A, Image Gen, Logic Apps
  - **Agent Types** — Hosted Agents, Workflow Agents
  - **Grounding** — Bing Grounding, Web Search, SharePoint Grounding
  - **Operations** — Tracing (App Insights), Foundry Portal (new)
- Each cell: checkmark, X, or warning triangle
- Footer: "Block public-internet tools via Azure Policy on day one."

**Pros:** Immediately useful. Saves teams hours of testing. Highly shareable — people screenshot tables. Matches the "Regulator" character perfectly.

**Cons:** Dense. Needs to be legible at LinkedIn image size. May need to simplify groupings.

**Art direction:** Monospace font. Dark charcoal background (#1E1E1E). Green (#4EC9B0), Red (#F44747), Amber (#FFCC02). Thin grid lines. {a}OS logo bottom-right. No gradients, no shadows. Looks like it came out of a security audit tool.

---

## Option B: Network Diagram with Annotations

A simplified architecture diagram showing a VNet boundary with tools plotted inside/outside/straddling the boundary.

**Layout:**

- VNet boundary drawn as a dashed rectangle
- Tools that work: inside the boundary with green indicators
- Tools that break: inside but with red strike-through
- Tools that go public: arrows punching through the boundary to a "Public Internet" cloud
- Bing/WebSearch/SharePoint highlighted with amber arrows leaving the VNet

**Pros:** Visually intuitive for network engineers. Tells the story spatially.

**Cons:** Harder to be precise. Loses the "receipt" feel. More complex to produce. May look like a generic cloud architecture diagram.

**Art direction:** Same dark palette. Dotted VNet boundary in white. Color-coded arrows.

---

## Option C: Before/After Split

Left side: the vendor slide ("End-to-end VNet isolation"). Right side: the actual state with red annotations.

**Layout:**

- Left panel: Clean, marketing-style checkmark list. "Private Endpoints. VNet Injection. Isolated Compute." All green.
- Right panel: Same list but annotated. Red X marks on broken items. Amber warnings on public-internet items. Handwritten-style annotations like "nope" and "goes to Bing over public."

**Pros:** Strong narrative tension. The "expectation vs. reality" format performs well on LinkedIn.

**Cons:** Potentially reads as adversarial toward Microsoft. Less useful as a reference artifact. The humor might undercut the Regulator character's credibility.

**Art direction:** Left side clean and polished. Right side rougher, with monospace annotations overlaid.

---

## Recommended Pick: Option A

The exceptions table is the post. It is the artifact people will screenshot, send to their security team, and pin in Slack. It matches the Regulator character — methodical, precise, no drama. It is the "receipt" the post promises.

The table must be legible at 1200x627 (LinkedIn recommended). Group rows tightly. Use abbreviations where needed. Include a "Last Verified" date to address the perishability concern.

**Production notes:**

- Create in Figma or as a styled HTML screenshot
- Test legibility at 50% zoom (simulates mobile LinkedIn feed)
- Include {a}OS branding but keep it subtle — this is a utility graphic, not a brand piece
- Consider a second version at higher resolution for the blog/docs site
