"""Generate product detail page wireframes from the five rewritten product documents."""
import html, re, sys, os

OUT = sys.argv[1]

def esc(s):
    s = html.escape(s, quote=False)
    # Bracketed text in the source docs = content still awaiting confirmation.
    return re.sub(r"\[([^\]]+)\]", r'<span class="pending">[\1]</span>', s)

RS_ROUTINE_NOTE = None

PRODUCTS = [
# ------------------------------------------------------------------ BIOPHOTONIZER A
dict(
  slug="biophotonizer-a",
  program="Recovery Sleep™",
  category="Recovery Sleep™",
  name="Tesla BioHealing® Biophotonizer A",
  short="Biophotonizer A",
  subtitle="Compact Recovery Sleep™ Companion for Adult General Wellness",
  price="$445.00", price_alt="",
  card_price="$445.00",
  meta=[("Model","Biophotonizer A"),("SKU","BHA-016"),("GTIN","00860016414907")],
  qty_label="One Biophotonizer A",
  purpose="Tesla BioHealing® Biophotonizer A is an optional, passive, noninvasive Tesla BioHealing® Low-Intensity Photon-Generator (LIPG) designed to complement Recovery Sleep™, an adult general-wellness program centered on consistent bedtime habits, relaxation, and responsible self-care.",
  image=None,
  photo_guidance="Use current photographs showing the front, back, sides, top, product scale, package contents, product label, and safe placement near a bed, desk, chair, or quiet relaxation area. Avoid medical settings, anatomical graphics, clinical-study imagery, before-and-after comparisons, or visual effects suggesting treatment.",
  thumbs=["Front","Back / label","Scale","Package contents","Bedside placement"],
  facts=[("Power","None — passive, no plug or battery"),("Size","≈ 3.4\" dia × 4\" H · 2.2 lb"),("Service period","36 months"),("Made in","United States")],
  review_note="Use only current, label-matched product photographs and final approved Instructions for Use. Publish photon-output or comparative-performance statements only after product-specific technical and regulatory approval.",
  conflicts=["Price: product-detail table lists $445.00; the add-to-cart table says “confirm approved price — source draft lists $345.00 and $299.00”. Page shows $445.00 until confirmed.",
             "Availability: [Confirm current inventory status]."],
  features_intro="Within Recovery Sleep™, Biophotonizer A may serve as an optional, non-powered cue for a calm and repeatable wellness routine.",
  features=["Complements a consistent bedtime and waking schedule",
            "Accompanies quiet activities such as reading, breathing, meditation, or reflection",
            "Fits alongside everyday relaxation and stress-management practices",
            "Supports a dedicated, uncluttered sleep or wellness space",
            "Operates passively without plugs, batteries, charging, software, or wireless connection",
            "Provides a compact format suitable for a bedroom, desk, office, or travel setting",
            "Can remain nearby during ordinary rest or quiet-time activities",
            "Serves as one optional element within a broader healthy lifestyle"],
  features_note="These statements describe a general-wellness role only. No medical, clinical, sleep, or physiological outcome is promised.",
  who_intro="This product may appeal to adults who want to:",
  who=["Create a calmer and more consistent bedtime environment",
       "Add a passive product to an evening wind-down routine",
       "Make time for relaxation, meditation, or quiet reflection",
       "Pair a wellness product with reading, desk work, or other quiet activities",
       "Follow a repeatable prepare-for-rest, protect-the-night, and begin-again rhythm",
       "Include personal vitality, balance, or qi-related practices in a general-wellness routine",
       "Use a compact format suitable for a bedroom, desk, office, or travel setting"],
  who_note="Recovery Sleep™ and this product are not intended for a symptom, diagnosis, disease, injury, pain, sleep disorder, or other medical condition.",
  routine=[("Prepare for Rest","Place the product on a dry, stable surface near the bed or another approved wellness area. Dim the lights and begin a calm activity such as reading, breathing, meditation, or reflection."),
           ("Protect the Night","Keep the room comfortable, quiet, darkened, and uncluttered. Maintain a consistent bedtime and leave the product safely positioned according to its instructions."),
           ("Begin Again","Wake at a consistent time, keep walkways clear, return the product to a safe location if it was moved, and continue ordinary daytime activities."),
           ("Everyday Wellness","Outside the bedroom, the product may accompany quiet desk, reading, meditation, or reflection time in an appropriate location.")],
  routine_note="Healthy habits remain the foundation of Recovery Sleep™. This product is optional and does not replace adequate rest, balanced nutrition, appropriate physical activity, relaxation, or professional care.",
  directions=["Remove the product from its packaging and confirm that the label, model, and SKU match your order.",
              "Inspect the product for visible damage before use.",
              "Place it on a dry, stable surface where it cannot fall, tip, or create a tripping hazard.",
              "Position the unit within approximately three feet of the personal wellness area, subject to the final approved instructions. A new user may begin three to six feet away if permitted by those instructions.",
              "Use it during ordinary rest, reading, work, meditation, or relaxation according to the supplied instructions.",
              "No plug, battery, charging, software connection, or direct body contact is required.",
              "Do not position the product to target a symptom, injury, painful area, or medical condition.",
              "Keep the product clean, dry, intact, and stored according to the care instructions.",
              "The final product label and Instructions for Use control if they differ from this website draft."],
  specs=[("Product name","Tesla BioHealing® Biophotonizer A"),
         ("Product category","Tesla BioHealing® Low-Intensity Photon-Generator (LIPG) for adult general wellness"),
         ("Model","Biophotonizer A"),("SKU","BHA-016"),("GTIN","00860016414907"),
         ("Intended user","Adult"),
         ("Dimensions","Approximately 3.4 inches in diameter × 4 inches high"),
         ("Weight","Approximately 2.2 lb"),
         ("Operation","Passive, solid-state operation"),
         ("External power / batteries / charging","None required"),
         ("Intended setting","Bedroom, home, office, travel, or designated Recovery Sleep™ wellness space, as appropriate"),
         ("Placement","Position the unit within approximately three feet of the personal wellness area, subject to the final approved instructions. A new user may begin three to six feet away if permitted by those instructions."),
         ("External housing","Metal and plastic; confirm exact approved materials"),
         ("Internal composition","Activated mineral composite; confirm the exact approved description"),
         ("Photon characterization","Publish only after product-specific technical and regulatory approval"),
         ("Surface-temperature information","Room temperature, subject to validated product-specific testing"),
         ("Expected service period","36 months"),
         ("Country of manufacture","United States"),
         ("Manufacturer","Tesla BioHealing, Inc., Delaware")],
  safety=["For adult general-wellness use only. Use only as directed.",
          "Place the product on a dry, stable surface and keep it out of walkways.",
          "Do not ingest, open, puncture, crush, cut, burn, heat, drill, modify, or intentionally damage the product.",
          "Do not use a product that is cracked, leaking, visibly damaged, or missing its label.",
          "Keep the product dry and away from excessive heat, open flame, young children, and pets.",
          "Do not use the product to target a symptom, injury, painful area, or medical condition.",
          "Do not use it as a substitute for sleep, nutrition, physical activity, professional healthcare, or emergency assistance.",
          "The product does not provide medical measurements, alarms, diagnoses, or treatment guidance.",
          "Discontinue use and contact Customer Support if the product is damaged or does not perform as described in its instructions."],
  included=["One Tesla BioHealing® Biophotonizer A","Approved product label","Placement guidance","Directions for Use",
            "General safety and product-care information","Warranty information","Protective retail packaging"],
  included_note="A carrying tote, protective sleeve, and other accessories are sold separately unless the selected offer expressly includes them.",
  faq=[("Does it require electricity or charging?","No. It operates passively and requires no plug, external power source, battery, charging, software, or wireless connection."),
       ("How does it fit into Recovery Sleep™?","Place it safely near a bed or quiet wellness area during the Prepare for Rest stage, then follow the approved placement and distance instructions supplied with the product."),
       ("How long may I use it?","Use it for the duration stated in the final Instructions for Use. It is designed for passive use during ordinary rest, work, reading, meditation, or relaxation."),
       ("Do I need to touch or wear it?","No. Direct body contact is not required."),
       ("Does it emit visible light?","Low-intensity photon emission is characterized with specialized optical equipment and may not be visible to the unaided eye. This is a physical product description, not a medical claim."),
       ("Does it treat insomnia, pain, or another medical condition?","No. Recovery Sleep™ is a general-wellness program, and this product is an optional wellness product. Neither is intended for diagnosis, treatment, cure, mitigation, or prevention of disease."),
       ("Can Customer Support recommend it for my symptoms?","No. Customer Support may explain product features and approved directions but cannot diagnose symptoms or recommend a product for a medical condition."),
       ("Can I use more than one unit?","Additional units may be placed in separate personal wellness spaces. No particular medical, biological, sleep, or wellness outcome is promised from using multiple units."),
       ("How long does it last?","The expected service period is 36 months. Final labeling and warranty terms control."),
       ("What maintenance is required?","No charging or electrical maintenance is required. Keep the product clean, dry, intact, and stored according to the supplied care instructions.")],
  shipping=["Shipping availability: Delaware and eligible U.S. destinations","Shipping charge: Calculated at checkout",
            "Estimated processing time: 1–3 business days","Estimated delivery time: 2–5 business days to a U.S. address",
            "Tracking information will be provided when available"],
  returns=["Return window: 60 calendar days after delivery","Required condition: Like-new condition with all included materials",
           "Return authorization: Required before shipment","Restocking fee: 10% of the purchase price for an accepted non-defective return",
           "Customer responsibility: Follow the complete Return and Refund Policy and return-shipping instructions"],
  warranty=["Warranty period: 36 months","Coverage: Qualifying defects in materials or workmanship while the product remains intact and is used as directed",
            "Exclusions: Misuse, accidental damage, unauthorized opening or modification, and failure to follow instructions",
            "Proof of purchase is required. The complete Product Warranty controls."],
  disclaimer=["Recovery Sleep™ is a general-wellness program. This Tesla BioHealing® product is an optional product for adult general-wellness use. Neither the program nor the product is intended to diagnose, treat, cure, mitigate, or prevent a disease, sleep disorder, injury, pain, or other medical condition.",
              "The product does not provide medical measurements or clinical guidance and is not a substitute for professional healthcare or an FDA-authorized medical device. Do not use product information to make decisions about medication or medical care.",
              "Physical measurements of photon emission, wavelength, intensity, surface temperature, or comparative output describe product characteristics under stated test conditions. They do not establish medical effectiveness or guarantee a sleep or wellness outcome.",
              "Individual experiences vary. No particular benefit, result, or timeframe is promised. Consult a qualified healthcare professional about medical concerns or healthcare decisions."],
  cta="Add Biophotonizer A to Cart", cta_disabled=False,
  ack="By proceeding to checkout, the purchaser acknowledges the product's optional role in Recovery Sleep™, its adult general-wellness purpose, directions, safety information, return terms, warranty, and General Wellness Disclaimer.",
  seo_title="Recovery Sleep™ Biophotonizer A | Tesla BioHealing®",
  seo_desc="Explore Tesla BioHealing® Biophotonizer A, an optional passive companion for adult Recovery Sleep™ and everyday general-wellness routines.",
),
# ------------------------------------------------------------------ PILLOW
dict(
  slug="pillow",
  program="Recovery Sleep™",
  category="Recovery Sleep™",
  name="Tesla BioHealing® Pillow",
  short="Pillow",
  subtitle="Recovery Sleep™ Comfort Pillow for Adult Bedtime Routines",
  price="$415.00", price_alt="One pillow · Soft or Firm",
  card_price="$415.00",
  meta=[("Model","Vita-45"),("SKU","BPW-045")],
  qty_label="One pillow",
  options=("Firmness", ["Soft","Firm"], "Soft: higher-loft, plush feel. Firm: more structured feel."),
  purpose="Tesla BioHealing® Pillow is an optional adult comfort product within Recovery Sleep™. It provides ordinary cushioning and may incorporate verified Tesla BioHealing® LIPG material as a passive general-wellness feature.",
  image="pillow.png", image_alt="Adult holding a white Tesla BioHealing pillow",
  photo_guidance="Use current photographs of the exact Soft and Firm versions, package contents, labels, pillow scale, vacuum packaging, and the pillow fully expanded inside a conventional pillowcase. Do not imply treatment, airway management, cervical correction, pain relief, or a guaranteed sleep result.",
  thumbs=["Soft version","Firm version","In pillowcase","Vacuum packaging","Label"],
  facts=[("Size","Standard · ≈ 20 × 26 × 6 in (expanded)"),("Power","None required"),("Made","To order · ≈ 7–10 days [confirm]"),("Made in","USA")],
  review_note="Confirm the bill of materials, exact fiber content, care label, expansion period, and flammability labeling before publication. Require the customer to select Soft or Firm before adding the pillow to the cart.",
  conflicts=["Price: product-detail table lists $415.00; the add-to-cart table lists $495.00. Page shows $415.00 until confirmed.",
             "Availability: [Confirm Made to Order / In Stock status].",
             "Former names (BioPhoton Restorative Pillow; NeuroPhoton Vitality Matrix) are kept in specs for reference only — do not use in marketing."],
  features_intro="The pillow is designed to make an adult bedtime setting comfortable and inviting.",
  features=["Provides ordinary cushioning for the head and neck","Offers Soft and Firm choices for individual comfort preference",
            "Uses a standard-size format suitable for many conventional pillowcases","Complements consistent bedtime and waking routines",
            "Requires no electricity, batteries, charging, software, or setup","May be used for nighttime rest or quiet relaxation",
            "May incorporate verified Tesla BioHealing® LIPG material as a passive wellness feature"],
  features_note="No faster sleep onset, longer sleep, improved sleep stages, greater energy, improved cognition, better circulation, or accelerated recovery is promised.",
  who_intro="The pillow may appeal to adults who:",
  who=["Want a standard-size pillow for ordinary sleep comfort","Are creating a calmer and more consistent bedtime environment",
       "Prefer a softer or firmer feel","Use reading, breathing, meditation, or quiet time before bed",
       "Prefer a non-powered wellness accessory","Want a made-to-order pillow in a familiar residential format"],
  who_note="Fit and comfort depend on anatomy, sleep position, mattress firmness, and personal preference. Anyone requiring medical positioning, airway management, postsurgical support, or treatment should consult a qualified professional.",
  routine=[("Prepare for Rest","Place the pillow in a clean, dry pillowcase, dim the lights, and allow time for reading, breathing, meditation, or quiet relaxation."),
           ("Protect the Night","Keep the room comfortable, quiet, and darkened; maintain a consistent bedtime; and use the selected firmness in a comfortable position."),
           ("Begin Again","Rise at a consistent time, air the pillow as appropriate, and return to ordinary daytime activities."),
           ("Care","Keep the pillow clean and dry and follow separate approved instructions for the cover and internal core.")],
  routine_note="The pillow is an optional comfort element. Healthy, repeatable habits remain the foundation of Recovery Sleep™.",
  directions=["Confirm that the selected Soft or Firm version was delivered and inspect the packaging, pillow, seams, closure, and labels.",
              "Remove the pillow carefully from its vacuum-sealed packaging and place it in a clean, dry, ventilated area.",
              "Allow up to 72 hours for expansion only if that period appears in the final approved instructions.",
              "Place the fully expanded pillow in a clean, appropriately sized pillowcase.",
              "Position it beneath the head and neck in a way that feels comfortable for the user's normal sleep position.",
              "Do not force the head or neck into a particular alignment or stack pillows to a height that interferes with breathing, swallowing, or movement.",
              "Stop use or reposition the pillow if it causes pain, numbness, tingling, breathing difficulty, skin irritation, headache, dizziness, or unusual discomfort.",
              "Follow the care label. Do not immerse the internal core, machine-wash it, or expose it to high heat unless expressly permitted."],
  specs=[("Product name","Tesla BioHealing® Pillow"),
         ("Former names","BioPhoton Restorative Pillow; NeuroPhoton Vitality Matrix"),
         ("Model / SKU","Vita-45 / BPW-045"),
         ("Purchase quantity","One pillow in the selected firmness"),
         ("Intended user","Adults"),
         ("Finished size","Approximately 20 × 26 × 6 inches after full expansion"),
         ("Firmness options","Soft or Firm"),
         ("Soft version","Higher-loft, plush feel — confirm final construction description"),
         ("Firm version","More structured feel — confirm final construction description"),
         ("Cover","Poly-cotton — [insert exact verified fiber percentages]"),
         ("Internal construction","Confirm bill of materials before publishing foam or fill claims"),
         ("Integrated material","Tesla BioHealing® LIPG material — confirm exact approved description"),
         ("External power / charging","None required"),
         ("Shipping configuration","Vacuum-sealed in a reusable bag — confirm"),
         ("Expansion period","Up to 72 hours — confirm through packaging validation"),
         ("Care","[Insert approved cover and core instructions separately]"),
         ("Flammability and law labels","Confirm applicable federal and state requirements"),
         ("Production time","Made to order; approximately 7–10 days — confirm"),
         ("Country of origin / manufacturer","USA / Tesla BioHealing, Inc."),
         ("Expected life","Confirm through durability testing")],
  safety=["For adult use only. Keep the pillow and plastic packaging away from infants and young children.",
          "Never place the pillow or packaging over the mouth or nose. Remove plastic packaging promptly after opening.",
          "Keep away from open flame, cigarettes, heaters, heating pads, electric blankets, and high-temperature sources.",
          "Do not cut, puncture, burn, or dismantle the pillow or incorporated materials.",
          "Use only after the pillow has fully expanded according to approved instructions.",
          "Stop use if it causes pain, numbness, tingling, breathing difficulty, skin irritation, headache, dizziness, or unusual discomfort.",
          "Do not use as a cervical brace, immobilizer, medical-positioning product, airway-management product, or rehabilitation device.",
          "CPAP and other medical-equipment compatibility has not been established.",
          "Review the complete material disclosure if the user has allergies or sensitivities.",
          "Inspect periodically and discontinue use if the cover, seams, core, fill, or incorporated material becomes damaged or exposed."],
  included=["One Tesla BioHealing® Pillow in the selected firmness","Removable pillow cover — [if confirmed]",
            "Reusable vacuum-storage or shipping bag — [if confirmed]","Expansion and setup instructions","Care and safety instructions","Warranty documentation"],
  included_note="A pillowcase, bedding, replacement cover, sleep monitor, medical equipment, and other Tesla BioHealing® products are not included unless expressly stated.",
  faq=[("How does the pillow fit into Recovery Sleep™?","It is an optional comfort product that may accompany the Prepare for Rest, Protect the Night, and Begin Again routine."),
       ("Does it treat insomnia or sleep apnea?","No. It is not intended to diagnose, treat, cure, mitigate, or prevent a sleep disorder or medical condition."),
       ("Does it guarantee deeper, longer, or faster sleep?","No. No sleep duration, stage, quality, onset, wellness result, or timeframe is promised."),
       ("What is the difference between Soft and Firm?","Soft is intended to feel plusher and higher-loft; Firm is intended to feel more structured. Final descriptions must match verified construction."),
       ("What if I do not select a firmness?","A Soft or Firm selection is required before checkout; no version is selected automatically."),
       ("Why does it arrive compressed?","Vacuum packaging reduces shipping volume. Allow the approved expansion period before use."),
       ("What materials are used?","[Publish only the verified bill of materials and exact fiber content. Do not use unverified memory-foam or open-cell-foam descriptions.]"),
       ("Is the entire pillow machine washable?","Do not machine-wash or immerse the internal core unless the approved care label expressly permits it."),
       ("Does it require electricity?","No. It requires no electricity, batteries, charging, software, or wireless connection."),
       ("Can it be used with a CPAP mask?","Compatibility has not been established. It must not interfere with mask fit, airflow, tubing, prescribed positioning, or operation.")],
  shipping=["Made-to-order product — [confirm the production period before publication]",
            "[Confirm whether the stated 7–10 days covers production only or production plus shipping]",
            "[Display eligible destinations, shipping charges, carrier, tracking, estimated transit time, and international duties before purchase]",
            "Inspect the package promptly and retain it until the pillow has fully expanded and been evaluated"],
  returns=["Return window: 30 calendar days after delivery for unopened, eligible products with prior authorization",
           "Made-to-order cancellation: Within 24 hours after purchase if production or customization has not begun",
           "Opened, used, slept-on, washed, or otherwise handled bedding is not returnable for hygiene reasons, except when damaged, defective, or incorrect",
           "Returned items must be unused, unwashed, clean, odor-free, and free of stains, hair, pet dander, smoke, fragrance, bodily fluids, or other contamination",
           "Return the product in its original sealed packaging with all labels, accessories, instructions, and included materials",
           "Customer pays return shipping for a non-defective return; the company covers reasonable return shipping for a confirmed defect or fulfillment error",
           "Approved non-defective returns may be subject to a 15% restocking and handling fee"],
  warranty=["Warranty period: [Insert approved term]",
            "The final warranty should address manufacturing defects; cover, seams, closure, core, and fill; normal compression and loft changes; misuse and cleaning damage; firmness preference; proof of purchase; remedies; shipping; and geographic limits."],
  disclaimer=["Recovery Sleep™ is a general-wellness program, and Tesla BioHealing® Pillow is an optional adult comfort product for ordinary rest, relaxation, and healthy sleep-management routines.",
              "Neither the program nor the pillow is intended to diagnose, treat, cure, mitigate, or prevent insomnia, sleep apnea, pain, injury, fatigue, cognitive impairment, a breathing disorder, or another medical condition. The pillow is not a medical positioning product, cervical brace, airway-management product, or rehabilitation device.",
              "No claim is made that the pillow changes sleep stages, improves REM sleep, causes faster sleep onset, increases sleep duration, improves circulation, enhances brain function, stimulates cellular activity, or accelerates recovery.",
              "Individual fit, comfort, and sleep experiences vary. No result or timeframe is promised. References to LIPG material or physical measurements describe the product only and do not establish a medical, physiological, cognitive, or sleep benefit."],
  cta="Add Selected Pillow to Cart", cta_disabled=True,
  ack="By proceeding to checkout, the purchaser acknowledges that the pillow is an optional adult comfort and general-wellness product, has selected a firmness, and has reviewed its care, hygiene-return, safety, warranty, and disclaimer terms.",
  seo_title="Recovery Sleep™ Comfort Pillow | Tesla BioHealing®",
  seo_desc="Choose Soft or Firm Tesla BioHealing® Pillow as an optional adult comfort companion for a consistent Recovery Sleep™ bedtime routine.",
),
# ------------------------------------------------------------------ CORNERSTONE
dict(
  slug="cornerstone",
  program="Recovery Sleep™",
  category="Recovery Sleep™",
  name="Tesla BioHealing® Cornerstone",
  short="Cornerstone",
  subtitle="Four-Unit Recovery Sleep™ Wellness-Space System",
  price="$9,999.00", price_alt="One complete four-unit system",
  card_price="$9,999.00",
  meta=[("Model","Cornerstone"),("SKU","HPS-080")],
  qty_label="Four units · one system",
  purpose="Tesla BioHealing® Cornerstone is an optional, passive, noninvasive four-unit LIPG system designed to help adults create a dedicated environment for Recovery Sleep™, consistent relaxation habits, and responsible self-care.",
  image="cornerstone.jpg", image_alt="Four gold Tesla BioHealing Cornerstone units",
  photo_guidance="Use current photographs showing all four Cornerstone units, each unit from multiple angles, package contents, labels, safe handling, and the approved four-unit room arrangement. Photographs must not imply a clinical, regenerative, or treatment environment.",
  thumbs=["Single unit","Unit — side","Room arrangement","Package contents","Safe handling"],
  facts=[("System","4 units sold together"),("Per unit","≈ 12.5 × 12.5 × 3 in · 27 lb"),("Power","None required"),("Shipping","Free to eligible U.S. destinations")],
  review_note="Confirm the final SKU and approved placement diagram before publication. This listing is for one complete four-unit system; individual units are not sold under this SKU.",
  conflicts=["SKU: product-detail table lists HPS-080; specs table says “confirm — HPS-080 or BPS-080”.",
             "Price: product-detail table lists “$9,999.00 per four-unit system or $2999/Unit”, but the same document says individual units are not sold under this SKU. Page shows the system price only.",
             "Availability: [Confirm current inventory status]."],
  features_intro="Cornerstone provides a coordinated four-unit format for an adult bedroom, meditation room, living area, or designated wellness space.",
  features=["Creates a clear environmental cue to begin an evening wind-down","Complements consistent bedtime and waking schedules",
            "Accompanies reading, meditation, breathing, or quiet reflection","Supports a calm, uncluttered space for ordinary relaxation",
            "Operates passively without household electricity, batteries, charging, or software","Allows adults to share a nonmedical general-wellness space",
            "Fits alongside personal vitality, balance, or qi-related wellness practices","Uses four coordinated units positioned according to the approved placement guide"],
  features_note="Cornerstone does not provide thermal therapy, acoustic therapy, electrical stimulation, medical monitoring, treatment, or a guaranteed sleep outcome.",
  who_intro="Cornerstone may appeal to adults who:",
  who=["Want a coordinated four-unit system for a dedicated wellness area","Have safe, stable floor space in a bedroom, meditation room, or quiet living area",
       "Follow relaxation, mindfulness, or consistent bedtime routines","Prefer passive products that do not require charging or household electricity",
       "Want a shared general-wellness environment for ordinary quiet activities","Can safely receive, move, and position four heavy units"],
  who_note="A shared room does not establish or guarantee equal exposure, benefit, or outcome. Cornerstone is not intended for diagnosis, treatment, rehabilitation, sleep-disorder management, or disease prevention.",
  routine=[("Prepare for Rest","Dim the lights, reduce unnecessary noise, and choose a calm activity such as reading, breathing, meditation, or reflection."),
           ("Protect the Night","Keep the room comfortable and uncluttered, maintain a consistent bedtime, and leave all four units safely positioned according to the approved diagram."),
           ("Begin Again","Rise at a consistent time, keep exits and walkways clear, and return to ordinary daytime activities."),
           ("Shared Wellness Time","Adults may use the space for quiet reflection, reading, meditation, gentle stretching, or other ordinary nonmedical activities.")],
  routine_note="Direct body contact and active interaction are not required.",
  directions=["Confirm that the shipment contains all four Cornerstone units and the required instructions.",
              "Inspect every unit, strap, handle, housing, and package for visible damage.",
              "Each unit weighs approximately 27 lb. Use appropriate lifting methods, moving equipment, and assistance.",
              "Do not lift, carry, drag, or support a unit by the decorative handle.",
              "Place each unit flat on a dry, level, stable floor capable of supporting its weight.",
              "Arrange all four units around the selected wellness area exactly as shown in the final approved placement diagram.",
              "Keep units away from beds, furniture, stairs, exits, walkways, heat, water, and unstable surfaces as directed.",
              "Do not sit, stand, sleep, stack, or place furniture on the units.",
              "No plug, battery, charging, software, wireless connection, or direct body contact is required."],
  specs=[("Product name","Tesla BioHealing® Cornerstone"),
         ("Product category","Tesla BioHealing® Low-Intensity Photon-Generator (LIPG) system"),
         ("Model","Cornerstone"),
         ("SKU","[Confirm — HPS-080 or BPS-080]"),
         ("System configuration","Four passive units sold together as one system"),
         ("Intended user","Adults"),
         ("Dimensions per unit","Approximately 12.5 × 12.5 × 3 inches"),
         ("Weight per unit","Approximately 27 lb / 12.25 kg"),
         ("Approximate total weight","108 lb / 49 kg"),
         ("Operation","Passive, solid-state; no external power, battery, or charging"),
         ("Suggested environment","Bedroom, meditation room, living area, or designated Recovery Sleep™ wellness space"),
         ("Placement","Four-unit perimeter arrangement; final diagram and distances must be approved"),
         ("Handle","For limited positioning assistance only; not for lifting or carrying"),
         ("Securing straps","Keep fitted unless approved instructions state otherwise"),
         ("External housing","ABS plastic; confirm final material description"),
         ("Internal composition","Mineral-based composite; confirm exact approved description"),
         ("Cleaning","Wipe the exterior gently with a clean, soft, dry cloth"),
         ("Coverage area","No specific square-foot coverage is claimed"),
         ("Multi-user performance","Individual experiences vary; no equal exposure, benefit, or outcome is promised"),
         ("Expected service period","36 months"),
         ("Manufacturer / origin","Tesla BioHealing, Inc. / United States")],
  safety=["For adult general-wellness use only.",
          "Use safe lifting methods, appropriate moving equipment, and assistance. Do not lift by the handle.",
          "Place every unit on a stable, level, dry floor. Do not use elevated or unstable surfaces.",
          "Do not stack units or place them where they create a trip, impact, doorway, or exit hazard.",
          "Do not sit, stand, climb, or place furniture or heavy objects on a unit.",
          "Do not open, puncture, cut, crush, dismantle, burn, or intentionally heat a unit.",
          "Keep the system dry and away from liquids, excessive moisture, extreme heat, open flame, children, and pets.",
          "Do not use a unit with damaged housing, straps, handle, or internal structure.",
          "Do not rely on Cornerstone for medical measurements, alarms, diagnosis, treatment decisions, or emergency assistance."],
  included=["Four Tesla BioHealing® Cornerstone units","Approved four-unit placement guide","Instructions for Use",
            "Safety, handling, and care information","Warranty documentation","Protective shipping packaging"],
  included_note="Furniture, dollies, moving equipment, room installation, and other Tesla BioHealing® products are not included unless expressly stated.",
  faq=[("How many units are included?","Four Cornerstone units are sold together as one complete system."),
       ("Can I purchase one unit?","Not under this SKU. Any individual-unit offer requires a separate name, SKU, price, instructions, and approved purpose statement."),
       ("Does it require electricity?","No. The system requires no household electricity, batteries, charging, software, or wireless connection."),
       ("Where should the units be placed?","Use the approved four-unit placement diagram and keep all units away from exits, walkways, water, heat, and unstable surfaces."),
       ("Does Cornerstone cover 400 square feet?","No specific square-foot coverage is claimed. Room size and distance are arrangement factors, not medical exposure measures."),
       ("May several adults share the space?","Yes, for ordinary general-wellness activities. No equal exposure, benefit, or result is promised."),
       ("Do four units create a stronger field?","No field-strength, coherence, synchronization, or comparative-performance claim is made without validated testing and approval."),
       ("Does it treat a sleep disorder or medical condition?","No. Recovery Sleep™ and Cornerstone are for general wellness only."),
       ("How long is the system expected to remain usable?","The expected service period is 36 months. Final labeling and warranty terms control."),
       ("What maintenance is required?","No electrical maintenance or charging is required. Inspect each unit and follow the approved cleaning, handling, and care instructions.")],
  shipping=["The four-unit system is expected to ship in two packages",
            "Approximate weight per package: 60 lb — [confirm before publication]",
            "Approximate package dimensions: 15 × 12 × 6 inches — [confirm before publication]",
            "Shipping and handling: Free shipping to eligible U.S. destinations",
            "Processing: 1–3 business days; estimated U.S. delivery: 2–5 business days",
            "Inspect all packages promptly. Retain packaging and photograph any damage before installation"],
  returns=["Request a return within 30 calendar days after delivery of the complete four-unit set.",
           "After authorization, ship the return within 14 calendar days using the approved RMA and return address.",
           "Return all four units together in clean, undamaged, unmodified, like-new condition with labels, instructions, and included materials.",
           "Use the original protective packaging or obtain approval for equivalent packaging.",
           "For a non-defective return, the customer is responsible for freight, insurance, tracking, and safe delivery.",
           "Accepted non-defective returns are subject to a 15% restocking fee based on the net product price paid.",
           "Verified defects, shipping damage, or fulfillment errors are not subject to the restocking fee.",
           "Financed and promotional purchases are adjusted according to the financing agreement and the complete return policy."],
  warranty=["Warranty period: 36 months",
            "[The complete warranty must identify coverage for the system and individual units, qualifying defects, exclusions, proof-of-purchase requirements, remedies, shipping responsibilities, and geographic limits.]"],
  disclaimer=["Recovery Sleep™ is a general-wellness program, and Tesla BioHealing® Cornerstone is an optional system for adult routines involving relaxation, bedtime consistency, everyday stress management, personal vitality, and qi-related wellness practices.",
              "Neither Recovery Sleep™ nor Cornerstone is intended to diagnose, treat, cure, mitigate, or prevent a disease or sleep disorder. They do not replace medical advice, treatment, medication, rehabilitation, or emergency care.",
              "Photon-output data, placement arrangements, room dimensions, and other physical characteristics describe the product only. They do not establish medical effectiveness, clinical benefit, or a sleep outcome.",
              "Individual experiences vary. No particular benefit, result, or timeframe is promised or guaranteed. General-wellness positioning does not mean the product has FDA clearance or approval for a medical purpose."],
  cta="Add One Four-Unit Cornerstone System to Cart", cta_disabled=False,
  ack="By proceeding to checkout, the purchaser acknowledges that Cornerstone is one four-unit adult general-wellness system and has reviewed its handling, placement, safety, delivery, return, warranty, and disclaimer terms.",
  seo_title="Recovery Sleep™ Cornerstone System | Tesla BioHealing®",
  seo_desc="Explore Tesla BioHealing® Cornerstone, a passive four-unit system for creating a dedicated adult Recovery Sleep™ and general-wellness space.",
),
# ------------------------------------------------------------------ QIRENEW
dict(
  slug="qirenew-system",
  program="General Wellness",
  category="Daily Wellness",
  name="Tesla BioHealing® QiRenew System",
  short="QiRenew System",
  subtitle="Four-Unit System for Rest, Relaxation, and Everyday Wellness",
  price="$2,290.00", price_alt="per set of four · or $625 per item",
  card_price="$2,290.00 / set",
  meta=[("Model","BPP-040"),("SKU","BPP-040")],
  qty_label="One set of four Biophotonizer Plus units",
  purpose="The Tesla BioHealing® QiRenew System is a collection of four passive LIPG units designed to complement adult routines involving relaxation, restful surroundings, quiet time, and personal well-being.",
  image="qirenew-system.png", image_alt="Four gold Biophotonizer Plus units",
  photo_guidance="Use current photographs of the exact four-unit configuration, package contents, labels, and the final approved arrangement in a home relaxation setting. Do not use medical, cellular-regeneration, treatment, or before-and-after imagery.",
  thumbs=["Single unit","Label","Approved arrangement","Package contents","Home setting"],
  facts=[("System","4 Biophotonizer Plus units"),("Power","None — no household power or batteries"),("Service period","36 months [confirm]"),("Made in","USA [confirm]")],
  review_note="Confirm the approved four-unit arrangement, distance, dimensions, weight, materials, return period, warranty term, and final price before publication. Do not use the former internal name CellRenew as a consumer-facing cellular-regeneration claim. Per the source document, the purchase button should remain disabled until the configuration, photographs, price, SKU, specifications, instructions, labeling, returns, and warranty receive documented approval.",
  conflicts=["Naming: the source document mixes “QiRenew System” with “Daily Wellness System” (features, FAQ, disclaimer, CTA, SEO). This page uses QiRenew System throughout — confirm the final consumer name.",
             "Availability: [Confirm current inventory status]."],
  features_intro="The QiRenew System is designed to:",
  features=["Complement a calm and comfortable home environment","Encourage consistency in personal relaxation routines",
            "Fit into quiet-time, meditation, and bedtime rituals","Provide a passive, noninvasive experience without complicated controls",
            "Remain in a designated home wellness area after safe setup","Operate without household power, batteries, or charging",
            "Support a general sense of well-being as part of a healthy lifestyle"],
  features_note="Individual experiences vary. No physical, physiological, cellular, medical, or sleep outcome is promised.",
  who_intro="The system may appeal to adults who:",
  who=["Want a consistent relaxation or quiet-time routine","Enjoy reading, meditation, reflection, or restorative downtime",
       "Prefer passive wellness products without complicated controls","Have a clean, dry, stable area for four units",
       "Understand that the system is intended only for general wellness"],
  who_note="The system is not intended to diagnose, treat, cure, mitigate, or prevent any disease or medical condition.",
  routine=[("Choose the Space","Select a clean, dry, comfortable area used for ordinary rest, reading, meditation, or relaxation."),
           ("Arrange the System","Place the four units only as shown in the final approved diagram and maintain the stated distance from the bed or wellness area."),
           ("Use Consistently","Include the system during quiet-time or evening wind-down activities according to the supplied instructions."),
           ("Support Healthy Habits","Pair the routine with consistent sleep hours, appropriate activity, balanced nutrition, and responsible self-care.")],
  routine_note="The system supplements — and does not replace — healthy lifestyle practices or professional medical care.",
  directions=["Remove all four units from the packaging and inspect them for damage.",
              "Place each unit upright on a stable, dry surface.",
              "Arrange the units only according to the approved product diagram.",
              "[Placement pending approval — source draft proposes one unit near each corner of a bed, approximately one foot from the bed frame, for overnight use.]",
              "Keep units dry and away from excessive heat, open flame, impact, children, and pets.",
              "Do not open, modify, drill, heat, burn, puncture, or disassemble any unit.",
              "Store the system in a clean, dry location when not in use.",
              "The final product label and Instructions for Use control."],
  specs=[("Product name","Tesla BioHealing® QiRenew System"),
         ("Product category","Four-unit Tesla BioHealing® LIPG system for adult general wellness"),
         ("Model / SKU","BPP-040 / BPP-040"),
         ("Units included","Four Biophotonizer Plus units"),
         ("Approved arrangement","[Confirm final diagram — source proposes four bed corners]"),
         ("Recommended distance","[Confirm — source proposes one foot from bed frame]"),
         ("Recommended duration","[Confirm — source proposes overnight]"),
         ("Dimensions per unit","[Insert verified dimensions]"),
         ("Weight per unit / packaged weight","[Insert verified values]"),
         ("External housing / internal composition","[Insert approved material descriptions]"),
         ("External power / battery","None required"),
         ("Country of manufacture","USA — confirm final country-of-origin statement"),
         ("Expected service period","36 months — confirm")],
  safety=["For adult general-wellness use only. Keep out of reach of children; this is not a toy.",
          "Do not ingest, open, crush, puncture, drill, heat, burn, or modify any unit.",
          "Do not use a cracked, leaking, damaged, or unlabeled unit.",
          "Keep all units dry and away from open flame and extreme temperatures.",
          "Use stable surfaces and prevent falling or tripping hazards.",
          "Do not place units inside a bed, beneath a mattress, or where they interfere with safe movement unless expressly validated and approved.",
          "Do not use the system as a substitute for medical evaluation or treatment or delay seeking care because of product information.",
          "Consult a qualified healthcare professional regarding medical conditions, pregnancy, or implanted medical devices before introducing a new wellness product."],
  included=["One set of four Tesla BioHealing® Biophotonizer Plus units","Approved arrangement and use guide",
            "Safety and product-care information","Product registration and warranty information","Protective packaging"],
  included_note="Photographs and package descriptions must match the exact products shipped to customers.",
  faq=[("Does the QiRenew System regenerate cells?","No. The system is offered solely for general wellness and is not intended to renew cells or alter cellular structure or function."),
       ("Is it intended to treat a medical condition?","No. It is not intended to diagnose, treat, cure, mitigate, or prevent disease."),
       ("What is an LIPG?","LIPG is Tesla BioHealing's product-category term for a Low-Intensity Photon-Generator. Performance statements require validated product-specific testing."),
       ("Does it require electricity or batteries?","No."),
       ("Where should the units be placed?","Follow only the approved arrangement and distance instructions supplied with the system, not testimonials, social media, or older marketing materials."),
       ("How often may I use it?","Follow the final approved instructions. The system is intended to complement ordinary relaxation and healthy-lifestyle routines."),
       ("Can several people use the same space?","Adults may share a general-wellness space when all safety instructions are followed. No shared or increased physiological effect is promised."),
       ("Will everyone have the same experience?","No. Wellness experiences are subjective and vary."),
       ("Can it replace medication or professional care?","No. Never discontinue or change medication, treatment, or professional care because of this product.")],
  shipping=["Orders are processed according to the shipping options displayed at checkout","Delivery estimates are not guarantees",
            "Tracking information will be provided when available",
            "[Confirm the four-unit package weight, dimensions, destinations, and any special handling before publication]"],
  returns=["Eligible returns must be requested within [insert verified return period] days after delivery.",
           "Products must meet the conditions in the complete Return and Refund Policy.",
           "[Confirm whether all four units must be returned together and identify any restocking or freight charges.]"],
  warranty=["Warranty period: [Insert verified warranty term]",
            "The limited warranty should cover qualifying defects in materials or workmanship and exclude misuse, unauthorized modification, accidental damage, normal cosmetic wear, and failure to follow instructions."],
  disclaimer=["Tesla BioHealing® QiRenew System is intended solely for adult general-wellness use as part of a healthy lifestyle. It is not intended to diagnose, treat, cure, mitigate, or prevent disease or to replace medical advice, diagnosis, or treatment.",
              "No representation is made that the system renews or regenerates cells, produces stem cells, repairs tissue, changes circulation, increases ATP, relieves pain, or affects the structure or function of the body.",
              "Individual experiences vary, and no particular result is guaranteed. Consult a qualified healthcare professional about symptoms, health conditions, medication, pregnancy, or implanted medical devices."],
  cta="Add QiRenew System to Cart", cta_disabled=True,
  ack="General-wellness product. Purchasing opens once configuration, photographs, price, SKU, specifications, instructions, labeling, returns, and warranty receive documented approval.",
  seo_title="QiRenew System | Tesla BioHealing®",
  seo_desc="Discover the Tesla BioHealing® QiRenew System, a passive four-unit system designed to complement relaxation, quiet-time, and everyday wellness routines at home.",
),
# ------------------------------------------------------------------ ENLOVA WATER
dict(
  slug="enlova-water",
  program="ENLOVA™",
  category="ENLOVA™ Hydration",
  name="ENLOVA™ Water",
  short="ENLOVA™ Water",
  subtitle="Bottled Water for Mindful Everyday Hydration",
  price="$192.00", price_alt="One case · 24 bottles × 16.9 fl oz / 500 mL",
  card_price="$192.00 / case",
  meta=[("SKU","BPW500"),("Package","24 × 500 mL")],
  qty_label="One 24-bottle case",
  purpose="ENLOVA™ Water is bottled water intended for ordinary consumption as part of a safe, balanced, and mindful hydration routine.",
  image="enlova-water.png", image_alt="ENLOVA water bottles",
  photo_guidance="Use current photographs of the exact bottle, cap, tamper-evident seal, approved label, lot and best-by code, case packaging, and the 24-bottle configuration. State clearly that one order includes one case of 24 bottles.",
  thumbs=["500 mL bottle","Cap & seal","Label","Lot / best-by code","24-bottle case"],
  facts=[("Case","24 sealed bottles"),("Per bottle","16.9 fl oz / 500 mL"),("Total","≈ 405.6 fl oz / 12 L"),("Prep","None — ready to drink")],
  review_note="Confirm the legal statement of identity, exact source and location, bottler/distributor, processing, ingredients, label, quality testing, bottle materials, best-by coding, shipping, and returns before publication. Do not publish 'spring water,' Appalachian foothills, Knox Aquifer, or source-location claims until documentation supports them.",
  conflicts=["Price: product-detail table lists $192.00; the add-to-cart table says [Insert approved case price]. Page shows $192.00 until confirmed.",
             "Photo: the supplied image shows large bottles labeled “Premium Water”; the product is a 500 mL bottle and photos must match the exact bottle and label shipped.",
             "Statement of identity: [Confirm Spring Water or Bottled Water after source verification].",
             "Availability: [Confirm current inventory status]."],
  features_intro="ENLOVA™ Water offers a simple way to keep drinking water available for ordinary daily use.",
  features=["Convenient bottled water for everyday drinking","Twenty-four individually sealed 16.9 fl oz / 500 mL bottles per case",
            "Suitable for home, office, meals, travel where permitted, or rotated emergency supplies",
            "Clearly labeled source, bottler, lot, best-by, and quality information after approval",
            "Requires no electricity, preparation, charging, waiting period, or special equipment",
            "Complements a mindful hydration routine within a balanced lifestyle"],
  features_note="No claim is made that ENLOVA™ Water hydrates better than other compliant bottled water or improves circulation, metabolism, cognition, sleep, recovery, energy, or physical performance.",
  who_intro="ENLOVA™ Water may suit people who:",
  who=["Want convenient bottled water for ordinary consumption","Keep sealed drinking water available at home or work",
       "Prefer individually sealed portions","Want a 24-bottle case for a household or workplace","Include mindful hydration in a balanced lifestyle"],
  who_note="Fluid needs vary. People with medically directed fluid, sodium, mineral, kidney, cardiac, or other dietary restrictions should follow professional guidance.",
  routine=[("Keep It Available","Store unopened bottles in a clean, cool, dry area away from sunlight, heat, chemicals, fuels, strong odors, pests, and contamination."),
           ("Inspect Before Opening","Confirm that the bottle, cap, and tamper-evident seal are intact."),
           ("Drink Normally","Consume according to personal preference, activity, environment, diet, and professional advice. No universal number of bottles is recommended."),
           ("After Opening","Refrigerate and consume promptly. Do not share or repeatedly refill a single-use bottle.")],
  routine_note="No charging, activation, waiting period, geometric arrangement, or special placement is required.",
  directions=["Inspect the bottle and tamper-evident seal before opening.",
              "Do not consume if the seal is broken, the bottle leaks, or the water has an unusual appearance, odor, or taste.",
              "Open with clean hands and drink according to ordinary hydration needs.",
              "Refrigerate after opening and consume promptly. Do not share an opened bottle.",
              "Do not refill or repeatedly reuse a bottle designed for single use.",
              "Store unopened bottles in a clean, cool, dry area away from sunlight, chemicals, fuels, strong odors, pests, and excessive heat.",
              "Do not microwave, boil, or heat water in the original plastic bottle. Transfer it to a suitable heat-safe container if warming is desired.",
              "Follow the printed lot and best-by information and recycle the empty bottle and cap where accepted."],
  specs=[("Product name","ENLOVA™ Water"),
         ("Statement of identity","[Confirm under applicable bottled-water requirements]"),
         ("SKU","BPW500"),
         ("Purchase quantity","One case containing 24 bottles"),
         ("Bottle volume","16.9 fl oz / 500 mL"),
         ("Total case volume","Approximately 405.6 fl oz / 12 liters"),
         ("Ingredients","[Natural spring water — publish only after identity and source verification]"),
         ("Water source","[Insert verified source name and location]"),
         ("Bottler / distributor","[Insert approved name, address, and statement]"),
         ("Treatment methods","[Insert verified filtration, ozone, UV, or other processes]"),
         ("Added ingredients","[State None or identify each ingredient]"),
         ("Nutrition Facts","[Insert approved panel or document applicable exemption]"),
         ("Mineral / quality analysis","[Insert approved report or link]"),
         ("Sodium / fluoride / TDS / pH","[Publish only verified values with approved methods and wording]"),
         ("Microbiological / chemical testing","[Confirm source-water and finished-product compliance]"),
         ("Bottle / cap / liner materials","[Insert verified food-contact materials and regulatory basis]"),
         ("Bottle reuse","Single-use unless validated and labeled otherwise"),
         ("Lot / best-by coding","[Required — insert approved period, location, and format]"),
         ("Storage","Cool, clean, dry storage away from sunlight, heat, chemicals, and odors"),
         ("Country of manufacture","United States — confirm")],
  safety=["Consume only from bottles with an intact tamper-evident seal.",
          "Do not consume from a leaking, swollen, punctured, opened, damaged, or abnormal bottle.",
          "Store away from sunlight, excessive heat, chemicals, gasoline, pesticides, cleaning products, and strong odors.",
          "Do not leave cases in a hot vehicle for extended periods.",
          "Do not microwave, boil, or heat water in the original plastic bottle.",
          "Refrigerate after opening, consume promptly, and do not repeatedly refill a single-use bottle.",
          "Keep caps and plastic packaging away from infants and young children.",
          "Do not use for wound care, contact-lens care, nasal rinsing, injection, inhalation equipment, or another medical use.",
          "Do not use as a substitute for prescribed oral rehydration products or medical treatment.",
          "Retain the bottle, lot code, case, and purchase information when reporting contamination, illness, damage, or a quality concern."],
  included=["One case of ENLOVA™ Water","Twenty-four sealed bottles","16.9 fl oz / 500 mL per bottle",
            "Required product and food labeling","Lot and best-by coding","Protective case packaging"],
  included_note="Reusable bottles, water-treatment products, LIPG products, subscriptions, and other products are not included unless expressly stated.",
  faq=[("How many bottles are included?","One case contains 24 individually sealed bottles."),
       ("How much water is in each bottle?","16.9 fluid ounces / 500 milliliters."),
       ("Is it spring water?","[Use the term spring water only after the source and collection method are verified to meet the applicable standard of identity.]"),
       ("Where does it come from?","[The approved label and product page must state the verified source name and location. Do not publish unverified aquifer or regional descriptions.]"),
       ("Is it energized or biophoton-infused?","No energized, charged, infused, restructured, or physically altered-water claim is made."),
       ("Does it hydrate better than ordinary bottled water?","No comparative or enhanced-hydration claim is made."),
       ("How much should I drink?","Fluid needs differ. Drink according to personal needs and professional advice; no universal number of bottles is recommended."),
       ("How should it be stored?","Keep unopened bottles in a cool, clean, dry area away from sunlight, heat, chemicals, pests, and strong odors."),
       ("Can I heat it?","Do not heat the original plastic bottle. Transfer the water to a suitable heat-safe container."),
       ("How is the water tested?","[The source water and finished product must be tested as required. Offer a quality report only after approval.]")],
  shipping=["Bottled water is a heavy consumable product; [display case weight and dimensions before purchase]",
            "[Confirm eligible destinations, shipping charge, processing time, delivery estimate, carrier, tracking, and temperature controls]",
            "[Provide a clear procedure for damaged, leaking, missing, or delayed shipments]",
            "Inspect the case promptly and retain damaged bottles, lot codes, the case, and shipping label"],
  returns=["Return status: [Insert approved final-sale or limited-return policy]",
           "Damaged shipment remedy: [Insert approved replacement or refund process]",
           "Quality complaint procedure and reporting period: [Insert approved details]",
           "Unopened and opened case eligibility: [Insert approved policy]",
           "A final-sale policy does not eliminate legally required remedies for contaminated, adulterated, misbranded, damaged, or improperly shipped products."],
  warranty=["A conventional device warranty does not apply to bottled water.",
            "[The product-quality policy should address broken seals, leaks, damage, foreign material, unusual appearance/odor/taste, incorrect quantity, lot traceability, complaint investigation, refunds or replacements, and recall communication.]"],
  warranty_title="Product-Quality Policy",
  disclaimer=["ENLOVA™ Water is bottled water intended for ordinary consumption as part of a safe and mindful hydration routine.",
              "No claim is made that the water is energized, charged, infused, restructured, amplified, enhanced with photons, or otherwise changed in its chemical, molecular, nutritional, vibrational, or biological properties.",
              "ENLOVA™ Water is not intended to diagnose, treat, cure, mitigate, or prevent dehydration requiring medical care or any disease or medical condition. It is not claimed to hydrate better than other compliant drinking water or improve energy, cognition, circulation, sleep, metabolism, fitness, or recovery.",
              "Bottled water is regulated as food; an individual brand is not FDA approved."],
  cta="Add One 24-Bottle Case to Cart", cta_disabled=False,
  ack="This listing includes one case containing 24 bottles. No medical, enhanced-hydration, energy-transfer, or disease-related benefit is promised. If a subscription is offered, all pricing, shipping, renewal, and cancellation terms are disclosed before enrollment.",
  seo_title="ENLOVA™ Water | 24-Bottle Case",
  seo_desc="ENLOVA™ Water offers 24 individually sealed 16.9 fl oz bottles for ordinary drinking and a mindful everyday hydration routine.",
  extra_internal="Post-bottling LIPG exposure: document internally; make no water-alteration claim (kept off the public spec table).",
),
]

