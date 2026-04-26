# {a}OS Web App — PRD + SPEC

## 1.0 Product Summary

### 1.1 Working Title

**{a}OS Explorer**

### 1.2 Product Thesis

{a}OS Explorer is a modular web application for classifying, comparing, and exploring AI products, agents, frameworks, workflows, skills, and tools against the canonical {a}OS reference model.

It is not a static directory.
It is an **interactive taxonomy and comparison engine**.

Its purpose is to let users answer questions like:

* What strata does this product actually touch?
* Which axes does it govern or influence?
* Which constructs and primitives does it produce or control?
* How does Azure AI Foundry compare to Paperclip + Kotana + other aftermarket stacks?
* What gaps, overlaps, and hidden dependencies exist between these systems?

### 1.3 Product Goal

Provide a flexible, evidence-backed system for:

* browsing the {a}OS model
* drilling from **Stratum → Substrate → Construct → Primitive**
* comparing products and frameworks across the same ontology
* filtering by category, capability, axis, maturity, deployment model, and more
* making the framework usable for both learning and architecture decision support

### 1.4 Product Type

Hybrid of:

* interactive knowledge model
* product intelligence browser
* architecture comparison tool
* taxonomy explorer

---

## 2.0 Product Vision

### 2.1 Vision Statement

Create the OSI-like reference interface for the agentic era: a web app where people can visually understand where AI systems live, where they overlap, and where they fail.

### 2.2 Core Value Proposition

Most AI tooling sites tell users **what a product claims to do**.
This product tells users:

* **where it belongs**
* **how it overlaps with other products**
* **what part of the stack it governs**
* **what primitives and constructs it touches**
* **what risks and gaps appear when composing systems together**

### 2.3 Product Principles

* **Ontology-first**: the model drives the UI, not the other way around
* **Flexible views**: same data, multiple browsing modes
* **Progressive drilldown**: broad first, deep on demand
* **Evidence-backed classification**: every placement can be justified
* **Multi-residency classification**: products can span multiple strata
* **Framework-agnostic**: compare {a}OS against alternative models later
* **Composable UI**: modules can be reused for product, framework, workflow, or agent exploration

---

## 3.0 Users and Use Cases

### 3.1 Primary Users

1. **Architects**
   Need to compare stacks and identify overlap, gaps, and governance implications.

2. **Engineers**
   Need to understand where tools sit and which layer is failing.

3. **Technical leaders / innovation leads**
   Need to explain architecture and defend adoption decisions.

4. **Researchers / buyers**
   Need to compare Azure-native vs aftermarket solutions.

5. **Content audience**
   Need a visual, engaging, memorable way to learn the model.

### 3.2 Core Use Cases

* Compare Azure AI Foundry against Paperclip + Kotana + other additions
* Explore how a product spans multiple strata
* Filter all products that touch L4 and Governance Axis
* Drill into a stratum and expand down to primitives
* Swap category from frameworks to agents, workflows, or skills
* Compare alternative reference frameworks side by side
* Identify whether a product is acting as substrate, construct producer, or axis-enforcer

---

## 4.0 Product Scope

### 4.1 In Scope for MVP

* Canonical {a}OS stack visualization
* Multi-entity browser: products, frameworks, agents, workflows, skills
* Drilldown explorer from Stratum to Primitive
* Compare mode for 2–4 items
* Filtering system
* Classification model with primary / secondary strata and axis roles
* Product detail pages
* Framework detail pages
* Evidence / rationale panels
* Relationship visualization between selected objects

### 4.2 Out of Scope for MVP

* User accounts / social features
* Crowd-sourced public editing
* Fully automated classification from scraped web data
* Billing / subscriptions
* Real-time usage telemetry from third-party tools
* AI-generated architecture recommendations without human review

### 4.3 Phase 2 Candidates

* Saved comparison sets
* Team workspaces
* Framework scoring and weighting system
* Scenario-based evaluation mode
* AI-assisted classification suggestions
* Public submission pipeline with moderation

