# Validation Verification Sheet — Cleanup Batch

**Registry:** OncologyAI Registry (https://oncologyairegistry.org)
**Schema:** v0.2
**Prepared:** 2026-05-31
**Scope:** (1) populate `vesta-risk-stratify` validation; (2) populate `vitara-pancreas-chemopredict` validation; (3) resolve RUO-vs-LDT contradiction on `aiforia-her2`, `mindpeak-pdl1`, `visiopharm-her2-connect`.
**Note:** This is a verification sheet only. `data.json` was NOT modified.

---

## TASK 1 — `vesta-risk-stratify` (Valar Labs "Vesta Bladder Risk Stratify")

### Key finding / corrections to current entry

The current entry's `key_publications[0]` title ("CHAI Biomarkers Validated in High Grade Ta Bladder Cancer") is a **press-release headline**, not the journal article, and the URL points to Business Wire. The actual peer-reviewed publication is:

- **Canonical title:** *Computational Histology Artificial Intelligence (CHAI) Enhances Risk Stratification of High-grade Ta Non–muscle-invasive Bladder Cancer in a Multicenter Cohort: Comparison to Current European Association of Urology and American Urological Association Stratification Schemes*
- **Journal:** European Urology
- **Year:** 2025
- **PMID:** 40514253
- **DOI:** 10.1016/j.eururo.2025.05.035
- **Article type:** Letter (PubMed lists "No abstract available"; methods/results are in the letter body, available open access via PMC).
- **PMC:** PMC12718547

**Two important reality-checks against the press release framing:**

1. **Cohort size is 269 patients, NOT a large external cohort.** This is a single multicenter analysis cohort, none of whom were in the biomarker development set, but there is **no separate independent external-validation cohort** in this paper. Treat `external_validation.performed` as `false` for this specific publication (the validation framing in the BCG paper, `vesta-bcg`, is a different study).
2. **Geography is predominantly US plus one international site (Chile)** — not the multi-country international spread of the BCG paper.

### Sources consulted

| Source | Type | Use |
|---|---|---|
| https://pubmed.ncbi.nlm.nih.gov/40514253/ | Peer-reviewed (PubMed metadata) | Canonical title/journal/year/PMID/DOI |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC12718547/ | Peer-reviewed (full text, open access) | All validation fields |
| https://www.businesswire.com/news/home/20250612200267/en/ | Press | Deployment only — retained in `sources` |

### Proposed `validation` block (JSON)

```json
"validation": {
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 269,
    "n_samples": null,
    "unit_note": "patients with BCG-naïve high-grade Ta NMIBC treated with adjuvant intravesical BCG after TURBT (2004–2024); none from the biomarker development set; this analysis cohort is distinct from the cohort in Valar's BCGPredict paper"
  },
  "n_sites": 13,
  "site_geography": "multi_center_us_plus_one_international",
  "comparator": "guideline_risk_stratification",
  "primary_endpoint": "high_grade_recurrence_free_survival",
  "primary_result": "Primary endpoint high-grade recurrence-free survival (HG-RFS): CHAI biomarker HR 2.23 (95% CI 1.45–3.44; p<0.001). On multivariable adjustment for CHAI, AUA risk (HR 1.93, 95% CI 1.07–3.48; p=0.029) and EAU risk (HR 1.47, 95% CI 0.96–2.23; p=0.074) were not independently significant. Secondary endpoint muscle-invasive bladder cancer progression-free survival (MIBC-PFS): CHAI AI component HR 4.55 (95% CI 1.39–14.92; p=0.012); neither AUA nor EAU risk was significant.",
  "external_validation": {
    "performed": false,
    "cohort_description": "Single multicenter analysis cohort of 269 patients, none of whom were in the biomarker development set; no separate independent external-validation cohort reported in this publication.",
    "result": "CHAI biomarker outperformed EAU and AUA/SUO guideline risk-stratification schemes for both HG-RFS and MIBC-PFS within this cohort."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Computational Histology Artificial Intelligence (CHAI) Enhances Risk Stratification of High-grade Ta Non-muscle-invasive Bladder Cancer in a Multicenter Cohort: Comparison to Current European Association of Urology and American Urological Association Stratification Schemes",
      "journal": "European Urology",
      "year": 2025,
      "url": "https://pubmed.ncbi.nlm.nih.gov/40514253/",
      "pmid": "40514253",
      "doi": "10.1016/j.eururo.2025.05.035",
      "pivotal": true
    }
  ],
  "limitations_noted": "Authors note the study is limited by its retrospective nature and potential for bias or variation in clinical factors across participating sites.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

> **Schema note for curator:** I added `pmid`/`doi` keys to the publication; if the v0.2 `key_publications` object does not allow extra keys, drop them and keep only the PubMed `url`. `site_geography` value `multi_center_us_plus_one_international` and `comparator` value `guideline_risk_stratification` are proposed enums — confirm against the controlled vocabulary used elsewhere (the BCG entry used `multi_center_international` / `clinicopathologic_factors`). If you must reuse existing enums, `multi_center_international` is defensible (Chile is international) and `clinicopathologic_factors` is the closest comparator match, but the more precise label is "EAU/AUA guideline risk groups."

### Field-by-field provenance (verbatim quotes from PMC12718547)

| Field | Proposed value | Verbatim source quote |
|---|---|---|
| study_design | retrospective | "Histology slides stained with hematoxylin and eosin were obtained from consecutive patients with BCG-naïve HG Ta NMIBC who received adjuvant intravesical BCG after TURBT between 2004 and 2024." (retrospective design) + limitations: "This study is limited by its retrospective nature…" |
| cohort_size.n_patients | 269 | "WSIs from 269 patients with HG Ta NMIBC were analyzed, none of whom were from the biomarker development set." |
| n_sites | 13 | Site list in full text: "Vanderbilt (Tennessee), Emory (Georgia), University of Iowa, University of Kentucky, University of Kansas, Moffitt Cancer Center (Florida), Clínica Alemana (Chile), Allina Health (Minnesota), University of Texas Medical Branch, Rutgers Cancer Institute (New Jersey), MD Anderson (Texas), UT Southwestern (Texas), and USC (California)." (13 named sites) |
| site_geography | multi_center_us_plus_one_international | Same site list: 12 US institutions + Clínica Alemana, Chile (1 international). |
| comparator | guideline_risk_stratification | "Comparison to Current European Association of Urology and American Urological Association Stratification Schemes" (title) |
| primary_endpoint | high_grade_recurrence_free_survival | "The primary endpoint was HG recurrence–free survival (HG-RFS); the secondary endpoint was muscle-invasive bladder cancer (MIBC) progression–free survival (MIBC-PFS)." |
| primary_result | (see block) | "HR 2.23, 95% CI 1.45–3.44; p < 0.001" (CHAI, HG-RFS); "HR 1.93, 95% CI 1.07–3.48; p = 0.029" (AUA); "HR 1.47, 95% CI 0.96–2.23; p = 0.074" (EAU); "HR 4.55, 95% CI 1.39–14.92; p = 0.012" (CHAI AI component, MIBC-PFS). |
| external_validation.performed | false | "WSIs from 269 patients … none of whom were from the biomarker development set." (held-out analysis cohort, but no separate dedicated external-validation cohort named) |
| limitations_noted | (see block) | "This study is limited by its retrospective nature and potential for bias or variation in clinical factors across participating sites." |
| fda_summary_url | null | LDT (no FDA submission). Consistent with current `regulatory.fda_status: "LDT"`. |

### Corrected `key_publications` (replacement)

Replace the Business Wire entry with the journal/PubMed entry shown in the JSON block above. **Keep** the Business Wire URL only in the top-level `sources` array (type `"press"`) for deployment context — it must not back any validation number.

---

## TASK 2 — `vitara-pancreas-chemopredict` (Valar Labs "Vitara Pancreas ChemoPredict")

### Key finding / corrections to current entry

Current `key_publications[0]` title ("Pivotal Study Validating AI to Predict Chemotherapy Response…") is the **press-release headline**, URL is Business Wire. Actual peer-reviewed publication:

- **Canonical title:** *Development and Validation of a Computational Histology Artificial Intelligence-Powered Predictive Biomarker for Selection of Chemotherapy in Advanced Pancreatic Cancer*
- **Journal:** Journal of Clinical Oncology (JCO)
- **Year:** 2026
- **PMID:** 41671529
- **DOI:** 10.1200/JCO-25-02199

The press release stated "JCO 2026"; PubMed confirms **2026** (note: the current entry's `year: 2026` is correct; the title and URL need fixing). The JCO full text is paywalled (HTTP 403); the **complete PubMed abstract was available** and is the basis for the numbers below.

### Sources consulted

| Source | Type | Use |
|---|---|---|
| https://pubmed.ncbi.nlm.nih.gov/41671529/ | Peer-reviewed (PubMed abstract) | All validation fields |
| https://ascopubs.org/doi/10.1200/JCO-25-02199 | Peer-reviewed (full text) | Paywalled / HTTP 403 — abstract only used |
| https://www.businesswire.com/news/home/20260210051551/en/ | Press | Deployment only — retained in `sources` |

### Proposed `validation` block (JSON)

```json
"validation": {
  "study_design": "development_and_external_validation",
  "cohort_size": {
    "n_patients": 477,
    "n_samples": null,
    "unit_note": "advanced PDAC patients: 178 in the multi-institutional development cohort + 299 in the independent validation cohort (F-pref n=173, G-pref n=126)"
  },
  "n_sites": null,
  "site_geography": "multi_center_international",
  "comparator": "alternative_chemotherapy_regimen",
  "primary_endpoint": "time_to_next_treatment_or_death_and_overall_survival",
  "primary_result": "In the independent validation cohort (n=299), the GvF biomarker predicted differential benefit. F-pref group (n=173): F-chemo vs G-chemo TNTD 8.6 vs 7.5 months (P=.035); OS 14.4 vs 11.7 months (P=.003). G-pref group (n=126): G-chemo vs F-chemo TNTD 9.6 vs 7.2 months (P=.038); OS 14.3 vs 12.4 months (P=.5, NS). Propensity-score-weighted biomarker-treatment interaction P<.001 (TNTD); P=.005 (OS).",
  "external_validation": {
    "performed": true,
    "cohort_description": "Independent validation cohort of 299 patients drawn from the prospective COMPASS and PanCAN Know Your Tumor studies, separate from the 178-patient development cohort. Biomarker and threshold were locked before validation.",
    "result": "Biomarker-treatment interaction was significant for both TNTD (P<.001) and OS (P=.005) on propensity-score-weighted analysis; the biomarker predicted differential benefit of first-line gemcitabine-based vs fluoropyrimidine-based chemotherapy."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Development and Validation of a Computational Histology Artificial Intelligence-Powered Predictive Biomarker for Selection of Chemotherapy in Advanced Pancreatic Cancer",
      "journal": "Journal of Clinical Oncology",
      "year": 2026,
      "url": "https://pubmed.ncbi.nlm.nih.gov/41671529/",
      "pmid": "41671529",
      "doi": "10.1200/JCO-25-02199",
      "pivotal": true
    }
  ],
  "limitations_noted": "Full-text limitations section not accessible (JCO article paywalled); abstract does not enumerate limitations. Validation cohort assembled from two distinct prospective studies (COMPASS, Know Your Tumor); not a single randomized prospective trial.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

> **`data_completeness: "partial"`** because: (a) `n_sites` could not be confirmed from the abstract (full text paywalled — affiliations list Canada, Ireland, Germany among others, but no explicit site count); (b) the formal limitations section is behind the paywall. Everything else is sourced from the verbatim PubMed abstract. Upgrade to `"full"` if the curator can access the JCO full text for site count + limitations.

> **Schema note:** Proposed enum values `study_design: "development_and_external_validation"`, `comparator: "alternative_chemotherapy_regimen"`, and the compound `primary_endpoint` may not exist in the controlled vocabulary — confirm/snap to existing enums. `site_geography: "multi_center_international"` matches the enum used in `vesta-bcg`.

### Field-by-field provenance (verbatim quotes from PubMed abstract, PMID 41671529)

| Field | Proposed value | Verbatim source quote |
|---|---|---|
| study_design | development_and_external_validation | "In a multi-institutional development cohort, features associated with differential outcomes … produced continuous biomarker scores… The biomarker and threshold were locked. An independent validation cohort from the prospective COMPASS and Know Your Tumor studies assessed differential treatment outcomes…" |
| cohort_size.n_patients | 477 | "Development cohort: 178 patients" + "Validation cohort: 299 patients" (178 + 299 = 477). F-pref n=173 and G-pref n=126 within the validation cohort. |
| n_sites | null | Not stated in abstract; full text paywalled. (Affiliations reference US plus Canada, Ireland, Germany.) |
| site_geography | multi_center_international | "multi-institutional development cohort" + international affiliations (US, Canada, Ireland, Germany). |
| comparator | alternative_chemotherapy_regimen | "predicts benefit from first-line fluoropyrimidine-based (F-chemo) versus gemcitabine-based (G-chemo) regimens" |
| primary_endpoint | TNTD + OS | "An independent validation cohort … assessed differential treatment outcomes by TNTD and overall survival (OS)." |
| primary_result | (see block) | "F-chemo vs G-chemo TNTD: 8.6 vs 7.5 months (P=.035)"; "OS: 14.4 vs 11.7 months (P=.003)"; "G-chemo vs F-chemo TNTD: 9.6 vs 7.2 months (P=.038)"; "OS: 14.3 vs 12.4 months (P=.5)"; "Biomarker-treatment interaction P<.001 (TNTD); P=.005 (OS)." |
| external_validation.performed | true | "An independent validation cohort from the prospective COMPASS and Know Your Tumor studies…" |
| fda_summary_url | null | LDT / early access (no FDA submission). Consistent with current `regulatory.fda_status: "LDT"`, `early_access_available: true`. |

### Corrected `key_publications` (replacement)

Replace the Business Wire entry with the JCO/PubMed entry above. Keep the Business Wire URL in top-level `sources` (type `"press"`) for deployment/early-access context only.

---

## TASK 3 — RUO-vs-LDT contradiction (3 entries)

All three are European digital-pathology image-analysis applications. The verbatim evidence shows the same pattern for each: **CE-IVD / IVDR for clinical diagnostic use in the EU (and UK for Visiopharm), but Research Use Only (RUO) in the US — i.e., no US clinical/LDT offering.** Therefore for all three, the correct triple is `fda_status: "Research Use"`, `ce_marked: true`, **`ldt: false`** (the current `ldt: true` is the error to fix).

### 3.1 `aiforia-her2` — Aiforia Clinical HER2 Breast (Aiforia Technologies)

| Field | Current | Recommended |
|---|---|---|
| fda_status | "Research Use" | **"Research Use"** (keep) |
| ldt | true | **false** (fix) |
| ce_marked | true | **true** (keep) |

Also consider correcting `deployment.primary_markets` from `["EU","US"]` to `["EU"]` (US is RUO-only, not a clinical market).

**Verbatim justification** (https://www.aiforia.com/aiforia-clinical-solutions):
> "All AI models in Aiforia® Breast Cancer Suite are CE-IVD marked for diagnostic use in EU and EEA countries and for Research Use Only (RUO) and Performance Studies Only (PSO) in all other market areas."

> "Only certain Aiforia® Clinical AI models and the Aiforia® Clinical Suite Viewer are CE-IVD marked for diagnostic use in EU and EEA countries. In all other countries, the use is limited to Research Use Only, not for use in diagnostic procedures."

→ The US falls under "all other market areas," so HER2 is RUO in the US, not deployed as a CLIA LDT. **`ldt: false`.**

### 3.2 `mindpeak-pdl1` — Mindpeak PD-L1 Lung (Mindpeak)

| Field | Current | Recommended |
|---|---|---|
| fda_status | "Research Use" | **"Research Use"** (keep) |
| ldt | true | **false** (fix) |
| ce_marked | true | **true** (keep) |

Also consider `deployment.primary_markets` `["EU","US"]` → `["EU"]`.

**Verbatim justification:**
- Product page (https://www.mindpeak.ai/products/mindpeak-lung-nsclc-pd-l1, via search snippet): *"Mindpeak Lung (NSCLC) PD-L1 is intended for Research Use Only, not for use in diagnostic procedures."* The CE-IVD marked variant is the region-of-interest (RoI) product: *"Mindpeak Lung PD-L1 RoI is available in the EU as a CE-IVD marked medical device."*
- Sectra Amplifier Marketplace listing (https://amplifiermarketplace.sectra.com/pathology/mindpeak-lung-nsclc-pd-l1/): the base Lung PD-L1 product carries the designation **"Research only"**; the separate "SP263 RoI" variant carries the "CE" mark.

→ The clinical (CE-IVD) offering is EU-only; the US/general product is RUO. No US CLIA LDT offering evidenced. **`ldt: false`.**

### 3.3 `visiopharm-her2-connect` — HER2-CONNECT (Visiopharm)

| Field | Current | Recommended |
|---|---|---|
| fda_status | "Research Use" | **"Research Use"** (keep) |
| ldt | true | **false** (fix) |
| ce_marked | true | **true** (keep) |

`deployment.primary_markets` is already `["EU"]` — correct, no change needed.

**Verbatim justification:**
- Visiopharm app-center disclaimer (https://visiopharm.com/app-center/app/her2-app-breast-cancer-ivdr/): *"Disclaimer: Unless otherwise stated all products are Research Use Only, not for use in diagnostic procedures."*
- Regulatory summary (per search of Visiopharm materials): *"Visiopharm's precision pathology APPs are IVDR-cleared for use in the EU and UK and designated for research use in other regions."* and *"Visiopharm's CE-IVD APPs are for in vitro diagnostic use in EU/UK. They are not for sale in the USA, where they have respective translational [RUO] APPs available."*

→ HER2-CONNECT is the membrane-connectivity algorithm inside Visiopharm's HER2 app; the clinical CE-IVD/IVDR version is EU/UK only, and the US receives a "translational" RUO version. No US clinical/LDT offering. **`ldt: false`.**

---

## SUMMARY — What the curator must decide

**Task 1 (`vesta-risk-stratify`) — apply with one judgment call:**
- Replace press-release "publication" with European Urology 2025 (PMID 40514253, DOI 10.1016/j.eururo.2025.05.035). Populate validation from PMC12718547. **Decision:** confirm `n_sites` count (I read 13 named sites; verify) and whether to use existing enums (`multi_center_international` / `clinicopathologic_factors`) or add more precise ones. **Key correction:** this paper is 269 patients with NO separate external-validation cohort — do NOT carry over the BCG paper's international-validation framing. `data_completeness: full`.

**Task 2 (`vitara-pancreas-chemopredict`) — apply, marked partial:**
- Replace press release with JCO 2026 (PMID 41671529, DOI 10.1200/JCO-25-02199). Validation populated from the verbatim PubMed abstract; 477 total patients (178 dev + 299 independent validation from COMPASS + Know Your Tumor). **Decision:** `n_sites` and the formal limitations section are behind the JCO paywall — left null and `data_completeness: partial`. If the curator can open the full text, fill site count + limitations and upgrade to `full`.

**Task 3 (all three) — apply the same one-field fix:**
- For `aiforia-her2`, `mindpeak-pdl1`, `visiopharm-her2-connect`: set **`ldt: false`**, keep `fda_status: "Research Use"` and `ce_marked: true`. All three are CE-IVD/IVDR in Europe but explicitly RUO in the US, with no CLIA LDT offering. **Decision:** also recommend trimming `deployment.primary_markets` to drop "US" for `aiforia-her2` and `mindpeak-pdl1` (currently `["EU","US"]`), since US is RUO-only, not a clinical market. `visiopharm-her2-connect` already lists EU only.

**Cross-cutting metadata note:** Both Valar publications had press-release headlines masquerading as journal titles with Business Wire URLs in `key_publications` — same defect class flagged in prior batches. Recommend a sweep of any other entries whose `key_publications[].url` points to businesswire.com / a press domain.
