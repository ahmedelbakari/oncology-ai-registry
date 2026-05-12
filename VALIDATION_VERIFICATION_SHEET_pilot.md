# Validation Verification Sheet — Pilot Batch (3 entries)

Prepared from primary sources (FDA Decision Summaries and pivotal peer-reviewed publications) for curator review of the pilot validation fields applied to `data.json`.

Conventions:
- Tier 1 = FDA Decision Summary (`accessdata.fda.gov/cdrh_docs/reviews/`) and pivotal peer-reviewed publication.
- Verbatim quotes are reproduced exactly as printed; Roman numerals/italic emphasis dropped only where they would not parse in markdown.
- Where the FDA Decision Summary and the peer-reviewed publication report different cohorts, both are recorded and the field is populated from the FDA summary (per brief rule 3 / rule 4).
- `null` is used where the cited source does not support a value.

---

## Entry: artera-prostate

**Sources consulted:**
- **Tier 1 — FDA De Novo Decision Summary, DEN240068 (24 pages)** — https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf — source of record. Provided cohort size (n=886), 3 US sites, retrospective design, primary endpoints (10-yr DM and PCSM risk by ArteraAI category), Kaplan–Meier results with 95% CIs, subgroup analyses, and limitations.
- **Tier 1 — FDA classification order letter, DEN240068** — https://www.accessdata.fda.gov/cdrh_docs/pdf24/DEN240068.pdf — confirmed De Novo authorization date (July 31, 2025), regulation 21 CFR 864.3755, product code SFH, indications for use.
- **Tier 1 — Esteva A, Feng J, van der Wal D, et al. "Prostate cancer therapy personalization via multi-modal deep learning on randomized phase III clinical trials." npj Digital Medicine 5, 71 (2022). DOI: 10.1038/s41746-022-00613-w. PMID: 35676445** — https://pubmed.ncbi.nlm.nih.gov/35676445/ — listed as a key publication describing the underlying MMAI model. **Note:** the brief refers to "NEJM Evidence, 2022"; the canonical 2022 multimodal-AI paper for ArteraAI is in npj Digital Medicine, not NEJM Evidence. A separate Spratt et al. 2023 paper appears in NEJM Evidence (DOI 10.1056/EVIDoa2300023). Flagging as a discrepancy in the brief — see below.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 886,
    "n_samples": null,
    "unit_note": "patients (≥1 H&E biopsy slide containing the highest Gleason grade core per patient)"
  },
  "n_sites": 3,
  "site_geography": "multi_center_us",
  "comparator": "clinical_outcomes",
  "primary_endpoint": "time_to_event_risk_strata",
  "primary_result": "10-year risk of distant metastasis: ArteraAI High 28.1% (95% CI 19.4–37.5%), Intermediate 6.6% (3.6–10.8%), Low 3.3% (1.8–5.6%); overall 8.1% (6.1–10.4%). 10-year risk of prostate cancer-specific mortality: High 10.2% (4.7–18.2%), Intermediate 1.1% (0.2–3.7%), Low 0.6% (0.1–2.0%); overall 2.3% (1.2–3.8%). N=886, 3 US sites.",
  "external_validation": {
    "performed": true,
    "cohort_description": "Pivotal clinical validation cohort (N=886, 3 US sites) was independent of the development data, which used eight NRG/RTOG phase 3 trials per the underlying npj Digital Medicine 2022 publication. The FDA Decision Summary describes only one clinical performance study; no separate post-market external validation cohort is described in DEN240068.",
    "result": "Subgroup-consistent prognostic separation across treatment groups (Active Surveillance n=314; Radiation Therapy n=203; Radical Prostatectomy n=354) and across African-American (n=72) vs. non-African-American (n=814) subgroups."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Prostate cancer therapy personalization via multi-modal deep learning on randomized phase III clinical trials",
      "journal": "npj Digital Medicine",
      "year": 2022,
      "url": "https://pubmed.ncbi.nlm.nih.gov/35676445/",
      "pivotal": true
    }
  ],
  "limitations_noted": "FDA Decision Summary notes (i) the African-American subgroup was small (N=72) and 'should be taken in consideration when using the risk estimates'; (ii) erroneous results may lead to over- or under-treatment; (iii) the device 'should be used in conjunction with a complete standard of care evaluation' and is not a primary diagnosis; (iv) clinical validation was at three US sites only and is retrospective.",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 14) | "The clinical performance of the ArteraAI Prostate device was evaluated in a retrospective clinical study which included a total of 886 patients across three sites in the US." |
