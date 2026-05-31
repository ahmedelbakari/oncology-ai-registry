# Pre-Launch Review

**Reviewer:** independent adversarial pass
**Date:** 2026-05-12
**Verdict:** GO WITH FIXES

## Top-line summary

The registry is substantively serious work — methodology is sound, the 17 `full` entries I spot-checked are grounded in real primary sources, partial entries are unusually honest about their gaps, and stub entries are flagged with an explicit "not yet populated" banner. **Do not launch as-is, though.** There are five concrete, fast-to-fix issues that a STAT reporter or a landscape-paper author would catch in the first hour: a numerical error in a `full` entry, two broken citation URLs, raw enum strings rendering on every detail page, a stale GitHub README that contradicts the live site, and three different "last updated" dates across the site. All are fixable in 1–2 evenings. After those fixes, ship it.

## Critical issues (MUST fix before launch)

1. **Numerical discrepancy in a `full` entry — Signatera cohort_size.**
   `v1/data.json` (`signatera-mrd`, `validation.cohort_size.unit_note`) says "795 longitudinal plasma samples". The Reinert 2019 JAMA Oncology paper (PMID 31070691) abstract states **"Plasma samples (n = 829) were collected before surgery, postoperatively at day 30, and every third month for up to 3 years."** Either fix to 829 or document why 795 is the right denominator (e.g., evaluable subset). This is the single most embarrassing thing in the registry — a curator who can't get the headline number of his pivotal paper right erodes trust in every other claim. Fix: edit `unit_note` to match the published 829 (or add an analytical-denominator explanation). 5 min.

2. **Raw enum strings render on every full/partial tool detail page.**
   `scripts/build_pages.py:134` outputs `v.get("primary_endpoint")` directly, so the public tool pages display `time_to_event_risk_strata`, `sensitivity_specificity`, `ppv_npv` verbatim instead of human labels. I confirmed this live on https://oncologyairegistry.org/tools/artera-prostate.html — the "Primary endpoint" cell literally reads `time_to_event_risk_strata`. This screams "draft" and undermines the citation-readiness pitch. Fix: add a `PRIMARY_ENDPOINT_LABEL` dict in build_pages.py (mirroring `COMPARATOR_LABEL`/`DESIGN_LABEL`) and rebuild all 30 affected pages. 15 min including rebuild.

3. **Two broken primary-source URLs in `full` entries.**
   - `ibex-galen-prostate` source → `https://ibex-ai.com/galen-prostate/` returns 404 (Ibex restructured their site).
   - `exact-oncotype-dx-breast` source → `https://www.exactsciences.com/products/oncotype-dx` returns 404. Replace with `https://www.exactsciences.com/cancer-testing/oncotype-dx-breast-recurrence-score-invasive-ductal` (confirmed live).
   Run a link-check on the full set before launch; even one dead link in a `full` entry is bad optics. 20 min.

4. **GitHub README contradicts the live site.**
   `README.md` still says "v0.1 preview · 12 inaugural entries", "domain to be registered", and a roadmap with v0.2 = "30+ entries". Live site is v0.2 / 116 entries. README is the first thing a journalist clicks from the site nav. Update version, entry count, the roadmap section (or delete it), and the citation block (currently shows `[v0.1]`). 20 min.

5. **"Last updated" date is inconsistent in three places.**
   - `methodology.html` line 25: "Version 0.2 — last updated May 7, 2026"
   - `v1/data.json` `last_updated`: `2026-04-22` (shown in index footer and on all 116 tool pages)
   - Recent commits adding 13 new entries (`d7ed94d` on May 12) are not reflected in `last_updated`.
   Pick one truth, propagate, and update both `data.json.last_updated` and the methodology page to today's actual date as part of any pre-launch commit. This matters because the citation block tells people to cite by version + date. 5 min.

## Important issues (SHOULD fix before launch)

