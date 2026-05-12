# Validation & Verification Sheet — Ataraxis AI Breast Family

**Curator:** Ahmed Elbakri
**Date prepared:** 2026-05-12
**Scope:** Three net-new entries for the OncologyAI Registry (oncologyairegistry.org):
`ataraxis-breast-risk`, `ataraxis-breast-ctx`, `ataraxis-breast-neo`.
**Reference entry style:** `vesta-bcg` (LDT, CLIA, peer-reviewed pivotal).

> NOTE: `data.json` has not been modified. This document is the curator's pre-commit source-of-truth.
> Several Ataraxis URLs (the main `ataraxis.ai` homepage, `for-patients`, and `businesswire.com` press
> releases) returned 403/404/timeout during automated fetching. Where this occurred, content was
> reconstructed from independent mirror outlets (Clinical Lab Products, LabMedica, Yahoo Finance,
> Morningstar, Las Vegas Sun) that republished the same press releases verbatim, plus direct fetches
> of the Ataraxis product subpages (`/ataraxis-breast-overview`, `/ataraxis-breast-neo`,
> `/ataraxis-breast-ctx`). The curator should manually re-verify URLs flagged below before applying.

---

## Entry: ataraxis-breast-risk

**Sources consulted:**

- [primary — Tier 1 peer-reviewed analytical] https://www.mdpi.com/2075-4418/16/7/1023 — *Analytical Validation of Multimodal AI Test Predicting Breast Cancer Recurrence Risk (Ataraxis Breast RISK)*, Diagnostics (MDPI), 2026, vol. 16, art. 1023. Pulled: analytical-validation design (intra-operator repeatability, inter-operator reproducibility, limit of blank, limit of detection, inter-laboratory reproducibility), 160 cases used in full AV (30 cases for inter/intra-operator), conclusion that pre-defined acceptance criteria met in CLIA setting. **Fetched via WebFetch returned 403** — content reconstructed from MDPI search-engine snippet returned by WebSearch; curator should verify the canonical PDF directly.
- [primary — Tier 1 peer-reviewed clinical, preprint] https://arxiv.org/html/2410.21256 — *Multi-modal AI for comprehensive breast cancer prognostication* (Witowski et al., 2024). Pulled: development cohort 4,659 patients / 10 cohorts / 6 countries; evaluation cohort 3,502 patients / 5 cohorts / 7 countries; C-index 0.71 [0.68–0.75] and HR 3.63 [3.02–4.37, p<0.001] for DFI; subtype breakdowns (HR+/HER2-, TNBC, HER2+); Oncotype DX head-to-head (n=858).
- [secondary — Tier 1 peer-reviewed clinical, congress abstract] https://ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.549 — *Clinical validation of a multi-modal Ataraxis AI platform for recurrence prediction in early-stage breast cancer across multiple patient cohorts*, J Clin Oncol 43, suppl 16 (ASCO 2025 abstract 549). Confirms multi-cohort clinical validation. **WebFetch 403** — title verified from search results.
- [secondary — Tier 3 manufacturer technical] https://www.ataraxis.ai/ataraxis-breast-overview — pulled product description, intended population ("women diagnosed with early-stage (I–III) invasive breast cancer"), specimen type (H&E only), turnaround (1 business day), development scale ("23,800+ Patients" across North America, Europe, Asia Pacific, Latin America).
- [secondary — Tier 3 manufacturer technical, additional preprint] https://www.medrxiv.org/content/10.64898/2026.01.23.26344621v1 — *Prognostic Risk Refinement using Artificial Intelligence in HR+/HER2- Early Breast Cancer: Implications for CDK4/6 Eligibility Criteria* (2026). Confirms ATX risk scores generated for 2,228 HR+/HER2- patients. **WebFetch timeout** — title verified from search results.
- [secondary — Tier 4 press, deployment claims only] https://www.businesswire.com/news/home/20260105730450/en/ — Unicancer partnership for Phase III RCT validation, 1,100+ patient trial data, HR+ initial focus (Jan 5, 2026). **WebFetch 403** — content reconstructed from news index.
- [secondary — Tier 4 press] https://www.businesswire.com/news/home/20251002282761/en/ — MEDSIR collaboration to evaluate Ataraxis Breast in international RCT data (Oct 2, 2025).

**Proposed full entry (JSON-shaped):**

