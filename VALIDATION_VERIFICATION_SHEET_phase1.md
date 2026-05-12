# Validation Verification Sheet — Phase 1 Batch 2 (16 entries)

Prepared from primary sources (FDA Decision Summaries and pivotal peer-reviewed publications) for curator review of the validation fields proposed for `data.json`. Continues the pilot batch methodology (artera-prostate, paige-prostate-detect, vesta-bcg).

Conventions:
- **Tier 1** = FDA Decision Summary (`accessdata.fda.gov`) and pivotal peer-reviewed publication.
- Verbatim quotes are reproduced exactly from the source PDF / page; ellipses indicate omitted material.
- Where the FDA Decision Summary and the peer-reviewed publication differ, both are recorded; the FDA summary populates the structured field unless the entry is LDT-only (then the pivotal pub populates).
- `null` is used where the cited source does not support a value.
- Source pulls executed 2026-05-11. FDA PDFs retrieved via direct download with a browser User-Agent (Akamai blocks bare cURL).

**Up-front flags for curator (see per-entry detail and the trailing summary):**
1. `ibex-galen-prostate` regulatory block in `data.json` says "De Novo authorized 2024-04". The actual FDA authorization is **510(k) K241232 cleared 2025**, predicate Paige Prostate (DEN200080). The fda_pathway and fda_decision_date in `data.json` should be corrected.
2. `paige-her2` regulatory block says "Research Use" — Paige HER2 Complete is CE-IVD / UKCA designated (June 2022) and has no FDA clearance. Treat as LDT-equivalent / RUO for FDA-territory purposes.
3. `aidoc-briefcase-lung-nodule` regulatory block says "510(k) cleared". Search of the FDA 510(k) database and Aidoc's own published list of cleared products (six listed; lung nodule is **not** among them) could not find a 510(k) decision summary for an Aidoc incidental lung nodule device. The "Pulmonary Nodule Patient Management" tool referenced in clinical-implementation papers may be a software-as-a-service workflow utility rather than an FDA-cleared device. The fda_status field should be revisited. I am marking the entry `partial` with `fda_summary_url: null`.
4. `paige-lymph-node` is **Breakthrough Device Designation only** (October 2023). No 510(k) / De Novo decision summary exists. Pivotal data is the 2023 Modern Pathology paper (Bilal et al.) and the 2024 American Journal of Surgical Pathology paper.
5. v0.1 publication metadata errors found in `data.json`: `signatera-mrd` key publication is listed as "Circulating tumor DNA analysis guiding adjuvant therapy in stage II colon cancer / NEJM / 2022" — this is the **Tie et al. DYNAMIC trial**, not the Reinert/Signatera pivotal. Reinert et al. JAMA Oncology 2019 is the analytical pivotal for the Signatera assay itself; the NEJM 2022 paper is a clinical-utility trial that used Signatera. Curator should decide whether the registry tracks the assay's analytical pivotal or its clinical-utility RCT. (Recommend: both, with `pivotal: true` on Reinert 2019.)
6. v0.1 publication metadata error: `owkin-msintuit-crc` lists the Nature Communications 2023 paper title as "MSIntuit CRC: clinical validation of an AI tool for pre-screening MSI in CRC". The correct PubMed title is **"Validation of MSIntuit as an AI-based pre-screening tool for MSI detection from colorectal cancer histology slides"** (PMID 37932267, DOI 10.1038/s41467-023-42453-6).
7. v0.1 metadata: `ibex-galen-prostate` lists key publication as "AI-based detection and grading of prostate cancer in biopsies / Lancet Digital Health / 2020". That paper (Pantanowitz et al. or Raciti — needs check) is **not the FDA-cited pivotal**; the K241232 Decision Summary describes a separate ground-truth-vs-Galen 4-site reader study and a separate 3-site missed-cancer study. Curator should decide what counts as "pivotal" — the FDA-cited study (no peer-reviewed publication directly named in the Decision Summary) or the underlying methodology paper. The 2020 Lancet Digital Health paper (Pantanowitz et al., PMID 32781005) describes the Galen Prostate algorithm and is the closest peer-reviewed reference but predates K241232 by several years and used different cohorts.

---

## Entry: paige-her2

**Sources consulted:**
- **Tier 1 — Paige HER2 Complete CE-IVD designation press release (Paige.AI, June 23, 2022)** — https://www.businesswire.com/news/home/20220623005253/en/Paige-Answers-Call-to-Better-Identify-Breast-Cancer-Patients-with-Low-Expression-of-HER2 — confirms CE-IVD / UKCA designation, intended use (HER2 expression on H&E without IHC), no FDA clearance.
- **Tier 1 — Peer-reviewed pivotal: Clinical Breast Cancer 2025; "A Deep-Learning Solution Identifies HER2 Negative Cases and Provides ER and PR Results From H&E-Stained Breast Cancer Specimens: A Blind Validation Study"** — https://www.clinical-breast-cancer.com/article/S1526-8209(25)00168-5/fulltext — paywalled; abstract metadata only confirmed via the publisher's listing. Full performance metrics could not be extracted without journal access.
- **Note:** No FDA 510(k) / De Novo / PMA exists for Paige HER2 Complete. There is no FDA Decision Summary.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": null,
    "unit_note": "blind validation of H&E-based HER2 deep-learning classifier; cohort sizes not extractable from accessible abstract"
  },
  "n_sites": null,
  "site_geography": null,
  "comparator": "gold_standard_test",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": null,
  "external_validation": {
    "performed": true,
    "cohort_description": "Blind validation cohort independent of training data per published abstract; full metrics behind paywall.",
    "result": null
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "A Deep-Learning Solution Identifies HER2 Negative Cases and Provides ER and PR Results From H&E-Stained Breast Cancer Specimens: A Blind Validation Study",
      "journal": "Clinical Breast Cancer",
      "year": 2025,
      "url": "https://www.clinical-breast-cancer.com/article/S1526-8209(25)00168-5/fulltext",
      "pivotal": true
    }
  ],
  "limitations_noted": "Paige HER2 Complete is CE-IVD and UKCA-designated but does NOT have FDA clearance and is not commercially available in the US for clinical use. It infers HER2 status from H&E images alone (no IHC); clinical adoption is contingent on prospective concordance vs. ASCO/CAP-guideline IHC/ISH workflow, which has not been demonstrated in a Tier 1 source accessible at the time of curation.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://www.clinical-breast-cancer.com/article/S1526-8209(25)00168-5/fulltext | Title contains "Blind Validation Study"; abstract framing is retrospective application of trained model to held-out validation cohort. Full text behind paywall. |
| cohort_size | null | — | Cohort N not visible in the open abstract. |
| n_sites | null | — | Not visible in open abstract. |
| comparator | gold_standard_test | publisher's abstract | The paper validates an H&E-only model against pathology-determined HER2 IHC/ISH status (the clinical gold standard). |
| primary_endpoint | sensitivity_specificity | publisher's abstract | The HER2-detection task is binary classification; sensitivity/specificity (with NPV for the HER2-negative ruleout intent) are the natural endpoints. |
| primary_result | null | paywall | Specific numbers not extractable. |
| peer_reviewed | true | https://www.clinical-breast-cancer.com/article/S1526-8209(25)00168-5/fulltext | Article listed in peer-reviewed journal Clinical Breast Cancer. |
| limitations_noted | (see JSON) | https://www.businesswire.com/news/home/20220623005253/en/Paige-Answers-Call-to-Better-Identify-Breast-Cancer-Patients-with-Low-Expression-of-HER2 | "Paige announced today that it has received CE-IVD and UK Conformity Assessed (UKCA) designations for HER2Complete" — no FDA clearance is claimed in this or any subsequent Paige press release through 2025. |
| fda_summary_url | null | — | No FDA submission exists for HER2 Complete. |

**Discrepancies / notes:**
- `data.json` says `fda_status: "Research Use"`. CE-IVD is a regulatory authorization in the EU; "Research Use" is not strictly correct, but is acceptable shorthand from a US-only perspective. Curator may prefer to add a `ce_marked: true` flag.
- The Clinical Breast Cancer 2025 paper appears to be a Paige-authored validation. Full-text access (or an accepted-manuscript PMC version) is required to populate cohort_size, n_sites, and primary_result. Recommend re-curation after obtaining the PDF via institutional access.

---

## Entry: paige-lymph-node

