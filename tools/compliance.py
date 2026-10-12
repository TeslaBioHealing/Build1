"""Apply the General Wellness Marketing Guide (v2.0, Oct 2026) to the product copy.

The product documents are kept as written; this layer rewrites or removes copy the guide
puts on the Red list (disease, symptom, treatment, medical-framing and FDA words, even when
phrased as a denial) and adds the guide's approved "Say this" lines.
"""

# Guide p.2 — "The required disclaimer. COPY EXACTLY."
REQUIRED_DISCLAIMER = ("Tesla BioHealing products are intended for general wellness purposes only, including "
                       "supporting relaxation, comfort, and everyday well-being. They are not intended to diagnose, "
                       "treat, cure, or prevent any disease or medical condition, and are not a substitute for "
                       "professional medical advice, diagnosis, or treatment.")

NO_RESULT = "These statements describe a general-wellness role only. Individual experiences vary, and no particular result is promised."
RS_MEANS = ("On HealthySleepSpace.com, Recovery Sleep™ is the name of our general-wellness routine: a calm environment, "
            "comfort, consistent bedtime habits, and ordinary rest. Individual experiences vary, and no particular result is promised.")
POSITIONING = "This product is offered as part of a lifestyle and environmental wellness routine. Individual experiences vary, and no particular result is promised."
COMFORT_STOP = "Stop using it if it feels uncomfortable, irritates the skin, or ever makes breathing feel restricted."

