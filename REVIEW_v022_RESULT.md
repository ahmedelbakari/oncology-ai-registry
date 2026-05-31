# Independent Review — v0.2.2 cleanup batch (pre-commit)

**Reviewer:** Independent skeptical reviewer
**Date:** 2026-05-31
**Baseline:** commit `adebce0` (v0.2.1, 116 entries)
**Method:** Verified each change against the PRIMARY source (PubMed abstracts/full text via PMC, FDA accessdata PDF, company product pages), NOT against the maintainer's verification sheet. Ran `scripts/validate.py` (116 entries valid) and `scripts/build_pages.py` (regenerated cleanly), spot-checked rendered `v1/tools/*.html`.

---

## OVERALL VERDICT: APPROVE WITH FIXES

All 12 substantive claims verify correct against primary sources. There is **one concrete execution defect** that should be fixed before commit (a duplicated sentence in `ataraxis-breast-risk` limitations text, item 5). Everything else is clean. The science, regulatory statements, numbers, URLs, enums, dates, and presentation fixes all hold up. Fix the one duplication, re-run the build, and this is good to commit.

---

## Per-item findings (1–12)

### A. Newly populated entries

**1. vesta-risk-stratify — PASS**
Source: PubMed PMID 40514253 + PMC12718547 (European Urology 2025).
- 269 patients: CONFIRMED ("WSIs from 269 patients with HG Ta NMIBC were analyzed, none of whom were from the biomarker development set").
- 13 sites = 12 US + 1 Chile (Clínica Alemana, Santiago): CONFIRMED in PMC affiliations.
- HG-RFS CHAI HR 2.23 (1.45–3.44, p<0.001); AUA 1.93 (1.07–3.48, p=0.029); EAU 1.47 (0.96–2.23, p=0.074); MIBC-PFS CHAI 4.55 (1.39–14.92, p=0.012): ALL match the abstract exactly.
- `external_validation.performed = false`: **CONFIRMED CORRECT.** PMC describes a single retrospective multicenter analysis cohort with no separate independent external-validation cohort. The judgment call is right; the prior BCGPredict "international validation" framing was correctly dropped.
- key_publications URL now `https://pubmed.ncbi.nlm.nih.gov/40514253/` — resolves and title matches the published paper.
- Enums: `comparator=clinicopathologic_factors` (paper compares vs EAU/AUA guideline risk groups — correct fit), `primary_endpoint=hazard_ratio` (allowed; HG-RFS reported as HR — reasonable), `site_geography=multi_center_international` (12 US + 1 Chile — correct). All in the v0.2 controlled vocab per `scripts/validate.py`. Original precise labels preserved in `limitations_noted`.

