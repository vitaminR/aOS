# {a}OS7 Agentic Threat Model (task-0302)

## MITRE ATLAS mapping across the seven strata

> Companion to the [Government Proposal](../aos7-government-proposal-2026-08.md) and the [Technology Stack Whitepaper](../aos7-technology-stack-whitepaper-2026-08.md).

> **Assessment date:** 2026-08-01<br>
> **System basis:** [{a}OS Technology Stack Whitepaper, commit `377faf7`](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md)<br>
> **Threat vocabulary:** [MITRE ATLAS](https://atlas.mitre.org/) and the official [ATLAS 2026.07 data release](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml)<br>
> **Status:** design-stage threat model; implementation and operating effectiveness were not tested

## Executive answer

The seven-stratum design has a credible control spine: LLM Guard and NeMo Guardrails screen model-facing content; OPA constrains authorization; Infisical protects machine secrets; gVisor contains untrusted execution; and Langfuse plus DeepEval provide detection and evidence. Those are **selected stack components**, not evidence that the controls are deployed or effective.

This assessment covers **35 scenarios: five threat families in each of seven strata, mapped to 32 distinct ATLAS technique or subtechnique IDs**. Each stratum has five mapped IDs. The selected stack provides at least a partial preventive or detective control for 26 scenarios. **Nine scenarios are marked UNMITIGATED** because the whitepaper does not select a control that directly addresses the attack path:

1. L1 model integrity and poisoning;
2. L2 data-supply-chain provenance;
3. L2 knowledge/dataset integrity;
4. L4 orchestration dependency rug pulls;
5. L5 malicious dependency reputation inflation;
6. L6 poisoned agent-tool publication;
7. L7 UI software supply-chain compromise;
8. L7 response-rendering exfiltration; and
9. L7 poisoned model adoption.

The most important government-review message is therefore bounded: **{a}OS7 has named control substrates for the main agentic attack paths, while artifact provenance, workload identity, DLP/egress enforcement, immutable audit, and RAG ingestion integrity remain design work.** This is not an authorization-to-operate, FedRAMP, CMMC, Section 889, or other compliance determination.

## Evidence and interpretation rules

- The ATLAS technique name, ID, and attack behavior are sourced facts linked directly to MITRE.
- The mitigating pick is sourced to the whitepaper's committed decision table. “Selected” does not mean installed, configured, tested, or continuously monitored.
- Each residual-risk statement is an **analyst judgment** derived from the cited technique and the stated control boundary.
- “UNMITIGATED” means the whitepaper contains no selected control that directly prevents or detects the scenario. It does not mean no future control is possible.
- ATLAS mappings express analytical applicability. MITRE does not certify this system or endorse the control choices.

## Control anchors from the selected stack

| Control function | Selected whitepaper pick | Boundary used in this model |
|---|---|---|
| Model-content screening | [LLM Guard and NeMo Guardrails](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) | Screens inputs/outputs; cannot prove that permitted content is truthful or that a model/tool artifact is genuine. |
| Authorization | [Open Policy Agent (OPA)](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) | Can deny actions when identity, resource, purpose, and tool claims reach the policy decision point. |
| Machine secrets | [Infisical](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) | Removes plaintext credentials from agent configuration; does not itself issue least-privilege workload identities. |
| Execution containment | [gVisor](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L263-L271) | Reduces host impact from untrusted code; does not validate tool descriptions, outputs, or allowed network destinations. |
| Evidence and evaluation | [Langfuse and DeepEval](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) | Detective controls for traces, outcomes, and drift; detection depends on complete, trustworthy telemetry. |
| Human approval | [gotoHuman](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L344-L352) and [AG-UI](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L596-L604) | Adds an approval boundary; the human can still be deceived and the UI does not establish identity by itself. |
| Provider policy and budgets | [LiteLLM Proxy behind the existing router](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L63-L73) | Constrains provider/model routes and spend; an allowlisted provider or model can still be compromised. |

## L1 — Models & Infrastructure

Whitepaper basis: [L1 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L63-L73).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0051.001 — LLM Prompt Injection: Indirect](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L2609.001) | Retrieved web, document, or multimodal content instructs a frontier or local model to ignore system intent. | [LLM Guard + NeMo Guardrails](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513), applied before and after the model route. | **High:** novel encodings, multimodal payloads, and allowed-but-malicious instructions can bypass screening. |
| Tool/model supply-chain compromise | [AML.T0010.003 — AI Supply Chain Compromise: Model](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1171) | An approved provider route or downloaded local model serves a tampered artifact. | [LiteLLM allowlist](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L63-L73) limits reachable providers and models; this is a scope limiter, not an integrity check. | **High:** no signature, digest, model-card, or provenance verification is selected for an allowlisted artifact. |
| Agent identity abuse | [AML.T0012 — Valid Accounts](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1396) | A stolen provider token or service credential is used through a legitimate route. | [Infisical + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) protect secrets and can constrain the actions bound to an identity. | **High:** a valid but compromised identity remains effective until detected, revoked, or denied by contextual policy. |
| Data exfiltration | [AML.T0024 — Exfiltration via AI Inference API](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1808) | Repeated inference queries recover private training information, model behavior, or protected artifacts. | [LiteLLM](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L63-L73) rate/budget boundaries plus [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) trace review. | **High:** budgets and traces are detective/limiting controls, not proof that sensitive material cannot be inferred. |
| Model poisoning | [AML.T0018.000 — Poison AI Model](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1678) | Weights or training behavior are altered to create targeted or latent malicious responses. | **UNMITIGATED.** DeepEval may reveal behavior drift, but the selected stack has no model-integrity or training-lineage gate. | **Critical:** trigger-specific poisoning can survive ordinary evaluation and appear only under rare conditions. |