# Exact sentence -> replacement (None removes it). Applies to every list and text field.
REWRITE = {
    # Biophotonizer A / Alpha
    "These statements describe a general-wellness role only. No medical, clinical, sleep, or physiological outcome is promised.": NO_RESULT,
    "Recovery Sleep™ and this product are not intended for a symptom, diagnosis, disease, injury, pain, sleep disorder, or other medical condition.": POSITIONING,
    "Do not position the product to target a symptom, injury, painful area, or medical condition.": None,
    "Do not use the product to target a symptom, injury, painful area, or medical condition.": None,
    "The product does not provide medical measurements, alarms, diagnoses, or treatment guidance.": None,
    "Do not use it as a substitute for sleep, nutrition, physical activity, professional healthcare, or emergency assistance.":
        "Use it alongside, not instead of, healthy habits such as adequate rest, balanced nutrition, and physical activity.",
    "The final product label and Instructions for Use control if they differ from this website draft.":
        "The final product label and Instructions for Use control if they differ from this page.",
    # Shared HealthySleepSpace.com documents
    "On HealthySleepSpace.com, Recovery Sleep™ describes a nonmedical wellness routine focused on a calm environment, comfort, consistent bedtime habits, and ordinary rest. It does not mean recovery from an illness, injury, or sleep disorder, and no particular sleep outcome is promised or guaranteed.": RS_MEANS,
    "This product is offered as part of a lifestyle and environmental wellness routine. It is not promoted for disease treatment, rehabilitation, or a guaranteed sleep outcome.": POSITIONING,
    # Biophotonizer C
    "No claim is made that the product causes sleep, changes behavior, improves school performance, modifies development, or produces a medical or biological outcome.": NO_RESULT,
    "Understand that the product is a general-wellness accessory, not a toy or medical treatment":
        "Understand that the product is a general-wellness accessory, not a toy",
    "Do not use for monitoring, diagnosis, behavioral assessment, treatment decisions, or emergency assistance": None,
    "Do not delay pediatric evaluation or discontinue professional care because of this product": None,
    "Technical measurements and material descriptions identify the product; they do not, by themselves, establish a biological, physiological, developmental, behavioral, or medical outcome.":
        "Technical measurements and material descriptions identify the product only.",
    "Adult purchase and supervision required. General wellness only; no medical, behavioral, developmental, or guaranteed sleep outcome is offered.":
        "Adult purchase and supervision required. Designed for general wellness; individual experiences vary, and no particular result is promised.",
    "Choose a dry, level, stable surface near the child's ordinary rest area.":
        "A caregiver should place the device on a dry, level, stable surface near the child's sleeping area.",
    # Pillow
    "No faster sleep onset, longer sleep, improved sleep stages, greater energy, improved cognition, better circulation, or accelerated recovery is promised.": NO_RESULT,
    "Fit and comfort depend on anatomy, sleep position, mattress firmness, and personal preference. Anyone requiring medical positioning, airway management, postsurgical support, or treatment should consult a qualified professional.":
        "Fit and comfort depend on sleep position, mattress firmness, and personal preference.",
    "Stop use or reposition the pillow if it causes pain, numbness, tingling, breathing difficulty, skin irritation, headache, dizziness, or unusual discomfort.":
        "Reposition the pillow or stop using it if it feels uncomfortable, irritates the skin, or ever makes breathing feel restricted.",
    "Stop use if it causes pain, numbness, tingling, breathing difficulty, skin irritation, headache, dizziness, or unusual discomfort.": COMFORT_STOP,
    "Do not use as a cervical brace, immobilizer, medical-positioning product, airway-management product, or rehabilitation device.":
        "Not designed to hold the head or neck in a fixed position.",
    "CPAP and other medical-equipment compatibility has not been established.":
        "Do not let the pillow interfere with any equipment you use while sleeping.",
    # Neck Pillow
    "No claim is made that the pillow relieves pain, treats stiffness, corrects posture, realigns the spine, improves circulation, restores mobility, accelerates recovery, or produces a physiological outcome.": NO_RESULT,
    "Keep the front of the throat open and ensure breathing, swallowing, hearing, vision, and movement remain unrestricted.":
        "Keep the front of the throat open so breathing, swallowing, hearing, sight, and movement stay unrestricted.",
    "Remove immediately if it causes pain, numbness, tingling, dizziness, headache, breathing or swallowing difficulty, skin irritation, or unusual discomfort.":
        "Remove it right away if it feels uncomfortable, irritates the skin, or makes breathing or swallowing feel restricted.",
    "Do not use as a cervical collar, brace, traction device, orthosis, immobilizer, emergency support, or rehabilitation product":
        "Not designed to hold the head or neck in a fixed position",
    "Do not use if it interferes with breathing, swallowing, circulation, vision, hearing, movement, or medical equipment":
        "Do not use it if it interferes with breathing, swallowing, sight, hearing, movement, or any equipment you use",
    "Consult a qualified healthcare professional for persistent symptoms, injury, or medical concerns": None,
    "Technical measurements and material descriptions identify the product; they do not, by themselves, establish a physiological or medical outcome.":
        "Technical measurements and material descriptions identify the product only.",
    # Eyemask
    "No claim is made that the eyemask guarantees deeper or longer sleep, changes sleep stages, relieves eye strain, improves vision, changes skin appearance, reduces wrinkles or puffiness, or produces a biological or medical effect.": NO_RESULT,
    "Remove it whenever desired or if it causes pressure, warmth, irritation, blurred vision, headache, or discomfort.":
        "Remove it whenever you like, or if it feels uncomfortable, presses on the eyes, or irritates the skin.",
    "Adjust the strap so breathing, hearing, circulation, and independent removal remain unrestricted.":
        "Adjust the strap so it is snug but not tight, and so breathing, hearing, and removing the mask stay easy.",
    "The mask is not protection from sunlight, lasers, ultraviolet radiation, particles, chemicals, or workplace hazards":
        "Not designed as protective eyewear",
    "Do not place over injured, inflamed, infected, or recently treated skin": "Do not use over irritated or broken skin",
    "Stop use for eye pressure, blurred vision, pain, redness, itching, numbness, headache, breathing difficulty, skin irritation, or unusual discomfort":
        "Stop using it if it feels uncomfortable, presses on the eyes, or irritates the skin",
    "Technical measurements and material descriptions identify the product; they do not, by themselves, establish an ophthalmic, cosmetic, physiological, or medical outcome.":
        "Technical measurements and material descriptions identify the product only.",
    "Normal wear, discoloration, improper washing or drying, heat, freezing, cosmetics, misuse, and unauthorized alteration are excluded.":
        "Normal wear, discoloration, improper washing or drying, heat, freezing, makeup or creams, misuse, and unauthorized alteration are excluded.",
    # Cornerstone (guide p.9 "Say this instead": Passive)
    "Cornerstone does not provide thermal therapy, acoustic therapy, electrical stimulation, medical monitoring, treatment, or a guaranteed sleep outcome.":
        "Passive: no lasers, no heat, no cords, nothing to set up. Individual experiences vary, and no particular result is promised.",
    "A shared room does not establish or guarantee equal exposure, benefit, or outcome. Cornerstone is not intended for diagnosis, treatment, rehabilitation, sleep-disorder management, or disease prevention.":
        "Individual experiences vary, including when a space is shared, and no particular result is promised.",
    "Do not rely on Cornerstone for medical measurements, alarms, diagnosis, treatment decisions, or emergency assistance.": None,
    # QiRenew
    "Individual experiences vary. No physical, physiological, cellular, medical, or sleep outcome is promised.": NO_RESULT,
    "Enjoy reading, meditation, reflection, or restorative downtime": "Enjoy reading, meditation, reflection, or restful downtime",
    "The system is not intended to diagnose, treat, cure, mitigate, or prevent any disease or medical condition.": POSITIONING,
    "Do not use the system as a substitute for medical evaluation or treatment or delay seeking care because of product information.": None,
    "Consult a qualified healthcare professional regarding medical conditions, pregnancy, or implanted medical devices before introducing a new wellness product.":
        "If you are pregnant or have an implanted device, check with your healthcare provider before introducing a new wellness product.",
    "The limited warranty should cover qualifying defects in materials or workmanship and exclude misuse, unauthorized modification, accidental damage, normal cosmetic wear, and failure to follow instructions.":
        "The limited warranty should cover qualifying defects in materials or workmanship and exclude misuse, unauthorized modification, accidental damage, normal wear, and failure to follow instructions.",
    # ENLOVA Water (a food: guide p.5 / p.11)
    "No claim is made that ENLOVA™ Water hydrates better than other compliant bottled water or improves circulation, metabolism, cognition, sleep, recovery, energy, or physical performance.":
        "ENLOVA™ Water is drinking water. No claim is made that it differs from or is better than other drinking water.",
    "Fluid needs vary. People with medically directed fluid, sodium, mineral, kidney, cardiac, or other dietary restrictions should follow professional guidance.":
        "Fluid needs vary from person to person. Follow any dietary guidance you have been given.",
    "Do not use for wound care, contact-lens care, nasal rinsing, injection, inhalation equipment, or another medical use.": "For drinking only.",
    "Do not use as a substitute for prescribed oral rehydration products or medical treatment.": None,
    "Retain the bottle, lot code, case, and purchase information when reporting contamination, illness, damage, or a quality concern.":
        "Retain the bottle, lot code, case, and purchase information when reporting a quality concern or damage.",
    "Reusable bottles, water-treatment products, LIPG products, subscriptions, and other products are not included unless expressly stated.":
        "Reusable bottles, LIPG products, subscriptions, and other products are not included unless expressly stated.",
    "This listing includes one case containing 24 bottles. No medical, enhanced-hydration, energy-transfer, or disease-related benefit is promised. If a subscription is offered, all pricing, shipping, renewal, and cancellation terms are disclosed before enrollment.":
        "This listing includes one case containing 24 bottles. If a subscription is offered, all pricing, shipping, renewal, and cancellation terms are disclosed before enrollment.",
    # ENLOVA Water Bottle
    "May contain a sealed, non-food-contact LIPG-related component, subject to verification":
        "May contain a sealed LIPG-related component that never touches the water, subject to verification",
    "No claim is made that the bottle changes water, improves absorption, increases hydration efficiency, adds nutrients, alters pH, transfers photons, removes contaminants, or produces a health benefit.":
        "No claim is made that the bottle changes the water in any way.",
    "Understand that the bottle is not a filter or water-treatment system": "Understand that the bottle is a container, not a filter",
    "It is not intended for infants, young children, infant formula, medication, medical nutrition, oral rehydration treatment, purification, disinfection, or unapproved beverages.":
        "For plain drinking water only. Not for infants or young children, or for infant formula or other liquids.",
    "Do not use for infant formula, medication, medical nutrition, or oral rehydration treatment.":
        "Use for plain drinking water only, not for infant formula or other liquids.",
    "By proceeding to checkout, the purchaser acknowledges that this product is a reusable food-contact container — not a filter, purifier, medical device, or water-treatment product — and that no claim is made that it changes water or produces a health benefit.":
        "By proceeding to checkout, the purchaser acknowledges that this product is a reusable container for plain drinking water, not a filter or purifier, and that no claim is made that it changes the water.",
}