exec(open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "new_products.py"), encoding="utf-8").read())
ORDER = ["biophotonizer-a", "biophotonizer-alpha", "biophotonizer-c", "pillow", "neck-pillow", "eyemask",
         "cornerstone", "qirenew-system", "enlova-water", "enlova-water-bottle"]
_by_slug = {p["slug"]: p for p in PRODUCTS + NEW_PRODUCTS}
PRODUCTS = [_by_slug[s] for s in ORDER]
_cns = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "compliance.py"), encoding="utf-8").read(), _cns)
PRODUCTS = _cns["apply"](PRODUCTS)
REQUIRED_DISCLAIMER = _cns["REQUIRED_DISCLAIMER"]

HEADER = """<div class="promo frame-note" data-label="00 · Announcement Bar"><b>Free Shipping</b> on Orders $150+</div>
<header class="site frame-note" data-label="01 · Header / Navigation">
  <nav class="nav-left">
    <a href="../frontpage.html#trending">Shop</a>
    <a>Our Technology</a>
    <a>Our Wellness Approach</a>
    <a>Support</a>
  </nav>
  <a class="logo serif" href="../frontpage.html">Healthy Sleep Space</a>
  <div class="nav-right"><span class="ic">A</span><span class="ic">Q</span><span class="ic">0</span></div>
</header>"""

