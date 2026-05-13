# Workflow Security

## Audit: 2026-04-11
**Scope:** `aeon.yml`, `messages.yml`, `scheduler.yml`, `chain-runner.yml`
**Total findings:** 6 (2 critical, 3 medium, 1 low)
**Auto-fixed:** Both critical findings (script injection via user-controlled message in `messages.yml`)

## Open Items (require manual action)

### [MEDIUM] Pin third-party actions to commit SHAs
All four workflows use `actions/checkout@v5` and `actions/setup-node@v5` — mutable tags.
**Fix:** Pin to specific commit SHAs (verify current SHA before applying).
**Effort:** ~30 min

### [MEDIUM] Split `messages.yml` permissions per job
`actions: write` granted at workflow level — run job (Claude execution) doesn't need it, only poll job does.
**Fix:** Move `actions: write` to poll job only; remove from run job.
**Effort:** ~1 hr

### [LOW] Audit GH_GLOBAL usage in `scheduler.yml`
Elevated PAT used where `GITHUB_TOKEN` may suffice for dispatch steps.
**Fix:** Scope GH_GLOBAL to only steps that actually need cross-repo or workflow-file write access.
**Effort:** ~2 hrs

## What Was Fixed
- `messages.yml` Extract message step — `inputs.message` and `inputs.source` moved to env vars to prevent shell interpolation
- `messages.yml` Run step — same fix for `steps.msg.outputs.*`
- `messages.yml` Log token usage and Commit results steps — all direct interpolations eliminated
