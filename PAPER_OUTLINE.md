# Registry methods paper — outline

**Working title:** The OncologyAI Registry: methodology, scope, and landscape of AI-based diagnostic tools in U.S. oncology

**Proposed journal:** *npj Digital Medicine* (primary), *Scientific Data* (alternate — explicit home for dataset/registry descriptors), or *JAMIA* (alternate).

**Target submission:** July 2026 (after v1 has ~60 entries and 3 months of public use).

**Authorship:** Ahmed Elbakri (first author, corresponding); invite one Baylor collaborator (Tamer Mohamed) and one academic pathologist with no Valar tie as co-authors for breadth.

## Why this paper matters (for the NIW record)

- Becomes the canonical citation for the registry → cumulative independent citations over time → objective Prong 2 evidence of field-level influence
- Establishes the curator (Ahmed) as the recognized authority on the U.S. AI oncology diagnostics landscape
- Demonstrates the endeavor produces publicly-disseminated, non-proprietary output (cures the denial's proprietary-information finding)

## Paper structure

### Abstract (~250 words)
Background · Methods · Results (counts, FDA-status distribution, modality distribution, evidence base) · Discussion · Conclusion.

### 1. Introduction
- The U.S. clinical deployment of AI-based oncology diagnostics has accelerated since 2020.
- Regulatory pathways span FDA 510(k), De Novo, PMA, Breakthrough Device Designation, and CLIA/CAP laboratory-developed tests (LDTs).
- No single curated public reference consolidates products, pathways, evidence, and deployment signals — fragmentation impairs research, policy, payer review, and patient/clinician decision-making.
- Precedents for similar registries in other domains (ClinicalTrials.gov, FDA AI/ML-Enabled Medical Devices list, MIMIC-III/IV datasets) and their demonstrated utility to the research community.

### 2. Methods
- Inclusion / exclusion criteria (verbatim from methodology.html)
- Source hierarchy (FDA databases > peer-reviewed > regulatory docs > company press)
- Field taxonomy and controlled vocabularies (modality, cancer type, fda_status)
- Validation and schema enforcement (`scripts/validate.py`, CI)
- Refresh cycle (quarterly), versioning, deprecation policy
- Conflict-of-interest policy and disclosure procedures

### 3. Results (v1 snapshot)
- Total entries: 30 at v1 launch
- Distribution by cancer type, modality, regulatory pathway, availability
- Number of entries with peer-reviewed evidence vs. LDT-only vs. research-use-only
- Geographic market distribution (U.S. vs. EU-only vs. both)
- Figure 1 — sankey: cancer type → modality → regulatory pathway
- Figure 2 — timeline: year of FDA clearance / designation by pathway
- Figure 3 — evidence-base histogram (journal impact, publication year)
- Table 1 — summary statistics
- Table 2 — full entry list with key fields (or supplementary)

### 4. Discussion
- Landscape observations (what the data reveal about the field's current state)
- Gaps — cancers underserved by AI tools; modalities underrepresented; evidence quality concerns
- Regulatory heterogeneity — LDTs vs. FDA-cleared; implications for payer coverage, clinical adoption, and equity
- Limitations of the registry (self-reported data, lag in pharma products, limited visibility into pre-market pipeline)
- Comparison to adjacent resources (FDA AI/ML-Enabled Medical Devices list, ECRI Institute registries, commercial trackers)

### 5. Conclusion
- Registry is openly maintained and will be updated quarterly.
- Call for community contributions.
- Citation format.

### Data availability
- GitHub repo URL (MIT + CC BY 4.0)
- DOI via Zenodo snapshot at v1.0

### Competing interests
- Author employed by Valar Labs (listed company); full disclosure reproduced from registry Methodology page.

## Companion assets to produce alongside the paper

- **Zenodo DOI** for v1.0 snapshot (standard for dataset papers — makes the artifact formally citable)
- **Pre-print on medRxiv** at submission time
- **Press kit** (one-pager, quotes, visualizations) for simultaneous release

## What I need from the user to move this forward

1. Confirm co-author approach (just Ahmed first-author, or invite Tamer / academic pathologist)
2. Decide target journal (my vote: npj Digital Medicine primary, Scientific Data backup)
3. Registry needs to reach ~60 entries and 3 months of quarterly-refresh track record before submission — timeline fits a July 2026 submission
