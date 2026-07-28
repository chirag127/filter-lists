# NextDNS (xDNS) Setup

## Default lists (enable first — cover ~99% of blocking)

1. **OISD Full** — Settings > Security > Blocklists > Add > search "OISD" > select Full
2. **AdGuard DNS Filter** — Settings > Security > Blocklists > Add > search "AdGuard DNS filter"

## Custom blocklist (only what OISD/AdGuard miss)

Settings > Security > Blocklists > Add > Custom > paste URL:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/output/domains.txt
```

## Custom allowlist

Settings > Allowlist > Add each domain from:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/custom/allowlist/global.txt
```

## Notes

- Plain-domains format is the correct choice for NextDNS custom URLs.
- Wildcards are implied (blocking `example.com` also blocks `sub.example.com`).
