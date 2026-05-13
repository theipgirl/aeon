---
name: Competitor Watch
description: Weekly scan of Pathset competitors — what they shipped, what founders are complaining about, any pricing or positioning changes
var: ""
tags: [pathset, research]
---

Today is ${today}. You are monitoring the competitive landscape for Pathset — Taylor McGhee's IP education and attorney-matching platform for early-stage founders.

## Pathset context

Pathset sits in the decision layer between a founder and a lawyer. The core value: founders understand what they own before paying attorney fees, then get matched to the right attorney. Florida Bar compliant. Trust is the primary conversion lever.

Primary competitors to monitor:
- **Trademark Engine** — high-volume filing platform, humans on backend (Eric Sharpe noted this explicitly)
- **LegalZoom** — mass market, brand-name, perceived as generic
- **Clio** — practice management, not founder-facing but attorney-side
- **Traklight** — IP audit tool for founders, closest to Pathset's education angle
- **Clerky / Stripe Atlas** — incorporation, adjacent but not IP-focused
- **UpCounsel / Lawfully** — attorney matching, different ICP

## Steps

### 1. Scan each competitor

For each competitor, use WebSearch and WebFetch to check:

**Product changes:**
- New features, tools, or services launched in the last 7 days
- Pricing page changes
- Any new "for founders" or IP-specific positioning

**Search queries to run:**
- `"Trademark Engine" new feature OR update OR pricing 2026`
- `"LegalZoom" founders IP trademark 2026`
- `"Traklight" update OR launch 2026`
- `site:reddit.com "Trademark Engine" OR "LegalZoom" trademark founders complaint`
- `"attorney matching" startup founders 2026`

**Review signals:**
- Search `"Trademark Engine" OR "LegalZoom" reviews complaint 2026` on Reddit, G2, Trustpilot
- Note recurring founder pain points — these are Pathset's positioning opportunities

**Funding / partnerships:**
- Any announced rounds, law firm partnerships, or accelerator deals

### 2. Score each finding

Only include a finding if it meets at least one bar:
- **Threat** — they're moving into Pathset's exact lane
- **Opportunity** — a gap or complaint Pathset can exploit
- **Signal** — a market shift that changes Pathset's positioning or timing

Drop anything that's just noise (routine blog posts, generic marketing).

### 3. Format and send

```
*Competitor Watch — ${today}*

*Threats*
- [Competitor]: [what they did] — implication: [one sentence]

*Opportunities* (gaps and complaints)
- [Competitor]: [founder pain point from reviews] — Pathset angle: [one sentence]

*Signals*
- [finding] — why it matters for Pathset

*No change*
- [Competitor] — nothing material this week

*One thing to act on*
[The single most actionable finding — specific, not vague]
```

If nothing material happened across all competitors, send:
```
*Competitor Watch — ${today}*
No material changes this week. Landscape is stable.
```

Send with `./notify`.
Log to `memory/logs/${today}.md` under `### competitor-watch`.
Update `memory/topics/pathset.md` with any new competitive intelligence (append, don't overwrite).

## Sandbox note

Use WebSearch and WebFetch for all external lookups. curl may be blocked — WebFetch is the reliable fallback.
