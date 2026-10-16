"""Builds the QiRenew email series for acupuncture center owners.

Every email shares one table-based, inline-styled template (matching the
existing QiRenew practitioner emails) so it pastes cleanly into an email
builder. Edit the copy in EMAILS below, then run:  python3 build.py
"""
from pathlib import Path

OUT = Path(__file__).parent

BOOKING_LINK = "https://api.leadconnectorhq.com/widget/booking/nARZoutps8cBpj9hxNWf"
UNSUBSCRIBE_LINK = "{{unsubscribe_link}}"  # GoHighLevel merge field
IMG_BASE = ("https://raw.githubusercontent.com/TeslaBioHealing/Build1/"
            "5ec57e6160d2f57a2b946fca0ad3d4e54642b766/emails/acupuncture-series/images")

# Brand tokens (same palette as the QiRenew practitioner emails)
DEEP = "#173625"
GOLD = "#b3893f"
INK = "#1d2c20"
SUB = "#6c7566"
PAPER = "#faf7ef"
OUTER = "#f3ecd9"
PANEL = "#f3ead2"
PANEL_LINE = "#e6dbbd"
SERIF = "Georgia,'Times New Roman',serif"
SANS = "Arial,Helvetica,sans-serif"

# Mandatory QiRenew footer disclaimer (QiRenew website copy compliance update, section 7)
DISCLAIMER = (
    "QiRenew products are intended for general wellness purposes only, including "
    "supporting relaxation, comfort, everyday vitality, and healthy sleep routines. They "
    "are not intended to diagnose, treat, cure, or prevent any disease or medical "
    "condition, and are not a substitute for professional medical advice, diagnosis, or "
    "treatment. QiRenew products are non-invasive, passive wellness devices designed to "
    "present a low risk when used as directed."
)


# ---------- building blocks ----------

def p(text):
    return (f'<p style="margin:0 0 18px 0;font-family:{SANS};font-size:15px;'
            f'line-height:1.65;color:{INK};">{text}</p>')


def h2(text):
    return (f'<p style="margin:26px 0 12px 0;font-family:{SERIF};font-size:19px;'
            f'line-height:1.35;color:{DEEP};">{text}</p>')


def rows(items):
    """Cream panel rows with a gold circle marker, as in the reference email.
    items: list of (glyph, title, description-or-None)."""
    out = []
    for glyph, title, desc in items:
        body = f'<span style="font-weight:bold;">{title}</span>' if desc else title
        if desc:
            body += (f'<br><span style="display:inline-block;margin-top:4px;color:{SUB};'
                     f'font-size:13.5px;line-height:1.55;">{desc}</span>')
        out.append(f'''
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 10px 0;">
  <tr>
    <td style="background:{PANEL};border:1px solid {PANEL_LINE};padding:16px 14px;">
      <table role="presentation" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td valign="top" style="width:30px;">
            <div style="width:30px;height:30px;line-height:30px;border-radius:50%;background:{GOLD};color:#ffffff;text-align:center;font-family:{SANS};font-size:14px;font-weight:bold;">{glyph}</div>
          </td>
          <td valign="middle" style="padding-left:14px;font-family:{SANS};font-size:14px;line-height:1.5;color:{INK};">{body}</td>
        </tr>
      </table>
    </td>
  </tr>
</table>''')
    return "".join(out) + '<div style="height:12px;line-height:12px;">&nbsp;</div>'


def quote(label, text):
    """Bordered example block (used for sample wording)."""
    return f'''
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 22px 0;">
  <tr>
    <td style="background:{PANEL};border-left:3px solid {GOLD};padding:16px 18px;font-family:{SANS};">
      <div style="font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:{GOLD};font-weight:bold;margin-bottom:8px;">{label}</div>
      <div style="font-family:{SERIF};font-size:16px;line-height:1.6;color:{DEEP};">{text}</div>
    </td>
  </tr>
</table>'''


def img(file, alt):
    """Full-width photo. Served from the public repo, pinned to the commit that added it."""
    return f'''
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 24px 0;">
  <tr>
    <td><img src="{IMG_BASE}/{file}" alt="{alt}" width="536" style="display:block;width:100%;max-width:536px;height:auto;border:0;outline:none;text-decoration:none;"></td>
  </tr>
</table>'''


def faq(q, a):
    return (f'<p style="margin:0 0 6px 0;font-family:{SANS};font-size:15px;line-height:1.5;'
            f'color:{DEEP};font-weight:bold;">{q}</p>' + p(a))


