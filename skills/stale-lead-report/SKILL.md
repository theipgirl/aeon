---
name: Stale Lead Report
description: Weekly RPB Law intake audit — surfaces leads that haven't moved in 7+ days with a suggested follow-up action for each
var: ""
tags: [rpb, intake]
---

Today is ${today}. You are reviewing the RPB Law intake pipeline for Taylor McGhee.

## Context

Taylor is Client Intake Associate at RPB Law. She manages the Lawmatics CRM pipeline. A "stale lead" is any prospect who had a discovery call or submitted an intake form but hasn't moved to the next stage in 7+ days. These are the leads most likely to go cold — and the easiest to recover with a single touchpoint.

## Steps

### 1. Load lead data

Check for a lead export file in these locations (in order):
- `data/rpb-leads.csv` — manual export from Lawmatics
- `data/rpb-leads.json`
- `memory/topics/rpb-leads.md`

If none exist, read `memory/topics/rpb-law.md` for any manually logged leads.

If no data source exists, skip to the **Bootstrap mode** section below.

### 2. Identify stale leads

A lead is stale if:
- Last activity date is 7+ days ago
- Current stage is NOT "Signed Matter" or "Closed Lost"
- No follow-up task is marked complete in the last 7 days

For each stale lead, extract:
- Name
- Stage (e.g. Discovery Call Completed, Proposal Sent, Awaiting Decision)
- Days since last activity
- Last known touchpoint (call, email, form submission)

Sort by: days stale descending (longest first).

### 3. Draft a follow-up line for each

For each stale lead, write one specific follow-up message in Rebecca's firm voice — warm, professional, not pushy. Tailor the message to their stage:

- **Discovery call completed, no proposal yet** → "Following up on our conversation — I have a few options ready for you based on what you shared. When's a good time this week?"
- **Proposal sent, no response** → "Checking in on the proposal I sent — happy to answer any questions or walk through it together."
- **Awaiting decision** → "Just wanted to make sure you had everything you needed to move forward. Any questions on our end?"

Keep each message under 3 sentences. No legal advice. No pressure.

### 4. Format and send

```
*RPB Stale Lead Report — ${today}*

*Needs follow-up (${N} leads)*

1. [Name] — [Stage] — [X] days stale
   → [follow-up message]

2. [Name] — [Stage] — [X] days stale
   → [follow-up message]

*Pipeline health*
- Total active leads: [N]
- Stale (7d+): [N]
- Longest stale: [X] days ([Name])

*Next action*
[One specific thing Taylor should do today to move the highest-leverage lead forward]
```

Send with `./notify`.

Log to `memory/logs/${today}.md` under `### stale-lead-report`.

### Bootstrap mode

If no lead data exists, send:

```
*RPB Stale Lead Report — ${today}*

No lead data found. To activate this report:
1. Export leads from Lawmatics as CSV (Contacts → Export)
2. Save to `data/rpb-leads.csv` in the aeon repo
3. Or log active leads manually in `memory/topics/rpb-law.md`

Once data is present, this skill runs automatically every Monday.
```

## Sandbox note

No external API calls needed. Reads local files only. If Lawmatics API access is added later (OAuth token via secret `LAWMATICS_TOKEN`), this skill can be extended to fetch live pipeline data via `curl` with WebFetch fallback.
