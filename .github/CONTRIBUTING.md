# Contributing

## Adding a domain

1. Verify it is **not already blocked** by OISD Full or AdGuard DNS Filter.
2. Add to the appropriate file under `custom/blocklist/`:
   - `paywall.txt` — paywall SDKs / metered-access engines
   - `analytics.txt` — analytics, crash reporters, telemetry
   - `microsoft.txt` — Microsoft/Xbox endpoints
   - `mobile.txt` — mobile-specific trackers
   - `social.txt` — social trackers, consent banners
   - `ads.txt` — ad loaders, bid SDKs
   - `misc.txt` — everything else
3. Use adblock syntax: `||domain^`
4. Run the build script: `python scripts/build.py`
5. Commit both the source change and the updated `output/` files.

## Adding to the allowlist

Add to `custom/allowlist/global.txt` with adblock allowlist syntax: `@@||domain^`

## Format rules

- Source files: adblock syntax (`||domain^`), one domain per line, `!` for comments.
- No duplicate domains across files (build script deduplicates; validate CI enforces it).
- Keep `output/` in sync — always run `scripts/build.py` before committing.
