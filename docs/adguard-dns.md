# AdGuard DNS Setup

## Default filters (enable first)

1. Open AdGuard DNS dashboard > DNS servers > your profile > Blocklists.
2. Enable **OISD Full** and **AdGuard DNS filter**.

## Custom blocklist

DNS servers > your profile > Blocklists > Add blocklist > Custom > paste URL:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt
```

## Custom allowlist

DNS servers > your profile > Allowlist > Add:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/custom/allowlist/global.txt
```

## Notes

- Adblock syntax (`||domain^`) is supported natively by AdGuard DNS.
- Both OISD and AdGuard DNS filter must be enabled for full coverage.
