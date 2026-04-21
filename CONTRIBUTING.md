# Contributing to the OncologyAI Registry

Thanks for your interest. Every entry in the registry is source-cited and reviewed — contributions from clinicians, regulators, researchers, company representatives, and journalists are welcome.

## Ways to contribute

- **Suggest a new entry** — a product we're missing.
- **Propose an edit** — a correction, new evidence, updated regulatory status, new partnership.
- **Flag an inaccuracy** — open an issue with a verifiable source.
- **Improve the site** — UX, filters, accessibility, rendering.

## Inclusion criteria (new entries)

To be listed, a product must meet all of the following:

1. Uses an AI or ML algorithm as a core component of clinical decision support, diagnosis, prognosis, or treatment selection.
2. Intended clinical use is in oncology (any cancer type, any modality).
3. Is available, in clinical trial, or formally announced for the U.S. market — including LDTs, FDA-cleared/approved devices, and Breakthrough Device-designated products.
4. Supported by at least one verifiable public source per claim (FDA database entry, peer-reviewed publication, or named-source press release).

See [Methodology](v1/methodology.html) for the full criteria and source hierarchy.

## How to submit a new entry

1. Fork the repo.
2. Copy `v1/entries/_template.yaml` to `v1/entries/<your-product-id>.yaml`.
3. Fill in every applicable field and cite your sources.
4. Run `python3 scripts/validate.py` locally to verify schema compliance.
5. Run `python3 scripts/build.py` to regenerate `v1/data.json`.
6. Open a pull request.

A maintainer will review within 14 days.

## PR review standards

- Every non-trivial claim must have a `source` URL and `date_accessed`.
- Performance metrics are only accepted from peer-reviewed publications — not press releases or marketing material.
- Regulatory claims must link to the FDA database, a named FDA decision letter, or the CE certificate.

## Conflict-of-interest

If you have a commercial, employment, advisory, or equity relationship with a listed company, disclose it in the PR description. This does not disqualify contributions but must be recorded for transparency.

## Code of conduct

Be respectful. Flag disagreements with evidence. The registry exists to help patients, clinicians, and the field — keep that in mind.
