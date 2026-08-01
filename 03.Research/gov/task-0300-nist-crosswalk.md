# {a}OS NIST Crosswalk: AI RMF and SP 800-53 rev 5 (task-0300)

> Companion to the [Government Proposal](../aos7-government-proposal-2026-08.md) Section 6 and the [Technology Stack Whitepaper](../aos7-technology-stack-whitepaper-2026-08.md).
> **Date:** 2026-08-01 · **Method:** mapped against NIST AI 100-1 (AI RMF 1.0), NIST AI 600-1 (Generative AI Profile), and SP 800-53 rev 5 with live document verification; an adversarial pass spot checked cited IDs. Corrections are annotated inline.
> **Discipline:** tools SUPPORT controls; only an assessor decides satisfaction. Nothing below claims an authorization outcome.
> **Why this exists now:** NIST COSAiS is drafting 800-53 control overlays for single agent and multi agent AI systems. Mapping the stack to the base documents today positions {a}OS to adopt those overlays the day they publish.

## NIST AI RMF 1.0 + Generative AI Profile

### L1 Models and Infrastructure

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **GOVERN 6.1** | The LiteLLM gateway enforces an ally origin model allowlist, which is exactly an approved provider list for third party GAI technology, applied at the only place model traffic can pass. | NIST AI 100-1, Sec. 5.1 Table 1, GOVERN 6.1; NIST AI 600-1, action GV-6.1-007 (inventory third party entities and establish approved GAI technology and service provider lists) |
| **MANAGE 3.1** | The gateway applies organizational risk tolerance and controls to every third party model call (allowlist, routing, per agent budget), giving a single documented choke point for third party resource risk (SP 800-53 rev 5 SA-9 and AC-4 in overlay terms). | NIST AI 100-1, Sec. 5.4 Table 4, MANAGE 3.1; NIST AI 600-1, action MG-3.1-001 (apply organizational risk tolerances and controls to third party GAI resources) |
| **GOVERN 6.2** | llama.cpp local models on the self managed Linux server are the rollover and fallback path when frontier APIs fail, are cut off, or must be avoided for a given data class. | NIST AI 100-1, Sec. 5.1 Table 1, GOVERN 6.2; NIST AI 600-1, action GV-6.2-006 (test and manage risks related to rollover and fallback technologies for GAI systems) |

### L2 Knowledge and Memory

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **MEASURE 2.10** | Qdrant, Mem0, and SQLite all run inside the boundary and agency data never leaves it, which is the examined and documented privacy posture MEASURE 2.10 asks for (SP 800-53 rev 5 SC-7 boundary protection and AC-4 information flow enforcement in overlay terms). | NIST AI 100-1, Sec. 5.3 Table 3, MEASURE 2.10; NIST AI 600-1, Sec. 2.4 Data Privacy |
| **MEASURE 2.5** | LlamaIndex RAG over Docling parsed agency documents grounds generations in retrievable sources, the specific check AI 600-1 asks for on retrieval augmented generation data, directly reducing confabulation risk. | NIST AI 600-1, action MS-2.5-005 (verify that retrieval augmented generation data is grounded) and Sec. 2.2 Confabulation; NIST AI 100-1, Table 3, MEASURE 2.5 |
| **GOVERN 1.6** | Mem0 memory plus SQLite state give each agent a queryable system of record whose entries carry source and versioning information, feeding the AI system inventory with the provenance fields the GAI profile lists. | NIST AI 100-1, Table 1, GOVERN 1.6; NIST AI 600-1, action GV-1.6-003 (inventory entries include data provenance information such as source and versioning) |

