# AdGuard Home Setup

## Default upstream lists

Filters > DNS blocklists > Add blocklist > choose from list:

- **OISD Full**: `https://big.oisd.nl`
- **AdGuard DNS filter**: `https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt`

## Custom blocklist

Filters > DNS blocklists > Add blocklist > Add a custom list:

- Name: `chirag127 custom`
- URL:
  ```
  https://raw.githubusercontent.com/chirag127/filter-lists/main/output/adblock.txt
  ```

## Custom allowlist

Filters > DNS allowlists > Add allowlist:

```
https://raw.githubusercontent.com/chirag127/filter-lists/main/custom/allowlist/global.txt
```

## Notes

- AdGuard Home supports both adblock syntax and hosts format.
- Allowlist entries override blocklist entries.
