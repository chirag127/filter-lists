# AdGuard Browser Extension Setup

## Default filter lists (enable first)

AdGuard popup > Settings icon > Filters:

- Enable **AdGuard Base filter** (includes AdGuard DNS filter entries)
- Enable **AdGuard Tracking Protection filter**

## Custom filter subscription

AdGuard popup > Settings > Filters > Custom > Add custom filter > paste URL:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt
```

## User rules (allowlist)

AdGuard popup > Settings > User rules > add lines from:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/custom/allowlist/global.txt
```

## Notes

- Adblock syntax is fully supported by the AdGuard extension.
- Custom filters auto-update based on the `Expires: 1 day` header.