### L3 Execution and Interfaces

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **MEASURE 2.7** | The gVisor sandboxed runtime contains tool and code execution, limiting blast radius from the autonomous agent and compromised dependency threats MS-2.7-001 says to assess (SP 800-53 rev 5 SC-39 process isolation, CM-7 least functionality). | NIST AI 600-1, action MS-2.7-001 (assess vulnerabilities and threats such as compromised dependencies and autonomous agents); NIST AI 100-1, Table 3, MEASURE 2.7 |
| **MAP 1.1** | FastMCP tool servers declare typed, scoped tool schemas, so the intended purpose and limits of every capability an agent can invoke are documented artifacts rather than implicit behavior. | NIST AI 100-1, Sec. 5.2 Table 2, MAP 1.1 (intended purposes and assumptions understood and documented) |
| **GOVERN 6.1** | Composio integrations enter the stack as third party tools and APIs, which the GAI profile says must pass acquisition due diligence covering security, data privacy, and monitoring. | NIST AI 600-1, action GV-6.1-009 (due diligence for GAI acquisition across tools and APIs and embedded tools); NIST AI 100-1, Table 1, GOVERN 6.1 |

### L4 Orchestration and Decisioning

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **GOVERN 2.1** | The file based coordination floor with ticket board and claim protocol binds every task to a named agent with a visible lifecycle, documenting roles, responsibilities, and lines of communication. | NIST AI 100-1, Sec. 5.1 Table 1, GOVERN 2.1 (roles, responsibilities, and lines of communication are documented and clear); same subcategory text restated in NIST AI 600-1 GOVERN 2.1 table |
| **MEASURE 2.6** | Hatchet durable workflows plus the Dagu scheduler give deterministic retries, resumption, and recovery, the fail safe and error recovery architecture property MS-2.6-005 says to verify. | NIST AI 600-1, action MS-2.6-005 (verify the system architecture can handle, recover from, and repair errors); NIST AI 100-1, Table 3, MEASURE 2.6 (fails safely, response times for failures) |
| **MEASURE 2.5** | Pydantic AI typed agents validate every model output against a schema before it propagates, a structural validity check on each step of a workflow. | NIST AI 100-1, Table 3, MEASURE 2.5 (system demonstrated to be valid and reliable) |

### L5 Observability and Evaluation

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **MEASURE 1.1** | DeepEval encodes the selected metrics for the most significant risks and its CI exit code makes the measurement mechanical and repeatable rather than judgment based. | NIST AI 100-1, Sec. 5.3 Table 3, MEASURE 1.1 (approaches and metrics selected for implementation starting with the most significant risks) |
| **GOVERN 1.3** | The DeepEval CI exit code functions as the minimum threshold go or no go deployment approval the GAI profile calls for, wired into the pipeline so a failing eval blocks release. | NIST AI 600-1, action GV-1.3-002 (establish minimum thresholds for performance as part of go or no go deployment approval) |
| **MANAGE 4.1** | The Langfuse trace store plus Healthchecks.io dead man monitoring implement post deployment monitoring with an alert when any scheduled loop goes silent (SP 800-53 rev 5 SI-4 system monitoring in overlay terms). | NIST AI 100-1, Sec. 5.4 Table 4, MANAGE 4.1; NIST AI 600-1, action MG-4.1-002 (establish and evaluate processes for post deployment monitoring of GAI systems) |
| **MEASURE 2.8** | OpenTelemetry GenAI semantic convention spans record every generation with model, input, and outcome attributes, giving the per instance traceability and accountability record MEASURE 2.8 wants examined (SP 800-53 rev 5 AU-2 event logging). | NIST AI 100-1, Table 3, MEASURE 2.8; NIST AI 600-1, action MS-2.8-003 (document each instance where content is generated to enable traceability) |