## L2 — Knowledge & Memory

Whitepaper basis: [L2 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L172-L181).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0070 — RAG Poisoning](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3379) | Malicious instructions or false assertions are placed where LlamaIndex will retrieve them into model context. | [LLM Guard](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) on retrieved chunks and assembled context. | **High:** semantic misinformation that contains no obvious instruction can pass a prompt-injection detector. |
| Tool/data supply-chain compromise | [AML.T0010.002 — AI Supply Chain Compromise: Data](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1139) | A trusted document feed, dataset, parser input, or annotation source is compromised before indexing. | **UNMITIGATED.** [Docling, LlamaIndex, and Qdrant](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L172-L181) move and store content but do not establish provenance. | **Critical:** a poisoned trusted source can propagate through re-indexing without a provenance or quarantine gate. |
| Agent identity abuse | [AML.T0082 — RAG Credential Harvesting](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3722) | An agent searches indexed repositories for secrets, tokens, or connection strings under a legitimate-looking query. | [Infisical + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) keep machine secrets out of documents and constrain retrieval authorization. | **High:** credentials already embedded in historical documents or code remain discoverable unless separately scanned and removed. |
| Data exfiltration | [AML.T0057 — LLM Data Leakage](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3069) | The model discloses retrieved private records, cross-user memory, or proprietary ledger content. | [OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) for retrieval authorization plus [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) for trace evidence. | **High:** vector-store metadata and source ACLs can diverge; traces do not stop a permitted response from containing excessive data. |
| Model/data poisoning | [AML.T0059 — Erode Dataset Integrity](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3088) | Gradual edits reduce the reliability of ledgers, graph facts, embeddings, or evaluation corpora. | **UNMITIGATED.** Git history helps human-readable files, but the selected L2 stack has no mandatory signed-ingest, data-quality, or rollback gate across every store. | **High:** low-rate corruption can look like ordinary data change and erode trust before detection. |

## L3 — Execution & Interfaces

Whitepaper basis: [L3 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L263-L271).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0051.002 — LLM Prompt Injection: Triggered](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L2609.002) | A browser event, email, issue, or external tool result activates hidden instructions when an agent acts. | [LLM Guard + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) screen tool data and re-authorize consequential calls. | **High:** event-driven agents may act before a human sees the content, and permitted actions can still be harmful in combination. |
| Tool supply-chain compromise | [AML.T0010.005 — AI Supply Chain Compromise: AI Agent Tool](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1218) | A FastMCP server, Playwright helper, integration package, or remote tool is malicious or compromised. | [gVisor](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L263-L271) contains code execution. | **High:** containment does not validate a tool's declared behavior or prevent abuse of network access explicitly granted to it. |
| Agent identity abuse | [AML.T0098 — AI Agent Tool Credential Harvesting](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4347) | A compromised agent queries connected tools and repositories for credentials. | [Infisical + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) separate secrets from content and authorize tool/resource pairs. | **High:** the whitepaper identifies short-lived, scoped agent credentials as an open design job. |
| Data exfiltration | [AML.T0086 — Exfiltration via AI Agent Tool Invocation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3919) | A legitimate email, browser, storage, or API tool sends sensitive data to an adversary-controlled destination. | [OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) for destination/action policy, [gVisor](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L263-L271) for containment, and [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) for evidence. | **Critical:** an allowed destination or opaque payload can carry data unless outbound content and egress are inspected. |
| Model/tool poisoning | [AML.T0110 — AI Agent Tool Poisoning](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4594) | An installed MCP/tool description, parameter, output, or hidden logic is altered to persistently redirect agent behavior. | [gVisor](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L263-L271) limits host impact and [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) can expose changed call patterns. | **High:** semantic poisoning can remain inside allowed permissions and look like normal tool behavior. |