---

## 5.0 Core Concept Model

### 5.1 Canonical Terms

* **Stratum** = top-level layer in the stack
* **Axis** = cross-cutting concern intersecting multiple strata
* **Substrate** = tools/frameworks/systems operating in a stratum
* **Construct** = meaningful artifact/state produced by a substrate
* **Primitive** = smallest atomic unit inside a construct

### 5.2 Entity Types

The app must support multiple top-level entity types using the same underlying model:

* Products
* Frameworks
* Agents
* Workflows
* Skills
* Axes
* Strata
* Substrates
* Constructs
* Primitives

### 5.3 Classification Rules

Each product or entity may have:

* one **primary stratum**
* zero or more **secondary strata**
* zero or more **axis roles**
* one or more **capabilities**
* one or more **constructs produced / governed**
* one or more **primitives touched / governed**
* confidence score
* rationale
* evidence links / notes

---

## 6.0 UX Model

### 6.1 Primary Interaction Concept

The app should feel like a **progressive morphing explorer**.

Users can start from a high-level stack, then click deeper and transform the interface into more detailed views without switching mental context.

### 6.2 Key UX Pattern

**Progressive Drilldown Explorer**

*Cognitive rationale:* The 4-level hierarchy (Stratum → Substrate → Construct → Primitive) maps to Cowan's 4±1 working memory limit. Each level is a meaningful chunk — users never see more than one hierarchy level at once unless they explicitly expand. See 6.5.4 (Chunking) and 6.5.6 (Progressive Disclosure) for enforcement rules.

User flow:

1. Start at stack or category view
2. Click a Stratum
3. Expand into Substrates
4. Expand a Substrate into Constructs
5. Expand a Construct into Primitives
6. Layer on filters, comparisons, and alternate framework views

This should not feel like navigating to a different page every time.
It should feel like the UI **unfolds deeper**.

### 6.3 Desired Interaction Modes

**MVP (ship these three):**

1. **Stack Mode**
   Classic 7-stratum vertical model

2. **Accordion Mode**
   Expand strata into substrate/construct/primitive rows

3. **Compare Mode**
   Side-by-side comparison of selected products/frameworks/entities

**Phase 2 (add these after MVP proves the core):**

1. **Map Mode**
   Multi-layer, multi-product span view showing overlaps and coverage

2. **Category Mode**
   Top-level toggle between Products, Frameworks, Agents, Workflows, Skills

3. **Axis Mode**
   Show how Governance & Trust and Observability & Evaluation cut across selected items

### 6.4 Top Navigation / Mode Buttons

At the top of the app, include color-coded pill buttons or segmented tabs for:

* Products
* Frameworks
* Workflows
* Compare
* Axes
* Strata

**MVP constraint:** Only show entity types with populated content. Agents and Skills buttons appear greyed out or hidden until Phase 2 content is seeded. Never show 8 buttons with 3 populated — it signals an empty product.

These must be globally accessible and instantly switch the object lens while preserving filters where appropriate.

### 6.5 UX Patterns *(informed by ui-patterns.com)*

The following patterns are required or strongly recommended. Each maps to a known UX pattern with documented cognitive rationale.

#### 6.5.1 Breadcrumbs *(Navigation)*

Every drilldown state must show a clickable breadcrumb trail:

```
{a}OS Stack → L4 Orchestration & Decisioning → Workflow Engine → Execution Graph → node_id
```

**Rules:**

* Always visible in main canvas header during drilldown
* Each segment is clickable — user can jump back to any level
* Breadcrumb updates in-place during morphing transitions (no page reload)
* Compare mode shows one breadcrumb per compared item

#### 6.5.2 Blank Slate *(Onboarding)*

Every container that can be empty must have a purposeful empty state:

