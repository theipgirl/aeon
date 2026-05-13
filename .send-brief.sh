#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
read -r -d '' BRIEF <<'BRIEF_EOF' || true
*Morning Brief — 2026-05-13*

*Focus today*
1. Push Pathset landing to Vercel — every day without a live URL kills attorney pitches
2. Send 3 Florida Bar attorney candidates the pitch — Q2 closes in 7 weeks, no supply yet
3. LSAT RC + LR, 90 min — June exam ~5 weeks, compounding is daily

*Since yesterday*
- morning-brief: recovered (4 fails → 0). hacker-news-digest, goal-tracker, heartbeat still failing once each this morning — watch for skill-repair trigger.
- No PRs open, no new operator commits since e4526e6.
- Two prior briefs already sent at 11:08 and 11:14 UTC — this is the third for today.

*Watch*
- USPTO launched Class ACT — trademark classification 5 months to 5 minutes. Implication for focus #1: Pathset's wedge sharpens to attorney clarity, not paperwork. Tighten the landing copy before deploy.

*Running today*
- hacker-news-digest @ 12:00 UTC
- heartbeat @ 14:00, 20:00 UTC
- idea-capture @ 14:00 UTC
- reg-monitor @ 14:00 UTC (Wed)
- goal-tracker, skill-health @ 18:00 UTC
- skill-analytics @ 18:30 UTC (Wed)
- action-converter @ 20:00 UTC
BRIEF_EOF
./notify "$BRIEF"