### L6 Governance and Trust

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **GOVERN 3.2** | The human decision queue with named approvals defines and differentiates who oversees which agent action, the human-AI configuration and oversight roles this subcategory requires. | NIST AI 100-1, Sec. 5.1 Table 1, GOVERN 3.2; NIST AI 600-1, GOVERN 3.2 action table (GV-3.2-001 through GV-3.2-005) |
| **MANAGE 2.4** | The OPA policy gate encodes deny criteria evaluated before every risky action and LiteLLM hard budgets deactivate an agent at its cap, together forming the supersede, disengage, or deactivate mechanism with codified criteria. | NIST AI 100-1, Sec. 5.4 Table 4, MANAGE 2.4; NIST AI 600-1, action MG-2.4-004 (establish and regularly review specific criteria that warrant deactivation) |
| **MEASURE 2.7** | LLM Guard screens prompts and outputs against prompt injection, the attack AI 600-1 names explicitly under Information Security, while Infisical keeps machine secrets out of prompts and repos (SP 800-53 rev 5 IA-5 authenticator management). | NIST AI 600-1, Sec. 2.9 Information Security (prompt injection, data poisoning) and action MS-2.7-007 (AI red teaming against adversarial prompts and prompt injection); NIST AI 100-1, Table 3, MEASURE 2.7 |
| **MANAGE 3.2** | NeMo Guardrails implements the rule based content filters the GAI profile prescribes for flagging problematic inputs and outputs from the pre trained models in use. | NIST AI 600-1, action MG-3.2-005 (implement content filters, rule based or model based, to flag problematic inputs and outputs); NIST AI 100-1, Table 4, MANAGE 3.2 |

### L7 Experience and Intent

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **MAP 3.5** | The AG-UI approval wire routes consequential actions into a decision dock where a named human approves or rejects, making the human oversight process an implemented, inspectable artifact. | NIST AI 100-1, Sec. 5.2 Table 2, MAP 3.5 (processes for human oversight are defined, assessed, and documented per GOVERN function policies) |
| **GOVERN 3.2** | assistant-ui chat plus the decision dock fix the acceptable human-AI configuration for chat and decision tasks, including what the assistant refuses and what must escalate to a person. | NIST AI 600-1, action GV-3.2-003 (define acceptable use policies for GAI interfaces, modalities, and human-AI configurations, for chatbots and decision making tasks); NIST AI 100-1, Table 1, GOVERN 3.2 |
| **GOVERN 5.1** | Pipecat voice is the surface where interaction with an AI is disclosed to the user before interactive activities begin, the disclosure the GAI profile asks for in higher risk contexts. | NIST AI 600-1, action GV-5.1-002 (document interactions with GAI systems to users prior to interactive activities) |
| **MEASURE 2.11** | Accessibility as design North Star targets the adoption, inclusion, and accessibility harms the GAI profile files under Harmful Bias and Homogenization, and the profile explicitly lists increased accessibility of GAI tools and interfaces as an organizational action. | NIST AI 600-1, Sec. 2.6 Harmful Bias and Homogenization and action GV-3.2-002 (increased accessibility of GAI tools, interfaces, and systems); NIST AI 100-1, Table 3, MEASURE 2.11 |

**Overlay note:** COSAiS status as of August 2026: NIST's project SP 800-53 Control Overlays for Securing AI Systems (COSAiS) published its concept paper on August 14, 2025, proposing five overlays that adapt SP 800-53 rev 5 controls to AI use cases: (1) adapting and using generative AI (assistant/LLM), (2) using and fine tuning predictive AI, (3) using AI agent systems, single agent, (4) using AI agent systems, multi agent, and (5) security controls for AI developers (the last one connects to the SSDF Community Profile). The only published discussion draft so far is the annotated outline for the Predictive AI overlay, released January 8, 2026 with comments due February 13, 2026. The single agent and multi agent overlays are named use cases on the CSRC project site but have no published draft yet; development runs through NIST's public Slack collaboration channel, and outside trackers expect agent overlay drafts in late 2026 through 2027. Sources: csrc.nist.gov/projects/cosais, csrc.nist.gov/Projects/cosais/use-cases, the concept paper PDF at csrc.nist.gov/csrc/media/Projects/cosais/documents/NIST-Overlays-SecuringAI-concept-paper.pdf, and the January 2026 Predictive AI annotated outline on the same site. What mapping early buys a vendor: first, the overlays are 800-53 rev 5 tailorings, and this stack already speaks 800-53 vocabulary at its choke points (SC-7/AC-4 at the data boundary, SC-39/CM-7 in the gVisor sandbox, IA-5 via Infisical, SI-4/AU-2 via Langfuse and OTel, SA-9 at the LiteLLM gateway), so when the agent overlay drafts land the vendor shows a preexisting control narrative instead of a retrofit. Second, the single agent and multi agent overlays are widely expected to seed future federal procurement baselines (a FedRAMP style trajectory), so early alignment is a sales asset for government adjacent buyers. Third, the drafts are being written now in an open process, and a vendor with a running reference stack can shape the control language through the Slack channel and comment windows rather than react to it. Fourth, the multi agent overlay will likely be the first authoritative treatment of coordination risks between agents (claims, tickets, inter agent messaging, delegation), which this stack already implements as explicit, inspectable controls at L4; being able to point at a working implementation of controls the overlay is still drafting is a differentiator no paper compliance program can match. Honest caveat: nothing can claim conformance to the single agent or multi agent overlays today because no draft exists to conform to; the defensible claim is alignment to AI RMF 1.0 and AI 600-1 now, 800-53 rev 5 control mapping now, and overlay readiness when the drafts publish.