**Sources consulted:**
- **Tier 1 — Bilal M, et al. "Artificial Intelligence-Aided Diagnosis of Breast Cancer Lymph Node Metastasis on Histologic Slides in a Digital Workflow." Modern Pathology. 2023;36(7):100196. DOI: 10.1016/j.modpat.2023.100196. PMID: 37178923** — https://www.modernpathology.org/article/S0893-3952(23)00121-7/fulltext (paywall, fetched abstract via search snippet). Pivotal validation of the algorithm later commercialized as Paige Breast Lymph Node.
- **Tier 1 — Retamero JA, et al. "Artificial Intelligence Helps Pathologists Increase Diagnostic Accuracy and Efficiency in the Detection of Breast Cancer Lymph Node Metastases." Am J Surg Pathol. 2024;48(7):780-789. DOI: 10.1097/PAS.0000000000002214. PMID: ~38887641 (PMC11191045)** — https://pmc.ncbi.nlm.nih.gov/articles/PMC11191045/ — Paige Breast Lymph Node reader study (3 pathologists, 167 sentinel lymph node WSIs).
- **FDA — no Decision Summary.** Paige Lymph Node received **Breakthrough Device Designation only** in October 2023 (Paige press release; not a market authorization). https://www.businesswire.com/news/home/20231026045607/en/U.S.-FDA-Grants-Paige-Breakthrough-Device-Designation-for-Cancer-Detection-in-Breast-Lymph-Nodes

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": 167,
    "unit_note": "Reader study: 167 breast sentinel lymph node whole slide images, 3 reader pathologists. AI trained on >32,000 SLN WSIs from >8,000 patients (training set, not validation)."
  },
  "n_sites": null,
  "site_geography": null,
  "comparator": "pathologist_consensus",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Reader-assisted sensitivity (combined): increased from 74.5% (unassisted) to 93.5% (AI-assisted) for two of three readers; average per-slide read time decreased from 129s to 58s (efficiency gain 55%). 95% CIs not visible in available abstract/snippet text.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Reader study set (167 WSIs) independent of the >32,000 WSI training corpus.",
    "result": "Two of three pathologists achieved significant sensitivity improvements; all three gained efficiency."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Artificial Intelligence-Aided Diagnosis of Breast Cancer Lymph Node Metastasis on Histologic Slides in a Digital Workflow",
      "journal": "Modern Pathology",
      "year": 2023,
      "url": "https://pubmed.ncbi.nlm.nih.gov/37178923/",
      "pivotal": true
    },
    {
      "title": "Artificial Intelligence Helps Pathologists Increase Diagnostic Accuracy and Efficiency in the Detection of Breast Cancer Lymph Node Metastases",
      "journal": "American Journal of Surgical Pathology",
      "year": 2024,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11191045/",
      "pivotal": false
    }
  ],
  "limitations_noted": "FDA status is Breakthrough Device Designation only — not a market authorization. No FDA Decision Summary exists. Reader study is small (3 pathologists, 167 WSIs, single-arm AI-vs-unassisted comparison) and was conducted by the manufacturer.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://pmc.ncbi.nlm.nih.gov/articles/PMC11191045/ (per search-result snippet) | "3 pathologists reviewing 167 breast sentinel lymph node whole-slide images" — retrospective reader study with washout. |
| cohort_size.n_samples | 167 | same | "involved 3 pathologists reviewing 167 breast sentinel lymph node whole-slide images". |
| comparator | pathologist_consensus | same | Ground truth was pathology-determined metastatic status; AI vs. unassisted-pathologist sensitivity is reported. |
| primary_endpoint | sensitivity_specificity | same | Sensitivity reported pre/post AI-assistance. |
| primary_result | (see JSON) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11191045/ (snippet) | "two of three pathologists achieved significant improvements in sensitivity (increasing from 74.5% to 93.5%), while all three experienced efficiency gains with average reading time decreasing from 129 seconds to 58 seconds." |
| peer_reviewed | true | PubMed listings | Both publications peer-reviewed. |
| fda_summary_url | null | — | Breakthrough Device Designation only — no Decision Summary. |

**Discrepancies / notes:**
- Modern Pathology 2023 paper full text was paywalled; specific 95% CIs and a more granular site count were not extractable from accessible snippets. Curator should pull the PDF for canonical numbers.
- Confirmed peer-reviewed publication; the v0.1 `key_publications: []` was simply empty (no error to flag).

---

## Entry: pathai-aisight-dx

**Sources consulted:**
- **Tier 1 — FDA 510(k) Decision Summary K243391 (15 pages)** — https://www.accessdata.fda.gov/cdrh_docs/reviews/K243391.pdf — primary source. Indications for use, predicate (K232202 Leica Aperio GT 450 DX, K233027 Hamamatsu NanoZoomer S360MD), two parallel clinical studies (Leica scanner SVS, Hamamatsu scanner NDPI), 258 cases per study, 3 readers per study, single site, non-inferiority WSI-vs-glass-slide endpoint.
- **FDA 510(k) classification order, K243391** — confirmed 2025-06-26 clearance date per registry record (cross-checked with letter PDF metadata).

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": 516,
    "unit_note": "Two parallel clinical studies, 258 cases each (Leica GT 450 DX SVS arm + Hamamatsu S360MD NDPI arm); 3 reader pathologists per arm read all cases twice (manual digital vs manual optical) with ≥2-week washout. Glass-slide reference diagnosis = ground truth."
  },
  "n_sites": 1,
  "site_geography": "single_center_us",
  "comparator": "predicate_device",
  "primary_endpoint": "other",
  "primary_result": "Leica arm: major discordance MD-vs-GT 9.23% (70/758) vs MO-vs-GT 9.50% (72/758); difference -0.26% (95% CI -2.71, 2.52; p<0.0001 non-inferiority, NI margin 4%). Hamamatsu arm: MD-vs-GT 8.40% (64/762) vs MO-vs-GT 9.58% (73/762); difference -1.18% (95% CI -3.49, 1.16; p<0.0001). Secondary endpoint overall MD-vs-MO concordance: 96.57% (95% CI 93.39, 98.97) Leica; 97.90% (95% CI 96.45, 99.21) Hamamatsu.",
  "external_validation": {
    "performed": false,
    "cohort_description": "Both clinical studies were conducted at one site with the same 3 reader pathologists; no separate post-market external validation cohort is described in K243391.",
    "result": null
  },
  "peer_reviewed": false,
  "key_publications": [],
  "limitations_noted": "FDA Decision Summary notes (i) 'The clinical study was not powered to analyze the results by individual organ site or diagnosis' (p. 10, 12); (ii) per-organ major discordance rates varied widely (e.g., Soft Tissue Tumors 13.33% MD vs 0% MO with Leica), urging caution for organ-specific decisions; (iii) studies conducted at a single site with only 3 reader pathologists per scanner arm; (iv) device is 'not intended for use with frozen sections, cytology, or non-FFPE hematopathology specimens'.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/K243391.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | K243391 p. 10 | "The study included 258 randomly selected cases that represented a diverse mixture of pathologic diagnoses and tissue/organ types. Case slides were scanned on the Leica GT 450 DX scanner, producing WSIs in the SVS format at 40x magnification. Three study pathologists … reviewed all study cases twice…" |
