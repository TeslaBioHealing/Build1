"""Build a Shopify product-import CSV (and per-product description HTML) from the product data."""
import csv, html, os, sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_products.py")
OUT = sys.argv[1]

# Load PRODUCTS without running the page generator.
src = open(SRC, encoding="utf-8").read()
ns = {}
exec(src[: src.index("HEADER = ")].replace("OUT = sys.argv[1]", "OUT = None"), ns)
PRODUCTS = ns["PRODUCTS"]

e = lambda s: html.escape(s, quote=False)

def ul(items):
    return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"

def body_html(p):
    out = [f"<p><strong>{e(p['subtitle'])}</strong></p>", f"<p>{e(p['purpose'])}</p>"]
    if p.get("intro_note"):
        out += [f"<p><small><strong>What Recovery Sleep™ means here:</strong> {e(p['intro_note'])}</small></p>"]
    out += ["<h3>General-Wellness Features</h3>", f"<p>{e(p['features_intro'])}</p>", ul(p["features"]), f"<p><em>{e(p['features_note'])}</em></p>"]
    out += ["<h3>Who May Enjoy It</h3>", f"<p>{e(p['who_intro'])}</p>", ul(p["who"]), f"<p><em>{e(p['who_note'])}</em></p>"]
    out += ["<h3>Your Daily Routine</h3>"]
    if isinstance(p["routine"][0], tuple):
        out += [f"<p><strong>{e(t)}:</strong> {e(d)}</p>" for t, d in p["routine"]]
    else:
        out += [ul(p["routine"])]
    out += [f"<p><em>{e(p['routine_note'])}</em></p>"]
    out += ["<h3>Directions for Use</h3>", "<ol>" + "".join(f"<li>{e(d)}</li>" for d in p["directions"]) + "</ol>"]
    out += ["<h3>Specifications</h3>", "<table><tbody>" +
            "".join(f"<tr><th style=\"text-align:left;vertical-align:top;padding:6px 12px 6px 0\">{e(k)}</th><td style=\"padding:6px 0\">{e(v)}</td></tr>" for k, v in p["specs"]) +
            "</tbody></table>"]
    out += ["<h3>Safety Information and Limitations</h3>", ul(p["safety"])]
    out += ["<h3>What Is Included</h3>", ul(p["included"]), f"<p><em>{e(p['included_note'])}</em></p>"]
    out += ["<h3>Frequently Asked Questions</h3>"]
    out += [f"<p><strong>{e(q)}</strong><br>{e(a)}</p>" for q, a in p["faq"]]
    out += ["<h3>Shipping</h3>", ul(p["shipping"]), "<h3>Returns</h3>", ul(p["returns"]),
            f"<h3>{e(p.get('warranty_title', 'Warranty'))}</h3>", ul(p["warranty"])]
    out += ["<h3>General Wellness Disclaimer</h3>"] + [f"<p><small>{e(x)}</small></p>" for x in p["disclaimer"]]
    out += [f"<p><small>{e(p['ack'])}</small></p>"]
    return "\n".join(out)

# Shopify-only fields not covered by the page data.
SHOP = {
    "biophotonizer-a": dict(type="Wellness Device", tags="Recovery Sleep, LIPG, Adult Wellness",
                            variants=[(None, "BHA-016", "445.00", "00860016414907", 998)]),
    "pillow": dict(type="Bedding", tags="Recovery Sleep, Pillow, Made to Order",
                   option="Firmness",
                   variants=[("Soft", "BPW-045-SOFT", "415.00", "", 0), ("Firm", "BPW-045-FIRM", "415.00", "", 0)]),
    "cornerstone": dict(type="Wellness Device", tags="Recovery Sleep, LIPG, Four-Unit System",
                        variants=[(None, "HPS-080", "9999.00", "", 48988)]),
    "qirenew-system": dict(type="Wellness Device", tags="Daily Wellness, LIPG, Four-Unit System",
                           variants=[(None, "BPP-040", "2290.00", "", 0)]),
    "enlova-water": dict(type="Bottled Water", tags="ENLOVA, Hydration, Water",
                         variants=[(None, "BPW500", "192.00", "", 0)]),
    "biophotonizer-alpha": dict(type="Wellness Device", tags="Recovery Sleep, LIPG, Adult Wellness",
                                variants=[(None, "BPA-032", "1250.00", "", 2654)]),
    "biophotonizer-c": dict(type="Wellness Device", tags="Recovery Sleep, LIPG, Family Wellness, Ages 5+",
                            variants=[(None, "BPC-012", "249.00", "", 544)]),
    "neck-pillow": dict(type="Comfort Accessory", tags="Recovery Sleep, Pillow, Travel",
                        variants=[(None, "BPN-030", "299.00", "", 0)]),
    "eyemask": dict(type="Comfort Accessory", tags="Recovery Sleep, Eyemask, Travel",
                    variants=[(None, "BPE-020", "199.00", "", 0)]),
    "enlova-water-bottle": dict(type="Drinkware", tags="ENLOVA, Hydration, Bottle",
                                variants=[(None, "BPW-075", "99.00", "", 998)]),
}

HEAD = ["Handle", "Title", "Body (HTML)", "Vendor", "Product Category", "Type", "Tags", "Published",
        "Option1 Name", "Option1 Value", "Variant SKU", "Variant Grams", "Variant Inventory Tracker",
        "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price",
        "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", "Image Src", "Image Position",
        "Image Alt Text", "Gift Card", "SEO Title", "SEO Description", "Variant Weight Unit", "Status"]

os.makedirs(os.path.join(OUT, "descriptions"), exist_ok=True)
rows = []
for p in PRODUCTS:
    s = SHOP[p["slug"]]
    body = body_html(p)
    with open(os.path.join(OUT, "descriptions", p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(body + "\n")
    for i, (opt, sku, price, barcode, grams) in enumerate(s["variants"]):
        r = dict.fromkeys(HEAD, "")
        r.update({"Handle": p["slug"], "Option1 Name": s.get("option", "Title") if i == 0 else "",
                  "Option1 Value": opt or "Default Title", "Variant SKU": sku, "Variant Grams": grams,
                  "Variant Inventory Policy": "deny", "Variant Fulfillment Service": "manual",
                  "Variant Price": price, "Variant Requires Shipping": "TRUE", "Variant Taxable": "TRUE",
                  "Variant Barcode": barcode, "Variant Weight Unit": "lb" if p["slug"] != "enlova-water" else "kg"})
        if i == 0:
            r.update({"Title": p["name"], "Body (HTML)": body, "Vendor": "Tesla BioHealing", "Type": s["type"],
                      "Tags": s["tags"], "Published": "FALSE", "Gift Card": "FALSE",
                      "SEO Title": p["seo_title"], "SEO Description": p["seo_desc"], "Status": "draft"})
        rows.append(r)

with open(os.path.join(OUT, "products_import.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HEAD)
    w.writeheader()
    w.writerows(rows)
print(len(rows), "rows")