## SP 800-53 rev 5 control families

### L1 Models and Infrastructure

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **SC-7 Boundary Protection** | The LiteLLM gateway is the single managed egress point for all frontier model API traffic, which SUPPORTS boundary protection at the model access layer. | SP 800-53 rev 5, SC-7 |
| **CM-7 Least Functionality** | The enforced ally origin model allowlist restricts invokable models to an approved set, which SUPPORTS least functionality for the model layer. | SP 800-53 rev 5, CM-7 |
| **SA-9 External System Services** | Routing every frontier API call through one gateway gives a single point to define and monitor requirements for external model providers, which SUPPORTS oversight of external system services. | SP 800-53 rev 5, SA-9 |
| **SR-3 Supply Chain Controls and Processes** | The ally origin policy applies an explicit provenance rule to model suppliers, which SUPPORTS supply chain controls for the model supply chain, a risk NIST names as value chain and component integration. | SP 800-53 rev 5, SR-3; NIST AI 600-1, sec. 2 (Value Chain and Component Integration risk) |

### L2 Knowledge and Memory

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **AC-4 Information Flow Enforcement** | Keeping Qdrant, SQLite, and Mem0 inside the boundary with a stated rule that agency data never leaves SUPPORTS information flow enforcement for agency data. | SP 800-53 rev 5, AC-4 |
| **SI-10 Information Input Validation** | Docling parses untrusted documents into normalized structured text before LlamaIndex ingestion, which SUPPORTS validation of information inputs to the RAG pipeline. | SP 800-53 rev 5, SI-10 |
| **SI-12 Information Management and Retention** | Mem0 provides a managed memory store where agent memories can be listed, updated, and deleted, which SUPPORTS information management and retention practices for AI memory. | SP 800-53 rev 5, SI-12 |

### L3 Execution and Interfaces

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **SC-39 Process Isolation** | The gVisor sandboxed runtime isolates tool execution from the host kernel with a userspace syscall boundary, which SUPPORTS process isolation for agent-executed code. | SP 800-53 rev 5, SC-39 |
| **CM-7 Least Functionality** | FastMCP tool servers expose a finite declared tool list instead of a general shell, which SUPPORTS least functionality for the agent action surface. | SP 800-53 rev 5, CM-7 |
| **SA-9 External System Services** | Composio centralizes third party SaaS connections in one brokered service, which SUPPORTS defining and monitoring security requirements for external system services used by agents. | SP 800-53 rev 5, SA-9 |

