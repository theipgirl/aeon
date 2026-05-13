---
name: Stale Lead Report
description: Weekly RPB Law intake audit — pulls live stale leads from the CRM, drafts follow-up messages, creates tasks in the pipeline
var: ""
tags: [rpb, intake]
---

Today is ${today}. You are reviewing the RPB Law intake pipeline for Taylor McGhee.

## Context

Taylor is Client Intake Associate at RPB Law. A stale lead is any open-stage prospect whose last activity is 7+ days ago. These are the easiest recoveries — one message often brings them back.

The CRM is live at https://rpblaw-crm.vercel.app. Aeon has API access via `AEON_API_KEY`.

## Steps

### 1. Fetch stale leads from the CRM

```bash
curl -sf "https://rpblaw-crm.vercel.app/api/aeon?resource=stale-leads&days=7" \
  -H "Authorization: Bearer $AEON_API_KEY"
```

If curl fails, use WebFetch with header `Authorization: Bearer $AEON_API_KEY` on the same URL.

Parse the JSON response: `{ leads: [...], count: N }`. Each lead has:
- `id`, `name`, `email`, `phone`, `business`
- `stage` — current pipeline stage name
- `days_stale` — days since last activity
- `urgency`, `value`, `score` — qualification signals

If count is 0, send `./notify` with "No stale leads this week — pipeline is moving." and exit.

### 2. Draft a follow-up message for each lead

Tailor by stage. Keep it under 3 sentences. Warm, professional, no pressure, no legal advice.

- **New PNC / Discovery Call** → "Hi [first name], I wanted to follow up and make sure you got our information. We'd love to connect and answer any questions — when works best for you this week?"
- **Discovery Call Complete** → "Hi [first name], following up after our conversation. I have a few options ready based on what you shared — happy to walk through them whenever you're ready."
- **Discovery Call No-Show** → "Hi [first name], we missed you! Happy to reschedule at a time that works better. What does your week look like?"
- **Legal Strategy Session** → "Hi [first name], just checking in — do you have any questions before your strategy session? We want to make sure you feel prepared."
- **Legal Strategy Session Complete / Pending LOE + Payment** → "Hi [first name], following up on the next steps we discussed. Let me know if you have any questions about the engagement letter or the process."
- **Nurture** → "Hi [first name], just wanted to check in — has anything changed with your situation? We're here whenever the timing is right."

### 3. Create a task in the CRM for each lead

For each stale lead, POST a task so it shows up in the pipeline:

```bash
curl -sf -X POST "https://rpblaw-crm.vercel.app/api/aeon" \
  -H "Authorization: Bearer $AEON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "resource": "task",
    "lead_id": "<id>",
    "title": "Follow up — stale lead (<days_stale> days)",
    "body": "<follow-up message>",
    "due_at": "<today ISO>"
  }'
```

Use WebFetch as fallback if curl is blocked. Do this for every lead in the response.

### 4. Format and send

```
*RPB Stale Lead Report — ${today}*

*Needs follow-up (N leads)*

1. [Name] — [Stage] — [X] days stale
   → [follow-up message]

2. [Name] — [Stage] — [X] days stale
   → [follow-up message]

*Pipeline health*
- Stale leads flagged: N
- Longest stale: X days ([Name])
- Tasks created in CRM: N

*Move first*
[The single highest-leverage lead based on score + days stale — name, why, one action]
```

Send with `./notify`.
Log to `memory/logs/${today}.md` under `### stale-lead-report`.

## Sandbox note

GitHub Actions may block outbound curl. Use WebFetch as fallback for all HTTP calls. The AEON_API_KEY secret is available as `$AEON_API_KEY` in the environment.