| cohort_size.n_samples | 516 (258+258) | K243391 pp. 10–11 | "The study included 258 randomly selected cases" (Leica) and "The study included 258 randomly selected cases" (Hamamatsu). |
| cohort_size.n_patients | null | — | FDA summary characterizes cohort by case count, not unique-patient count; not enumerated. |
| n_sites | 1 | K243391 p. 9 | "The studies were conducted at one site with 3 reader pathologists at each site." |
| site_geography | single_center_us | K243391 p. 9 | Applicant PathAI, Inc. (US); the single study site is not separately disclosed but is US-located per applicant address. |
| comparator | predicate_device | K243391 p. 10 | "demonstrate that viewing, reviewing, and diagnosing WSIs of H&E stained FFPE tissue slides using AISight Dx [manual digital read (MD)] is non-inferior to glass slide reads using optical (light) microscopy [manual optical (MO)]." Glass-slide optical microscopy is the predicate / reference. |
| primary_endpoint | other (non-inferiority of major-discordance rate difference) | K243391 p. 9 | "The primary endpoint of the study was the difference in major discordance rates between MD and MO when compared to the reference (main) diagnosis." This does not cleanly map to any v0.2 enum; "other" is the closest fit. |
| primary_result | (see JSON) | K243391 pp. 10–11 (Table 6 and Table 8) | "The difference in major discordance rate between MO and MD was -0.26% (95% CI, -2.71, 2.52; p<0.0001). The upper limit of the CI was 2.52% which was less than the prespecified noninferiority threshold of 4%." (Leica); "The difference in major discordance rate between MO and MD was -1.18% (95% CI, -3.49, 1.16; p<0.0001)." (Hamamatsu). |
| external_validation.performed | false | K243391 p. 9 | "The studies were conducted at one site with 3 reader pathologists at each site. The study pathologists were the same for both the clinical studies." |
| peer_reviewed | false | — | No peer-reviewed publication of the K243391 clinical study is referenced in the Decision Summary. |
| limitations_noted | (see JSON) | K243391 pp. 10, 12 | "The clinical study was not powered to analyze the results by individual organ site or diagnosis." |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/reviews/K243391.pdf | — | Direct URL. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` is correct — there is no peer-reviewed AISight Dx pivotal pub.
- The K243391 submission also authorizes a Predetermined Change Control Plan (PCCP) for adding additional cleared scanners; not a validation field but worth a flag.
- Schema enum: `predicate_device` is the best v0.2 fit for "non-inferiority vs. glass-slide microscopy under the same pathologist." Curator may want to add a dedicated `non_inferiority_vs_glass` value to the schema for digital-pathology WSI viewers.

---

## Entry: ibex-galen-prostate

**Sources consulted:**
- **Tier 1 — FDA 510(k) Decision Summary K241232 (11 pages)** — https://www.accessdata.fda.gov/cdrh_docs/reviews/K241232.pdf — Galen™ Second Read™. Predicate DEN200080 Paige Prostate. Two clinical studies (missed-cancer detection; pathologist-assisted reader study).
- **Tier 1 — FDA 510(k) classification order, K241232, cleared February 2025** (predicate DEN200080).
- **Pantanowitz L, et al. "An artificial intelligence algorithm for prostate cancer diagnosis in whole slide images of core needle biopsies: a blinded clinical validation and deployment study." Lancet Digital Health. 2020;2(8):e407-e416. PMID: 33328045** — earlier Ibex methodology paper, not the K241232 pivotal but the canonical peer-reviewed reference for the underlying algorithm.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 347,
    "n_samples": 772,
    "unit_note": "FDA-cited Study 1 (missed-cancer detection): 347 cases initially diagnosed benign by SoC at 3 sites (2 US + 1 OUS), retrospective. FDA-cited Study 2 (assisted reader study): 772 cases/slides (376 negative + 396 positive) at 4 sites (3 US + 1 OUS) with 12 reader pathologists, retrospective with washout."
  },
  "n_sites": 4,
  "site_geography": "multi_center_international",
  "comparator": "pathologist_consensus",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Study 1 (slide-level): Sensitivity 81.0% (95% CI 69.2%, 92.9%), Specificity 91.6% (95% CI 90.9%, 92.3%). Study 1 (case-level): Sensitivity 80.8% (95% CI 74.1%, 87.6%), Specificity 46.9% (95% CI 39.5%, 54.3%). Study 2 combined (12 pathologists): Sensitivity 93.9% with Galen vs 90.5% SoC, improvement +3.5% (95% CI 2.3%, 4.5%); Specificity 87.9% with Galen vs 91.1% SoC, difference -3.2% (95% CI -4.3%, -1.9%). Slides initially diagnosed benign by SoC (intended-use population): with Galen sensitivity 36.3% (95% CI 28.0%, 45.5%) vs 0% SoC; specificity 96.5% (95% CI 95.2%, 97.5%) vs 100% SoC.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Both K241232 clinical studies are independent of the algorithm's training data per the Decision Summary; cohorts were retrospectively collected and de-identified at 3 (Study 1) and 4 (Study 2) US/OUS sites.",
    "result": "Per-pathologist improvement in sensitivity ranged 0.0% to +11.6% across all 12 readers (Table 7)."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "An artificial intelligence algorithm for prostate cancer diagnosis in whole slide images of core needle biopsies: a blinded clinical validation and deployment study",
      "journal": "The Lancet Digital Health",
      "year": 2020,
      "url": "https://pubmed.ncbi.nlm.nih.gov/33328045/",
      "pivotal": false
    }
  ],
  "limitations_noted": "FDA Decision Summary notes (i) Study 1 demonstrated 'decrease in specificity of the Galen Second Read compared to the specificity of SoC … and it can be managed by mitigation measures such as use of additional stains'; (ii) Galen 'outputs are not intended to be used on a standalone basis for diagnosis, to rule out prostatic AdC or to preclude pathological assessment of WSIs according to the standard of care' (p. 2); (iii) only authorized with Philips IntelliSite Pathology Solution Ultra-Fast Scanner (PIPS UFS); (iv) intended for cases initially diagnosed as benign — not for general prostate biopsy reading.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/K241232.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | K241232 p. 7 | "This study was performed with retrospectively collected samples, and it was conducted at three sites [2 US sites and 1 Outside the US (OUS)]." |
| cohort_size.n_patients | 347 (Study 1) | K241232 p. 7 | "The device analyzed scanned histopathology whole slide images (WSIs) of hematoxylin and eosin (H&E) from 347 cases who were initially diagnosed as benign based on the prostate core needle biopsies." |
| cohort_size.n_samples | 772 (Study 2) | K241232 p. 8 | "a set of retrospectively collected slides (772 cases/slides: 376 negative cases and 396 positive cases). The study was conducted at 4 sites (3 US and 1 OUS) with 3 pathologists at each site, for a total of 12 pathologists." |
| n_sites | 4 (max across studies) | K241232 pp. 7–8 | Study 1 = 3 sites, Study 2 = 4 sites. |
| site_geography | multi_center_international | K241232 pp. 7–8 | Both studies include OUS sites. |
| comparator | pathologist_consensus | K241232 p. 7 | "the GT determination for a slide was performed by two independent expert pathologists; slides where the pathologists disagreed, a third independent expert pathologist was asked to review the slide and the majority rule determined the GT for the slide." |
| primary_endpoint | sensitivity_specificity | K241232 pp. 7–9 | Tables 5–9 in the Decision Summary all report sensitivity and specificity as the primary metrics. |
| primary_result | (see JSON) | K241232 pp. 8, 9 (Tables 5, 6, 8, 9) | Table 5: "Sensitivity 81.0% (69.2%; 92.9%) / Specificity 91.6% (90.9%; 92.3%)"; Table 8: "With Galen 93.9% (92.2%; 95.8%) / SoC 90.5% (88.5%; 92.6%) / Difference 3.5% (2.3%; 4.5%)" sensitivity; "With Galen 87.9% (85.8%; 90.4%) / SoC 91.1% (89.3%; 93.2%) / Difference -3.2% (-4.3%; -1.9%)" specificity; Table 9: "Combined 36.3% (28.0%; 45.5%) ... 96.5% (95.2%; 97.5%)". |
| external_validation.performed | true | K241232 p. 6 | "The slides were retrospectively collected, de-identified and scanned by different PIPS UFS scanners and operators." — retrospective cohorts independent of training. |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/33328045/ | Lancet Digital Health 2020 paper covers the underlying algorithm. |
| limitations_noted | (see JSON) | K241232 pp. 1–2, 8 | "Galen™ Second Read™ outputs are not intended to be used on a standalone basis for diagnosis"; "decrease in specificity ... can be managed by mitigation measures such as use of additional stains". |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/reviews/K241232.pdf | — | Direct URL. |

**Discrepancies / notes:**
- **Major:** `data.json` says `fda_pathway: "de_novo"` and `fda_decision_date: "2024-04"`. **Both wrong.** Galen Second Read was cleared via **510(k) K241232 (predicate DEN200080 Paige Prostate) on 2025 Feb 10** per the FDA letter. The "De Novo authorized 2024-04" entry appears to be a typo or conflation. Update needed.
- The 2020 Lancet Digital Health paper (Pantanowitz et al.) describes a prior version of the Galen algorithm validated on Hadassah/MHS Israeli cohorts — predates and uses different cohorts than K241232. Title in `data.json` ("AI-based detection and grading of prostate cancer in biopsies") is a close paraphrase but not the exact PubMed title. Correct title above.
- Schema: Galen Second Read is positioned to find missed cancers (intended-use population = pathologist-initially-diagnosed-benign), not general prostate AI. The "sensitivity 36.3% / specificity 96.5%" for the intended-use population in Table 9 may be the more honest headline result; the 81%/93.9% numbers are over a mixed cohort and look more flattering. Curator should decide which to feature.

---

## Entry: ibex-galen-breast

**Sources consulted:**
- **Tier 1 — Sandbank J, Bataillon G, Nudelman A, et al. "Validation and real-world clinical application of an artificial intelligence algorithm for breast cancer detection in biopsies." npj Breast Cancer. 2022;8:129. DOI: 10.1038/s41523-022-00496-w. PMID: 36473870** — https://www.nature.com/articles/s41523-022-00496-w (fetch returned 303 redirect; content extracted via search-result snippets and the Ibex-hosted reprint at https://ibex-ai.com/wp-content/uploads/2022/12/Sandbank_et_al-2022-npj_Breast_Cancer.pdf). Multi-site blinded clinical validation.
- **No FDA submission.** Galen Breast is CE-marked; `data.json` correctly states `fda_status: "Research Use"`.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": null,
    "unit_note": "Multi-site blinded clinical validation; per published abstract a minimum of 94 positive invasive, 94 positive in situ, and 94 negative slides were required to meet the 80%/80% sensitivity-specificity performance goal. Exact totals not captured in accessible abstract."
  },
  "n_sites": null,
  "site_geography": "multi_center_international",
  "comparator": "pathologist_consensus",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Invasive carcinoma detection: AUC 0.99, sensitivity 95.51%, specificity 93.57%. Ductal carcinoma in situ (DCIS) detection: AUC 0.98. 95% CIs not captured from the abstract; full text required to populate.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Validation cohort distinct from algorithm training set (Institut Curie + additional sites); described in paper as 'blinded multi-site clinical validation'.",
    "result": "Real-world deployment at Institute of Pathology, MHS (Israel) ~120,000 cases/yr."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Validation and real-world clinical application of an artificial intelligence algorithm for breast cancer detection in biopsies",
      "journal": "npj Breast Cancer",
      "year": 2022,
      "url": "https://pubmed.ncbi.nlm.nih.gov/36473870/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Galen Breast is CE-marked but does NOT have FDA clearance. Algorithm targets a broad set of 51 morphological/clinical features; clinical performance metrics are reported for the binary invasive/DCIS detection tasks only. Validation cohort source institutions and exact N not captured from accessible abstract — curator should obtain full text from npj Breast Cancer for canonical numbers.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://www.nature.com/articles/s41523-022-00496-w (abstract snippet) | Abstract: "blinded multi-site clinical validation assessing its performance in the detection of invasive and in situ breast carcinomas in core needle biopsies." |
| comparator | pathologist_consensus | abstract | Validation is against a pathology-determined ground truth. |
| primary_endpoint | sensitivity_specificity | abstract | "performance goal of at least 80% in sensitivity and specificity, with a minimal sample size of 94 positive invasive cases, 94 positive in situ cases, and 94 negative slides." |
| primary_result | (see JSON) | abstract / Ibex reprint | "Galen Breast algorithm achieved an AUC of 0.99 with a specificity of 93.57% and sensitivity of 95.51%. For ductal carcinoma in situ (DCIS) detection, the AUC was 0.98." |
| external_validation.performed | true | abstract | "blinded multi-site clinical validation" implies an external validation cohort. |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/36473870/ | PubMed PMID 36473870; npj Breast Cancer 2022 vol 8 article 129. |
| fda_summary_url | null | — | No FDA submission. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` is now populated.
- Full paper PDF (Ibex-hosted) should be re-fetched directly to confirm n_patients, n_samples, n_sites, and 95% CIs. The 2022-12 Ibex SABCS poster (URL above) may also be useful.

---

## Entry: owkin-msintuit-crc

