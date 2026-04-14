# AFS04 — Research Pack

## Azure AI Foundry RBAC Role Detail

| Role | Scope | Data Plane | Control Plane | Access Mgmt | Risk Level |
|------|-------|------------|---------------|-------------|------------|
| Azure AI User | Project | Yes | No | No | LOW |
| Azure AI Project Manager | Project | Yes | Limited | Yes (project) | MEDIUM |
| Azure AI Account Owner | Hub/Account | No | Yes | Limited | MEDIUM |
| Azure AI Owner | Hub + Project | Yes | Yes | Yes (full) | HIGH |

### Granular Permissions Breakdown

**Azure AI User**

- `Microsoft.CognitiveServices/accounts/deployments/read`
- `Microsoft.CognitiveServices/accounts/deployments/inference/action`
- `Microsoft.MachineLearningServices/workspaces/data/read`
- `Microsoft.MachineLearningServices/workspaces/experiments/read`
- Cannot: create resources, manage access, deploy models

**Azure AI Account Owner**

- `Microsoft.MachineLearningServices/workspaces/write`
- `Microsoft.CognitiveServices/accounts/deployments/write`
- `Microsoft.MachineLearningServices/workspaces/connections/write`
- Cannot: `*/dataActions/*` (no inference, no data reads)

**Azure AI Owner**

- All actions from both User and Account Owner
- `Microsoft.Authorization/roleAssignments/write`
- Full `dataActions` and `actions` across all scopes

## API Key vs Managed Identity Comparison

| Attribute | API Key | Managed Identity |
|-----------|---------|-----------------|
| Auth mechanism | Shared secret | Entra ID token |
| Per-user audit | No | Yes |
| RBAC enforcement | Bypassed | Enforced |
| Conditional access | Not supported | Supported |
| Secret rotation | Manual | Automatic |
| Scope control | All-or-nothing | Role-based |
| Lifecycle mgmt | Manual revocation | Tied to resource or managed centrally |
| Compliance posture | Weak | Strong |

## Managed Identity Scopes in Foundry

### Hub-level (System-assigned)

- Applies to the Foundry hub resource itself
- Used for hub-to-hub or hub-to-dependency connections
- Auto-created when enabled on the hub resource
- Deleted when the hub is deleted

### Project-level (User-assigned recommended)

- Shareable across multiple projects
- Centrally managed in Entra ID
- Survives project deletion if needed
- Can be pre-provisioned by platform team

### Service-to-service

- Foundry resources accessing Key Vault, Storage, AI Services
- Managed identity eliminates connection string secrets
- Role assignments grant specific access per dependency

## Custom Role Example

```json
{
  "Name": "AI Inference Only",
  "Description": "Can call deployed models but cannot deploy, delete, or manage access.",
  "Actions": [],
  "NotActions": [],
  "DataActions": [
    "Microsoft.CognitiveServices/accounts/deployments/inference/action",
    "Microsoft.CognitiveServices/accounts/deployments/read"
  ],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/{sub-id}/resourceGroups/{rg}/providers/Microsoft.MachineLearningServices/workspaces/{hub}"
  ]
}
```

## Security Incident Patterns

### Pattern: Leaked API Key

1. Developer copies API key from Azure Portal
2. Key stored in `.env` or `appsettings.json`
3. File committed to Git (even if later removed, key is in history)
4. Key grants full data plane access — inference, data reads, prompt history
5. No per-user audit trail — impossible to attribute actions
6. Remediation: regenerate key, audit all actions since creation

### Pattern: Over-privileged Role Assignment

1. Platform team assigns Owner to unblock dev team quickly
2. Developer accidentally deletes shared deployment or modifies hub config
3. No guardrails — Owner role permits all actions
4. Remediation: downgrade to User, create custom role if needed

### Pattern: Correct Deployment

1. Platform team provisions hub with system-assigned managed identity
2. Developers get Azure AI User role at project scope
3. Team leads get Project Manager role
4. API keys disabled at hub level via policy
5. Conditional access enforces MFA, device compliance
6. Custom "AI Inference Only" role for CI/CD service principals

## Source References

- Azure AI Foundry RBAC built-in roles documentation
- Microsoft Entra ID managed identity overview
- Azure RBAC custom role definitions for Cognitive Services
- Azure Policy definitions for disabling key-based auth
- Microsoft Learn: Secure Azure AI services with managed identities