## L4 — Orchestration & Decisioning

Whitepaper basis: [L4 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L344-L352).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0080 — AI Agent Context Poisoning](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3621) | Malicious memory or thread context alters plans, stop conditions, delegation, or tool selection across later runs. | [LLM Guard + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) plus [gotoHuman](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L344-L352) for high-impact decisions. | **High:** poisoned context can shape the evidence shown to both policy and human reviewers. |
| Tool supply-chain compromise | [AML.T0109 — AI Supply Chain Rug Pull](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4570) | A previously trusted workflow, scheduler, orchestration library, or agent package ships a malicious update. | **UNMITIGATED.** [Pydantic AI, Hatchet, and Dagu](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L344-L352) are orchestration substrates, not dependency-integrity gates. | **Critical:** reputation and prior clean versions do not protect a later update without pinning, signing, review, and rollback. |
| Agent identity abuse | [AML.T0081 — Modify AI Agent Configuration](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3694) | An attacker changes agent tools, endpoints, system instructions, budgets, or approval thresholds. | [OPA + Infisical](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) constrain changes; [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) supplies detective evidence. | **High:** controls fail if configuration changes bypass the policy point or audit identity is not strongly bound. |
| Data exfiltration | [AML.T0086 — Exfiltration via AI Agent Tool Invocation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3919) | A plan deliberately sequences permitted reads and writes to move protected data outward. | [OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513), [gotoHuman](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L344-L352), and [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439). | **Critical:** each step can be individually allowed while the end-to-end sequence violates purpose or data-handling intent. |
| Model/context poisoning | [AML.T0092 — Manipulate User LLM Chat History](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4143) | An attacker edits, inserts, or removes conversation history to hide persistence or redirect future decisions. | [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) supplies an independent trace view. | **High:** the whitepaper does not establish immutable, append-only, independently retained audit evidence. |

## L5 — Observability & Evaluation

Whitepaper basis: [L5 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0068 — LLM Prompt Obfuscation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3284) | Encoded, hidden, or multimodal instructions evade guardrails and human trace review. | [LLM Guard](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) plus [Langfuse and DeepEval](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439). | **High:** an obfuscation not represented in the detection/evaluation corpus can pass unnoticed. |
| Tool supply-chain compromise | [AML.T0111 — AI Supply Chain Reputation Inflation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4758) | Malicious packages, models, datasets, or MCP servers accumulate credible-looking adoption signals before selection. | **UNMITIGATED.** [Langfuse, DeepEval, and Healthchecks.io](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) observe runtime outcomes but do not authenticate provenance. | **High:** stars, downloads, prior clean behavior, and familiar maintainers can all be misleading trust signals. |
| Agent identity abuse | [AML.T0074 — Masquerading](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3467) | Malicious traces, task names, services, or agent metadata imitate a trusted identity. | [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) records attribution and sequence evidence. | **High:** logging attacker-supplied identity labels creates plausible but false attribution without cryptographic workload identity. |
| Data exfiltration | [AML.T0057 — LLM Data Leakage](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3069) | Sensitive prompt, response, tool, or retrieved data leaves the system or is copied into telemetry. | [Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) provides detective trace evidence. | **Critical:** the whitepaper names PII detection/redaction as an open gap, and telemetry itself can become a sensitive repository. |
| Model poisoning | [AML.T0031 — Erode AI Model Integrity](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1945) | Adversarial inputs or model changes gradually degrade outcomes and operator trust. | [DeepEval + Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) compare outcomes and expose drift. | **High:** trigger-specific degradation may not appear in routine test sets or aggregate metrics. |

## L6 — Governance & Trust

