*5 Actions — 2026-05-13*
Shape: Make Pathset visible — deploy, recruit, scaffold the funnel; protect LSAT compounding.

1. Deploy the Pathset landing page with `vercel --prod` and verify the public URL serves the founder-side IP wedge copy.
why: 0 attorney signs and a frozen $50 funnel both unblock the moment the URL is live — single load-bearing artifact.
done: Public Vercel URL returns 200 with landing copy; URL committed to memory/topics/pathset.md under Status.
loop: deploy-pathset-landing

2. Email 3 named Florida Bar IP attorneys today with the Pathset partner pitch — pull names from RPB's referral list or a Florida Bar IP filter.
why: 0 of 3 partners signed, Q2 closes in 7 weeks — attorney supply is the binding constraint on the funnel.
done: 3 outbound emails sent; recipient names + dates appended to memory/topics/pathset.md.
loop: sign-attorneys

3. Do one 35-min RC section + one 35-min LR section from the latest PrepTest, score them, and append a 5-bullet error pattern to memory/topics/work.md.
why: June exam is ~5 weeks out; daily LR/RC compounding is the named protocol from 154 → 170.
done: Both sections scored; dated heading with 5-bullet error pattern in memory/topics/work.md.
loop: lsat-rc-lr

4. Create the Stripe payment link for the $50 IP Clarity Session and a 30-min Cal.com booking page, then commit both URLs to the Pathset repo on a clarity-session feature branch with PR opened.
why: Funnel primitives don't depend on landing being live — parallelize so launch day is one-click.
done: Stripe link + Cal.com URL committed to Pathset repo; PR open against main.
loop: build-50-funnel

5. Inspect the latest GitHub Actions run for hacker-news-digest, identify the cause from logs, and either fix it on a branch or file memory/issues/ISS-001.md with the error trace and severity.
why: 3 cron skills failed this morning; HN digest is the news input for morning-brief — fix once, daily flow recovers.
done: PR opened against the skill, or memory/issues/ISS-001.md exists with full frontmatter (id, severity, root_cause).
loop: fix-hacker-news-digest

sources: memory=46 logs=1 topics=4 prs=0 cron_failing=3 mode=OK