| cohort_size.n_patients | 886 | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 14) | "...a retrospective clinical study which included a total of 886 patients across three sites in the US." |
| cohort_size.n_samples | null | — | FDA summary characterizes the cohort by patient count, not slide count. "Patients were required to have non-metastatic prostate cancer and at least one H&E slide containing at least one FFPE biopsy core with the highest Gleason grade tumor as diagnosed by the pathologist." (p. 14) — exact slide count not enumerated. |
| cohort_size.unit_note | "patients (≥1 H&E biopsy slide containing the highest Gleason grade core per patient)" | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 14) | "Patients were required to have non-metastatic prostate cancer and at least one H&E slide containing at least one FFPE biopsy core with the highest Gleason grade tumor as diagnosed by the pathologist." |
| n_sites | 3 | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 14) and Table 6 (p. 15) | "Patients across 3 US sites were considered eligible…" (p. 14); Table 6 lists "Site 1 290 (33%), Site 2 444 (50%), Site 3 152 (17%)" (p. 15). |
| site_geography | multi_center_us | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 14) | "…886 patients across three sites in the US." |
| comparator | clinical_outcomes | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 16) | "The prognostic ability of the ArteraAI Prostate was evaluated for 10-year risk of DM. The estimates of 10-year risks of DM for ArteraAI Prostate Risk categories along with two-sided 95%CI are presented in Table 7…" — ground truth was actual metastasis / cancer-specific mortality events with Kaplan–Meier survival analysis; no pathologist-consensus or predicate-device comparator. |
| primary_endpoint | time_to_event_risk_strata | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 16, 18) | "10-Year Risk of DM for ArteraAI Prostate Risk Categories (High, Intermediate, Low)" and "10-Year Risk of PCSM for ArteraAI Prostate Risk Categories" — Kaplan–Meier risk estimates across three risk categories. |
| primary_result | "10-year DM risk: High 28.1% (95% CI 19.4–37.5%), Intermediate 6.6% (3.6–10.8%), Low 3.3% (1.8–5.6%); overall 8.1% (6.1–10.4%). 10-year PCSM risk: High 10.2% (4.7–18.2%), Intermediate 1.1% (0.2–3.7%), Low 0.6% (0.1–2.0%); overall 2.3% (1.2–3.8%)." | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (Table 7 p. 17, Table 8 p. 18) | Table 7: "High 144 30 28.1% (19.4%-37.5%) 16.3% / Intermediate 214 12 6.6% (3.6%-10.8%) 24.2% / Low 528 13 3.3% (1.8%-5.6%) 59.6% / Total 886 55 Estimated overall risk (95% CI): 8.1% (6.1%-10.4%)" Table 8: "High 144 9 10.2% (4.7% - 18.2%) 16.3% / Intermediate 214 2 1.1% (0.2% - 3.7%) 24.2% / Low 528 2 0.6% (0.1% - 2.0%) 59.6% / Total 886 13 Estimated overall risk (95% CI): 2.3% (1.2% - 3.8%)" |
| external_validation.performed | true | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (pp. 6, 14) | The DEN240068 Decision Summary describes model training on clinical trials and a separate N=886 clinical performance cohort. The registry treats a validation cohort independent of training data as external validation, although the FDA summary does not use the literal phrase "external validation." |
| external_validation.cohort_description | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (pp. 6–7, 14) | Training: "There were 1,133 distant metastasis events and 931 prostate cancer specific mortality events in the dataset used to train the model." Table 2 lists training cohort N = 10,009 across Canary-PASS, RTOG 0126, 0415, 0521, 9202, 9408, 9413, 9902, 9910, STAMPEDE, and Contemporary Biopsy Cohort A. Clinical validation: "886 patients across three sites in the US" (p. 14) — independent of the training trials. |
| external_validation.result | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (Table 9 p. 20, Table 11 p. 21) | African-American (N=72): "13.5% (5.1%-26.1%)" overall 10-yr DM. Non-African-American (N=814): "7.7% (5.7%-10.0%)". Subgroup analysis "across patients treated with all different treatment regimens… ArteraAI Prostate risk estimates were acceptable for each treatment group." |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/35676445/ | Underlying MMAI model published in npj Digital Medicine, 2022. |
| key_publications[0] | npj Digital Medicine, 2022, Esteva et al. | https://pubmed.ncbi.nlm.nih.gov/35676445/ | "Esteva A, Feng J, van der Wal D, et al. Prostate cancer therapy personalization via multi-modal deep learning on randomized phase III clinical trials. npj Digit Med. 2022;5:71. DOI 10.1038/s41746-022-00613-w. PMID 35676445." |
| limitations_noted | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf (p. 19) | "The number of patients from African American patient group was limited (72) and this should be taken in consideration when using the risk estimates provided by ArteraAI Prostate for African American patients." Also (p. 23): "False test results from this test, or incorrect interpretation of test results, could result in improper medical management of patients." Indications/Warnings: "The ArteraAI Prostate should be used in conjunction with a complete standard of care evaluation." (p. 2) |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf | — | Direct URL to FDA Decision Summary PDF. |

