# QiRenew · Janno Appointment Emails (GHL)

Five HTML emails for a GoHighLevel appointment workflow on Janno's calendar.

| File | GHL template name | Send | Subject | Preview text |
|---|---|---|---|---|
| `01-confirmation.html` | Booking Confirmation Email | Immediately after booking | Your appointment with {{appointment.user.name}} is confirmed | {{appointment.only_start_date}} at {{appointment.only_start_time}}. We look forward to seeing you. |
| `02-reminder-24-hours.html` | Booking Email 24 Hours | 24 hours before start | Reminder: your appointment is tomorrow | See you tomorrow at {{appointment.only_start_time}} with {{appointment.user.name}}. |
| `03-reminder-1-hour.html` | Booking Email 1 Hour Before | 1 hour before start | Starting soon: your appointment in 1 hour | See you at {{appointment.only_start_time}} with {{appointment.user.name}}. |
| `04-cancellation.html` | Booking Cancellation Email | When an appointment is cancelled | Your appointment has been cancelled | Your appointment with {{appointment.user.name}} was cancelled. Book a new time anytime. |
| `05-reschedule.html` | Booking Reschedule Email | When an appointment is rescheduled | Your appointment has been rescheduled | New time: {{appointment.only_start_date}} at {{appointment.only_start_time}} with {{appointment.user.name}}. |

## Setup

The templates are saved in the **Cell Renew** sub-account under *Marketing → Emails → Templates*.
Janno's calendar (*Janno's Personal Calendar*) is assigned to Janno Ray Guinayhan, so
`{{appointment.user.name}}` resolves to his name. The Zoom link comes from
`{{appointment.meeting_location}}`, which is only filled when the calendar's meeting location is set to Zoom.

1. **Logo:** already in every template, loaded from the Cell Renew Media Library
   (`https://assets.cdn.filesafe.space/AkwM87DEglqY1HOx6mnF/media/6abd313511d7faddd405dd21.png`).
2. **Workflow:** trigger *Customer Booked Appointment*, filtered to Janno's calendar.
   - Send Email → `01-confirmation.html`
   - Wait → *Event/Appointment time*, 24 hours before → Send Email → `02-reminder-24-hours.html`
   - Wait → *Event/Appointment time*, 1 hour before → Send Email → `03-reminder-1-hour.html`
3. In each Send Email step, choose *Code editor / Custom HTML*, paste the file contents, and set the subject and preview text from the table.
4. Make sure **Settings → Business Profile** (name, address, phone, email) is filled in — the footer uses those values.

Janno's booking link (used in the cancellation and reschedule emails):
https://api.leadconnectorhq.com/widget/booking/iWg3H3Ls5qLVwdm5xwL1

## Merge fields used

`{{contact.first_name}}`, `{{appointment.user.name}}`, `{{appointment.only_start_date}}`,
`{{appointment.only_start_time}}`, `{{appointment.timezone}}`, `{{appointment.meeting_location}}`,
`{{appointment.reschedule_link}}`, `{{appointment.cancellation_link}}`,
`{{appointment.add_to_google_calendar}}`, `{{appointment.add_to_ical_outlook}}`,
`{{location.full_address}}`, `{{location.phone}}`, `{{location.email}}`

Brand colors: green `#07931D` (from logo), dark green `#056E16`, tint `#EAF6EC`.
