"""Rebuild the frontpage product row from the product data."""
import os, sys, html
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_products.py")
src = open(SRC, encoding="utf-8").read()
ns = {"__name__": "x"}
exec(src[: src.index("HEADER = ")].replace("OUT = sys.argv[1]", "OUT = None"), ns)
page = sys.argv[1]
s = open(page, encoding="utf-8").read()
start = s.index('<div class="product-row">')
end = s.index('</div>\n    </div>\n    <div class="genprompt" style="max-width:640px;margin:14px auto 0;">')
out = '<div class="product-row">\n'
for p in ns["PRODUCTS"]:
    name = html.escape(p["name"])
    if p.get("image"):
        media = (f'<div class="ph" style="padding:0;background:#fff;overflow:hidden;"><img src="assets/products/{p["image"]}" '
                 f'alt="{name}" style="width:100%;height:100%;object-fit:contain;"></div>')
    else:
        media = f'<div class="ph">[ {html.escape(p["short"])} — approved photo pending ]</div>'
    out += f'''        <a class="card" href="products/{p["slug"]}.html">
          {media}
          <div class="cat">{html.escape(p["category"])}</div>
          <h4 class="serif">{name}</h4>
          <div class="price">{html.escape(p["card_price"])}</div>
        </a>
'''
s = s[:start] + out + "      " + s[end:]
open(page, "w", encoding="utf-8").write(s)
print(len(ns["PRODUCTS"]), "cards")