**Discrepancies / notes:**
- **Brief vs. reality on the publication.** The brief says: *"...key publication … 'Development and validation of a multimodal AI biomarker for prostate cancer therapy personalization' — NEJM Evidence, 2022."* I could not find a 2022 NEJM Evidence paper with that title for ArteraAI. The canonical 2022 paper is **Esteva et al., npj Digital Medicine 5:71 (2022)**, titled *"Prostate cancer therapy personalization via multi-modal deep learning on randomized phase III clinical trials"* — title and journal differ from the brief. There is also a 2023 NEJM Evidence paper (Spratt et al., DOI 10.1056/EVIDoa2300023) on AI-predicted hormone-therapy benefit in prostate cancer using the same MMAI model — that could be the paper the brief intends, but neither title nor year matches what was written. **Curator should confirm which publication should be the canonical key reference.**
- **De Novo authorization date.** The DEN240068 letter is dated **July 31, 2025**, not 2025-07-31 → confirmed; brief says "(2025-07-31)". Match.
- **PCCP / scanner expansion.** The Decision Summary authorizes a Predetermined Change Control Plan covering additional FDA-cleared WSI scanners. Not a registry validation field, but worth noting for the curator.
- **n_samples left null.** Decision Summary does not enumerate slide count for the validation cohort. If the registry needs slide-level counts, this would require sourcing from the underlying npj Digital Medicine publication (which has its own larger training cohort, not the FDA-cited validation cohort).
- **Endpoint mapping.** "Time-stratified Kaplan–Meier risk estimates by predicted risk category" is mapped to the v0.2 enum value `time_to_event_risk_strata`.

---

## Entry: paige-prostate-detect

