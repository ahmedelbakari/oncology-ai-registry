# Validation Summary — Schema Proposal (v0.2)

**Status:** Approved by Ahmed 2026-05-08. Schema applied to all 103 entries; phase-1 pilot (3 entries) populated; remaining 15 phase-1 entries pending.

## Approved enum extensions (2026-05-08)

After the pilot batch surfaced cases that didn't fit the original enums:

- `primary_endpoint`: added `time_to_event_risk_strata` (K–M event rates by pre-specified risk categories — for prognostic classifiers like ArteraAI, Decipher, Oncotype DX, MammaPrint, Prosigna), and `ppv_npv` (for screening tests like GRAIL Galleri).
- `comparator`: added `clinicopathologic_factors` (AI vs. baseline demographic/pathologic variables in multivariable analysis — for prognostic biomarkers).

## Goal

Extend each registry entry with a **structured validation summary** so users (journalists, researchers, payers, policy analysts) can compare the *evidence behind* each tool, not just its FDA pathway. This is the feature that converts the registry from a list into a comparison reference.

## Schema additions (per entry)

Replace the current `clinical_evidence` object with a richer `validation` object. Old field stays under `validation.key_publication` for back-compat.

```json
"validation": {
  "study_design": "prospective | retrospective | rct | meta_analysis | bench_only | unpublished",
  "cohort_size": {
    "n_patients": 1234,
    "n_samples": null,
    "unit_note": "patients | slides | images | scans"
  },
  "n_sites": 5,
  "site_geography": "single_center_us | multi_center_us | multi_center_international",
  "comparator": "pathologist_consensus | gold_standard_test | clinical_outcomes | predicate_device | none",
  "primary_endpoint": "AUC | sensitivity | specificity | hazard_ratio | concordance | other",
  "primary_result": "AUC 0.89 (95% CI 0.85–0.92)",
  "external_validation": {
    "performed": true,
    "cohort_description": "independent multi-center cohort, n=412",
    "result": "AUC 0.86"
  },
  "peer_reviewed": true,
  "evidence_quality": "high | moderate | limited | unknown",
  "key_publications": [
    {
      "title": "...",
      "journal": "...",
      "year": 2024,
      "url": "...",
      "pivotal": true
    }
  ],
  "limitations_noted": "Retrospective; predominantly white male cohort; single-vendor scanner.",
  "fda_summary_url": "https://www.accessdata.fda.gov/...",
  "data_completeness": "full | partial | stub"
}
```

### Field rationale

- **`study_design`** — one categorical, one tag. `bench_only` is honest about 510(k) clearances that didn't see a clinical cohort.
- **`cohort_size`** — separate `n_patients` from `n_samples` because pathology and radiology AI are often validated on slide/image counts, not patient counts. `unit_note` disambiguates.
- **`site_geography`** — three buckets cover the meaningful distinctions for generalizability claims.
- **`comparator`** — the most-asked question by reviewers. `predicate_device` is the honest answer for many 510(k)s.
- **`primary_endpoint` + `primary_result`** — endpoint as enum for filtering; result as free text because numbers + CIs don't fit cleanly into a fixed schema.
- **`external_validation`** — separate object because the question "was this validated outside the discovery cohort" is the single highest-signal field for evidence quality.
- **`evidence_quality`** — curator judgment, with criteria documented in methodology. Yes, this is opinionated. That's the point.
- **`key_publications`** — array (replaces today's single field). `pivotal: true` flags the trial a reviewer should read first.
- **`limitations_noted`** — sourced from the paper or FDA summary, not curator opinion.
- **`data_completeness`** — `full` / `partial` / `stub` lets the site filter and lets readers see honestly what we know vs don't.

## What this enables

- Filterable views: "show all FDA-cleared tools with prospective multi-center validation"
- Compare-two-tools side-by-side
- Honest "evidence still emerging" markers on tools where it is
- A defensible methods paper: "OncologyAI Registry: a structured catalogue of clinical validation evidence for AI diagnostics in U.S. oncology"

## Curation cost (honest)

- Per entry, populating fully: 30–60 min (read pivotal paper / FDA summary, extract numbers).
- All 103 entries: 50–100 hours.
- **Recommendation:** ship v0.2 with 15–20 entries fully populated and the rest marked `data_completeness: stub`. Fill the rest as v0.3 / v0.4.

## Phase 1 — entries to deep-populate before launch (18 entries)

Picked for: (a) a journalist would name them in a story, (b) they span modalities, (c) they have published pivotal evidence to extract.

| # | id | Company | Tool | Why include |
|---|----|---------|------|-------------|
| 1 | `paige-prostate-detect` | Paige.AI | Paige Prostate Detect | First FDA-authorized AI in pathology (De Novo) |
| 2 | `paige-her2` | Paige.AI | Paige HER2 Assistant | Recognized brand; breast |
| 3 | `pathai-aisight-dx` | PathAI | AISight Dx | Major pathology AI platform |
| 4 | `ibex-galen-prostate` | Ibex | Galen Prostate | Prospective trial published |
| 5 | `ibex-galen-breast` | Ibex | Galen Breast | Multi-site validation |
| 6 | `owkin-msintuit-crc` | Owkin | MSIntuit CRC | CE-marked, peer-reviewed |
| 7 | `vesta-bcg` | Valar Labs | Vesta BCGPredict | Your own; J Urol 2024 |
| 8 | `tempus-xt` | Tempus | xT | Largest oncology genomic platform |
| 9 | `tempus-xm` | Tempus | xM (MRD) | Newer MRD entrant |
| 10 | `signatera-mrd` | Natera | Signatera | Most-cited MRD test |
| 11 | `grail-galleri` | GRAIL | Galleri | Highest-profile MCED; PATHFINDER trial |
| 12 | `exact-oncotype-dx-breast` | Exact Sciences | Oncotype DX | Decades of evidence; payer-relevant |
| 13 | `veracyte-decipher-prostate` | Veracyte | Decipher Prostate | NCCN-cited |
| 14 | `veracyte-afirma-gsc` | Veracyte | Afirma GSC | Thyroid; payer-covered |
| 15 | `artera-prostate` | Artera | ArteraAI Prostate | NRG/RTOG validated |
| 16 | `icad-profound-ai-dbt` | iCAD | ProFound AI for DBT | Mammography AI flagship |
| 17 | `hologic-genius-ai-detection` | Hologic | Genius AI Detection | Mammography; large vendor |
| 18 | `aidoc-briefcase-lung-nodule` | Aidoc | Incidental Lung Nodule | Radiology workflow AI |

Spans pathology (7), genomics (6), radiology (3), liquid biopsy (2). All have published pivotal evidence.

## Decisions needed from Ahmed

1. **Approve schema?** Specifically: are the field names and enums right? Anything missing (e.g., regulatory submission cohort vs. post-market evidence as separate slots)?
2. **Approve the 18-entry phase-1 list?** Swap any in/out?
3. **Evidence-quality grading** — am I authorized to publish curator judgments (`high/moderate/limited`)? This is the most opinionated field. Alternative: drop it for v0.2 and just publish the underlying facts.
4. **Methodology paper as v1.0 deliverable?** This validation work is the substrate for a methods paper — worth committing to before launch?

## Next steps once approved

1. Apply schema to `data.json` (all 103 entries get the new structure with `data_completeness: stub` where unfilled).
2. Update `scripts/validate.py` to enforce the new schema.
3. Update `methodology.html` with the new fields + grading criteria.
4. Populate the 18 phase-1 entries (real source research per entry, ~10–15 hours).
5. Update site UI to display validation summary + add filter UI.