| Container | Blank Slate Content |
|-----------|-------------------|
| Compare basket (0 items) | "Add products to compare — click the + on any product card" + illustration |
| Search (no results) | "No matches for '{query}' — try browsing by stratum or filtering by category" |
| Filter results (0 matches) | "No products match these filters — [clear filters] or [broaden search]" |
| Stratum with no products seeded | "This stratum has no classified products yet — [contribute a mapping]" (Phase 2) |

**Rule:** Never show an empty white/black box. Every empty state must explain what belongs there and how to fill it.

#### 6.5.3 Guided Tour / Coachmarks *(Onboarding)*

**MVP:** First-visit coachmark sequence (dismissable, max 4 steps):

1. "This is the {a}OS reference stack — 7 strata from Experience to Infrastructure"
2. "Click any stratum to drill into substrates, constructs, and primitives"
3. "Add products to your compare basket to see them side by side"
4. "Use filters to narrow by vendor, deployment model, or axis"

**Rules:**

* Shown once per browser (localStorage flag)
* Skippable with "Skip tour" link on first step
* Each coachmark highlights the relevant UI region with a spotlight mask
* Never blocks interaction — user can click through at any time

**Phase 2:** Context-sensitive coachmarks that trigger on first use of new features (compare mode, axis overlay, framework switch).

#### 6.5.4 Chunking *(Cognition / Perception)*

The Stratum → Substrate → Construct → Primitive hierarchy is itself a chunking pattern — it breaks a complex system into 4 nested levels that match human working memory limits (Miller's 7±2 / Cowan's 4±1).

**UI enforcement:**

* Never show more than one hierarchy level expanded at a time by default (user can manually expand multiple, but auto-expand collapses siblings)
* Each level visually nests with indentation + progressive size reduction
* Substrate count per stratum should target 3-7 visible items before "show more" truncation
* Count badges on collapsed items ("12 substrates", "4 constructs") give scale without overwhelming

#### 6.5.5 Recognition over Recall *(Cognition)*

Users should never need to memorize ontology vocabulary to use the app.

**Rules:**

* Stratum names always appear with their boundary question as a subtitle (e.g., "L4 — Orchestration & Decisioning" / *What happens next, in what order, with which agent?*)
* Vocabulary terms (Stratum, Axis, Substrate, Construct, Primitive) show tooltip definitions on first hover
* Entity type icons are consistent and always paired with text labels — no icon-only navigation
* Filter labels use plain language with ontology term in parentheses where needed

#### 6.5.6 Progressive Disclosure *(Cognition)*

**Rules (formalized):**

* Default view: 7 strata as collapsed cards — no substrates visible
* First click: expand one stratum → show substrates
* Second click: expand one substrate → show constructs
* Third click: expand one construct → show primitives
* Detail panels (rationale, evidence, confidence) are always behind a "Show details" affordance, never shown on first render
* Filters start with 4 visible filter groups; "More filters" reveals the full set
* Compare mode starts with coverage heatmap; "Detailed comparison" reveals construct/primitive-level diff

#### 6.5.7 Morphing Controls *(Interaction)*

Formalizes Rule 11.4 with specific pattern guidance:

* When a user clicks a stratum, the stratum card morphs into an expanded container (same DOM element, animated) — no route change
* When compare mode is activated, selected cards slide and resize into comparison columns
* Mode switches (Stack → Accordion → Compare) should cross-fade content while maintaining the header and breadcrumb — never a full page flash
* Entity-type switches (Products → Frameworks) preserve scroll position and filter state

#### 6.5.8 Favorites *(Personalization — Phase 2)*

* Users can star/bookmark products and strata
* Favorited items appear in a "Favorites" quick-access section in the left rail
* Favorites persist in localStorage (MVP) or user profile (Phase 2 with accounts)

#### 6.5.9 Keyboard Shortcuts *(Interaction)*

| Shortcut | Action |
|----------|--------|
| `/` | Focus global search |
| `Esc` | Close detail panel / exit compare / collapse current drilldown |
| `↑` `↓` | Navigate between strata or list items |
| `→` | Expand / drill deeper |
| `←` | Collapse / drill up |
| `c` | Toggle compare mode |
| `1`–`7` | Jump to stratum L1–L7 |
| `?` | Show keyboard shortcut overlay |

