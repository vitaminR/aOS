# 6.aOS — Governance

## Versioning

- Reference model uses semantic versioning: v{major}.{minor}
- Current version: **v1.0** (locked)
- Breaking layer changes increment major version
- Layer detail additions increment minor version
- Every version increment must update the AI RMF crosswalk if strata definitions changed

## License

See [`LICENSE.md`](../LICENSE.md) for the dual-license structure:

- **CC BY 4.0** — Reference model, governance, and research materials
- **Apache 2.0** — Explorer software (`90.aOS-Explorer/`)
- **Atlas Addendum** — [`ATLAS_LICENSE_ADDENDUM.md`](ATLAS_LICENSE_ADDENDUM.md)

## Standards Track

The standardization roadmap is maintained at [`standardization-pack/ROADMAP.md`](standardization-pack/ROADMAP.md).

- Neutral standards-track title: **Agentic Systems — Reference Model and Vocabulary**
- Current status: **Phase 0 complete — Phase 1 in preparation**
- End-to-end submission checklist: [`standardization-pack/CHECKLIST.md`](standardization-pack/CHECKLIST.md)

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

- Every vendor mapping must cover all 7 strata
- Every vendor mapping must include a "Gaps" section per stratum
- Research briefs must include a "Marketing vs. Reality" section
- LinkedIn series plans must include post dependencies
- Every version increment must update the AI RMF crosswalk if strata definitions changed
