# AFS08 — Research Notes

## The Default Storage Problem

Azure AI Foundry offers two storage tiers for agent data:

**Basic (default):**

- Microsoft-managed multitenant storage
- Zero customer visibility into underlying storage accounts
- No customer-managed encryption keys
- No private endpoints on the storage layer
- Documents uploaded for RAG, agent thread history, and intermediate artifacts all live here
- Fastest path to "hello world" — which is why teams end up here

**Standard (opt-in):**

- Customer provides their own Azure Storage account
- Customer-managed keys (CMK) for encryption at rest
- Private endpoint support — storage stays inside the customer's VNet
- Full lifecycle control: retention, access policies, key rotation, diagnostic logging
- Visible in the customer's Azure subscription — auditable, manageable

The critical detail: this choice is made at Foundry resource provisioning time. Teams that start with Basic and later discover they need Standard face a reprovisioning exercise, not a configuration change.

## The Environment Boundary Trap

Projects within Azure AI Foundry are organizational containers — they let teams group agents, data, and deployments. But projects within the same Foundry resource share:

- Parent networking configuration (VNet, private endpoints, NSGs)
- Parent storage configuration (Basic or Standard)
- Parent identity and access boundary

This means: a "dev" project and a "prod" project in the same Foundry resource share the same blast radius. A network misconfiguration in dev affects prod. A storage access policy change applies to both.

**Correct pattern:** One Foundry resource per environment. Dev Foundry, staging Foundry, production Foundry. Each gets its own:

- Network boundary
- Storage tier and configuration
- Identity assignments
- Access policies

This is the pattern enterprise teams discover after their first security review, not before.

## RAG Architecture in Foundry

Three RAG paths exist in Foundry:

1. **Azure AI Search (GA)** — Production-ready. Supports private endpoints. Customer manages the index, schema, and data lifecycle. This is what you should build on.

2. **Document Intelligence (GA)** — Document processing (PDF extraction, OCR, form recognition, layout). Feeds into AI Search. Production-ready.

3. **Foundry IQ (Preview)** — Microsoft-managed enterprise RAG pipeline. Handles ingestion, chunking, indexing automatically. Convenient. Also preview, which means: no SLA, may change without notice, not recommended for production workloads in regulated environments.

The temptation: Foundry IQ is much easier to set up than the AI Search + Document Intelligence pipeline. Teams building POCs gravitate toward it. Then the POC becomes "production" and nobody reassesses the preview dependency.

## Defense / Healthcare / Finance Callout

For these industries, the storage question is not "nice to have":

- **Defense (CMMC/NIST 800-171):** CUI must be stored in customer-controlled infrastructure with auditable key management. Basic storage cannot satisfy this.
- **Healthcare (HIPAA):** PHI requires BAA-covered storage with customer-managed access controls. Microsoft-managed multitenant storage introduces audit complexity.
- **Finance (SOX/PCI-DSS/GLBA):** Financial records require documented data lineage and customer-managed encryption. Basic storage provides neither.

The pattern: teams in these industries build the POC on Basic (because it's fast), then discover during security review that they need Standard, then discover that migration is not a toggle.

## File Search VNet Limitation

From AFS05 research: the File Search agent tool does NOT work in VNet-isolated Foundry deployments. This matters for RAG because File Search is one of the easiest paths to document retrieval in agents. Teams that enforce network isolation (which regulated industries must) lose this tool and must build the AI Search integration path instead.

## What Teams Should Do

1. Decide Basic vs Standard at project inception, not after first deployment
2. If handling any sensitive data category, choose Standard
3. Use separate Foundry resources per environment — projects are not isolation boundaries
4. Build RAG on AI Search + Document Intelligence (GA), not Foundry IQ (preview)
5. If enforcing VNet isolation, plan for AI Search integration — File Search won't work