# FAQ questions removed site-wide (disease/treatment framing that fails the one-question test).
DROP_FAQ = {
    "Does it treat insomnia, pain, or another medical condition?",
    "Can Customer Support recommend it for my symptoms?",
    "Can it treat a child's sleep, behavioral, or medical condition?",
    "Does it treat insomnia or sleep apnea?",
    "Can it be used with a CPAP mask?",
    "Is it intended to treat neck pain or stiffness?",
    "Does it realign the cervical spine?",
    "Is it compatible with CPAP equipment?",
    "Does it relieve eye strain or improve vision?",
    "Does it reduce puffiness, wrinkles, or dark circles?",
    "Does it treat a sleep disorder or medical condition?",
    "Does the QiRenew System regenerate cells?",
    "Is it intended to treat a medical condition?",
    "Can it replace medication or professional care?",
    "Does water need to remain in it for 24 or 48 hours?",
}

# FAQ answers/questions rewritten in place: question -> (new question or None to keep, new answer)
FAQ_REWRITE = {
    "Can I use more than one unit?": (None, "Additional units may be placed in separate personal wellness spaces. Individual experiences vary, and no particular result is promised from using more than one unit."),
    "Does it emit visible light?": (None, "Low-intensity photon emission is characterized with specialized optical equipment and may not be visible to the unaided eye."),
    "How does the Neck Pillow fit into Recovery Sleep?": (None, "It can provide cushioning during the wind-down before bed, such as seated reading, meditation, or calm breathing. Individual experiences vary, and no particular result is promised."),
    "Does it guarantee deeper, longer, or faster sleep?": ("Does it guarantee a particular sleep result?", "No. Individual experiences vary, and no particular result or timeframe is promised."),
    "Can several people use the same space?": (None, "Adults may share a general-wellness space when all safety instructions are followed. Individual experiences vary."),
    "Is it energized or biophoton-infused?": ("Is the water changed in any way?", "No. No claim is made that the water is changed in any way."),
    "Does it energize or charge water?": ("Does it change the water?", "No. It is a container for plain drinking water, and no claim is made that it changes the water."),
    "Does it improve hydration?": ("Does it make hydration different?", "It is a reusable container for drinking water. It is designed to make hydration a mindful part of your daily routine."),
    "Will several bottles produce a stronger effect?": ("Does using several bottles make a difference?", "No. Grouping bottles is not claimed to change the water or produce a different result."),
    "Do activated materials contact the water?": ("Does any internal material touch the water?", "No. Any LIPG-related component must remain permanently sealed and isolated from the water."),
}