**Rules:**

* Shortcuts only active when no text input is focused
* Shortcut overlay (triggered by `?`) uses a modal cheat-sheet — same pattern as GitHub, Linear, Notion

#### 6.5.10 Curiosity / Information Gaps *(Engagement)*

Use strategic information gaps to pull users deeper:

* Product cards show primary stratum + "spans N strata" — user must click to see which ones
* Compare heatmap shows overlap count — user must expand to see specific construct-level overlap
* Stratum cards show substrate count badge — user must expand to see the list
* "3 disputed classifications" tag on a product → user clicks to see the debates

**Rule:** Tease the count or one interesting fact; never hide critical navigation or classification data behind curiosity traps.

#### 6.5.11 Feedback Loops *(Trust)*

Classification confidence is a feedback loop between the system and the user's trust:

* High confidence (≥0.8): solid badge, no qualifier
* Medium confidence (0.5–0.79): badge with "~" prefix, tooltip shows rationale
* Low confidence (<0.5): dashed badge with "?" icon, rationale panel auto-visible
* Disputed: amber border, "alternate interpretation" link visible without click

### 6.6 Primary Layout Structure

**Header**

* product name / logo
* search bar
* entity-type mode buttons
* framework selector
* compare basket
* breadcrumb trail (visible during drilldown — see 6.5.1)

**Left Rail**

* strata list
* axes list
* saved filters
* quick toggles

**Main Canvas**

* dynamic interactive explorer
* stack / accordion / compare / map rendering area

**Right Rail**

* details panel
* rationale / evidence
* selected item metadata
* overlap notes

---

## 7.0 Core Screens

### 7.1 Home / Explorer Screen

Purpose:
Introduce the stack and let users start from any stratum or entity type.

Must include:

* canonical 7-stratum stack
* axis overlay toggle
* entity-type switcher
* featured products / frameworks
* compare basket entry point
* **first-visit guided tour** (coachmark sequence — see 6.5.3)
* **blank slate for empty compare basket** (see 6.5.2)

### 7.2 Stratum Detail Screen

Purpose:
Deep dive into one stratum.

Must include:

* definition
* boundary question
* substrates
* constructs
* primitives
* related products
* axis interactions
* common failures

### 7.3 Product Detail Screen

Purpose:
Classify one product against the full ontology.

Must include:

* summary
* primary / secondary strata
* axis roles
* capabilities
* constructs produced / governed
* primitives touched / governed
* overlap notes
* confidence / rationale
* related products

### 7.4 Compare Screen

Purpose:
Compare 2–4 products or frameworks on equal footing.

Must include:

* layer coverage heatmap
* axis role comparison
* constructs/primitives overlap table
* maturity / deployment / ownership tags
* gap and overlap summary
* **blank slate when basket has <2 items** ("Add at least 2 products to compare" — see 6.5.2)

### 7.5 Framework Comparison Screen — PHASE 2

Purpose:
Compare {a}OS to other reference frameworks.

**Phase gate:** This screen requires at least two fully defined frameworks. MVP ships with {a}OS only. Build this when the second framework mapping is complete.

Must include:

* framework definitions
* layer count / ontology terms
* coverage mapping
* where concepts collapse or differ
* normalized translation matrix

---

## 8.0 Functional Requirements

### 8.1 Explorer Requirements

* User can click a stratum to expand it
* User can click into substrate, construct, and primitive levels
* User can collapse back upward without losing context
* Breadcrumb trail must update in real time during drilldown (see 6.5.1)
* Explorer state must support multiple expanded branches
* Explorer must visually distinguish primary vs secondary relationships

### 8.2 Filtering Requirements

User can filter by:

* entity type
* stratum
* axis
* substrate type
* deployment model
* vendor
* open source vs proprietary
* local vs cloud vs hybrid
* maturity
* confidence score
* category tags

