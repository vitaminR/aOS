# AFS08 — Research Pack: RAG and the Data Residency Question Nobody Asked

## Core Thesis

Azure AI Foundry defaults to "Basic" agent storage — Microsoft-managed, multitenant, opaque. Most teams never change this. For regulated industries (defense, healthcare, finance), this is a compliance failure waiting to happen. "Standard" storage with BYO accounts, customer-managed keys, and private endpoints exists, but requires deliberate selection before first deployment. Additionally, Foundry projects share parent networking, making them unsuitable as environment boundaries.

## Key Facts

### Basic vs Standard Agent Storage

- **Basic storage** = Microsoft-managed multitenant. Default on new Foundry resources. Documents uploaded for RAG, agent artifacts, and intermediate data sit in storage Microsoft controls. No customer-managed encryption keys. No private endpoints on the storage layer. Easiest setup path.
- **Standard storage** = BYO (Bring Your Own) storage account. Customer-managed encryption keys (CMK). Private endpoints available. Storage account visible in customer's Azure subscription. Customer controls lifecycle, access policies, and key rotation.
- The choice is made at Foundry resource creation time. Migrating from Basic to Standard after deployment is not a simple toggle — it requires reprovisioning.

### Environment Separation

- Projects within a single Azure AI Foundry resource share the parent resource's networking configuration
- A "dev" project and a "prod" project in the same Foundry resource share the same network boundary
- Projects are NOT environment boundaries — they are organizational units within a shared infrastructure
- Recommended pattern: separate Foundry resources per environment (dev, staging, prod)
- Each Foundry resource gets its own networking, storage, and access configuration

### RAG & Document Processing

- **Azure AI Search** via private endpoint: supported, GA. This is the production-ready RAG backend.
- **Azure Document Intelligence** for document processing: GA. Handles PDF extraction, form recognition, layout analysis.
- **Foundry IQ** (enterprise RAG): preview. Microsoft-managed RAG pipeline. Not production-ready. Do not build critical document pipelines on preview services in regulated environments.
- File Search (agent tool): does NOT work in VNet-isolated environments (confirmed limitation from AFS05 research)

### Data Categories Requiring Standard Storage

- PII (Personally Identifiable Information) — GDPR, CCPA, state privacy laws
- PHI (Protected Health Information) — HIPAA
- Financial records — SOX, PCI-DSS, GLBA
- CUI (Controlled Unclassified Information) — NIST 800-171, CMMC
- Classified or export-controlled data — ITAR, EAR
- Any data subject to data residency requirements (EU Data Act, sovereignty regulations)

## Receipts

| # | Claim | Evidence |
|---|---|---|
| R1 | Basic storage is Microsoft-managed multitenant | Azure AI Foundry docs: "Basic" tier uses Microsoft-managed storage. Customer has no visibility into underlying storage account. |
| R2 | Standard storage supports CMK and private endpoints | Azure AI Foundry docs: "Standard" tier requires customer-provided storage account. Supports CMK, private endpoints, and customer-managed lifecycle. |
| R3 | Projects share parent networking | Azure AI Foundry architecture: projects inherit networking from parent resource. No per-project network isolation. |
| R4 | Foundry IQ is preview | Azure AI Foundry docs: Foundry IQ labeled "preview" as of April 2026. Preview services carry no SLA and are not recommended for production workloads. |
| R5 | AI Search via private endpoint is GA | Azure AI Search docs: private endpoint connectivity GA. Supported with Foundry integration. |
| R6 | Document Intelligence is GA | Azure Document Intelligence docs: GA for document processing, form recognition, layout analysis. |
| R7 | File Search breaks in VNet | Azure AI Foundry VNet limitations: File Search tool not supported in network-isolated deployments. |

## Anti-Patterns to Avoid in Post

- Don't make this a tutorial — the post reveals the problem and the decision point, not the step-by-step fix
- Don't imply Basic storage is "bad" — it's fine for non-sensitive workloads. The problem is defaulting to it without understanding the implications.
- Don't oversimplify the Basic-to-Standard migration — it's not a toggle
- Don't position Foundry IQ as broken — it's preview, which means "not ready for production," not "doesn't work"
- Don't skip the environment separation content — this absorbed the cut Post 11 and is critical
