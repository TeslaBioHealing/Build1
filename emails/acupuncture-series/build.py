"""Builds the 5-day QiRenew acupuncture-practitioner email series.

Every email shares one table-based, inline-styled template (matching the
existing QiRenew practitioner emails) so it pastes cleanly into an email
builder. Edit the copy in EMAILS below, then run:  python3 build.py
"""
from pathlib import Path

OUT = Path(__file__).parent

BOOKING_LINK = "https://api.leadconnectorhq.com/widget/booking/nARZoutps8cBpj9hxNWf"
UNSUBSCRIBE_LINK = "{{unsubscribe_link}}"  # GoHighLevel merge field

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
                <td align="right" style="font-family:{SANS};font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:#d9e2d6;">By Tesla BioHealing</td>
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
            &copy; 2026 QiRenew, a Tesla BioHealing company &nbsp;&middot;&nbsp; <a href="{UNSUBSCRIBE_LINK}" style="color:#ffffff;text-decoration:underline;">Unsubscribe</a>
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

# Each email stands alone (no references to other emails) and follows
# Problem -> Agitate -> Solution. The "problem" is always about the practice,
# the space, or the conversation, never a health condition.
EMAILS = [
    {
        "day": 1,
        "slug": "day-1-what-it-is",
        "subject": "What biophoton wellness is, and what it isn't",
        "preheader": "A plain-language explanation. No pitch attached.",
        "eyebrow": "A note for acupuncture practitioners",
        "headline": "A plain-language look at biophoton wellness",
        "body": [
            # Problem
            p("New wellness technologies come across a practitioner's desk all the time. Most "
              "arrive with big promises and very little explanation of what the product "
              "actually is."),
            # Agitate
            p("That leaves you guessing. When the claims are bigger than the explanation, it's "
              "hard to know what you'd be bringing into your space, or what you'd say to the "
              "clients who trust your judgment."),
            # Solution
            h2("So here is QiRenew, in plain language"),
            p("The QiRenew System is a general wellness device system crafted with proprietary "
              "biophoton technology. Made with activated mineral composites, its solid-state units "
              "are designed to enhance the flow of Qi (&ldquo;energy&rdquo;), promote a soothing "
              "environment, and support healthy, restful sleep routines. You simply place it near "
              "a bed, chair, or workspace."),
            rows([
                ("&#10003;", "Passive: no setup and nothing to adjust", None),
                ("&#10003;", "No lasers, no heat, no cords", None),
                ("&#10003;", "Designed for relaxation, comfort, and everyday well-being", None),
            ]),
            h2("What it isn't"),
            p("It isn't a medical device, and it isn't intended to diagnose, treat, cure, or "
              "prevent any condition. It's not a substitute for professional care, and it doesn't "
              "replace anything you do in your practice. We think being clear about that up front "
              "is the most useful thing we can offer."),
            p("If you'd like to know more about how it works in a space like yours, Janno is "
              "happy to answer questions. No pitch, just information."),
        ],
        "cta": "Ask Janno a Question",
    },
    {
        "day": 2,
        "slug": "day-2-qi-and-environment",
        "subject": "The room is part of the experience",
        "preheader": "Qi, environment, and the space around a session.",
        "eyebrow": "Qi, energy, and environment",
        "headline": "Why the space around a session matters",
        "body": [
            # Problem
            p("A session can feel calm. The space around it often doesn't. Clients arrive "
              "straight from traffic, a full inbox, or a busy day, and they sit under bright "
              "lights with their phones while they wait."),
            # Agitate
            p("Those few minutes before and after a session shape how the whole visit feels. "
              "When the room feels rushed, it's harder for clients to settle in and unwind, no "
              "matter how much care goes into your work."),
            # Solution
            h2("Making the environment part of the experience"),
            p("In your work, Qi (&ldquo;energy&rdquo;) is a central idea, and you already know "
              "that the setting matters: the light, the quiet, the temperature. That setting is "
              "the part of the picture QiRenew is designed for. The QiRenew System creates a "
              "calming biophoton environment that supports the flow of Qi and a calm mind. It "
              "isn't a technique. It's part of the room itself."),
            p("Some practitioners layer QiRenew with the relaxation sessions, mindfulness "
              "practices, and holistic modalities they already offer in their wellness space."),
            quote("A simple way to think about it",
                  "Your work is the session. QiRenew is designed to be part of the calm "
                  "environment the session happens in."),
            h2("What a calm environment can include"),
            rows([
                ("1", "Comfortable seating and a quiet place to rest", None),
                ("2", "Soft lighting and an uncluttered, peaceful room", None),
                ("3", "A biophoton environment that supports the flow of Qi", None),
            ]),
            h2("What we don't claim"),
            p("We don't claim QiRenew changes the outcome of any session, and it isn't meant to "
              "be part of anyone's health plan. It's a general wellness product, a way to help a "
              "calm space feel even more restful."),
        ],
        "cta": "Talk It Through with Janno",
    },
    {
        "day": 3,
        "slug": "day-3-placement",
        "subject": "Where practitioners actually place it",
        "preheader": "Practical notes: waiting areas, relaxation rooms, and your own desk.",
        "eyebrow": "Practical placement",
        "headline": "Where it fits in a working practice",
        "body": [
            # Problem
            p("Adding anything new to a working practice usually comes with strings attached: "
              "setup, cords, training, upkeep, or a change to how your sessions run."),
            # Agitate
            p("When your schedule is already full, even small changes add friction. And anything "
              "that needs regular attention tends to end up pushed into a closet within a few "
              "months."),
            # Solution
            h2("Designed to stay in the background"),
            p("The QiRenew System is passive, so there's nothing for you or your clients to do. "
              "It's simple to incorporate into relaxation rooms and other wellness spaces, and "
              "it sits quietly where you place it."),
            h2("Three common places"),
            rows([
                ("1", "The waiting area",
                 "Placed near seating to create a calm, relaxing environment from the moment "
                 "clients arrive."),
                ("2", "The relaxation room",
                 "Positioned near a chair or quiet corner where clients unwind before heading "
                 "back into their day."),
                ("3", "Your own workspace",
                 "Many practitioners start with one near their own desk or chair, so they can "
                 "experience the environment for themselves first."),
            ]),
            h2("A few practical notes"),
            p("There are no cords, no heat, and nothing to switch on, so it won't add steps to "
              "your day or change how you run your sessions."),
            p("We also don't recommend a number of units or hours for any health goal. "
              "Placement is simply about comfort and the feel of the room, and that's a "
              "conversation about your space, not about anyone's health."),
        ],
        "cta": "Walk Through Your Space with Janno",
    },
    {
        "day": 4,
        "slug": "day-4-talking-with-clients",
        "subject": "How to talk about it with your clients",
        "preheader": "The wording we use, and the simple test behind it.",
        "eyebrow": "Talking with clients",
        "headline": "How to talk about it with your clients",
        "body": [
            # Problem
            p("Clients notice anything new in your space, and they ask about it, often with a "
              "personal health question attached."),
            # Agitate
            p("Without clear wording ready, a well-meaning answer can easily drift into promises "
              "about health or results that no wellness product should make. That puts you in an "
              "awkward spot, and it isn't fair to the client either."),
            # Solution
            h2("The words we use"),
            p("We've put a lot of care into how we describe QiRenew, and we're happy to share "
              "that language with you: relaxation, comfort, calm, everyday well-being, a restful "
              "sleep routine, and the flow of Qi (&ldquo;energy&rdquo;). We stay away from "
              "anything about health conditions, symptoms, or medical results, and we don't "
              "compare it to medical devices."),
            h2("If a client asks about a health concern"),
            rows([
                ("1", "Acknowledge",
                 "Thank them for asking. There's no need to comment on their concern."),
                ("2", "Clarify",
                 "Explain that it's a general wellness device, not designed for any medical "
                 "condition, and that their doctor is the best person for health questions."),
                ("3", "Refocus",
                 "Bring it back to comfort, relaxation, and the calm of the space."),
            ]),
            quote("Example wording",
                  "&ldquo;Thanks for asking. It isn't designed for any medical condition, so I "
                  "can't say that, and your doctor is the best person to ask. Many people simply "
                  "enjoy it as part of a calm, relaxing space.&rdquo;"),
            h2("The one-question test"),
            p("Before describing it, we ask ourselves one question: <em>would this sentence still "
              "make sense to someone with no health concerns at all?</em> If it would, it's "
              "wellness language. If it wouldn't, we rephrase it."),
        ],
        "cta": "Ask Janno Your Questions",
    },
    {
        "day": 5,
        "slug": "day-5-common-questions",
        "subject": "Your questions, answered",
        "preheader": "The questions practitioners ask us most, in one place.",
        "eyebrow": "Common questions",
        "headline": "Answers to the questions practitioners ask most",
        "body": [
            # Problem
            p("Practitioners looking at something new for their space tend to ask the same "
              "handful of practical questions."),
            # Agitate
            p("The answers are usually buried in sales pages or vague marketing language, which "
              "makes it hard to tell whether something is even worth a conversation."),
            # Solution
            p("So here are straight answers to the questions we hear most often."),
            faq("Does it need power or setup?",
                "No. It's passive: no cords, nothing to switch on, and nothing to set up."),
            faq("Does it produce heat, or anything I need to manage?",
                "No lasers and no heat. The QiRenew System is solid-state and designed to create a calming "
                "biophoton environment, and it sits quietly in the background."),
            faq("Is it meant to be part of a client's health plan?",
                "No. It's a general wellness product designed to support relaxation, comfort, and "
                "everyday well-being. It isn't intended to diagnose, treat, cure, or prevent any "
                "condition, and it doesn't replace anything you or a client's doctor does."),
            faq("How many would I need?",
                "There's no &ldquo;right amount&rdquo; for any health goal, and we won't suggest "
                "one. If we talk, it's about your space: its size, its layout, and where clients "
                "rest."),
            faq("Can it be used at home, too?",
                "Yes. The QiRenew System is designed to support the flow of Qi "
                "(&ldquo;energy&rdquo;) and create a relaxing, wellness-supportive environment at "
                "home. Some people place it near their bed, chair, or workspace as part of their "
                "everyday routine."),
            faq("What happens on a call?",
                "A relaxed, 30-minute conversation with Janno about your space and any questions "
                "you still have. If it's not a fit, that's a perfectly good outcome too."),
            p("Whether or not QiRenew is right for your practice, we hope these answers are "
              "useful."),
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