Whitepaper basis: [L6 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0051 — LLM Prompt Injection](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L2609) | Malicious instructions attempt to bypass system intent, safety policy, budgets, or human-approval boundaries. | [LLM Guard + NeMo Guardrails + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513). | **High:** guardrails are probabilistic and OPA can evaluate only the facts and action schema presented to it. |
| Tool supply-chain compromise | [AML.T0115.002 — AI Agent Tools](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4996) | A malicious MCP server or tool package is published and passes informal selection checks. | **UNMITIGATED.** The whitepaper explicitly lists MCP supply-chain vetting as an open gap; none of the [L6 picks](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) establishes publisher or artifact trust. | **Critical:** a poisoned tool enters behind the policy boundary and may receive legitimate permissions. |
| Agent identity abuse | [AML.T0083 — Credentials from AI Agent Configuration](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3738) | Static keys, tokens, or connection strings in agent configuration are stolen and replayed. | [Infisical + OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) externalize secrets and constrain authorized use. | **High:** secrets management alone does not provide short-lived, audience-bound, per-task credentials. |
| Data exfiltration | [AML.T0086 — Exfiltration via AI Agent Tool Invocation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3919) | A policy-compliant-looking tool call sends sensitive content to an attacker-controlled destination. | [OPA + Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) for authorization and trace evidence. | **Critical:** no selected DLP/content inspection or default-deny egress broker proves the payload is safe. |
| Model/data poisoning | [AML.T0020 — Training Data Poisoning](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1764) | Malicious or mislabeled data enters fine-tuning, evaluation, retrieval, or feedback pipelines. | [DeepEval + Langfuse](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L432-L439) provide detective testing and lineage evidence when instrumented. | **High:** the whitepaper states fine-tuning is not used today and selects no signed dataset lineage or training admission gate for future use. |

## L7 — Experience & Intent

Whitepaper basis: [L7 decisions](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L596-L604).