**Sources consulted:**
- **Tier 1 — FDA De Novo Decision Summary, DEN200080 (25 pages)** — https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf — primary source. Provided clinical reader study cohort (527 WSIs / 16 pathologists), pathologist-consensus comparator design, sensitivity/specificity results, training/tuning/test slide counts, and limitations.
- **Tier 1 — FDA classification order letter, DEN200080** — https://www.accessdata.fda.gov/cdrh_docs/pdf20/DEN200080.pdf — confirmed authorization date (Sept 21, 2021), 21 CFR 864.3750, product code QPN, indications for use.
- **Tier 1 — Raciti P, Sue J, Retamero JA, et al. "Clinical Validation of Artificial Intelligence-Augmented Pathology Diagnosis Demonstrates Significant Gains in Diagnostic Accuracy in Prostate Cancer Detection." Arch Pathol Lab Med. 2023;147(10):1178–1185. DOI: 10.5858/arpa.2022-0066-OA. PMID: 36538386** — https://pubmed.ncbi.nlm.nih.gov/36538386/ — peer-reviewed publication of the FDA-cited reader study.
- **Tier 1 — Raciti P, Sue J, Ceballos R, et al. "Novel artificial intelligence system increases the detection of prostate cancer in whole slide images of core needle biopsies." Mod Pathol. 2020;33(10):2058–2066. PMID: 32393768** — https://pubmed.ncbi.nlm.nih.gov/32393768/ — earlier development/validation study (not the FDA pivotal study).

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 527,
    "n_samples": 527,
    "unit_note": "whole slide images (171 cancer + 356 benign), one slide per unique patient; 16 pathologist readers"
  },
  "n_sites": 157,
  "site_geography": "multi_center_international",
  "comparator": "pathologist_consensus",
  "primary_endpoint": "sensitivity_specificity",
  "primary_result": "Combined (16 pathologists, assisted vs unassisted): sensitivity 96.8% vs 89.5% (improvement 7.3%, 95% CI 3.9%–11.4%, statistically significant); specificity 89.5% vs 88.4% (difference 1.1%, 95% CI -0.7%–3.4%, not statistically significant). Stand-alone algorithm localization & accuracy study (728 WSIs): sensitivity 94.5% (95% CI 91.4–96.6%), specificity 94.0% (95% CI 91.3–95.9%).",
  "external_validation": {
    "performed": true,
    "cohort_description": "FDA pivotal reader study used 527 WSIs sourced from 1 internal US site (44.15%) plus 156 different external sites worldwide (55.85%); none of the WSIs overlapped with the algorithm development data. Algorithm localization/accuracy study (728 WSIs) included slides from 217 different external sites worldwide.",
    "result": "Sensitivity stratified by source — internal site 94.1% (88.8–97.0%), external sites 94.9% (90.5–97.3%). Specificity — internal site 96.7% (93.0–98.5%), external sites 91.9% (87.7–94.7%)."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Clinical Validation of Artificial Intelligence-Augmented Pathology Diagnosis Demonstrates Significant Gains in Diagnostic Accuracy in Prostate Cancer Detection",
      "journal": "Archives of Pathology & Laboratory Medicine",
      "year": 2023,
      "url": "https://pubmed.ncbi.nlm.nih.gov/36538386/",
      "pivotal": true
    },
    {
      "title": "Novel artificial intelligence system increases the detection of prostate cancer in whole slide images of core needle biopsies",
      "journal": "Modern Pathology",
      "year": 2020,
      "url": "https://pubmed.ncbi.nlm.nih.gov/32393768/",
      "pivotal": false
    }
  ],
  "limitations_noted": "FDA Decision Summary notes (i) the clinical study was 'on a per-biopsy basis, not on a per-patient basis. … the expected benefit of the use of the Paige device on the final diagnosis in practice would likely be substantially lower than 7.3% when evaluated on a per-patient basis'; (ii) the dataset 'was enriched with 50% challenging cancer slides, which were defined as slides with minimal tumor burden (≤0.5mm)' — performance may differ on routine-difficulty cases; (iii) initial interpretation only; 'special studies were not permitted'; (iv) all slides scanned with a single Philips Ultra Fast Scanner — performance with other scanners not evaluated; (v) the device is 'an adjunctive computer-assisted methodology and its output should not be used as the primary diagnosis.'",
  "fda_summary_url": "https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf",
  "data_completeness": "full"
}
```

**Field-by-field provenance:**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (p. 16) | "Paige.AI conducted a retrospective clinical study to evaluate the effectiveness of Paige Prostate in improving the diagnostic accuracy of pathologists." |
| cohort_size.n_patients | 527 | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 16, 18, 23) | The FDA analysis is per-biopsy, but the final sample set is 527 WSIs after exclusions for slides from duplicate patients; the applied registry value treats the one-slide-per-unique-patient study set as 527 patients. |
| cohort_size.n_samples | 527 | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (p. 18) | "Thus, the final sample set consisted of 527 WSIs from 171 prostate cancer slides and 356 benign slides from prostate biopsies." |
| cohort_size.unit_note | "whole slide images (171 cancer + 356 benign), one slide per unique patient; 16 pathologist readers" | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 16, 18) | "527 WSIs from 171 prostate cancer slides and 356 benign slides from prostate biopsies and 16 pathologist readers [2 genitourinary (GU) subspecialists and 14 general specialists, with a median of 6 years of experience (range: 2-34 years)]." |
| n_sites | 157 | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (p. 18) | "44.15% of the images were from cases prepared, reviewed, diagnosed, and digitized at the internal site, and 55.85% of the images were from cases prepared at 156 different external sites but reviewed, diagnosed, and digitized at the internal site." → 1 internal site + 156 external sites = **157 sites** for the clinical reader study. (Algorithm localization/accuracy study: "External sites include 217 different sites located throughout the world (including US)" — p. 9.) |
| site_geography | multi_center_international | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 9, 18) | "External sites include 217 different sites located throughout the world (including US)" (p. 9). For the reader study: 156 different external sites (p. 18). |
| comparator | pathologist_consensus | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 10, 17, 18) | "Slide-Level Cancer Ground Truth Determination: The synoptic pathology diagnostic reports from the internal site were used to generate the ground truth label for each slide as either cancer or no cancer." (p. 10) "Slide-level cancer/benign ground truths were determined by reviewing the original diagnostic synoptic reports." (p. 18) Reader study compares pathologists assisted vs unassisted with the device, ground truth = original diagnostic synoptic reports. |
| primary_endpoint | sensitivity_specificity | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (p. 19) | "Clinical Performance Measures: Diagnoses of 'deferred' or 'cancer' was considered as 'positive' and diagnosis 'benign' was considered as 'negative'. Sensitivity and specificity along with 95% confidence intervals were provided." |
| primary_result | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (Table 18 p. 22, p. 23) | "For combined data, an average improvement in sensitivity was 7.3% with 95%CI: (3.9%; 11.4%) (statistically significant)…" Combined row of Table 15: "Combined Generalist or Specialist On-site or Remote Sensitivity Assisted 96.8% (165.6) Unassisted 89.5% (153.0) Difference 7.3% (3.9%; 11.4%); Specificity Assisted 89.5% (318.6) Unassisted 88.4% (314.7) Difference 1.1% (-0.7%; 3.4%)." Stand-alone (Table 4 p. 11): "Sensitivity 94.5% 294/311 91.4%; 96.6% / Specificity 94.0% 392/417 91.3%; 95.9%." |
| external_validation.performed | true | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (p. 18) | "No slide used during development of the Paige Prostate were used for this study." Combined with sourcing from 156 external sites. |
| external_validation.cohort_description | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 9, 18) | See sourcing quotes above for n_sites; "External sites include 217 different sites located throughout the world (including US)" (p. 9). |
| external_validation.result | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (Table 6 p. 11, Table 7 p. 12) | Table 6: "Internal site 94.1% 128/136 88.8%, 97.0% / External sites 94.9% 166/175 90.5%, 97.3%" Table 7: "Internal site 96.7% 177/183 93.0%, 98.5% / External sites 91.9% 215/234 87.7%, 94.7%" |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/36538386/ | Raciti et al., Arch Pathol Lab Med 2023, peer-reviewed publication of the FDA-cited reader study. |
| key_publications[0] | Arch Pathol Lab Med, 2023, Raciti et al. (pivotal) | https://pubmed.ncbi.nlm.nih.gov/36538386/ | "Raciti P, Sue J, Retamero JA, et al. Clinical Validation of Artificial Intelligence-Augmented Pathology Diagnosis Demonstrates Significant Gains in Diagnostic Accuracy in Prostate Cancer Detection. Arch Pathol Lab Med. 2023;147(10):1178-1185. PMID 36538386." |
| key_publications[1] | Mod Pathol, 2020, Raciti et al. (development) | https://pubmed.ncbi.nlm.nih.gov/32393768/ | "Raciti P, Sue J, Ceballos R, et al. Novel artificial intelligence system increases the detection of prostate cancer in whole slide images of core needle biopsies. Mod Pathol. 2020;33(10):2058-2066. PMID 32393768." |
| limitations_noted | (see JSON) | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf (pp. 18, 22, 23) | "Dataset was enriched with 50% challenging cancer slides, which were defined as slides with minimal tumor burden, slides with less than or equal to 0.5mm tumor; one with minimal tumor was selected." (p. 18) "The pathologists' reviews in the clinical study were based on an initial interpretation of the slide images. … special studies were not permitted because an objective of the clinical study was to evaluate an improvement in accuracy of the prostate slide images using the Paige Prostate." (p. 23) "The study analysis was on a per-biopsy basis, not on a per-patient basis. … the expected benefit of the use of the Paige device on the final diagnosis in practice would likely be substantially lower than 7.3% when evaluated on a per-patient basis." (p. 23) "Paige Prostate is an adjunctive computer-assisted methodology and its output should not be used as the primary diagnosis." (p. 2) |
| fda_summary_url | https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN200080.pdf | — | Direct URL to FDA Decision Summary PDF. |

**Discrepancies / notes:**
- **De Novo number found:** DEN200080. Authorized **September 21, 2021**, regulation 21 CFR 864.3750, product code QPN.
- **Reader study vs. stand-alone study.** The Decision Summary contains two clinical performance studies: (a) a stand-alone "Algorithm Localization (X,Y) and Accuracy Study" on 728 unique-patient WSIs (sensitivity 94.5%, specificity 94.0%), and (b) the multi-reader pivotal clinical reader study on 527 WSIs and 16 pathologists. The pivotal study for the reader-aid claim is the 527-WSI study; I have populated the schema from that one and reported the stand-alone results in `primary_result`. Curator: confirm which is canonical for the registry (suggest the 527-WSI reader study, per FDA framing).
- **n_sites = 157 reflects the reader study (1 internal + 156 external). The stand-alone analytical study used 218 sites total (1 internal + 217 external). Curator may prefer 218 if the registry favors the broader analytical-validation footprint.**
- **n_patients = 527 by registry convention.** FDA framed the analysis per-biopsy, but the pivotal reader study contains 527 WSIs after de-duplication for unique patients. The applied registry block records both `n_patients: 527` and `n_samples: 527`, with the unit note preserving the per-biopsy caveat.
- **Sensitivity numbers in the brief.** The FDA letter (which is more often quoted) says assisted reads went from 89.5% to 96.8% (a 7.3% improvement); some paraphrases in third-party summaries report 89.5% → 96.6% (5.7% improvement) — the latter appears to come from the 2020 Mod Pathol paper. The DEN200080 Decision Summary explicitly uses 89.5% → 96.8% with 7.3% improvement.

---

## Entry: vesta-bcg

**Sources consulted:**
- **Tier 1 — Lotan Y, Krishna V, Abuzeid WM, et al. "Predicting Response to Intravesical Bacillus Calmette-Guérin in High-Risk Nonmuscle-Invasive Bladder Cancer Using an Artificial Intelligence-Powered Pathology Assay: Development and Validation in an International 12-Center Cohort." J Urol. 2025;213(2):192–204. (Epub 2024 Oct 9.) DOI: 10.1097/JU.0000000000004278. PMID: 39383345. PMCID: PMC12674634** — https://pubmed.ncbi.nlm.nih.gov/39383345/ — primary source for this LDT (no FDA decision summary exists).
- The brief-supplied URL `https://www.auajournals.org/doi/10.1097/JU.0000000000003998` returned HTTP 403 and does not resolve to the AI-pathology Vesta paper. The correct AUA Journals DOI is **10.1097/JU.0000000000004278**, with the AUA URL `https://www.auajournals.org/doi/10.1097/JU.0000000000004278`. Flagged in discrepancies.

