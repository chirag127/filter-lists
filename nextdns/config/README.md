# NextDNS Sanitized Profile Exports

Six NextDNS profile exports, sanitized for public sharing.

**Scrubbed:** profile IDs (filenames), device names in `settings.name`, specific CDN fingerprints.
**Kept:** blocklist selections, custom allow/deny domain rules, security/privacy/parental-control settings.

| File | Context | Key blocklists |
|---|---|---|
| config-1.json | General browser + social blocking | adguard-dns-filter, oisd |
| config-2.json | PC/desktop telemetry focus | adguard-dns-filter, nextdns-recommended, oisd |
| config-3.json | Android/Xiaomi device | adguard-dns-filter, oisd, nextdns-recommended |
| config-4.json | Edge browser profile | adguard-dns-filter |
| config-5.json | Exam/focus mode | adguard-dns-filter |
| config-6.json | Router-wide baseline | nextdns-recommended, oisd, adguard-dns-filter |

Import via NextDNS dashboard → Settings → Import configuration.