def button(label):
    return f'''
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:10px 0 30px 0;">
  <tr>
    <td style="background:{DEEP};border-radius:999px;">
      <a href="{BOOKING_LINK}" style="display:inline-block;padding:14px 30px;font-family:{SANS};font-size:14px;font-weight:bold;color:#ffffff;text-decoration:none;border-radius:999px;">{label} &rarr;</a>
    </td>
  </tr>
</table>'''


def render(e):
    body = "".join(e["body"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e["subject"]}</title>
<!-- Day {e["day"]} | Subject: {e["subject"]} | Preheader: {e["preheader"]} -->
</head>
<body style="margin:0;padding:0;background:{OUTER};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{OUTER};">{e["preheader"]}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{OUTER};">
  <tr>
    <td align="center" style="padding:28px 12px;">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:{PAPER};">

        <!-- Header -->
        <tr>
          <td style="background:{DEEP};border-bottom:4px solid {GOLD};padding:26px 32px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="font-family:{SERIF};font-size:22px;color:#ffffff;">QiRenew <span style="color:{GOLD};">&middot;</span></td>
                <td align="right" style="font-family:{SANS};font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:#d9e2d6;">Biophoton wellness for calm spaces</td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding:36px 32px 8px 32px;">
            <p style="margin:0 0 12px 0;font-family:{SANS};font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:{GOLD};font-weight:bold;">{e["eyebrow"]}</p>
            <h1 style="margin:0 0 22px 0;font-family:{SERIF};font-size:26px;line-height:1.3;font-weight:normal;color:{DEEP};">{e["headline"]}</h1>
            {p("Hi {{contact.first_name}},")}
            {body}
            {button(e["cta"])}
            <p style="margin:0 0 32px 0;font-family:{SANS};font-size:14px;line-height:1.75;color:{SUB};">Warmly,<br>Janno Ray Guinayhan<br>QiRenew Team</p>
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background:{DEEP};padding:24px 32px;font-family:{SANS};font-size:11px;line-height:1.7;color:#c9d4c6;">
            <span style="color:#ffffff;font-weight:bold;">General Wellness Notice:</span> {DISCLAIMER}
            <div style="height:12px;line-height:12px;">&nbsp;</div>
            &copy; 2026 QiRenew &nbsp;&middot;&nbsp; <a href="{UNSUBSCRIBE_LINK}" style="color:#ffffff;text-decoration:underline;">Unsubscribe</a>
          </td>
        </tr>

      </table>
    </td>
  </tr>
</table>
</body>
</html>
'''


# ---------- the series ----------

# Written for acupuncture center owners and decision makers. Each email stands
# alone and follows Problem -> Agitate -> Solution. The "problem" is always a
# business or client-experience problem, never a health condition.
EMAILS = [
    {
        "day": 1,
        "slug": "day-1-what-it-is",
        "subject": "What makes a client choose your acupuncture center?",
        "preheader": "When every center offers acupuncture, the experience is what clients remember.",
        "eyebrow": "For acupuncture center owners",
        "headline": "Give clients a reason to choose your center",
        "body": [
            # Problem
            p("Most acupuncture centers in a given area offer similar services, similar session "
              "lengths, and similar prices. From the outside, it's hard for a new client to tell "
              "one center from the next."),
            # Agitate
            p("When the experience feels interchangeable, clients decide on price and "
              "convenience. They try the center that's closer, cheaper, or running a promotion, "
              "and the relationship you've built becomes easy to walk away from."),
            # Solution
            h2("Meet the QiRenew System"),
            img("qirenew-system-units.jpg", "The QiRenew System: four solid-state biophoton units"),
            p("The QiRenew System is a general wellness device system crafted with proprietary "
              "biophoton technology and made with activated mineral composites. Its solid-state "
              "units are designed to enhance the flow of Qi (&ldquo;energy&rdquo;), promote a "
              "soothing environment, and support healthy, restful sleep routines."),
            p("For an acupuncture center, that means a calm, Qi-centered environment clients can "
              "feel the moment they walk in, built around the same idea your practice is built "
              "on."),
            h2("Why centers choose it"),
            rows([
                ("1", "A signature client experience",
                 "A Qi-centered environment gives clients something to remember about your "
                 "center, and something to tell their friends about."),
                ("2", "A natural fit for your philosophy",
                 "It's designed around the flow of Qi, so it feels at home in an acupuncture "
                 "center instead of feeling like a gadget."),
                ("3", "No added work for your team",
                 "It's passive: no setup, no cords, no heat, and nothing for your staff to "
                 "manage."),
            ]),
            p("It's a general wellness device. It isn't intended to diagnose, treat, cure, or "
              "prevent any condition, and it doesn't change the work you do. It elevates the "
              "space that work happens in."),
            p("Janno can show you how centers like yours set it up in a short, practical call."),
        ],
        "cta": "See How QiRenew Fits Your Center",
    },
    {
        "day": 2,
        "slug": "day-2-qi-and-environment",
        "subject": "Wellness technology that speaks the language of Qi",
        "preheader": "Most wellness tech feels out of place in an acupuncture center. This was designed for it.",
        "eyebrow": "Built around Qi",
        "headline": "Wellness technology that belongs in an acupuncture center",
        "body": [
            # Problem
            p("Most wellness technology is designed for gyms, spas, or tech-savvy consumers: "
              "screens, apps, blinking lights, and subscription dashboards."),
            # Agitate
            p("Bring that into an acupuncture center and it clashes with everything you've "
              "built. The calm, Qi-centered experience clients come to you for starts to feel "
              "like a showroom, and your team ends up explaining a gadget instead of focusing on "
              "clients."),
            # Solution
            h2("Designed around the same idea as your practice"),
            p("QiRenew starts where your practice starts: with Qi (&ldquo;energy&rdquo;). The "
              "QiRenew System creates a calming biophoton environment that supports the flow of "
              "Qi and a calm mind. There are no screens and nothing to operate. It's simply part "
              "of the room."),
            p("That makes it easy to layer QiRenew with the relaxation sessions, mindfulness "
              "practices, and holistic modalities your center already offers."),
            quote("Why it fits",
                  "Your work is the session. QiRenew makes the environment around it feel as "
                  "intentional as the work itself."),
            h2("What your clients notice"),
            rows([
                ("1", "A calm, intentional atmosphere from the moment they arrive", None),
                ("2", "A space that reflects the Qi philosophy they chose you for", None),
                ("3", "Nothing distracting: no screens, no sounds, no setup", None),
            ]),
            h2("What we don't claim"),
            p("We don't claim QiRenew changes the outcome of any session, and it isn't meant to "
              "be part of anyone's health plan. It's a general wellness product designed to make "
              "your center feel even more restful."),
        ],
        "cta": "Talk to Janno About Your Center",
    },
    {
        "day": 3,
        "slug": "day-3-placement",
        "subject": "Zero setup, zero staff time: how centers place QiRenew",
        "preheader": "It fits a busy acupuncture schedule without changing a single session.",
        "eyebrow": "Built for busy centers",
        "headline": "It fits your center without changing how you run it",
        "body": [
            # Problem
            p("Every acupuncture center owner knows the math: rooms turn over all day, and your "
              "team's time belongs to clients."),
            # Agitate
            p("New equipment usually means setup, training, cords, upkeep, and a few extra "
              "minutes per session. Across a full week, that adds up, and anything that needs "
              "regular attention tends to end up pushed into a closet."),
            # Solution
            h2("Passive by design"),
            img("qirenew-acupuncture-room.jpg",
                "A calm acupuncture session room with QiRenew units placed along the walls"),
            p("The QiRenew System is passive: no cords, no heat, nothing to switch on, and "
              "nothing for your staff to learn. Place it once and it simply stays part of the "
              "room."),
            h2("Where centers place it"),
            rows([
                ("1", "Session rooms",
                 "Placed along the walls or near the table, out of the way of your work."),
                ("2", "The waiting area",
                 "Near seating, so a calm, relaxing environment greets clients at check-in."),
                ("3", "The relaxation room",
                 "Near a chair or quiet corner where clients unwind before heading back into "
                 "their day."),
            ]),
            p("We size each setup to your center: its rooms, its layout, and where clients spend "
              "their time. We don't recommend a number of units or hours for any health goal. "
              "It's about the feel of your space."),
        ],
        "cta": "Plan Your Space with Janno",
    },
    {
        "day": 4,
        "slug": "day-4-talking-with-clients",
        "subject": "What your clients do between visits",
        "preheader": "Keep your center part of their everyday routine, not just their appointment.",
        "eyebrow": "Beyond the session",
        "headline": "Stay part of your clients' routine between visits",
        "body": [
            # Problem
            p("Your relationship with a client is strongest during their visit. Then they go "
              "home, and for days or weeks, your center isn't part of their day at all."),
            # Agitate
            p("That's when routines drift and other options start to look appealing. Clients ask "
              "what they can do at home, and if you don't have an answer, they find one "
              "somewhere else, usually from a store or website that has nothing to do with your "
              "center."),
            # Solution
            h2("A natural recommendation from your center"),
            p("The QiRenew System is designed to support the flow of Qi (&ldquo;energy&rdquo;) "
              "and create a relaxing, wellness-supportive environment at home. Clients can place "
              "it near their bed, chair, or workspace as part of their everyday routine, and "
              "every time they see it, they're reminded of your center."),
            h2("Talking about it the right way"),
            p("We give partner centers clear, approved wording so every recommendation stays "
              "focused on wellness: relaxation, comfort, calm, everyday well-being, and the flow "
              "of Qi. If a client asks about a health concern, the answer is simple:"),
            quote("Example wording",
                  "&ldquo;Thanks for asking. It isn't designed for any medical condition, so I "
                  "can't say that, and your doctor is the best person to ask. Many people simply "
                  "enjoy it as part of a calm, relaxing space at home.&rdquo;"),
            p("Clear wording protects your center's reputation and keeps every conversation "
              "honest, which is exactly what clients expect from you."),
        ],
        "cta": "Ask Janno About Offering QiRenew",
    },
    {
        "day": 5,
        "slug": "day-5-common-questions",
        "subject": "The questions acupuncture center owners ask before saying yes",
        "preheader": "Straight answers on setup, fit, sizing, and next steps.",
        "eyebrow": "Before you decide",
        "headline": "The questions center owners ask before saying yes",
        "body": [
            # Problem
            p("Bringing anything new into your center is a business decision. You need to know "
              "it will be used, that it fits your brand, and that it won't create extra work or "
              "risk."),
            # Agitate
            p("Most wellness products bury those answers under sales language. Guess wrong, and "
              "you're left with a box in the closet and an awkward conversation with your team."),
            # Solution
            p("So here are straight answers."),
            img("qirenew-packaging.jpg", "QiRenew units in their gold packaging"),
            faq("Will my team need training or setup time?",
                "No. It's passive: no cords, nothing to switch on, and nothing to adjust. Unpack "
                "it, place it, and you're done."),
            faq("Will it fit the look and feel of my center?",
                "The solid-state units have a clean, minimal gold finish designed to sit quietly "
                "in session rooms, waiting areas, and relaxation rooms."),
            faq("How many units does my center need?",
                "That depends on your space, not on any health goal. On a call, we look at your "
                "rooms and layout and recommend a setup that fits."),
            faq("What can my team say to clients?",
                "We provide approved wellness wording, so your team can talk about it with "
                "confidence. It's a general wellness product designed to support relaxation, "
                "comfort, and everyday well-being. It isn't intended to diagnose, treat, cure, or "
                "prevent any condition."),
            faq("Can clients use it at home?",
                "Yes. The QiRenew System is designed to create a relaxing, wellness-supportive "
                "environment at home, too, which gives your center a natural way to stay part of "
                "clients' everyday routine."),
            faq("What happens on the call?",
                "A focused, 30-minute conversation with Janno about your center, your rooms, and "
                "your goals. If it's not a fit, you'll know quickly, and that's a perfectly good "
                "outcome."),
            p("If QiRenew makes sense for your center, the next step is simple."),
        ],
        "cta": "Book a 30-Minute Call with Janno",
    },
]


def build_index():
    cards = "".join(
        f'<section><h2>Day {e["day"]}: {e["subject"]}</h2>'
        f'<p><b>Preheader:</b> {e["preheader"]} &nbsp;|&nbsp; <a href="{e["slug"]}.html">Open on its own</a></p>'
        f'<iframe src="{e["slug"]}.html" title="Day {e["day"]}"></iframe></section>'
        for e in EMAILS)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Acupuncture Email Series</title>
<style>
body{{margin:0;background:{OUTER};font-family:{SANS};color:{INK};}}
header{{background:{DEEP};color:#fff;padding:22px 16px;border-bottom:4px solid {GOLD};text-align:center;}}
header h1{{margin:0;font-family:{SERIF};font-weight:normal;font-size:24px;}}
header p{{margin:6px 0 0;color:#d9e2d6;font-size:13px;}}
section{{max-width:680px;margin:28px auto;padding:0 16px;}}
section h2{{font-family:{SERIF};font-weight:normal;color:{DEEP};font-size:20px;margin:0 0 4px;}}
section p{{font-size:13px;color:{SUB};margin:0 0 10px;}}
section a{{color:{DEEP};}}
iframe{{width:100%;height:1500px;border:1px solid {PANEL_LINE};background:#fff;}}
</style></head><body>
<header><h1>QiRenew &middot; Acupuncture Practitioner Series</h1><p>5 standalone emails &middot; Problem, Agitate, Solution</p></header>
{cards}
</body></html>
'''


if __name__ == "__main__":
    for e in EMAILS:
        (OUT / f'{e["slug"]}.html').write_text(render(e))
    (OUT / "index.html").write_text(build_index())
    print(f"Built {len(EMAILS)} emails + index.html in {OUT}")