### L4 Orchestration and Decisioning

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **SI-10 Information Input Validation** | Pydantic AI enforces typed schemas on agent inputs and outputs at every orchestration step, which SUPPORTS information input validation between agents and workflows. | SP 800-53 rev 5, SI-10 |
| **CP-10 System Recovery and Reconstitution** | Hatchet durable workflows checkpoint state and resume interrupted runs, which SUPPORTS recovery and reconstitution of agent work after failure. | SP 800-53 rev 5, CP-10 |
| **AC-5 Separation of Duties** | The ticket board claim protocol assigns one recorded owner per task and separates the doer from the reviewer in the lifecycle, which SUPPORTS separation of duties among agents. | SP 800-53 rev 5, AC-5 |

### L5 Observability and Evaluation

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **AU-2 Event Logging** | OpenTelemetry GenAI semantic conventions define which model and tool interactions get emitted as gen_ai spans, which SUPPORTS selection and consistent capture of auditable AI events. | SP 800-53 rev 5, AU-2 |
| **AU-3 Content of Audit Records** | Langfuse stores traces with actor, timestamps, inputs, outputs, and token costs, which SUPPORTS complete audit record content for AI actions. | SP 800-53 rev 5, AU-3 |
| **CA-7 Continuous Monitoring** | DeepEval in CI with hard exit codes plus Healthchecks.io dead man monitoring SUPPORTS ongoing assessment that agent behavior and scheduled functions remain within expectations. | SP 800-53 rev 5, CA-7 |

### L6 Governance and Trust

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **AC-3 Access Enforcement** | OPA evaluates policy before risky actions execute and the human decision queue holds high impact actions for a named approval, which SUPPORTS access enforcement over agent actions. | SP 800-53 rev 5, AC-3 |
| **IA-5 Authenticator Management** | Infisical issues, stores, and rotates machine secrets from one place, which SUPPORTS authenticator management for service and agent credentials. | SP 800-53 rev 5, IA-5 |
| **SI-10 Information Input Validation** | LLM Guard screens prompts for injection and NeMo Guardrails constrains content on the way in and out, which SUPPORTS input validation and output filtering for model traffic against the GAI information security risk. | SP 800-53 rev 5, SI-10; NIST AI 600-1, sec. 2 (Information Security risk) |
| **SC-6 Resource Availability** | LiteLLM hard budget enforcement per agent caps spend and call volume, which SUPPORTS resource availability protections including denial of wallet defense. | SP 800-53 rev 5, SC-6 |

### L7 Experience and Intent

| Maps to | How the stack supports it | Citation |
|---|---|---|
| **AC-3 Access Enforcement** | The AG-UI approval wire routes high impact agent actions into a decision dock where a human must explicitly authorize before execution, which SUPPORTS access enforcement at the human oversight point consistent with AI RMF human oversight roles. | SP 800-53 rev 5, AC-3; NIST AI 100-1, GOVERN 3.2 (roles for human oversight of AI) |
| **AU-3 Content of Audit Records** | The decision dock captures the named approver, the action, and the outcome for each approval, which SUPPORTS audit record content that ties consequential actions to a person. | SP 800-53 rev 5, AU-3 |
| **SC-15 Collaborative Computing Devices and Applications** | Pipecat voice runs behind an explicit microphone permissions policy so the microphone cannot be activated silently or by embedded content, which SUPPORTS restrictions on collaborative computing devices. | SP 800-53 rev 5, SC-15 |

**Overlay note:** The NIST COSAiS project (SP 800-53 Control Overlays for Securing AI Systems, concept paper released August 2025 at csrc.nist.gov/projects/cosais) names five use cases, and two of them, single agent AI systems and multi agent AI systems, describe exactly this stack: systems that plan, reason, and execute tasks with limited human supervision. Based on the concept paper, the January 2026 predictive AI annotated outline, and where AI specific findings concentrate, expect the agentic overlays to modify these families most: AC (least privilege and access enforcement for autonomous actions, information flow between agents), IA (machine and agent identity, especially IA-9 service identification and authentication between agents and tool servers), AU (logging content and retention for model and tool interactions), SC (boundary protection, process isolation, resource limits against runaway agents), SI (input validation and monitoring reframed around prompt injection and data poisoning), CM (least functionality of tool surfaces and model configurations), plus SA and SR for external model services and AI supply chain provenance, with RA and CA tailored for AI specific risk assessment and continuous monitoring of nondeterministic behavior. Status caveat as of mid 2026: only the predictive AI annotated outline had published as a discussion draft; the single agent and multi agent overlays were still in development with drafts expected late 2026 to 2027, so treat this family emphasis as directional until NIST publishes them. Tools in this stack SUPPORT these controls; an assessor decides satisfaction.