6. **Tagline–scope mismatch.** Hero on index.html says "every AI-based diagnostic tool in U.S. oncology" but ~18 entries (Vesta BCG, ArteraAI, Oncotype DX, MammaPrint, Decipher, Prolaris, the Ataraxis trio, Castle DecisionDx, Veracyte Prosigna, Owkin RlapsRisk, Stratipath, Vitara, etc.) are predictive/prognostic, not diagnostic. ~16% of the registry contradicts the tagline. Recommended change (already on your open-items list): "AI-based diagnostic, predictive, and prognostic tools." Update in `index.html` (hero h1 and meta description), `methodology.html` (Purpose paragraph), `about.html` (Why this exists), README, and the schema-version metadata if appropriate.

7. **19 FDA-authorized entries lack their FDA submission number.**
   17 entries marked `510(k) cleared` have no `fda_510k_number`, 1 `De Novo` has no `fda_de_novo_number`, 1 `PMA approved` has no `fda_pma_number`. One of those (`icad-profound-ai-dbt`) is `full`. Without a 510(k)/PMA/De Novo number a reader cannot cross-check the regulatory claim in the FDA database — which is the registry's central credibility claim. Affected IDs: `lunit-insight-mmg`, `deephealth-saige-q`, `icad-profound-ai-dbt`, `icad-profound-risk`, `screenpoint-transpara`, `volpara-scorecard`, `therapixel-mammoscreen`, `riverain-clearread-ct`, `aidoc-oncology`, `koios-ds-thyroid`, `cellavision-dc1`, `scopio-hemaq`, `lunit-insight-cxr`, `qure-qxr`, `paige-breast`, `aiforia-clinical-prostate`, `vuno-med-lungct-ai`, `deepbio-deepdx-prostate`, `guardant360-cdx`. Fixing all 19 may not be tractable in 18 days; fixing the `full` entry (icad-profound-ai-dbt) is mandatory; fixing 5–10 of the highest-profile stubs (Lunit, Volpara, Transpara, qXR, Guardant360 CDx) would close the worst gaps.

8. **CONTRIBUTING.md describes a workflow that doesn't work and `build.py` is broken.**
   CONTRIBUTING.md tells a contributor to copy `_template.yaml`, fill it in, then run `python3 scripts/build.py` to regenerate `data.json`. But `scripts/build.py` reads only `v1/entries/*.yaml` (which currently contains just `_template.yaml`) and would write a `data.json` with **zero entries** and `schema_version: "0.1"`. A new contributor following the docs literally would either be very confused or PR a destructive change. Either: (a) fix `build.py` to use `data.json` as source-of-truth and just validate/regenerate pages, or (b) update CONTRIBUTING.md to reflect the actual hand-edit workflow, or (c) delete `build.py` and the template. Pick one.

9. **ArteraAI shows both "De Novo authorized" badge AND "LDT: Yes" without explanation.**
   On https://oncologyairegistry.org/tools/artera-prostate.html the regulatory table has both fields true. Technically correct (it was offered as an LDT pre-De Novo and is now the first AI prostate prognostic to clear De Novo), but to a journalist the juxtaposition looks like a data error. Add a one-line note in `intended_use` or a `regulatory.note` field: "Originally offered as an LDT; FDA De Novo authorized 2025-07-31 (DEN240068)."

10. **`paige-her2` `intended_use` is misleading.** Says "AI assistant for HER2 IHC interpretation in invasive breast cancer." But the cited pivotal paper (Clinical Breast Cancer 2025) and the entry's own `limitations_noted` make clear the tool infers HER2 status from **H&E images alone, not IHC**. Fix `intended_use` to "AI inference of HER2 status from H&E-stained breast cancer slides (no IHC required)."

11. **"Number of sites" column will be widely misread.** Several full entries (e.g., `tempus-xt` shows `n_sites: 1`) reflect the *manufacturing/CLIA lab* site, not validation cohort diversity. A casual reader sees "1 site, US single-center" next to a PMA-approved test and assumes weak validation. The unit_note clarifies but it's buried. Either separate `n_sites_lab` from `n_sites_validation`, or rename the table label to "Number of validation sites" and require this to refer to validation cohort sites only.

## Nice-to-have (optional)

