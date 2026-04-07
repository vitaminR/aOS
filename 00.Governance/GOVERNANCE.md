# 6.aOS — Governance

## Versioning

- Reference model uses semantic versioning: v{major}.{minor}
- Current version: **v0.1** (pre-release)
- Breaking layer changes increment major version
- Layer detail additions increment minor version

## Contribution Rules

- Layer definitions live in `01.Reference-Model/layer-definitions.md`
- Vendor mappings live in `02.Vendor-Mappings/{vendor-name}.md`
- Research briefs live in `03.Research/`
- LinkedIn series plans live in `04.LinkedIn-Series/`
- Architecture patterns live in `05.Architecture/`
- Never modify layer names without updating all vendor mappings
- All content is GitHub-flavored Markdown
- Use absolute paths when referencing other workspace files

## Quality Gates

- Every vendor mapping must cover all 6 layers
- Every vendor mapping must include a "Gaps" section per layer
- Research briefs must include a "Marketing vs. Reality" section
- LinkedIn series plans must include post dependencies