## The honest gap register

Every gap below is stated so the pilot and roadmap can close it, and so no assessor finds it before we say it.

- **L1:** One self managed Linux server is a single point of failure with no documented contingency baseline (SP 800-53 rev 5 CP-2, CP-9); GOVERN 6.2 is only half met by local model fallback.
- **L1:** The allowlist screens provider origin but there is no per model version risk assessment or model card review before a new allowed model is adopted (AI 100-1 MAP 4.1; AI 600-1 MG-3.1-005).
- **L1:** No documented supplier risk assessment framework behind the allowlist decisions (AI 600-1 GV-6.1-005); the list exists, the vetting evidence trail does not.
- **L2:** No poisoning assessment of the RAG index; a hostile document that reaches Docling flows into Qdrant unmeasured (AI 600-1 MS-2.7-001 names data poisoning and compromised dependencies).
- **L2:** No PII minimization or anonymization pass on stored memories (AI 600-1 MS-2.2-002, MS-2.2-004); the boundary protects against exfiltration, not against over retention inside it.
- **L2:** No documented retention and deletion policy for memories and vectors at decommissioning time (AI 600-1 GV-1.7-002).
- **L3:** Playwright browses untrusted web content and there is no measured indirect prompt injection result for the browse then act loop; the LLM Guard defense sits at L6 but no red team numbers exist at this layer (AI 600-1 MS-2.7-007).
- **L3:** No per tool least privilege audit proving each MCP server runs with minimum scopes (SP 800-53 rev 5 AC-6); typed schemas define shape, not privilege.
- **L3:** Sandbox escape is assumed away rather than tested; no adversarial evaluation of the gVisor boundary itself (AI 100-1 MEASURE 2.7 asks for evaluation, not just deployment).
- **L4:** The claim protocol has no cryptographic identity; any process with filesystem access can claim or release work, so GOVERN 2.1 attribution is spoofable (SP 800-53 rev 5 IA family).
- **L4:** No documented go or no go determination per workflow before it is allowed to run in production (AI 100-1 MANAGE 1.1).
- **L4:** Emergent multi agent failure modes (retry storms, deadlocks between claimed tickets) are not measured anywhere; this is precisely the territory the forthcoming COSAiS multi agent overlay targets.
- **L5:** The eval suite measures correctness style metrics; fairness and bias (AI 100-1 MEASURE 2.11) and privacy red teaming (AI 600-1 MS-2.10-001) are not in it.
- **L5:** No regular adversarial testing cadence against the deployed system (AI 600-1 MS-4.2-001); traces observe, they do not attack.
- **L5:** Healthchecks.io is itself an external SaaS single point for the dead man signal, and nothing watches the watcher.
- **L6:** Guardrail and injection defense effectiveness is asserted, not measured; no bypass rate numbers from red teaming (AI 600-1 MS-2.7-007 asks for the exercise, not just the shield).
- **L6:** Budget enforcement measures gateway side spend; server side reconciliation against provider reported usage is not closed, so a bypassed gateway is unbounded.
- **L6:** No incident disclosure or after action review procedure for guardrail failures (AI 600-1 GV-1.5-002, MG-4.3-001), and no whistleblower path (GV-2.1-005).
- **L6:** Deactivation criteria live in policy code but there is no documented periodic review cadence for them, which is the second half of MG-2.4-004.
- **L7:** Automation bias and over reliance (AI 600-1 Sec. 2.7 Human-AI Configuration) are not measured; the approval dock could become a rubber stamp and nothing would detect it (AI 600-1 MS-4.2-004 monitors override patterns).
- **L7:** No user feedback and recourse mechanism with instructions (AI 600-1 GV-3.2-004; AI 100-1 MEASURE 3.3).
- **L7:** Accessibility is a stated goal, not yet a measured conformance result per surface; no WCAG numbers attached to the chat, dock, or voice interfaces.
- **L7:** Voice raises anthropomorphization risk that the profile says to track in interfaces (AI 600-1 MS-2.5-004) and nothing tracks it.
- **L1:** One self managed Linux server is a single point of failure; no alternate processing site or tested reconstitution is evidenced, so CP-7 and CP-10 are open at this layer.
- **L1:** No evidenced hash or signature verification of downloaded llama.cpp model weights, leaving SI-7 integrity checking and SR-4 provenance open.
- **L1:** Allowlist support only holds if every agent is forced through the gateway; any direct provider network path bypasses the SC-7 support claimed above.
- **L2:** No evidence of encryption at rest for Qdrant, SQLite, or Mem0, so SC-28 is open.
- **L2:** No RAG corpus provenance tracking or poisoning detection; NIST AI 600-1 sec. 2 lists information integrity and data privacy as GAI risks that land directly on this retrieval layer.
- **L2:** No tested backup and restore for vectors, memory, and state, so CP-9 is open.
- **L3:** Playwright browser automation ingests untrusted web content, the classic indirect prompt injection path; NIST AI 600-1 sec. 2 names information security (including prompt injection) as a GAI risk, and defense here depends entirely on the L6 screens.
- **L3:** No mutual authentication or signing between agents and MCP tool servers is evidenced, so IA-9 service identification and authentication is open.
- **L3:** Sandbox escape and covert egress from the sandboxed runtime are not independently monitored at this layer.
- **L4:** The file based coordination floor has no integrity protection or authentication; any process with file access can forge claims or move tickets, leaving AU-9 style protection of coordination records and IA-9 open.
- **L4:** Dagu scheduled jobs and workflow workers appear to share one machine identity, so per agent accountability blurs at the OS level.
- **L4:** No watchdog policy for runaway autonomous loops beyond the L6 budget caps.
- **L5:** Traces hold raw prompts and outputs, so the Langfuse store itself needs access control and protection of audit information; AU-9 is open, and NIST AI 600-1 sec. 2 flags data privacy risk in exactly this kind of store.
- **L5:** Evaluation gates measure quality and behavior regressions, not security; there is no adversarial testing or red team cadence, so CA-8 is open.
- **L5:** Alerts terminate at a dead man switch rather than a monitored incident response process, so IR-4 and IR-6 are open.
- **L6:** Every control here is in the request path only if agents cannot reach providers or tools directly; a raw network path around the gateway and the OPA gate defeats the whole layer, so SC-7 completeness must be verified, not assumed.
- **L6:** Named approvals are recorded but not cryptographically signed, so AU-10 non-repudiation is weak.
- **L6:** The guardrail stack itself is never adversarially tested on a schedule; CA-8 is open, and AI 600-1 suggested actions call for structured adversarial testing of GAI defenses.
- **L7:** The chat surface is itself an untrusted input channel; pasted or dictated content can carry injected instructions, and only the upstream L6 screens defend it, a Human-AI Configuration risk in NIST AI 600-1 sec. 2.
- **L7:** No session lock or re-authentication before approvals is evidenced, so AC-11 and AC-12 are open, which matters when one click in the dock executes a real action.
- **L7:** The voice path has no speaker verification, so spoken commands are weakly authenticated and IA-2 is open for that channel.
- **L7:** Accessibility as North Star is a Section 508 and WCAG obligation, not an SP 800-53 security control; it maps to AI RMF human factors guidance rather than any rev 5 family, so do not claim a control for it.

