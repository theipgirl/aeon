# Omi Memory Sync

Fetch all memories from the Omi API and update `soul/data/omi-memories.md`. This keeps Aeon's soul grounded in Taylor's real-world context — what she's working on, thinking about, and doing day-to-day.

## Steps

1. Read the current `soul/data/omi-memories.md` to get the existing count and last sync date from the header line.

2. Fetch ALL memories from the Omi API using pagination (100 per page until empty):
   ```
   GET https://api.omi.me/v1/mcp/memories?limit=100&offset=0
   Authorization: Bearer $OMI_API_KEY
   ```
   Keep incrementing `offset` by 100 until a page returns fewer than 100 results.

   **Sandbox note:** If curl fails due to network restrictions, use WebFetch as fallback for each page URL with the Authorization header.

3. Compare new total count to existing count from the file header. If unchanged, log `OMI_SYNC_OK — no new memories` and exit without committing.

4. If memories changed, write the updated `soul/data/omi-memories.md` with this structure:
   ```markdown
   # Omi Memories
   *Synced: YYYY-MM-DD — N total memories*

   Source material for Aeon's soul. Browse for grounding, patterns, and recurring themes.
   Do not copy-paste directly — absorb the context.

   ## Manual (N)

   - memory content
   - memory content
   ...

   ## System (N)

   - memory content
   ...

   ## Interesting (N)

   - memory content
   ...
   ```
   Group by `category` field. Sort categories alphabetically. Each memory is one bullet line.

5. Commit the file:
   ```
   git add soul/data/omi-memories.md
   git commit -m "omi-sync: update memories (N total)"
   git push
   ```

6. Notify: `./notify "Omi sync complete — N memories (+X new)"`

## Exit conditions

- **No change:** Log `OMI_SYNC_OK` silently, no commit, no notify.
- **API error:** Log the error, notify `"Omi sync failed — check OMI_API_KEY secret"`, exit 1.
- **Missing secret:** If `OMI_API_KEY` is not set, notify and exit 1.

## Sandbox note

The Omi API requires HTTPS with a Bearer token. Use curl with `-k` flag if SSL verification fails:
```bash
curl -sk "https://api.omi.me/v1/mcp/memories?limit=100&offset=0" \
  -H "Authorization: Bearer $OMI_API_KEY"
```
If curl is fully blocked, use WebFetch for each page URL.