### 8.3 Comparison Requirements

* User can add items to a compare basket
* User can compare 2–4 items at once
* System must normalize comparisons using shared ontology fields
* Comparison must highlight overlap, unique coverage, and gaps
* Comparison must work across entity types when valid

### 8.4 Framework Mapping Requirements

* System must support multiple frameworks, not just {a}OS
* Every non-{a}OS framework must be mappable to canonical ontology fields
* System must support translation tables between frameworks
* User must be able to overlay alternative frameworks on top of the explorer

### 8.5 Evidence Requirements

* Each classification placement must support rationale text
* Each placement may optionally support evidence links, notes, or quotes
* UI must expose confidence and disputed classifications

### 8.6 Search Requirements

* Global search across products, frameworks, agents, workflows, skills, and terms
* Search must support partial matches, tags, and ontology terms

---

## 9.0 Information Architecture

### 9.1 Core Data Objects

1. **Entity**
   Base object for product/framework/agent/workflow/skill

2. **Placement**
   Relationship between entity and stratum/axis

3. **Capability**
   Named function or feature

4. **Construct Mapping**
   Link between entity or substrate and constructs

5. **Primitive Mapping**
   Link between construct and primitives

6. **Framework**
   Alternate layer model or comparison taxonomy

7. **Evidence**
   Rationale, notes, links, confidence data

### 9.2 Suggested Schema Shape

**Entity**

* id
* type
* name
* slug
* summary
* vendor
* tags[]
* deployment_modes[]
* maturity
* open_source
* last_verified_at

**Placement**

* id
* entity_id
* target_type: stratum | axis | substrate | construct | primitive
* target_id
* role_type: primary | secondary | cross_cutting | compared_to
* confidence
* rationale

**Capability**

* id
* entity_id
* name
* description
* mapped_strata[]
* mapped_axes[]

**Evidence**

* id
* placement_id
* source_type
* source_label
* source_url
* excerpt
* note

---

## 10.0 Visual System

### 10.1 UI Character

Target feel:

* architectural
* elegant
* modern
* cinematic — think Linear's dot-grid animations, Raycast's glass effects, Artificial Analysis's floating card depth. Not "flashy SaaS marketing." Cinematic means physical simulation, staggered reveals, atmosphere through negative space.
* not toy-like
* not dashboard sludge

**Color mode:** Dark-first. Near-black foundation (`rgb(7-10, 9-12, 10-14)`), indigo-to-blue accent gradient, 4-level text opacity hierarchy (primary white → quaternary gray). Light mode supported but dark is the default — this audience lives in dark terminals and IDEs.

### 10.2 Visual Principles

* Stable vertical hierarchy for the stack
* Motion used for orientation, not decoration
* Multiple selection states must remain readable
* Filters must feel powerful, not overwhelming
* Color should communicate type and role, not just aesthetics

### 10.3 Color System

Use distinct but controlled colors for the main entity types:

* Products
* Frameworks
* Agents
* Workflows
* Skills
* Axes
* Strata

Each stratum should have its own stable color identity.
Each axis should have a distinct overlay style.

### 10.4 Motion Patterns

* Expand / collapse morph (Framer Motion `layoutId` + `AnimatePresence`)
* Layer highlight on hover (Aceternity spotlight card effect)
* Span lines for multi-stratum products (Aceternity tracing beams)
* Compare transitions (Framer shared-layout transitions)
* Filter fade / isolate interactions (Framer spring physics + opacity)
* Scroll-triggered layer reveals (GSAP ScrollTrigger, staggered 200ms)
* Aurora/gradient shift on stratum focus (Magic UI aurora component)
* Floating dock for compare basket (Aceternity dock component)
* Moving-border buttons for primary CTAs (Aceternity moving-border)

### 10.5 Core Visual Components