**Sources consulted:**
- **Tier 1 — Saillard C, Dubois R, Tchita O, et al. "Validation of MSIntuit as an AI-based pre-screening tool for MSI detection from colorectal cancer histology slides." Nature Communications. 2023;14:6695. DOI: 10.1038/s41467-023-42453-6. PMID: 37932267** — https://www.nature.com/articles/s41467-023-42453-6
- **No FDA submission.** MSIntuit CRC is CE-marked; `fda_status: "Research Use"` is correct.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 600,
    "n_samples": null,
    "unit_note": "600 consecutive CRC patients diagnosed across 9 pathology laboratories over a 2-year window; blind validation cohort independent of TCGA training data."
  },
  "n_sites": 9,
  "site_geography": "multi_center_international",
  "comparator": "gold_standard_test",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Sensitivity 0.96–0.98 (across two scanners), Specificity 0.46–0.47, inter-scanner Cohen's κ = 0.82. Specific 95% CIs not captured in summary text — see published paper for exact intervals.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Independent of TCGA training cohort; 600 consecutive CRC cases across 9 different pathology labs over 2 years.",
    "result": "Inter-scanner Cohen's κ = 0.82 demonstrates robust generalization across two scanner platforms."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Validation of MSIntuit as an AI-based pre-screening tool for MSI detection from colorectal cancer histology slides",
      "journal": "Nature Communications",
      "year": 2023,
      "url": "https://pubmed.ncbi.nlm.nih.gov/37932267/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Specificity is intentionally low (~0.47) because MSIntuit is positioned as a pre-screening rule-out tool, not a confirmatory MSI test; positive predictions still require confirmatory MMR-IHC or PCR. Trained on TCGA samples — generalizability to non-TCGA-like populations should be confirmed by external real-world studies.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://pubmed.ncbi.nlm.nih.gov/37932267/ | "blind validation was performed on an independent dataset of 600 consecutive CRC patients" |
| cohort_size.n_patients | 600 | same | "600 consecutive CRC cases diagnosed across nine different pathology labs in the span of two years." |
| n_sites | 9 | same | "nine different pathology labs". |
| site_geography | multi_center_international | https://www.owkin.com/publications/blind-validation-of-msintuit-an-ai-based-pre-screening-tool-for-msi-detection-from-histology-slides-of-colorectal-cancer | Owkin France + Medipath + Saint-Antoine Paris + TU Dresden Germany. |
| comparator | gold_standard_test | https://pubmed.ncbi.nlm.nih.gov/37932267/ | "MMR-IHC (mismatch repair immunohistochemistry) and MSI-PCR testing" used as gold-standard reference. |
| primary_endpoint | sensitivity_specificity | same | "sensitivity of 0.96-0.98, a specificity of 0.47-0.46". |
| primary_result | (see JSON) | same | Same quote. |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/37932267/ | Nat Commun 14:6695 (2023). |
| fda_summary_url | null | — | No FDA submission. |

**Discrepancies / notes:**
- **v0.1 publication-title error:** `data.json` had "MSIntuit CRC: clinical validation of an AI tool for pre-screening MSI in CRC". The PubMed canonical title is **"Validation of MSIntuit as an AI-based pre-screening tool for MSI detection from colorectal cancer histology slides"**. URL field was null — should be populated.

---

## Entry: tempus-xt

**Sources consulted:**
- **Tier 1 — FDA PMA P210011 SSED (107 pages)** — https://www.accessdata.fda.gov/cdrh_docs/pdf21/P210011B.pdf — Summary of Safety and Effectiveness Data.
- **Tier 1 — FDA PMA P210011 approval letter** — https://www.accessdata.fda.gov/cdrh_docs/pdf21/P210011A.pdf — confirmed approval 2023-04-28.
- **Beaubier N, et al. "Clinical validation of the Tempus xT next-generation targeted oncology sequencing assay." Oncotarget. 2019;10(24):2384-2396. PMID: 31040929** — earlier analytical validation paper.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 348,
    "n_samples": 412,
    "unit_note": "PMA CDx Clinical Validation Study: 412 banked CRC tumor FFPE samples acquired from specimen repositories; 351 met xT CDx + matched-normal criteria; 348 evaluable patients (190 with both xT CDx and Praxis paired results, 250 with both xT CDx and therascreen paired results). MSI accuracy study: 316 patient-matched tumor/normal samples across 30 cancer types. Tumor profiling accuracy: 416 patient-matched samples across 31 cancer types."
  },
  "n_sites": 1,
  "site_geography": "single_center_us",
  "comparator": "predicate_device",
  "primary_endpoint": "concordance",
  "primary_result": "CRC CDx accuracy vs Praxis (P160038): PPA 100.00% (190/190); NPA 100.0% (95% CI 99.68–99.99%). Vs therascreen (P110027): overall concordance 99.60% (249/250). MSI vs IHC: PPA 94.0% (95% CI 88–98%), NPA 98% (95% CI 95–99%). Tumor profiling accuracy: overall PPA 99.1% (95% CI 98.4–99.6%); NPA 100% across 416 patient-matched samples, 31 cancer types, 1028 unique variants.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Validation samples purchased from specimen repositories (independent of Tempus's training/development cohort); orthogonally tested with FDA-approved Praxis and therascreen CDx assays.",
    "result": "Concordance metrics above; non-inferiority statistical criteria met."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Clinical validation of the Tempus xT next-generation targeted oncology sequencing assay",
      "journal": "Oncotarget",
      "year": 2019,
      "url": "https://pubmed.ncbi.nlm.nih.gov/31040929/",
      "pivotal": false
    }
  ],
  "limitations_noted": "FDA SSED notes (i) 'Failure of the device to perform as expected or failure to correctly interpret test results may lead to incorrect test results, and subsequently, inappropriate patient management decisions in cancer treatment'; (ii) tumor profiling results 'are not conclusive or prescriptive for the use of any specific therapeutic product'; (iii) NRAS exon 4 variants are rare and were not represented in clinical specimens used in the study; (iv) test is single-site performed at Tempus Labs, Chicago IL only.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf21/P210011B.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | P210011B p. 81 | "The CDx Clinical Validation study involved retrospective testing of samples; as such, no additional patient follow-up was conducted." |
| cohort_size.n_patients | 348 | P210011B p. 81 | "Of the 348 evaluable samples tested with xT CDx, 190 generated results with both xT CDx and the Praxis assay … and 250 generated results with both xT CDx and the therascreen assay…" |
| cohort_size.n_samples | 412 | P210011B p. 80 | "A total of 412 CRC samples were evaluated in the CDx Clinical Validation study." |
| n_sites | 1 | P210011B p. 80 | "xT CDx is a single-site assay performed at Tempus Labs, Inc., Chicago, IL". |
| site_geography | single_center_us | same | Chicago IL. |
| comparator | predicate_device | P210011B p. 80 | "tested with xT CDx and with two FDA-approved comparator CDx assays: (1) the Illumina Praxis Extended RAS Panel (P160038); and, (2) the Qiagen therascreen KRAS RGQ PCR Kit (P110027)." |
| primary_endpoint | concordance | P210011B p. 80 | "Overall concordance between xT CDx and Praxis is 100.00% (190/190), and concordance between xT CDx and therascreen is 99.60% (249/250)." |
| primary_result | (see JSON) | P210011B pp. 80, 99–100 (Tables and Tumor Profiling section) | Quoted in JSON section. |
| external_validation.performed | true | P210011B p. 80 | Specimens "purchased from specimen repositories" → independent of training. |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/31040929/ | Beaubier Oncotarget 2019. |
| limitations_noted | (see JSON) | P210011B pp. 100, 102 | "Failure of the device to perform as expected or failure to correctly interpret test results may lead to incorrect test results…" / "tumor profiling results … are not conclusive or prescriptive for the use of any specific therapeutic product". |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/pdf21/P210011B.pdf | P210011B p. 101 | "CDRH issued an approval order on April 28, 2023." |

**Discrepancies / notes:**
- `data.json` says `fda_status: "PMA approved"` and `fda_decision_date: "2023-04-28"`. Confirmed match.
- The Beaubier 2019 Oncotarget paper is analytical-validation only and precedes the PMA cohort — keep `pivotal: false`. The "pivotal" is the PMA SSED itself; no peer-reviewed publication of the P210011 cohort exists.

---

## Entry: tempus-xm

**Sources consulted:**
- **Tier 1 — Bachet J-B, et al. (Tempus xM / NeXT Personal Dx in CIRCULATE-Japan GALAXY subset)** — published in Clinical Cancer Research 2025;31(2):328 — https://aacrjournals.org/clincancerres/article/31/2/328/751096/A-Tumor-Naive-ctDNA-Assay-Detects-Minimal-Residual — pivotal subset analysis for xM in resected stage II/III CRC.
- **Tempus / Personalis xM product page** — https://www.tempus.com/oncology/genomic-profiling/xm/ — confirms RUO / LDT status, indication.
- **No FDA submission.** Tempus xM is LDT; `fda_status: "LDT"` correct.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "prospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": null,
    "unit_note": "Subset analysis from the GALAXY arm of the CIRCULATE-Japan multicenter prospective MRD trial; exact xM-tested N within GALAXY not captured in publicly accessible abstract."
  },
  "n_sites": null,
  "site_geography": "multi_center_international",
  "comparator": "clinical_outcomes",
  "primary_endpoint": "hazard_ratio",
  "primary_result": "Stage II/III CRC: xM ctDNA status post-surgery was a stronger DFS prognostic biomarker (adjusted HR 9.69) than CEA (adjusted HR 2.13). 87% of patients who recurred were detected within the 2–8 week early landmark window; 85% detected by week 4. 95% CIs not captured in accessible summaries.",
  "external_validation": {
    "performed": true,
    "cohort_description": "GALAXY arm of CIRCULATE-Japan — a prospective multicenter Japanese MRD trial; independent of any Tempus-internal training data.",
    "result": "HR 9.69 for DFS by post-surgery xM ctDNA status."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "A Tumor-Naive ctDNA Assay Detects Minimal Residual Disease in Resected Stage II or III Colorectal Cancer and Predicts Recurrence: Subset Analysis from the GALAXY Study in CIRCULATE-Japan",
      "journal": "Clinical Cancer Research",
      "year": 2025,
      "url": "https://aacrjournals.org/clincancerres/article/31/2/328/751096/A-Tumor-Naive-ctDNA-Assay-Detects-Minimal-Residual",
      "pivotal": true
    }
  ],
  "limitations_noted": "Tempus xM is offered as an LDT for early-stage CRC; broader-indication MRD detection (breast, other solid tumors) is RUO. xM is tumor-naïve in the early-stage CRC indication and tumor-informed (NeXT Personal Dx) in advanced settings — registry should clarify which variant is tracked. Pivotal data is a subset analysis of a larger trial, not a dedicated prospective validation.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | prospective | Clin Cancer Res 2025 abstract | "Subset analysis from the GALAXY Study in CIRCULATE-Japan" — GALAXY is a prospective observational MRD trial. |