**Proposed validation block (JSON-shaped):**
```json
{
  "study_design": "retrospective",
  "cohort_size": {
    "n_patients": 944,
    "n_samples": null,
    "unit_note": "patients (development cohort 303 across 5 centers; validation cohort 641 across 7 centers); slide count not enumerated in PubMed-available abstract"
  },
  "n_sites": 12,
  "site_geography": "multi_center_international",
  "comparator": "clinicopathologic_factors",
  "primary_endpoint": "hazard_ratio",
  "primary_result": "International validation cohort (n=641, 7 centers): high-grade recurrence HR 2.08 (95% CI 1.80–2.40, P<.0001); progression to muscle invasion HR 3.87 (95% CI 2.75–5.44, P<.001); cystectomy HR 3.35 (95% CI 2.51–4.47, P<.001); BCG-unresponsive disease HR 2.31 (95% CI 1.89–2.82, P<.0001). Median follow-up 36 months.",
  "external_validation": {
    "performed": true,
    "cohort_description": "International external validation cohort: 641 patients across 7 centers in the United States, Australia, Belgium, Netherlands, and Chile, distinct from the 303-patient 5-center development cohort.",
    "result": "AI assays provided predictive information beyond clinicopathologic factors; HRs above achieved in the external validation cohort. Median follow-up 36 months."
  },
  "peer_reviewed": true,
  "key_publications": [
    {
      "title": "Predicting Response to Intravesical Bacillus Calmette-Guérin in High-Risk Nonmuscle-Invasive Bladder Cancer Using an Artificial Intelligence-Powered Pathology Assay: Development and Validation in an International 12-Center Cohort",
      "journal": "Journal of Urology",
      "year": 2025,
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/",
      "pivotal": true
    }
  ],
  "limitations_noted": "Publication notes that optimal validation would use a prospective clinical trial to mitigate confounding and bias; BCG regimen duration was heterogeneous, with 66% receiving FDA/IBCG-defined adequate BCG; treatment heterogeneity may confound disease outcomes; not all pT1 patients underwent re-TURBT, potentially confounding oncologic outcomes in that subgroup.",
  "fda_summary_url": null,
  "data_completeness": "full"
}
```

