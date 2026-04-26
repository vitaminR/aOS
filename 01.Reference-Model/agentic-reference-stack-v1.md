# CANONICAL FRAMEWORK

# Agentic Reference Stack v1.0

# Locked vocabulary: Stratum / Axis / Substrate / Construct / Primitive

> **Version:** v1.0
> **Date:** 2026-04-07
> **Status:** Canonical — locked vocabulary, strata, and axes
> **Supersedes:** {a}OS-6L v0.1 (layer-definitions.md)

## 1.0 CORE TERMS

1.1 Stratum
A top-level layer in the stack.
Purpose: define a stable responsibility boundary.

1.2 Axis
A cross-cutting concern that intersects multiple strata.
Purpose: measure, constrain, or govern behavior across the stack.

1.3 Substrate
The tools, frameworks, runtimes, or systems operating within a stratum.

1.4 Construct
A meaningful artifact, state, or object produced by a substrate.

1.5 Primitive
The smallest atomic unit used inside a construct.

1.6 Optional Deployment Term
Stratum 0 / Sovereignty
A pre-stack deployment constraint used only when residency, air-gap, tenancy, classification, or ownership materially change the system design.

---

## 2.0 DESIGN RULES

2.1 Stratum Count Rule
Use 7 canonical strata.

2.2 Product Placement Rule
Products do not live in only one place.
Every product gets:

- primary stratum
- secondary strata
- axis roles if applicable

2.3 Incident Tagging Rule
Every incident gets:

- origin stratum
- impact stratum

2.4 Axis Rule
Axes are not extra strata.
They cut across the strata.

2.5 New Stratum Test
A new top-level stratum only earns existence if it changes all three:

- owner
- interface contract
- failure mode

If it does not change all three, it is a substrate, sublayer, or axis concern.

---

## 3.0 CORE AXES

3.1 Governance & Trust Axis
What it does:

- identity
- access control
- policy
- safety
- approvals
- budget boundaries
- auditability
- compliance

Touches:

- strongest home: L6 Governance & Trust
- affects all strata

Typical metrics:

- unauthorized action attempts
- approval latency
- policy denial rate
- budget variance
- compliance pass rate

3.2 Observability & Evaluation Axis
What it does:

- tracing
- logging
- metrics
- evals
- drift detection
- incident visibility
- performance measurement
- cost visibility

Touches:

- strongest home: L5 Observability & Evaluation
- affects all strata

Typical metrics:

- trace coverage
- p95/p99 latency
- eval pass rate
- hallucination/error rate
- cost per successful task

3.3 Secondary Optional Axes
Only formalize later if needed:

- Security Axis
- FinOps Axis
- Compliance Axis
- Privacy Axis

Recommendation:
Keep only the 2 core axes canonical for now:

- Governance & Trust
- Observability & Evaluation

---

## 4.0 THE 7 CANONICAL STRATA

### 4.1 L7 — Experience & Intent

Definition:
The human boundary where requests enter, responses render, and approvals happen.

Boundary question:
What is the user asking, seeing, approving, or rejecting?

Inputs:

- prompt
- file upload
- API request
- approval action
- user context

Outputs:

- normalized task request
- rendered response
- approval decision
- user-visible status
- escalated clarification request

Substrates:

- chat UI
- portal
- CLI
- dashboard
- approval surface
- API gateway

Constructs:

- user session
- task request
- approval request
- rendered response
- scoped work item

Primitives:

- user_id
- session_id
- message_text
- file_handle
- role_string
- approval_bool

Typical failures:

- wrong intent captured
- ambiguous user instruction
- poor UX causes misuse
- approval action not recorded
- response rendered without context

Core metrics:

- task completion rate
- time to first response
- approval completion rate
- user drop-off rate
- correction rate

### 4.2 L6 — Governance & Trust

Definition:
The policy boundary where access, safety, approval, budget, and compliance are enforced.

Boundary question:
Who is allowed to do this, under what policy, with what risk and budget?

Inputs:

- user identity
- policy rules
- safety signals
- budget policies
- approval policies
- data classification

Outputs:

- access decision
- policy decision
- trust envelope
- audit event
- safety verdict
- budget permit/deny

Substrates:

- IAM / RBAC
- policy engine
- content safety
- secrets manager
- key manager
- budget guardrails
- approval workflows

Constructs:

- access token
- policy decision
- trust envelope
- audit trail
- safety verdict
- budget envelope

Primitives:

- scope
- allow_deny_flag
- policy_rule
- secret_ref
- risk_score
- budget_threshold
- classification_tag

Typical failures:

- unauthorized tool access
- over-permissive policy
- missing audit evidence
- secret exposure
- budget runaway
- unsafe content not blocked

Core metrics:

- policy violation rate
- unauthorized attempt count
- audit completeness
- budget variance
- approval latency
- safety block accuracy