* Stratum Bar (Aceternity spotlight card + unique aurora color per layer)
* Axis Overlay (Magic UI shimmer border + Framer Motion fade)
* Capability Chip (shadcn badge + Aceternity moving-border on hover)
* Placement Badge (primary = solid glow, secondary = ring outline)
* Expandable Knowledge Row (Framer layout animation + Aceternity expandable card)
* Compare Card (triple-shadow floating card with brand-color ambient glow)
* Confidence Meter (Magic UI animated progress + score label)
* Rationale Panel (shadcn sheet/drawer with slide-in transition)
* Relationship Line / Span Indicator (Aceternity tracing beam between strata)

---

## 11.0 Product Behavior Rules

### 11.1 Multi-Placement Rule

A product may span multiple strata.
The UI must never force false exclusivity.

### 11.2 Primary vs Secondary Rule

Primary placement must be visually stronger than secondary placement.

### 11.3 Dispute Rule

If a classification is debatable, the UI must show:

* confidence
* rationale
* alternate interpretations

### 11.4 Morph Rule

When expanding from stratum to substrate to construct to primitive, the app should transform the current layout instead of hard switching pages whenever possible.

### 11.5 Compare Integrity Rule

Comparisons must only align fields that are ontologically compatible.
If two objects cannot be meaningfully compared on a field, show "not comparable" rather than inventing symmetry.

---

## 12.0 Technical Architecture

### 12.1 Frontend Stack

```
Next.js 15 + TypeScript + Tailwind CSS v4
  + Aceternity UI        --> 200+ cinematic copy-paste components (aurora, lamp, 3D cards, tracing beams, moving borders, floating dock)
  + Magic UI             --> supplemental particle/shimmer/orbit effects (oklch color space)
  + assistant-ui         --> agentic AI primitives (threads, tool-call UIs, MCP integration, human-in-the-loop)
  + shadcn/ui + Radix    --> accessible base primitives underneath
  + Framer Motion        --> layout morphs, spring physics, shared-layout transitions, accordion expand/collapse
  + GSAP ScrollTrigger   --> scroll-based cinematic choreography, staggered reveal wavefronts, timeline sequences
  + Zustand              --> lightweight state (compare basket, filters, drilldown state)
  + TanStack Query       --> data fetching when moving to API/DB
```

### 12.1.1 Why This Stack

| Layer | Choice | Why |
|-------|--------|-----|
| **Cinematic components** | Aceternity UI | 200+ components with built-in 3D effects, aurora backgrounds, lamp glow, tracing beams, moving borders, parallax scroll. Framer Motion core. shadcn-compatible. Next.js + TS + Tailwind native. |
| **Supplemental effects** | Magic UI | Orbit animations, meteor showers, shimmer borders, ripple effects. oklch color space for perceptually smooth gradients. Copy-paste, non-conflicting with Aceternity. |
| **AI/agentic primitives** | assistant-ui | Thread management, tool-call rendering, generative UI, multi-agent interfaces. MCP + Vercel AI SDK + LangChain integrations. Headless — layers cleanly under cinematic visuals. |
| **Layout animations** | Framer Motion | `layoutId` for morphing panes, `AnimatePresence` for enter/exit, spring physics for buttons, shared-layout transitions for drilldown. Already bundled with Aceternity. |
| **Scroll choreography** | GSAP ScrollTrigger | Timeline-based staggered reveals, scroll-snapped layer transitions, "cinematic entrance" sequences. The industry standard for scroll-driven storytelling. |
| **Base primitives** | shadcn/ui + Radix | Accessible, unstyled primitives (dialogs, popovers, dropdowns, tabs). Aceternity and Magic UI are built on top of these. |
| **State** | Zustand | Lightweight, URL-syncable, handles compare basket + filter state + drilldown tree without Redux boilerplate. |

### 12.1.2 Visual Design System

**Atmosphere:**

* Near-black foundation: `rgb(8, 10, 12)` base
* Indigo-to-blue accent gradient: `indigo-600` → `blue-500`
* 4-level text opacity: primary `white/90`, secondary `white/60`, tertiary `white/40`, quaternary `white/20`
* Triple-shadow card system: inset highlight (white 10% opacity) + heavy drop shadow (30px blur) + colored ambient glow

