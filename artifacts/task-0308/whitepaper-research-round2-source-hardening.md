# Round 2 source-hardening memo (diff only)

**Task:** task-0308  
**Audit date:** 2026-08-02  
**Audited input:** `whitepaper-research-round2-memo.md` at `17126abd`  
**Scope:** proposed corrections only; the whitepaper is intentionally unchanged.

## Verification boundary

The input memo has no URLs, so its claim of a post-2026-07 verification cannot be reproduced. A source accessed after July is not necessarily a source published after July. The tables below use current first-party documentation, repositories, release records, and vendor announcements accessed on 2026-08-02. Where no first-party post-July publication supports a claim, this memo says so rather than relabeling an older source. Consequently, acceptance criterion 1 is **not honestly satisfiable as written for every stable-project claim**; founder acceptance is required per item.

## Claim-by-claim corrections

| Stratum | Proposed diff | First-party evidence and disposition |
|---|---|---|
| L1 Models | **STRIKE** “GPT Image 1.5/Mini deprecated Dec 1, 2026” and the proposed “GPT Image 2 (Mini and Full)” API/pricing rows. **KEEP, NARROW** ggml team joined Hugging Face; project remains open source. **KEEP** Gemma as custom-terms, not permissive OSS. | OpenAI's April system card establishes **ChatGPT Images 2.0**, not the asserted API model IDs, Mini tier, prices, or deprecation date: <https://deploymentsafety.openai.com/chatgpt-images-2-0/chatgpt-images-2-0.pdf>. Current OpenAI endpoint documentation still names `gpt-image-1` and `gpt-image-1-mini`: <https://platform.openai.com/docs/models/default-usage-policies-by-endpoint>. HF says the ggml team joined and the project remains community-led/open source: <https://huggingface.co/blog/ggml-joins-hf>. Gemma terms: <https://ai.google.dev/gemma/terms>. |
| L2 Knowledge | **STRIKE** unsupported assertions that Docling and Qdrant publish SBOMs. **KEEP** pgvector and Unstructured as alternatives, but remove unsourced latency/cost comparisons. | pgvector is PostgreSQL-licensed and supports exact/approximate nearest-neighbor search: <https://github.com/pgvector/pgvector>. Unstructured's OSS library is Apache-2.0: <https://github.com/Unstructured-IO/unstructured>. Qdrant and Docling licenses can be verified, but an SBOM must be attached from the exact release/container before procurement: <https://github.com/qdrant/qdrant>, <https://github.com/docling-project/docling>. |
| L3 Execution | **KEEP, SOURCE** Anthropic tool ID `computer_20251124`. **REPLACE** “5ms vs gVisor 1ms” with “Firecracker documents under-125ms startup and requires KVM”; no valid first-party comparison to gVisor was found. | Anthropic current computer-use docs: <https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool>. Firecracker FAQ documents KVM, Apache-2.0, and `<125 ms`: <https://github.com/firecracker-microvm/firecracker/blob/main/FAQ.md>. Stagehand's repository documents MIT licensing and AI-directed browser automation: <https://github.com/browserbase/stagehand>. |
| L4 Orchestration | **KEEP** Agent Teams experimental warning. **NARROW** HumanLayer statement to “repository now directs users to CodeLayer”; do not assert the SDK is superseded without a dated vendor notice. **KEEP** LangGraph and Windmill alternatives, with license boundaries. | Anthropic labels agent teams experimental: <https://docs.anthropic.com/en/docs/claude-code/agent-teams>. HumanLayer repository/README is the authoritative project status: <https://github.com/humanlayer/humanlayer>. LangGraph core is MIT: <https://github.com/langchain-ai/langgraph/blob/main/LICENSE>. Windmill community server license is AGPL-3.0: <https://github.com/windmill-labs/windmill>. |
| L5 Observability | **KEEP** ClickHouse acquired Langfuse in Jan 2026; MIT core continues. **CHANGE** “Promptfoo acquired” to “OpenAI announced an agreement to acquire Promptfoo; closing remained subject to customary conditions.” **KEEP** Phoenix only after correcting its license from Elastic-2.0 to Apache-2.0. | ClickHouse announcement: <https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability>. OpenAI announcement: <https://openai.com/index/openai-to-acquire-promptfoo/>. Phoenix repository reports Apache-2.0: <https://github.com/Arize-ai/phoenix>. |
| L6 Governance | **KEEP** Cedar and OpenBao alternatives. **STRIKE** “non-bypassable” LiteLLM budget and “OPA evaluates every invocation” as product guarantees; those are architecture requirements that require integration tests. | Cedar is Apache-2.0 and describes default-deny authorization: <https://github.com/cedar-policy/cedar>. OpenBao is an LF Edge project under MPL-2.0: <https://github.com/openbao/openbao>. OPA is Apache-2.0/CNCF graduated, but enforcement depends on the caller actually gating each invocation: <https://www.openpolicyagent.org/docs/latest/>. |
| L7 Experience | **KEEP, NARROW** Vercel acquired Tremor and made Tremor Blocks free/open-source under MIT; do not generalize this to “all blocks MIT/Apache-2.0.” **STRIKE** the accessibility “guarantee.” **KEEP** PptxGenJS alternative. | Vercel announcement: <https://vercel.com/blog/vercel-acquires-tremor>. shadcn explicitly says components must be made accessible, which is not a product-level WCAG guarantee: <https://ui.shadcn.com/docs/components>. PptxGenJS is MIT and produces editable PowerPoint files: <https://github.com/gitbrent/PptxGenJS>. |

