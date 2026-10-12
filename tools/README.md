# Page build tools

The product data lives in `build_products.py` (first five products) and `new_products.py`, as written in
the product documents. `compliance.py` then applies the General Wellness Marketing Guide wording rules.

Rebuild everything from the repo root:

```
python3 tools/build_products.py wireframes/products
python3 tools/build_frontpage_row.py wireframes/frontpage.html
python3 tools/build_shopify.py shopify-import
```
