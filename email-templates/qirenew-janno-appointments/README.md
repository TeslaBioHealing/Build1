# QiRenew · Janno Appointment Emails (GHL)

Three HTML emails for a GoHighLevel appointment workflow on Janno's calendar.

| File | GHL template name | Send | Subject | Preview text |
|---|---|---|---|---|
| `01-confirmation.html` | Booking Confirmation Email | Immediately after booking | Your appointment with {{appointment.user.name}} is confirmed | {{appointment.only_start_date}} at {{appointment.only_start_time}}. We look forward to seeing you. |
| `02-reminder-24-hours.html` | Booking Email 24 Hours | 24 hours before start | Reminder: your appointment is tomorrow | See you tomorrow at {{appointment.only_start_time}} with {{appointment.user.name}}. |
| `03-reminder-1-hour.html` | Booking Email 1 Hour Before | 1 hour before start | Starting soon: your appointment in 1 hour | See you at {{appointment.only_start_time}} with {{appointment.user.name}}. |

## Setup

The templates are saved in the **Cell Renew** sub-account under *Marketing → Emails → Templates*.
Janno's calendar (*Janno's Personal Calendar*) is assigned to Janno Ray Guinayhan, so
`{{appointment.user.name}}` resolves to his name. The Zoom link comes from
`{{appointment.meeting_location}}`, which is only filled when the calendar's meeting location is set to Zoom.

1. **Logo:** upload `qirenew-logo.png` to *Media Library*, copy its URL, and create a custom value
   named **QiRenew Logo URL** (key `{{custom_values.qirenew_logo_url}}`) under *Settings → Custom Values*.
2. **Workflow:** trigger *Customer Booked Appointment*, filtered to Janno's calendar.
   - Send Email → `01-confirmation.html`
   - Wait → *Event/Appointment time*, 24 hours before → Send Email → `02-reminder-24-hours.html`
   - Wait → *Event/Appointment time*, 1 hour before → Send Email → `03-reminder-1-hour.html`
3. In each Send Email step, choose *Code editor / Custom HTML*, paste the file contents, and set the subject and preview text from the table.
4. Make sure **Settings → Business Profile** (name, address, phone, email) is filled in — the footer uses those values.

## Merge fields used

`{{contact.first_name}}`, `{{appointment.user.name}}`, `{{appointment.only_start_date}}`,
`{{appointment.only_start_time}}`, `{{appointment.timezone}}`, `{{appointment.meeting_location}}`,
`{{appointment.reschedule_link}}`, `{{appointment.cancellation_link}}`,
`{{appointment.add_to_google_calendar}}`, `{{appointment.add_to_ical_outlook}}`,
`{{location.name}}`, `{{location.full_address}}`, `{{location.phone}}`, `{{location.email}}`,
`{{custom_values.qirenew_logo_url}}`

Brand colors: green `#07931D` (from logo), dark green `#056E16`, tint `#EAF6EC`.
