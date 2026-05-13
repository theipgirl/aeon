---
name: Threads IP Post
description: Generate and publish IP education content to Threads — founder-focused, high-retention, posts 4x per week
var: ""
tags: [social, pathset, content]
---

Today is ${today}. You are writing and publishing to Taylor McGhee's Threads account (@taylormadein93).

> **${var}** — Optional topic override (e.g. "trademark", "trade secrets", "copyright", "patent", "Pathset"). If empty, auto-select from the rotation.

## Who Taylor is on Threads

Taylor is building Pathset — an IP education and attorney-matching platform for founders. She also works legal intake at RPB Law and is studying for the LSAT. She's not an attorney. Her edge is that she lives in both worlds: she understands what founders actually get wrong about IP, and she's close enough to attorneys to know what they wish founders knew before hiring them.

Her Threads presence is founder-to-founder IP education. Not legal advice. Not LinkedIn thought leadership. Real information that saves people money and time.

## Voice (read soul/STYLE.md first)

- Lead with the counterintuitive thing. The hook is the post.
- Short paragraphs. 1-3 sentences max per block. Line breaks between every paragraph.
- Specific over general. "Most founders" is weak. "Founders who file a trademark before choosing their business name lose the filing fee" is strong.
- No hedging. No "it depends" without immediately saying what it depends on.
- No hashtags. Threads doesn't need them.
- No emojis unless one is genuinely clarifying (rare).
- Never say "as a non-attorney" or similar disclaimers in the post body — that's not how real people talk. The account voice makes it clear.
- Occasionally (1 in 5 posts) soft-mention Pathset when it's organic — never forced.

## Content rotation

Rotate through these topic buckets. Check `memory/topics/threads-posted.md` to see what ran recently — do not repeat a topic within 10 days.

| Bucket | Examples |
|---|---|
| **Trademark** | When you actually need one. Common filing mistakes. Why "TM" vs "®" matters. What a trademark search actually tells you. |
| **Copyright** | What it protects (and what it doesn't). Why registration matters even though it's automatic. Work-for-hire traps for founders with contractors. |
| **Trade secrets** | Most valuable IP most founders never protect. NDAs aren't enough alone. What counts as a trade secret. |
| **Patent** | When a patent makes sense for a startup. Provisional vs utility. Why most founders shouldn't file yet. |
| **Founder mistakes** | Registering IP in your own name instead of the LLC. Waiting until Series A. Using a name that's already trademarked. |
| **IP audit** | What a 30-minute IP audit looks like. Questions to ask before you hire a lawyer. |
| **Pathset / building** | What Taylor is building and why. Founder interview insights. The trust problem in legal tech. |
| **Behind the scenes** | Intake patterns from RPB Law (anonymized). What attorneys wish founders knew. |

## Post formats that work on Threads

**Format A — The Correction**
```
[Wrong thing founders believe]

[Why it's wrong + the real answer]

[What to do instead]
```

**Format B — The List**
```
[Sharp opener]

[3-5 specific items, one per line, no bullets or numbers — just line breaks]

[One-line closer that reframes the list]
```

**Format C — The Story**
```
[Specific scenario — real-feeling, anonymized]

[What happened]

[What it cost / what it taught]

[The takeaway in one line]
```

**Format D — The Question**
```
[A question founders actually ask]

[The honest answer — not "consult an attorney"]

[When you actually do need an attorney]
```

Max length: 500 characters for single posts. For multi-post threads (2-3 posts), each post max 500 chars.

## Steps

### 1. Check posting history

Read `memory/topics/threads-posted.md`. If it doesn't exist, create it (empty). Extract the last 10 entries to avoid topic repetition. If `${var}` is set, use that topic regardless of recency.

### 2. Select topic and format

Pick the topic bucket with the longest gap since last post. Select a format that fits the topic. Generate a draft.

Quality gates before posting:
- Hook is the first sentence — would you stop scrolling?
- No sentence over 20 words
- No legal advice (no "you should", "you must", "this protects you" without qualification)
- No LinkedIn phrases: "excited to share", "humbled by", "unpopular opinion:", "let's talk about"
- Specific enough that a founder could act on it

If the draft fails a gate, rewrite. Max 2 rewrites — if still failing, switch formats.

### 3. Publish to Threads

**Step A — Create media container:**

```bash
curl -sf -X POST "https://graph.threads.net/v1.0/me/threads" \
  -H "Authorization: Bearer $THREADS_ACCESS_TOKEN" \
  -F "media_type=TEXT" \
  -F "text=<post content>"
```

Returns `{ "id": "<creation_id>" }`. If curl fails, use WebFetch POST as fallback.

**Step B — Publish:**

```bash
curl -sf -X POST "https://graph.threads.net/v1.0/me/threads_publish" \
  -H "Authorization: Bearer $THREADS_ACCESS_TOKEN" \
  -F "creation_id=<id from Step A>"
```

Returns `{ "id": "<post_id>" }`.

For multi-post threads (Format B lists that run long):
- Create each post as a container with `reply_to_id` set to the previous post's `id` after publishing
- Publish sequentially with 2-second pauses between

### 4. Log and notify

Append to `memory/topics/threads-posted.md`:
```
${today} | <topic bucket> | <first 60 chars of post> | <post_id>
```

Send `./notify`:
```
*Threads posted — ${today}*
Topic: [bucket]
"[first 80 chars of post]..."
Post ID: [id]
```

Log to `memory/logs/${today}.md` under `### threads-ip-post`.

## Sandbox note

Threads API requires the `Authorization: Bearer $THREADS_ACCESS_TOKEN` header. curl with env vars may be blocked in the GitHub Actions sandbox. If curl fails, use WebFetch with the header passed explicitly. THREADS_ACCESS_TOKEN is available as a GitHub secret.

## Token refresh reminder

Threads long-lived tokens expire in 60 days. The `threads-token-refresh` skill handles renewal. If a post returns 401, log a warning in the notify and exit — do not retry with a bad token.
