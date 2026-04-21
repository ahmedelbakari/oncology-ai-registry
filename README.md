# OncologyAI Registry

The public, curated registry of AI/ML-based diagnostic tools in U.S. oncology.
Regulatory status · clinical evidence · deployment signals — every entry sourced. CC BY 4.0.

> **v0.1 — public preview** · 12 inaugural entries · launching publicly mid-2026

## Quick links
- 🌐 **Live site:** https://oncologyairegistry.org *(domain to be registered)*
- 📋 **[Methodology](v1/methodology.html)** — inclusion criteria, source hierarchy, conflict-of-interest disclosure
- ℹ️ **[About](v1/about.html)** — what the registry is and who maintains it
- 📊 **[Browse the registry](v1/index.html)**

## Why this exists

There is no single public, curated reference for AI-based diagnostic tools in U.S. oncology. Researchers, clinicians, regulators, payers, and journalists currently piece together this landscape manually — from FDA databases, individual press releases, and company sites. This produces inconsistent counts, out-of-date information, and no shared denominator for the field.

The OncologyAI Registry consolidates that information into one open-data resource with consistent inclusion criteria and a quarterly refresh.

## Tech

- Plain HTML + Tailwind (CDN) — no build step
- `data.json` is the source of truth for entries
- Hostable on GitHub Pages, Vercel, Netlify, or any static host

## Local preview

```bash
cd v1
python3 -m http.server 8000
# open http://localhost:8000
```

## Contributing

PRs welcome. Each new entry must:
- Meet the inclusion criteria in [Methodology](v1/methodology.html)
- Cite at least one verifiable public source per claim
- Include a `data_accessed` date

## Roadmap

- v0.1 (Apr 2026): scaffold + 12 inaugural entries
- v0.2 (May 2026): 30+ entries, About page polished, contributions intake form
- v0.3 (Jun 2026): 50+ entries, search improvements, programmatic API
- v1.0 (Jul 2026): public launch with press push (STAT, Endpoints, MedTech Dive)

## Citation

Until a methods paper is published, cite as:

```
Elbakri A. OncologyAI Registry [v0.1]. Available at: https://oncologyairegistry.org. Accessed [date].
```

## License

Content (registry data): **CC BY 4.0**
Code: **MIT**

## Curator

Ahmed Elbakri — Head of Laboratory Operations & Regulatory Strategy, Valar Labs · Stanford MBA. Conflict-of-interest disclosure published in the [Methodology](v1/methodology.html#conflict-of-interest-disclosure).