**Cinematic patterns to use:**

* Staggered animation wavefronts for layer reveals (diagonal timing, 200ms stagger)
* Glassmorphism with physical simulation on hero/overlay panels
* Aurora/gradient backgrounds on stratum headers (each stratum gets a unique color identity)
* Moving-border buttons for primary actions
* Tracing beam connections between related strata in compare mode
* Floating dock for compare basket (Aceternity's Mac-dock component)
* Lamp glow effect on active/expanded stratum

**Design references:**

* Linear (dot-grid animation, opacity-layered depth, hardware-gated effects)
* Raycast (command palette, WebGL glass, near-black foundation)
* Artificial Analysis (floating cards, bar charts with brand colors, scatter plots for comparison)
* Stripe Developer Docs (progressive disclosure, generous negative space)

### 12.1.3 Accessibility + Performance

* Hardware-detect animation gating (check `navigator.hardwareConcurrency` — disable heavy effects on low-end devices)
* `prefers-reduced-motion` respected on all animations
* Keyboard navigation for all drilldown, filter, and compare interactions
* WCAG 2.1 AA contrast ratios on all text (dark mode makes this easier, not harder)
* Code-split animation libraries — GSAP and Three.js only load on pages that use them

### 12.2 Data Layer Recommendation

Start with structured content + schema validation.
Good paths:

* local JSON / YAML / MDX content for fast iteration
* Prisma + Postgres once dynamic editing/querying grows

**Bridging rule:** JSON content files must mirror the relational schema shape (entity files with embedded placements, capabilities, and evidence arrays — not flat markdown). This makes the migration to Postgres mechanical, not a restructure. Use Zod or a JSON Schema validator to enforce shape from day one.

### 12.3 State Management

Needs strong support for:

* multi-select
* deep drilldown state
* compare basket
* shared filters
* mode switching

Recommended:

* URL-synced filter state
* Zustand or equivalent lightweight state layer
* React Query / TanStack Query if moving to DB/API

### 12.4 Search / Indexing

* local fuzzy search for MVP
* evolve to indexed structured search later

### 12.5 Rendering Strategy

* SSR or SSG for content-heavy pages
* client-side interactive explorer for morphing interface

---

## 13.0 Modularity Requirements

### 13.1 Must Be Modular By

* entity type
* explorer mode
* filter group
* framework overlay
* detail panel type

### 13.2 Reusable Modules

* EntityCard
* StratumExplorer
* DrilldownAccordion
* AxisOverlay
* CompareMatrix
* FrameworkTranslator
* FilterPanel
* EvidencePanel
* PlacementLegend

### 13.3 Future-Proofing Requirement

The ontology and UI must allow later addition of:

* new frameworks
* new axes
* new entity types
* alternate scoring systems
* scenario-based evaluation layers
  without requiring major redesign of the explorer core.

---

## 14.0 Analytics and Insight Layer

### 14.1 Clarification

The product does not need business analytics first.
It needs **exploration intelligence**.

### 14.2 What to Support

* filter combinations
* overlap counts
* coverage summaries
* gaps by stratum
* axis intensity by product
* compare summaries

### 14.3 Useful Derived Insights

* which products span the most strata
* which strata have the highest overlap density
* which frameworks collapse distinctions most aggressively
* which combinations leave major governance or observability gaps

---

## 15.0 Scoring and Evaluation Model — PHASE 2

**Phase gate:** MVP shows raw classification data (strata, axes, constructs, confidence) without computed scores. Scoring without explicit methodology undermines the evidence-backed principle. Define the rubric, scale (1-5 or 1-10), and weighting system before implementing any computed scores.

### 15.1 For Products

Potential normalized scoring dimensions:

* stratum coverage breadth
* governance depth
* observability depth
* execution safety
* deployment flexibility
* modularity
* maturity

### 15.2 For Frameworks

Potential normalized scoring dimensions:

* memorability
* diagnostic clarity
* boundary precision
* enterprise governance fit
* vendor neutrality
* extensibility

### 15.3 Rule

Scores must always be tied to explicit definitions and visible methodology.
No black-box scoring.

---

## 16.0 MVP Definition

### 16.1 MVP Must Deliver

* canonical {a}OS explorer
* 7 strata
* 2 core axes
* 3 entity types minimum: products, frameworks, workflows
* drilldown explorer
* compare basket and compare screen
* product detail pages
* filter panel
* evidence panel

### 16.2 MVP Sample Content Set

At minimum include:

* Azure AI Foundry
* Paperclip
* Kotana
* NemoClaw / OpenShell
* LangGraph
* CrewAI
* Mem0
* Azure AI Search
* Open Policy Agent

This is enough to prove the ontology and UI across all 7 strata.

### 16.3 Content Seeding Estimate

Each product classification requires: primary stratum, secondary strata, axis roles, capabilities, constructs produced/governed, primitives touched, rationale, evidence, and confidence scores.

**Estimated effort:** 2-4 hours per product for full classification.
**9 products = 18-36 hours of content work** before the tool is demo-ready.

**Recommendation:** Seed Azure AI Foundry first (already mapped in `02.Vendor-Mappings/`). Use it as the template for all subsequent product classifications. Parallelize content seeding with UI development — they are independent workstreams.

---

## 17.0 Success Criteria

### 17.1 Product Success

* Users can explain what a product does in stack terms faster than before
* Users can compare Azure-native and aftermarket stacks with less ambiguity
* Users can identify overlap and missing coverage without external diagrams
* The model remains stable while adding new products/frameworks

### 17.2 UX Success

* Users can expand from stratum to primitive without getting lost
* Compare mode is understandable in under 60 seconds
* Filters feel empowering, not confusing

### 17.3 Architecture Success

* New entity types can be added without redesigning the ontology
* Alternate frameworks can be overlaid without rewriting the explorer

---

## 18.0 Risks

### 18.1 Product Risks

* ontology becomes too abstract
* UI becomes graph spaghetti
* over-modeling slows iteration
* false confidence in classifications
* too many top-level modes confuse users

### 18.2 UX Risks

* drilldown state becomes hard to manage
* compare mode becomes cluttered
* too many filters overwhelm first-time users

### 18.3 Technical Risks

* poorly normalized data model blocks extensibility
* hardcoded framework assumptions break alternate overlay support
* weak state architecture causes brittle interactions

---

## 19.0 Non-Functional Requirements

* Fast initial load
* Smooth transitions
* Strong keyboard accessibility (full shortcut map defined in 6.5.9)
* URL-shareable states for filters and compare sets
* Mobile support for browse mode, desktop-first for compare mode
* Strong type safety and schema validation
* Easy content updates by non-developers later

### 19.1 Content Authoring Workflow

**MVP:** Product classifications are authored as structured JSON files in the repo. Changes go through PR review. Each product file must validate against the Entity + Placement + Capability schema before merge.

**Phase 2:** Admin UI with form-based editing, preview, and publish workflow. Non-developers can update classifications without touching JSON directly.

---

## 20.0 Implementation Recommendation

### 20.1 Build Order

1. Ontology schema
2. Explorer shell
3. Stratum drilldown accordion
4. Product detail page template
5. Compare basket + compare screen
6. Filter system
7. Framework overlay support
8. Evidence/rationale support

### 20.2 First Prototype Goal

A user should be able to:

* open the stack
* click L4
* expand into substrates
* select Azure AI Foundry and Kotana
* see where each spans strata
* compare them side by side
* understand where Azure-native ends and aftermarket begins

---

## 21.0 Product Summary One-Liner

**{a}OS Explorer is a modular, ontology-driven comparison web app that lets users browse, expand, filter, and compare AI systems from Stratum to Primitive across products, frameworks, agents, workflows, and skills.**
