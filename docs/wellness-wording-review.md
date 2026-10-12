# Wellness wording review — October 2026

Site copy checked against the **General Wellness Marketing Guide v2.0 (October 2026)**.
Scope: the frontpage, all 10 product pages, and the Shopify import descriptions,
including page titles, meta descriptions and image alt text.

## What changed

**Applied to every page**
- The footer and each product's disclaimer now use the guide's required disclaimer, copied exactly.
- Disease, symptom, treatment and medical-device words were removed or rewritten, including where they
  appeared as denials ("not intended to treat insomnia…", "no claim is made that it relieves pain…").
  The guide treats every word on the page as a claim.
- All mentions of the FDA were removed from page copy (guide rule 2: never borrow the FDA's authority).
  The approved "Is this FDA approved?" answer is for customer service, used only when a customer asks.
- FAQ entries framed around medical conditions were removed. That includes insomnia, sleep apnea, CPAP,
  neck pain, the spine, eye strain and vision, wrinkles, cell regeneration, medication, and children's
  behavior or development.
- Former product names were removed from public spec tables because they contain Red or Amber words:
  BioHealer for Children, BioPhoton Restorative Pillow, NeuroPhoton Vitality Matrix, Biophoton Eye Revive
  and Water Energizing System. They are kept in each page's internal review note.
- The guide's approved "Say this" lines were added as the first feature on Biophotonizer A, Biophotonizer C,
  QiRenew, Pillow, Neck Pillow, Eyemask and ENLOVA™ Water Bottle.
- Safety warnings were kept but reworded without symptom lists ("Stop using it if it feels uncomfortable,
  irritates the skin, or ever makes breathing feel restricted").

**Frontpage**
- Removed: "2.7-Fold CD34+ Marker Study", the "stem cell markers" article, "Peer-Reviewed Research",
  "backed by extensive research", "Boost Vitality & Energy", "Peer Reviewed · Biohack Yourself",
  "The Science of Light", "Wake Up to Renewed Energy" and "Mental Focus".
- The feature spotlight now shows Biophotonizer A with the guide's approved positioning line and the
  "Passive: no lasers, no heat, no cords, nothing to set up" line.

All rewrites live in one file, `tools/compliance.py`, so each change can be reviewed. The original product
documents were left unchanged.

## Open items for Regulatory (Amber: check first)

| Item | Where | Why it needs review |
|---|---|---|
| **"Recovery Sleep™" program name** | 7 product pages, frontpage cards | "Recovery" is an Amber word. The program name appears on every Recovery Sleep page, so it needs sign-off or a new name. |
| "36 months" expected service period | Biophotonizer A and Alpha, Cornerstone, QiRenew | Numbers and durations ("lasts 3+ years") need test data on file. The 36-month warranty is a policy, not a claim, so it is fine. |
| "Approximately three years" service period | Biophotonizer C | Same as above. |
| "Up to 72 hours" expansion period | Pillow | A duration; confirm it through packaging validation. |
| Product names vs. the guide | All | The guide uses "CornerStone System", "Biophoton Pillow", "Energized Neck Pillow", "Energized Eye Mask", "Water Energizing System & Bottle" and "Energized Spring Water". The product documents and the site use "Cornerstone", "Pillow", "Neck Pillow", "Eyemask", "ENLOVA™ Water Bottle" and "ENLOVA™ Water". The guide requires one official name everywhere, and the product documents avoid "energized". Pick one set. |
| "Mental acuity" in the approved lines for Alpha and CornerStone | Not used | Amber (FTC-level evidence needed), so these lines were left off the site until reviewed. |
| Label correction log (Appendix A) | Product labels | The packaging fixes for C, Neck Pillow, Alpha, Eye Mask, etc. are a Product & Labeling task. The website now follows the same wording. |

## Still to do before launch
- Old pages and URLs: the guide calls out `/stem-renew-at-home` and `/products/overnight-medbed-session-woburn-ma`.
  Redirect or unpublish them in the live store. They are not part of this site build.
- Shopify: re-import or paste the updated descriptions so the live product pages match.
- Run the guide's Section 6 checklist and log the approval date.