# Spec rows removed from public pages (former names carry Red/Amber words; kept in the internal note).
DROP_SPEC = {"Former names", "Former name", "Former family"}
SPEC_REWRITE = {
    "Coverage / output claims": ("Coverage / output claims", "No coverage or comparative-strength claim is made"),
    "Treatment methods": ("Processing methods", "[Insert verified filtration, ozone, UV, or other processes]"),
}

# Guide Section 3 "Say this" lines, added as the first feature bullet.
SAY_THIS = {
    "biophotonizer-a": "Place near your bed, chair, or workspace to create a calming biophoton environment for everyday wellness.",
    "biophotonizer-c": "Supports a calm environment and complements a restful sleep routine for children 5 and older.",
    "qirenew-system": "Supports the flow of Qi (“energy”) and creates a relaxing, wellness-supportive environment at home.",
    "pillow": "Pairs ergonomic support with biophoton-infused materials to support relaxation as part of your evening routine.",
    "neck-pillow": "Provides a comfortable resting position to create a soothing environment for relaxation and restful sleep.",
    "eyemask": "Light-blocking eye mask designed for comfort, travel, screen breaks, and restful sleep routines.",
    "enlova-water-bottle": "Fill with drinking water to make daily hydration a mindful, refreshing part of your routine.",
}