| comparator | clinical_outcomes | abstract | xM status compared with disease-free survival events. |
| primary_endpoint | hazard_ratio | abstract | "adjusted HR 9.69" for DFS by xM ctDNA status. |
| primary_result | (see JSON) | abstract | "xM ctDNA status was a stronger prognostic biomarker for disease-free survival (adjusted HR, 9.69) compared with standard-of-care carcinoembryonic antigen (adjusted HR, 2.13)." |
| peer_reviewed | true | aacrjournals.org URL | Clinical Cancer Research peer-reviewed. |
| fda_summary_url | null | — | LDT. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` now populated.
- xM has dual variants (tumor-naïve methylation+variant integrative for early-stage CRC; tumor-informed NeXT Personal Dx for advanced). The registry's tracked variant should be made explicit. Recommend curator note.

---

## Entry: signatera-mrd

**Sources consulted:**
- **Tier 1 — Reinert T, Henriksen TV, Christensen E, et al. "Analysis of Plasma Cell-Free DNA by Ultradeep Sequencing in Patients With Stages I to III Colorectal Cancer." JAMA Oncology. 2019;5(8):1124-1131. DOI: 10.1001/jamaoncol.2019.0528. PMID: 31070691** — pivotal Signatera analytical/clinical validation in resected stage I–III CRC.
- **Tier 1 — Tie J, et al. "Circulating Tumor DNA Analysis Guiding Adjuvant Therapy in Stage II Colon Cancer." NEJM. 2022;386:2261-2272. DOI: 10.1056/NEJMoa2200075. PMID: 35657320** — DYNAMIC RCT using Signatera (clinical utility, not assay validation).
- **No FDA submission.** Signatera is LDT (NY CLEP cleared, Medicare-covered for select indications); `fda_status: "LDT"` correct.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "prospective",
  "cohort_size": {
    "n_patients": 125,
    "n_samples": 795,
    "unit_note": "Reinert 2019: 125 patients (stage I–III CRC, post-curative-surgery); 795 longitudinal plasma samples (baseline + 30-d post-op + every 3 months until death, withdrawal, or 3 years). 122 evaluable pre-op."
  },
  "n_sites": null,
  "site_geography": "multi_center_international",
  "comparator": "clinical_outcomes",
  "primary_endpoint": "hazard_ratio",
  "primary_result": "30-day post-operative MRD-positive vs negative: recurrence-free survival HR 7.2 (P<0.001). Serial ctDNA analysis: RFS HR 43.5 (P<0.001). Pre-operative detection: 88.5% (108/122); stage-stratified sensitivity: stage I 40%, stage II 92%, stage III 90%. Post-treatment MRD detection identified 14/16 relapses (87.5%). Surveillance-setting sensitivity 88%, specificity 98%.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Reinert 2019 cohort was an external prospective real-world Danish multicenter CRC cohort independent of Signatera training; further multicenter clinical-utility validation in NEJM 2022 DYNAMIC RCT (Australia/NZ).",
    "result": "Consistent HR direction across surveillance windows; replicated by DYNAMIC reductions in adjuvant chemo without DFS detriment."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Analysis of Plasma Cell-Free DNA by Ultradeep Sequencing in Patients With Stages I to III Colorectal Cancer",
      "journal": "JAMA Oncology",
      "year": 2019,
      "url": "https://pubmed.ncbi.nlm.nih.gov/31070691/",
      "pivotal": true
    },
    {
      "title": "Circulating Tumor DNA Analysis Guiding Adjuvant Therapy in Stage II Colon Cancer",
      "journal": "New England Journal of Medicine",
      "year": 2022,
      "url": "https://pubmed.ncbi.nlm.nih.gov/35657320/",
      "pivotal": false
    }
  ],
  "limitations_noted": "Reinert 2019 cohort is modest (N=125) and stage-imbalanced (stage I detection sensitivity only 40%). Single-country Danish cohort; broader external generalizability rests on subsequent CIRCULATE-Japan / DYNAMIC trials. Signatera is tumor-informed — assay requires upstream WES of the resected tumor; failed WES → no Signatera result.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | prospective | Reinert 2019 abstract | "This prospective, multicenter cohort study … included 130 patients with stages I to III CRC" (PMID 31070691). |
| cohort_size.n_patients | 125 | same | "included 125 patients with stage I to III CRC" (per analysis-population summary). |
| cohort_size.n_samples | 795 | same | "795 plasma samples were collected longitudinally". |
| comparator | clinical_outcomes | same | Compared against recurrence events at follow-up. |
| primary_endpoint | hazard_ratio | same | "HR 7.2" and "HR 43.5" for recurrence-free survival. |
| primary_result | (see JSON) | same | "the study reported a significantly higher RFS for ctDNA+ patients both at a 30-day timepoint (HR 7.2, P < 0.001) and, markedly, in the serial ctDNA analysis (HR 43.5, P < 0.001). In this surveillance setting, the reported values for sensitivity and specificity were 88% and 98%, respectively." |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/31070691/ | JAMA Oncol 2019. |
| fda_summary_url | null | — | LDT. |

**Discrepancies / notes:**
- **v0.1 publication mismatch:** `data.json` listed Tie 2022 NEJM as the pivotal — that paper is a clinical-utility RCT, not the Signatera assay-validation pivotal. Reinert 2019 JAMA Oncol is the canonical analytical+clinical pivotal. Both should be in `key_publications`, with `pivotal: true` reserved for Reinert.
- "Multi_center_international" is conservative — Reinert 2019 is Danish only; pivotal may be more accurately tagged `multi_center_international` if including subsequent confirmatory studies, otherwise `multi_center_us` is wrong; consider adding a `multi_center_european` enum.

---

## Entry: grail-galleri

**Sources consulted:**
- **Tier 1 — Schrag D, Beer TM, McDonnell CH 3rd, et al. "Blood-based tests for multicancer early detection (PATHFINDER): a prospective cohort study." Lancet. 2023;402(10409):1251-1260. DOI: 10.1016/S0140-6736(23)01700-2. PMID: 37805216** — PATHFINDER pivotal prospective validation.
- **No FDA submission yet.** PATHFINDER 2 registrational study top-line announced 2025 but not yet authorized; current Galleri is LDT.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "prospective",
  "cohort_size": {
    "n_patients": 6621,
    "n_samples": null,
    "unit_note": "6,662 enrolled adults ≥50 years without cancer symptoms; 6,621 with analysable results (63.5% women, 36.5% men, 91.7% White)."
  },
  "n_sites": 7,
  "site_geography": "multi_center_us",
  "comparator": "clinical_outcomes",
  "primary_endpoint": "ppv_npv",
  "primary_result": "Cancer signal detected in 92/6,621 participants (1.4%). True positives 35/92 (PPV 38.0%); false positives 57/92 (62.0%). 29 new cancers diagnosed in the cohort; 14/29 (48%) Stage I or II. Specificity ~99.1%. Median time to diagnostic resolution 79 days (IQR 37–219). 74% of cancers detected lacked USPSTF screening recommendations.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Prospective cohort drawn from 7 US health networks; independent of GRAIL's original Circulating Cell-free Genome Atlas (CCGA) training cohort.",
    "result": "PPV 38%; specificity ~99.1%; 48% of new cancers Stage I/II at detection."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Blood-based tests for multicancer early detection (PATHFINDER): a prospective cohort study",
      "journal": "The Lancet",
      "year": 2023,
      "url": "https://pubmed.ncbi.nlm.nih.gov/37805216/",
      "pivotal": true
    }
  ],
  "limitations_noted": "PATHFINDER is a single-arm prospective study with no comparator arm and an over-representation of White (91.7%) and well-resourced US participants. Test-version PPV was 38% (later versions report 43% per GRAIL but not in this paper). The trial does not establish mortality benefit — only test characteristics. Galleri remains an LDT pending FDA review of PATHFINDER 2.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | prospective | https://pubmed.ncbi.nlm.nih.gov/37805216/ | "a prospective cohort study". |
| cohort_size.n_patients | 6621 | same | "6,662 enrolled; 6,621 with analysable results". |
| n_sites | 7 | same | "Seven US health networks". |
| site_geography | multi_center_us | same | Same. |
| comparator | clinical_outcomes | same | Confirmed cancer diagnoses are the reference; no head-to-head comparator. |
| primary_endpoint | ppv_npv | same | "time to, and extent of, diagnostic testing required to confirm the presence or absence of cancer" — operationalized via PPV/NPV per protocol. |
| primary_result | (see JSON) | same | "Cancer signal detected in 92 participants (1.4%) … True positives: 35 (38%) … False positives: 57 (62%) … Of 29 new cancers, '14 (48%) were Stage I or II'". |
| peer_reviewed | true | Lancet 2023 | PMID 37805216. |
| fda_summary_url | null | — | LDT pending FDA review. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` populated.
- Galleri's "99.1% specificity" headline is from CCGA-3 / earlier versions; the PATHFINDER paper reports the prospective specificity implicitly through the false-positive count. Curator may want to cite both.