FOOTER = """<footer class="frame-note on-deep" data-label="Footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h5>Our Commitment to You</h5>
        <p>We believe in clear product information, responsible wellness positioning, and respectful customer support — so you understand what a product is and how it's intended to be used before you buy.</p>
      </div>
      <div><h5>Shop</h5><ul>
{SHOP_LINKS}
      </ul></div>
      <div><h5>Help</h5><ul><li>Contact Support</li><li>Shipping &amp; Delivery</li><li>Returns &amp; Refunds</li><li>Product Warranty</li><li>Track My Order</li></ul></div>
      <div><h5>Our Company</h5><ul><li>Our Technology</li><li>Our Wellness Approach</li><li>Wellness Library</li><li>Careers</li></ul></div>
    </div>
    <div class="legal">
      <p><strong>General Wellness Disclaimer:</strong> {REQUIRED}</p>
      <div class="bottom-row">
        <span>&copy; 2026 Healthy Sleep Space. All rights reserved.</span>
        <span>United States (USD $) &nbsp;·&nbsp; Privacy Policy &nbsp;·&nbsp; Terms of Service</span>
      </div>
    </div>
  </div>
</footer>"""

def ul(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"

def spec_row(k, v):
    pending = "[" in v or re.search(r"\bconfirm\b", v, re.I) or v.lower().startswith("publish only")
    cls = ' class="unconfirmed"' if pending and "[" not in v else ""
    return f"<tr{cls}><th>{esc(k)}</th><td>{esc(v)}</td></tr>"

def img_src(name):
    return f"../assets/products/{name}"

def render(p):
    others = [o for o in PRODUCTS if o["slug"] != p["slug"]]
    shop_links = "\n".join(f'        <li><a href="{o["slug"]}.html">{esc(o["short"])}</a></li>' for o in PRODUCTS)
    gallery_main = (f'<div class="main"><img src="{img_src(p["image"])}" alt="{html.escape(p["image_alt"])}"></div>'
                    if p.get("image") else
                    '<div class="main ph">[ Insert current approved product photograph ]</div>')
    thumbs = "".join(f'<div class="ph">{esc(t)}</div>' for t in p["thumbs"])
    meta = " &nbsp;·&nbsp; ".join(f"{esc(k)} <b>{esc(v)}</b>" for k, v in p["meta"])
    intro_note = (f'<p class="fine" style="margin:-8px 0 20px"><b>What Recovery Sleep™ means here:</b> {esc(p["intro_note"])}</p>'
                  if p.get("intro_note") else "")
    opt_html = ""
    if p.get("options"):
        label, opts, hint = p["options"]
        radios = "".join(f'<label><input type="radio" name="opt" value="{o}"><span>{o}</span></label>' for o in opts)
        opt_html = f'''<div class="option-group">
          <div class="lbl">{label} <em>· required</em></div>
          <div class="options">{radios}</div>
          <p class="fine" style="font-style:normal">{esc(hint)}</p>
        </div>'''
    disabled = " disabled" if p["cta_disabled"] else ""
    facts = "".join(f"<div><b>{esc(k)}</b>{esc(v)}</div>" for k, v in p["facts"])
    conflicts = "".join(f"<li>{esc(c)}</li>" for c in p["conflicts"])
    if p.get("extra_internal"):
        conflicts += f"<li>{esc(p['extra_internal'])}</li>"
    steps = "".join(
        f'<div class="step"><div class="n">Step {i+1:02d}</div><h3 class="serif">{esc(r[0])}</h3><p>{esc(r[1])}</p></div>'
        if isinstance(r, tuple) else
        f'<div class="step"><div class="n">Step {i+1:02d}</div><p>{esc(r)}</p></div>'
        for i, r in enumerate(p["routine"]))
    directions = "".join(f"<li>{esc(d)}</li>" for d in p["directions"])
    specs = "".join(spec_row(k, v) for k, v in p["specs"])
    faq = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in p["faq"])
    disclaimer = "".join(f"<p>{esc(x)}</p>" for x in p["disclaimer"])
    related = ""
    for o in others:
        im = (f'<div class="img"><img src="{img_src(o["image"])}" alt="{html.escape(o["image_alt"])}"></div>'
              if o.get("image") else f'<div class="img ph">[ {esc(o["short"])} photo ]</div>')
        related += f'''<a class="rcard" href="{o["slug"]}.html">{im}<div class="cat">{esc(o["category"])}</div><h4 class="serif">{esc(o["name"])}</h4><div class="p">{esc(o["card_price"])}</div></a>'''
    cta_note = ('<p class="fine" style="font-style:normal;color:var(--flag)">Button disabled in wireframe: ' +
                ("a firmness must be selected first." if p.get("options") else "awaiting documented approval (see review note).") + "</p>"
                ) if p["cta_disabled"] else ""
    script = ""
    if p.get("options"):
        script = """<script>
  // Require an explicit firmness choice before enabling add-to-cart.
  document.querySelectorAll('input[name="opt"]').forEach(function(r){
    r.addEventListener('change', function(){
      var b = document.getElementById('add-to-cart');
      b.disabled = false;
      b.textContent = 'Add ' + r.value + ' Pillow to Cart';
      document.getElementById('cta-note').style.display = 'none';
    });
  });
</script>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{esc(p["seo_title"])}</title>
<meta name="description" content="{html.escape(p["seo_desc"])}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="../assets/product.css">
</head>
<body>

{HEADER}

<!-- PDP 01 :: BUY BOX -->
<section class="buy frame-note" data-label="PDP 01 · Buy Box">
  <div class="wrap">
    <div class="crumbs"><a href="../frontpage.html">Home</a><span>/</span><a href="../frontpage.html#trending">Shop</a><span>/</span>{esc(p["category"])}<span>/</span>{esc(p["short"])}</div>
    <div class="buy-grid">
      <div class="gallery">
        {gallery_main}
        <div class="thumbs">{thumbs}</div>
        <div class="devnote"><b>PHOTO GUIDANCE:</b> {esc(p["photo_guidance"])}</div>
      </div>
      <div class="buy-copy">
        <div class="program">{esc(p["program"])}</div>
        <h1 class="serif">{esc(p["name"])}</h1>
        <div class="subtitle serif">{esc(p["subtitle"])}</div>
        <div class="price-row"><span class="price serif">{esc(p["price"])}</span><span class="price-alt">{esc(p["price_alt"])}</span></div>
        <div class="meta-row">{meta}</div>
        <p class="purpose">{esc(p["purpose"])}</p>
        {intro_note}
        {opt_html}
        <div class="qty-row">
          <div class="qty"><span>−</span><span>1</span><span>+</span></div>
          <button class="btn solid block" id="add-to-cart"{disabled}>{esc(p["cta"])}</button>
        </div>
        <div id="cta-note">{cta_note}</div>
        <p class="ack">Includes: {esc(p["qty_label"])}. {esc(p["ack"])}</p>
        <div class="buy-facts">{facts}</div>
        <div class="devnote flag"><b>PUBLICATION REVIEW NOTE (internal — remove before launch):</b> {esc(p["review_note"])}<ul>{conflicts}</ul></div>
      </div>
    </div>
  </div>
</section>

<nav class="tabnav">
  <div class="wrap">
    <a href="#overview">Overview</a><a href="#routine">Daily Routine</a><a href="#directions">Directions</a>
    <a href="#specs">Specifications</a><a href="#safety">Safety &amp; Included</a><a href="#faq">FAQ</a>
    <a href="#policies">Shipping &amp; Returns</a>
  </div>
</nav>

<!-- PDP 02 :: FEATURES + WHO -->
<section class="section frame-note" id="overview" data-label="PDP 02 · Features / Who It's For">
  <div class="wrap two-col">
    <div class="col">
      <div class="eyebrow">General-Wellness Features</div>
      <h3 class="serif" style="margin-top:8px">{esc(p["features_intro"])}</h3>
      {ul(p["features"])}
      <p class="fine">{esc(p["features_note"])}</p>
    </div>
    <div class="col">
      <div class="eyebrow">Who May Enjoy It</div>
      <h3 class="serif" style="margin-top:8px">{esc(p["who_intro"])}</h3>
      {ul(p["who"])}
      <p class="fine">{esc(p["who_note"])}</p>
    </div>
  </div>
</section>

<!-- PDP 03 :: DAILY ROUTINE -->
<section class="routine frame-note on-deep" id="routine" data-label="PDP 03 · Daily Routine">
  <div class="wrap">
    <div class="eyebrow" style="color:var(--gold-light)">How to Incorporate It</div>
    <h2 class="big serif" style="margin-top:8px">Your Daily Routine</h2>
    <p class="lead">{esc(p["routine_note"])}</p>
    <div class="steps">{steps}</div>
  </div>
</section>

<!-- PDP 04 :: DIRECTIONS -->
<section class="section alt frame-note" id="directions" data-label="PDP 04 · Directions for Use">
  <div class="wrap">
    <div class="eyebrow">Directions for Use</div>
    <h2 class="big serif" style="margin-top:8px">Setting Up &amp; Using {esc(p["short"])}</h2>
    <p class="lead">The final product label and Instructions for Use control if they differ from this page.</p>
    <ol class="directions">{directions}</ol>
  </div>
</section>

<!-- PDP 05 :: SPECIFICATIONS -->
<section class="section frame-note" id="specs" data-label="PDP 05 · Specifications &amp; Materials">
  <div class="wrap">
    <div class="eyebrow">Product Specifications &amp; Materials</div>
    <h2 class="big serif" style="margin:8px 0 24px">Specifications</h2>
    <table class="specs">{specs}</table>
  </div>
</section>

<!-- PDP 06 :: SAFETY + INCLUDED -->
<section class="section alt frame-note" id="safety" data-label="PDP 06 · Safety / What's Included">
  <div class="wrap two-col">
    <div class="col">
      <div class="eyebrow">Safety Information &amp; Limitations</div>
      <h3 class="serif" style="margin-top:8px">Use Safely</h3>
      {ul(p["safety"], "ticks warn")}
    </div>
    <div class="col">
      <div class="eyebrow">What Is Included</div>
      <h3 class="serif" style="margin-top:8px">In the Box</h3>
      {ul(p["included"])}
      <p class="fine">{esc(p["included_note"])}</p>
    </div>
  </div>
</section>

<!-- PDP 07 :: FAQ -->
<section class="section frame-note" id="faq" data-label="PDP 07 · FAQ">
  <div class="wrap">
    <div class="eyebrow">Frequently Asked Questions</div>
    <h2 class="big serif" style="margin:8px 0 24px">Questions, Answered</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<!-- PDP 08 :: SHIPPING / RETURNS / WARRANTY -->
<section class="section alt frame-note" id="policies" data-label="PDP 08 · Shipping, Returns &amp; Warranty">
  <div class="wrap">
    <div class="eyebrow">Shipping, Returns &amp; Warranty</div>
    <h2 class="big serif" style="margin:8px 0 24px">Ordering With Confidence</h2>
    <div class="policy-grid">
      <div class="policy"><h3 class="serif">Shipping</h3>{ul(p["shipping"], "")}</div>
      <div class="policy"><h3 class="serif">Returns</h3>{ul(p["returns"], "")}</div>
      <div class="policy"><h3 class="serif">{esc(p.get("warranty_title", "Warranty"))}</h3>{ul(p["warranty"], "")}</div>
    </div>
  </div>
</section>

<!-- PDP 09 :: DISCLAIMER -->
<section class="section frame-note" data-label="PDP 09 · Wellness Disclaimer">
  <div class="wrap">
    <div class="disclaimer">
      <h3>General Wellness Disclaimer</h3>
      {disclaimer}
    </div>
  </div>
</section>

<!-- PDP 10 :: RELATED -->
<section class="section alt frame-note" data-label="PDP 10 · Explore the Collection">
  <div class="wrap">
    <h2 class="big serif" style="margin-bottom:28px;text-align:center">Explore the Collection</h2>
    <div class="related">{related}</div>
  </div>
</section>

<!-- SEO annotation -->
<section class="section frame-note" data-label="SEO (internal)">
  <div class="wrap seo">
    <div class="devnote"><b>SEO TITLE:</b><br>{esc(p["seo_title"])}</div>
    <div class="devnote"><b>META DESCRIPTION:</b><br>{esc(p["seo_desc"])}</div>
  </div>
</section>

{FOOTER.replace("{SHOP_LINKS}", shop_links).replace("{REQUIRED}", esc(REQUIRED_DISCLAIMER))}
{script}
</body>
</html>
"""

os.makedirs(OUT, exist_ok=True)
for p in PRODUCTS:
    with open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(render(p))
    print("wrote", p["slug"])