# Product-specific lines kept under the required disclaimer (no Red words).
DISCLAIMER_EXTRA = {
    "biophotonizer-c": ["Biophotonizer C is not a toy and must be positioned and managed by an adult."],
    "enlova-water": ["ENLOVA™ Water is drinking water. No claim is made that the water is changed in any way."],
    "enlova-water-bottle": ["The ENLOVA™ Water Bottle does not filter or purify water. Fill it only with water that is already safe to drink."],
}

REWRITE.update({
    "Do not share; treat the eyemask as a personal-use hygiene product": "Do not share; keep the eyemask for personal use only",
    "Use stable surfaces and prevent falling or tripping hazards.": "Use stable surfaces and avoid falling or tripping hazards.",
})

# Guide p.14 house style: "and", not "&", in body text.
STYLE = {"Seated rest & passenger travel": "Seated rest and passenger travel"}


def _fix(text):
    for a, b in STYLE.items():
        text = text.replace(a, b)
    return text


def apply(products):
    for p in products:
        former = [f"{k}: {v}" for k, v in p["specs"] if k in DROP_SPEC]
        for key, val in list(p.items()):
            if isinstance(val, str) and val in REWRITE and REWRITE[val] is not None:
                p[key] = REWRITE[val]
            elif isinstance(val, list) and val and isinstance(val[0], str) and key not in ("disclaimer", "conflicts", "thumbs"):
                p[key] = [REWRITE.get(v, v) for v in val if REWRITE.get(v, v) is not None]
        p["faq"] = [(FAQ_REWRITE[q][0] or q, FAQ_REWRITE[q][1]) if q in FAQ_REWRITE else (q, a)
                    for q, a in p["faq"] if q not in DROP_FAQ]
        p["specs"] = [SPEC_REWRITE.get(k, (k, v)) for k, v in p["specs"] if k not in DROP_SPEC]
        if p["slug"] in SAY_THIS:
            p["features"] = [SAY_THIS[p["slug"]]] + p["features"]
        p["disclaimer"] = [REQUIRED_DISCLAIMER] + DISCLAIMER_EXTRA.get(p["slug"], [])
        p["facts"] = [(k, _fix(v)) for k, v in p["facts"]]
        if former:
            p["conflicts"] = p["conflicts"] + [f"Removed from public specs per Wellness Guide (Red/Amber words): {'; '.join(former)}."]
        p["conflicts"] = p["conflicts"] + ["Wellness Guide: “Recovery” is an Amber word — the Recovery Sleep™ program name needs Regulatory sign-off."] \
            if "Recovery Sleep" in p["program"] or "Recovery Sleep" in p["purpose"] else p["conflicts"]
    return products