---

## Entry: exact-oncotype-dx-breast

**Sources consulted:**
- **Tier 1 — Sparano JA, Gray RJ, Makower DF, et al. "Adjuvant Chemotherapy Guided by a 21-Gene Expression Assay in Breast Cancer." NEJM. 2018;379(2):111-121. DOI: 10.1056/NEJMoa1804710. PMID: 29860917** — TAILORx pivotal RCT.
- **No FDA submission.** Oncotype DX is LDT; Medicare-covered; in NCCN/ASCO/ESMO guidelines. `fda_status: "LDT"` correct.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "rct",
  "cohort_size": {
    "n_patients": 10273,
    "n_samples": null,
    "unit_note": "TAILORx enrolled 10,273 women with HR+/HER2-/N0 breast cancer (2006–2010); 9,719 eligible with follow-up; primary analysis on the 6,711 (69%) with midrange Recurrence Score 11–25 randomly assigned to chemoendocrine vs endocrine-alone."
  },
  "n_sites": null,
  "site_geography": "multi_center_international",
  "comparator": "clinical_outcomes",
  "primary_endpoint": "time_to_event_risk_strata",
  "primary_result": "9-year iDFS rate in midrange RS 11–25: endocrine alone 83.3% vs chemoendocrine 84.3% (HR 1.08; 95% CI 0.94–1.24; non-inferiority criterion met). 9-year distant-recurrence rate: endocrine 4.9% vs chemoendocrine 4.6%. Subgroup signal of chemo benefit in women ≤50 years with RS 16–25. For RS 0–15: 9-yr distant recurrence 3% irrespective of age (endocrine alone).",
  "external_validation": {
    "performed": true,
    "cohort_description": "TAILORx is itself a prospective external validation of the Recurrence Score categories originally derived from NSABP B-14 / B-20 archived cohorts; ~1,200 US/Canada/Australia/Ireland/Peru sites.",
    "result": "Confirmed prognostic stratification and lack of chemo benefit for RS 11–25 overall."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Adjuvant Chemotherapy Guided by a 21-Gene Expression Assay in Breast Cancer",
      "journal": "New England Journal of Medicine",
      "year": 2018,
      "url": "https://pubmed.ncbi.nlm.nih.gov/29860917/",
      "pivotal": true
    }
  ],
  "limitations_noted": "TAILORx primary analysis applies only to women with RS 11–25; women with RS 0–10 (assigned endocrine alone) and RS 26–100 (assigned chemoendocrine) were not randomized. Race/ethnicity subgroup analyses underpowered for non-White populations. Test is LDT; analytical validation rests on prior NSABP archival-cohort studies (Paik 2004 NEJM, Paik 2006 JCO).",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | rct | https://pubmed.ncbi.nlm.nih.gov/29860917/ | TAILORx was a prospective randomized non-inferiority trial — RCT. |
| cohort_size.n_patients | 10273 | same | "involved 10,273 women recruited between 2006 and 2010." |
| comparator | clinical_outcomes | same | Endpoints are iDFS / distant recurrence / OS — clinical outcomes. |
| primary_endpoint | time_to_event_risk_strata | same | "The trial was designed to show noninferiority of endocrine therapy alone for invasive disease-free survival" (time-to-event). |
| primary_result | (see JSON) | same / NEJM abstract | "9-year iDFS rate in midrange RS 11–25: endocrine alone 83.3% vs chemoendocrine 84.3% (HR 1.08; 95% CI 0.94–1.24)". |
| peer_reviewed | true | NEJM | PMID 29860917. |
| fda_summary_url | null | — | LDT. |

**Discrepancies / notes:**
- TAILORx site count is published as ~1,182 sites in 6 countries — curator may want to drop a number into `n_sites` from the NEJM paper rather than leaving null.

---

## Entry: veracyte-decipher-prostate

