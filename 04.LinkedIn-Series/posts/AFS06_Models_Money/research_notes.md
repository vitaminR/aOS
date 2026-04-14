# AFS06 — Research Notes

## Model Availability Reality

### The "11,000+ Models" Claim

Azure AI Foundry markets a catalog of 11,000+ models. The breakdown:

- **Azure-hosted (first-party and partner):** ~50-100 models that are deployed and managed by Azure
- **Marketplace/catalog models:** Thousands of open-source and third-party models available through the catalog, many requiring self-deployment or partner hosting
- **Production-relevant for enterprise:** The subset that has SLA, compliance documentation, and deployment support is dramatically smaller

The marketing number is technically accurate. The operational reality is a fraction of it.

### Deployment Types

**PTU (Provisioned Throughput Units):**

- Reserved capacity — you pay whether you use it or not
- Predictable latency and throughput guarantees
- Significant monthly commitment (enterprise pricing, not public)
- Decision often made by procurement/finance, not architecture
- Not available for all models or in all regions
- Required for production workloads that need latency guarantees

**Pay-as-you-go (Consumption):**

- Token-based pricing, pay for what you use
- No capacity reservation — shared infrastructure
- No latency guarantees — can experience throttling under load
- Lower barrier to entry, higher variance in production
- Available more broadly than PTU

**Global vs Regional Deployments:**

- Global deployments route to best available region — good for dev, problematic for data residency
- Regional deployments pin to a specific region — required for compliance but limits failover
- Data-zone deployments — newer option for geographic grouping

### Model Router

- Routes requests across model deployments for load balancing
- Poorly documented as of research date
- Not auditable — cannot trace which specific model instance handled a request
- Problematic for compliance environments that require model-level audit trails
- Not available in Gov cloud

## Government Cloud Constraints

### IL5 (Gov Community Cloud High)

- Model availability significantly reduced compared to commercial
- GPT-4.1: Available but with 300K context window (vs 1M in commercial)
- GPT-5.4: Not available
- Embeddings: Limited selection
- No batch deployments
- No Model Router
- PTU availability limited
- New Foundry resource model: not documented for Gov cloud as of research date

### IL6 (Gov Secret)

- Azure OpenAI service does not exist at IL6
- No model hosting, no inference endpoints
- Teams targeting IL6 must use alternative approaches (on-prem, disconnected)
- This is a hard architectural constraint, not a configuration issue

### Key Patterns

1. **Context window reduction:** Models available in Gov cloud often have reduced context windows. This breaks architectures designed around the commercial context limit.
2. **Deployment type gaps:** PTU availability is more limited in Gov cloud. Pay-as-you-go may be the only option.
3. **Feature lag:** Features that reach GA in commercial may remain in preview or unavailable in Gov cloud for months or longer.
4. **No batch:** Batch deployments (for offline processing workloads) are not available in Gov cloud. This affects cost optimization strategies.

## The Portability Principle

### Why Hardcoded Model Names Are Tech Debt

- Model availability changes. Models get deprecated, renamed, or region-restricted.
- A model available in US East today may not be available in US Gov Virginia tomorrow.
- Context window changes (as with GPT-4.1 commercial vs Gov) can break pipelines silently.
- PTU commitment to one model creates switching cost — architectural flexibility matters.

### Abstraction Layer Pattern

- Model name as configuration parameter, not code constant
- Prompt templates that adapt to context window limits
- Fallback chains: primary model -> secondary model -> degraded mode
- Test suite that validates against multiple models, not just the development model
- Cost model that accounts for deployment type differences

## Competitive Context (not for use in post — Azure-focused framing)

AWS Bedrock and Vertex AI have analogous constraints:

- Bedrock model availability varies by region, GovCloud has reduced selection
- Vertex AI model availability varies by region, no sovereign cloud equivalent
- All three platforms have the same pattern: marketing number >> operational availability

The principle is universal even though the post uses Azure-specific examples.

## Methodology for Checking Current State

Because model availability changes frequently, the post must teach methodology, not list static facts:

1. **Azure AI Foundry Model Catalog:** Filter by region and deployment type to see actual availability
2. **Azure Government documentation:** Sovereign cloud model lists are maintained separately
3. **Quota page:** A model being "available" in a region does not mean you have quota for it
4. **PTU pricing calculator:** Run cost models before procurement commits to a deployment type
5. **Release notes:** Subscribe to Azure AI updates for model availability changes

This methodology is the durable content. Specific model lists are not.
