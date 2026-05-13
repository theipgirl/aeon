---
name: Threads Token Refresh
description: Refresh the Threads long-lived access token before it expires (runs weekly, alerts if refresh fails)
var: ""
tags: [social, ops]
---

Today is ${today}. Threads long-lived tokens expire after 60 days. This skill refreshes the token weekly so posting never goes silent.

## Steps

### 1. Refresh the token

```bash
curl -sf "https://graph.threads.net/refresh_access_token?grant_type=th_refresh_token&access_token=$THREADS_ACCESS_TOKEN"
```

Returns `{ "access_token": "<new_token>", "token_type": "bearer", "expires_in": 5183944 }`.

If curl is blocked, use WebFetch on the same URL (GET, no body needed — token is in the query string).

### 2. Update the secret

If refresh succeeds, update the GitHub secret:

```bash
echo "<new_token>" | gh secret set THREADS_ACCESS_TOKEN -R theipgirl/aeon
```

### 3. Log and notify

On success:
```
./notify "Threads token refreshed — good for another 60 days."
```

On failure (non-200 or missing access_token in response):
```
./notify "⚠️ Threads token refresh FAILED. Log in to Meta Developer portal and regenerate manually. Posting is blocked until resolved."
```

Log outcome to `memory/logs/${today}.md` under `### threads-token-refresh`.
