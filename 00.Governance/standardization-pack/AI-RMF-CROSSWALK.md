# AI RMF Crosswalk

## What an AI RMF crosswalk is

A **crosswalk** is a mapping table between one framework and another framework.

In this case, an **AI RMF crosswalk** maps `{a}OS` concepts to the **NIST AI Risk Management Framework (AI RMF)** to document:

- where `{a}OS` aligns with AI RMF
- where `{a}OS` helps operationalize AI RMF ideas
- where `{a}OS` goes beyond AI RMF
- where there is **no direct mapping**

## What a crosswalk is not

A crosswalk is **not** a claim that both frameworks are identical.

A good crosswalk is honest about:

- strong alignment
- partial alignment
- support / implementation relationship
- extension / additional detail
- no direct match

## Why this matters

A good AI RMF crosswalk helps answer:

- Why does `{a}OS` matter beyond its own vocabulary?
- How does it connect to widely used AI governance language?
- Can architecture teams use `{a}OS` without abandoning AI RMF?

## Recommended relationship labels

Recommended relationship labels for the mapping table:

- `aligns strongly`
- `partially aligns`
- `supports implementation`
- `extends beyond AI RMF`
- `no direct mapping`

## Starter mapping table

> Treat the rows below as **draft starter rows**, not final truth.

| aOS Artifact | Type | aOS Meaning | NIST AI RMF Element | Relationship | Notes / Rationale |
| --- | --- | --- | --- | --- | --- |
| L6 Governance & Trust | Stratum | Policy, approval, accountability, trust controls | Govern | aligns strongly | Strongest top-level alignment candidate |
| L5 Observability & Evaluation | Stratum | Evaluation, telemetry, monitoring, validation | Measure / Manage | aligns strongly | Natural home for performance and monitoring evidence |
| Governance & Trust | Axis | Cross-cutting governance concern across strata | Govern | aligns strongly | Cross-cutting version of governance activity |
| Observability & Evaluation | Axis | Cross-cutting visibility and evaluation concern | Measure | aligns strongly | Strong overlap with measurement and monitoring concerns |
| Confidence / rationale / evidence fields | Schema fields | Classification support metadata | Govern / Measure | supports implementation | Helps explain and defend classification decisions |
| Primary / secondary placement model | Classification rule | Distinguishes core vs supporting role | Map | partially aligns | Useful for characterization, but not a one-to-one AI RMF concept |
| Stratum → Substrate → Construct → Primitive | Reference hierarchy | Multi-level architecture and classification drilldown | No single direct AI RMF equivalent | extends beyond AI RMF | This is likely where `{a}OS` adds distinct structure |

## Questions each row should answer

For each proposed mapping, ask:

1. Is this a real conceptual match, or just similar wording?
2. Does `{a}OS` provide structure where AI RMF stays higher-level?
3. Is the relation one-to-one, one-to-many, or only partial?
4. Would a skeptical reviewer accept this mapping?
5. What evidence or explanation supports the claim?

## Suggested workflow

1. Start with top-level strata and axes
2. Map only strong alignments first
3. Mark weak matches honestly
4. Add rationale before adding more rows
5. Avoid forcing every `{a}OS` term into AI RMF language

## Relevant NIST links

- AI RMF overview: <https://www.nist.gov/itl/ai-risk-management-framework>
- AI RMF Playbook: <https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook>
- AI RMF crosswalks page: <https://www.nist.gov/itl/ai-risk-management-framework/crosswalks-nist-artificial-intelligence-risk-management-framework>
- NIST contact for crosswalk comments: `AIframework@nist.gov`