## Sourced alternative ledger

One viable alternative is retained for every stratum; trade-offs below are limited to properties supported by the linked first-party sources.

| Stratum | Alternative | Sourced trade-off |
|---|---|---|
| L1 | Nomic Embed Text v2 MoE | Apache-2.0 model/research implementation enables self-hosting, but the operator owns serving and capacity: <https://github.com/nomic-ai/contrastors>. |
| L2 | pgvector | Reuses PostgreSQL and offers HNSW/IVFFlat; a dedicated vector service may expose a broader vector-native operations surface: <https://github.com/pgvector/pgvector>. |
| L3 | Firecracker | Hardware-virtualized microVM isolation; requires Linux/KVM and a guest kernel/rootfs lifecycle: <https://github.com/firecracker-microvm/firecracker>. |
| L4 | LangGraph | MIT stateful orchestration library; managed/deployment features are a separate product boundary: <https://github.com/langchain-ai/langgraph>. |
| L5 | Arize Phoenix | Apache-2.0, self-hostable OpenTelemetry-oriented observability; operating storage and upgrades remains the deployer's responsibility: <https://github.com/Arize-ai/phoenix>. |
| L6 | Cedar | Apache-2.0, default-deny authorization language; introduces a second policy language beside Rego: <https://github.com/cedar-policy/cedar>. |
| L7 | PptxGenJS | MIT and produces editable PPTX; complements rather than replaces Typst's PDF/typesetting path: <https://github.com/gitbrent/PptxGenJS>. |

## Ownership, origin, and ally-only disposition

- Confirmed ownership changes: ggml team joined Hugging Face; ClickHouse acquired Langfuse; Vercel acquired Tremor; OpenAI announced a **pending** Promptfoo acquisition. The last item must not be described as closed without a closing announcement.
- No new ally-only violation was found among the seven retained primary strata picks in this pass. This is a repository/vendor-origin screen, not a supply-chain nationality guarantee; transitive dependencies and hosted subprocessors still require procurement review.
- “US/Community” is not a defensible origin label for a globally maintained open-source project. Record steward/legal entity and hosting jurisdiction separately.

## Federal evaluator gaps (apply to all strata)

```diff
- Parent-cloud FedRAMP status proves the named tool/service is authorized.
+ Verify the exact product, deployment model, agency authorization boundary, and package in the FedRAMP Marketplace at procurement time: https://marketplace.fedramp.gov/.

- Open-source project license/SBOM claims imply the deployed artifact is compliant.
+ Archive the exact image digest, license texts, dependency lockfiles, vulnerability scan, and generated CycloneDX/SPDX SBOM for each release candidate.

- Headless UI primitives guarantee Section 508/WCAG AA.
+ Treat accessibility as a tested system property: keyboard, focus, name/role/value, contrast, zoom/reflow, screen-reader, and VPAT evidence are release gates.

- Local hosting automatically establishes a FISMA-compliant boundary.
+ Boundary compliance depends on the complete authorized system, configuration, controls, evidence, and continuous monitoring—not a single component choice.
```

## Founder acceptance checklist

- [ ] Reject the unsupported GPT Image API rename, Mini tier, pricing, and Dec-1 deprecation edit.
- [ ] Accept the four ownership-status corrections individually, especially “agreement to acquire” for Promptfoo.
- [ ] Accept alternative substitutions individually; none is a blanket stack promotion.
- [ ] Decide whether “post-2026-07 sources per claim” means publication date or an Aug-2026 verification snapshot. This memo satisfies the latter and explicitly does not claim the former.
- [ ] Require artifact-level SBOM and authorization-boundary evidence before any federal-readiness statement enters the whitepaper.