**Sources consulted:**
- **Tier 1 — Klein EA, Yousefi K, Haddad Z, et al. "A genomic classifier improves prediction of metastatic disease within 5 years after surgery in node-negative high-risk prostate cancer patients managed by radical prostatectomy without adjuvant therapy." European Urology. 2015;67(4):778-786. DOI: 10.1016/j.eururo.2014.10.036. PMID: 25466945** — pivotal analytical+clinical validation for the post-prostatectomy indication.
- **Tier 1 — Feng FY, Huang H-C, Spratt DE, et al. "Validation of a 22-Gene Genomic Classifier in Patients With Recurrent Prostate Cancer: An Ancillary Study of the NRG/RTOG 9601 Randomized Clinical Trial." JAMA Oncology. 2021;7(4):544-552. DOI: 10.1001/jamaoncol.2020.7671. PMID: 33570548** — phase III ancillary validation.
- **NCCN-cited level I evidence inclusion.** No FDA submission; LDT.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": null,
    "unit_note": "Klein 2015 pivotal: independent validation cohort of node-negative high-risk RP patients managed without adjuvant therapy; exact N not captured in accessible abstract. NRG/RTOG 9601 ancillary (Feng/Spratt 2021): post-prostatectomy biochemical recurrence cohort from the phase III RCT."
  },
  "n_sites": null,
  "site_geography": "multi_center_us",
  "comparator": "clinicopathologic_factors",
  "primary_endpoint": "hazard_ratio",
  "primary_result": "Klein 2015: Decipher independently predicted 5-yr metastasis after RP — OR 1.48 (P=0.018) in multivariable analysis adjusting for clinicopathologic factors; c-index 0.77 vs Stephenson model 0.75 and CAPRA-S 0.72. NRG/RTOG 9601 ancillary (Feng/Spratt 2021): sHR for distant metastasis 1.28 (95% CI 1.06–1.55, P=0.01); PCSM sHR 1.45 (95% CI 1.2–1.76, P<0.001); biochemical failure sHR 1.22 (95% CI 1.1–1.37, P<0.001); disease progression sHR 1.12 (95% CI 1.0–1.26, P=0.04).",
  "external_validation": {
    "performed": true,
    "cohort_description": "Klein 2015 used an independent post-prostatectomy validation cohort distinct from the Decipher development data. NRG/RTOG 9601 is a phase III RCT ancillary genomic analysis — external by design.",
    "result": "Independent prognostic value beyond CAPRA-S, Stephenson nomogram, GPSM, and standard clinicopathologic factors."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "A genomic classifier improves prediction of metastatic disease within 5 years after surgery in node-negative high-risk prostate cancer patients managed by radical prostatectomy without adjuvant therapy",
      "journal": "European Urology",
      "year": 2015,
      "url": "https://pubmed.ncbi.nlm.nih.gov/25466945/",
      "pivotal": true
    },
    {
      "title": "Validation of a 22-Gene Genomic Classifier in Patients With Recurrent Prostate Cancer: An Ancillary Study of the NRG/RTOG 9601 Randomized Clinical Trial",
      "journal": "JAMA Oncology",
      "year": 2021,
      "url": "https://pubmed.ncbi.nlm.nih.gov/33570548/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Klein 2015 cohort is from a single tertiary referral center — generalizability to community practice rests on subsequent prospective registry data. The 22-gene classifier was developed in radical prostatectomy specimens; biopsy-specimen validation (Spratt 2017 European Urology, Berlin 2019 Urology) extended use but was added retrospectively. Decipher is LDT — no FDA review of analytical performance. Cohort N values omitted because the source abstracts did not enumerate them in the accessible text — full paper required.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://pubmed.ncbi.nlm.nih.gov/25466945/ | Retrospective independent validation cohort. |
| comparator | clinicopathologic_factors | same | "after adjusting for clinical risk factors" — incremental value beyond CAPRA-S, Stephenson, GPSM. |
| primary_endpoint | hazard_ratio | NRG/RTOG 9601 abstract | "sHR 1.28 ... sHR 1.45 ... sHR 1.22 ..." for multiple endpoints. |
| primary_result | (see JSON) | https://pubmed.ncbi.nlm.nih.gov/25466945/ ; https://jamanetwork.com/journals/jamaoncology/fullarticle/2776225 | "Decipher was a significant predictor of rapid metastasis with an odds ratio of 1.48 (p=0.018)" / "distant metastasis sHR 1.28 (95% CI 1.06-1.55, P=0.01)". |
| peer_reviewed | true | Both PubMed entries | EUR 2015 and JAMA Oncol 2021. |
| fda_summary_url | null | — | LDT. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` populated.
- The exact cohort N for Klein 2015 (commonly reported as N=169, but please confirm against the paper) is missing from accessible search snippets. Curator should pull the EUR 2015 paper for canonical N and 5-yr metastasis rates by Decipher risk category.

---

## Entry: veracyte-afirma-gsc

**Sources consulted:**
- **Tier 1 — Patel KN, Angell TE, Babiarz J, et al. "Performance of a Genomic Sequencing Classifier for the Preoperative Diagnosis of Cytologically Indeterminate Thyroid Nodules." JAMA Surgery. 2018;153(9):817-824. DOI: 10.1001/jamasurg.2018.1153. PMID: 29799911** — pivotal multicenter clinical validation.
- **No FDA submission.** Afirma GSC is LDT (NY CLEP cleared, Medicare-covered); `fda_status: "LDT"` correct.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "prospective",
  "cohort_size": {
    "n_patients": 191,
    "n_samples": 191,
    "unit_note": "Prospective, multicenter, blinded cohort of 191 cytologically indeterminate (Bethesda III/IV) thyroid nodule FNA samples; ground truth = blinded expert histopathology."
  },
  "n_sites": null,
  "site_geography": "multi_center_us",
  "comparator": "gold_standard_test",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Sensitivity 91% (95% CI 79–98%); Specificity 68% (95% CI 60–76%); NPV 96% (95% CI 90–99%) at a 24% cancer prevalence in the Bethesda III/IV cohort; PPV 47% (95% CI 36–58%).",
  "external_validation": {
    "performed": true,
    "cohort_description": "Prospective multicenter cohort recruited independently of Afirma GSC training data; blinded histopathology adjudication.",
    "result": "Performance validated against blinded expert histopathology."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Performance of a Genomic Sequencing Classifier for the Preoperative Diagnosis of Cytologically Indeterminate Thyroid Nodules",
      "journal": "JAMA Surgery",
      "year": 2018,
      "url": "https://pubmed.ncbi.nlm.nih.gov/29799911/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Patel 2018 cohort is small (N=191); cancer prevalence (24%) is higher than some real-world indeterminate-nodule populations, which affects NPV. Test is intended as a rule-out (high NPV) — PPV is moderate; benign Afirma calls should still be followed by ultrasound surveillance per ATA guidelines. Afirma GSC is LDT — no FDA analytical review.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | prospective | https://pubmed.ncbi.nlm.nih.gov/29799911/ | "prospective, multicenter, blinded cohort". |
| cohort_size.n_patients | 191 | same | "191 indeterminate thyroid nodule fine needle aspiration samples". |
| comparator | gold_standard_test | same | "blinded expert histopathology diagnoses". |
| primary_endpoint | sensitivity_specificity | same | "sensitivity of 91% and a specificity of 68%". |
| primary_result | (see JSON) | same | "negative predictive value (NPV) of 96% (95% CI, 90-99) at a 24% cancer prevalence". |
| peer_reviewed | true | JAMA Surg | PMID 29799911. |
| fda_summary_url | null | — | LDT. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` populated.
- n_sites was not captured from the abstract — likely "multi-center" with ~20+ US institutions per the Veracyte study network; curator should confirm against the full paper for an exact site count.

---

## Entry: icad-profound-ai-dbt

**Sources consulted:**
- **Tier 1 — FDA 510(k) K182373 Decision Summary** — https://www.accessdata.fda.gov/cdrh_docs/pdf18/K182373.pdf — PowerLook Tomo Detection V2 (the original ProFound AI DBT submission), cleared December 2018. Predicate: Imagen OsteoDetect (DEN180005), regulation 21 CFR 892.2090.
- **Tier 1 — Conant EF, Toledano AY, Periaswamy S, et al. "Improving Accuracy and Efficiency with Concurrent Use of Artificial Intelligence for Digital Breast Tomosynthesis." Radiology: Artificial Intelligence. 2019;1(4):e180096. DOI: 10.1148/ryai.2019180096. PMID: 33937794** — peer-reviewed publication of the K182373 pivotal reader study.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": 260,
    "unit_note": "Pivotal reader study: 260 enriched Hologic DBT cases (65 cancer cases with 66 malignant lesions) read by 24 tomosynthesis radiologist readers in a fully-crossed MRMC design. Standalone studies: 655 Hologic DBT cases (235 cancer with 242 malignant lesions) and 610 GE DBT cases (204 cancer with 221 malignant lesions)."
  },
  "n_sites": null,
  "site_geography": "multi_center_us",
  "comparator": "predicate_device",
  "primary_endpoint": "AUC",
  "primary_result": "Pivotal MRMC reader study: case-level AUC with CAD 0.852 vs without CAD 0.795; difference +0.057 (95% CI 0.028, 0.087; non-inferiority p<0.01, superiority p<0.01). Case-level sensitivity: with CAD 0.850 vs without 0.770 (+0.080, 95% CI 0.026, 0.134). Lesion-level sensitivity: 0.853 vs 0.769 (+0.084, 95% CI 0.029, 0.139). Specificity: 0.696 vs 0.627 (+0.069, 95% CI 0.030, 0.108). Recall rate in non-cancers: 0.309 vs 0.380 (reduction 0.072, 95% CI 0.031, 0.112). Reading time reduced 52.7% (95% CI 41.8%, 61.5%; p<0.01).",
  "external_validation": {
    "performed": true,
    "cohort_description": "Pivotal MRMC reader study used 260 enriched Hologic DBT cases distinct from the training data per the Decision Summary; standalone studies included a separate GE DBT cohort (610 cases) confirming non-inferior performance across scanner manufacturer.",
    "result": "Non-inferiority across Sensitivity, FPPI, and AUC for PowerLook Tomo Detection 2.0 with GE DBT vs Hologic DBT (K182373 pp. 11–13)."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Improving Accuracy and Efficiency with Concurrent Use of Artificial Intelligence for Digital Breast Tomosynthesis",
      "journal": "Radiology: Artificial Intelligence",
      "year": 2019,
      "url": "https://pubmed.ncbi.nlm.nih.gov/33937794/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Reader study used an enriched dataset (25% cancer prevalence vs ~0.5% in screening) — performance estimates do not directly translate to screening-population recall or PPV. 24 radiologist readers, of whom 13 were breast subspecialists — generalizability to general radiologists is partly addressed but limited. The pivotal study is retrospective and was conducted by the manufacturer.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf18/K182373.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | K182373 p. 9 | "A pivotal reader study, which was a retrospective, fully-crossed, multi-reader, multi-case (MRMC) study". |
| cohort_size.n_samples | 260 | K182373 p. 9 | "an enriched sample of 260 Hologic digital breast tomosynthesis (DBT) cases, including 65 cancer cases with 66 malignant lesions". |
| comparator | predicate_device | K182373 p. 9 | "compare clinical performance of radiologists using CAD detections … with DBT images to that of radiologists using DBT without CAD". DBT-without-CAD is the comparator. |
| primary_endpoint | AUC | K182373 p. 9 | "Radiologist performance was assessed by measuring case-level area under the receiver operating characteristic (ROC) curve (AUC) for the detection of malignant lesions". |
| primary_result | (see JSON) | K182373 pp. 9–11 | "Radiologists had superior per-subject average area under the receiver operating characteristic (ROC) curve (AUC) with CAD, 0.852, versus without CAD, 0.795. The average difference in AUC was 0.057 (95% CI: 0.028, 0.087…)". |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/33937794/ | Radiology: AI 2019. |
| limitations_noted | (see JSON) | K182373 pp. 4 (per Conant) | "Interpreting physicians reading times may vary based on the specific functionality of the viewing application used for interpretation." |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/pdf18/K182373.pdf | — | Direct URL. |

**Discrepancies / notes:**
- v0.1 `key_publications: []` populated.
- iCAD ProFound AI has had multiple subsequent 510(k) clearances (K191994 — GE DBT compatibility 2019; K221449 — V3.0; later K-numbers for V4.0). The K182373 cohort is the historically-canonical pivotal.

---

## Entry: hologic-genius-ai-detection

**Sources consulted:**
- **Tier 1 — FDA 510(k) K201019 Decision Summary** — https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201019.pdf — Genius AI Detection. Predicate K182373 PowerLook Tomo Detection V2. Cleared November/December 2020.
- **Tier 1 — FDA 510(k) K221449 Decision Summary** — https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221449.pdf — Genius AI Detection 2.0. Predicate K201019.
- **No peer-reviewed pivotal publication of the K201019 reader study has been published as of search date.**

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": null,
    "n_samples": 390,
    "unit_note": "MRMC pivotal reader study: 390 cases (106 cancers + 284 negative cases) included in the per-protocol analysis; 17 readers reviewed each case in both reading modes (with CAD and without CAD) separated by ≥4 weeks. Standalone study used a larger 764-case overall set (106 cancers + 658 non-cancers) on Hologic standard and high-resolution tomosynthesis."
  },
  "n_sites": null,
  "site_geography": "multi_center_us",
  "comparator": "predicate_device",
  "primary_endpoint": "AUC",
  "primary_result": "MRMC: average AUC 0.825 with CAD (95% CI 0.783, 0.867) vs 0.794 without CAD (95% CI 0.748, 0.840); difference +0.031 (95% CI 0.012, 0.051). Average reader sensitivity for cancer cases 75.9% with CAD vs 66.8% without; difference +9.0% (99% CI 6.0%, 12.1%). Recall rate in non-cancer cases 25.8% with CAD vs 23.4% without; difference +2.4% (99% CI 0.7%, 4.2%). Read time 52.0s with CAD vs 46.3s without; difference 5.7s (95% CI 4.9s to 6.4s).",
  "external_validation": {
    "performed": true,
    "cohort_description": "Reader study cohort distinct from training; standalone study confirmed equivalent performance across Hologic standard-resolution (~100μm) and high-resolution (70μm) tomosynthesis acquisitions, and across 3DQuorum SmartSlices.",
    "result": "No significant differences in detection performance between acquisition modes; stratified fROC analysis by lesion type and breast density also consistent."
  },
  "peer_reviewed": false,
  "key_publications": [],
  "limitations_noted": "K201019 Decision Summary explicitly cautions that the reported analyses 'do not control type I error and therefore cannot be generalized to specific comparisons outside this particular study' (p. 10). Read time increased slightly (+5.7s) with CAD vs without — note this contrasts with iCAD's 52.7% reduction, likely reflecting concurrent-vs-second-read workflow differences. Cohort enriched for cancer cases (~27% prevalence) — performance does not translate directly to screening-population recall rates.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201019.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | K201019 p. 10 | MRMC reader study (retrospective by design). |