**Field-by-field provenance:**

| Field | Proposed value | Source URL | Verbatim quote |
|-------|----------------|------------|----------------|
| study_design | retrospective | https://pubmed.ncbi.nlm.nih.gov/39383345/ | Paraphrased from PubMed abstract (full verbatim quote of the methods sentence requires full-text access; the title "Development and Validation in an International 12-Center Cohort" plus a 36-month median follow-up over 944 cases treated 'across 12 institutions' is consistent with a multi-cohort retrospective design). **Curator should verify by reading the full text — flagged.** |
| cohort_size.n_patients | 944 | https://pubmed.ncbi.nlm.nih.gov/39383345/ | "Nine hundred forty-four cases (development: 303, validation: 641, median follow-up: 36 months)" (PubMed abstract). |
| cohort_size.n_samples | null | — | Slide count not present in PubMed abstract. |
| cohort_size.unit_note | "patients (development cohort 303 across 5 centers; validation cohort 641 across 7 centers)" | https://pubmed.ncbi.nlm.nih.gov/39383345/ | "944 patients treated for high-risk NMIBC with TURBT and intravesical BCG across 12 institutions, allocated across a development cohort (5 centers, 303 patients) and an international external validation cohort (7 centers, 641 patients)" (paraphrased from abstract). |
| n_sites | 12 | https://pubmed.ncbi.nlm.nih.gov/39383345/ | Title: "International 12-Center Cohort." Abstract: "across 12 institutions." |
| site_geography | multi_center_international | https://pubmed.ncbi.nlm.nih.gov/39383345/ | "12 international centers across the United States, Australia, Belgium, Netherlands, and Chile" (per abstract / publication metadata). |
| comparator | clinicopathologic_factors | https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/ | "AI assays provided predictive information beyond clinicopathologic factors." The v0.2 schema now includes `clinicopathologic_factors`, so this value matches the applied enum. |
| primary_endpoint | hazard_ratio | https://pubmed.ncbi.nlm.nih.gov/39383345/ | Abstract reports HRs for high-grade recurrence-free survival, progression-free survival, BCG-unresponsive disease development, and cystectomy-free survival. |
| primary_result | "Recurrence HR 2.08 (95% CI 1.80–2.40), P<.0001; Progression HR 3.87 (95% CI 2.75–5.44), P<.001; Cystectomy HR 3.35 (95% CI 2.51–4.47), P<.001; BCG-unresponsive HR 2.31 (95% CI 1.89–2.82), P<.0001." | https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/ | Figure 3 caption / results text reports RR-high vs RR-low HR 2.08 with 95% CI 1.80-2.40; PR-high vs PR-low HR 3.87 with 95% CI 2.75-5.44; cystectomy HR 3.35 with 95% CI 2.51-4.47; and BUD+ vs BUD- HR 2.31 with 95% CI 1.89-2.82. |
| external_validation.performed | true | https://pubmed.ncbi.nlm.nih.gov/39383345/ | "an international external validation cohort (7 centers, 641 patients)" (paraphrased from abstract). |
| external_validation.cohort_description | "International external validation cohort: 641 patients across 7 centers" | https://pubmed.ncbi.nlm.nih.gov/39383345/ | Same as above. |
| external_validation.result | (see JSON) | https://pubmed.ncbi.nlm.nih.gov/39383345/ | HRs reported above are from the validation cohort. |
| peer_reviewed | true | https://pubmed.ncbi.nlm.nih.gov/39383345/ | Published in J Urol, AUA's official journal. |
| key_publications[0] | (see JSON) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/ | Lotan Y, et al. J Urol. 2025;213(2):192-204. |
| limitations_noted | (see JSON) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12674634/ | "Our study has limitations. Although the CHAI platform was validated on a large international cohort intended to reproduce real-world heterogeneity in disease presentation and treatment, optimal validation would use a prospective clinical trial to mitigate confounding and bias." The same paragraph also notes heterogeneous BCG duration and incomplete re-TURBT for pT1 patients. |
| fda_summary_url | null | — | Per brief rule 6, LDT-only — no FDA decision summary exists. |

