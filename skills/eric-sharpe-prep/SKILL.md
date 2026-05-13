---
name: Eric Sharpe Meeting Prep
description: 24-hour prep brief for Taylor's weekly 1:1 with Eric Sharpe — what you said you'd do, what actually happened, 3 agenda items
var: ""
tags: [pathset, mentor]
---

Today is ${today}. You are preparing Taylor McGhee for her weekly 1:1 with Eric Sharpe, her business mentor.

## Eric Sharpe context

Eric is a straight-talking business mentor who meets with Taylor weekly. He gives her real comp math, pushes back on assumptions, and holds her accountable to specifics. He told her: think of time as having a dollar value, don't break even, aim for 2x return on time. He does not want vague updates — he wants numbers, decisions, and honest reporting on what stalled.

His last known guidance (from memory):
- Move from commission to flat-fee pay-per-lead as volume grows ($390/lead target)
- Find out WHY the two converted clients converted (offer $25 gift card for 15-min debrief)
- Ask the patent attorney: what does he pay for leads, what's his close rate
- Focus on local entrepreneurs first — trust is the wedge
- Don't over-automate early

## Steps

### 1. Pull what happened since last meeting

Read `memory/logs/` — last 7 days. Extract:
- Pathset activity: interviews done, clients contacted, revenue moved
- RPB Law: leads processed, consultations booked, anything notable
- Commitments Taylor made in previous Eric sessions (search logs for "eric" or "sharpe" or "committed" or "promised")
- Anything that stalled and why

Read `memory/topics/pathset.md` if it exists.

Check `memory/MEMORY.md` for any flagged action items or goals.

### 2. Score the week honestly

For each commitment from last week, mark it:
- **Done** — completed, evidence of completion
- **Partial** — started but not finished, specific blocker
- **Not done** — didn't happen, honest reason why

Eric will ask about these. Don't soften them.

### 3. Build 3 agenda items

Select the 3 things most worth raising with Eric, ranked by:
1. **Decision needed** — something you can't move forward on without his input
2. **Accountability update** — a commitment you need to report on honestly
3. **New information** — something that changes the picture (new data, a conversion, a setback, a market signal)

For each item, prepare:
- The situation in 2 sentences max
- The specific question or update you're bringing
- What you're hoping to get from him (a decision, a framework, a reality check)

### 4. Flag the number

Eric always asks about money. Prepare:
- Pathset revenue this month (or pipeline value if pre-revenue)
- RPB comp this month (leads × $50 + signed × $100, or updated rate if changed)
- Gap to $20K/month goal
- One specific lever to close the gap

### 5. Format and send

```
*Eric Sharpe Prep — ${today}*

*Last week's commitments*
✓ [Done item]
~ [Partial item] — blocked by: [specific reason]
✗ [Not done] — reason: [honest reason]

*Agenda (bring these 3)*
1. [Item] — asking: [specific question]
2. [Item] — update: [honest status]
3. [Item] — input needed on: [decision]

*The number*
- RPB this month: $[X]
- Pathset pipeline: $[X]
- Gap to $20K: $[X]
- Lever: [one specific thing to move the number]

*Don't forget*
[Any logistical note — time, location, anything to bring]
```

Send with `./notify` 24 hours before the scheduled meeting.

Log to `memory/logs/${today}.md` under `### eric-sharpe-prep`.

## Timing

This skill should run the day before Taylor's weekly Eric Sharpe session. If the meeting day is Tuesday, schedule for Monday. Adjust `aeon.yml` cron accordingly once the meeting cadence is confirmed.

## Bootstrap note

If memory logs are sparse (cold start), send what's available and flag:
`Note: Limited log history — add memory/topics/pathset.md with current Pathset status for richer prep next week.`
