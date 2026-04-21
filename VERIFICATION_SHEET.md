# Registry batch-02 verification sheet — instructions

**File:** [`VERIFICATION_SHEET.csv`](./VERIFICATION_SHEET.csv) — 43 rows, one per batch-02 entry.

**Goal:** confirm the FDA status, pathway, decision date, and intended-use claim for each batch-02 entry before the July 2026 press push.

## How to use the sheet

Open `VERIFICATION_SHEET.csv` in Numbers, Excel, or Google Sheets (drag-and-drop works). Each row has:

| Column | What it is |
|--------|-----------|
| `id` | Registry entry ID (matches `v1/data.json`). |
| `product_name`, `company` | What the entry claims. |
| `cancer_type`, `modality` | For context. |
| `claimed_fda_status` | One of: 510(k) cleared, De Novo authorized, PMA approved, LDT, Research Use, Breakthrough Device Designation. |
| `claimed_pathway` | Regulatory pathway slug (510k / pma / de_novo / ldt / research_use). |
| `claimed_decision_date` | YYYY-MM or YYYY-MM-DD, or `null` if not yet populated. |
| `company_url` | Product page. Click through to confirm the product exists and the intended-use summary matches. |
| `fda_search_url` | Pre-built FDA database search link. Click and search by applicant name to find the 510(k) K-number, De Novo DEN-number, or PMA P-number. |
| `what_to_confirm` | The specific items you need to verify for this row. |
| `OK (tick)` | Fill with `x` when the row is verified. |
| `correction` | If a claimed field is wrong, put the correct value here (e.g. "510(k) number: K221234; decision 2022-11"). |
| `notes` | Any commentary. If the entry should be deleted or merged, say so here. |

## How long this takes

Average **~3 minutes per row** if the FDA database cooperates. 43 rows × 3 min = ~2 hours total. **Do it in batches of 10.** First batch of 10 is highest priority because it unblocks the press kit; the rest can slide through May–June.

## Verification workflow per row

1. **Read the claimed status** (`claimed_fda_status` + `claimed_pathway`).
2. **Click `company_url`** — confirm the product exists and that its current intended use matches what the sheet says. If the company has renamed, retired, or materially changed the product, note it in `correction` and `notes`.
3. **Click `fda_search_url`** if the row claims 510(k) / De Novo / PMA:
   - On the FDA 510(k) database, search by the company name in the "Applicant" field. Find the product. Capture the **K number** and the **decision date**.
   - On the De Novo database, find by company name. Capture the **DEN number** and date.
   - On the PMA database, find by company name. Capture the **P number** and date.
   - For LDT entries, the FDA DB won't have a record. Verify via the company's current Test Information / IFU.
4. **Fill in the sheet:**
   - If everything matches the claim → put `x` in `OK (tick)`. Done.
   - If the status / number / date is wrong → put the correct value in `correction`.
   - If the product has been retired or the entry should be deleted → say so in `notes`.
5. **Move on.** Do not try to verify more than the `what_to_confirm` column asks for. Pivotal publications, partner lists, and clinical evidence are NOT in scope for this verification pass.

## After you finish a batch

Email or Slack me the completed CSV (or just overwrite this file in the repo — the CSV is tracked). I will:
1. Apply every `correction` to `v1/data.json`.
2. Remove the flag from `NEEDS_VERIFICATION.md` for every `OK` row.
3. Re-run `scripts/validate.py` to confirm schema is still clean.
4. Commit + push; the site auto-deploys.

If you find **more than ~5 entries** need substantive correction, stop and tell me — it probably means I should change my sourcing approach for any future batches rather than fix them one by one.

## Quick links

- Live site: https://oncologyairegistry.org
- Underlying data: [`v1/data.json`](v1/data.json)
- Schema validator: [`scripts/validate.py`](scripts/validate.py)
- Existing verification tracker: [`NEEDS_VERIFICATION.md`](NEEDS_VERIFICATION.md)
- FDA 510(k) database: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm
- FDA De Novo database: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/denovo.cfm
- FDA PMA database: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pma.cfm
