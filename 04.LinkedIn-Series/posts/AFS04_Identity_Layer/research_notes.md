# AFS04 — Research Notes

## Key Findings

### Azure AI Foundry RBAC Roles

Four Foundry-specific built-in roles exist, distinct from generic Azure RBAC:

1. **Azure AI User** — Least privilege for developers. Grants data plane actions: call endpoints, run inference, read resources. Cannot create/delete resources or manage access. This is the intended developer default.

2. **Azure AI Project Manager** — Superset of User. Adds user management within project scope. Designed for team leads who need to grant/revoke access without platform team involvement.

3. **Azure AI Account Owner** — Control plane focused. Resource creation, model deployment, hub/project configuration. Notably does NOT include data plane actions by default. For platform/infra engineers.

4. **Azure AI Owner** — Full control across both planes. Data actions, control actions, access management. Should be restricted to platform admins with explicit justification.

### API Key Authentication Risks

- API keys bypass RBAC entirely — they authenticate at the service level, not the identity level
- No per-user audit trail when using shared API keys
- No conditional access policy enforcement
- No automatic rotation without manual configuration
- A single leaked key grants full data plane access regardless of any role assignments
- Keys do not expire by default in most configurations

### Managed Identity Benefits

- Works at both hub (resource) scope and project scope
- System-assigned: tied to resource lifecycle, auto-cleaned
- User-assigned: shareable across resources, managed centrally
- Integrates with Entra ID conditional access policies
- No secrets stored in code or config files
- Audit trail per identity principal

### Custom Roles

- Azure AI Foundry supports custom role definitions with granular `dataActions`
- Allows fine-grained control beyond the four built-in roles
- Recommended for production environments with specific compliance requirements
- Example: a role that can call inference but not deploy new models

## Patterns Observed

- Most quickstarts and tutorials default to API key auth for simplicity
- Teams that start with API keys rarely migrate to managed identities without a security incident
- "Owner" is the most over-assigned role because it "just works" during development
- The gap between Azure AI Account Owner (no data actions) and Azure AI Owner (everything) catches teams off guard

## Supporting Examples

- Common anti-pattern: API key in .env file committed to repo, shared across team via Slack
- Common anti-pattern: every developer assigned Owner role "to unblock development"
- Correct pattern: User role default + managed identity + custom roles for elevated scenarios
- Correct pattern: API keys disabled at hub level, Entra-only auth enforced via policy
