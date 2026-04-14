# AFS12 — Research Pack: A Framework for Every AI Platform Decision

## Core Thesis

The {a}OS 7-stratum model, built through 11 posts of Azure AI Foundry analysis, reveals a universal pattern in managed AI platforms: strong at L1-L3 (Models, Knowledge, Execution), partial at L4 (Orchestration), and structurally weak at L5-L7 (Observability, Governance, Experience). The framework is portable — it applies to Azure, AWS, GCP, and internal platforms equally. What appeared to be "one governance gap" is actually three distinct strata with different owners, tools, and failure modes.

## Key Facts

- Azure AI Foundry: Strong L1-L3, preview L4, weak L5-L6, partial L7
- AWS Bedrock: Strong L1-L3, preview L4, weak L5-L6, partial L7 — same pattern
- Vertex AI: Strong L1-L3, partial L4-L5 (slightly better observability), weak L6, partial L7 — same shape
- Internal platforms built on top of these services inherit the same gaps and often make them worse
- All three major platforms invest in developer adoption (L1-L3) and agent capability (L3-L4) because those drive PLG and demo well
- None invest deeply in L5-L7 because those require org-specific customization that is hard to productize
- The gap is a rational product boundary, not negligence or a roadmap oversight

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Same pattern across platforms | Azure: Content Safety only at L6, no workflow governance. AWS: Guardrails = I/O filtering only. Vertex: Model monitoring only. None ship compliance reporting, approval gates, or cost enforcement natively. |
| R2 | Three strata, not one gap | L5 (observability) is owned by platform/SRE. L6 (governance) is owned by security/compliance. L7 (experience) is owned by product. Different owners, different tools, different failure modes. Collapsing them into "governance" hides the problem. |
| R3 | Framework portability | The 7-stratum mapping was built on Azure AI Foundry, tested against AWS Bedrock and Vertex AI documentation, and applied to two internal platforms. The coverage pattern is consistent across all five. |
| R4 | Series arc integrity | Post 1 named the gap without a framework. Post 3 introduced {a}OS and gave the gap coordinates. Post 12 proves the coordinates work on any map. The arc is: problem → framework → universality. |
| R5 | Explorer is open source | github.com/vitaminR/aos-explorer — MIT license. Community can map their own platforms, add products, validate or challenge the taxonomy. The framework is open to scrutiny by design. |

## Cross-Platform Coverage Summary

| Stratum | Azure AI Foundry | AWS Bedrock | Vertex AI | Internal (typical) |
|---|---|---|---|---|
| L7 Experience | Partial | Partial | Partial | Weak |
| L6 Governance | Weak | Weak | Weak | Very Weak |
| L5 Observability | Weak | Weak | Partial | Weak |
| L4 Orchestration | Partial (preview) | Partial (preview) | Partial | Custom |
| L3 Execution | Strong | Strong | Strong | Strong |
| L2 Knowledge | Good | Good | Good | Varies |
| L1 Models | Strong | Strong | Strong | Inherited |

## Anti-Patterns to Avoid in Post

- Do not declare victory — the framework is useful, not complete. It emerged; it was not designed.
- Do not bash vendors — the pattern is structural and rational, not negligent
- Do not over-explain the model — 11 posts did that. This post zooms out.
- Do not use "Part 12 of 12" — the post must stand alone for new readers
- Do not make it a product pitch — the Explorer is a tool shared openly, not a launch
- Do not be grandiose — reflective authority, not TED Talk energy
- Callbacks to Post 1 and Post 3 should feel natural, not forced