## Verifier notes (claims the fact check pass changed or could not confirm)

- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** L1 GOVERN 6.1 'how': the LiteLLM allowlist 'is exactly an approved provider list for third party GAI technology' -> SATISFIES-claim; downgrade to supports. GV-6.1-007 has two halves ,  inventory all third-party entities with access to organizational content AND the approved list ,  and the parent subcategory requires policies and proc
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** L2 MEASURE 2.10 'how': data staying in-boundary 'is the examined and documented privacy posture MEASURE 2.10 asks for' -> SATISFIES-claim; downgrade to supports. MEASURE 2.10 requires privacy risk to be 'examined and documented.' An architecture that keeps data inside a boundary is a control, not an examination or documentation of privacy r
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** MS-2.5-005 exists and concerns verifying retrieval-augmented generation data is grounded (L2, MEASURE 2.5 citation) -> ID is real and text close: 'Verify GAI system training data and TEVV data provenance, and that fine-tuning or retrieval-augmented generation data is grounded.' But the mapping inverts it into a satisfies-claim: the actio
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** L2 gap citation: 'AI 600-1 MS-2.7-001 names data poisoning and compromised dependencies' -> MS-2.7-001 names compromised dependencies but NOT data poisoning. Data poisoning appears in Section 2.9 Information Security, in MS-2.7-007's ML-attack list, and in MG-3.1-002. Minor mis-attribution; the gap's substance 
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** L4 GOVERN 2.1 'how': the file-based ticket board and claim protocol 'documents roles, responsibilities, and lines of communication' -> Subcategory is real (verified in both documents), but this is a satisfies-shaped stretch: GOVERN 2.1 concerns documented organizational roles and lines of communication for mapping, measuring, and managing AI risks ,  ta
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** GV-1.3-002 exists and covers minimum thresholds as part of go/no-go deployment approval (L5, GOVERN 1.3 citation) -> ID and text confirmed: 'Establish minimum thresholds for performance or assurance criteria and review as part of deployment approval (go/no-go) policies, procedures, and processes...' But the how-text claims the DeepEval
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** MG-2.4-004 exists and covers establishing and regularly reviewing specific criteria warranting deactivation (L6, MANAGE 2.4 citation) -> ID confirmed: 'Establish and regularly review specific criteria that warrants the deactivation of GAI systems in accordance with set risk tolerances and appetites.' But the how-text claims OPA + budget caps 'together for
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** L7 MEASURE 2.11 mapping: accessibility-as-North-Star cited to MEASURE 2.11 and GV-3.2-002 ('increased accessibility of GAI tools, interfaces, and systems') -> Both IDs are real and the quoted phrase appears verbatim inside GV-3.2-002 ,  but as one bullet in a list about adjusting organizational roles across lifecycle stages, not a standalone accessibility action. More importan
- **[corrected] NIST AI RMF 1.0 + Generative AI Profile:** Satisfies-vs-supports sweep across all 24 mappings (task item 2) -> Seven mappings cross from supports into satisfies-language and should be softened: L1 GOVERN 6.1 ('is exactly an approved provider list'), L2 MEASURE 2.10 ('is the examined and documented privacy posture'), L2 MEASURE 2.
- **[unverifiable] SP 800-53 rev 5 control families:** COSAiS overlay note: single-agent and multi-agent overlay drafts 'expected late 2026 to 2027' and family-emphasis prediction (AC, IA, AU, SC, SI, CM, SA/SR, RA/ -> No NIST-published schedule confirms the late-2026-to-2027 window for the agent overlays specifically. NIST's stated intent was initial public drafts of NISTIR 8605 volumes by Q3 FY2026 (April-June 2026), with additional 
- **[corrected] SP 800-53 rev 5 control families:** L7 gap cites AC-11 and AC-12 for 'no session lock or re-authentication before approvals' -> Minor title/scope drift, not an invented ID: in rev 5 AC-11 is titled 'Device Lock' ('Session Lock' is the rev 4 name) and AC-12 is 'Session Termination'; re-authentication before high-impact approvals is IA-11 'Re-authe