**2. vitara-pancreas-chemopredict — PASS**
Source: PubMed PMID 41671529 abstract (JCO 2026; full text paywalled).
- 477 total = 178 dev + 299 validation; F-pref n=173, G-pref n=126: all match abstract.
- F-pref: TNTD 8.6 vs 7.5 mo (P=.035), OS 14.4 vs 11.7 mo (P=.003); G-pref: TNTD 9.6 vs 7.2 (P=.038), OS 14.3 vs 12.4 (P=.5 NS); interaction P<.001 TNTD, P=.005 OS: all match.
- `n_sites=null` + `data_completeness=partial`: HONEST. The abstract does not state site count; full text is paywalled. Marked partial appropriately, not lazily — every populated number is abstract-supported and the limitations note flags what couldn't be checked.
- Enums: `comparator=clinical_outcomes`, `primary_endpoint=other`, `site_geography=multi_center_international` — all allowed and defensible (TNTD/OS aren't in the endpoint enum, so "other" is the honest choice).
- key_publications URL now PubMed — resolves, title matches.

### B. Numerical correction

**3. signatera-mrd (829 plasma samples) — PASS**
Source: PubMed PMID 31070691 (Reinert 2019, JAMA Oncology). Abstract states verbatim: "Plasma samples (n = 829) were collected before surgery, postoperatively at day 30, and every third month for up to 3 years." The correction 795 → 829 is correct. (125 patients and "122 evaluable pre-op" left unchanged and consistent.)

### C. Regulatory contradiction fix (ldt true→false, RUO-in-US)

**4. aiforia-her2 / mindpeak-pdl1 / visiopharm-her2-connect — PASS**
RUO-in-US verified for each against company/primary sources:
- **aiforia-her2:** Aiforia Breast Cancer HER2 is "CE-IVD marked for diagnostic use in EU/EEA (IVDR) and for Research Use Only (RUO) and Performance Studies Only in all other market areas" — i.e. RUO in the US. Correct. `primary_markets` correctly dropped "US" → ["EU"].
- **mindpeak-pdl1:** Mindpeak's own product page states the PD-L1 product is "for research use only, not for use in diagnostic procedures" in the USA; CE-IVD in the EU. Correct. `primary_markets` → ["EU"].
- **visiopharm-her2-connect:** Visiopharm CE-IVD APPs are "not for sale in the USA" / research-use outside EU/UK. Correct. (Note: this entry's `primary_markets` was already ["EU"] in baseline — no change needed, consistent.)
All three keep `fda_status: "Research Use"`, `ce_marked: true`, `ldt: false`. Internally consistent and matches reality.

### D. Peer-review flag flip

**5. ataraxis-breast-risk (peer_reviewed false→true) — PASS on judgment, FAIL on execution (FIX REQUIRED)**
- **Judgment:** Defensible, NOT overclaiming, given the accompanying note. The analytical validation (Diagnostics 2026, MDPI) is a genuine peer-reviewed publication; the entry transparently states the headline clinical numbers (C-index, HRs, Oncotype DX head-to-head) are still arXiv preprint + ASCO 2025 abstract. `data_completeness` stays `partial`. A reader is not misled. I accept the flip.
- **DEFECT (must fix before commit):** The `limitations_noted` text contains a **duplicated sentence**. The newly prepended sentence ("Peer-review status: analytical validation IS peer-reviewed (Diagnostics 2026, MDPI); the headline clinical-validation numbers ... neither of which has completed peer review.") restates almost verbatim the pre-existing next sentence ("Analytical validation (Diagnostics 2026) is peer-reviewed; the clinical headline numbers ... neither has yet completed peer review."). This is a copy-paste artifact. It renders on the live page `v1/tools/ataraxis-breast-risk.html` ("is peer-reviewed" appears twice). Cosmetic but visible and sloppy. **Fix:** delete one of the two redundant sentences in `v1/data.json`, re-run `build_pages.py`.

### E. Text/labeling fixes

**6. artera-prostate intended_use (LDT→De Novo note) — PASS**
- DEN240068 decision date: FDA De Novo letter (accessdata.fda.gov/cdrh_docs/pdf24/DEN240068.pdf, retrieved via curl+pdftotext) is dated **July 31, 2025**. The data's `2025-07-31` is correct. (The 2025-08-13 figure floating around is just the company press-release date, not the FDA decision date.)
- "Originally offered as a laboratory-developed test": CONFIRMED — ArteraAI Prostate was/is offered as an LDT through Artera's CLIA-certified, CAP-accredited Jacksonville FL lab, predating the De Novo. Accurate.

**7. paige-her2 intended_use (H&E inference, no IHC) — PASS**
Paige HER2Complete detects HER2 expression from digital images of H&E-stained tissue "without the need for special staining approaches" — it infers HER2 from H&E, not from IHC interpretation. The corrected text matches the tool's actual mechanism. The old "AI assistant for HER2 IHC interpretation" was wrong.

**8. exact-oncotype-dx-breast source URL — PASS**
New URL `https://www.exactsciences.com/cancer-testing/oncotype-dx-breast-recurrence-score-invasive-ductal` resolves (HTTP 200) and is the correct Oncotype DX Breast Recurrence Score page. (The old `/products/oncotype-dx` would need separate confirmation of its 404; the replacement is valid regardless.)

### F. Presentation fixes

**9. build_pages.py (PRIMARY_ENDPOINT_LABEL + "Number of validation sites") — PASS**
Verified on rebuilt pages:
- `artera-prostate.html` renders "Time-to-event by risk category" (human label) instead of the raw enum `time_to_event_risk_strata`. Confirmed.
- `vesta-risk-stratify.html` renders "Hazard ratio" for `hazard_ratio`. Confirmed.
- Table label "Number of sites" → "Number of validation sites" renders correctly.
- Swept all 116 rendered pages for raw enum leaks: the only hit (`avenda-prostate-cancer-planning.html`) is a *preserved original label* inside a `[Source-detail: ...]` bracket in `limitations_noted` (`sensitivity_specificity_lesion_contouring`), not a mis-rendered endpoint cell. Not a bug. No actual enum leaks.

### G. Scope + metadata

**10. Tagline broadened ("diagnostic" → "diagnostic, predictive, and prognostic") — PASS**
Consistent across `index.html` (title, meta description, subtitle, h1), `methodology.html` (Purpose), `about.html` (Why this exists), `README.md`. Swept for residual "diagnostic"-only scope claims and the old "every AI-based diagnostic tool" h1 — none remain.

**11. README.md rewrite (v0.1/12 → v0.2/116) — PASS**
- Entry count 116 matches `data.json` (validator: "116 entries valid").
- Version v0.2 throughout; stale "v0.1 / 12 inaugural entries / roadmap" block removed.
- Citation block updated to `[v0.2]`.
- All internal links resolve: `v1/methodology.html`, `v1/about.html`, `v1/index.html`, `scripts/validate.py`, `scripts/build_pages.py`, and `CONTRIBUTING.md` all exist.

**12. Dates (last_updated, methodology date) — PASS**
- `data.json.last_updated` 2026-04-22 → 2026-05-31. Confirmed.
- `methodology.html` "May 7" → "May 31". Confirmed.
- Swept index/methodology/about/README for stale dates (May 7, 2026-04-22, April 22): none remain.

---

## New issues found (not on the maintainer's list)

1. **(Blocking-lite, item 5) Duplicated sentence in `ataraxis-breast-risk.limitations_noted`** — see item 5 above. The only required fix.
2. **(Non-blocking, note only) artera-prostate `fda_summary_url`** points to `https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN240068.pdf` (rendered link), but the De Novo decision letter actually lives at `.../cdrh_docs/pdf24/DEN240068.pdf` (the `/reviews/` path is where decision summaries usually sit, but the De Novo letter I retrieved was under `/pdf24/`). Worth a quick click-test that the `/reviews/` URL resolves; if it 404s, swap to the `pdf24` path. Not a baseline change in this batch, so not a blocker — flagging for hygiene.
3. **(Observation, not a defect)** vitara's `primary_endpoint=other` and vesta's `hazard_ratio` are both defensible, but note the registry now has two different conventions for time-to-event/HR endpoints (`hazard_ratio`, `time_to_event_risk_strata`, and `other`). Fine for v0.2; consider documenting the convention in methodology later.

---

## Pending parallel verification job — is the commit blocked?

The brief lists 2–3 facts still landing: replacement URL for `ibex-galen-prostate` (current source 404s), `fda_510k_number` + decision date for `icad-profound-ai-dbt`, and any numerical errors found in 9 other `full` entries.

**My position: NOT blocked by the pending job, with one caveat.**
- None of those pending facts touch the 12 items in this batch; this batch can commit on its own merits once the ataraxis duplication is fixed.
- HOWEVER: if the 9-entry deep-check is expected to surface numerical errors in *already-live* `full` entries, and you'd rather not ship a known-stale number twice, you may prefer to fold them into one commit. That's a release-hygiene preference, not a correctness blocker for *this* batch.
- The `ibex-galen-prostate` 404 source is a pre-existing defect already on the site (not introduced here), so it doesn't block this commit either — but it should be fixed before any public launch push.
- When those land, give them the same primary-source check: confirm the iCAD 510(k) number against the FDA 510(k) database (not the press release), and confirm the Ibex URL actually resolves to the matching product/paper.

---

## Bottom line

Verify-and-fix one thing (ataraxis duplicated sentence), re-run `scripts/build_pages.py`, and commit. All scientific, regulatory, numerical, URL, enum, date, and presentation claims in items 1–12 are correct against primary sources. The `external_validation.performed=false` call on vesta (the riskiest judgment) is right, the 829 correction is right, the three RUO-in-US flips are right, and the ataraxis peer-review flip is defensible as documented.