12. **Sources sections on full-entry tool pages don't include the FDA decision summary URL** (only the manufacturer/company link). The FDA URL appears in the validation table but not in the Sources list. Adding it is a one-line change in build_pages.py and improves citation hygiene.
13. **Mobile UX:** the 6-column registry table is wrapped in `overflow-x-auto`, so it horizontal-scrolls on phones. Usable but ugly. A simple `<details>` per row or a column-collapse at narrow widths would be nicer (not a launch blocker).
14. **Pre-rendered SEO/social-preview content is empty.** Entry count and last-updated in the footer are populated by JS after `fetch('data.json')`. Real users with JS are fine; Twitter/LinkedIn link cards and a `curl` of the homepage show "— entries · last updated [blank]". Consider server-side stamping the count into the static HTML during release.
15. **Citation block on tool pages doesn't include an entry version or last-modified date.** Says "Accessed [date]" but not "Last revised [date]". For long-term citability, per-entry change history (or at minimum a `last_modified` per entry) would matter.
16. **Validator dead code:** `ALLOWED_DATA_COMPLETENESS` in `scripts/validate.py:81` includes `stub_phase1`, which no entry uses. Harmless but worth pruning.
17. **`tempus-xt` `company` field reads "Tempus AI"** — correct since the 2024 NASDAQ rename. Fine, but ensure historical citations to "Tempus Labs" are searchable (the search box in index.html searches `product_name + company + cancer_types + intended_use`, so a search for "Tempus Labs" would miss this entry. Consider an `aliases` field.

## Dimension scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Data integrity | **3.5** | 17/17 full entries spot-checked map to real FDA filings or PubMed-indexed papers. One numerical error found (Signatera 795 vs 829). Two broken source URLs. 19 FDA-authorized entries missing their submission numbers. The signal-to-noise is good but not press-ready. |
| Methodology defensibility | **4** | Methodology page is genuinely strong: clear inclusion/exclusion, explicit source hierarchy, comparator/endpoint taxonomies are well-thought-out, completeness asymmetry is acknowledged honestly. COI section is adequate (curator works at Valar, products are listed under same rules; could be slightly stronger by stating no editorial advantage was given to Valar entries — currently implied, not stated). Missing: explicit refresh cadence in days (says "quarterly + 2 weeks for material updates" — fine), explicit deprecation/removal policy, formal versioning of individual entries. |
| Scope coherence | **2.5** | The tagline–content mismatch is real. ~16% of entries are not "diagnostic." Several of the highest-profile entries (Artera, Vesta, Oncotype, MammaPrint) are predictive/prognostic. Either narrow the scope or — much better — broaden the tagline. The scope decision is on the open-items list; resolving it before launch matters. |
| UX / presentation | **3** | Index page works, filters work, table is readable. Stub pages have an honest amber "not yet populated" banner — that's well done. But the raw enum on every full/partial page (`time_to_event_risk_strata`, etc.) is a visible flaw. Mobile is usable but the wide table is awkward. Sources sections are inconsistent. |
| Citation-readiness | **3** | Per-tool URLs are stable and canonical-tagged — good. Citation block format is reasonable. But date is inconsistent across pages (May 7 in methodology, April 22 in data.json/footer). The "until methods paper is published, cite this" framing is fine but the per-version stability needs to actually be honored — each release tag needs a frozen URL. |
| Launch-readiness | **2.5** | The 6 open items listed in the brief (methodology white paper, press kit, endorsements, scope decision, plus the data/UX fixes I'm raising) are not all going to land cleanly in 18 days. Endorsements alone — sending an ask, waiting for response, drafting a quote, getting approval — typically takes 2–4 weeks per ask. Realistic launch is mid-to-late June for a polished press push; end-of-May is feasible only for a quieter soft launch. |

## Spot-check details

**Full entries verified against primary sources:**

- **vesta-bcg** (Valar Labs · LDT): J Urol 2024/Feb 2025 paper confirmed via PMC12674634; HRs 2.08 / 3.87 / 2.31 / 3.35 match the entry verbatim; 944 patients / 303-dev / 641-validation / 12 centers all match. PASS.
- **paige-prostate-detect** (De Novo DEN200080): FDA Decision Summary PDF loads, decision date 2021-09-21 matches (FDA database confirms applicant Paige.AI, device "Paige Prostate"). Sensitivity 96.8% vs 89.5% AI-assisted vs unassisted matches the FDA SSED. PASS.
- **artera-prostate** (De Novo DEN240068): FDA De Novo database confirms decision date 2025-07-31, applicant "artera, inc.", device "ArteraAI Prostate". 886 / 3 US sites matches the validation paper. PASS on numbers; FAIL on UX (raw enum + LDT/De Novo dual-flag confusion).
- **signatera-mrd** (LDT): PubMed 31070691 confirms title, journal, 125 patients. **FAIL on plasma sample count** — entry says 795, abstract says 829. Other numbers (HR 7.2 / 43.5, 88% surveillance sensitivity, 98% specificity) match. One numerical error.
- **hologic-genius-ai-detection** (K201019): K201019 confirmed via FDA 510(k) database; manufacturer Hologic; decision 2020-11-09. FDA SSED PDF loads. AUC 0.825 vs 0.794 numbers are SSED-traceable. PASS.
- **grail-galleri** (LDT): PATHFINDER paper PMID 37805216 confirmed — Lancet 2023, 6,621 analysable participants, 92 signals, PPV 38%, all match. PASS.
- **exact-oncotype-dx-breast** (LDT): PMID 29860917 confirmed as TAILORx NEJM 2018. Sources URL broken (404). FAIL on URL.
- **tempus-xt** (PMA P210011): FDA PMA confirmed; SSED PDF loads. Concordance numbers per the SSED. PASS on numbers; n_sites=1 is misleading without explanation (it's the lab, not validation cohorts).

**Partial entries reviewed:**
- `ibex-galen-breast`, `paige-lymph-node`, `paige-her2` — partial-data caveats are unusually honest ("full text required to populate", "95% CIs not visible in available abstract", "FDA status is Breakthrough Device Designation only — not a market authorization"). `paige-her2` `intended_use` mislabels the modality (H&E vs IHC). Otherwise impressive transparency for partials.

**Stub entries reviewed:** `qure-qxr`, `aignostics-raptor`, `roche-upath-her2-breast`, `castle-decisiondx-sqcc` all render with the explicit amber "Validation summary not yet populated. … queued for v0.3" banner. This is the right call — visitors won't be misled into thinking blank = no evidence. Good.

**Regulatory-contradiction check:** the earlier `proscia-concentriq-ai` issue (Research Use + 510(k) number) is resolved (now `Research Use` + `ce_marked: true` + no 510(k) number). No other current contradictions of that type found across 116 entries.

## Recommendation

**GO WITH FIXES.** The substance is real and the registry is the only thing of its kind that I'm aware of in the public domain. Don't launch with `time_to_event_risk_strata` on the marquee Artera page, a wrong sample count on the marquee Signatera page, dead links in two `full` entries, a README that says v0.1 / 12 entries, and three different "last updated" dates.

**Conditions that flip my answer to a clean GO:**
1. Fix the five critical issues (Signatera 795→829, primary_endpoint label rendering, two broken URLs, README, dates) — half a day of work.
2. Make the scope-language decision on the open-items list (broaden tagline) and propagate it — 30 minutes.
3. Add the FDA submission number to `icad-profound-ai-dbt` (the only full entry missing one) — 5 minutes.

**Conditions that flip my answer to NO-GO:**
- Launching the press push without first finding/fixing whatever other Signatera-style numerical errors exist in the remaining 16 full entries. I only spot-checked 8/17 closely; the Signatera 795-vs-829 finding suggests there may be 1–2 more. A 30-minute self-audit pass (curator re-reads each full entry's `primary_result` and `cohort_size.unit_note` against the cited PubMed/FDA URL) is cheap insurance.

**On the end-of-May timeline specifically:** end-of-May is realistic for the *site* if the critical fixes go in this week. End-of-May is **not** realistic for the press push, because endorsement quotes from Elkhanany/Gerrard haven't been requested yet and that pipeline is 2–4 weeks. Recommend: ship the site fixes by 2026-05-20, post a "v0.2 quietly live" tweet/LinkedIn, then run the press push 2–3 weeks later with endorsements in hand.
