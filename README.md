# OncologyAI Registry

The public, curated registry of AI/ML-based **diagnostic, predictive, and prognostic** tools in U.S. oncology.
Regulatory status · clinical evidence · deployment signals — every entry sourced. CC BY 4.0.

> **v0.2 · 116 entries · structured validation summaries · launching mid-2026**

## Quick links
- 🌐 **Live site:** https://oncologyairegistry.org
- 📋 **[Methodology](v1/methodology.html)** — inclusion criteria, source hierarchy, validation-summary schema, conflict-of-interest disclosure
- ℹ️ **[About](v1/about.html)** — what the registry is and who maintains it
- 📊 **[Browse the registry](v1/index.html)**

## Why this exists

There is no single public, curated reference for AI-based diagnostic, predictive, and prognostic tools in U.S. oncology. Researchers, clinicians, regulators, payers, and journalists currently piece this landscape together manually — from FDA databases, individual press releases, and company sites. This produces inconsistent counts, out-of-date information, and no shared denominator for the field.

The OncologyAI Registry consolidates that information into one open-data resource with consistent inclusion criteria, structured validation summaries, and a quarterly refresh.

## What's in an entry

Each entry captures, where verifiable:
- **Regulatory status** — FDA pathway (510(k), De Novo, PMA, Breakthrough Device), LDT/RUO status, NY CLEP, CLIA/CAP, CE mark
- **Validation summary** — study design, cohort size, sites, comparator, primary endpoint + result, external validation, peer-reviewed publications, limitations, FDA decision-summary link
- **Deployment signals** — market availability, partner labs, estimated adoption
- **Sources** — every claim linked to a verifiable URL with a date accessed

Entries carry an explicit `data_completeness` flag (`full` / `partial` / `stub`) so readers can see exactly how much has been verified for each tool. As of v0.2: ~30 entries have full or partial validation summaries; the remainder are scaffolded stubs being populated on a rolling basis.

## Tech

- Plain HTML + Tailwind (CDN) — no framework build step
- `v1/data.json` is the source of truth for entries
- `scripts/validate.py` enforces the schema; `scripts/build_pages.py` generates per-tool detail pages
- Hosted on GitHub Pages

## Local preview

```bash
cd v1
python3 -m http.server 8000
# open http://localhost:8000
```

To regenerate per-tool pages after editing `data.json`:

```bash
python3 scripts/validate.py        # must pass
python3 scripts/build_pages.py     # regenerates v1/tools/*.html
```

## Contributing

PRs welcome. Each new or edited entry must:
- Meet the inclusion criteria in [Methodology](v1/methodology.html)
- Cite at least one verifiable public source per claim (FDA database or peer-reviewed publication preferred; press releases for deployment claims only, never for validation numbers)
- Include a `date_accessed` on every source
- Pass `python3 scripts/validate.py`

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

Until a methods paper is published, cite as:

```
Elbakri A. OncologyAI Registry [v0.2]. Available at: https://oncologyairegistry.org. Accessed [date].
```

To cite a specific tool, use its per-tool URL — e.g. `https://oncologyairegistry.org/tools/<tool-id>.html`.

## License

Content (registry data): **CC BY 4.0**
Code: **MIT**

## Curator

Ahmed Elbakri — Head of Laboratory Operations & Regulatory Strategy, Valar Labs · Stanford MBA. Conflict-of-interest disclosure published in the [Methodology](v1/methodology.html#conflict-of-interest-disclosure).