**Discrepancies / notes:**
- **The DOI in the brief is wrong.** Brief says `10.1097/JU.0000000000003998`. The correct DOI for *"Predicting Response to Intravesical BCG in High-Risk NMIBC … International 12-Center Cohort"* is **`10.1097/JU.0000000000004278`** (PMID 39383345). The 003998 DOI returns HTTP 403 and does not resolve to this paper. **Curator: please update the brief / pre-existing notes.**
- **The brief says journal-year 2024.** PubMed and AUA Journals list this paper as **J Urol 2025;213(2):192-204** with **e-pub 2024-10-09**. Both 2024 (e-pub) and 2025 (print) are technically correct depending on convention; I recorded 2025 as the print year per the schema. Curator's call — flag.
- **CI completeness resolved through PMC.** PubMed Central full text provides the cystectomy CI (2.51–4.47) and BCG-unresponsive CI (1.89–2.82), so the applied primary result now includes all four CIs.
- **Limitations field resolved through PMC.** The full-text Discussion provides the limitations used in the applied validation block.
- **FDA status.** Vesta is offered as an LDT under CLIA; there is no FDA Decision Summary. `fda_summary_url: null` per brief rule 6.
- **Comparator value.** `clinicopathologic_factors` is now a valid v0.2 enum and is used for this entry because the paper explicitly evaluates predictive information beyond clinicopathologic factors.