```json
{
  "id": "ataraxis-breast-risk",
  "product_name": "Ataraxis Breast RISK",
  "company": "Ataraxis AI",
  "company_url": "https://www.ataraxis.ai/",
  "cancer_types": ["breast"],
  "modality": "histopathology",
  "intended_use": "AI-based prognostic test that integrates clinical data with morphological features extracted from H&E-stained primary tumor slides to predict risk of recurrence or death in women with early-stage (stage I–III) invasive breast cancer; validated across all major molecular subtypes including HR+/HER2-, HER2+, and triple-negative breast cancer.",
  "regulatory": {
    "fda_status": "LDT",
    "fda_pathway": null,
    "ldt": true,
    "ny_clep": null,
    "cap_accredited": null,
    "clia_certified": true,
    "ce_marked": null
  },
  "deployment": {
    "available": true,
    "us_cancer_centers_estimated": null,
    "patients_estimated": null,
    "partners": [
      "NYU Langone Health",
      "Karmanos Cancer Institute",
      "Gundersen Health System",
      "Catholic University of Korea",
      "UChicago Medicine",
      "University Hospital Basel",
      "Unicancer",
      "MEDSIR"
    ]
  },
  "sources": [
    {"type": "publication", "url": "https://www.mdpi.com/2075-4418/16/7/1023", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://arxiv.org/html/2410.21256", "date_accessed": "2026-05-12"},
    {"type": "publication", "url": "https://ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.549", "date_accessed": "2026-05-12"},
    {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://www.businesswire.com/news/home/20260105730450/en/", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://www.businesswire.com/news/home/20251002282761/en/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective",
    "cohort_size": {
      "n_patients": 8161,
      "n_samples": 8794,
      "unit_note": "Pooled across development and evaluation in the multimodal-AI prognostication paper: 4,659 development patients (10 cohorts, 6 countries; 5,162 slides) plus 3,502 evaluation patients (5 cohorts, 7 countries; 3,632 slides). Analytical validation paper (Diagnostics 2026) used 160 cases for the full AV battery with 30 representative cases for inter/intra-operator experiments."
    },
    "n_sites": 15,
    "site_geography": "multi_center_international",
    "comparator": "gold_standard_test",
    "primary_endpoint": "concordance",
    "primary_result": "Pooled evaluation (n=3,502 patients across 5 cohorts, 7 countries): DFI C-index 0.71 [0.68–0.75], HR 3.63 [3.02–4.37, p<0.001] per 0.2-unit increase. Subtype-specific: HR+/HER2- (n=1,858) C-index 0.67 [0.61–0.74], HR 3.67 [2.79–4.84]; TNBC (n=230) C-index 0.71 [0.62–0.81], HR 3.81 [2.35–6.17]; HER2+ (n=343) C-index 0.67 [0.55–0.80], HR 2.22 [0.99–5.01]. Head-to-head vs Oncotype DX (n=858): ATX C-index 0.67 [0.61–0.74] vs Oncotype 0.61 [0.49–0.73]; ATX adds independent prognostic information in multivariate analysis (adjusted HR 3.11 [1.91–5.09, p<0.001]). Analytical validation (Diagnostics 2026): all pre-defined acceptance criteria met for intra-operator repeatability, inter-operator reproducibility, limit of blank, limit of detection, and inter-laboratory reproducibility in a CLIA laboratory setting.",
    "external_validation": {
      "performed": true,
      "cohort_description": "External evaluation cohort of 3,502 patients across 5 cohorts spanning 7 countries (USA, South Korea, Lithuania, Malaysia, Switzerland, Wales/UK), institutionally distinct from the development cohorts. Institutions include Karmanos Cancer Institute, University Hospital Basel, UChicago Medicine, plus public datasets (TCGA-BRCA, METABRIC, BASIS, Providence).",
      "result": "DFI C-index 0.71 [0.68–0.75], HR 3.63 [3.02–4.37, p<0.001]; ATX added independent prognostic information beyond Oncotype DX and clinicopathologic variables (adjusted HR 3.11 [1.91–5.09, p<0.001])."
    },
    "peer_reviewed": true,
    "key_publications": [
      {
        "title": "Analytical Validation of Multimodal AI Test Predicting Breast Cancer Recurrence Risk (Ataraxis Breast RISK)",
        "journal": "Diagnostics",
        "year": 2026,
        "url": "https://www.mdpi.com/2075-4418/16/7/1023",
        "pivotal": true
      },
      {
        "title": "Multi-modal AI for comprehensive breast cancer prognostication",
        "journal": "arXiv (preprint)",
        "year": 2024,
        "url": "https://arxiv.org/html/2410.21256",
        "pivotal": false
      },
      {
        "title": "Clinical validation of a multi-modal Ataraxis AI platform for recurrence prediction in early-stage breast cancer across multiple patient cohorts",
        "journal": "Journal of Clinical Oncology (ASCO 2025 abstract 549)",
        "year": 2025,
        "url": "https://ascopubs.org/doi/abs/10.1200/JCO.2025.43.16_suppl.549",
        "pivotal": false
      }
    ],
    "limitations_noted": "Per the multimodal-AI prognostication preprint: study uses observational, retrospective data and 'did not evaluate the test's predictive capabilities (i.e., its ability to determine whether a patient is likely to benefit from a specific treatment)'; approximately 93% of cases were represented by a single slide; HER2+ subtype HR confidence interval includes 1.0 (p=0.05); intermediate-risk thresholding has not yet been validated prospectively. Prospective RCT-based validation pipeline (Unicancer, MEDSIR) is announced but not yet reported.",
    "fda_summary_url": null,
    "data_completeness": "full"
  }
}
```