| cohort_size.n_samples | 390 | K201019 p. 10 | "the results below represent a per-protocol analysis of the 390 cases (106 cancers, and 284 negative cases) included in the MRMC where both rounds of reading were completed." |
| comparator | predicate_device | K201019 p. 11 | "the Genius AI Detection device and its predicate device, PowerLook® Tomo Detection V2 both have a similar intended use". Reader-without-CAD also serves as comparator within the MRMC. |
| primary_endpoint | AUC | K201019 p. 10 | "The average observed AUC was 0.825 (95% CI: 0.783, 0.867) with CAD and 0.794 (95% CI: 0.748, 0.840) without CAD." |
| primary_result | (see JSON) | K201019 p. 10 | Same as JSON. |
| external_validation.performed | true | K201019 pp. 10–11 | Standalone study used a separate 764-case dataset. |
| peer_reviewed | false | — | No PubMed entry for the K201019 reader study located as of search date. |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201019.pdf | — | Direct URL. |

**Discrepancies / notes:**
- `data.json` `regulatory.fda_decision_date` is null — actual K201019 clearance was 2020-11-09 per the FDA letter. Curator should populate.
- Genius AI Detection 2.0 (K221449) followed in 2022 with reportedly improved specificity; the registry should decide whether to track the original or the latest variant.

---

## Entry: aidoc-briefcase-lung-nodule

**Sources consulted:**
- **No FDA 510(k) Decision Summary located.** Search of Aidoc's published list of FDA-cleared products (https://www.aidoc.com/about/news/fda-incidental-pulmonary-embolism/) lists six clearances: intracranial hemorrhage, c-spine fracture, large vessel occlusion, intra-abdominal free gas, pulmonary embolism, incidental pulmonary embolism. **Lung nodule is NOT among Aidoc's published FDA-cleared products** as of search date.
- **Sole peer-reviewed reference:** Kanne JP, et al. "Leveraging Artificial Intelligence as a Safety Net for Incidentally Identified Lung Nodules at a Tertiary Center." (PMID 39803962, 2025) describes an Aidoc-marketed "Pulmonary Nodule Patient Management" workflow tool — implementation study, not an FDA pivotal.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "unpublished",
  "cohort_size": {
    "n_patients": null,
    "n_samples": null,
    "unit_note": "No FDA-cited pivotal cohort identified. A tertiary-center implementation study reports the tool brought 30% of clinically significant incidental nodules to clinician attention that would otherwise have been missed."
  },
  "n_sites": null,
  "site_geography": null,
  "comparator": null,
  "primary_endpoint": null,
  "primary_result": "Implementation-study reported PPV 95% for identifying ≥8 mm nodules needing follow-up, sensitivity 100% with no false negatives (small single-center retrospective sample, not an FDA pivotal).",
  "external_validation": {
    "performed": null,
    "cohort_description": "Single tertiary-center implementation paper, not a multi-site validation.",
    "result": null
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Leveraging Artificial Intelligence as a Safety Net for Incidentally Identified Lung Nodules at a Tertiary Center",
      "journal": "Journal of the American College of Radiology",
      "year": 2025,
      "url": "https://pubmed.ncbi.nlm.nih.gov/39803962/",
      "pivotal": false
    }
  ],
  "limitations_noted": "FDA STATUS UNVERIFIED — no 510(k) Decision Summary was found for an Aidoc incidental lung nodule device in the FDA database, and lung nodule is not listed among Aidoc's six publicly-claimed FDA-cleared products as of curation date. The registry entry has been conservatively downgraded from 510(k) cleared to Research Use pending follow-up. Possible explanations: (i) the product is a CE-marked-only / non-US tool; (ii) clearance is held under a partner manufacturer's K-number (e.g., the Riverain-Aidoc partnership for lung nodule detection); (iii) the registry entry is premature. Recommend confirming with Aidoc or revising the product/company scope.",
  "fda_summary_url": null,
  "data_completeness": "partial"
}
```

**Field-by-field provenance:**
| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | unpublished | — | No FDA Decision Summary; no pivotal published validation. |
| primary_result | (see JSON) | https://pubmed.ncbi.nlm.nih.gov/39803962/ | Single-center implementation paper. |
| peer_reviewed | true | same | Peer-reviewed implementation paper exists, though not a pivotal. |
| limitations_noted | (see JSON) | — | Discrepancy with `data.json` regulatory block — see note. |
| fda_summary_url | null | — | None located. |

**Discrepancies / notes:**
- **Highest-priority curator action.** Confirm Aidoc's incidental lung nodule FDA status. Per the Aidoc-Riverain partnership (https://appliedradiology.com/articles/partnership-will-streamline-access-to-chest-ai-solutions), Aidoc integrates Riverain's FDA-cleared lung nodule detection — the K-number likely belongs to Riverain, not Aidoc. If so, the registry entry product name and company should be revisited.

---

## Top-level Summary

### Population status per entry (16 entries, 14 populatable validation fields each)

| Entry | Fields populated | Fields left null | data_completeness |
|-------|------------------|------------------|--------------------|
| paige-her2 | 6 | 8 | partial |
| paige-lymph-node | 9 | 5 | partial |
| pathai-aisight-dx | 13 | 1 (n_patients) | full |
| ibex-galen-prostate | 14 | 0 | full |
| ibex-galen-breast | 8 | 6 | partial |
| owkin-msintuit-crc | 13 | 1 (n_samples) | full |
| tempus-xt | 14 | 0 | full |
| tempus-xm | 7 | 7 | partial |
| signatera-mrd | 13 | 1 (n_sites) | full |
| grail-galleri | 13 | 1 (n_samples) | full |
| exact-oncotype-dx-breast | 12 | 2 (n_samples, n_sites) | full |
| veracyte-decipher-prostate | 10 | 4 | partial |
| veracyte-afirma-gsc | 12 | 2 (n_sites, n_samples) | full |
| icad-profound-ai-dbt | 13 | 1 (n_patients) | full |
| hologic-genius-ai-detection | 12 | 2 (n_patients, n_sites) | full |
| aidoc-briefcase-lung-nodule | 4 | 10 | partial |

### Curator should look at first
1. **`aidoc-briefcase-lung-nodule`** — FDA status appears incorrect; product may not have its own FDA clearance, or clearance is via Riverain partnership. Revisit fda_pathway / fda_status / company fields.
2. **`ibex-galen-prostate`** — FDA pathway and decision date in `data.json` are wrong. Correct to `510k` / `2025-02-10`, predicate Paige Prostate DEN200080.
3. **`paige-lymph-node`** — Currently has Breakthrough Device Designation only, not a market authorization. fda_status acceptable but worth clarifying.
4. **`signatera-mrd`** — `data.json` v0.1 pivotal publication is Tie 2022 NEJM (DYNAMIC). The assay-validation pivotal is Reinert 2019 JAMA Oncol. Re-assign `pivotal: true`.
5. **`owkin-msintuit-crc`** — v0.1 publication title is paraphrased incorrectly. Replace with PubMed canonical title (above).
6. **`paige-her2`** — `data.json` shows `fda_status: "Research Use"`; product is CE-IVD / UKCA. Consider adding `ce_marked: true`. No FDA clearance exists.

### v0.1 publication / metadata errors uncovered
1. `owkin-msintuit-crc`: wrong title for the Nat Commun 2023 paper. Correct title is **"Validation of MSIntuit as an AI-based pre-screening tool for MSI detection from colorectal cancer histology slides"** (PMID 37932267).
2. `signatera-mrd`: pivotal publication points to Tie 2022 NEJM. Correct analytical pivotal is **Reinert et al. JAMA Oncology 2019** (PMID 31070691); keep Tie 2022 as a non-pivotal clinical-utility citation.
3. `ibex-galen-prostate`: pivotal listed as "AI-based detection and grading of prostate cancer in biopsies / Lancet Digital Health / 2020" — paraphrased title. Canonical PubMed title: **"An artificial intelligence algorithm for prostate cancer diagnosis in whole slide images of core needle biopsies: a blinded clinical validation and deployment study"** (Pantanowitz et al., Lancet Digital Health 2020, PMID 33328045). Note: this paper is the methodology reference but is **not** the FDA-cited K241232 cohort.
4. `ibex-galen-prostate`: `regulatory.fda_pathway` and `regulatory.fda_decision_date` both incorrect (see #2 above).
5. `aidoc-briefcase-lung-nodule`: `regulatory.fda_status` and `regulatory.fda_pathway` cannot be substantiated against the FDA 510(k) database.

### Schema enum mismatches
- **`primary_endpoint = "other"`** chosen for `pathai-aisight-dx` because the FDA pivotal is a "non-inferiority of major-discordance rate vs glass-slide reference" — no clean v0.2 enum exists. Suggest adding `non_inferiority_glass_slide` for digital-pathology viewers, or accepting "other" with a comment field.
- **`site_geography`** does not have a `multi_center_european` value — used for `signatera-mrd` (Reinert 2019 Danish multicenter cohort), but had to fall back to `multi_center_international`. Suggest adding.
- **`study_design = "unpublished"`** used for `aidoc-briefcase-lung-nodule`; this is appropriate given no FDA Decision Summary located.

### Cohort metadata gaps requiring full-text retrieval
- `paige-her2` — Clinical Breast Cancer 2025 paywall.
- `paige-lymph-node` — Modern Pathology 2023 and AJSP 2024 paywall (95% CIs).
- `ibex-galen-breast` — npj Breast Cancer 2022 (need 95% CIs and exact cohort N).
- `veracyte-decipher-prostate` — European Urology 2015 and JAMA Oncol 2021 (need exact cohort Ns).

End of phase 1 batch 2 verification sheet. Curator review requested before applying to `data.json`. No data.json modifications made.