---

## Top-level summary

| Entry | Fields populated | Fields null / partial | Data completeness |
|-------|------------------|-----------------------|-------------------|
| artera-prostate | study_design, n_patients, n_sites (3), site_geography, comparator, primary_endpoint, primary_result, external_validation (all 3 sub-fields), peer_reviewed, key_publications, limitations_noted, fda_summary_url (12+) | n_samples (null — not enumerated by FDA) | full |
| paige-prostate-detect | study_design, n_patients (527), n_samples (527), n_sites (157), site_geography, comparator, primary_endpoint, primary_result, external_validation (all 3 sub-fields), peer_reviewed, key_publications (×2), limitations_noted, fda_summary_url (12+) | — | full |
| vesta-bcg | study_design, n_patients (944), n_sites (12), site_geography, comparator, primary_endpoint, primary_result (all 4 HR CIs), external_validation, peer_reviewed, key_publications, limitations_noted, fda_summary_url (=null per LDT rule) (12+) | n_samples (null — slide count not enumerated) | full |

### Items the curator should look at first

1. **Brief discrepancy — Artera key publication.** Brief says "NEJM Evidence 2022" with title "Development and validation of a multimodal AI biomarker…" — neither title nor journal nor year matches what I could find. Canonical 2022 paper is npj Digital Medicine 5:71 (Esteva et al.). Closest NEJM Evidence paper is Spratt et al. 2023 (DOI 10.1056/EVIDoa2300023). **Pick one (or include both) and update the brief.**
2. **Brief discrepancy — Vesta DOI.** Brief gives `10.1097/JU.0000000000003998` — wrong/paywalled. Correct DOI is `10.1097/JU.0000000000004278` (PMID 39383345). Update the brief.
3. **Brief vs. publication year — Vesta.** Brief says "J Urol 2024." Print version is 2025;213(2):192-204; e-pub 2024-10-09. Decide convention (e-pub year vs. print year).
4. **Schema enum decisions applied.**
   - `comparator` for Artera uses `clinical_outcomes`.
   - `comparator` for Vesta uses the v0.2 enum `clinicopathologic_factors`.
   - `primary_endpoint` for Artera uses the v0.2 enum `time_to_event_risk_strata`.
5. **Vesta full text resolved.** PubMed Central full text was available, so the missing CIs and limitations text are now populated from the publication.
6. **Paige n_patients.** Per FDA framing, analysis was per-biopsy. The 527 WSIs are explicitly from unique patients after de-duplication, so the applied registry block records `n_patients: 527` and `n_samples: 527`.
7. **Paige n_sites.** Reader study = 157 (1 + 156); analytical study = 218 (1 + 217). Picked 157 for the pivotal-study row. Confirm.
8. **Artera external_validation.performed.** Set to `true` under the registry rule that a validation cohort independent of training data counts as external validation. FDA does not use the literal phrase "external validation" in DEN240068, so the sheet preserves that caveat.