### 4.3 L5 — Observability & Evaluation

Definition:
The proof boundary where execution becomes visible, measurable, and judged.

Boundary question:
What actually happened, how well did it perform, and where did it fail?

Inputs:

- traces
- logs
- metrics
- outputs
- ground truth / eval data
- cost telemetry

Outputs:

- trace graph
- scorecard
- alert
- regression report
- drift warning
- incident record

Substrates:

- distributed tracing
- logging pipeline
- metrics store
- eval harness
- dashboard
- alerting system
- drift monitor

Constructs:

- trace graph
- eval scorecard
- alert object
- cost curve
- regression report
- incident record

Primitives:

- timestamp
- trace_id
- span_id
- metric_point
- severity
- token_count
- score_float

Typical failures:

- silent failure with no trace
- eval blind spot
- cost spike unseen
- bad alert thresholds
- drift not detected
- success measured incorrectly

Core metrics:

- trace coverage
- p95 / p99 latency
- eval pass rate
- false positive alert rate
- drift detection lag
- cost per successful task

### 4.4 L4 — Orchestration & Decisioning

Definition:
The control boundary where work is routed, sequenced, delegated, retried, and stopped.

Boundary question:
What happens next, in what order, with which agent, under which stop conditions?

Inputs:

- normalized task
- current state
- policy constraints
- memory references
- tool results
- retry state

Outputs:

- execution plan
- handoff
- routing decision
- stop condition
- retry action
- escalated branch

Substrates:

- workflow engine
- router
- state machine
- planner
- handoff manager
- queue
- retry logic
- circuit breaker

Constructs:

- execution graph
- plan
- routing table
- session state
- handoff packet
- stop condition

Primitives:

- node_id
- edge
- task_id
- state_key
- retry_count
- timeout_value
- branch_flag

Typical failures:

- infinite loop
- wrong specialist selected
- retry storm
- broken stop condition
- dead branch
- state corruption

Core metrics:

- task success rate
- average steps per task
- loop rate
- retry rate
- handoff success rate
- orchestration latency

### 4.5 L3 — Execution & Interfaces

Definition:
The action boundary where external tools, APIs, scripts, and sandboxes are invoked.

Boundary question:
What external action was invoked, against which interface, and what happened?

Inputs:

- tool call request
- payload
- auth context
- execution policy
- job parameters

Outputs:

- API response
- script result
- job result
- file change
- side effect
- execution log

Substrates:

- tool gateway
- function-calling adapter
- MCP server
- API connector
- sandbox
- job runner
- script executor
- microVM / container task

Constructs:

- tool call
- payload
- job run
- connector response
- executed script
- microVM task

Primitives:

- endpoint_url
- method
- function_name
- arg_field
- exit_code
- file_path
- process_id

Typical failures:

- malformed payload
- auth mismatch
- wrong tool executed
- destructive script run
- sandbox escape risk
- connector timeout

Core metrics:

- tool success rate
- interface latency
- side-effect accuracy
- sandbox failure rate
- connector coverage
- execution rollback rate

### 4.6 L2 — Knowledge & Memory

Definition:
The context boundary where facts, documents, semantic relationships, and memory are stored and retrieved.

Boundary question:
What context did the system know, retrieve, remember, or forget?

Inputs:

- documents
- embeddings
- transcripts
- entity relations
- prior memory
- query context

Outputs:

- retrieved chunks
- memory object
- semantic thread
- citation set
- entity graph
- context bundle

Substrates:

- vector store
- graph store
- document index
- memory store
- transcript store
- RAG pipeline

Constructs:

- embedding set
- chunk set
- memory object
- semantic thread
- citation set
- entity graph

Primitives:

- float_value
- document_id
- chunk_id
- entity_id
- memory_key
- embedding_dimension

Typical failures:

- wrong retrieval
- stale context
- forgotten session detail
- duplicate memory
- low-quality chunking
- bad entity resolution

Core metrics:

- retrieval precision
- retrieval recall
- citation coverage
- memory hit rate
- stale context rate
- rerank lift

### 4.7 L1 — Models & Infrastructure

Definition:
The foundation boundary where models, runtimes, compute, storage, and network resources actually operate.

Boundary question:
Is the model/runtime/compute/network foundation available and behaving correctly?

Inputs:

- inference request
- runtime config
- model deployment
- network path
- resource allocation
- storage access

Outputs:

- model response
- token stream
- embedding output
- runtime allocation
- packet flow
- infrastructure event

Substrates:

- model endpoint
- inference runtime
- container runtime
- GPU / CPU
- scheduler
- storage
- network fabric
- service mesh

Constructs:

- model response
- token stream
- embedding output
- container
- packet flow
- runtime allocation

Primitives:

- token
- byte
- packet
- request_id
- ip_address
- port
- gpu_second

Typical failures:

- model unavailable
- cold start / scaling lag
- network segmentation issue
- GPU exhaustion
- endpoint timeout
- bad model deployment

Core metrics:

- availability
- model latency
- tokens per second
- error rate
- infrastructure utilization
- cost per call

---

## 5.0 OPTIONAL S0

### 5.1 S0 — Sovereignty & Deployment Constraints

Definition:
A deployment precondition for environments where physical, legal, tenancy, residency, or air-gap constraints materially shape the architecture.

Boundary question:
Where may this system legally and physically exist?

Inputs:

- region policy
- data residency requirement
- tenancy model
- clearance requirement
- export control

Outputs:

- deployment boundary
- residency policy
- trust zone
- hosting attestation

Substrates:

- residency controls
- tenancy controls
- enclave / air-gap boundary
- sovereign hosting controls

Constructs:

- trust zone
- residency envelope
- deployment boundary
- hosting attestation

Primitives:

- region_code
- tenant_id
- enclave_id
- classification_tag
- sovereignty_flag

Use rule:
Do not make S0 part of the default public 7 unless sovereignty is central to the story.

---

## 6.0 STANDARD PRODUCT CLASSIFICATION TEMPLATE

6.1 Product Record

- name
- vendor
- category
- open_source_bool
- deployment_modes
- last_verified_date

6.2 Placement Record

- primary_stratum
- secondary_strata[]
- axis_roles[]
- rationale
- evidence
- confidence_score

6.3 Capability Record

- capability_name
- mapped_stratum
- role_type: primary | secondary | cross-cutting
- rationale
- evidence
- confidence_score

6.4 Operational Metadata

- ideal_use_case
- maturity
- lock_in_risk
- governance_risk
- common_failure_modes
- overlap_risk

---

## 7.0 INCIDENT CLASSIFICATION TEMPLATE

- incident_name
- origin_stratum
- impact_stratum
- affected_axes[]
- trigger
- observed_symptom
- root_cause
- containment_action
- remediation_action

Example:
Hallucinated destructive script

- origin_stratum: L4
- impact_stratum: L3
- affected_axes: Governance & Trust, Observability & Evaluation

---

## 8.0 SAMPLE PRODUCT MAPPINGS

### 8.1 Kotana

Primary stratum:

- L1 Models & Infrastructure

Secondary strata:

- L2 Knowledge & Memory
- L3 Execution & Interfaces
- L4 Orchestration & Decisioning

Possible axis roles:

- Observability & Evaluation if it exposes traces/metrics
- Governance & Trust if it enforces policy or routing constraints

Why:

- local / hybrid model access
- persistent memory
- tool use
- multi-agent orchestration

### 8.2 Paperclip

Primary stratum:

- L4 Orchestration & Decisioning

Secondary strata:

- L6 Governance & Trust
- L5 Observability & Evaluation

Why:

- hierarchical coordination
- task routing
- status / heartbeat semantics
- budgets / control semantics

### 8.3 NemoClaw / OpenShell

Primary stratum:

- L3 Execution & Interfaces

Secondary strata:

- L6 Governance & Trust
- L1 Models & Infrastructure

Why:

- sandboxed execution
- policy enforcement
- runtime isolation
- script / shell action boundary

---

## 9.0 WEBSITE / PRODUCT MODEL DIRECTIONS

### 9.1 Core Browsing Modes

- browse by Stratum
- browse by Axis
- browse by Product
- compare products

### 9.2 Minimum Viable Views

- stack view
- product profile
- compare view

### 9.3 Every product page should show

- primary stratum
- secondary strata
- axis roles
- capabilities
- rationale
- evidence
- confidence
- overlap / dispute notes

---

## 10.0 LOCKED CANONICAL REFERENCE

10.1 Strata

- L7 Experience & Intent
- L6 Governance & Trust
- L5 Observability & Evaluation
- L4 Orchestration & Decisioning
- L3 Execution & Interfaces
- L2 Knowledge & Memory
- L1 Models & Infrastructure

10.2 Axes

- Governance & Trust Axis
- Observability & Evaluation Axis

10.3 Vocabulary

- Stratum
- Axis
- Substrate
- Construct
- Primitive

10.4 Optional

- S0 Sovereignty & Deployment Constraints

---

## 11.0 ONE-LINE MEMORY VERSION

L7 Experience & Intent:
What the human asks, sees, and approves.

L6 Governance & Trust:
What is allowed, safe, compliant, and budgeted.

L5 Observability & Evaluation:
What happened, how it performed, and how we know.

L4 Orchestration & Decisioning:
What happens next, by whom, and in what order.

L3 Execution & Interfaces:
What external action was actually taken.

L2 Knowledge & Memory:
What context the system knew, retrieved, or forgot.

L1 Models & Infrastructure:
What compute, runtime, model, and network foundation made it all possible.