| Threat family | ATLAS mapping | Stratum-specific attack path | Mitigating pick from the whitepaper | Residual risk — analyst judgment |
|---|---|---|---|---|
| Prompt injection | [AML.T0051.000 — LLM Prompt Injection: Direct](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L2609.000) | A user enters malicious instructions through chat, voice, approval notes, or uploaded artifacts. | [LLM Guard + NeMo Guardrails](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513). | **High:** a valid user may intentionally misuse authorized capability, and accessibility channels add multimodal inputs. |
| Tool/software supply-chain compromise | [AML.T0010.001 — AI Supply Chain Compromise: AI Software](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1091) | A compromised chat, dashboard, approval, voice, or document-generation dependency alters what the user sees or approves. | **UNMITIGATED.** [assistant-ui, Next.js, AG-UI, Pipecat, and Typst](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L596-L604) are selected capabilities, not a software-integrity control. | **Critical:** a compromised presentation or approval dependency can falsify the last human-visible boundary. |
| Agent identity abuse | [AML.T0073 — Impersonation](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3442) | An attacker poses as a trusted operator, approver, vendor, or agent to obtain approval or sensitive output. | [AG-UI](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L596-L604) presents evidence and [OPA](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L504-L513) constrains the approved action. | **High:** the approval UX does not independently establish who is approving, and convincing evidence can itself be fabricated. |
| Data exfiltration | [AML.T0077 — LLM Response Rendering](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3546) | Generated Markdown, HTML, or media embeds sensitive data in an automatic request to an attacker-controlled resource. | **UNMITIGATED.** The [L7 UI picks](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md#L596-L604) do not specify safe rendering, URL proxying, or remote-resource blocking. | **Critical:** exfiltration can occur when content renders, before a user clicks or recognizes the request. |
| Model poisoning | [AML.T0115.001 — Models](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4974) | A poisoned model is adopted and generates convincing but targeted false guidance in the user-facing layer. | **UNMITIGATED.** Guardrails may filter harmful content, but no selected L7 or L1 control authenticates model provenance or intended behavior. | **Critical:** a polished interface can increase trust in targeted malicious outputs. |

## Cross-stratum attack chains

### Chain A — indirect prompt to exfiltration

1. Malicious external content enters L2/L7 as [AML.T0051.001](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L2609.001) or [AML.T0070](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3379).
2. L4 context changes the plan through [AML.T0080](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3621).
3. L3 invokes a legitimate write-capable tool and exfiltrates data through [AML.T0086](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3919).
4. L5 may record the sequence in Langfuse, but a trace is evidence after the fact unless OPA or a human approval blocks the action.

### Chain B — trusted dependency to persistent compromise

1. A component builds credibility through [AML.T0111](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4758).
2. A later malicious update performs [AML.T0109](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4570).
3. A compromised MCP/tool persists through [AML.T0110](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4594).
4. gVisor limits host impact, but an authorized tool can still manipulate outputs or use permitted network and data access.

### Chain C — stolen identity to governance bypass

1. The attacker retrieves a configuration credential through [AML.T0083](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3738) or tool-connected content through [AML.T0098](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L4347).
2. The attacker operates as a [valid account (AML.T0012)](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L1396).
3. Agent configuration is altered through [AML.T0081](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml#L3694), changing routes, tools, or approval thresholds.
4. Infisical and OPA reduce exposure only if credentials are short-lived, identity claims are trustworthy, and every control path is enforced.

## Security treatment backlog

This is a proposed risk-treatment order, not a fleet priority or implementation assignment.

| Treatment order | Control gap | Minimum evidence needed to close the gap | Decision status |
|---|---|---|---|
| 1 | **Outbound DLP and egress control** for agent tools and rendered content | Default-deny destination policy; content inspection/redaction; remote-resource proxy or block; tests proving sensitive canaries do not leave through email, browser, storage, API, Markdown, HTML, image, audio, or telemetry paths. | **FOUNDER DECISION:** acceptable destinations, false-positive tolerance, and whether government data may reach commercial model providers. |
| 2 | **Workload identity and credential brokering** | Short-lived, audience-bound, per-agent/per-task credentials; OPA input bound to verified workload identity; automatic revocation; replay and confused-deputy tests. | **FOUNDER DECISION:** identity authority and commercial-Azure versus self-hosted trust boundary. |
| 3 | **Artifact, model, dataset, container, and MCP provenance** | Approved registries; immutable digests; signed releases/attestations; SBOM/AIBOM/model/data cards; dependency pinning; update review; rollback drill. | **FOUNDER DECISION:** signer trust roots and the exception process for unsigned artifacts. |
| 4 | **RAG and memory admission integrity** | Source identity, ACL preservation, quarantine, malware/injection scan, reviewer provenance, content hash, re-index audit, deletion/rollback proof. | Open design work; no selected control currently closes it. |
| 5 | **Independent immutable audit** | Append-only storage outside the agent's write authority; verified identity, policy decision, approval, tool input/output hash, and model route per event; retention and tamper tests. | **FOUNDER DECISION:** paid Langfuse audit capability versus an external compensating store. |
| 6 | **Adversarial evaluation and continuous detection** | ATLAS-tagged test corpus for direct, indirect, triggered, obfuscated, RAG, tool, exfiltration, identity, and poisoning cases; release thresholds; regression history; incident runbooks. | Extend DeepEval/Langfuse after the preventive boundaries are defined. |

## Proposal-safe wording

Use:

> “{a}OS7 is designed around seven explicit responsibility boundaries and maps agentic threats to MITRE ATLAS. The selected architecture includes policy enforcement, secret management, sandboxing, content guardrails, human approval, and trace/evaluation substrates. The current threat model identifies nine scenarios without a directly selected preventive or detective control; those gaps become measurable implementation and verification work in the pilot.”

Avoid:

- “ATLAS compliant” or “MITRE certified”; ATLAS is a threat knowledge base, not a certification.
- “Secure,” “zero trust,” “government ready,” or “ATO ready” without deployed-control and operating-effectiveness evidence.
- Treating the ally-only model allowlist as supply-chain assurance, statutory compliance, or proof of model integrity.
- Treating Langfuse traces as immutable audit without separate evidence about identity binding, retention, tamper resistance, and write authority.
- Claiming OPA prevents prompt injection; OPA can deny modeled actions, while model-content attacks still require guardrails, isolation, and testing.

## Verification checklist

- [x] Seven strata covered.
- [x] Five threat families covered in every stratum.
- [x] Five ATLAS mappings per stratum; minimum required was two.
- [x] 35 scenario rows and 32 distinct ATLAS technique/subtechnique IDs.
- [x] Every scenario names a selected mitigating tool or says **UNMITIGATED**.
- [x] Every scenario states residual risk.
- [x] MITRE technique links and immutable whitepaper source links are present in every scenario row.
- [x] Selected architecture is separated from verified implementation.
- [x] No compliance, past-performance, deployment, or control-effectiveness claim is made.
- [x] No direct DoD funding route is recommended.

## Primary sources

1. [MITRE ATLAS threat matrix](https://atlas.mitre.org/)
2. [MITRE ATLAS Data repository](https://github.com/mitre-atlas/atlas-data)
3. [MITRE ATLAS 2026.07 data release, pinned at commit `2306ecaf`](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/v6/ATLAS-2026.07.yaml)
4. [MITRE ATLAS release manifest and version pointers](https://github.com/mitre-atlas/atlas-data/blob/2306ecaf04fb7a14be068b97e3ff40c2d9112e28/dist/manifest.yaml)
5. [{a}OS Technology Stack Whitepaper at the cited source commit](https://github.com/vitaminR/aOS/blob/377faf70b298b29d48f49912785f82ebd0ecc1f2/03.Research/aos7-technology-stack-whitepaper-2026-08.md)