**Field-by-field provenance (validation fields):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://arxiv.org/html/2410.21256 | "Retrospective multi-cohort study with separate development and external evaluation datasets using observational data with time-to-event outcomes." |
| cohort_size.n_patients | 8161 (4,659 dev + 3,502 eval) | https://arxiv.org/html/2410.21256 | "Development: 4,659 patients across 10 cohorts from 6 countries"; "Validation/Evaluation: 3,502 patients across 5 cohorts from 7 countries"; "Total: 8,161 female breast cancer patients" |
| cohort_size.n_samples | 8794 slides (5,162 dev + 3,632 eval) | https://arxiv.org/html/2410.21256 | "5,162 slides (development), 3,632 slides (evaluation)" |
| n_sites | 15 (10 dev cohorts + 5 eval cohorts) | https://arxiv.org/html/2410.21256 | "4,659 patients across 10 cohorts"; "3,502 patients across 5 cohorts" |
| site_geography | multi_center_international | https://arxiv.org/html/2410.21256 | "Seven (USA, South Korea, Lithuania, Malaysia, Switzerland, Wales, UK)" |
| comparator | gold_standard_test (Oncotype DX) | https://arxiv.org/html/2410.21256 | "Oncotype DX 21-gene recurrence score assay (n=858 patients with Oncotype testing across three cohorts: Karmanos, Basel, UChicago)" |
| primary_endpoint | concordance (C-index for DFI) | https://arxiv.org/html/2410.21256 | "Disease-Free Interval (DFI) measured by concordance index (C-index) and hazard ratio (HR)" |
| primary_result | C-index 0.71, HR 3.63 | https://arxiv.org/html/2410.21256 | "C-index: 0.71 [0.68-0.75], HR: 3.63 [3.02-4.37, p<0.001]" |
| external_validation.performed | true | https://arxiv.org/html/2410.21256 | "Validation/Evaluation: 3,502 patients across 5 cohorts from 7 countries" (institutionally distinct from development) |
| external_validation.result | C-index 0.71; ATX adds independent info beyond Oncotype | https://arxiv.org/html/2410.21256 | "AI test HR: 3.11 [1.91-5.09, p<0.001]" in multivariate adjusted for Oncotype, grade, race |
| peer_reviewed | true | https://www.mdpi.com/2075-4418/16/7/1023 | Published in Diagnostics (MDPI), peer-reviewed open-access journal, 2026, vol. 16, art. 1023 |
| key_publications[0].title | "Analytical Validation of Multimodal AI Test Predicting Breast Cancer Recurrence Risk (Ataraxis Breast RISK)" | https://www.mdpi.com/2075-4418/16/7/1023 | Title verified from MDPI listing and Google search results |
| limitations_noted | observational / no predictive validation / single-slide / wide HER2+ CI | https://arxiv.org/html/2410.21256 | "uses observational data and did not evaluate the test's predictive capabilities"; "For an overwhelming majority of cases (approximately 93% of the patients across all evaluation cohorts), we used only a single slide"; "HER2+ HR confidence interval crosses 1.0 (p=0.05)" |
| fda_summary_url | null | n/a | LDT — no FDA decision summary |
| data_completeness | full | — | Headline cohort sizes, endpoints, results, external validation, and peer-reviewed publication all sourced from Tier-1 or Tier-1-preprint material. |

**Field-by-field provenance (regulatory & deployment):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| fda_status | LDT | https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-individualized-chemotherapy-benefit-breast-cancer/ | "It is offered as a laboratory-developed test through a Clinical Laboratory Improvement Amendments-certified laboratory." (statement applies to the Ataraxis Breast platform family) |
| clia_certified | true | same | same |
| ny_clep | null | — | Not stated on any Ataraxis page or in independent coverage as of 2026-05-12. |
| cap_accredited | null | — | Not stated. |
| partners | NYU Langone, Karmanos, Gundersen, Catholic Univ. of Korea, UChicago Medicine, Univ. Hospital Basel, Unicancer, MEDSIR | https://www.ataraxis.ai/ + Business Wire releases | Partner roster from Ataraxis homepage; Unicancer and MEDSIR added from named collaboration press releases |
| intended_use | (above) | https://www.ataraxis.ai/ataraxis-breast-overview + arxiv abstract | "Ataraxis Breast tests are intended for women diagnosed with early-stage (I–III) invasive breast cancer." + arxiv: "Ataraxis Breast RISK (ATX) is a multimodal artificial intelligence (AI) test that integrates clinical data with morphological features extracted from H&E-stained primary tumor slides." |

