# APR004 — Research Pack: {a}OS 6-Layer AI/ML Model

## Core Thesis

AI systems need a shared reference architecture the way networking needed OSI. The {a}OS-6L model provides 6 layers with clear boundaries, vendor-neutral naming, and practical debugging utility.

## Key Facts

- AI vocabulary is fragmented: "tool" vs "skill" vs "action" vs "capability" across Azure, AWS, OpenAI, Anthropic
- No existing framework covers the full stack from compute (L1) through human oversight (L6)
- The OSI Model succeeded because it gave networking engineers a shared language — {a}OS aims for the same in AI
- v0.1 scope: layer definitions and boundaries. Next: canonical glossary, vendor crosswalks, rollout guidance

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Vocabulary fragmentation exists | Direct comparison of Azure AI Foundry, Semantic Kernel, AutoGen, LangChain, Anthropic API docs — same concepts, different names |
| R2 | OSI analogy is apt | OSI succeeded by providing clear layer boundaries that let experts in different layers communicate. Same need exists in AI |
| R3 | Production cost of ambiguity | Author experience: debugging cross-vendor agent systems where "the agent failed" could mean model error (L1), context overflow (L2), tool timeout (L3), or orchestration misroute (L5) |
| R4 | Vendor-neutral is achievable | Layer names deliberately avoid vendor-specific terms (no "Semantic Kernel", no "Bedrock", no "Foundry") |

## Anti-Patterns to Avoid in Post

- Don't position as "replacing" existing frameworks (additive, not competitive)
- Don't overclaim adoption before it happens (this is v0.1, be honest)
- Don't make it too academic — the value is practical debugging, not taxonomy for taxonomy's sake