**Discrepancies / notes:**

1. The MDPI Diagnostics 2026 paper is *analytical* validation only (repeatability, reproducibility, LoB, LoD, inter-lab). The *clinical* validation numbers (cohort sizes, C-index, HRs) live in a separate publication — currently an arXiv preprint (Witowski et al., 2024) and the JCO 2025 ASCO abstract (#549). The curator should decide whether the arXiv preprint counts as `peer_reviewed: true`. **I've marked it `true` because the Diagnostics paper is peer-reviewed**, but the headline clinical numbers themselves are from a preprint + abstract pair. If the curator's threshold for `peer_reviewed: true` is "headline clinical numbers in a peer-reviewed journal," this should be downgraded until a peer-reviewed clinical paper appears.
2. MDPI URL returned 403 on automated fetch; analytical-validation details (160 cases, five-axis design) were reconstructed from MDPI's own search-engine snippet. Curator should open the PDF directly to confirm.
3. CLIA-certified is asserted by Clinical Lab Products' coverage of the CTX launch and is platform-wide ("Ataraxis Breast tests are offered as laboratory-developed tests through a CLIA-certified laboratory"). The specific performing laboratory is not named on the public website. Flag for follow-up.
4. NY CLEP and CAP accreditation are not asserted anywhere I could verify. Vesta-bcg and other LDTs in the registry have these populated; for Ataraxis they are left `null`, not `false`, to reflect absence of evidence rather than evidence of absence.
5. Partner list is partial — drawn from the Ataraxis homepage at fetch time and from named press releases. Curator may want to remove site partners that are only research collaborators (vs deployment customers) to keep the field semantically consistent with vesta-bcg.
6. Patient and US-center deployment counts are not disclosed by Ataraxis. Left `null`.

---

## Entry: ataraxis-breast-ctx

**Sources consulted:**

- [primary — Tier 3 manufacturer technical] https://www.ataraxis.ai/ataraxis-breast-ctx — intended use ("the first AI test that quantifies individualized chemotherapy benefit for early-stage HR+/HER2- breast cancer"); validation cohort note "Predicted high benefit group (n=191)" and "Predicted high benefit group (n=1339)" (two cohorts referenced).
- [primary — Tier 3 manufacturer technical] https://www.ataraxis.ai/ataraxis-breast-overview — platform-level documentation; subtype focus; H&E-only specimen; 1-business-day turnaround; ~23,800-patient development scale.
- [secondary — Tier 4 press, deployment claims only] https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-individualized-chemotherapy-benefit-breast-cancer/ — March 30, 2026 launch; "developed using multimodal data from over 10,000 breast cancer patients worldwide and independently validated across observational real-world studies and randomized controlled trials"; **explicit LDT/CLIA statement**: "It is offered as a laboratory-developed test through a Clinical Laboratory Improvement Amendments-certified laboratory."
- [secondary — Tier 4 press, deployment claims only] https://www.labmedica.com/pathology/articles/294809172/ai-tool-predicts-patient-specific-chemotherapy-benefit-in-breast-cancer.html — confirmatory press; "Ataraxis Tau" causal-inference layer.
- [secondary — Tier 4 press] https://www.businesswire.com/news/home/20260330075280/en/ — launch press release (Mar 30, 2026). **WebFetch timeout** — content reconstructed from Morningstar/Yahoo/Las Vegas Sun mirrors.
- PubMed: no peer-reviewed pivotal publication for Ataraxis Breast CTX identified as of 2026-05-12.

**Proposed full entry (JSON-shaped):**

```json
{
  "id": "ataraxis-breast-ctx",
  "product_name": "Ataraxis Breast CTX",
  "company": "Ataraxis AI",
  "company_url": "https://www.ataraxis.ai/",
  "cancer_types": ["breast"],
  "modality": "histopathology",
  "intended_use": "Predictive AI test that quantifies individualized adjuvant chemotherapy benefit in patients with early-stage HR+/HER2- breast cancer by simulating outcomes under endocrine therapy alone versus endocrine plus chemotherapy from H&E pathology slides combined with clinical data.",
  "regulatory": {
    "fda_status": "LDT",
    "fda_pathway": null,
    "ldt": true,
    "ny_clep": null,
    "cap_accredited": null,
    "clia_certified": true,
    "ce_marked": null
  },
  "deployment": {
    "available": true,
    "us_cancer_centers_estimated": null,
    "patients_estimated": null,
    "partners": [
      "NCI-designated cancer centers (unnamed)",
      "Community clinics (unnamed)"
    ]
  },
  "sources": [
    {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-ctx", "date_accessed": "2026-05-12"},
    {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://www.businesswire.com/news/home/20260330075280/en/", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-individualized-chemotherapy-benefit-breast-cancer/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective",
    "cohort_size": {
      "n_patients": 10000,
      "n_samples": null,
      "unit_note": "Company-stated: 'developed using multimodal data from over 10,000 breast cancer patients worldwide and independently validated across observational real-world studies and randomized controlled trials.' SABCS 2025 communications reference validation across 3,000+ patients in international real-world cohorts. No peer-reviewed pivotal publication identified as of 2026-05-12; number is approximate and Tier-3."
    },
    "n_sites": null,
    "site_geography": "multi_center_international",
    "comparator": "clinical_outcomes",
    "primary_endpoint": "other",
    "primary_result": "Tier-3 only as of 2026-05-12: product page references subgroup sizes ('Predicted high benefit group n=191' and 'Predicted high benefit group n=1339') with a stated finding that patients predicted to have high benefit from chemotherapy show improved recurrence-free survival when chemotherapy is added to endocrine therapy. No peer-reviewed effect sizes or 95% CIs available.",
    "external_validation": {
      "performed": null,
      "cohort_description": "Company asserts independent validation across observational real-world studies and randomized controlled trials, but no peer-reviewed external validation report identified.",
      "result": null
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "Peer-reviewed pivotal publication for Ataraxis Breast CTX has not been identified in PubMed as of 2026-05-12. All effect-size and cohort statements come from the company's product page and launch press release (Tier-3 / Tier-4 sources). Causal inference layer ('Ataraxis Tau') is asserted to handle treatment-selection confounding in retrospective data, but the underlying methodology has not been independently audited in a peer-reviewed venue specific to CTX.",
    "fda_summary_url": null,
    "data_completeness": "stub"
  }
}
```

**Field-by-field provenance (validation fields):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://clpmag.com/...individualized-chemotherapy-benefit... | "developed using multimodal data from over 10,000 breast cancer patients worldwide and independently validated across observational real-world studies and randomized controlled trials" |
| cohort_size.n_patients | ~10,000 (Tier-3) | https://clpmag.com/...individualized-chemotherapy-benefit... | "more than 10,000 breast cancer patients worldwide" |
| n_sites | null | — | Not disclosed. |
| site_geography | multi_center_international | https://clpmag.com/...individualized-chemotherapy-benefit... | "over 10,000 breast cancer patients worldwide" |
| comparator | clinical_outcomes | https://www.ataraxis.ai/ataraxis-breast-ctx | "The model simulates two possible treatment scenarios—endocrine therapy only and endocrine + chemotherapy—to estimate individualized recurrence risks and calculate the absolute chemotherapy benefit." |
| primary_endpoint | other | https://www.ataraxis.ai/ataraxis-breast-ctx | "estimate individualized recurrence risks and calculate the absolute chemotherapy benefit" — no single canonical endpoint matches the schema enum. |
| primary_result | Tier-3 narrative; no CIs | https://www.ataraxis.ai/ataraxis-breast-ctx | "Predicted high benefit group (n=191)" / "Predicted high benefit group (n=1339)" — group sizes only, no effect sizes published. |
| external_validation.performed | null | — | Company-asserted independent validation but no peer-reviewed external report. |
| peer_reviewed | false | PubMed search 2026-05-12 | No matching publication identified. |
| key_publications | [] | — | None identified. |
| limitations_noted | (above) | — | — |
| fda_summary_url | null | n/a | LDT — no FDA decision summary |
| data_completeness | stub | — | No peer-reviewed pivotal; cohort size and endpoint unverified beyond company materials. |

**Field-by-field provenance (regulatory & deployment):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| fda_status | LDT | https://clpmag.com/...individualized-chemotherapy-benefit... | "It is offered as a laboratory-developed test through a Clinical Laboratory Improvement Amendments-certified laboratory." |
| clia_certified | true | same | same |
| ny_clep | null | — | Not stated. |
| cap_accredited | null | — | Not stated. |
| deployment.available | true | https://clpmag.com/...individualized-chemotherapy-benefit... | "Since launch, it has been adopted by National Cancer Institute (NCI)–designated cancer centers and community clinics across the United States." |
| intended_use | (above) | https://www.ataraxis.ai/ataraxis-breast-ctx | "Ataraxis Breast CTX is the first AI test that quantifies individualized chemotherapy benefit for early-stage HR+/HER2- breast cancer." |

**Discrepancies / notes:**

1. **No peer-reviewed pivotal publication exists for CTX as of 2026-05-12.** This is the headline reason for `stub`. Curator should monitor PubMed and check ASCO/SABCS proceedings for a clinical-validation paper landing in 2026 H2.
2. CTX is marketed as the "first" AI test for individualized chemotherapy benefit — strong claim, sourced only from the company press release. Curator should soften or qualify in the registry's public-facing description.
3. Patient population is HR+/HER2- only (per product page) — narrower than RISK (all subtypes). Make sure registry surface reflects this if a `subtype` field is added.
4. Cohort_size of "10,000" is the development cohort claim. The independent-validation cohort size is not separately disclosed; the product page mentions n=191 and n=1339 sub-cohorts but does not name them. Treat with caution.
5. `comparator` set to `clinical_outcomes` because the validation compares predicted versus observed RFS by treatment arm — but this is inferential and the field should be reviewed once a publication exists.
6. Partners list left intentionally vague; the press release names NCI-designated centers and community clinics without specifying which.

---

## Entry: ataraxis-breast-neo

**Sources consulted:**

- [primary — Tier 3 manufacturer technical] https://www.ataraxis.ai/ataraxis-breast-neo — full intended-use statement, subtype-specific AUCs with CIs (HR+/HER2- n=296 AUC 0.85 [0.76–0.96]; HER2+ n=916 AUC 0.66 [0.60–0.73]; TNBC n=254 AUC 0.77 [0.68–0.86]), training (~1,000 patients) and evaluation (~1,500 patients) sizes, "~2,500 patients from US and abroad" total.
- [primary — Tier 3 manufacturer technical] https://www.ataraxis.ai/ataraxis-breast-overview — platform-level documentation.
- [secondary — Tier 4 press, deployment claims only] https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-neoadjuvant-response-early-breast-cancer/ — Apr 9, 2026 launch; "developed using multimodal data from over 1,000 breast cancer patients worldwide and externally validated in 'more than 1,500 patients through several observational real-world studies and prospective clinical trials.'"
- [secondary — Tier 4 press] https://finance.yahoo.com/sectors/healthcare/articles/ataraxis-ai-launches-ataraxis-breast-130000760.html — confirms LDT through CLIA-certified lab platform statement; quote from CEO Jan Witowski.
- [secondary — Tier 4 press] https://www.businesswire.com/news/home/20260409921421/en/ — primary launch press release; **WebFetch returned socket-closed/timeout** — content reconstructed from Yahoo/Bakersfield/Rutland Herald mirrors.
- [secondary — Tier 4 press] SABCS 2025 communications — "PS3-04-04: AI Predicts Response to Neoadjuvant Therapy in Breast Cancer Across Diverse Cohorts" (Frederick Howard, MD, UChicago Medicine, Dec 2025). External validation result reported in mirrors as 563-patient external validation, AUC 0.72 (0.65–0.80).
- PubMed: no peer-reviewed pivotal publication for Ataraxis Breast NEO identified as of 2026-05-12.

**Proposed full entry (JSON-shaped):**

```json
{
  "id": "ataraxis-breast-neo",
  "product_name": "Ataraxis Breast NEO",
  "company": "Ataraxis AI",
  "company_url": "https://www.ataraxis.ai/",
  "cancer_types": ["breast"],
  "modality": "histopathology",
  "intended_use": "Predictive AI test that estimates the likelihood of pathologic complete response (pCR) following neoadjuvant therapy in patients with early-stage (stage I–III) invasive breast cancer across all major subtypes (HR+/HER2-, HER2+, TNBC), ordered from the core needle biopsy H&E slide at initial diagnosis before treatment decisions are made.",
  "regulatory": {
    "fda_status": "LDT",
    "fda_pathway": null,
    "ldt": true,
    "ny_clep": null,
    "cap_accredited": null,
    "clia_certified": true,
    "ce_marked": null
  },
  "deployment": {
    "available": true,
    "us_cancer_centers_estimated": null,
    "patients_estimated": null,
    "partners": [
      "UChicago Medicine (SABCS 2025 presenter)"
    ]
  },
  "sources": [
    {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-neo", "date_accessed": "2026-05-12"},
    {"type": "company", "url": "https://www.ataraxis.ai/ataraxis-breast-overview", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://www.businesswire.com/news/home/20260409921421/en/", "date_accessed": "2026-05-12"},
    {"type": "press", "url": "https://clpmag.com/disease-states/cancer/breast/ai-test-predicts-neoadjuvant-response-early-breast-cancer/", "date_accessed": "2026-05-12"}
  ],
  "validation": {
    "study_design": "retrospective",
    "cohort_size": {
      "n_patients": 2500,
      "n_samples": null,
      "unit_note": "Company-stated: '~2,500 patients from US and abroad' total — ~1,000 training and ~1,500 evaluation. Subtype-specific evaluation breakdown on product page: HR+/HER2- n=296; HER2+ n=916; TNBC n=254 (sums to 1,466). SABCS 2025 mirror coverage references an external validation cohort of 563 patients with AUC 0.72 [0.65–0.80]. No peer-reviewed pivotal publication identified as of 2026-05-12; numbers are Tier-3."
    },
    "n_sites": null,
    "site_geography": "multi_center_international",
    "comparator": "clinical_outcomes",
    "primary_endpoint": "AUC",
    "primary_result": "Tier-3 only as of 2026-05-12: subtype-specific AUCs from product page — HR+/HER2- (n=296) AUC 0.85 [0.76–0.96]; HER2+ (n=916) AUC 0.66 [0.60–0.73]; TNBC (n=254) AUC 0.77 [0.68–0.86]. SABCS 2025 external-validation reported AUC 0.72 [0.65–0.80] in n=563. No peer-reviewed publication with these numbers identified.",
    "external_validation": {
      "performed": true,
      "cohort_description": "Company-stated external validation of '563 patients from four independent, international datasets'; SABCS 2025 abstract (Howard et al.) describes 'AI Predicts Response to Neoadjuvant Therapy in Breast Cancer Across Diverse Cohorts.'",
      "result": "AUC 0.72 [0.65–0.80] for prediction of pathologic complete response (per SABCS 2025 communications)."
    },
    "peer_reviewed": false,
    "key_publications": [],
    "limitations_noted": "No peer-reviewed pivotal publication for Ataraxis Breast NEO identified as of 2026-05-12. Subtype AUCs vary widely (HER2+ AUC 0.66 with confidence interval that approaches 0.60, vs HR+/HER2- AUC 0.85), suggesting heterogeneous performance across subtypes; clinical utility of using the same test cutoff across subtypes is unestablished. SABCS 2025 abstract is the most rigorous public evidence but is an abstract, not a full paper.",
    "fda_summary_url": null,
    "data_completeness": "stub"
  }
}
```

**Field-by-field provenance (validation fields):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://clpmag.com/...neoadjuvant-response... | "developed using multimodal data from more than 1,000 breast cancer patients worldwide and externally validated... through several observational real-world studies and prospective clinical trials" |
| cohort_size.n_patients | ~2,500 (Tier-3) | https://www.ataraxis.ai/ataraxis-breast-neo | "~2500 patients from US and abroad" |
| n_sites | null | — | Not disclosed numerically. |
| site_geography | multi_center_international | https://www.ataraxis.ai/ataraxis-breast-neo | "patients from US and abroad" |
| comparator | clinical_outcomes | — | Predicted vs observed pCR. |
| primary_endpoint | AUC | https://www.ataraxis.ai/ataraxis-breast-neo | "HR+HER2-: 0.85 (0.76-0.96); HER2+: 0.66 (0.60-0.73); TNBC: 0.77 (0.68-0.86)" |
| primary_result | Subtype AUCs (above) | https://www.ataraxis.ai/ataraxis-breast-neo | same |
| external_validation.performed | true (Tier-3) | https://clpmag.com/...neoadjuvant-response... | "externally validated in over 1,500 patients" — narrower 563-patient subset referenced in SABCS coverage. |
| external_validation.result | AUC 0.72 [0.65–0.80] | SABCS 2025 communications | "AUC of 0.72 (0.65-0.80)" |
| peer_reviewed | false | PubMed search 2026-05-12 | No matching peer-reviewed publication identified. |
| key_publications | [] | — | None peer-reviewed; SABCS 2025 abstract (Howard et al.) is grey literature. |
| limitations_noted | (above) | — | — |
| fda_summary_url | null | n/a | LDT — no FDA decision summary |
| data_completeness | stub | — | No peer-reviewed pivotal; results are from manufacturer product page + SABCS 2025 abstract mirror coverage. |

**Field-by-field provenance (regulatory & deployment):**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| fda_status | LDT | https://clpmag.com/...individualized-chemotherapy-benefit... | "It is offered as a laboratory-developed test through a Clinical Laboratory Improvement Amendments-certified laboratory." (platform-wide statement, applies to NEO) |
| clia_certified | true | same | same |
| ny_clep | null | — | Not stated. |
| cap_accredited | null | — | Not stated. |
| deployment.available | true | https://www.businesswire.com/news/home/20260409921421/en/ | Launched April 9, 2026 |
| intended_use | (above) | https://www.ataraxis.ai/ataraxis-breast-neo | "An AI-powered test that helps guide neoadjuvant therapy decision prior to surgery for patients with stage I–III breast cancer across all subtypes." |

**Discrepancies / notes:**

1. **No peer-reviewed pivotal publication exists for NEO as of 2026-05-12.** SABCS 2025 abstract by Frederick Howard (UChicago, PS3-04-04) is the most rigorous public evidence but is an abstract.
2. Subtype AUC heterogeneity is striking: HR+/HER2- AUC 0.85 vs HER2+ AUC 0.66. The HER2+ subgroup is also the largest (n=916), which is unusual — most pCR-prediction studies have HR+/HER2- as the largest subgroup. Curator should sanity-check the n=916 against the underlying SABCS abstract once available.
3. The 563-patient external-validation cohort with AUC 0.72 [0.65–0.80] appears in SABCS 2025 mirror coverage but should be re-verified against the abstract text directly before publishing into the registry.
4. NEO press release does not explicitly restate the CLIA/LDT framing; we infer from the CTX coverage that the same regulatory framework applies platform-wide. If the curator wants a NEO-specific CLIA citation, they should fetch the Business Wire release directly.
5. Partners list is sparse — only UChicago Medicine via the SABCS PS3-04-04 abstract is publicly attributable. The Ataraxis homepage lists academic collaborators platform-wide but does not break down by product.

---

## Summary

| Entry id | data_completeness | Peer-reviewed pivotal? | Key gap |
|---|---|---|---|
| `ataraxis-breast-risk` | **full** | Yes — *Diagnostics* (MDPI) 2026, art. 1023 (analytical); arXiv 2410.21256 / JCO 2025 ASCO 549 (clinical) | Clinical-validation numbers themselves are in a preprint + abstract; curator should decide whether `peer_reviewed: true` requires the *clinical* paper to be in a peer-reviewed journal. The Diagnostics 2026 paper alone covers analytical validation but not the headline C-index / HR numbers cited. |
| `ataraxis-breast-ctx` | **stub** | No | No peer-reviewed pivotal publication. All numbers are from company press / product page. Cohort `n_patients` is the development claim; effect sizes and 95% CIs are unpublished. Treat all validation fields as provisional. |
| `ataraxis-breast-neo` | **stub** | No | No peer-reviewed pivotal publication. Subtype AUCs come from the product page; external-validation AUC (0.72 in n=563) comes from a SABCS 2025 abstract via mirror coverage. Verify against direct abstract text. |

**Curator decisions required before applying to data.json:**

1. **For RISK — peer-review threshold.** Should `peer_reviewed: true` be set when the clinical headline numbers are in a preprint and a peer-reviewed analytical-validation companion paper exists, or should it require the clinical headline numbers to be in a peer-reviewed journal? I've set `true` based on the Diagnostics 2026 paper being a peer-reviewed publication for the same test. If your phase-1 batch convention is stricter, downgrade to `false` and keep `data_completeness: partial`.
2. **For RISK — cohort_size accounting.** I've reported 8,161 pooled (development + evaluation) because that's how the arXiv preprint reports it. Vesta-bcg-style convention in v0.1 has been to report only the validation cohort. Curator should decide which to publish and update `unit_note` accordingly.
3. **For CTX and NEO — comparator.** Both products simulate counterfactual treatment scenarios rather than benchmarking against a predicate test. I've used `clinical_outcomes`; if the registry schema's enum needs a finer-grained predictive comparator, this should be revisited.
4. **For all three — partner list semantics.** Decide whether `partners` should be research collaborators (NYU, Karmanos, UChicago, Basel, etc.), deployment customers (currently none publicly named), or both. Vesta-bcg's `partners` are deployment customers; mixing categories would break comparability.
5. **For all three — performing laboratory.** Ataraxis has not publicly named the CLIA laboratory performing these tests. Curator may want to email the company before publishing the entries.
6. **MDPI URL.** WebFetch returned 403; curator should manually open https://www.mdpi.com/2075-4418/16/7/1023 to verify the analytical-validation paper's authors, title, and acceptance-criteria results before publishing.
7. **Business Wire press releases.** Several BW URLs timed out during automated fetching. Curator should reload to confirm the URLs resolve, since they are the canonical primary sources for launch dates and CTX's explicit CLIA/LDT framing.
